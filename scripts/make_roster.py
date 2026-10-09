#!/usr/bin/env python3
"""生成显式的主将花名册：现有池 + 新并入的主将。"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
current = [c["en"] for c in pool["commanders"]]
new = json.loads((DATA / "new_pool_members.json").read_text(encoding="utf-8"))

roster = list(current)
for name in new:
    if name not in roster:
        roster.append(name)

(DATA / "pool_roster.json").write_text(
    json.dumps(roster, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"原有 {len(current)} 位 + 新增 {len(new)} 位 → 花名册 {len(roster)} 位")
