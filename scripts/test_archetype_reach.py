#!/usr/bin/env python3
"""测「武具思路」与「部族思路」能否被这套测试表达并匹配到。

武具在玩法轴上对应 voltron（主将单挑）+ artifacts（神器）；
部族对应 tribal。

要回答三个问题：
  ① 题库里有没有足够多的选项承载这些轴？（答得出来吗）
  ② 这些轴能否成为某人偏好向量的主导轴？
  ③ 擅长这些思路的主将，能否进入推荐？
"""
from __future__ import annotations

import json
import math
import pathlib
import random
import sys
from collections import Counter


# --- 路径相对本文件解析，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))
from engine import load_commanders, load_quiz, score_commanders, tally  # noqa: E402

DATA = ROOT / "data"
TARGETS = ["voltron", "artifacts", "tribal"]

quiz = load_quiz()
payload = load_commanders()
by_name = {c["en"]: c for c in payload["commanders"]}

# ① 题库承载量
print("=== ① 题库里这些轴有多少选项在承载 ===")
total_w: Counter = Counter()
opts_with: Counter = Counter()
for q in quiz["questions"]:
    for o in q["opts"]:
        for a, v in (o.get("s") or {}).items():
            total_w[a] += v
            if a in TARGETS:
                opts_with[a] += 1
grand = sum(total_w.values())
uniform = grand / len(total_w)
for a in TARGETS:
    print(f"  {a:<10} 总权重 {total_w[a]:>6.1f}（均匀基准 {uniform:.1f}，"
          f"{total_w[a] / uniform:.2f}×）　出现在 {opts_with[a]} 个选项里")

# ② 承载这些轴的题目都有哪些
print("\n=== ② 哪些「生活题」在考察这些轴 ===")
for a in TARGETS:
    print(f"\n  【{a}】")
    for q in quiz["questions"]:
        hits = [(i, o) for i, o in enumerate(q["opts"]) if (o.get("s") or {}).get(a)]
        if not hits:
            continue
        best = max(hits, key=lambda t: t[1]["s"][a])
        if best[1]["s"][a] < 1.0:      # 只列权重≥1 的，避免噪声
            continue
        print(f"    [{q['id']}] {q['q'][:34]}")
        print(f"        {'ABCDEF'[best[0]]}. {best[1]['t'][:44]}（{a} {best[1]['s'][a]:g}）")

# ③ 纯口味测试
print("\n=== ③ 只想要这一个玩法时，前五是谁 ===")
NEUTRAL = {"complex": 3.5, "budget": 3.5, "salt": 3.0, "exp": 3, "breadth": 0.5}
for a in TARGETS:
    res = score_commanders(payload, {a: 1.0}, {}, dict(NEUTRAL))[:5]
    names = " ｜ ".join(f"{by_name[r['en']]['zh']}({by_name[r['en']]['vec'].get(a, 0):.1f})"
                        for r in res)
    print(f"  {a:<10} {names}")

# ④ 人格抽样：想玩这些思路的人拿到的概率
print("\n=== ④ 200 个「口味明确」样本的命中率 ===")


def random_unit(rng, axes):
    v = {ax: rng.gauss(0, 1) for ax in axes}
    n = math.sqrt(sum(x * x for x in v.values()))
    return {k: x / n for k, x in v.items()}


axes = sorted({a for c in payload["commanders"] for a in c["vec"]})
by_id = {q["id"]: q for q in quiz["questions"]}
rng = random.Random(20261012)
agree = Counter()
tries = Counter()
for _ in range(200):
    d = random_unit(rng, axes)
    want = max(d, key=lambda k: d[k])
    answers = {}
    cur = quiz["start"]
    guard = 0
    while cur and guard < 600:
        q = by_id[cur]
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
    pref, colors, cons = tally(quiz, answers)
    got = by_name[score_commanders(payload, pref, colors, cons)[0]["en"]]
    lead = max(got["vec"], key=lambda k: got["vec"][k])
    tries[want] += 1
    agree[want] += (lead == want)
for a in TARGETS:
    if tries[a]:
        print(f"  {a:<10} 样本 {tries[a]:>3}　命中 {agree[a] / tries[a] * 100:>5.1f}%")
    else:
        print(f"  {a:<10} 样本 0")
