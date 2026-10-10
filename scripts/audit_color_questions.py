#!/usr/bin/env python3
"""盘点题库里带颜色得分（col）的题目，评估「一眼看穿」的程度。"""
from __future__ import annotations

import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"D:\万智\commander-quiz\data")
COLOR_WORDS = ["红", "蓝", "黑", "白", "绿", "灰", "紫", "橙", "黄", "粉", "青", "金", "银"]
COLOR_NAMES = {"W": "白", "U": "蓝", "B": "黑", "R": "红", "G": "绿"}

quiz = json.loads((DATA / "questions.json").read_text(encoding="utf-8"))
rows = []
for q in quiz["questions"]:
    colored = [opt for opt in q["opts"] if opt.get("col")]
    if not colored:
        continue
    text = q["q"] + "".join(opt["t"] for opt in q["opts"])
    # 颜色得分是否「一选项一色」——最容易被看穿的形态
    one_each = all(len(opt["col"]) == 1 for opt in colored) and len(colored) >= 4
    word_hits = sum(text.count(w) for w in COLOR_WORDS)
    rows.append({
        "id": q["id"], "sec": q.get("sec"), "q": q["q"], "opts": len(q["opts"]),
        "colored": len(colored), "one_each": one_each, "word_hits": word_hits,
    })

print(f"带颜色得分的题目：{len(rows)} 道\n")
print(f"  {'题号':<6} {'选项':>4} {'带色':>4} {'一选项一色':>10} {'颜色词':>6}  题干")
for row in rows:
    flag = "  ← 直球" if row["one_each"] and row["word_hits"] >= 3 else ""
    print(f"  {row['id']:<6} {row['opts']:>4} {row['colored']:>4} "
          f"{'是' if row['one_each'] else '否':>10} {row['word_hits']:>6}  "
          f"{row['q'][:34]}{flag}")

obvious = [r for r in rows if r["one_each"] and r["word_hits"] >= 3]
print(f"\n『一选项一色 + 题干或选项里出现 3 个以上颜色词』的：{len(obvious)} 道")
for row in obvious:
    print(f"  {row['id']}  {row['q']}")
