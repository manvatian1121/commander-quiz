# -*- coding: utf-8 -*-
"""诊断：把超长条目的文本按块打印，方便定位要砍的部分。"""
import json
import pathlib
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path(ROOT / "data" / "descriptions_1.json")
data = json.loads(D.read_text(encoding="utf-8"))


def count(s):
    return sum(1 for ch in s.replace("\n", "") if not ch.isspace())


only = sys.argv[1:] or None
for k, v in data.items():
    if only and k not in only:
        continue
    for f in ("intro", "build"):
        n = count(v[f])
        if (f == "intro" and n > 120) or (f == "build" and n > 170):
            print(f"==== {k} / {f} = {n}")
            # 按句号/分号切块，打印每块长度
            chunks = re.split(r"(?<=[。；])", v[f])
            for c in chunks:
                if c.strip():
                    print(f"   [{count(c):>3}] {c.strip()}")
