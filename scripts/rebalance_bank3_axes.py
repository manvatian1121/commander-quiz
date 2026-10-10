# -*- coding: utf-8 -*-
"""bank3.json 轴覆盖再平衡补丁：保证 20 个轴每个至少被 12 个选项引用。
在 make_bank3.py 生成之后运行（也可单独运行）。
"""
import json
import sys
from pathlib import Path



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

BANK = Path(ROOT / "data" / "bank3.json")

# id -> 该题 4 个选项的轴得分（按原顺序）
PATCH = {
    "s33": [
        {"aggro": 2.5, "wide": 1.5, "tribal": 1.5}, {"control": 2.5, "removal": 1.0}, {"wide": 2.5, "tribal": 1.5, "blink": 1.0},
        {"drain": 2.0, "enchant": 1.0}],
    "s34": [
        {"aggro": 2.0, "spells": 1.0, "voltron": 1.5}, {"control": 2.0, "combo": 1.5, "clonesteal": 1.0}, {"drain": 1.5, "enchant": 1.0},
        {"artifacts": 1.5, "wide": 1.0, "tribal": 1.5}],
    "s35": [
        {"aggro": 2.5, "spells": 1.5}, {"drain": 2.5, "counters": 1.0}, {"clonesteal": 2.5, "combo": 1.5},
        {"stax": 2.0, "wide": 1.5, "artifacts": 1.0}],
    "s36": [
        {"removal": 1.5, "control": 1.5, "ramp": 1.5}, {"drain": 2.0, "control": 1.5}, {"removal": 2.0, "stax": 1.5},
        {"spells": 1.5, "chaos": 1.0, "aggro": 1.5}],
    "s37": [
        {"aggro": 2.0, "removal": 1.5, "voltron": 1.5}, {"politics": 1.5, "stax": 1.5, "control": 1.5},
        {"drain": 1.5, "enchant": 1.5, "grave": 1.0}, {"combo": 2.0, "clonesteal": 1.5, "counters": 1.0}],
    "s38": [
        {"ramp": 2.0, "control": 1.5, "artifacts": 1.5}, {"politics": 1.5, "drain": 1.5, "enchant": 1.5},
        {"wide": 2.0, "blink": 1.5, "artifacts": 1.0}, {"chaos": 2.5, "aggro": 1.0}],
    "s39": [
        {"stax": 1.5, "chaos": 1.0, "blink": 1.5}, {"control": 2.0, "artifacts": 1.5, "combo": 1.0},
        {"chaos": 1.5, "aggro": 1.5, "spells": 1.0}, {"chaos": 2.5, "spells": 1.0, "stompy": 1.5}],
    "h3a1": [
        {"stax": 2.0, "ramp": 1.5, "artifacts": 1.0}, {"combo": 1.5, "blink": 1.5, "clonesteal": 1.5},
        {"politics": 2.5, "tribal": 1.5, "enchant": 1.0}, {"aggro": 2.5, "chaos": 1.5, "counters": 1.0}],
    "h3a2": [
        {"control": 2.5, "ramp": 1.5, "counters": 1.0}, {"enchant": 2.0, "tribal": 1.5, "grave": 1.0},
        {"aggro": 2.0, "stompy": 2.0, "spells": 1.0}, {"clonesteal": 2.0, "politics": 2.0, "combo": 1.0}],
    "h3a3": [
        {"tribal": 2.0, "blink": 1.0, "enchant": 1.0}, {"ramp": 2.0, "counters": 1.5}, {"removal": 2.5, "combo": 1.5, "ramp": 1.0},
        {"drain": 2.5, "stax": 1.0, "grave": 1.0}],
    "h3b1": [
        {"aggro": 2.5, "stompy": 1.5, "voltron": 1.0}, {"politics": 1.5, "control": 1.5}, {"stax": 2.5, "spells": 1.0},
        {"chaos": 1.5, "grave": 2.5, "enchant": 1.0}],
    "h3b2": [
        {"aggro": 2.5, "stompy": 1.5}, {"blink": 2.0, "clonesteal": 1.5, "grave": 1.0}, {"stax": 2.0, "grave": 1.5},
        {"politics": 2.5, "wide": 1.5, "tribal": 1.0}],
    "h3b3": [
        {"politics": 1.5, "drain": 1.5, "enchant": 1.5}, {"grave": 2.0, "stax": 1.5, "counters": 1.0}, {"tribal": 2.0, "enchant": 1.5},
        {"blink": 1.5, "chaos": 1.5}],
    "h3c1": [
        {"aggro": 2.5, "stax": 1.5, "stompy": 1.0}, {"politics": 2.5, "counters": 1.5}, {"blink": 2.0, "wide": 1.5, "combo": 1.0},
        {"voltron": 2.0, "chaos": 1.5, "spells": 1.0}],
    "h3c2": [
        {"ramp": 2.0, "stax": 1.5, "artifacts": 1.5}, {"control": 2.0, "removal": 1.5, "artifacts": 1.0}, {"removal": 2.0, "voltron": 1.5},
        {"blink": 2.0, "wide": 1.5}],
    "h3c3": [
        {"counters": 2.5, "ramp": 1.0}, {"spells": 2.0, "chaos": 1.5, "artifacts": 1.0}, {"combo": 2.0, "artifacts": 1.5, "clonesteal": 1.0},
        {"tribal": 1.5, "drain": 1.0, "blink": 1.0}],
    "s41": [
        {"aggro": 2.5, "voltron": 1.5, "stompy": 1.0}, {"control": 2.0, "counters": 1.0, "clonesteal": 1.0}, {"tribal": 2.0, "politics": 1.5},
        {"ramp": 1.5, "wide": 1.0, "stompy": 1.5}],
    "s42": [
        {"removal": 2.0, "counters": 1.5, "blink": 1.0}, {"artifacts": 2.0, "clonesteal": 1.5, "combo": 1.0},
        {"drain": 2.0, "stax": 1.5, "grave": 1.0}, {"artifacts": 2.0, "counters": 1.5, "ramp": 1.0}],
    "s43": [
        {"aggro": 2.0, "removal": 1.5, "spells": 1.0}, {"politics": 1.0, "control": 1.5}, {"drain": 2.0, "stax": 1.0, "grave": 1.0},
        {"combo": 1.5, "clonesteal": 1.5, "blink": 1.0}],
    "s44": [
        {"removal": 1.5, "politics": 1.5, "voltron": 1.0}, {"wide": 1.5, "voltron": 1.5, "stompy": 1.0},
        {"drain": 2.0, "control": 1.0}, {"enchant": 1.5, "counters": 1.5}],
    "s45": [
        {"aggro": 2.5, "stax": 1.5}, {"chaos": 1.0, "drain": 1.5, "spells": 1.0}, {"stax": 2.0, "removal": 1.5, "counters": 1.0},
        {"tribal": 1.5, "wide": 1.5, "enchant": 1.0}],
    "s46": [
        {"aggro": 2.0, "tribal": 1.5, "stompy": 1.0}, {"politics": 2.5, "clonesteal": 1.5, "combo": 1.0}, {"spells": 2.0, "wide": 1.5},
        {"chaos": 1.5, "grave": 1.0, "artifacts": 1.0}],
    "s47": [
        {"aggro": 2.5, "stompy": 1.5, "voltron": 1.0}, {"control": 2.0, "counters": 1.5, "enchant": 1.0}, {"removal": 2.0, "voltron": 1.5, "stompy": 1.0},
        {"combo": 1.5, "clonesteal": 1.5, "ramp": 1.0}],
    "s48": [
        {"counters": 2.0, "wide": 1.5, "blink": 1.0}, {"control": 1.5, "tribal": 1.0}, {"drain": 2.0, "stax": 1.0, "grave": 1.5},
        {"chaos": 2.5, "spells": 1.5}],
}


def main():
    data = json.loads(BANK.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data["questions"]}
    changed = 0
    skipped = []
    for q in data["questions"]:
        if q["id"] not in PATCH:
            continue
        new = PATCH[q["id"]]
        if len(new) != len(q["opts"]):
            skipped.append(q["id"])
            continue
        for o, s in zip(q["opts"], new):
            if o["s"] != s:
                changed += 1
            o["s"] = s
    BANK.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    freq = {}
    for q in data["questions"]:
        for o in q["opts"]:
            for a in o["s"]:
                freq[a] = freq.get(a, 0) + 1
    print(f"patched {changed} 个选项；轴引用合计 {sum(freq.values())}" + (f"；跳过（选项数不符）{skipped}" if skipped else ""))
    for a in sorted(freq, key=lambda x: freq[x]):
        print(f"  {a:<12}{freq[a]}")


if __name__ == "__main__":
    main()
