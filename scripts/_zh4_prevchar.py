# -*- coding: utf-8 -*-
"""观察已交付文件里「无官方中文名」的牌名是怎么并列表述的（前一个字符是什么）。"""
import glob
import json
import os
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
D = ROOT / "data"
card_zh = json.load(open(os.path.join(D, "card_zh.json"), encoding="utf-8"))
cmd_zh = json.load(open(os.path.join(D, "commander_zh.json"), encoding="utf-8"))


def zl(n):
    return card_zh.get(n) or cmd_zh.get(n)


paren = re.compile(r"（([A-Za-z][^（）]*?)）")
for f in sorted(glob.glob(os.path.join(D, "descriptions_*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    nozh = []
    for k, e in d.items():
        for fld in ("tagline", "intro", "build"):
            v = str(e.get(fld, ""))
            for m in paren.finditer(v):
                frag = m.group(1).strip()
                if zl(frag) is None:
                    prev = v[max(0, m.start() - 4):m.start()]
                    nozh.append((k, fld, frag, repr(prev), bool(re.search(r"[\u4e00-\u9fff]$", prev))))
    han = [x for x in nozh if x[4]]
    print(f"{os.path.basename(f)}: 无中文名牌名 {len(nozh)} 处，其中前面紧跟汉字（会被 5b 判违规）{len(han)} 处")
    for x in nozh[:5]:
        print("     样例:", x)
