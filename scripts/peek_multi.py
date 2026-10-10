#!/usr/bin/env python3
"""检查某个题库里的多选题与枢纽题。用法：python peek_multi.py 5"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

for which in (sys.argv[1:] or ["1", "2", "3", "4", "5"]):
    path = DATA / f"bank{which}.json"
    if not path.exists():
        print(f"bank{which}: 尚未产出\n")
        continue
    questions = json.loads(path.read_text(encoding="utf-8"))["questions"]
    multis = [q for q in questions if q.get("multi")]
    hubs = [q for q in questions if q.get("kind") == "hub"]
    print(f"=== bank{which}：{len(questions)} 题，多选 {len(multis)}，枢纽 {len(hubs)} ===")
    for q in hubs:
        print(f"  枢纽 {q['id']} → next={q.get('next')}")
        print(f"    {q['q']}")
        for i, o in enumerate(q["opts"]):
            print(f"      {'ABCDE'[i]}. {o['t'][:44]}  ⇒{o.get('goto')}")
    for q in multis:
        print(f"  多选 {q['id']}（最多 {q['multi']}）→ next={q.get('next')}")
        print(f"    {q['q']}")
        for i, o in enumerate(q["opts"]):
            print(f"      {'ABCDE'[i]}. {o['t'][:48]}  {o.get('s')}")
    print()
