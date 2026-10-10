#!/usr/bin/env python3
"""修两处收尾问题：
① Omo 的介绍被中文名注入损坏（主将名里的 Vesuva 也被替换了，括号嵌套）
② Ozai 的定位写「主将就无敌」——那是夸大，实际是获得「不灭」
"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

FIXES = [
    ("descriptions_4.json", "Omo, Queen of Vesuva", "intro",
     "维苏瓦女皇欧茉（Omo, Queen of 维苏瓦（Vesuva））是蓝绿的三费变形兽。",
     "维苏瓦女皇欧茉（Omo, Queen of Vesuva）是蓝绿的三费变形兽。",
     "注入器把主将名里的 Vesuva 也当成搭配牌替换了，造成括号嵌套"),
    ("descriptions_7.json", "Ozai, the Phoenix King", "tagline",
     "手上留着六点法术力，主将就无敌",
     "手上留着六点法术力，主将就打不死",
     "「无敌」是夸大；牌面实际给的是「不灭」，改成准确说法"),
]


def main() -> int:
    changed = 0
    for fname, commander, field, old, new, why in FIXES:
        path = DATA / fname
        data = json.loads(path.read_text(encoding="utf-8"))
        entry = data.get(commander)
        if not entry:
            print(f"✗ 找不到 {fname} / {commander}")
            return 1
        if entry.get(field) != old and old not in (entry.get(field) or ""):
            print(f"✗ {commander}.{field} 与预期不符：{entry.get(field)[:60]!r}")
            return 1
        entry[field] = entry[field].replace(old, new)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✓ [{fname}] {commander}.{field}")
        print(f"    理由：{why}")
        changed += 1
    print(f"\n共修正 {changed} 处")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
