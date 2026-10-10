#!/usr/bin/env python3
"""直接看：选了某个广度选项的人，实际拿到什么主将。"""
from __future__ import annotations

import pathlib
import random
import sys


# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, load_quiz, score_commanders, tally  # noqa: E402

DATA = pathlib.Path(r"ROOT\data")
COLOR_Q = ["s49", "s59", "s60", "s62"]
BREADTH_Q = "s62b"
LABELS = ["单色", "双色", "三色", "五色", "无色"]

quiz = load_quiz()
payload = load_commanders()
by_name = {c["en"]: c for c in payload["commanders"]}
rng = random.Random(7)

for idx, label in enumerate(LABELS):
    print(f"\n{'=' * 70}\n选了「{label}」的人（其余颜色题与全部玩法题用同一套固定答案）")
    answers = {BREADTH_Q: idx}
    # 颜色题固定选第一个选项，确保只有广度在变
    for qid in COLOR_Q:
        answers[qid] = 0
    for q in quiz["questions"]:
        if q["id"] in answers:
            continue
        n = len(q["opts"])
        answers[q["id"]] = ([rng.randrange(n) for _ in range(min(q.get("multi", 1), n))]
                            if q.get("multi") else rng.randrange(n))
    pref, colors, cons = tally(quiz, answers)
    print(f"  实际广度值 = {cons['breadth']:.2f}　颜色向量 = "
          f"{ {k: round(v, 1) for k, v in sorted(colors.items())} }")
    results = score_commanders(payload, pref, colors, cons)
    for rank, row in enumerate(results[:3], 1):
        card = by_name[row["en"]]
        print(f"    {rank}. {card['zh']:<18} {card['colors']:<6} "
              f"色数 {len(card['colors'])}　总 {row['score']:.4f}　"
              f"颜色分 {row['affinity']:.3f}")
