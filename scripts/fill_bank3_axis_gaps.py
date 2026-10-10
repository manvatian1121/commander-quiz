# -*- coding: utf-8 -*-
"""bank3.json 轴覆盖填充（deficit-driven）：
反复挑「当前引用数最少」的轴，放进一个语义合适、且加进去不会让该题任意两选项
余弦相似度超过 COS_SOFT 的空位。直到每个轴都达到 TARGET 或没有可用空位。
"""
import json
import math
import sys
from pathlib import Path



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

BANK = Path(ROOT / "data" / "bank3.json")

AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]

TARGET = 13
COS_SOFT = 0.84

# 每题每个选项最适合追加的轴（每题 4 个选项各给一串语义合理的候选）
FIT = {
    "s33": [["tribal", "counters", "spells"], ["removal", "stax", "clonesteal"], ["tribal", "blink", "stompy"], ["grave", "enchant", "counters"]],
    "s34": [["spells", "aggro", "chaos"], ["combo", "clonesteal", "control"], ["grave", "enchant", "blink"], ["artifacts", "tribal", "ramp"]],
    "s35": [["spells", "aggro", "stompy"], ["counters", "drain", "control"], ["clonesteal", "combo", "artifacts"], ["artifacts", "stax", "ramp"]],
    "s36": [["ramp", "control", "counters"], ["counters", "drain", "stax"], ["stax", "removal", "grave"], ["chaos", "aggro", "spells"]],
    "s37": [["voltron", "aggro", "stompy"], ["control", "stax", "counters"], ["enchant", "grave", "drain"], ["clonesteal", "combo", "blink"]],
    "s38": [["ramp", "artifacts", "control"], ["drain", "enchant", "politics"], ["blink", "wide", "tribal"], ["chaos", "spells", "aggro"]],
    "s39": [["stax", "tribal", "control"], ["artifacts", "combo", "counters"], ["chaos", "spells", "aggro"], ["spells", "stompy", "voltron"]],
    "s40": [["stax", "aggro", "voltron"], ["counters", "clonesteal", "politics"], ["stompy", "removal", "voltron"], ["blink", "control", "enchant"]],
    "h3a1": [["ramp", "artifacts", "stax"], ["blink", "clonesteal", "combo"], ["tribal", "politics", "enchant"], ["chaos", "spells", "aggro"]],
    "h3a2": [["counters", "control", "ramp"], ["grave", "enchant", "tribal"], ["stompy", "voltron", "aggro"], ["politics", "clonesteal", "combo"]],
    "h3a3": [["blink", "tribal", "enchant"], ["counters", "ramp", "control"], ["combo", "removal", "artifacts"], ["stax", "grave", "drain"]],
    "h3b1": [["stompy", "voltron", "aggro"], ["control", "politics", "artifacts"], ["spells", "stax", "voltron"], ["grave", "chaos", "enchant"]],
    "h3b2": [["stompy", "aggro", "voltron"], ["grave", "clonesteal", "blink"], ["counters", "stax", "grave"], ["politics", "wide", "tribal"]],
    "h3b3": [["enchant", "drain", "politics"], ["counters", "grave", "stax"], ["tribal", "enchant", "wide"], ["blink", "chaos", "clonesteal"]],
    "h3c1": [["voltron", "aggro", "stompy"], ["counters", "politics", "artifacts"], ["wide", "blink", "tribal"], ["chaos", "voltron", "spells"]],
    "h3c2": [["artifacts", "ramp", "control"], ["removal", "control", "combo"], ["voltron", "removal", "aggro"], ["blink", "wide", "tribal"]],
    "h3c3": [["grave", "counters", "ramp"], ["chaos", "spells", "artifacts"], ["artifacts", "combo", "clonesteal"], ["tribal", "drain", "blink"]],
    "s41": [["voltron", "aggro", "stompy"], ["counters", "control", "clonesteal"], ["politics", "tribal", "wide"], ["ramp", "stompy", "artifacts"]],
    "s42": [["blink", "counters", "grave"], ["clonesteal", "artifacts", "combo"], ["stax", "grave", "drain"], ["artifacts", "counters", "ramp"]],
    "s43": [["spells", "aggro", "voltron"], ["control", "politics", "artifacts"], ["stax", "drain", "grave"], ["clonesteal", "blink", "combo"]],
    "s44": [["voltron", "politics", "removal"], ["stompy", "wide", "aggro"], ["control", "drain", "counters"], ["counters", "enchant", "blink"]],
    "s45": [["stax", "aggro", "stompy"], ["spells", "chaos", "blink"], ["removal", "counters", "voltron"], ["wide", "tribal", "enchant"]],
    "s46": [["tribal", "aggro", "stompy"], ["clonesteal", "politics", "combo"], ["wide", "spells", "artifacts"], ["grave", "artifacts", "chaos"]],
    "s47": [["stompy", "aggro", "voltron"], ["enchant", "counters", "artifacts"], ["voltron", "removal", "stompy"], ["ramp", "combo", "clonesteal"]],
    "s48": [["blink", "counters", "grave"], ["tribal", "control", "politics"], ["grave", "stax", "drain"], ["spells", "chaos", "aggro"]],
}


def cos(v1, v2):
    keys = set(v1) | set(v2)
    dot = sum(v1.get(k, 0) * v2.get(k, 0) for k in keys)
    n1 = math.sqrt(sum(v1.get(k, 0) ** 2 for k in keys))
    n2 = math.sqrt(sum(v2.get(k, 0) ** 2 for k in keys))
    return dot / (n1 * n2) if n1 and n2 else 0.0


def max_cos_in_question(q):
    vs = [o["s"] for o in q["opts"]]
    m = 0.0
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            m = max(m, cos(vs[i], vs[j]))
    return m


def main():
    data = json.loads(BANK.read_text(encoding="utf-8"))
    qs = data["questions"]
    freq = {a: 0 for a in AXES}
    for q in qs:
        for o in q["opts"]:
            for a in o["s"]:
                freq[a] += 1

    added = {}
    guard = 0
    while guard < 800:
        guard += 1
        deficits = [a for a in AXES if freq[a] < TARGET]
        if not deficits:
            break
        a = min(deficits, key=lambda x: (freq[x], AXES.index(x)))
        cands = []
        for q in qs:
            for i, o in enumerate(q["opts"]):
                if len(o["s"]) >= 3 or a in o["s"]:
                    continue
                rank = FIT[q["id"]][i].index(a) if a in FIT[q["id"]][i] else 9
                cands.append((rank, max_cos_in_question(q), q["id"], i))
        placed = False
        for rank, _mc, qid, i in sorted(cands):
            q = next(x for x in qs if x["id"] == qid)
            o = q["opts"][i]
            backup = dict(o["s"])
            o["s"][a] = 1.5 if rank == 0 else 1.0
            if max_cos_in_question(q) < COS_SOFT:
                freq[a] += 1
                added[a] = added.get(a, 0) + 1
                placed = True
                break
            o["s"] = backup
        if not placed:
            print(f"  [WARN] {a} 找不到合适空位，停在 {freq[a]}")
            break

    BANK.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"追加 {sum(added.values())} 个轴得分；合计引用 {sum(freq.values())}")
    for ax in sorted(freq, key=lambda x: freq[x]):
        flag = "" if freq[ax] >= TARGET else "  <-- 仍不足"
        print(f"  {ax:<12}{freq[ax]:>3}{flag}")


if __name__ == "__main__":
    main()
