# -*- coding: utf-8 -*-
"""检查各 zh 映射文件的覆盖情况与 schema，判断 card_zh.json 是否唯一权威。"""
import json
import os
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
D = ROOT / "data"

files = ["card_zh.json", "card_zh_b2.json", "card_zh_batch1.json", "_card_zh_3.json",
         "_card_zh_new3.json", "zh_cards.json", "commander_zh.json", "card_display.json"]

maps = {}
for f in files:
    p = os.path.join(D, f)
    if not os.path.exists(p):
        print(f"{f}: 不存在")
        continue
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        print(f"{f}: 读取失败 {e}")
        continue
    if isinstance(d, dict):
        sample = list(d.items())[:2]
        print(f"{f}: dict, {len(d)} 条, 样例 {sample}")
        maps[f] = d
    else:
        print(f"{f}: 非 dict 类型 {type(d)}")

# 素材里所有牌名
md = open(os.path.join(D, "writing_batch_new_4.md"), encoding="utf-8").read()
body = md.split("# 素材：30 位主将", 1)[1]
sections = re.split(r"\n## ", body)
allnames = set()
cmdnames = []
for sec in sections[1:]:
    lines = sec.split("\n")
    head = lines[0]
    if "｜" not in head:
        continue
    cname = head.split("｜")[0].strip()
    cmdnames.append(cname)
    allnames.add(cname)
    for line in lines:
        m = re.match(r"^\s{2,}(?:\d+\.|-)\s+(.+?)（", line)
        if m:
            allnames.add(m.group(1).strip())

print(f"\n素材牌名（含主将）去重共 {len(allnames)}")
print("\n--- 各文件对素材牌名的命中数 ---")
for f, d in maps.items():
    hit = [n for n in allnames if n in d]
    print(f"  {f}: {len(hit)}/{len(allnames)}")

# 合并视图
nonempty = {}
for f, d in maps.items():
    if f in ("card_display.json",):
        continue
    for k, v in d.items():
        if isinstance(v, str) and v.strip() and k not in nonempty:
            nonempty[k] = (v, f)
hit = [n for n in allnames if n in nonempty]
print(f"\n各 zh 文件并集覆盖: {len(hit)}/{len(allnames)}")
miss = sorted(n for n in allnames if n not in nonempty)
print(f"仍然缺失 {len(miss)}:")
for m in miss:
    print("   ", m)
