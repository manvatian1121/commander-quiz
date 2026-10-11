#!/usr/bin/env python3
"""放宽各经验段的难度/档位上限，让新人也有广泛的推荐面。

问题：原来完全新人被卡在「难度 ≤1.6 且 Bracket ≤2」，全池 506 位里只有
43 位（8%）不被扣分，推荐必然集中。

而扣分本身已经在起引导作用——实测放宽到 2.6/B3 后，推荐主将的
难度中位数只从 1.60 升到 1.97，仍然偏低，但候选面宽了近一倍。

四个档位重新排（原来 1/2/3 档在新口径下会重叠）：
  完全新人        1.6/2 → 2.4/3
  玩过牌没打过EDH  2.6/3 → 3.2/4
  打过一段时间     3.8/4 → 4.2/5
  老手            5.0/5 → 5.0/5（不变）
"""
from __future__ import annotations

import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)

NEW = {
    1: (2.4, 3),
    2: (3.2, 4),
    3: (4.2, 5),
    4: (5.0, 5),
}
OLD_NAMES = {
    1: "完全新人", 2: "玩过万智牌，没打过指挥官",
    3: "打过一段时间指挥官", 4: "老手",
}

# ① Python 引擎
py = ROOT / "scripts" / "engine.py"
t = py.read_text(encoding="utf-8")
print("=== engine.py ===")
for line in t.split("\n"):
    if re.search(r'^\s*[1-4]:\s*\{', line):
        print("  旧:", line.strip())
block = "EXP_PROFILE = {\n"
for lvl in (1, 2, 3, 4):
    cc, bc = NEW[lvl]
    mult = {1: 1.35, 2: 1.20, 3: 1.00, 4: 0.85}[lvl]
    block += (f'    {lvl}: {{"name": "{OLD_NAMES[lvl]}", "complex_cap": {cc}, '
              f'"pop_mul": {mult}, "bracket_cap": {bc}}},\n')
block += "}"
t2 = re.sub(r"EXP_PROFILE = \{.*?\n\}", block, t, count=1, flags=re.S)
py.write_text(t2, encoding="utf-8")
print("  新:")
for line in t2.split("\n"):
    if re.search(r'^\s*[1-4]:\s*\{', line):
        print("   ", line.strip())

# ② JS 模板
js = ROOT / "templates" / "quiz_template.html"
jt = js.read_text(encoding="utf-8")
print("\n=== quiz_template.html ===")
for line in jt.split("\n"):
    if re.search(r'^\s*[1-4]:\s*\{', line) and ("complexCap" in line or "complex_cap" in line):
        print("  旧:", line.strip())
jblock = "var EXP_PROFILE = {\n"
for lvl in (1, 2, 3, 4):
    cc, bc = NEW[lvl]
    mult = {1: 1.35, 2: 1.20, 3: 1.00, 4: 0.85}[lvl]
    jblock += (f'    {lvl}: {{ name:"{OLD_NAMES[lvl]}", complexCap:{cc}, '
               f'popMul:{mult}, bracketCap:{bc} }},\n')
jblock += "  };"
jt2 = re.sub(r"var EXP_PROFILE = \{.*?\n\s*\};", jblock, jt, count=1, flags=re.S)
if jt2 == jt:
    print("  ✗ 未匹配到 JS 的 EXP_PROFILE，需要手工核对")
else:
    js.write_text(jt2, encoding="utf-8")
    print("  新:")
    for line in jt2.split("\n"):
        if "complexCap" in line:
            print("   ", line.strip())
