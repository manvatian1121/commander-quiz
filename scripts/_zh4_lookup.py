# -*- coding: utf-8 -*-
"""解析 writing_batch_new_4.md，为每位主将的清单牌名查 card_zh.json 官方中文名。"""
import json
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

MD = ROOT / "data" / "writing_batch_new_4.md"
ZH = ROOT / "data" / "card_zh.json"

md = open(MD, encoding="utf-8").read()
zh = json.load(open(ZH, encoding="utf-8"))

body = md.split("# 素材：30 位主将", 1)[1]
sections = re.split(r"\n## ", body)

out = []
order = []
for sec in sections[1:]:
    lines = sec.split("\n")
    head = lines[0]
    if "｜" not in head:
        continue
    cname, czh = [p.strip() for p in head.split("｜", 1)]
    order.append(cname)
    cards = []
    for line in lines:
        m = re.match(r"^\s{2,}(?:\d+\.|-)\s+(.+?)（", line)
        if m:
            cards.append(m.group(1).strip())
    out.append((cname, czh, cards))

print(f"主将数 = {len(out)}")
missing_zh_any = []
for cname, czh, cards in out:
    c_lookup = zh.get(cname)
    print()
    print(f"## {cname}")
    print(f"   主将中文：素材={czh}  card_zh={c_lookup}  {'OK' if c_lookup == czh else '!!不同/缺失'}")
    for c in cards:
        v = zh.get(c)
        if v is None:
            missing_zh_any.append(c)
        print(f"   - {c}  ->  {v}")

print()
print(f"清单牌名总数（去重）={len(set(missing_zh_any))}")
print("card_zh 缺中文的牌名：")
for m in sorted(set(missing_zh_any)):
    print("   ", m)
