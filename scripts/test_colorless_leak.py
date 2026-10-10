#!/usr/bin/env python3
"""验证无色：选了无色选项的人才拿得到无色主将，其他人拿不到。"""
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
LABELS = ["单色", "双色", "三色", "四色", "五色", "无色"]

quiz = load_quiz()
payload = load_commanders()
rng = random.Random(555)
ROUNDS = 40

print("各选项下，无色主将进入前三的频率（40 轮 × 3 个位置 = 120）")
print("-" * 66)
for idx, label in enumerate(LABELS):
    hits = 0
    total = 0
    for _ in range(ROUNDS):
        answers = {BREADTH_Q: idx}
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
            total += 1
            hits += (r["colors"] == "C")
    rate = hits / total * 100
    bar = "█" * int(rate / 2)
    flag = "  ← 想要无色" if label == "无色" else ""
    print(f"  {label:<5} {hits:>3}/{total}  {rate:>5.1f}%  {bar}{flag}")

print("\n无色主将全池只有 5 位（占 1.0%）。")
print("理想结果：选「无色」的那一档明显高于其它档，其它档接近或低于 1%。")
