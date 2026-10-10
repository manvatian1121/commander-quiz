#!/usr/bin/env python3
"""快速预览某个题库文件。用法：python peek_bank.py 1"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

which = sys.argv[1] if len(sys.argv) > 1 else "1"
path = DATA / f"bank{which}.json"
payload = json.loads(path.read_text(encoding="utf-8"))
questions = payload["questions"]
print(f"# bank{which}.json —— {len(questions)} 题\n")

show = int(sys.argv[2]) if len(sys.argv) > 2 else 6
for q in questions[:show]:
    kind = f" [{q.get('kind')}]" if q.get("kind") else ""
    multi = f" [多选×{q['multi']}]" if q.get("multi") else ""
    print(f"{q['id']}{kind}{multi} ({q.get('sec')}) → next={q.get('next')}")
    print(f"  {q['q']}")
    for i, o in enumerate(q["opts"]):
        goto = f" ⇒{o['goto']}" if o.get("goto") else ""
        cval = f" cval={o['cval']}" if o.get("cval") else ""
        col = f" col={o['col']}" if o.get("col") else ""
        print(f"    {'ABCDE'[i]}. {o['t']}   {o.get('s')}{goto}{cval}{col}")
    print()

ids = [q["id"] for q in questions]
print(f"全部 id：{', '.join(ids)}")
