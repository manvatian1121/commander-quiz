#!/usr/bin/env python3
"""决定性测量：喜欢某种玩法的人，到底拿不拿得到那种玩法的主将？

对每个「人格」样本，看它抽到的口味方向主导轴，与最终推荐主将的主导轴是否一致。
一致率高 = 引擎真的把对的人配给了对的主将。
"""
from __future__ import annotations

import math
import pathlib
import random
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, load_quiz, score_commanders, tally  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

DATA = pathlib.Path(ROOT / "data")
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 400
NOISE = float(sys.argv[2]) if len(sys.argv) > 2 else 0.3
SEED = 20261009


def random_unit(rng, axes):
    v = {axis: rng.gauss(0, 1) for axis in axes}
    n = math.sqrt(sum(x * x for x in v.values()))
    return {k: x / n for k, x in v.items()}


def main() -> None:
    quiz = load_quiz()
    payload = load_commanders()
    by_name = {c["en"]: c for c in payload["commanders"]}
    axes = sorted({a for c in payload["commanders"] for a in c["vec"]})
    by_id = {q["id"]: q for q in quiz["questions"]}
    rng = random.Random(SEED)

    agree = 0
    per_axis: dict[str, list[int]] = defaultdict(list)
    for _ in range(SAMPLES):
        direction = random_unit(rng, axes)
        want = max(direction, key=lambda k: direction[k])
        answers: dict = {}
        current = quiz["start"]
        guard = 0
        while current and guard < 600:
            q = by_id[current]
            n = len(q["opts"])
            scores = [sum((o.get("s") or {}).get(k, 0.0) * direction.get(k, 0.0)
                          for k in direction) + rng.gauss(0, NOISE) for o in q["opts"]]
            if q.get("multi"):
                order = sorted(range(n), key=lambda i: -scores[i])
                answers[q["id"]] = order[:min(q["multi"], n)]
                nxt = q.get("next")
            else:
                idx = max(range(n), key=lambda i: scores[i])
                answers[q["id"]] = idx
                nxt = q["opts"][idx].get("goto") or q.get("next")
            current = nxt
            guard += 1
        pref, colors, cons = tally(quiz, answers)
        results = score_commanders(payload, pref, colors, cons)
        got_card = by_name[results[0]["en"]]
        got = max(got_card["vec"], key=lambda k: got_card["vec"][k])
        hit = 1 if got == want else 0
        agree += hit
        per_axis[want].append(hit)

    print(f"=== {SAMPLES} 个样本（噪声 {NOISE}）：想玩 X 的人拿到 X 主将的比例 ===")
    print(f"  总体命中率 {agree / SAMPLES * 100:.1f}%"
          f"（随机猜是 {100 / len(axes):.1f}%）\n")
    for axis in axes:
        tries = per_axis.get(axis, [])
        if not tries:
            print(f"  {axis:<11}   样本 0")
            continue
        rate = sum(tries) / len(tries) * 100
        bar = "█" * int(rate / 4)
        print(f"  {axis:<11} 样本 {len(tries):>3}  命中 {rate:>5.1f}%  {bar}")

    top = Counter()
    for _ in range(0):
        pass
    print(f"\n=== 各轴命中率排序 ===")
    ranked = sorted(((sum(v) / len(v), a) for a, v in per_axis.items() if v), reverse=True)
    for rate, axis in ranked:
        print(f"  {rate * 100:5.1f}%  {axis}")


if __name__ == "__main__":
    main()
