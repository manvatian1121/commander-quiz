#!/usr/bin/env python3
"""六档广度的统计测试：多套玩法答案取平均，避免单样本偶然。

颜色向量固定为五色均等（隔离掉「哪几个色」的干扰），只让广度变化。
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
EXPECT = [(0, 1, "单色"), (1, 2, "双色"), (2, 3, "三色"),
          (3, 4, "四色"), (4, 5, "五色"), (5, 0, "无色")]
ROUNDS = int(sys.argv[1]) if len(sys.argv) > 1 else 12

quiz = load_quiz()
payload = load_commanders()
by_name = {c["en"]: c for c in payload["commanders"]}
pool_count = Counter(0 if c["colors"] == "C" else len(c["colors"])
                     for c in payload["commanders"])
FLAT_COLORS = {c: 2.0 for c in "WUBRG"}
rng = random.Random(2024)

# 每轮重新抽一套玩法答案
playstyle_sets = []
for _ in range(ROUNDS):
    s = {}
    for q in quiz["questions"]:
        if q["id"] in COLOR_Q or q["id"] == BREADTH_Q:
            continue
        n = len(q["opts"])
        s[q["id"]] = ([rng.randrange(n) for _ in range(min(q.get("multi", 1), n))]
                      if q.get("multi") else rng.randrange(n))
    playstyle_sets.append(s)

print(f"{ROUNDS} 套玩法答案 × 6 档广度。池中各色数的主将数量："
      f"{ {k: pool_count[k] for k in range(6)} }\n")
print(f"{'选择':<6} {'想要':>4} {'进前三':>8} {'占比':>7} {'池中占比':>9} {'倍数':>7}")
print("-" * 62)
for idx, want, label in EXPECT:
    hits = 0
    total = 0
    for base in playstyle_sets:
        answers = dict(base)
        answers[BREADTH_Q] = idx
        for qid in COLOR_Q:
            answers[qid] = 0
        pref, _c, cons = tally(quiz, answers)
        for r in score_commanders(payload, pref, FLAT_COLORS, cons)[:3]:
            total += 1
            n_col = 0 if by_name[r["en"]]["colors"] == "C" else len(by_name[r["en"]]["colors"])
            hits += (n_col == want)
    pool_share = pool_count[want] / len(payload["commanders"]) * 100
    share = hits / total * 100
    ratio = share / pool_share if pool_share else 0
    bar = "█" * int(min(ratio, 4) * 6)
    print(f"  {label:<5} {want:>4} {hits:>4}/{total:<4} {share:>6.1f}% "
          f"{pool_share:>8.1f}% {ratio:>6.2f}× {bar}")

print("\n倍数 = 该档位的进前三占比 ÷ 它在池中的占比。")
print("1.0× 左右代表「想要几个色」被准确兑现；远低于 1 代表这个口味够不到。")
