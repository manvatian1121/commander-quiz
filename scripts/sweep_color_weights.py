#!/usr/bin/env python3
"""参数扫描：找出让「五色/无色」口味真正生效的权重配置。

评价指标（都是「越高越对」）：
  ① 五色爱好者拿到五色主将的比例
  ② 无色爱好者拿到无色主将的比例
  ③ 单色爱好者拿到单色主将的比例（不能被牺牲掉）
  ④ 五个颜色身份的触达是否接近池中占比（过度集中的反向指标）
"""
from __future__ import annotations

import pathlib
import random
import sys
from collections import Counter


# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import engine  # noqa: E402

DATA = pathlib.Path(r"ROOT\data")
COLOR_Q = ["s49", "s59", "s60", "s62"]
BREADTH_Q = "s62b"
rng = random.Random(99)

quiz = engine.load_quiz()
payload = engine.load_commanders()
by_color = Counter(c["colors"] for c in payload["commanders"])
total_cmds = len(payload["commanders"])
# 预先生成一批随机答题底本（颜色题与广度题除外），保证各配置跑的是同一批人
BASE: list[dict] = []
for _ in range(60):
    answers = {}
    for q in quiz["questions"]:
        if q["id"] in COLOR_Q or q["id"] == BREADTH_Q:
            continue
        n = len(q["opts"])
        answers[q["id"]] = ([rng.randrange(n) for _ in range(min(q.get("multi", 1), n))]
                            if q.get("multi") else rng.randrange(n))
    BASE.append(answers)

CONFIGS = [
    ("现状 0.14 / 60:40", 0.14, 0.60, 0.40),
    ("提高颜色权重 0.20 / 60:40", 0.20, 0.60, 0.40),
    ("提高颜色权重 0.20 / 50:50", 0.20, 0.50, 0.50),
    ("大幅提高 0.26 / 50:50", 0.26, 0.50, 0.50),
    ("只调配比 0.14 / 45:55", 0.14, 0.45, 0.55),
]


def run(w_color: float, w_match: float, w_breadth: float) -> dict:
    engine.W_COLOR, engine.W_COLOR_MATCH, engine.W_BREADTH_MATCH = w_color, w_match, w_breadth
    stats = {i: Counter() for i in range(5)}
    overall: Counter = Counter()
    for breadth_idx in range(5):
        for base in BASE:
            answers = dict(base)
            answers[BREADTH_Q] = breadth_idx
            for qid in COLOR_Q:
                answers[qid] = rng.randrange(5)
            pref, colors, cons = engine.tally(quiz, answers)
            top = engine.score_commanders(payload, pref, colors, cons)[:3]
            for r in top:
                stats[breadth_idx][r["colors"]] += 1
                overall[r["colors"]] += 1
    n = len(BASE) * 3
    return {
        "five_for_five": stats[3].get("WUBRG", 0) / n,
        "none_for_none": stats[4].get("C", 0) / n,
        "mono_for_mono": sum(v for k, v in stats[0].items() if len(k) == 1) / n,
        "overall": overall,
        "grand": sum(overall.values()),
    }


print(f"{'配置':<26} {'五色口味拿到五色':>16} {'无色口味拿到无色':>16} {'单色口味拿到单色':>16}")
print("-" * 82)
results = {}
for label, wc, wm, wb in CONFIGS:
    r = run(wc, wm, wb)
    results[label] = r
    print(f"{label:<26} {r['five_for_five'] * 100:>15.1f}% "
          f"{r['none_for_none'] * 100:>15.1f}% {r['mono_for_mono'] * 100:>15.1f}%")

print(f"\n{'配置':<26} {'五色总占比':>10} {'池中':>7} {'倍数':>7} {'无色占比':>9} {'单绿占比':>9}")
print("-" * 82)
for label, r in results.items():
    g = r["grand"]
    five = r["overall"].get("WUBRG", 0) / g * 100
    none = r["overall"].get("C", 0) / g * 100
    gmono = r["overall"].get("G", 0) / g * 100
    print(f"{label:<26} {five:>9.1f}% {by_color['WUBRG'] / total_cmds * 100:>6.1f}% "
          f"{five / (by_color['WUBRG'] / total_cmds * 100):>6.2f}× "
          f"{none:>8.1f}% {gmono:>8.1f}%")
