#!/usr/bin/env python3
"""测各经验段的推荐集中度，以及「够得着」的主将池有多大。

如果新人档被难度与档位两道限制卡成一个很小的子集，
推荐必然集中在少数几位身上——这不是评分错，是候选池太小。
"""
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
rng = random.Random(777)
EXP_Q = "e0"

print("=== 各经验段「够得着」的主将有多少（不被扣大分的）===")
print(f"  {'经验段':<20} {'难度上限':>8} {'档位上限':>8} {'难度内':>7} {'档位内':>7} {'两者都内':>9}")
for exp in (1, 2, 3, 4):
    prof = EXP_PROFILE[exp]
    cc, bc = prof["complex_cap"], prof["bracket_cap"]
    diff_ok = [c for c in cmds if c["difficulty"] <= cc]
    br_ok = [c for c in cmds if int(c["bracket"]) <= bc]
    both = [c for c in cmds if c["difficulty"] <= cc and int(c["bracket"]) <= bc]
    print(f"  {prof['name']:<20} {cc:>8} {bc:>8} {len(diff_ok):>7} "
          f"{len(br_ok):>7} {len(both):>9}  ({len(both) / len(cmds) * 100:.0f}%)")


def unit():
    v = {ax: rng.gauss(0, 1) for ax in axes}
    n = math.sqrt(sum(x * x for x in v.values()))
    return {k: x / n for k, x in v.items()}


def sample(exp: int):
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


print(f"\n=== {SAMPLES} 个样本的推荐集中度 ===")
print(f"  {'经验段':<20} {'第一名种类':>10} {'前三种类':>10} {'最多重复':>9} {'前10占比':>9}")
for exp in (1, 2, 3, 4):
    top1: Counter = Counter()
    top3: Counter = Counter()
    for _ in range(SAMPLES):
        res = sample(exp)
        top1[res[0]["en"]] += 1
        for r in res[:3]:
            top3[r["en"]] += 1
    top10 = sum(c for _, c in top3.most_common(10))
    print(f"  {EXP_PROFILE[exp]['name']:<20} {len(top1):>10} {len(top3):>10} "
          f"{top1.most_common(1)[0][1]:>9} {top10 / (SAMPLES * 3) * 100:>8.0f}%")
    if exp == 1:
        print(f"      新人最常被推荐的 8 位：")
        for name, cnt in top1.most_common(8):
            print(f"        {cnt / SAMPLES * 100:>5.1f}%  {by_name[name]['zh']}"
                  f"（难度{by_name[name]['complexity']} B{by_name[name]['bracket']}）")
