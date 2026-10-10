#!/usr/bin/env python3
"""把「档位封顶」改成「随经验上移的目标档位」，让老手真的偏好高强度。

原逻辑： bracket_pen = max(0, 主将档位 − 上限) × 0.030
  新人上限 3 → Bracket 5 扣 0.06 ✓
  老手上限 5 → 永远不扣分，且高强度也没有加分 → 对强度完全无感 ✗

新逻辑： bracket_pen = |主将档位 − 目标档位| × 0.025
  目标随经验上移：新人 2.0 → 老手 4.4
  新人拿到 Bracket 5 仍然要扣 0.075（比原来还稍重）
  老手拿到 Bracket 2 要扣 0.06，拿到 Bracket 5 只扣 0.01 → 真的会往高强度走
"""
from __future__ import annotations

import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"D:\万智\commander-quiz")

TARGET = {1: 2.0, 2: 2.7, 3: 3.6, 4: 4.4}
P_BRACKET = 0.025

# ---------- Python 引擎 ----------
py = ROOT / "scripts" / "engine.py"
t = py.read_text(encoding="utf-8")

# ① EXP_PROFILE 里 bracket_cap → bracket_target
for lvl, val in TARGET.items():
    t = re.sub(rf'({lvl}: \{{"name": "[^"]+", "complex_cap": [\d.]+, '
               rf'"pop_mul": [\d.]+, )"bracket_cap": \d+', rf'\1"bracket_target": {val}', t)

# ② 扣分公式
old = 'bracket_pen = max(0, int(card.get("bracket", 3)) - profile["bracket_cap"]) * P_BRACKET'
new = ('# 目标档位随经验上移：新人被拉向低强度，老手被拉向高强度。\n'
       '        # 原来只对「超过上限」扣分，老手上限是 5 所以永远不扣分、\n'
       '        # 高强度也没有加分——结果就是对强度完全无感。\n'
       '        bracket_pen = abs(int(card.get("bracket", 3))\n'
       '                          - profile["bracket_target"]) * P_BRACKET')
if old in t:
    t = t.replace(old, new)
    print("✓ Python 扣分公式已替换")
else:
    print("✗ Python 未找到原公式")

# ③ 常量注释
t = re.sub(r"P_BRACKET = 0\.030[^\n]*",
           "P_BRACKET = 0.025    # 与目标档位的偏离（双向：太高太低都扣）", t)
t = re.sub(r"(?<!W_)P_BRACKET = 0\.025(?!\s*#)", "P_BRACKET = 0.025", t)
py.write_text(t, encoding="utf-8")
print("\n=== 改后的 EXP_PROFILE ===")
for line in t.split("\n"):
    if re.search(r'^\s*[1-4]:\s*\{"name"', line):
        print("  ", line.strip())
for line in t.split("\n"):
    if "P_BRACKET =" in line:
        print("  ", line.strip())

# ---------- JS 模板 ----------
js = ROOT / "templates" / "quiz_template.html"
jt = js.read_text(encoding="utf-8")
for lvl, val in TARGET.items():
    jt = re.sub(rf'({lvl}: \{{ name:"[^"]+",\s*complexCap:[\d.]+,\s*popMul:[\d.]+,\s*)'
                rf'bracketCap:\d+', rf'\1bracketTarget:{val}', jt)
old_js = re.compile(r"var bracketPen = Math\.max\(0,[^\n]*\n[^\n]*")
m = old_js.search(jt)
print("\n=== JS 原公式 ===")
print("  ", m.group(0).replace("\n", "\n   ") if m else "✗ 未找到")
if m:
    jt = old_js.sub(
        "// 目标档位随经验上移：新人被拉向低强度，老手被拉向高强度\n"
        "      var bracketPen = Math.abs((c.bracket || 3) - prof.bracketTarget)\n"
        "                     * CONST.P_BRACKET;", jt, count=1)
    js.write_text(jt, encoding="utf-8")
    print("✓ JS 公式已替换")
print("\n=== 改后的 JS EXP_PROFILE ===")
for line in jt.split("\n"):
    if "complexCap" in line and "name:" in line:
        print("  ", line.strip())
