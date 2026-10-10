#!/usr/bin/env python3
"""按新难度评分列出全部主将，检查分档是否合理。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
rows = sorted(payload["commanders"],
              key=lambda c: (c["complexity"], -(c.get("text_level", 0)
                                                * 0.58 + c.get("pilot_level", 0) * 0.42)))

current = None
for card in rows:
    level = card["complexity"]
    if level != current:
        current = level
        print(f"\n{'=' * 74}\n【{level}/5 档】")
    mark = " ★" if card["en"] == "Wilhelt, the Rotcleaver" else ""
    print(f"  {card['zh']:<18} 牌面{card.get('text_level', 0):<5} "
          f"操作{card.get('pilot_level', 0):<5} {card['en'][:34]:<34}{mark}")
