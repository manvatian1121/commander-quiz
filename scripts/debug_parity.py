#!/usr/bin/env python3
"""精确定位两引擎的分歧：用 JS 走出来的答案集，逐位主将比对分数与分项。"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, load_quiz, score_commanders, tally  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

DATA = pathlib.Path(ROOT / "data")


def main() -> None:
    quiz = load_quiz()
    payload = load_commanders()
    js = json.loads((DATA / "js_results.json").read_text(encoding="utf-8"))
    by_name = {c["en"]: c for c in payload["commanders"]}

    only = sys.argv[1] if len(sys.argv) > 1 else None

    for name, record in js["sets"].items():
        if only and name != only:
            continue
        answers = dict(record["answers"])
        pref, colors, cons = tally(quiz, answers)
        results = score_commanders(payload, pref, colors, cons)
        js_scores = record.get("scores") or {}

        diffs = sorted(((abs(r["score"] - js_scores[r["en"]]), r) for r in results
                        if r["en"] in js_scores), key=lambda x: -x[0])
        bad = [(d, r) for d, r in diffs if d > 1e-6]
        print(f"\n【{name}】分歧 {len(bad)} 位，最大差 {(bad[0][0] if bad else 0):.6f}")
        if not bad:
            continue

        worst = bad[0][1]
        card = by_name[worst["en"]]
        print(f"\n  分歧最大的「{worst['en']}」")
        print(f"    颜色身份 = {card['colors']!r}（长度 {len(card['colors'])}）")
        print(f"    玩家颜色倾向 = {colors}")
        print(f"    py 总分 = {worst['score']:.6f}   js 总分 = {js_scores[worst['en']]:.6f}")
        print(f"    py 分项：sim={worst['sim']:.6f} affinity={worst['affinity']:.6f} "
              f"popularity={worst['popularity']:.6f} pen={worst['pen']}")
        print(f"    complexity={worst['complexity']} difficulty={card.get('difficulty')} "
              f"budget={worst['budget']} salt={worst['salt']}")
        print(f"    约束 = {cons}")

        # 列出所有分歧主将的颜色身份，找规律
        print("\n  分歧主将的颜色身份分布：")
        from collections import Counter
        kinds = Counter(by_name[r["en"]]["colors"] for _, r in bad)
        for colors_str, count in kinds.most_common(12):
            print(f"    {colors_str:<8} {count} 位")
        # 无分歧的对照
        good = [(d, r) for d, r in diffs if d <= 1e-6]
        good_kinds = Counter(by_name[r["en"]]["colors"] for _, r in good)
        print("  无分歧主将的颜色身份分布：")
        for colors_str, count in good_kinds.most_common(12):
            print(f"    {colors_str:<8} {count} 位")


if __name__ == "__main__":
    main()
