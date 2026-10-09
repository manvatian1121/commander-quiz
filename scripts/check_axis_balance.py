#!/usr/bin/env python3
"""查残余偏差的来源：题库是否偏向某些玩法轴？

如果「口味明确的人」答出来的偏好向量，主导轴分布是均匀的，
那么剩余的过度推荐就来自主将向量的几何分布，而不是题库。
"""
from __future__ import annotations

import math
import pathlib
import random
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, load_quiz, score_commanders, tally  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

DATA = pathlib.Path(ROOT / "data")
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 400
NOISE = float(sys.argv[2]) if len(sys.argv) > 2 else 0.2
SEED = 20261009


def random_unit(rng, axes):
    v = {axis: rng.gauss(0, 1) for axis in axes}
    n = math.sqrt(sum(x * x for x in v.values()))
    return {k: x / n for k, x in v.items()}


def main() -> None:
    quiz = load_quiz()
    payload = load_commanders()
    by_name = {c["en"]: c for c in payload["commanders"]}
    axes = sorted({a for c in payload["commanders"] for a in c["vec"]})
    by_id = {q["id"]: q for q in quiz["questions"]}
    rng = random.Random(SEED)

    dominant: Counter = Counter()
    top3: Counter = Counter()
    for _ in range(SAMPLES):
        direction = random_unit(rng, axes)
        answers: dict = {}
        current = quiz["start"]
        guard = 0
        while current and guard < 600:
            q = by_id[current]
            n = len(q["opts"])
            scores = [sum((o.get("s") or {}).get(k, 0.0) * direction.get(k, 0.0)
                          for k in direction) + rng.gauss(0, NOISE) for o in q["opts"]]
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
        if pref:
            top_axis = max(pref, key=lambda k: pref[k])
            dominant[top_axis] += 1
        results = score_commanders(payload, pref, colors, cons)
        for row in results[:3]:
            top3[row["en"]] += 1

    print(f"=== {SAMPLES} 个「口味明确」样本（噪声 {NOISE}）的主导轴分布 ===")
    print("  若均匀，每个轴应约 "
          f"{SAMPLES / len(axes):.0f} 次（{100 / len(axes):.1f}%）")
    for axis, count in dominant.most_common(20):
        bar = "█" * int(count / SAMPLES * 60)
        print(f"  {axis:<11} {count:>4} 次  {count / SAMPLES * 100:5.1f}%  {bar}")

    print(f"\n=== 前 12 名推荐（对照用）===")
    expected = SAMPLES * 3 / len(payload["commanders"])
    for name, count in top3.most_common(12):
        card = by_name[name]
        lead = max(card["vec"], key=lambda k: card["vec"][k])
        print(f"  {count / SAMPLES * 100:5.1f}%  ({count / expected:4.1f}×)  "
              f"{card['zh']:<18} 主导轴 {lead}")


if __name__ == "__main__":
    main()
