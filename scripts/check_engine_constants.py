#!/usr/bin/env python3
"""快速守卫：比对 Python 引擎与 JS 模板里的评分权重常量。

双引擎架构最容易犯的错就是「只改了一边」——这次就踩到了：
Python 的 W_COLOR_MATCH 改成了 0.50，JS 模板还停在 0.60，
导致 436 位主将分数不一致。完整的一致性测试能抓到，但要跑几分钟。
这个脚本在两秒内就能给出答案，适合放在流水线最前面。
"""
from __future__ import annotations

import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parent.parent
PY = ROOT / "scripts" / "engine.py"
JS = ROOT / "templates" / "quiz_template.html"

# 两边都要一致的常量（名字 → 在 JS 里叫什么）
PAIRS = [
    ("W_SIM", "W_SIM"), ("W_COLOR", "W_COLOR"), ("W_POPULAR", "W_POPULAR"),
    ("P_COST", "P_COST"), ("P_BUDGET", "P_BUDGET"), ("P_SALT", "P_SALT"),
    ("P_BRACKET", "P_BRACKET"),
    ("W_COLOR_MATCH", "W_COLOR_MATCH"), ("W_BREADTH_MATCH", "W_BREADTH_MATCH"),
]

py_text = PY.read_text(encoding="utf-8")
js_text = JS.read_text(encoding="utf-8")

problems = []
print("=== 评分权重常量比对（engine.py vs quiz_template.html）===")
print(f"  {'常量':<20} {'Python':>10} {'JS':>10}")
for py_name, js_name in PAIRS:
    py_match = re.search(rf"^{py_name}\s*=\s*([\d.]+)", py_text, re.M)
    js_match = re.search(rf"{js_name}\s*:\s*([\d.]+)", js_text)
    py_val = float(py_match.group(1)) if py_match else None
    js_val = float(js_match.group(1)) if js_match else None
    ok = py_val is not None and js_val is not None and abs(py_val - js_val) < 1e-9
    if not ok:
        problems.append((py_name, py_val, js_val))
    print(f"  {py_name:<20} {str(py_val):>10} {str(js_val):>10}  {'✓' if ok else '✗ 不一致'}")

# 其它必须一致的结构性常量
print("\n=== 其它结构性常量 ===")
for label, py_pat, js_pat in [
    ("难度权重 text/pilot", r"TEXT_W\s*=\s*([\d.]+)", r"textW\s*[:=]\s*([\d.]+)"),
    ("咸度阈值表", r"SALT_THRESHOLD\s*=\s*\{[^}]*\}", r"var SALT_CAP\s*=\s*\[[^\]]*\]"),
]:
    a = re.search(py_pat, py_text)
    b = re.search(js_pat, js_text)
    print(f"  {label:<20} Python {'有' if a else '无'} / JS {'有' if b else '无'}"
          f"　（只报告，不比对数值）")

print()
if problems:
    print(f"✗ {len(problems)} 个常量不一致：")
    for name, a, b in problems:
        print(f"    {name}：engine.py = {a}，quiz_template.html = {b}")
    print("\n  两处必须同步修改，否则两个引擎算出的推荐会不一样。")
    sys.exit(1)
print("✓ 两个引擎的权重常量完全一致")
