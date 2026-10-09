#!/usr/bin/env python3
"""拆解「过度推荐」主将的得分构成：是余弦高，还是扣分少？"""
from __future__ import annotations

import math
import pathlib
import random
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import cosine, load_commanders, load_quiz, score_commanders, tally  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

DATA = pathlib.Path(ROOT / "data")
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 200
SEED = 20261009

SUSPECTS = ["Alexios, Deimos of Kosmos", "Vnwxt, Verbose Host", "Rendmaw, Creaking Nest",
            "Kynaios and Tiro of Meletis", "Alela, Artful Provocateur", "Ramos, Dragon Engine",
            "Tannuk, Memorial Ensign", "Queen Marchesa", "Kenrith, the Returned King"]


def random_unit(rng, axes):
    v = {axis: rng.gauss(0, 1) for axis in axes}
    n = math.sqrt(sum(x * x for x in v.values()))
    return {k: x / n for k, x in v.items()}


def main() -> None:
    quiz = load_quiz()
    payload = load_commanders()
    by_name = {c["en"]: c for c in payload["commanders"]}
    axes = sorted({a for c in payload["commanders"] for a in c["vec"]})
    rng = random.Random(SEED)

    print("=== 嫌疑主将的向量与静态属性 ===")
    for name in SUSPECTS:
        card = by_name.get(name)
        if not card:
            continue
        print(f"\n  {card['zh']}（{name}）")
        print(f"    轴数 {len(card['vec'])}  咸度 {card['salt']:.2f}  "
              f"难度 {card['difficulty']:.2f}  造价 {card['budget']}  "
              f"Bracket {card['bracket']}  套牌 {card['num_decks']}")
        print(f"    向量 {dict(sorted(card['vec'].items(), key=lambda kv: -kv[1]))}")

    # 跑样本，累计各主将的得分构成
    stats: dict[str, dict[str, float]] = {}
    all_rank: dict[str, list[int]] = {}
    for _ in range(SAMPLES):
        direction = random_unit(rng, axes)
        by_id = {q["id"]: q for q in quiz["questions"]}
        answers: dict = {}
        current = quiz["start"]
        guard = 0
        while current and guard < 600:
            q = by_id[current]
            n = len(q["opts"])
            scores = [sum((o.get("s") or {}).get(k, 0.0) * direction.get(k, 0.0)
                          for k in direction) + rng.gauss(0, 0.9) for o in q["opts"]]
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
        for rank, row in enumerate(results, 1):
            s = stats.setdefault(row["en"], {"sim": 0.0, "aff": 0.0, "pop": 0.0,
                                             "pen": 0.0, "score": 0.0, "n": 0})
            s["sim"] += row["sim"]
            s["aff"] += row["affinity"]
            s["pop"] += row["popularity"]
            s["pen"] += sum(row["pen"].values())
            s["score"] += row["score"]
            s["n"] += 1
            all_rank.setdefault(row["en"], []).append(rank)

    print(f"\n=== {SAMPLES} 个样本的平均得分构成（按平均得分排序）===")
    print(f"  {'主将':<18} {'得分':>7} {'余弦×0.6':>9} {'颜色×.14':>9} "
          f"{'流行×.08':>9} {'扣分':>7} {'平均名次':>8}")
    ordered = sorted(stats.items(), key=lambda kv: -kv[1]["score"] / kv[1]["n"])
    for name, s in ordered[:22]:
        n = s["n"]
        avg_rank = sum(all_rank[name]) / len(all_rank[name])
        print(f"  {by_name[name]['zh']:<18} {s['score'] / n:>7.4f} "
              f"{s['sim'] / n * 0.60:>9.4f} {s['aff'] / n * 0.14:>9.4f} "
              f"{s['pop'] / n * 0.08:>9.4f} {s['pen'] / n:>7.4f} {avg_rank:>8.1f}")

    print(f"\n=== 全池平均名次对照 ===")
    ranks = [sum(v) / len(v) for v in all_rank.values()]
    print(f"  全池平均名次 {sum(ranks) / len(ranks):.1f}"
          f"（均匀应为 {(len(payload['commanders']) + 1) / 2:.1f}）")


if __name__ == "__main__":
    main()
