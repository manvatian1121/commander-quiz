#!/usr/bin/env python3
"""广度题上线后，重测各颜色身份的触达率。

重点看：五色与无色主将进前三的比例，是否从「明显低于池中占比」变为接近。
"""
from __future__ import annotations

import pathlib
import random
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, load_quiz, score_commanders, tally  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent

DATA = pathlib.Path(r"ROOT\data")
COLOR_Q = ["s49", "s59", "s60", "s62"]
BREADTH_Q = "s62b"
SAMPLES_PER_BREADTH = int(sys.argv[1]) if len(sys.argv) > 1 else 80

quiz = load_quiz()
payload = load_commanders()
by_color = Counter(c["colors"] for c in payload["commanders"])
total_cmds = len(payload["commanders"])
rng = random.Random(20261010)

top3: Counter = Counter()
by_breadth: dict[float, Counter] = {}

print("=== 按广度选项分别取样，看各色主将进前三的频率 ===")
for breadth_idx in range(5):
    label = ["单色", "双色", "三色", "五色", "无色"][breadth_idx]
    counter: Counter = Counter()
    for _ in range(SAMPLES_PER_BREADTH):
        answers = {BREADTH_Q: breadth_idx}
        for qid in COLOR_Q:
            answers[qid] = rng.randrange(5)
        for q in quiz["questions"]:
            if q["id"] in answers:
                continue
            n = len(q["opts"])
            answers[q["id"]] = ([rng.randrange(n) for _ in range(min(q.get("multi", 1), n))]
                                if q.get("multi") else rng.randrange(n))
        pref, colors, cons = tally(quiz, answers)
        for r in score_commanders(payload, pref, colors, cons)[:3]:
            counter[r["colors"]] += 1
            top3[r["colors"]] += 1
    by_breadth[breadth_idx] = counter
    five = counter.get("WUBRG", 0) / (SAMPLES_PER_BREADTH * 3) * 100
    none = counter.get("C", 0) / (SAMPLES_PER_BREADTH * 3) * 100
    print(f"  选「{label}」的人：五色主将 {five:>5.1f}%   无色主将 {none:>5.1f}%")

grand = sum(top3.values())
print(f"\n=== 总体（{grand} 个前三位置）===")
print(f"  {'颜色身份':<10} {'进前三':>8} {'占比':>7} {'池中占比':>9} {'倍数':>6}")
for code in ["WUBRG", "C", "G", "WB", "UR"]:
    n = top3.get(code, 0)
    label = {"WUBRG": "五色", "C": "无色", "G": "单绿", "WB": "白黑", "UR": "蓝红"}[code]
    pool_share = by_color[code] / total_cmds * 100
    share = n / grand * 100
    ratio = share / pool_share if pool_share else 0
    print(f"  {label:<10} {n:>8} {share:>6.1f}% {pool_share:>8.1f}% {ratio:>5.2f}×")

print("\n=== 对照（广度题上线前）===")
print("  五色 2.9%（池中 6.3%，0.46×）")
print("  无色 0.6%（池中 1.0%，0.60×）")
print("  单绿 10.0%（池中 3.9%，2.56×）")
