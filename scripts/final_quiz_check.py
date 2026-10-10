#!/usr/bin/env python3
"""交付前最终核对：确认新题库（性格题 + 分支）真的进了成品。"""
from __future__ import annotations

import json
import pathlib
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)

html = (ROOT / "commander_quiz.html").read_text(encoding="utf-8")
match = re.search(r'<script id="payload" type="application/json">(.*?)</script>',
                  html, re.S)
data = json.loads(match.group(1).replace("<\\/", "</"))
quiz = data["quiz"]
questions = quiz["questions"]
by_id = {q["id"]: q for q in questions}

print("=== 成品内嵌数据 ===")
print(f"  题库 {len(questions)} 题 ｜ 起始 {quiz['start']} ｜ 主线 {len(quiz['spine'])} ｜ "
      f"快速版 {len(quiz['quick'])} 道主线题")
print(f"  主将 {len(data['commanders'])} 位 ｜ 介绍文 {len(data['descriptions'])} 篇 ｜ "
      f"搭配牌 {len(data['cardInfo'])} 张")
print(f"  文件大小 {(ROOT / 'commander_quiz.html').stat().st_size / 1024:.0f} KB")

hubs = [q["id"] for q in questions if q.get("kind") == "hub"]
multis = [q["id"] for q in questions if q.get("multi")]
branches = [q["id"] for q in questions if q["id"] not in quiz["spine"]]
print(f"\n  枢纽题 {len(hubs)}：{hubs}")
print(f"  多选题 {len(multis)}：{multis}")
print(f"  分支衍生题 {len(branches)} 道")

print("\n=== 抽查：性格题是否真的生活化 ===")
for qid in ["s01", "s08", hubs[1] if len(hubs) > 1 else hubs[0], "s35", "s56", multis[0], "c01"]:
    q = by_id.get(qid)
    if not q:
        continue
    tag = "【枢纽】" if q.get("kind") == "hub" else ("【多选】" if q.get("multi") else "")
    print(f"\n  {qid}{tag} {q['q']}")
    for i, o in enumerate(q["opts"][:3]):
        goto = f"  ⇒{o['goto']}" if o.get("goto") else ""
        print(f"      {'ABCDE'[i]}. {o['t']}{goto}")

print("\n=== 分支示例（s08 的 A 分支）===")
for qid in [o.get("goto") for o in by_id["s08"]["opts"] if o.get("goto")][:1]:
    while qid and qid in by_id:
        q = by_id[qid]
        print(f"  {qid}: {q['q'][:56]}")
        qid = q.get("next") if qid not in quiz["spine"] else None

# 术语抽查
JARGON = ["主将", "牌组", "咒语", "铺场", "坟场", "法术力", "万智"]
hits = [(q["id"], w) for q in questions
        for w in JARGON if w in q["q"] + "".join(o["t"] for o in q["opts"])]
print(f"\n=== 万智牌术语扫描：{len(hits)} 处命中 ===")
for qid, w in hits[:10]:
    print(f"  {qid}: 「{w}」")
if not hits:
    print("  干净")
