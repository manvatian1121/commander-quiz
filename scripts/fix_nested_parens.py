#!/usr/bin/env python3
"""修二次注入造成的嵌套括号。

原因：inject_card_zh.py 判断「是否已经是中文（English）形式」时，
要求括号前一个字符是中文。像「潘妮驾驭的SP//dr（...）」这种中文名里带拉丁字母的，
守卫失效，于是被注入第二次，形成嵌套括号。
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
    ("descriptions_4.json", "Cosmic Spider-Man", "build",
     "潘妮驾驭的SP//dr（潘妮驾驭的SP//dr（SP//dr, Piloted by Peni））",
     "潘妮驾驭的SP//dr（SP//dr, Piloted by Peni）"),
    ("descriptions_4.json", "Éowyn, Shieldmaiden", "build",
     "埃奥尔勇往直前！（埃奥尔勇往直前！（Forth Eorlingas!））",
     "埃奥尔勇往直前！（Forth Eorlingas!）"),
]


def main() -> int:
    for fname, commander, field, old, new in FIXES:
        path = DATA / fname
        data = json.loads(path.read_text(encoding="utf-8"))
        entry = data.get(commander)
        if not entry:
            print(f"✗ 找不到 {commander}")
            return 1
        if old not in (entry.get(field) or ""):
            print(f"✗ {commander}.{field} 找不到目标文本")
            continue
        entry[field] = entry[field].replace(old, new)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✓ {commander}.{field}：去掉一层嵌套括号")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
