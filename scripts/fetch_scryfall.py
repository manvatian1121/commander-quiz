#!/usr/bin/env python3
"""用 Scryfall collection 接口批量拉取候选主将的权威牌面数据。"""
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
UA = "dsh-mtg-agent/1.0"


def post(endpoint: str, payload: dict):
    request = urllib.request.Request(
        "https://api.scryfall.com" + endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"User-Agent": UA, "Accept": "application/json",
                 "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8", "replace"))


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
    candidates = json.loads((DATA / "edhrec_candidates.json").read_text(encoding="utf-8"))
    names = [c["name"] for c in candidates]
    print(f"待查 {len(names)} 位")

    found: dict[str, dict] = {}
    missing: list[str] = []

    for start in range(0, len(names), 70):
        batch = names[start:start + 70]
        result = post("/cards/collection", {"identifiers": [{"name": n} for n in batch]})
        for card in result.get("data", []):
            found[card["name"]] = slim(card)
        for miss in result.get("not_found", []):
            missing.append(miss.get("name", "?"))
        time.sleep(0.2)

    # 对未命中的做模糊搜索兜底
    still_missing = []
    for name in missing:
        head = name.split(" // ")[0]
        try:
            card = get("/cards/named?fuzzy=" + urllib.parse.quote(head))
            found[card["name"]] = slim(card)
            print(f"  兜底命中: {name} -> {card['name']}")
        except urllib.error.HTTPError:
            still_missing.append(name)
        time.sleep(0.15)

    (DATA / "commanders_scryfall.json").write_text(
        json.dumps(found, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"命中 {len(found)} / 未命中 {len(still_missing)}")
    for name in still_missing:
        print(f"  ✗ {name}")
    return 0


if __name__ == "__main__":
    import urllib.parse
    raise SystemExit(main())
