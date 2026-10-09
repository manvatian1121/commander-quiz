#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""人读版 dump：把 bank1.json 展开成方便通读的文本。"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

BANK = pathlib.Path(ROOT / "data" / "bank1.json")
data = json.loads(BANK.read_text(encoding="utf-8"))

for q in data["questions"]:
    tag = " [枢纽]" if q.get("kind") == "hub" else ""
    print(f"{q['id']}{tag}  {q['q']}")
    print(f"      next={q['next']}   选项 {len(q['opts'])} 个")
    for i, o in enumerate(q["opts"], 1):
        axes = ",".join(f"{k}:{v}" for k, v in o["s"].items())
        go = f"   goto={o['goto']}" if "goto" in o else ""
        print(f"   {i}. {o['t']}")
        print(f"      [{axes}]{go}")
    print()
