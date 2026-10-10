#!/usr/bin/env python3
"""测量：五色 / 无色 / 多色主将目前能不能被匹配到。

现状是四道颜色题、每选项只给一个颜色（值 2），所以玩家的颜色向量至多
在 5 个轴上各有分布，无法表达「我就喜欢五色」或「我不在乎颜色」。
"""
from __future__ import annotations

import itertools
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

DATA = pathlib.Path(r"ROOT\data")
COLOR_Q = ["s49", "s59", "s60", "s62"]

quiz = load_quiz()
payload = load_commanders()
by_id = {q["id"]: q for q in quiz["questions"]}
by_color = Counter(c["colors"] for c in payload["commanders"])

print("=== 主将池的颜色身份分布 ===")
for code, n in by_color.most_common(14):
    label = {"C": "无色", "WUBRG": "五色"}.get(code, code)
    print(f"  {label:<8} {n:>3} 位")
print(f"  （共 {len(by_color)} 种颜色组合）")

# 颜色倾向公式的边界：五色/无色主将最多能拿多少颜色分？
print("\n=== 颜色契合度的理论上限 ===")
print("  公式 = Σ(玩家对该主将各色的偏好) / (最高偏好 × 颜色数)")


def affinity(colors_pref: dict, card_colors: str) -> float:
    max_color = max(colors_pref.values()) if colors_pref else 0.0
    if max_color == 0 or card_colors == "C":
        return 0.5
    return sum(colors_pref.get(c, 0.0) for c in card_colors) / (max_color * len(card_colors))


scenarios = {
    "只爱单色（白8）": {"W": 8.0},
    "爱两色（白蓝各8）": {"W": 8.0, "U": 8.0},
    "均匀爱五色（各8）": {c: 8.0 for c in "WUBRG"},
    "均衡散开（各1.6）": {c: 1.6 for c in "WUBRG"},
}
print(f"\n  {'玩家画像':<20} {'单色':>7} {'双色':>7} {'三色':>7} {'五色':>7} {'无色':>7}")
for label, pref in scenarios.items():
    row = [affinity(pref, "W"), affinity(pref, "WU"), affinity(pref, "WUG"),
           affinity(pref, "WUBRG"), "—"]
    print(f"  {label:<20} " + " ".join(f"{v:>7.2f}" if isinstance(v, float) else f"{v:>7}"
                                       for v in row))

# 实际答题：枚举四道颜色题的所有组合
print("\n=== 枚举颜色题的 5^4 = 625 种组合，看各色主将进前三的频率 ===")
combos = list(itertools.product(range(5), repeat=4))
top3_colors: Counter = Counter()
top1_colors: Counter = Counter()
rng = random.Random(20261010)

for combo in combos:
    answers = {}
    for qid, idx in zip(COLOR_Q, combo):
        answers[qid] = idx
    # 其余题随机填答，模拟「只有颜色题不同」
    for q in quiz["questions"]:
        if q["id"] in answers:
            continue
        n = len(q["opts"])
        answers[q["id"]] = ([rng.randrange(n) for _ in range(min(q.get("multi", 1), n))]
                            if q.get("multi") else rng.randrange(n))
    pref, colors, cons = tally(quiz, answers)
    results = score_commanders(payload, pref, colors, cons)
    for r in results[:3]:
        top3_colors[r["colors"]] += 1
    top1_colors[results[0]["colors"]] += 1

total3 = sum(top3_colors.values())
print(f"  前三位共 {total3} 个位置")
print(f"\n  {'颜色身份':<10} {'进前三':>8} {'占比':>7}   该色在池中占比")
for code, n in top3_colors.most_common(12):
    pool_share = by_color[code] / len(payload["commanders"])
    label = {"C": "无色", "WUBRG": "五色"}.get(code, code)
    print(f"  {label:<10} {n:>8} {n / total3 * 100:>6.1f}%   {pool_share * 100:>5.1f}%")

five = top3_colors.get("WUBRG", 0)
colorless = top3_colors.get("C", 0)
print(f"\n  五色主将进前三：{five} 次（{five / total3 * 100:.1f}%），"
      f"池中占比 {by_color['WUBRG'] / len(payload['commanders']) * 100:.1f}%")
print(f"  无色主将进前三：{colorless} 次（{colorless / total3 * 100:.1f}%），"
      f"池中占比 {by_color['C'] / len(payload['commander']) * 100:.1f}%"
      if False else
      f"  无色主将进前三：{colorless} 次（{colorless / total3 * 100:.1f}%），"
      f"池中占比 {by_color['C'] / len(payload['commanders']) * 100:.1f}%")
