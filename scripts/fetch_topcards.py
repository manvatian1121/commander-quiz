#!/usr/bin/env python3
"""抓取每位主将的真实搭配牌数据（协同度榜 + 出场率榜），来自 EDHREC 主将页。"""
from __future__ import annotations

import json
import pathlib
import sys
import time
import urllib.error
import urllib.request



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# 任何牌组都会放的基础件，不体现主将特色，不作为「灵魂牌」推荐
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
MIN_DECKS = 400        # 协同榜的最低套牌数，滤掉统计噪声
MIN_PLAYRATE = 0.12    # 出场率榜的最低占比


def fetch(slug: str, tries: int = 3):
    url = f"https://json.edhrec.com/pages/commanders/{slug}.json"
    for attempt in range(tries):
        request = urllib.request.Request(
            url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as error:
            if error.code in (403, 404):
                return None
            time.sleep(1.5 * (attempt + 1))
        except Exception:  # noqa: BLE001
            time.sleep(1.5 * (attempt + 1))
    return None


def extract(payload: dict) -> dict:
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

    synergy_pool = [r for r in by_name.values()
                    if r.get("synergy") is not None
                    and r["num_decks"] >= MIN_DECKS
                    and r["name"] not in GENERIC
                    and r["name"] not in BASIC_LANDS]
    synergy_pool.sort(key=lambda r: -r["synergy"])

    popular_pool = [r for r in by_name.values()
                    if r["playrate"] >= MIN_PLAYRATE
                    and r["name"] not in GENERIC
                    and r["name"] not in BASIC_LANDS]
    popular_pool.sort(key=lambda r: -r["num_decks"])

    return {
        "name": card.get("name"),
        "num_decks": total,
        "synergy_top": [
            {"name": r["name"], "synergy": round(r["synergy"], 3),
             "num_decks": r["num_decks"], "playrate": r["playrate"]}
            for r in synergy_pool[:10]],
        "popular_top": [
            {"name": r["name"], "num_decks": r["num_decks"], "playrate": r["playrate"]}
            for r in popular_pool[:10]],
    }


def main() -> int:
    profiles = json.loads((DATA / "commander_profiles.json").read_text(encoding="utf-8"))
    payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    roster = [c["en"] for c in payload["commanders"]]

    results: dict[str, dict] = {}
    failed: list[str] = []
    for index, name in enumerate(roster, 1):
        profile = profiles.get(name)
        if not profile:
            failed.append(f"{name} (无档案)")
            continue
        page = fetch(profile.get("slug"))
        if page is None:
            failed.append(f"{name} ({profile.get('slug')})")
            continue
        results[name] = extract(page)
        if index % 25 == 0:
            print(f"  ...{index}/{len(roster)}")
        time.sleep(0.3)

    (DATA / "commander_cards.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✓ 成功 {len(results)} / 失败 {len(failed)}")
    for item in failed:
        print(f"  ✗ {item}")

    empty_syn = sorted(n for n, d in results.items() if not d["synergy_top"])
    empty_pop = sorted(n for n, d in results.items() if not d["popular_top"])
    print(f"⚠ 协同榜为空 {len(empty_syn)} 位：{empty_syn[:12]}")
    print(f"⚠ 出场榜为空 {len(empty_pop)} 位：{empty_pop[:12]}")

    for probe in ["Krenko, Mob Boss", "Light-Paws, Emperor's Voice", "Brago, King Eternal"]:
        sample = results.get(probe)
        if not sample:
            continue
        print(f"\n抽样 {sample['name']}：")
        print(f"  协同榜: {[c['name'] for c in sample['synergy_top'][:6]]}")
        print(f"  出场榜: {[c['name'] for c in sample['popular_top'][:6]]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
