#!/usr/bin/env python3
"""验证「老手偏好高强度」：各经验段拿到的主将强度档位分布。"""
from __future__ import annotations

import math
import pathlib
import random
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import EXP_PROFILE, load_commanders, load_quiz, score_commanders, tally  # noqa: E402

SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 150

quiz = load_quiz()
payload = load_commanders()
cmds = payload["commanders"]
by_name = {c["en"]: c for c in cmds}
axes = sorted({a for c in cmds for a in c["vec"]})
by_id = {q["id"]: q for q in quiz["questions"]}
EXP_Q = "e0"


def sample(exp: int, rng):
    def unit():
        v = {ax: rng.gauss(0, 1) for ax in axes}
        n = math.sqrt(sum(x * x for x in v.values()))
        return {k: x / n for k, x in v.items()}
    d = unit()
    answers = {}
    cur = quiz["start"]
    guard = 0
    while cur and guard < 600:
        q = by_id[cur]
        if q["id"] == EXP_Q:
            answers[q["id"]] = exp - 1
            cur = q["opts"][exp - 1].get("goto") or q.get("next")
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
    pref, colors, cons = tally(quiz, answers)
    return score_commanders(payload, pref, colors, cons)


# 同一个种子 → 四档看到的是同一批口味，差异只来自经验门槛
rng = random.Random(31337)
print(f"{SAMPLES} 个口味样本 × 4 个经验段（同一批口味，只改第 1 题答案）\n")
print(f"  {'经验段':<20} {'目标档':>6} {'平均档位':>8} {'B1':>5} {'B2':>5} "
      f"{'B3':>5} {'B4':>5} {'B5':>5} {'B4+5占比':>9}")
print("  " + "-" * 74)
rows = {}
for exp in (1, 2, 3, 4):
    rng2 = random.Random(31337)          # 每档重置，保证口味相同
    brs = Counter()
    tot = 0
    for _ in range(SAMPLES):
        res = sample(exp, rng2)
        b = int(by_name[res[0]["en"]]["bracket"])
        brs[b] += 1
        tot += b
    prof = EXP_PROFILE[exp]
    hi = (brs[4] + brs[5]) / SAMPLES * 100
    print(f"  {prof['name']:<20} {prof['bracket_target']:>6.1f} {tot / SAMPLES:>8.2f} "
          f"{brs[1] / SAMPLES * 100:>4.0f}% {brs[2] / SAMPLES * 100:>4.0f}% "
          f"{brs[3] / SAMPLES * 100:>4.0f}% {brs[4] / SAMPLES * 100:>4.0f}% "
          f"{brs[5] / SAMPLES * 100:>4.0f}% {hi:>8.0f}%")
    rows[exp] = brs

print("\n池中各档位的占比（基准）")
base = Counter(int(c["bracket"]) for c in cmds)
for b in sorted(base):
    print(f"    B{b}: {base[b] / len(cmds) * 100:>5.1f}%", end="")
print()
