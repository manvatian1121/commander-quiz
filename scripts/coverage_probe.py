#!/usr/bin/env python3
"""直接统计已产出的题库文件的轴 / 颜色 / 约束覆盖，不必等全部齐。"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]
COLORS = ["W", "U", "B", "R", "G"]
CVALS = ["complex", "budget", "salt"]

axis_hits: Counter = Counter()
color_hits: Counter = Counter()
cval_hits: Counter = Counter()
per_bank: dict[str, Counter] = {}
total = 0

for name in ["bank1", "bank2", "bank3", "bank4", "bank5", "bankC"]:
    path = DATA / f"{name}.json"
    if not path.exists():
        print(f"{name}: 尚未产出")
        continue
    questions = json.loads(path.read_text(encoding="utf-8"))["questions"]
    total += len(questions)
    local: Counter = Counter()
    for q in questions:
        for opt in q["opts"]:
            for axis in (opt.get("s") or {}):
                axis_hits[axis] += 1
                local[axis] += 1
            for color in (opt.get("col") or {}):
                color_hits[color] += 1
            for key in (opt.get("cval") or {}):
                cval_hits[key] += 1
    per_bank[name] = local
    print(f"{name}: {len(questions)} 题")

print(f"\n合计 {total} 题\n")
print("各轴被多少选项引用（目标 ≥12）：")
for axis in AXES:
    count = axis_hits.get(axis, 0)
    flag = " " if count >= 12 else "✗"
    print(f"  {flag} {axis:<11} {count:>3}  " + " ".join(
        f"{b.replace('bank', 'b')}:{per_bank.get(b, Counter()).get(axis, 0)}"
        for b in ("bank1", "bank2", "bank3", "bank4", "bank5", "bankC")
        if b in per_bank))
print(f"\n颜色：{ {c: color_hits.get(c, 0) for c in COLORS} }")
print(f"约束：{ {k: cval_hits.get(k, 0) for k in CVALS} }")
