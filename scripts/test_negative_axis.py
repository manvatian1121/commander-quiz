#!/usr/bin/env python3
"""验证：某个轴为负时，引擎会不会错误推荐该轴的主将。

复现用户截图的口味画像：吸血消耗 100%、随机搞事 96%、精准互动 76%、
控制反击 62%、锁场剥夺 8%、铺场爆兵 -4%。
"""
from __future__ import annotations

import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, score_commanders  # noqa: E402

payload = load_commanders()
by_name = {c["en"]: c for c in payload["commanders"]}

# 按截图的比例还原成中心化后的偏好向量（最强者为 1.0）
PROFILE = {
    "drain": 1.00, "chaos": 0.96, "removal": 0.76,
    "control": 0.62, "stax": 0.08, "wide": -0.04,
}
NEUTRAL = {"complex": 3.5, "budget": 3.5, "salt": 3.0, "exp": 3}

print("=== 输入画像 ===")
for axis, value in PROFILE.items():
    print(f"  {axis:<11} {value:+.2f}")

results = score_commanders(payload, dict(PROFILE), {}, dict(NEUTRAL))

print("\n=== 引擎推荐的前 8 位 ===")
print(f"  {'主将':<20} {'总分':>7} {'余弦':>7}  该主将最强的三个轴")
for row in results[:8]:
    card = by_name[row["en"]]
    top3 = sorted(card["vec"].items(), key=lambda kv: -kv[1])[:3]
    desc = "、".join(f"{a} {v:.1f}" for a, v in top3)
    print(f"  {card['zh']:<20} {row['score']:>7.4f} {row['sim']:>7.4f}  {desc}")

print("\n=== 结论 ===")
wide_in_top8 = [r for r in results[:8] if by_name[r["en"]]["vec"].get("wide", 0) >= 2.0]
print(f"  前八里「铺场爆兵」达到 2.0 以上的：{len(wide_in_top8)} 位")
for row in wide_in_top8:
    card = by_name[row["en"]]
    print(f"    {card['zh']}（wide {card['vec']['wide']:.2f}）")

# 反证：把 wide 从 -0.04 提到 +1.00，排名会怎么变？
higher = dict(PROFILE, wide=1.00)
alt = score_commanders(payload, higher, {}, dict(NEUTRAL))
print(f"\n  对照：把「铺场爆兵」从 -0.04 改成 +1.00 后的前三：")
for row in alt[:3]:
    print(f"    {by_name[row['en']]['zh']}")
print(f"\n  原画像的前三：")
for row in results[:3]:
    print(f"    {by_name[row['en']]['zh']}")
