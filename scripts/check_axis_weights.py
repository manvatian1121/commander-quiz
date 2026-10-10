#!/usr/bin/env python3
"""量化题库的轴权重分布：每个玩法轴在全部选项里一共给了多少分。"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")


def main() -> None:
    quiz = json.loads((DATA / "questions.json").read_text(encoding="utf-8"))
    pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))

    total: Counter = Counter()
    count: Counter = Counter()
    for q in quiz["questions"]:
        for opt in q["opts"]:
            for axis, value in (opt.get("s") or {}).items():
                total[axis] += value
                count[axis] += 1

    axes = sorted(total, key=lambda a: -total[a])
    grand = sum(total.values())
    print(f"=== 题库轴权重总量（合计 {grand:.0f} 分，{len(axes)} 个轴）===")
    print(f"  {'轴':<11} {'总权重':>8} {'占比':>7} {'出现次数':>8} {'与均匀比':>9}")
    uniform = grand / len(axes)
    for axis in axes:
        ratio = total[axis] / uniform
        bar = "█" * int(ratio * 12)
        print(f"  {axis:<11} {total[axis]:>8.1f} {total[axis] / grand * 100:>6.1f}% "
              f"{count[axis]:>8} {ratio:>8.2f}× {bar}")

    # 对照：主将池里各轴的权重总量
    pool_total: Counter = Counter()
    for card in pool["commanders"]:
        for axis, value in card["vec"].items():
            pool_total[axis] += value
    print(f"\n=== 主将池的轴权重总量（对照）===")
    pool_grand = sum(pool_total.values())
    pool_uniform = pool_grand / len(axes)
    for axis in axes:
        ratio = pool_total[axis] / pool_uniform
        print(f"  {axis:<11} {pool_total[axis]:>8.1f} {ratio:>8.2f}×")

    print(f"\n=== 错配诊断 ===")
    print("  题库占比 ÷ 主将池占比（<1 表示这个口味在题库里说得少、可选主将却不少）")
    for axis in axes:
        q_share = total[axis] / grand
        p_share = pool_total[axis] / pool_grand
        gap = q_share / p_share if p_share else 0
        flag = ""
        if gap < 0.5:
            flag = "  ← 题库说得太少"
        elif gap > 1.8:
            flag = "  ← 题库说得太多"
        print(f"  {axis:<11} 题库 {q_share * 100:>5.1f}%  池子 {p_share * 100:>5.1f}%  "
              f"{gap:>6.2f}{flag}")


if __name__ == "__main__":
    main()
