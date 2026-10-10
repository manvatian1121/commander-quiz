#!/usr/bin/env python3
"""① 统计当前主将池的发行年份分布，验证「新主将偏少」；
   ② 检查 EDHREC 主将页里的 similar 字段，看能不能用来挖更深的名单。"""
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

payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
scry = json.loads((DATA / "commanders_scryfall.json").read_text(encoding="utf-8"))

lookup = {}
for name, card in scry.items():
    lookup[name] = card
    lookup.setdefault(name.split(" // ")[0], card)

print("=== 当前主将池（110 位）的发行年份分布 ===")
years: Counter = Counter()
for card in payload["commanders"]:
    info = lookup.get(card["en"]) or lookup.get(card["en"].split(" // ")[0]) or {}
    year = (info.get("released_at") or "????")[:4]
    years[year] += 1
for year in sorted(years):
    bar = "█" * years[year]
    print(f"  {year}  {years[year]:>3} {bar}")

recent = sum(v for k, v in years.items() if k >= "2025")
print(f"\n2025 年及以后发行的：{recent} 位（占 {recent / len(payload['commanders']) * 100:.0f}%）")

print("\n=== EDHREC 主将页的 similar 字段结构 ===")
probe = DATA / "supp_brago-king-eternal.json"
raw = json.loads(probe.read_text(encoding="utf-8"))
similar = raw.get("similar")
print(f"  类型 {type(similar).__name__}")
if isinstance(similar, list) and similar:
    print(f"  条目数 {len(similar)}")
    print(f"  sample keys: {sorted(similar[0].keys())}")
    print(f"  sample: {json.dumps(similar[0], ensure_ascii=False)[:300]}")
    names = [s.get("name") for s in similar[:10]]
    print(f"  前 10 个：{names}")
elif isinstance(similar, dict):
    print(f"  keys: {list(similar.keys())[:11]}")
    for key, value in list(similar.items())[:3]:
        if isinstance(value, list) and value:
            print(f"  [{key}] {len(value)} 条，sample keys={sorted(value[0].keys())}")
            print(f"     {[v.get('name') for v in value[:5]]}")

print("\n=== 已抓过档案但没进池的主将（commander_profiles.json 里有、池里没有）===")
profiles = json.loads((DATA / "commander_profiles.json").read_text(encoding="utf-8"))
in_pool = {c["en"] for c in payload["commanders"]}
unused = []
for name, prof in profiles.items():
    if name in in_pool:
        continue
    info = lookup.get(name) or lookup.get(name.split(" // ")[0]) or {}
    unused.append((prof.get("rank") or 99999, prof.get("num_decks") or 0,
                   (info.get("released_at") or "????")[:7], name))
unused.sort()
print(f"  共 {len(unused)} 位")
for rank, decks, released, name in unused[:40]:
    print(f"    #{rank:>4}  {decks:>6} 副  {released}  {name}")
