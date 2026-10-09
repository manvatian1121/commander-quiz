#!/usr/bin/env python3
"""确认 EDHREC 主将页里「最常搭配的牌」列表的位置与字段。"""
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

print("顶层键:", list(payload.keys()))
print()
for key in ("creature", "instant", "artifact"):
    node = payload.get(key)
    if isinstance(node, dict):
        print(f"[{key}] dict keys = {list(node.keys())}")
        cards = node.get("cards") or node.get("cardviews") or []
        print(f"    条目数 {len(cards)}")
        if cards:
            sample = cards[0]
            print(f"    sample keys = {sorted(sample.keys())}")
            print(f"    sample = {json.dumps(sample, ensure_ascii=False)[:320]}")
    elif isinstance(node, list):
        print(f"[{key}] list len={len(node)} sample={json.dumps(node[0], ensure_ascii=False)[:260]}")
    print()

print("panels 结构:")
panels = payload.get("panels") or {}
print("  panel keys =", list(panels.keys())[:20])
for name, panel in list(panels.items())[:12]:
    if isinstance(panel, dict):
        lists = panel.get("cardlists") or []
        print(f"  [{name}] cardlists={len(lists)}", end="")
        for cl in lists[:6]:
            tag = cl.get("tag") or cl.get("header") or "?"
            views = cl.get("cardviews") or []
            names = [v.get("name") for v in views[:4]]
            print(f"\n      {tag}: {names}", end="")
        print()
