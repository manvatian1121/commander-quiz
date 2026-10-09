#!/usr/bin/env python3
"""把取不到搭配牌数据的主将移出花名册。

目前只有一位：Kraum + Tymna 搭档组合。EDHREC 对搭档组合用的是另一个 slug，
我们拿到的页面是单卡 Kraum 的 23 副套牌存根页，取不到有意义的搭配牌。
它同时是 cEDH 档（90% 套牌为 Bracket 5），不适合推荐给新人，故直接移除。
"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

DROP = ["Kraum, Ludevic's Opus // Tymna the Weaver"]

roster_path = DATA / "pool_roster.json"
roster = json.loads(roster_path.read_text(encoding="utf-8"))
before = len(roster)
roster = [n for n in roster if n not in DROP]
roster_path.write_text(json.dumps(roster, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"花名册 {before} → {len(roster)} 位")
for name in DROP:
    print(f"  移除：{name}")
