#!/usr/bin/env python3
"""生成要补进池子的主将名单（遗漏且套牌数 ≥ 门槛）。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
THRESHOLD = int(sys.argv[1]) if len(sys.argv) > 1 else 5000

missing = json.loads((DATA / "missing_commanders.json").read_text(encoding="utf-8"))
picks = [m["name"] for m in sorted(missing, key=lambda m: -m["num_decks"])
         if m["num_decks"] >= THRESHOLD]

(DATA / "new_pool_members.json").write_text(
    json.dumps(picks, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"套牌数 ≥ {THRESHOLD} 的遗漏主将：{len(picks)} 位，已写出 new_pool_members.json")
print(f"\n前 25 位：")
for name in picks[:25]:
    print(f"  {name}")
print(f"\n末 5 位：")
for name in picks[-5:]:
    print(f"  {name}")
