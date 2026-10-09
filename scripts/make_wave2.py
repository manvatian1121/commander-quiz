#!/usr/bin/env python3
"""把「相似推荐」爬到的候选并入队伍（第二批）。"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
in_pool = {c["en"] for c in pool["commanders"]}
rows = json.loads((DATA / "similar_candidates.json").read_text(encoding="utf-8"))

members = []
for row in rows:
    name = row.get("edhrec_name") or row.get("name")
    if name and name not in in_pool and name not in members:
        members.append(name)

(DATA / "new_pool_members.json").write_text(
    json.dumps(members, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"第二批 {len(members)} 位：")
for name in members:
    print(f"  {name}")
