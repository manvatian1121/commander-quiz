#!/usr/bin/env python3
"""测某位主将是否被过度推荐。

用法：python diagnose_one.py "Massacre Girl, Known Killer"
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

TARGET = sys.argv[1] if len(sys.argv) > 1 else "Massacre Girl, Known Killer"
SAMPLES = int(sys.argv[2]) if len(sys.argv) > 2 else 300

quiz = load_quiz()
payload = load_commanders()
by_name = {c["en"]: c for c in payload["commanders"]}
total = len(payload["commanders"])

card = by_name.get(TARGET)
if not card:
    print(f"✗ 池子里没有 {TARGET}")
    sys.exit(1)

print(f"=== {card['zh']}（{TARGET}）===")
print(f"  颜色 {card['colors']}　难度 {card['complexity']}（连续值 {card['difficulty']:.2f}）"
      f"　造价 {card['budget']}　咸度 {card['salt']:.2f}　Bracket {card['bracket']}")
print(f"  套牌 {card['num_decks']:,}　历史第 {card['all_time_rank']} 位")
print(f"  向量（{len(card['vec'])} 个轴）：")
for axis, val in sorted(card["vec"].items(), key=lambda kv: -kv[1]):
    print(f"      {axis:<12} {val:.2f}")
norm = math.sqrt(sum(v * v for v in card["vec"].values()))
print(f"  向量模长 {norm:.2f}　轴数 {len(card['vec'])}")
pool_norms = [math.sqrt(sum(v * v for v in c["vec"].values())) for c in payload["commanders"]]
pool_norms.sort()
print(f"  池中模长中位数 {pool_norms[len(pool_norms) // 2]:.2f}　"
      f"她的百分位 {sum(1 for n in pool_norms if n < norm) / len(pool_norms) * 100:.0f}%")

axes = sorted({a for c in payload["commanders"] for a in c["vec"]})
by_id = {q["id"]: q for q in quiz["questions"]}
rng = random.Random(20261013)


def random_unit(rng, axes):
    v = {ax: rng.gauss(0, 1) for ax in axes}
    n = math.sqrt(sum(x * x for x in v.values()))
    return {k: x / n for k, x in v.items()}


top1 = 0
top3 = 0
total_slots = 0
others: Counter = Counter()
scores: list[float] = []

for _ in range(SAMPLES):
    d = random_unit(rng, axes)
    answers = {}
    cur = quiz["start"]
    guard = 0
    while cur and guard < 600:
        q = by_id[cur]
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
    total_slots += 3
    top1 += (res[0]["en"] == TARGET)
    top3 += sum(1 for r in res[:3] if r["en"] == TARGET)
    for r in res[:3]:
        others[r["en"]] += 1
    scores.append(1 if res[0]["en"] == TARGET else 0)

exp3 = SAMPLES * 3 / total
print(f"\n=== {SAMPLES} 个「口味明确」样本 ===")
print(f"  排第一      {top1:>4} 次（{top1 / SAMPLES * 100:.1f}%）")
print(f"  进前三      {top3:>4} 次（{top3 / total_slots * 100:.1f}%）")
print(f"  均匀预期    进前三 {exp3:.1f} 次（{exp3 / total_slots * 100:.2f}%），"
      f"即 {top3 / exp3 if exp3 else 0:.1f} 倍")
print(f"\n  进前三最多的其它主将：")
for name, cnt in others.most_common(8):
    if name == TARGET:
        continue
    print(f"      {cnt / total_slots * 100:>5.1f}%  {by_name[name]['zh']}")
