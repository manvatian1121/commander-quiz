#!/usr/bin/env python3
"""一致性测试：用 JS 走流程得到的答案集，比对 Python 引擎的输出。"""
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
TOLERANCE = 5e-4


def main() -> int:
    quiz = load_quiz()
    payload = load_commanders()
    js_path = DATA / "js_results.json"
    if not js_path.exists():
        print("✗ 缺少 js_results.json，请先运行 parity_js.mjs")
        return 1
    js = json.loads(js_path.read_text(encoding="utf-8"))

    problems: list[str] = []
    for name, record in js["sets"].items():
        answers = dict(record["answers"])
        pref, colors, cons = tally(quiz, answers)
        results = score_commanders(payload, pref, colors, cons)
        py_top = [(r["en"], round(r["score"], 4)) for r in results[:12]]
        js_top = [(r["en"], r["score"]) for r in record["top"]]

        print(f"\n【{name}】走了 {record['steps']} 题")
        print(f"  约束  py={ {k: round(v, 4) for k, v in cons.items()} }  "
              f"js={record['constraints']}")
        print(f"  {'#':<3}{'主将':<38}{'Python':>10}{'JS':>10}  状态")
        for index, (py, jsv) in enumerate(zip(py_top, js_top), 1):
            same, close = py[0] == jsv[0], abs(py[1] - jsv[1]) < TOLERANCE
            if not (same and close):
                problems.append(f"{name} 第{index}名：py={py} js={jsv}")
            print(f"  {index:<3}{py[0][:37]:<38}{py[1]:>10.4f}{jsv[1]:>10.4f}  "
                  f"{'✓' if same and close else '✗'}")

        for key, value in cons.items():
            if abs(round(value, 4) - record["constraints"][key]) > TOLERANCE:
                problems.append(f"{name} 约束 {key} 不一致：py={value} "
                                f"js={record['constraints'][key]}")

        js_scores = record.get("scores") or {}
        diffs = [(abs(r["score"] - js_scores[r["en"]]), r["en"])
                 for r in results if r["en"] in js_scores]
        bad = sorted([d for d in diffs if d[0] > 1e-6], reverse=True)
        if bad:
            problems.append(f"{name} 有 {len(bad)} 位分数不一致，最大差 {bad[0][0]:.6f}"
                            f"（{bad[0][1]}）")

    print("\n" + "=" * 70)
    if problems:
        print(f"✗ 发现 {len(problems)} 处不一致：")
        for item in problems[:12]:
            print(f"  - {item}")
        return 1
    print("✓ 两个引擎完全一致（排名与分数均在容差内）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
