#!/usr/bin/env python3
"""测量主将的「过度推荐」程度。

方法：生成大量答题组合（结构化 + 随机），统计每位主将进入前三的频率。
如果某些主将出现频率远高于同侪，说明它们的向量太「讨喜」——
余弦相似度对「轴少而集中」的向量天然有利，容易刷出一堆高分。
"""
from __future__ import annotations

import json
import pathlib
import random
import sys
from collections import Counter


# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, load_quiz, score_commanders, tally  # noqa: E402


DATA = pathlib.Path(ROOT / "data")
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 600
SEED = 20261009


def walk(quiz: dict, picker) -> dict:
    by_id = {q["id"]: q for q in quiz["questions"]}
    answers: dict = {}
    current = quiz["start"]
    guard = 0
    while current and guard < 600:
        q = by_id[current]
        n = len(q["opts"])
        if q.get("multi"):
            count = min(q["multi"], n)
            chosen = picker(q, n, True, count)
            answers[q["id"]] = chosen
            nxt = q.get("next")
        else:
            idx = picker(q, n, False, 1)
            answers[q["id"]] = idx
            opt = q["opts"][idx]
            nxt = opt.get("goto") or q.get("next")
        current = nxt
        guard += 1
    return answers


def main() -> None:
    quiz = load_quiz()
    payload = load_commanders()
    by_name = {c["en"]: c for c in payload["commanders"]}
    rng = random.Random(SEED)

    top1: Counter = Counter()
    top3: Counter = Counter()
    total = 0

    for sample in range(SAMPLES):
        if sample < 8:
            # 前 8 个用结构化策略（固定选第 k 个选项），其余随机
            fixed = sample
            picker = lambda q, n, multi, k, f=fixed: (f % n if not multi  # noqa: E731
                                                       else [(f + c) % n for c in range(k)])
        else:
            picker = lambda q, n, multi, k: (  # noqa: E731
                [rng.randrange(n) for _ in range(k)] if multi else rng.randrange(n))
        answers = walk(quiz, picker)
        pref, colors, cons = tally(quiz, answers)
        results = score_commanders(payload, pref, colors, cons)
        total += 1
        top1[results[0]["en"]] += 1
        for row in results[:3]:
            top3[row["en"]] += 1

    print(f"样本 {total} 组答题")
    print(f"\n=== 进入前三的频率（前 20 名）===")
    for name, count in top3.most_common(20):
        card = by_name[name]
        axes = len(card["vec"])
        pct = count / total * 100
        flag = "  ← 明显偏高" if pct > 12 else ""
        print(f"  {pct:5.1f}%  ({count:>3} 次)  {card['zh']:<16} "
              f"轴数 {axes:>2}  咸度 {card['salt']:.2f}  B{card['bracket']}{flag}")

    print(f"\n=== 被排第一的频率（前 12 名）===")
    for name, count in top1.most_common(12):
        card = by_name[name]
        print(f"  {count / total * 100:5.1f}%  ({count:>3} 次)  {card['zh']}")

    expected = total * 3 / len(payload["commanders"])
    print(f"\n=== 诊断 ===")
    print(f"  池子 {len(payload['commanders'])} 位，若完全均匀，每位预期进前三 "
          f"{expected:.1f} 次（{expected / total * 100:.2f}%）")
    mar = top3.get("Queen Marchesa", 0)
    print(f"  玛切莎女王：进前三 {mar} 次（{mar / total * 100:.2f}%），"
          f"是均匀预期的 {mar / expected:.1f} 倍" if expected else "")
    if "Queen Marchesa" in by_name:
        card = by_name["Queen Marchesa"]
        print(f"  她的向量（{len(card['vec'])} 个轴）：{card['vec']}")


if __name__ == "__main__":
    main()
