#!/usr/bin/env python3
"""补齐：为 EDHREC 候选之外的补位主将抓 Scryfall 数据并合并。"""
from __future__ import annotations

import json
import pathlib
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
UA = "dsh-mtg-agent/1.0"


def get(endpoint: str):
    request = urllib.request.Request(
        "https://api.scryfall.com" + endpoint,
        headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8", "replace"))


def slim(card: dict) -> dict:
    faces = card.get("card_faces") or []
    return {
        "name": card.get("name"),
        "mana_cost": card.get("mana_cost") or " // ".join(f.get("mana_cost", "") for f in faces),
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


def main() -> int:
    store = DATA / "commanders_scryfall.json"
    cards = json.loads(store.read_text(encoding="utf-8"))
    supplements = json.loads((DATA / "supplement_probe.json").read_text(encoding="utf-8"))

    print(f"现有 {len(cards)} 张；补位名单 {len(supplements)} 位")
    added, skipped, failed = 0, 0, []

    for record in supplements:
        name = record["name"]
        if name in cards or name.split(" // ")[0] in cards:
            skipped += 1
            continue
        try:
            card = get("/cards/named?exact=" + urllib.parse.quote(name))
        except urllib.error.HTTPError:
            try:
                card = get("/cards/named?fuzzy=" + urllib.parse.quote(name))
            except urllib.error.HTTPError as error:
                failed.append(f"{name} ({error.code})")
                continue
        cards[card["name"]] = slim(card)
        added += 1
        print(f"  + {card['name']}  MV{card['cmc']}  ${card['prices'].get('usd')}")
        time.sleep(0.15)

    store.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n新增 {added} / 已存在 {skipped} / 失败 {len(failed)}，现共 {len(cards)} 张")
    for item in failed:
        print(f"  ✗ {item}")

    # 自检：检查所有 oracle_text 为空的条目
    empty = [name for name, card in cards.items() if not (card.get("oracle_text") or "").strip()]
    if empty:
        print(f"\n⚠ oracle_text 为空的条目（{len(empty)}）：")
        for name in empty:
            print(f"  - {name}")
    else:
        print("\n✓ 无空 oracle_text")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
