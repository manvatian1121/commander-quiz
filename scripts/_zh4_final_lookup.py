# -*- coding: utf-8 -*-
"""主将中文名：素材标题 vs card_zh.json vs commander_zh.json 三方对照；
并输出每位主将「有官方中文名」的可用牌名清单（供写作用）。"""
import json
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
D = ROOT / "data"
md = open(D + r"\writing_batch_new_4.md", encoding="utf-8").read()
card_zh = json.load(open(D + r"\card_zh.json", encoding="utf-8"))
cmd_zh = json.load(open(D + r"\commander_zh.json", encoding="utf-8"))

body = md.split("# 素材：30 位主将", 1)[1]
secs = [s for s in re.split(r"\n## ", body)[1:] if "｜" in s.split("\n")[0]]
print(f"主将数 {len(secs)}\n")
diff = []
for s in secs:
    lines = s.split("\n")
    cname, czh = [p.strip() for p in lines[0].split("｜", 1)]
    a, b = card_zh.get(cname), cmd_zh.get(cname)
    truth = a or b
    if truth != czh:
        diff.append((cname, czh, a, b))
    cards = []
    for line in lines:
        m = re.match(r"^\s{2,}(?:\d+\.|-)\s+(.+?)（", line)
        if m:
            n = m.group(1).strip()
            cards.append((n, card_zh.get(n)))
    usable = [(n, z) for n, z in cards if z]
    print(f"## {cname}  →  素材「{czh}」 card_zh={a} cmd_zh={b}")
    print(f"   可用（有中文名 {len(usable)}/{len(cards)}）：" +
          "、".join(f"{z}（{n}）" for n, z in usable))
print("\n素材标题与官方映射不一致的主将：")
for d in diff:
    print("   ", d)
