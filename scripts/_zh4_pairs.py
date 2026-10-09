# -*- coding: utf-8 -*-
"""已交付的 descriptions_*.json 里的「中文（English）」配对，能否在 card_zh.json 中解析？"""
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
zh = json.load(open(os.path.join(D, "card_zh.json"), encoding="utf-8"))
cmdzh = json.load(open(os.path.join(D, "commander_zh.json"), encoding="utf-8"))

pat = re.compile(r"([\u4e00-\u9fff·]+)（([A-Za-z][A-Za-z0-9,'’\-\. ]*)）")

for f in sorted(glob.glob(os.path.join(D, "descriptions_*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    pairs, miss = 0, []
    for k, e in d.items():
        txt = "".join(str(e.get(x, "")) for x in ("tagline", "intro", "build"))
        for zhname, en in pat.findall(txt):
            pairs += 1
            if zh.get(en.strip()) != zhname:
                miss.append((k, zhname, en.strip(), zh.get(en.strip()), cmdzh.get(en.strip())))
    print(f"{os.path.basename(f)}: 配对 {pairs}，card_zh 不匹配 {len(miss)}")
    for m in miss[:8]:
        print("    ", m)
