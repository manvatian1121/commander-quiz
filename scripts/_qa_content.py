# -*- coding: utf-8 -*-
"""内容 QA：禁用词、感叹号、中英牌名配对（后缀匹配法，避免把连接符吃进名字）。"""
import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
data = json.loads((DATA / "descriptions_1.json").read_text(encoding="utf-8"))
zh = json.loads((DATA / "card_zh_batch1.json").read_text(encoding="utf-8"))

BANNED = ["voltron", "stax", "ramp", "引擎", "曲线", "Bracket", "EDHREC", "咸度",
          "cEDH", "组合技", "上分", "最强"]
print("【禁用词扫描】")
hits = [(c, b) for c, v in data.items() for b in BANNED
        if b.lower() in (v["tagline"] + v["intro"] + v["build"]).lower()]
print("  ", hits or "无命中")

print("【感叹号】")
print("  ", [c for c, v in data.items() if "！" in "".join(v.values())] or "无")

print("【中英牌名配对（后缀匹配）】")
paren = re.compile(r"（([A-Za-z][^（）]*?)）")
NAMES = sorted({v for v in zh.values() if v}, key=len, reverse=True)
bad, unknown, pairs = [], [], 0
for c, v in data.items():
    for f in ("intro", "build"):
        text = v[f]
        for m in paren.finditer(text):
            en = m.group(1).strip()
            pairs += 1
            before = text[:m.start()]
            hit = next((n for n in NAMES if before.endswith(n)), None)
            if en not in zh:
                unknown.append((c, f, hit, en))
                continue
            official = zh[en]
            if official and hit != official:
                bad.append((c, f, hit, en, official))
print(f"   共 {pairs} 处中英配对")
if bad:
    for c, f, hit, en, official in bad:
        print(f"   ✗ {c}/{f}: 写了「{hit}」但 {en} 的官方中文名是「{official}」")
else:
    print("   ✓ 每处「中文（English）」的英文都对应刚写的中文名")
if unknown:
    print("   需人工核对（不在中文名表的英文）：")
    for c, f, hit, en in unknown:
        print(f"     ? {c}/{f}: 「{hit}」/ {en}")
