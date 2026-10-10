#!/usr/bin/env python3
"""再修两处措辞（与「养」同类的搭配/重复问题）。"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"D:\万智\commander-quiz\data")

FIXES = [
    ("s49",
     "把当时的照片、聊天记录、写下的东西翻出来，按年份归到一处，标清楚是哪一年",
     "把当时的照片、聊天记录、写下的东西都翻出来，按时间归好，一样不落",
     "「按年份归到一处」已经包含「标清楚是哪一年」，后半句语义重复"),
    ("s59",
     "不急着一次用透，先摆到顺手的位置天天用，越用越合手，顺手把耗材备上",
     "不急着一次用透，先放在手边天天用，用着用着就熟了，耗材提前备上",
     "一句话里出现两个「顺手」；「合手」多用于工具，改用「熟了」"),
]


def main() -> int:
    path = DATA / "bank4.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in payload["questions"]}
    changed = 0
    for qid, old, new, why in FIXES:
        q = by_id.get(qid)
        if q is None:
            print(f"✗ 找不到 {qid}")
            return 1
        hit = False
        for opt in q["opts"]:
            if opt["t"] == old:
                opt["t"] = new
                print(f"[{qid}] {old}")
                print(f"    → {new}")
                print(f"      理由：{why}\n")
                changed += 1
                hit = True
        if not hit:
            print(f"✗ {qid} 找不到目标文本：{old!r}")
            return 1
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ 修正 {changed} 处")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
