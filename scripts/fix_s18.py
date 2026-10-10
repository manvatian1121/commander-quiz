#!/usr/bin/env python3
"""修正 s18 选项 B 的措辞（原文「全家的时间表」与搬家情境对不上）。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
PATH = DATA / "bank2.json"

OLD = "把全家的时间表排出来，谁哪天干什么都写清楚"
NEW = "先把整套流程排成时间表，谁哪天干什么都写清楚"

payload = json.loads(PATH.read_text(encoding="utf-8"))
hits = 0
for q in payload["questions"]:
    for opt in q["opts"]:
        if opt["t"] == OLD:
            opt["t"] = NEW
            hits += 1
            print(f"  {q['id']}: 「{OLD}」")
            print(f"        → 「{NEW}」")

if not hits:
    print("✗ 没找到目标文本，未做修改")
    raise SystemExit(1)

PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"✓ 修正 {hits} 处")
