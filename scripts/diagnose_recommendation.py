#!/usr/bin/env python3
"""诊断「过度推荐」的真正成因。

两个测量：
① 解析式：每位主将的向量与「均匀随机单位向量」的平均余弦。
   这个值高 = 该主将匹配球面上的大部分方向 = 天生容易被推荐。
② 经验式：按「人格」抽样答题——先随机抽一个口味方向（20 维），
   每题选与该方向最合的选项（加噪），这样样本之间才真正有差异。
"""
from __future__ import annotations

import json
import math
import pathlib
import random
import sys
from collections import Counter


# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import cosine, load_commanders, load_quiz, score_commanders, tally  # noqa: E402


DATA = pathlib.Path(ROOT / "data")
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 500
SEED = 20261009


def axis_list(quiz: dict, payload: dict) -> list[str]:
    axes: set[str] = set()
    for card in payload["commanders"]:
        axes |= set(card["vec"])
    for q in quiz["questions"]:
        for opt in q["opts"]:
            axes |= set(opt.get("s") or {})
    return sorted(axes)


def random_unit(rng: random.Random, axes: list[str]) -> dict[str, float]:
    v = {axis: rng.gauss(0, 1) for axis in axes}
    n = math.sqrt(sum(x * x for x in v.values()))
    return {k: x / n for k, x in v.items()}


def dot(scores: dict, direction: dict) -> float:
    return sum(scores.get(k, 0.0) * direction.get(k, 0.0) for k in direction)


def main() -> None:
    quiz = load_quiz()
    payload = load_commanders()
    by_name = {c["en"]: c for c in payload["commanders"]}
    axes = axis_list(quiz, payload)
    rng = random.Random(SEED)
    total_cmds = len(payload["commanders"])
    print(f"玩法轴 {len(axes)} 个，主将 {total_cmds} 位")

    print("\n=== ① 解析式：与均匀随机方向的平均余弦（越高越容易被推荐）===")
    directions = [random_unit(rng, axes) for _ in range(4000)]
    ranked = sorted(((sum(cosine(c["vec"], d) for d in directions) / len(directions),
                      c["en"]) for c in payload["commanders"]), reverse=True)
    mean_all = sum(m for m, _ in ranked) / len(ranked)
    print(f"  全池平均 {mean_all:.3f}")
    for value, name in ranked[:15]:
        card = by_name[name]
        print(f"  {value:.3f}  ({value / mean_all:.2f}×)  {card['zh']:<18} "
              f"轴数 {len(card['vec']):>2}  咸度 {card['salt']:.2f}")
    print("  … 最低 5 位 …")
    for value, name in ranked[-5:]:
        card = by_name[name]
        print(f"  {value:.3f}  ({value / mean_all:.2f}×)  {card['zh']:<18} "
              f"轴数 {len(card['vec']):>2}")

    print(f"\n=== ② 经验式：{SAMPLES} 个「人格」样本的前三频率 ===")
    top3: Counter = Counter()
    top1: Counter = Counter()
    for _ in range(SAMPLES):
        direction = random_unit(rng, axes)
        by_id = {q["id"]: q for q in quiz["questions"]}
        answers: dict = {}
        current = quiz["start"]
        guard = 0
        while current and guard < 600:
            q = by_id[current]
            n = len(q["opts"])
            scores = [dot(o.get("s") or {}, direction) + rng.gauss(0, 0.9)
                      for o in q["opts"]]
            if q.get("multi"):
                order = sorted(range(n), key=lambda i: -scores[i])
                answers[q["id"]] = order[:min(q["multi"], n)]
                nxt = q.get("next")
            else:
                idx = max(range(n), key=lambda i: scores[i])
                answers[q["id"]] = idx
                nxt = q["opts"][idx].get("goto") or q.get("next")
            current = nxt
            guard += 1
        pref, colors, cons = tally(quiz, answers)
        results = score_commanders(payload, pref, colors, cons)
        top1[results[0]["en"]] += 1
        for row in results[:3]:
            top3[row["en"]] += 1

    expected = SAMPLES * 3 / total_cmds
    print(f"  均匀预期：每位 {expected:.1f} 次（{expected / SAMPLES * 100:.2f}%）")
    for name, count in top3.most_common(18):
        card = by_name[name]
        ratio = count / expected
        flag = "  ← 偏高" if ratio > 5 else ""
        print(f"  {count / SAMPLES * 100:5.1f}%  ({count:>3} 次, {ratio:4.1f}×)  "
              f"{card['zh']:<18} 轴数 {len(card['vec']):>2}{flag}")

    print(f"\n=== 玛切莎女王对照 ===")
    mar = top3.get("Queen Marchesa", 0)
    mean_mar = next(m for m, n in ranked if n == "Queen Marchesa")
    rank_mar = [n for _, n in ranked].index("Queen Marchesa") + 1
    print(f"  平均余弦 {mean_mar:.3f}（全池第 {rank_mar}/{total_cmds} 位）")
    print(f"  人格样本进前三 {mar} 次（{mar / SAMPLES * 100:.2f}%，"
          f"{mar / expected:.1f}×）")
    print(f"  人格样本排第一 {top1.get('Queen Marchesa', 0)} 次")


if __name__ == "__main__":
    main()
