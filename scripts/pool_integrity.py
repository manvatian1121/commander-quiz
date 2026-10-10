#!/usr/bin/env python3
"""扩池后的完整性检查：每位主将是否都有牌面、中文名、搭配牌、介绍文。"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")


def load(name, default):
    path = DATA / name
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


pool = load("commanders.json", {"commanders": []})
cmds = pool["commanders"]
scry = load("commanders_scryfall.json", {})
cards = load("commander_cards.json", {})
display = load("card_display.json", {})

scr_lookup = {}
for name, card in scry.items():
    scr_lookup[name] = card
    scr_lookup.setdefault(name.split(" // ")[0], card)

desc = {}
for i in range(1, 21):
    desc.update(load(f"descriptions_{i}.json", {}))

print(f"主将 {len(cmds)} 位")
missing_zh = [c["en"] for c in cmds if not c["zh"]]
missing_scry = [c["en"] for c in cmds
                if not (scr_lookup.get(c["en"]) or scr_lookup.get(c["en"].split(" // ")[0]))]
missing_cards = [c["en"] for c in cmds if not (cards.get(c["en"]) or {}).get("synergy_top")]
missing_display = [c["en"] for c in cmds if not (display.get(c["en"]) or {}).get("synergy")]
missing_desc = [c["en"] for c in cmds if c["en"] not in desc]
thin_synergy = [(c["en"], len((cards.get(c["en"]) or {}).get("synergy_top") or []))
                for c in cmds if len((cards.get(c["en"]) or {}).get("synergy_top") or []) < 4]

print(f"  无中文名 {len(missing_zh)}：{missing_zh[:8]}")
print(f"  无 Scryfall 牌面 {len(missing_scry)}：{missing_scry[:8]}")
print(f"  无搭配牌数据 {len(missing_cards)}：{missing_cards[:8]}")
print(f"  未进 card_display {len(missing_display)}：{missing_display[:8]}")
print(f"  无介绍文 {len(missing_desc)}")
print(f"  高协同牌少于 4 张的 {len(thin_synergy)} 位：{thin_synergy[:12]}")

print(f"\n颜色分布：{dict(Counter(c['colors'] for c in cmds).most_common(10))}")
print(f"难度分布：{dict(sorted(Counter(c['complexity'] for c in cmds).items()))}")
print(f"套牌数区间：{min(c['num_decks'] for c in cmds)} ~ {max(c['num_decks'] for c in cmds)}")

# 新并入的主将里，发行年份
# 新并入的主将分两批，发行年份合起来看
new = load("new_pool_members.json", []) + load("_new_pool_members_120.json", [])
years = Counter()
for name in new:
    info = scr_lookup.get(name) or scr_lookup.get(name.split(" // ")[0]) or {}
    years[(info.get("released_at") or "????")[:4]] += 1
print(f"\n新增 {len(new)} 位的首次印刷年份：{dict(sorted(years.items()))}")
