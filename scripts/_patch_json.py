# -*- coding: utf-8 -*-
"""按精确长度逐条微调（幂等），并把结果写回分段文件所依赖的 JSON。"""
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


def sub(key, field, old, new, expect=None):
    v = data[key][field]
    if old not in v:
        print(f"!! 未匹配 {key}/{field}: {old[:20]}")
        return
    v = v.replace(old, new, 1)
    data[key][field] = v
    n = count(v)
    flag = "✓" if (expect is None or n == expect) else f"(预期 {expect})"
    print(f"{key}/{field}: {n} {flag}")


# Cloud build 173 -> 170
sub("Cloud, Ex-SOLDIER", "build", "让他攻击时找一张地，", "让他攻击时找地，")
sub("Cloud, Ex-SOLDIER", "build", "能补上多个对手时的收益", "补上多个对手时的收益")
# Frodo intro 122 -> 118
sub("Frodo, Adventurous Hobbit // Sam, Loyal Attendant", "intro", "攒够次数还能抽牌", "攒够还抽牌")
# Esika build 171 -> 170
sub("Esika, God of the Tree", "build", "能让地变任意颜色", "能让地变任意色")

D.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("--- 复测")
for k, v in data.items():
    tl, it, bd = count(v["tagline"]), count(v["intro"]), count(v["build"])
    if tl > 20 or not (70 <= it <= 120) or not (110 <= bd <= 170):
        print("✗", tl, it, bd, k)
