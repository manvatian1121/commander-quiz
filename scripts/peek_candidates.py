#!/usr/bin/env python3
"""查看候选产出文件的状态与摘要。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

for name, title in (("new_candidates.json", "新主将候选"),
                    ("similar_candidates.json", "相似推荐候选")):
    path = DATA / name
    if not path.exists():
        print(f"{title}：尚未产出\n")
        continue
    rows = json.loads(path.read_text(encoding="utf-8"))
    print(f"{title}：{len(rows)} 位")
    for row in rows[:18]:
        colors = "".join(row.get("color_identity") or []) or "C"
        label = row.get("edhrec_name") or row.get("name")
        print(f"  {row.get('num_decks'):>6} 副  #{str(row.get('rank')):>5}  "
              f"{colors:<6} {label}")
    print()
