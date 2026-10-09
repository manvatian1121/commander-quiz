#!/usr/bin/env python3
"""分析遗漏扫描结果：不同套牌数门槛下各有多少位遗漏，其中多少是非生物主将。"""
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

missing = json.loads((DATA / "missing_commanders.json").read_text(encoding="utf-8"))
allp = json.loads((DATA / "all_commander_profiles.json").read_text(encoding="utf-8"))
pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))

print(f"能当主将且 EDHREC 有档案的：{len(allp)} 位")
print(f"其中已在池中：{len(pool['commanders'])} 位")
print(f"遗漏（≥1200 副）：{len(missing)} 位")

print("\n=== 按套牌数门槛看遗漏规模 ===")
for threshold in (20000, 15000, 10000, 8000, 5000, 3000, 2000, 1200):
    group = [m for m in missing if m["num_decks"] >= threshold]
    noncreature = [m for m in group if "Creature" not in (m.get("type_line") or "")]
    print(f"  ≥{threshold:>6} 副：{len(group):>4} 位  "
          f"（其中非生物主将 {len(noncreature)} 位）"
          f"　→ 若全补，池子 {len(pool['commanders']) + len(group)} 位")

print("\n=== 遗漏的鹏洛客 / 非生物主将（≥1200 副，按套牌数）===")
noncreature = [m for m in missing if "Creature" not in (m.get("type_line") or "")]
noncreature.sort(key=lambda m: -m["num_decks"])
for row in noncreature[:40]:
    kind = (row.get("type_line") or "").split("—")[0].strip()
    print(f"  {row['num_decks']:>6} 副  #{str(row['rank']):>4}  {row['name'][:42]:<42} {kind}")

print(f"\n非生物主将合计 {len(noncreature)} 位")

print("\n=== 遗漏主将的发行年份分布（≥5000 副）===")
recent = [m for m in missing if m["num_decks"] >= 5000]
years = Counter((m.get("released_at") or "????")[:4] for m in recent)
print(f"  {dict(sorted(years.items()))}")
