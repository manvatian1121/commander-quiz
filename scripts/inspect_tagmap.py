#!/usr/bin/env python3
"""抽查关键标签的轴映射，人工核对质量。"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
m = json.loads((DATA / "tag_axis_map.json").read_text(encoding="utf-8"))
mp, ig = m["mapped"], m["ignored"]

INTEREST = [
    "Wheels", "Defenders", "Pillow Fort", "Prison", "Combo", "Midrange", "Good Stuff",
    "Card Draw", "Legends", "Historic", "Toughness Matters", "Mill", "Chaos", "Group Hug",
    "Monarch", "Aikido", "Forced Combat", "Discard", "Stax", "Hatebears", "Land Destruction",
    "Treasure", "Food", "Infect", "+1/+1 Counters", "Voltron", "Auras", "Enchantress",
    "Blink", "ETB", "Clones", "Theft", "Reanimator", "Aristocrats", "Lifegain", "Group Slug",
    "Burn", "Tokens", "Aggro", "Ramp", "Big Mana", "X Spells", "Lands Matter", "Landfall",
    "Spellslinger", "Storm", "Equipment", "Artifacts", "Vehicles", "Sacrifice", "Graveyard",
    "Self-Mill", "Dredge", "Populate", "Go Wide", "Unblockable", "Extra Combats",
    "Attack Triggers", "Discover", "Cascade", "Eldrazi", "Pingers", "Spell Copy",
    "Counterspells", "Extra Turns", "Wheels", "Politics", "Donate", "Attractions", "Dungeon",
    "Die Roll", "Planeswalkers", "Shrines", "Sagas", "Totem", "Modified Creatures",
]

print("=== 已映射的关键标签 ===")
for tag in INTEREST:
    if tag in mp:
        print(f"  {tag:22s} -> {mp[tag]}")
    elif tag in ig:
        print(f"  {tag:22s} -> [忽略] {ig[tag]}")
    else:
        print(f"  {tag:22s} -> ?? 不在映射表")

print(f"\n=== 被忽略的 {len(ig)} 种标签 ===")
for tag, reason in sorted(ig.items()):
    print(f"  {tag:24s} {reason[:80]}")

# 统计各轴被多少标签指向
from collections import Counter

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
axis_tags: Counter = Counter()
for weights in mp.values():
    for axis in weights:
        axis_tags[axis] += 1
print("\n=== 各轴由多少标签指向 ===")
for axis, count in axis_tags.most_common():
    print(f"  {axis:<11} {count}")
