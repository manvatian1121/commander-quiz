#!/usr/bin/env python3
"""验证「人格抽样」的噪声假设。

如果答题时的噪声远大于口味信号，答出来的偏好向量就会收敛到「平均选项向量」，
于是所有人看起来都一样、推荐也被少数「居中」的主将垄断。
这里扫不同的噪声水平，并直接测量不同人格之间偏好向量的相似度。
"""
from __future__ import annotations

import math
import pathlib
import random
import statistics
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import cosine, load_commanders, load_quiz, score_commanders, tally  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

DATA = pathlib.Path(ROOT / "data")
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 300
SEED = 20261009
NOISES = [0.2, 0.5, 0.9, 1.5]


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
    total_cmds = len(payload["commanders"])
    expected = SAMPLES * 3 / total_cmds

    for noise in NOISES:
        rng = random.Random(SEED)
        top3: Counter = Counter()
        prefs: list[dict] = []
        for _ in range(SAMPLES):
            direction = random_unit(rng, axes)
            answers: dict = {}
            current = quiz["start"]
            guard = 0
            while current and guard < 600:
                q = by_id[current]
                n = len(q["opts"])
                scores = [sum((o.get("s") or {}).get(k, 0.0) * direction.get(k, 0.0)
                              for k in direction) + rng.gauss(0, noise)
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
            prefs.append(pref)
            results = score_commanders(payload, pref, colors, cons)
            for row in results[:3]:
                top3[row["en"]] += 1

        # 不同人格之间的偏好向量相似度
        sample_pairs = [(rng.randrange(len(prefs)), rng.randrange(len(prefs)))
                        for _ in range(400)]
        sims = [cosine(prefs[a], prefs[b]) for a, b in sample_pairs if a != b]

        print(f"\n{'=' * 68}\n噪声 {noise}："
              f"不同人格的偏好向量相似度 中位 {statistics.median(sims):.3f} "
              f"（越高越说明大家答出来都一样）")
        for name, count in top3.most_common(6):
            print(f"   {count / SAMPLES * 100:5.1f}%  ({count / expected:4.1f}×)  "
                  f"{by_name[name]['zh']}")


if __name__ == "__main__":
    main()
