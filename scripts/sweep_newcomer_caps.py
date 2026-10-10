#!/usr/bin/env python3
"""参数扫描：放宽新人的难度/档位上限，看推荐多样性如何变化。

不能只看多样性——还要看放开之后推荐的主将会不会变太难。
所以同时报告：推荐主将的平均难度、以及有多少比例是可接受的。
"""
from __future__ import annotations

import math
import pathlib
import random
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import engine  # noqa: E402

SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 150

quiz = engine.load_quiz()
payload = engine.load_commanders()
cmds = payload["commanders"]
by_name = {c["en"]: c for c in cmds}
axes = sorted({a for c in cmds for a in c["vec"]})
by_id = {q["id"]: q for q in quiz["questions"]}
EXP_Q = "e0"

CONFIGS = [
    ("现状 1.6 / B2", 1.6, 2),
    ("2.0 / B2", 2.0, 2),
    ("2.2 / B3", 2.2, 3),
    ("2.6 / B3", 2.6, 3),
    ("3.0 / B3", 3.0, 3),
]


def run(cc: float, bc: int, seed: int = 4242):
    prof = engine.EXP_PROFILE[1]
    engine.EXP_PROFILE[1] = dict(prof, complex_cap=cc, bracket_cap=bc)
    rng = random.Random(seed)

    def unit():
        v = {ax: rng.gauss(0, 1) for ax in axes}
        n = math.sqrt(sum(x * x for x in v.values()))
        return {k: x / n for k, x in v.items()}

    top1: Counter = Counter()
    top3: Counter = Counter()
    diffs = []
    for _ in range(SAMPLES):
        d = unit()
        answers = {}
        cur = quiz["start"]
        guard = 0
        while cur and guard < 600:
            q = by_id[cur]
            if q["id"] == EXP_Q:
                answers[q["id"]] = 0
                cur = q["opts"][0].get("goto") or q.get("next")
                guard += 1
                continue
            n = len(q["opts"])
            sc = [sum((o.get("s") or {}).get(k, 0.0) * d.get(k, 0.0) for k in d)
                  + rng.gauss(0, 0.3) for o in q["opts"]]
            if q.get("multi"):
                order = sorted(range(n), key=lambda i: -sc[i])
                answers[q["id"]] = order[:min(q["multi"], n)]
                cur = q.get("next")
            else:
                idx = max(range(n), key=lambda i: sc[i])
                answers[q["id"]] = idx
                cur = q["opts"][idx].get("goto") or q.get("next")
            guard += 1
        pref, colors, cons = engine.tally(quiz, answers)
        res = engine.score_commanders(payload, pref, colors, cons)
        top1[res[0]["en"]] += 1
        for r in res[:3]:
            top3[r["en"]] += 1
        diffs.append(by_name[res[0]["en"]]["difficulty"])
    engine.EXP_PROFILE[1] = prof
    diffs.sort()
    return {
        "top1_kinds": len(top1),
        "top3_kinds": len(top3),
        "top10_share": sum(c for _, c in top3.most_common(10)) / (SAMPLES * 3),
        "max_repeat": top1.most_common(1)[0][1] / SAMPLES,
        "diff_med": diffs[len(diffs) // 2],
        "diff_p90": diffs[int(len(diffs) * 0.9)],
        "top8": top1.most_common(8),
    }


HARD = 3.5   # 难度连续值超过这个数算「对新人不友好」
print(f"{SAMPLES} 个新人样本（经验段固定为完全新人）\n")
print(f"  {'配置':<16} {'第一名种类':>9} {'前三种类':>9} {'前10占比':>9} "
      f"{'最高重复':>9} {'难度中位':>9} {'难度P90':>8}")
print("  " + "-" * 78)
results = {}
for label, cc, bc in CONFIGS:
    r = run(cc, bc)
    results[label] = r
    print(f"  {label:<16} {r['top1_kinds']:>9} {r['top3_kinds']:>9} "
          f"{r['top10_share'] * 100:>8.0f}% {r['max_repeat'] * 100:>8.1f}% "
          f"{r['diff_med']:>9.2f} {r['diff_p90']:>8.2f}")

print("\n=== 各配置下新人最常拿到的 6 位 ===")
for label, r in results.items():
    names = "、".join(f"{by_name[n]['zh']}({c / SAMPLES * 100:.0f}%)"
                     for n, c in r["top8"][:6])
    print(f"  {label:<16} {names}")
