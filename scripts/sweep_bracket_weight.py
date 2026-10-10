#!/usr/bin/env python3
"""扫描档位权重：老手该被多强地拉向高强度？

池子里 B4+B5 只占 7.9%，所以「老手偏好高强度」最多只能把推荐推到这一小撮上。
权重太低 → 老手对强度无感（现状）；太高 → 为了强度牺牲玩法契合度。
同时报告玩法契合度（余弦），确保没把核心指标压垮。
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

SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 120

quiz = engine.load_quiz()
payload = engine.load_commanders()
cmds = payload["commanders"]
by_name = {c["en"]: c for c in cmds}
axes = sorted({a for c in cmds for a in c["vec"]})
by_id = {q["id"]: q for q in quiz["questions"]}
EXP_Q = "e0"
pool_avg = sum(int(c["bracket"]) for c in cmds) / len(cmds)

CONFIGS = [
    ("现状 0.025 定权", 4.4, {1: 0.025, 2: 0.025, 3: 0.025, 4: 0.025}),
    ("0.025 / 老手 0.045", 4.6, {1: 0.025, 2: 0.030, 3: 0.038, 4: 0.045}),
    ("0.025 / 老手 0.070", 4.6, {1: 0.025, 2: 0.038, 3: 0.054, 4: 0.070}),
    ("0.020 / 老手 0.100", 4.8, {1: 0.020, 2: 0.045, 3: 0.072, 4: 0.100}),
]


def run(pbr_map, target4):
    old_prof = dict(engine.EXP_PROFILE)
    old_p = engine.P_BRACKET
    targets = {1: 2.0, 2: 2.7, 3: 3.6, 4: target4}
    for lvl in (1, 2, 3, 4):
        engine.EXP_PROFILE[lvl] = dict(engine.EXP_PROFILE[lvl],
                                       bracket_target=targets[lvl])
    out = {}
    for exp in (1, 4):
        engine.P_BRACKET = pbr_map[exp]
        rng = random.Random(31337)
        brs = Counter()
        sims = []
        for _ in range(SAMPLES):
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
            pref, colors, cons = engine.tally(quiz, answers)
            res = engine.score_commanders(payload, pref, colors, cons)
            brs[int(by_name[res[0]["en"]]["bracket"])] += 1
            sims.append(res[0]["sim"])
        out[exp] = {
            "avg": sum(b * n for b, n in brs.items()) / SAMPLES,
            "hi": (brs[4] + brs[5]) / SAMPLES * 100,
            "sim": sum(sims) / len(sims),
        }
    engine.EXP_PROFILE = old_prof
    engine.P_BRACKET = old_p
    return out


print(f"池子平均档位 {pool_avg:.2f}　B4+B5 占池 {sum(1 for c in cmds if int(c['bracket']) >= 4) / len(cmds) * 100:.1f}%\n")
print(f"  {'配置':<22} {'新人均档':>8} {'老手均档':>8} {'老手B4+5':>9} {'老手余弦':>8}")
print("  " + "-" * 62)
for label, t4, pmap in CONFIGS:
    r = run(pmap, t4)
    print(f"  {label:<22} {r[1]['avg']:>8.2f} {r[4]['avg']:>8.2f} "
          f"{r[4]['hi']:>8.0f}% {r[4]['sim']:>8.3f}")
