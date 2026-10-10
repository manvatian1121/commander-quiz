#!/usr/bin/env python3
"""定位 EDHREC 单主将页里「该主将自身」的套牌数。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
TARGET = "Brago, King Eternal"


def walk(node, path="", depth=0):
    if isinstance(node, dict):
        if node.get("name") == TARGET or node.get("sanitized") == "brago-king-eternal":
            keys = sorted(node.keys())
            print(f"\n命中 @ {path}")
            print(f"  keys: {keys}")
            for key in ("name", "num_decks", "rank", "potential_decks", "url", "id"):
                if key in node:
                    print(f"  {key} = {node[key]}")
        for key, value in node.items():
            walk(value, f"{path}.{key}", depth + 1)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            walk(item, f"{path}[{index}]", depth + 1)


payload = json.loads((DATA / "supp_brago-king-eternal.json").read_text(encoding="utf-8"))
print("顶层键:", list(payload.keys()))
walk(payload)
