#!/usr/bin/env python3
"""把档位权重做成随经验递增，并微调目标档位。

扫描结论（老手 B4+5 占比 vs 玩法余弦）：
  定权 0.025          8%   0.564
  老手 0.070         18%   0.542   ← 选这档
  老手 0.100         36%   0.516   玩法契合被压垮
"""
from __future__ import annotations

import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)

TARGETS = {1: 2.0, 2: 2.7, 3: 3.6, 4: 4.6}
WEIGHTS = {1: 0.025, 2: 0.038, 3: 0.054, 4: 0.070}

py = ROOT / "scripts" / "engine.py"
t = py.read_text(encoding="utf-8")
for lvl in (1, 2, 3, 4):
    t = re.sub(rf'({lvl}: \{{"name": "[^"]+", "complex_cap": [\d.]+, "pop_mul": [\d.]+, )'
               rf'"bracket_target": [\d.]+',
               rf'\1"bracket_target": {TARGETS[lvl]}, "p_bracket": {WEIGHTS[lvl]}', t)
t = t.replace('-- profile["bracket_target"]) * P_BRACKET)',
              '-- profile["bracket_target"]) * profile["p_bracket"])')
py.write_text(t, encoding="utf-8")
print("=== engine.py ===")
for line in t.split("\n"):
    if re.search(r'^\s*[1-4]:\s*\{"name"', line):
        print("  ", line.strip())
for line in t.split("\n"):
    if "profile[\"p_bracket\"]" in line:
        print("  ", line.strip())

js = ROOT / "templates" / "quiz_template.html"
jt = js.read_text(encoding="utf-8")
for lvl in (1, 2, 3, 4):
    jt = re.sub(rf'({lvl}: \{{ name:"[^"]+",\s*complexCap:[\d.]+,\s*popMul:[\d.]+,\s*)'
                rf'bracketTarget:[\d.]+',
                rf'\1bracketTarget:{TARGETS[lvl]}, pBracket:{WEIGHTS[lvl]}', jt)
jt = jt.replace('* CONST.P_BRACKET;', '* prof.pBracket;')
js.write_text(jt, encoding="utf-8")
print("\n=== quiz_template.html ===")
for line in jt.split("\n"):
    if "complexCap" in line and "name:" in line:
        print("  ", line.strip())
for line in jt.split("\n"):
    if "prof.pBracket" in line:
        print("  ", line.strip())
