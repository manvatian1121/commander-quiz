#!/usr/bin/env python3
"""独立验证改写后的颜色题：颜色信号是否仍然有效。

方法：在四道颜色题里各选「同一个颜色」的选项，其余题随便答，
看最终的颜色倾向向量是否确实偏向该颜色。
"""
from __future__ import annotations

import json
import pathlib
import sys


# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"ROOT\data")
COLOR_Q = ["s49", "s59", "s60", "s62"]
NAMES = {"W": "白", "U": "蓝", "B": "黑", "R": "红", "G": "绿"}

quiz = json.loads((DATA / "questions.json").read_text(encoding="utf-8"))
by_id = {q["id"]: q for q in quiz["questions"]}

print("=== 四道颜色题的颜色分布 ===")
print(f"  {'题号':<6} " + "　".join(f"{'ABCDE'[i]}" for i in range(5)))
matrix = {}
for qid in COLOR_Q:
    row = []
    for opt in by_id[qid]["opts"]:
        color = next(iter(opt.get("col") or {}), "?")
        row.append(color)
        matrix[(qid, color)] = opt
    print(f"  {qid:<6} " + "　".join(f"{NAMES.get(c, c)}" for c in row))

print("\n=== 逐色验证：四题都选该色的选项，颜色倾向应偏向该色 ===")
ok = 0
for color in "WUBRG":
    colors: dict[str, float] = {}
    for qid in COLOR_Q:
        opt = matrix.get((qid, color))
        if not opt:
            continue
        for key, value in (opt.get("col") or {}).items():
            colors[key] = colors.get(key, 0.0) + value
    top = max(colors, key=lambda k: colors[k])
    hit = top == color
    ok += hit
    detail = "　".join(f"{NAMES[k]}{colors[k]:.0f}" for k in "WUBRG" if k in colors)
    print(f"  全选「{NAMES[color]}」→ 最高是 {NAMES[top]}　{'✓' if hit else '✗'}　[{detail}]")

print(f"\n命中 {ok}/5")
print("✓ 颜色信号有效" if ok == 5 else "✗ 颜色信号有问题，需检查")
