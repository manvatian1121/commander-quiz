#!/usr/bin/env python3
"""列出 EDHREC 主将页 container.json_dict.cardlists 的各个分区。"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
payload = json.loads((DATA / "supp_brago-king-eternal.json").read_text(encoding="utf-8"))

jd = payload["container"]["json_dict"]
print("json_dict keys:", list(jd.keys()))
lists = jd.get("cardlists") or []
print(f"cardlists 共 {len(lists)} 个\n")

for index, group in enumerate(lists):
    header = group.get("header")
    tag = group.get("tag")
    views = group.get("cardviews") or []
    print(f"[{index}] header={header!r} tag={tag!r} 条目={len(views)}")
    if views:
        print(f"     sample keys: {sorted(views[0].keys())}")
    for view in views[:5]:
        print(f"     - {view.get('name')}  "
              f"(inclusion={view.get('inclusion')} synergy={view.get('synergy')} "
              f"num_decks={view.get('num_decks')} potential={view.get('potential_decks')})")
    print()
