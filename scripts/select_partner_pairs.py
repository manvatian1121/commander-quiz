#!/usr/bin/env python3
"""定稿要补进去的拍档 / 身世组合。

发现的组合有 30 个（≥800 副），但其中身世组合被漏掉了——身世牌是灵气不是主将，
多数没有独立的 EDHREC 页面，所以「按单卡热度筛候选」那一步把它们滤没了。
用直接探针验过的 3 组身世补上。

最终口径：拍档组合取 ≥2000 副，身世组合取 ≥1000 副（身世本来就是更小的类别）。
"""
from __future__ import annotations

import json
import pathlib
import sys


# --- 路径相对本文件解析，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = ROOT / "data"

# 直接探针确认存在的身世组合（单卡热度筛不到，见上面的说明）
BACKGROUND_PAIRS = [
    {"name": "Gale, Waterdeep Prodigy // Scion of Halaster",
     "num_decks": 2915, "rank": 898, "kind": "身世"},
    {"name": "Karlach, Fury of Avernus // Sword Coast Sailor",
     "num_decks": 1363, "rank": 1427, "kind": "身世"},
    {"name": "Shadowheart, Dark Justiciar // Haunted One",
     "num_decks": 1139, "rank": 1578, "kind": "身世"},
]

PARTNER_MIN = 2000
BACKGROUND_MIN = 1000

rows = json.loads((DATA / "partner_candidates.json").read_text(encoding="utf-8"))
pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
in_pool = {c["en"] for c in pool["commanders"]}

partners = [r for r in rows if r["num_decks"] >= PARTNER_MIN]
backgrounds = [b for b in BACKGROUND_PAIRS if b["num_decks"] >= BACKGROUND_MIN][:3]

picks = partners + backgrounds
picks = [p for p in picks if p["name"] not in in_pool]
picks.sort(key=lambda r: -r["num_decks"])

(DATA / "new_pool_members.json").write_text(
    json.dumps([p["name"] for p in picks], ensure_ascii=False, indent=2),
    encoding="utf-8")

print(f"待补入 {len(picks)} 组组合")
print(f"\n  {'套牌数':>8} {'排名':>6}  {'类型':<6} 组合")
for p in picks:
    print(f"  {p['num_decks']:>8,} #{str(p['rank']):>5}  {p['kind']:<6} {p['name']}")

already = [r for r in rows if r["name"] in in_pool]
if already:
    print(f"\n已在池中（跳过）：")
    for r in already:
        print(f"  {r['num_decks']:>8,}  {r['name']}")
