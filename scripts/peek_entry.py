#!/usr/bin/env python3
"""打印指定主将的介绍文全文与字数。用法：python peek_entry.py "Omo" """
from __future__ import annotations

import json
import pathlib
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
needle = sys.argv[1] if len(sys.argv) > 1 else "Omo"

for index in range(1, 9):
    path = DATA / f"descriptions_{index}.json"
    if not path.exists():
        continue
    data = json.loads(path.read_text(encoding="utf-8"))
    for key, entry in data.items():
        if needle.lower() not in key.lower():
            continue
        print(f"[descriptions_{index}] {key}")
        for field in ("tagline", "intro", "build"):
            text = entry.get(field) or ""
            print(f"\n{field}（{len(re.sub(chr(92)+'s', '', text))} 字）：")
            print(text)
