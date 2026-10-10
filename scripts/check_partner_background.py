#!/usr/bin/env python3
"""检查主将池里有没有拍档（Partner）与身世（Background）主将。"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"D:\万智\commander-quiz\data")

pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))["commanders"]
scry = json.loads((DATA / "commanders_scryfall.json").read_text(encoding="utf-8"))

lookup = {}
for name, card in scry.items():
    lookup[name] = card
    lookup.setdefault(name.split(" // ")[0], card)

PATTERNS = {
    "Partner（可选任意搭档）": re.compile(r"\bPartner\b(?! with)", re.I),
    "Partner with（指定搭档）": re.compile(r"Partner with ", re.I),
    "Choose a Background（身世）": re.compile(r"Choose a Background", re.I),
    "Friends forever": re.compile(r"Friends forever", re.I),
    "Doctor's companion": re.compile(r"Doctor's companion", re.I),
    "Background 牌（灵气）": re.compile(r"^Background", re.I | re.M),
}
# Background 是子类型，看 type_line
BG_TYPE = re.compile(r"—\s*Background\b", re.I)

print(f"主将池共 {len(pool)} 位\n")
print("=== 池中的拍档 / 身世 主将 ===")
found: dict[str, list[str]] = {k: [] for k in PATTERNS}
found["Background 子类型"] = []
bg_commanders = []

for c in pool:
    info = lookup.get(c["en"]) or lookup.get(c["en"].split(" // ")[0]) or {}
    text = info.get("oracle_text") or ""
    tline = info.get("type_line") or ""
    for label, pat in PATTERNS.items():
        if pat.search(text):
            found[label].append(c["en"])
    if BG_TYPE.search(tline):
        found["Background 子类型"].append(c["en"])
    if "Choose a Background" in text:
        bg_commanders.append(c["en"])

for label, names in found.items():
    if label == "Background 牌（灵气）":
        continue
    print(f"\n  【{label}】{len(names)} 位")
    for n in names[:14]:
        print(f"      {n}")
    if len(names) > 14:
        print(f"      …还有 {len(names) - 14} 位")

# 全库（不只池子）里有多少这类主将
print("\n=== 全库（1578 位有 EDHREC 档案的）里这类主将有多少 ===")
allp = json.loads((DATA / "all_commander_profiles.json").read_text(encoding="utf-8"))
poolset = {c["en"] for c in pool}
print(f"  有档案的主将 {len(allp)} 位，池中 {len(poolset)} 位")
