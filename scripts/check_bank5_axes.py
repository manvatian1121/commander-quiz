#!/usr/bin/env python3
"""附加体检：同选项内不出现方向相反的两个高权重轴。"""
import json
import itertools
import pathlib
import sys


# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
BANK = pathlib.Path(ROOT / "data" / "bank5.json")

OPPOSED = [("aggro", "control"), ("aggro", "drain"), ("aggro", "stax"),
           ("chaos", "control"), ("chaos", "stax"), ("chaos", "ramp"),
           ("wide", "voltron"), ("wide", "stompy"), ("combo", "stompy"),
           ("blink", "aggro"), ("drain", "stompy"), ("politics", "stompy"),
           ("enchant", "chaos"), ("counters", "chaos")]

data = json.loads(BANK.read_text(encoding="utf-8"))
issues = []
for q in data["questions"]:
    for i, o in enumerate(q["opts"], 1):
        for a, b in OPPOSED:
            if o["s"].get(a, 0) >= 2.0 and o["s"].get(b, 0) >= 2.0:
                issues.append((q["id"], i, a, b, o["s"]))

# 反向轴同时出现在同一题不同选项里是正常的，只看同选项
print(f"同选项内出现反向双高权重的情况：{len(issues)} 处")
for it in issues:
    print("  ✗", it)

# 顺便统计权重分布与题均引用
from collections import Counter

w = Counter()
refs = 0
opts = 0
for q in data["questions"]:
    for o in q["opts"]:
        opts += 1
        for axis, val in o["s"].items():
            w[val] += 1
            refs += 1
print(f"\n选项数 {opts}，轴引用 {refs}，题均选项 {opts / len(data['questions']):.1f}，"
      f"选项均轴 {refs / opts:.2f}")
print("权重分布：", dict(sorted(w.items())))
