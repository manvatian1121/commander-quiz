# -*- coding: utf-8 -*-
"""打印 bank3 全文与轴得分，供人工复核。"""
import json
import sys
from pathlib import Path



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

qs = json.loads(Path(ROOT / "data" / "bank3.json").read_text(encoding="utf-8"))["questions"]
for q in qs:
    kind = f" [{q.get('kind')}]" if q.get("kind") else ""
    print(f"### {q['id']}{kind}  next={q.get('next')}")
    print(f"Q: {q['q']}")
    for i, o in enumerate(q["opts"]):
        s = " ".join(f"{a}:{v}" for a, v in o["s"].items())
        g = f"  goto={o['goto']}" if "goto" in o else ""
        print(f"   {chr(65+i)}. {o['t']}    <{s}>{g}")
    print()
