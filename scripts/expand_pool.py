#!/usr/bin/env python3
"""把新主将并入现有数据集：档案、牌面、中文名、搭配牌。

幂等：已经存在的条目会跳过，可以反复跑。
输入：data/new_pool_members.json（一个主将英文名数组）
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

GENERIC = {
    "Sol Ring", "Arcane Signet", "Command Tower", "Exotic Orchard", "Reliquary Tower",
    "Swiftfoot Boots", "Lightning Greaves", "Thought Vessel", "Mind Stone",
    "Fellwar Stone", "Rogue's Passage", "Path of Ancestry", "Commander's Sphere",
    "Chromatic Lantern", "Bojuka Bog", "Terramorphic Expanse", "Evolving Wilds",
    "Swords to Plowshares", "Counterspell", "Cultivate", "Kodama's Reach",
    "Rampant Growth", "Beast Within", "Generous Gift", "Chaos Warp",
    "Anguished Unmaking", "Return to Nature", "Nature's Lore", "Three Visits",
    "Farseek", "Sign in Blood", "Night's Whisper", "Read the Bones",
    "Arcane Denial", "Negate", "Disenchant", "Naturalize", "Wrath of God",
}
BASIC_LANDS = {"Island", "Plains", "Swamp", "Mountain", "Forest", "Wastes"}
MIN_DECKS = 400
MIN_PLAYRATE = 0.12
SYNERGY_N, POPULAR_N = 6, 4


def get_json(url: str, headers: dict, tries: int = 3):
    for attempt in range(tries):
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                return json.loads(response.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as error:
            if error.code in (403, 404):
                return None
            time.sleep(1.5 * (attempt + 1))
        except Exception:  # noqa: BLE001
            time.sleep(1.5 * (attempt + 1))
    return None


def edhrec(slug: str):
    return get_json(f"https://json.edhrec.com/pages/commanders/{slug}.json",
                    {"User-Agent": UA, "Accept": "application/json"})


def extract_profile(payload: dict) -> dict:
    card = (payload.get("container") or {}).get("json_dict", {}).get("card") or {}
    return {
        "name": card.get("name"),
        "slug": card.get("slug"),
        "num_decks": card.get("num_decks"),
        "all_time_rank": card.get("rank"),
        "salt": card.get("salt"),
        "color_identity": card.get("color_identity"),
        "cmc": card.get("cmc"),
        "type_line": card.get("type_line"),
        "is_commander": card.get("is_commander"),
        "legal_commander": card.get("legal_commander"),
        "bracket_counts": payload.get("bracket_counts"),
        "tag_counts": payload.get("tag_counts"),
    }


def extract_cards(payload: dict) -> dict:
    jd = (payload.get("container") or {}).get("json_dict") or {}
    card = jd.get("card") or {}
    total = card.get("num_decks") or 1
    by_name: dict[str, dict] = {}
    for group in jd.get("cardlists") or []:
        for view in group.get("cardviews") or []:
            name = view.get("name")
            if not name:
                continue
            record = by_name.setdefault(name, {"name": name, "num_decks": 0})
            record["num_decks"] = max(record["num_decks"], view.get("num_decks") or 0)
            if view.get("synergy") is not None:
                record["synergy"] = view["synergy"]
    for record in by_name.values():
        record["playrate"] = round(record["num_decks"] / total, 4) if total else 0.0
    synergy = [r for r in by_name.values()
               if r.get("synergy") is not None and r["num_decks"] >= MIN_DECKS
               and r["name"] not in GENERIC and r["name"] not in BASIC_LANDS]
    synergy.sort(key=lambda r: -r["synergy"])
    popular = [r for r in by_name.values()
               if r["playrate"] >= MIN_PLAYRATE and r["name"] not in GENERIC
               and r["name"] not in BASIC_LANDS]
    popular.sort(key=lambda r: -r["num_decks"])
    return {
        "name": card.get("name"),
        "num_decks": total,
        "synergy_top": [{"name": r["name"], "synergy": round(r["synergy"], 3),
                         "num_decks": r["num_decks"], "playrate": r["playrate"]}
                        for r in synergy[:10]],
        "popular_top": [{"name": r["name"], "num_decks": r["num_decks"],
                         "playrate": r["playrate"]} for r in popular[:10]],
    }


def scryfall_card(name: str):
    for endpoint in (f"/cards/named?exact={urllib.parse.quote(name)}",
                     f"/cards/named?fuzzy={urllib.parse.quote(name)}"):
        card = get_json("https://api.scryfall.com" + endpoint,
                        {"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"})
        if card and card.get("name"):
            faces = card.get("card_faces") or []
            return {
                "name": card["name"],
                "mana_cost": card.get("mana_cost") or " // ".join(
                    f.get("mana_cost", "") for f in faces),
                "cmc": card.get("cmc"),
                "type_line": card.get("type_line"),
                "oracle_text": card.get("oracle_text") or "\n//\n".join(
                    f.get("oracle_text", "") for f in faces),
                "color_identity": card.get("color_identity"),
                "keywords": card.get("keywords"),
                "set": card.get("set"),
                "set_name": card.get("set_name"),
                "released_at": card.get("released_at"),
                "edhrec_rank": card.get("edhrec_rank"),
                "usd": (card.get("prices") or {}).get("usd"),
                "commander_legal": (card.get("legalities") or {}).get("commander"),
                "is_legendary_creature": "Legendary Creature" in (card.get("type_line") or ""),
                "can_be_commander": card.get("can_be_commander"),
            }
    return None


def mtgch_zh(name: str):
    payload = get_json(
        "https://mtgch.com/api/v1/autocomplete/?"
        + urllib.parse.urlencode({"q": name, "view": "name"}),
        {"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"})
    for item in (payload or {}).get("items") or []:
        candidate = item.get("name") or ""
        zh = item.get("display_name") or item.get("translated_name") or ""
        if zh and (candidate == name or candidate.startswith(name + " //")):
            return zh.split(" // ")[0].strip()
    return ""


DIACRITICS = str.maketrans({
    "á": "a", "à": "a", "â": "a", "ä": "a", "ã": "a", "å": "a",
    "é": "e", "è": "e", "ê": "e", "ë": "e",
    "í": "i", "ì": "i", "î": "i", "ï": "i",
    "ó": "o", "ò": "o", "ô": "o", "ö": "o", "õ": "o",
    "ú": "u", "ù": "u", "û": "u", "ü": "u",
    "ñ": "n", "ç": "c", "ß": "ss", "ø": "o", "æ": "ae",
    "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U", "Ñ": "N",
})


def slugify(name: str) -> str:
    """EDHREC 的 slug 规则：小写、重音字母转写成 ASCII、非字母数字转连字符。

    注意「A // B」有歧义：
      - 双面牌（一张牌两个面）的 slug 只用正面，如 Esika -> esika-god-of-the-tree
      - 拍档 / 身世组合（两张牌）的 slug 是两半拼起来，
        如 "Thrasios, Triton Hero // Tymna the Weaver"
           -> thrasios-triton-hero-tymna-the-weaver
    这里按「两半拼起来」推导（组合是我们要找的），双面牌走 existing 里存的
    正确 slug（expand_pool 优先用存档 slug，只有新条目才走这里）。
    """
    base = name.replace(" // ", "-")
    base = base.translate(DIACRITICS)
    base = base.replace("'", "").replace("\u2019", "").replace(",", "")
    base = base.replace(" ", "-").lower()
    base = re.sub(r"[^a-z0-9\-]", "", base)
    return re.sub(r"-+", "-", base).strip("-")


def load(name: str, default):
    path = DATA / name
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def save(name: str, payload) -> None:
    (DATA / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                             encoding="utf-8")


def main() -> int:
    members = load("new_pool_members.json", [])
    if not members:
        print("✗ 缺少 data/new_pool_members.json")
        return 1
    print(f"待并入 {len(members)} 位新主将")

    profiles = load("commander_profiles.json", {})
    scry = load("commanders_scryfall.json", {})
    zh = load("commander_zh.json", {})
    cards = load("commander_cards.json", {})

    added = {"profile": 0, "scryfall": 0, "zh": 0, "cards": 0}
    failed: list[str] = []

    for index, name in enumerate(members, 1):
        existing = profiles.get(name) or {}
        # 优先用已存档的 slug（搭档牌、重音名的推导容易出错）
        slug = existing.get("slug") or slugify(name)
        page = None
        if not existing.get("tag_counts") or name not in cards:
            page = edhrec(slug)
            if page is None and slug != slugify(name):
                page = edhrec(slugify(name))       # 兜底：再用推导值试一次
            time.sleep(0.3)

        if name not in profiles:
            if page is None:
                failed.append(f"{name}（EDHREC 无档案）")
                continue
            profiles[name] = extract_profile(page)
            profiles[name]["edhrec_name"] = name
            added["profile"] += 1
        if name not in cards and page is not None:
            cards[name] = extract_cards(page)
            added["cards"] += 1
        if name not in scry:
            card = scryfall_card(name)
            if card:
                scry[card["name"]] = card
                added["scryfall"] += 1
            time.sleep(0.15)
        if name not in zh:
            got = mtgch_zh(name)
            zh[name] = got
            added["zh"] += 1 if got else 0
            if not got:
                failed.append(f"{name}（无中文名）")
            time.sleep(0.3)

        if index % 20 == 0:
            print(f"  …{index}/{len(members)}  {added}", flush=True)

    save("commander_profiles.json", profiles)
    save("commanders_scryfall.json", scry)
    save("commander_zh.json", zh)
    save("commander_cards.json", cards)

    print(f"\n✓ 新增：档案 {added['profile']} / 牌面 {added['scryfall']} / "
          f"中文名 {added['zh']} / 搭配牌 {added['cards']}")
    if failed:
        print(f"⚠ 需人工复核 {len(failed)} 项：")
        for item in failed[:15]:
            print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
