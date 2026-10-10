#!/usr/bin/env python3
"""整理每位主将要展示的搭配牌，并用 Scryfall 核实牌名真实存在。"""
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
SYNERGY_N = 6
POPULAR_N = 4


def post(endpoint: str, payload: dict):
    request = urllib.request.Request(
        "https://api.scryfall.com" + endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"User-Agent": UA, "Accept": "application/json",
                 "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8", "replace"))


def main() -> int:
    payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    cards = json.loads((DATA / "commander_cards.json").read_text(encoding="utf-8"))

    wanted: set[str] = set()
    display: dict[str, dict] = {}
    for card in payload["commanders"]:
        name = card["en"]
        entry = cards.get(name) or {}
        synergy = [c["name"] for c in (entry.get("synergy_top") or [])[:SYNERGY_N]]
        popular_pool = [c["name"] for c in (entry.get("popular_top") or [])]
        popular = [n for n in popular_pool if n not in synergy][:POPULAR_N]
        display[name] = {"synergy": synergy, "popular": popular}
        wanted.update(synergy)
        wanted.update(popular)

    names = sorted(wanted)
    print(f"待核实牌名 {len(names)} 张（{len(display)} 位主将）")

    found: dict[str, dict] = {}
    not_found: list[str] = []
    for start in range(0, len(names), 70):
        batch = names[start:start + 70]
        result = post("/cards/collection", {"identifiers": [{"name": n} for n in batch]})
        for card in result.get("data", []):
            found[card["name"]] = {
                "name": card["name"],
                "mana_cost": card.get("mana_cost") or "",
                "cmc": card.get("cmc"),
                "type_line": card.get("type_line"),
                "oracle_text": (card.get("oracle_text") or "")[:400],
            }
        for miss in result.get("not_found", []):
            not_found.append(miss.get("name", "?"))
        time.sleep(0.25)

    print(f"✓ Scryfall 批量命中 {len(found)} / 未命中 {len(not_found)}")

    # 兜底：分体牌等特殊牌型用精确查询重试，避免静默丢牌
    still_missing: list[str] = []
    for name in not_found:
        url = "https://api.scryfall.com/cards/named?exact=" + urllib.parse.quote(name)
        request = urllib.request.Request(
            url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                card = json.loads(response.read().decode("utf-8", "replace"))
            found[card["name"]] = {
                "name": card["name"],
                "mana_cost": card.get("mana_cost") or "",
                "cmc": card.get("cmc"),
                "type_line": card.get("type_line"),
                "oracle_text": (card.get("oracle_text") or "")[:400],
            }
            print(f"  兜底命中: {name}")
        except urllib.error.HTTPError:
            still_missing.append(name)
        time.sleep(0.2)

    print(f"✓ 最终命中 {len(found)} / 仍未命中 {len(still_missing)}")
    for item in still_missing:
        print(f"  ✗ {item}")

    (DATA / "card_display.json").write_text(
        json.dumps(display, ensure_ascii=False, indent=2), encoding="utf-8")
    (DATA / "card_verified.json").write_text(
        json.dumps(found, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"已写出 card_display.json 与 card_verified.json")
    return 0 if not still_missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
