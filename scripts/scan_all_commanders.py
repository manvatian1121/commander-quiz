#!/usr/bin/env python3
"""彻底扫描：把「所有能当主将的牌」都查一遍 EDHREC 真实套牌数，找出池子里漏掉的。

此前的三条发现路径（全时段 Top 100 / 新牌首印 / 相似主将）覆盖不到
鹏洛客主将、载具主将这类非生物主将，所以做一次穷举。
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

MAX_CARDS = int(sys.argv[1]) if len(sys.argv) > 1 else 1600
MIN_DECKS = int(sys.argv[2]) if len(sys.argv) > 2 else 1200

DIACRITICS = str.maketrans({
    "á": "a", "à": "a", "â": "a", "ä": "a", "ã": "a", "å": "a",
    "é": "e", "è": "e", "ê": "e", "ë": "e", "í": "i", "ì": "i", "î": "i",
    "ï": "i", "ó": "o", "ò": "o", "ô": "o", "ö": "o", "õ": "o",
    "ú": "u", "ù": "u", "û": "u", "ü": "u", "ñ": "n", "ç": "c", "ø": "o",
    "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U",
})


def slugify(name: str) -> str:
    base = name.split(" // ")[0].translate(DIACRITICS)
    base = base.replace("'", "").replace("\u2019", "").replace(",", "")
    base = base.replace(" ", "-").lower()
    base = re.sub(r"[^a-z0-9\-]", "", base)
    return re.sub(r"-+", "-", base).strip("-")


def scryfall_all() -> list[dict]:
    url = ("https://api.scryfall.com/cards/search?unique=cards&order=edhrec&q="
           + urllib.parse.quote("is:commander"))
    cards: list[dict] = []
    while url and len(cards) < MAX_CARDS:
        request = urllib.request.Request(
            url, headers={"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                payload = json.loads(response.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as error:
            print(f"  Scryfall HTTP {error.code}")
            break
        for card in payload.get("data", []):
            cards.append({
                "name": card["name"],
                "released_at": card.get("released_at"),
                "set_name": card.get("set_name"),
                "type_line": card.get("type_line"),
                "color_identity": card.get("color_identity"),
                "cmc": card.get("cmc"),
                "usd": (card.get("prices") or {}).get("usd"),
                "edhrec_rank": card.get("edhrec_rank"),
            })
        url = payload.get("next_page") if payload.get("has_more") else None
        print(f"    Scryfall 累计 {len(cards)} …", flush=True)
        time.sleep(0.15)
    return cards[:MAX_CARDS]


def edhrec_profile(slug: str):
    url = f"https://json.edhrec.com/pages/commanders/{slug}.json"
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8", "replace"))
    except Exception:  # noqa: BLE001
        return None
    card = (payload.get("container") or {}).get("json_dict", {}).get("card") or {}
    if not card.get("num_decks"):
        return None
    return {"num_decks": card.get("num_decks"), "rank": card.get("rank"),
            "slug": card.get("slug"), "edhrec_name": card.get("name"),
            "color_identity": card.get("color_identity")}


def main() -> int:
    pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    in_pool = {c["en"] for c in pool["commanders"]}

    print("① 拉取所有能当主将的牌（按 EDHREC 卡牌热度排序）")
    cards = scryfall_all()
    print(f"   共 {len(cards)} 张")

    print("② 逐个查 EDHREC 的真实套牌数")
    hits: list[dict] = []
    for index, card in enumerate(cards, 1):
        profile = edhrec_profile(slugify(card["name"]))
        if profile:
            hits.append({**card, **profile})
        if index % 200 == 0:
            print(f"    …{index}/{len(cards)}  命中 {len(hits)}", flush=True)
        time.sleep(0.26)

    (DATA / "all_commander_profiles.json").write_text(
        json.dumps(hits, ensure_ascii=False, indent=2), encoding="utf-8")

    missing = [h for h in hits
               if h["name"] not in in_pool
               and h["name"].split(" // ")[0] not in in_pool
               and h["num_decks"] >= MIN_DECKS]
    missing.sort(key=lambda h: -h["num_decks"])

    print(f"\n③ 池中已有 {len(in_pool)} 位；查到档案 {len(hits)} 位")
    print(f"④ 不在池中且套牌数 ≥ {MIN_DECKS} 的：{len(missing)} 位")
    for row in missing[:60]:
        type_hint = "非生物" if "Creature" not in (row.get("type_line") or "") else ""
        print(f"   {row['num_decks']:>6} 副  #{str(row['rank']):>4}  "
              f"{row['released_at']}  {row['name'][:42]:<42} {type_hint}")

    (DATA / "missing_commanders.json").write_text(
        json.dumps(missing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n已写出 all_commander_profiles.json 与 missing_commanders.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
