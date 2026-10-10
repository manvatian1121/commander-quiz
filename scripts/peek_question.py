#!/usr/bin/env python3
"""查看某一道题。用法：python peek_question.py s15 [bank1]"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
qid = sys.argv[1]
banks = sys.argv[2:] or ["bank1", "bank2", "bank3", "bank4", "bank5", "bankC"]

for bank in banks:
    path = DATA / f"{bank}.json"
    if not path.exists():
        continue
    for q in json.loads(path.read_text(encoding="utf-8"))["questions"]:
        if q["id"] != qid:
            continue
        print(f"{bank} / {qid}  ({q.get('sec')}) next={q.get('next')}")
        print(f"题干：{q['q']}")
        for i, o in enumerate(q["opts"]):
            print(f"  {'ABCDEFG'[i]}. {o['t']!r}")
            print(f"       s={o.get('s')}")
        sys.exit(0)
print(f"没找到 {qid}")
