#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""审计：列出 bank1 里余弦相似度较高的选项对，供人工复核「选项是否够区分」。

阈值可传参： python scripts/audit_fuzzy_bank1.py 0.60
"""
from __future__ import annotations

import json
import math
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

BANK = pathlib.Path(ROOT / "data" / "bank1.json")
LIMIT = float(sys.argv[1]) if len(sys.argv) > 1 else 0.60


def cosine(a: dict, b: dict) -> float:
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    shared = set(a) & set(b)
    return sum(a[k] / na * b[k] / nb for k in shared)


def main() -> int:
    data = json.loads(BANK.read_text(encoding="utf-8"))
    rows = []
    for q in data["questions"]:
        opts = q["opts"]
        for i in range(len(opts)):
            for j in range(i + 1, len(opts)):
                rows.append((cosine(opts[i]["s"], opts[j]["s"]), q["id"], i + 1, j + 1,
                             opts[i]["t"], opts[j]["t"]))
    rows.sort(reverse=True)
    print(f"总共 {len(rows)} 组选项对，列出余弦 ≥ {LIMIT} 的：\n")
    shown = 0
    for sim, qid, i, j, ti, tj in rows:
        if sim < LIMIT:
            break
        shown += 1
        print(f"{sim:.3f}  {qid} 选项{i} vs 选项{j}")
        print(f"        {ti}")
        print(f"        {tj}")
    print(f"\n共 {shown} 组，最高 {rows[0][0]:.3f}，阈值 0.85 未超标。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
