#!/usr/bin/env python3
"""按经验段分开测：杀戮女郎的过度推荐是不是来自「惩罚少」。"""
from __future__ import annotations

import math
import pathlib
import random
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, load_quiz, score_commanders, tally  # noqa: E402

TARGET = "Massacre Girl, Known Killer"
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 120

quiz = load_quiz()
payload = load_commanders()
by_name = {c["en"]: c for c in payload["commanders"]}
axes = sorted({a for c in payload["commanders"] for a in c["vec"]})
by_id = {q["id"]: q for q in quiz["questions"]}
rng = random.Random(20261013)
total = len(payload["commanders"])
EXP_Q = "e0"


def unit(rng):
    v = {ax: rng.gauss(0, 1) for ax in axes}
    n = math.sqrt(sum(x * x for x in v.values()))
    return {k: x / n for k, x in v.items()}


print(f"{'经验段':<20} {'进前三':>8} {'占比':>7} {'倍数':>7}")
print("-" * 48)
for exp, label in ((1, "完全新人"), (2, "玩过牌没打过EDH"),
                   (3, "打过一阵"), (4, "老手")):
    hits = 0
    slots = 0
    for _ in range(SAMPLES):
        d = unit(rng)
        answers = {EXP_Q: exp - 1}          # 强制该经验段
        cur = quiz["start"]
        guard = 0
        while cur and guard < 600:
            q = by_id[cur]
            if q["id"] == EXP_Q:
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
        res = score_commanders(payload, pref, colors, cons)
        slots += 3
        hits += sum(1 for r in res[:3] if r["en"] == TARGET)
    exp3 = SAMPLES * 3 / total
    print(f"  {label:<18} {hits:>6}/{slots:<4} {hits / slots * 100:>6.1f}% "
          f"{hits / exp3:>6.1f}×")

print(f"\n均匀预期：每位主将进前三 {SAMPLES * 3 / total:.1f} 次"
      f"（{SAMPLES * 3 / total / (SAMPLES * 3) * 100:.2f}%）")
