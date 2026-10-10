#!/usr/bin/env python3
"""把 bank5.json 打印成可读文本，供人工复核。"""
import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
BANK = pathlib.Path(ROOT / "data" / "bank5.json")

data = json.loads(BANK.read_text(encoding="utf-8"))
for q in data["questions"]:
    tag = f"{q['id']} [{q['sec']}]"
    if "multi" in q:
        tag += f" multi={q['multi']}"
    if q.get("kind") == "hub":
        tag += " HUB"
    print(f"{tag}  → next: {q.get('next')}")
    print(f"  Q: {q['q']}")
    for o in q["opts"]:
        g = f"  goto={o['goto']}" if "goto" in o else ""
        print(f"    - {o['t']}")
        print(f"        {o['s']}{g}")
    print()
