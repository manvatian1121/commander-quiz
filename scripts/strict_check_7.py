# -*- coding: utf-8 -*-
"""严格补充校验：
 S1 「中文（English）」里的 English 必须与素材牌名**逐字**相同（不做标点归一化）。
 S2 主将中文名（含简称片段）若在正文出现，必须紧邻英文原名（否则算纯中文提牌）。
 S3 禁用词/营销腔：引擎、曲线、ramp、stax、voltron、Bracket、EDHREC、咸度、最强、神级、！ 等。
 S4 数字清点：列出正文里所有阿拉伯数字，人工确认都来自素材 oracle text（非编造的套牌统计）。
"""
import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
SRC = DATA / "writing_batch_new_4.md"
OUT = DATA / "descriptions_7.json"

text = SRC.read_text(encoding="utf-8")
commanders = re.findall(r"^## (.+?) ｜ (.+)$", text, re.M)
zh_of = {en.strip(): zh.strip() for en, zh in commanders}

whitelist = set(zh_of)
for line in text.splitlines():
    m = re.match(r"^(?:\d+\.|[-*])\s+(.+?)\uff08", line.strip())
    if m:
        n = m.group(1).strip()
        if n and not n.startswith("**"):
            whitelist.add(n)

data = json.loads(OUT.read_text(encoding="utf-8"))
problems = 0

# S1 精确英文
bad_exact = []
for k, e in data.items():
    for f in ("tagline", "intro", "build"):
        for m in re.finditer(r"（([A-Za-z][^（）]*?)）", e[f]):
            if m.group(1) not in whitelist:
                bad_exact.append((k, f, m.group(1)))
print(f"S1 括号内英文与素材牌名逐字一致：{'通过' if not bad_exact else '失败'}")
for b in bad_exact:
    print("   ✗", b)
problems += bool(bad_exact)

# S2 主将中文名片段
print("S2 主将中文名（含 2~4 字简称）出现位置：")
hits = []
for k, e in data.items():
    zh = zh_of[k]
    cands = {zh}
    for L in (2, 3, 4):                     # 简称：去掉前 2~4 字的前缀名字部分
        if len(zh) - L >= 2:
            cands.add(zh[L:])
    for f in ("tagline", "intro", "build"):
        v = e[f]
        for c in cands:
            for m in re.finditer(re.escape(c), v):
                tail = v[m.end():m.end() + 40]
                paired = re.match(r"^（[A-Za-z]", tail) is not None
                hits.append((k, f, c, paired))
for k, f, c, paired in hits:
    flag = "OK（已并列）" if paired else "✗ 纯中文提到主将名"
    print(f"   {flag}  {k} / {f}：{c}")
    if not paired:
        problems += 1

# S3 禁用词
BANNED = ["引擎", "曲线", "ramp", "stax", "voltron", "Voltron", "Bracket", "EDHREC",
          "咸度", "最强", "神级", "上分", "无敌强", "！", "!", "军备竞赛", "打分"]
banned_hits = []
for k, e in data.items():
    for f in ("tagline", "intro", "build"):
        for w in BANNED:
            if w in e[f]:
                banned_hits.append((k, f, w))
print(f"S3 禁用词：{'无' if not banned_hits else banned_hits}")
problems += bool(banned_hits)

# S4 数字
print("S4 正文里的阿拉伯数字/数量词：")
for k, e in data.items():
    for f in ("tagline", "intro", "build"):
        for m in re.finditer(r"[0-9]+(?:/[0-9]+)?", e[f]):
            print(f"   {k} / {f}：{m.group(0)}     …{e[f][max(0,m.start()-14):m.end()+10]}…")

print(f"\n补充校验总判定：{'通过' if not problems else '存在问题'}")
