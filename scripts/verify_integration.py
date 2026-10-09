#!/usr/bin/env python3
"""确认三批介绍文的最新内容都已进入最终交付物。"""
from __future__ import annotations

import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)

html = (ROOT / "commander_quiz.html").read_text(encoding="utf-8")
md = (ROOT / "commander_quiz.md").read_text(encoding="utf-8")
match = re.search(r'<script id="payload" type="application/json">(.*?)</script>',
                  html, re.S)
embedded = json.loads(match.group(1).replace("<\\/", "</"))

print(f"成品内嵌介绍文：{len(embedded['descriptions'])} 篇")

all_ok = True
for index in (1, 2, 3):
    src = json.loads((ROOT / "data" / f"descriptions_{index}.json").read_text(encoding="utf-8"))
    missing_html, missing_md, mismatch = [], [], []
    for name, entry in src.items():
        got = embedded["descriptions"].get(name)
        if got != entry:
            mismatch.append(name)
        if entry["tagline"] not in html:
            missing_html.append(name)
        if entry["tagline"] not in md:
            missing_md.append(name)
    ok = not missing_html and not missing_md and not mismatch
    all_ok &= ok
    print(f"  批次 {index}：{len(src)} 篇 -> 与内嵌一致 "
          f"{'✓' if not mismatch else '✗ ' + str(mismatch[:3])}；"
          f"出现在 HTML {'✓' if not missing_html else '✗'}；"
          f"出现在 MD {'✓' if not missing_md else '✗'}")

# 抽查几条具体内容
print("\n抽查：")
for probe in ["Esika, God of the Tree", "Krenko, Mob Boss", "Y'shtola, Night's Blessed"]:
    entry = embedded["descriptions"][probe]
    print(f"  {probe}: 「{entry['tagline']}」")

print(f"\nEsika 背面名写入成品：{'The Prismatic Bridge' in html}")
print("\n" + ("✓ 三批内容全部进入最终交付物，且与源文件一致"
              if all_ok else "✗ 存在不一致，需要重建"))
sys.exit(0 if all_ok else 1)
