#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bank1.json 轴覆盖收尾配平（按选项文本定位，避免序号错位）。"""
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

# (题目 id, 选项文本前缀) -> 新的轴向量；None 表示删除指定轴
PATCH: list[tuple[str, str, dict | None, list[str]]] = [
    # s16 天气预报：修掉上一轮错位，并给「外套」补 voltron
    ("s16", "伞照带", {"control": 2.0, "ramp": 1.5}, []),
    ("s16", "不带，淋湿了", {"stompy": 1.5, "chaos": 1.0, "aggro": 1.0}, []),
    ("s16", "带一件能当伞用的外套", {"artifacts": 2.5, "voltron": 1.5, "clonesteal": 1.5}, []),
    ("s16", "看别人怎么选", {"politics": 2.0, "blink": 1.5, "clonesteal": 1.0}, []),
    # 给各条短板轴各加 1 个选项覆盖（腾出的槽位来自过采样的轴）
    ("s01", "手表一震动就醒", {"stax": 2.0, "counters": 1.0}, ["artifacts"]),
    ("s01", "前一晚衣服和包都摆好了", None, ["politics"]),
    ("s04", "自己一个人去跑一趟", {"blink": 1.5, "wide": 2.0, "voltron": 1.0}, []),
    ("s05", "报上我每次都点的那几样", {"tribal": 2.5, "counters": 1.0, "spells": 1.5}, []),
    ("h1a3", "细到半小时一格", {"control": 2.5, "stax": 2.5, "combo": 1.5}, []),
    ("h1b2", "包装盒、备用线、备用零件", {"artifacts": 2.0, "ramp": 1.5, "enchant": 1.5}, []),
    ("h1b2", "别人送的礼物", {"blink": 1.5, "enchant": 2.0, "drain": 1.5}, []),
    ("h1c3", "两个一起玩", {"tribal": 2.5, "counters": 1.0, "stompy": 1.5}, []),
    ("s09", "什么都不干，睡到自然醒", {"drain": 2.0, "control": 1.0, "stax": 1.5}, []),
    ("s13", "看心情，有时候一口气全回完", {"chaos": 2.0, "stompy": 2.5}, []),
]


def main() -> int:
    data = json.loads(BANK.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data["questions"]}
    applied = 0

    for qid, prefix, vec, drops in PATCH:
        q = by_id[qid]
        target = next((o for o in q["opts"] if o["t"].startswith(prefix)), None)
        if target is None:
            print(f"✗ 找不到选项：{qid} / {prefix}")
            return 1
        for axis in drops:
            target["s"].pop(axis, None)
        if vec is not None:
            target["s"] = dict(vec)
        applied += 1

    BANK.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    hits: Counter = Counter()
    for q in data["questions"]:
        for o in q["opts"]:
            for a in o["s"]:
                hits[a] += 1
    print(f"应用 {applied} 处改动。各轴引用数：")
    for a in AXES:
        c = hits.get(a, 0)
        print(f"  {a:<11} {c:>3}" + ("  ← 仍不足" if c < 12 else ""))
    short = [a for a in AXES if hits.get(a, 0) < 12]
    print(f"\n题数 {len(data['questions'])}，选项 {sum(len(q['opts']) for q in data['questions'])} 个，"
          f"轴引用 {sum(hits.values())} 次，不足 12 的轴：{short or '无'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
