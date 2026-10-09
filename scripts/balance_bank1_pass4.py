#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bank1.json 轴覆盖收尾（第 4 轮，最终）。

要点：clonesteal 之前几乎只出现在分支题里（主线只有 s06 一处），
这一轮把它铺进主线与分支的多条「照别人的做法来 / 抄近路 / 用现成的」选项，
并补齐 enchant / tribal / politics 各一处。
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

PATCH: list[tuple[str, str, dict | None, list[str]]] = [
    # --- 新增 5 选项：s15 快递 ---
    ("s15", "__append__", {"clonesteal": 2.0, "politics": 1.5, "artifacts": 1.0}, []),
    # --- clonesteal 铺进主线与分支 ---
    ("s02", "盯着报站和路线", {"control": 1.5, "removal": 1.5, "clonesteal": 1.0}, []),
    ("s03", "工具和文具顺手摆在手边", {"artifacts": 1.5, "aggro": 1.5, "clonesteal": 1.0}, []),
    ("s07", "开省电模式", {"drain": 2.0, "clonesteal": 1.5}, ["stax"]),
    ("s10", "顺便把冰箱清一遍", {"blink": 1.5, "wide": 1.5, "clonesteal": 1.0}, ["spells"]),
    ("h1b3", "旧的都留下不要了", {"stax": 1.0, "spells": 1.0, "clonesteal": 1.5}, ["chaos"]),
    # --- enchant 补 6 处 ---
    ("s02", "听播客或者看书", {"ramp": 1.5, "drain": 1.5, "enchant": 2.0}, ["combo"]),
    ("s07", "不管，低电就低电", {"stompy": 1.5, "chaos": 1.5, "enchant": 1.5}, []),
    ("s08", "那就不安排了", {"chaos": 2.0, "spells": 1.0, "enchant": 1.5}, []),
    ("s12", "站那儿发会儿呆", {"stompy": 2.0, "drain": 1.0, "enchant": 1.5}, ["combo"]),
    ("s13", "一条条追着看完", {"combo": 1.5, "spells": 1.0, "enchant": 1.5}, []),
    ("h1c2", "好，什么时候，现在就去报名", {"aggro": 2.0, "blink": 1.5, "enchant": 1.5}, []),
    # --- tribal 补 3 处 ---
    ("s15", "先问问邻居是不是拿错了", {"politics": 1.0, "clonesteal": 1.0, "tribal": 1.5}, ["enchant"]),
    ("s04", "临时决定去哪儿走走", {"chaos": 2.5, "ramp": 1.5, "tribal": 1.0}, []),
    ("s09", "看谁在线就跟着谁的安排走", {"politics": 2.0, "voltron": 1.5, "tribal": 1.0}, []),
    # --- politics 补 1 处，同时给 s15 的「投诉」补上被削掉的 aggro ---
    ("s15", "直接找客服投诉", {"aggro": 2.0, "politics": 1.5}, []),
    # --- 最后一轮：combo ×3、stompy ×1（槽位从过采样的 aggro/chaos 里腾）---
    ("s10", "压根忘了这事", {"chaos": 1.5, "blink": 1.0, "combo": 1.5}, ["stompy"]),
    ("h1c1", "直接挑一个方向往里走", {"chaos": 1.5, "aggro": 1.5, "combo": 1.0}, []),
    ("h1b1", "全塞进一个箱子封起来", {"stax": 1.5, "counters": 1.0, "combo": 1.0}, ["grave"]),
    ("s03", "堆得挺高", {"chaos": 1.5, "grave": 2.5, "stompy": 1.0}, ["counters"]),
]
NEW_S15 = {"t": "看看身边人上次是怎么弄的，照着来一遍",
           "s": {"clonesteal": 2.0, "politics": 1.5, "artifacts": 1.0}}


def main() -> int:
    data = json.loads(BANK.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data["questions"]}
    added = 0

    for qid, prefix, vec, drops in PATCH:
        if prefix == "__append__":
            opts = by_id[qid]["opts"]
            if not any(o["t"] == NEW_S15["t"] for o in opts):  # 幂等：不重复追加
                opts.append(dict(NEW_S15))
                added += 1
            continue
        target = next((o for o in by_id[qid]["opts"] if o["t"].startswith(prefix)), None)
        if target is None:
            print(f"✗ 找不到选项：{qid} / {prefix}")
            return 1
        for axis in drops:
            target["s"].pop(axis, None)
        if vec is not None:
            target["s"] = dict(vec)

    BANK.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    hits: Counter = Counter()
    for q in data["questions"]:
        for o in q["opts"]:
            for a in o["s"]:
                hits[a] += 1
    print(f"新增选项 {added} 个。各轴引用数：")
    for a in AXES:
        c = hits.get(a, 0)
        print(f"  {a:<11} {c:>3}" + ("  ← 仍不足" if c < 12 else ""))
    short = [a for a in AXES if hits.get(a, 0) < 12]
    print(f"\n轴引用 {sum(hits.values())} 次，不足 12 的轴：{short or '无'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
