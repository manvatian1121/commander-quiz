#!/usr/bin/env python3
"""确认 EDHREC 单主将页中「该主将自身」的套牌数字段位置。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")


def hits(node, path="", found=None):
    if found is None:
        found = []
    if isinstance(node, dict):
        for key, value in node.items():
            hits(value, f"{path}.{key}", found)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            hits(item, f"{path}[{index}]", found)
    else:
        if path.endswith("num_decks"):
            found.append((path, node))
    return found


payload = json.loads((DATA / "supp_brago-king-eternal.json").read_text(encoding="utf-8"))
all_hits = hits(payload)
print(f"num_decks 字段共 {len(all_hits)} 处，前 25 处路径：")
for path, value in all_hits[:25]:
    print(f"  {value:>8}  {path}")
