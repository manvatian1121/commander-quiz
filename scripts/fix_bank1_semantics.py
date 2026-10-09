#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bank1.json 语义校正：修掉少数轴与语义不符的选项，并保持 20 轴 ≥12。

修正点：
  - s09 选项3「看谁在线就跟着谁的安排走」原本挂了 voltron，语义相反（是借力/随大流）→ clonesteal
  - h1c1 选项4「等我熟的人来带我」原本挂 voltron，但按语义是「等别人来扛」→ 换成 blink
  - voltron 改挂到真正「自己扛」的选项上：s09 选项1、h1c2 选项3
  - s01 选项3「手表震动就醒」→ artifacts（器具）比 stax 更贴语义
  - h1c3 选项3 的 enchant 换 grave（旧东西）,h1c2 选项1 的 enchant 也换成 blink
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
    ("s09", "看谁在线就跟着谁的安排走", {"politics": 2.0, "clonesteal": 1.5, "tribal": 1.0}, []),
    ("s09", "赶紧把一直想做没空做的事趁这天办了",
     {"aggro": 2.0, "voltron": 1.5, "removal": 1.0}, ["spells", "ramp"]),
    ("h1c1", "找个地方坐下不动", {"blink": 2.0, "tribal": 2.0, "wide": 1.0}, ["voltron"]),
    ("h1c2", "我先看一遍别人玩的视频", {"clonesteal": 2.0, "voltron": 1.5, "grave": 1.0}, []),
    ("h1c2", "好，什么时候，现在就去报名", {"aggro": 2.0, "blink": 2.0}, ["enchant"]),
    ("h1c3", "把它改成我熟的那套玩法", {"clonesteal": 2.0, "voltron": 1.5, "grave": 1.0}, ["enchant"]),
    ("s01", "手表一震动就醒", {"artifacts": 2.0, "counters": 1.0}, ["stax"]),
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
