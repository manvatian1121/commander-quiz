#!/usr/bin/env python3
"""检查各题库的 next 链是否接得上。"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

by_id: dict[str, dict] = {}
for name in ["bank1", "bank2", "bank3", "bank4", "bank5", "bankC"]:
    path = DATA / f"{name}.json"
    if not path.exists():
        continue
    for q in json.loads(path.read_text(encoding="utf-8"))["questions"]:
        q["__bank"] = name
        by_id[q["id"]] = q

print("== 主线题的 next ==")
for i in range(1, 81):
    qid = f"s{i:02d}"
    node = by_id.get(qid)
    if not node:
        print(f"  {qid}: 不存在")
        continue
    nxt = node.get("next")
    status = ""
    if nxt is None:
        status = "  ← 终点"
    elif nxt not in by_id:
        status = f"  ← ✗ 指向不存在的题"
    print(f"  {qid} ({node['__bank']}) → {nxt}{status}")
