#!/usr/bin/env python3
"""边界修正：把各 batch 之间断掉的主线链接接回去。

各 batch 由不同 agent 独立编写，交界处的 next 容易写成 null；
这里统一修补，并把修了什么打印出来（不做静默修改）。
"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

# 期望的主线链接：若某题的 next 为 null 但后面还有主线题，就补上
BOUNDARIES = [
    ("bank1", "s16", "s17"),
    ("bank2", "s32", "s33"),
    ("bank3", "s48", "s49"),
    ("bank4", "s64", "s65"),
    ("bank5", "s74", None),          # s74 由 merge 脚本接到 c01
]

fixed = []
for bank, qid, expected in BOUNDARIES:
    path = DATA / f"{bank}.json"
    if not path.exists():
        continue
    payload = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for q in payload["questions"]:
        if q["id"] == qid and q.get("next") != expected:
            old = q.get("next")
            if expected is None:
                continue
            q["next"] = expected
            fixed.append(f"{bank}: {qid}.next {old!r} → {expected!r}")
            changed = True
    if changed:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

if fixed:
    print("已修补主线断点：")
    for item in fixed:
        print(f"  - {item}")
else:
    print("主线断点检查：无需修补")
