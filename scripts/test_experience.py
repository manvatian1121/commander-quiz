#!/usr/bin/env python3
"""验证「接触时长」确实切换了评分标准：同样的答案、只改第 1 题，看推荐如何变化。"""
from __future__ import annotations

import json
import pathlib
import sys


# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import (EXP_PROFILE, load_commanders, load_quiz,  # noqa: E402

                    score_commanders, tally)

DATA = pathlib.Path(ROOT / "data")


def walk(quiz: dict, exp_index: int, pick) -> dict:
    """按 goto/next 走一遍流程，返回答案字典。exp_index 是第 1 题（e0）的选项。"""
    by_id = {q["id"]: q for q in quiz["questions"]}
    answers: dict = {}
    current = quiz["start"]
    guard = 0
    while current and guard < 600:
        q = by_id[current]
        idx = exp_index if q["id"] == "e0" else pick(q, guard) % len(q["opts"])
        if q.get("multi"):
            count = min(q["multi"], len(q["opts"]))
            answers[q["id"]] = [(idx + c) % len(q["opts"]) for c in range(count)]
            nxt = q.get("next")
        else:
            answers[q["id"]] = idx
            opt = q["opts"][idx]
            nxt = opt.get("goto") or q.get("next")
        current = nxt
        guard += 1
    return answers


def main() -> None:
    quiz = load_quiz()
    payload = load_commanders()
    by_name = {c["en"]: c for c in payload["commanders"]}

    for picker_name, pick in (("每题选 B", lambda q, s: 1), ("每题选 C", lambda q, s: 2)):
        print(f"\n{'=' * 78}\n【{picker_name}】")
        for exp_index in range(4):
            answers = walk(quiz, exp_index, pick)
            pref, colors, cons = tally(quiz, answers)
            results = score_commanders(payload, pref, colors, cons)
            prof = EXP_PROFILE[cons["exp"]]
            top = results[:5]
            print(f"\n  ── 经验段 {cons['exp']}（{prof['name']}）"
                  f"　难度容忍上限 {prof['complex_cap']}　Bracket 上限 {prof['bracket_cap']}")
            print(f"     作答题数 {len(answers)}　"
                  f"实得约束 复杂度 {cons['complex']:.2f} / 预算 {cons['budget']:.2f} "
                  f"/ 咸度 {cons['salt']:.2f}")
            for i, r in enumerate(top, 1):
                card = by_name[r["en"]]
                pen = r["pen"]
                print(f"     {i}. {card['zh']:<14} 难度{card['difficulty']:<5} "
                      f"B{card['bracket']}  {r['score']:.4f}"
                      f"　(难度扣 {pen['cost']:.3f} / 档位扣 {pen['bracket']:.3f})")

    # 汇总：新人与老手的推荐差异有多大
    print(f"\n{'=' * 78}\n【新人 vs 老手的推荐重合度】")
    for picker_name, pick in (("选 B", lambda q, s: 1), ("选 C", lambda q, s: 2),
                              ("选 D", lambda q, s: 3)):
        sets = []
        for exp_index in (0, 3):
            answers = walk(quiz, exp_index, pick)
            pref, colors, cons = tally(quiz, answers)
            results = score_commanders(payload, pref, colors, cons)
            sets.append({r["en"] for r in results[:5]})
        overlap = len(sets[0] & sets[1])
        print(f"  {picker_name}：前五重合 {overlap}/5"
              f"{'  ← 差异明显，评分标准确实生效' if overlap <= 2 else ''}")


if __name__ == "__main__":
    main()
