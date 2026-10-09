#!/usr/bin/env python3
"""检查某位主将在 commander_cards.json 里的条目。"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
name = sys.argv[1] if len(sys.argv) > 1 else "Kraum, Ludevic's Opus // Tymna the Weaver"
cards = json.loads((DATA / "commander_cards.json").read_text(encoding="utf-8"))
print(f"{name!r} 是否在 commander_cards.json：{name in cards}")
print(json.dumps(cards.get(name), ensure_ascii=False)[:600])

print("\n名字相近的键：")
for key in cards:
    if "kraum" in key.lower() or "tymna" in key.lower():
        print(f"  {key!r}  协同榜 {len(cards[key].get('synergy_top') or [])} 条")
