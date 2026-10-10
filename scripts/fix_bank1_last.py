#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bank1.json 收尾：补 spells / drain 覆盖，并把 s16.next 复位为 null。

注意：后续脚本会重写整个 JSON，会把 s16.next 写回 "s17"，所以这一步必须最后跑。
本脚本自身用 next=None 写出，保持幂等。
"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

BANK = pathlib.Path(ROOT / "data" / "bank1.json")
AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]

PATCH: list[tuple[str, str, dict, list[str]]] = [
    ("s02", "听播客或者看书", {"ramp": 1.5, "spells": 1.5, "enchant": 2.0}, ["drain"]),
    ("s16", "看别人怎么选", {"politics": 2.0, "blink": 2.0, "drain": 1.0}, ["tribal"]),
]


def main() -> int:
    data = json.loads(BANK.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data["questions"]}

    for qid, prefix, vec, drops in PATCH:
        target = next((o for o in by_id[qid]["opts"] if o["t"].startswith(prefix)), None)
        if target is None:
            print(f"✗ 找不到选项：{qid} / {prefix}")
            return 1
        for axis in drops:
            target["s"].pop(axis, None)
        target["s"] = dict(vec)
        print(f"{qid}  {prefix}  ->  {target['s']}")

    # batch1 是最后一批题目文件里的一员，但 s17 不在本文件内，按 QUESTION_MAP 第 7 行写 null
    if by_id["s16"]["next"] is not None:
        print(f"s16.next {by_id['s16']['next']!r} -> None")
        by_id["s16"]["next"] = None

    BANK.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    hits: Counter = Counter()
    for q in data["questions"]:
        for o in q["opts"]:
            for a in o["s"]:
                hits[a] += 1
    short = [a for a in AXES if hits.get(a, 0) < 12]
    print(f"\n轴引用 {sum(hits.values())} 次，不足 12 的轴：{short or '无'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
