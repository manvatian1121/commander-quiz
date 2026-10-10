# -*- coding: utf-8 -*-
"""对比重写前后的模糊度（余弦）与轴覆盖：读两份 json 打分。"""
import json
import math
import sys
from pathlib import Path



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")


def cos(v1, v2):
    keys = set(v1) | set(v2)
    dot = sum(v1.get(k, 0) * v2.get(k, 0) for k in keys)
    n1 = math.sqrt(sum(v1.get(k, 0) ** 2 for k in keys))
    n2 = math.sqrt(sum(v2.get(k, 0) ** 2 for k in keys))
    return dot / (n1 * n2) if n1 and n2 else 0.0


def report(path, tag):
    qs = json.loads(Path(path).read_text(encoding="utf-8"))["questions"]
    mx, at, over = 0.0, "", []
    pairs = 0
    for q in qs:
        vs = [(o["t"], o["s"]) for o in q["opts"]]
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                c = cos(vs[i][1], vs[j][1])
                pairs += 1
                if c > mx:
                    mx, at = c, f"{q['id']} | {vs[i][0][:20]} x {vs[j][0][:20]} | {vs[i][1]} vs {vs[j][1]}"
                if c >= 0.85:
                    over.append((q["id"], round(c, 4)))
    freq = {}
    for q in qs:
        for o in q["opts"]:
            for a in o["s"]:
                freq[a] = freq.get(a, 0) + 1
    print(f"--- {tag} ---")
    print(f"  options={sum(len(q['opts']) for q in qs)}  pairs={pairs}")
    print(f"  max cosine = {mx:.4f}   over 0.85: {len(over)} {over}")
    print(f"  worst pair: {at}")
    print(f"  axis refs: {sum(freq.values())}  min={min(freq.values())} ({min(freq, key=freq.get)})  "
          f"max={max(freq.values())} ({max(freq, key=freq.get)})")
    print(f"  under 12: {sorted([a for a, n in freq.items() if n < 12])}")
    print()


for p, t in [
    (ROOT / "data" / "_bank3_stage1_hand.json", "stage 1: hand-written scores (before axis rebalance)"),
    (ROOT / "data" / "bank3.json", "stage 2: final bank3.json"),
]:
    if Path(p).exists():
        report(p, t)
    else:
        print(f"(missing {p})")
