#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性把 bank1.json 的轴覆盖配平到每轴 ≥12（含新增选项与个别选项的轴增删）。

做法：按 (题目 id, 选项序号) 定位，做三类原子操作：
  - add_opt  : 追加一个新选项（5 选项题）
  - set      : 覆盖该选项的轴向量
  - add/drop : 单个轴的增减

跑一次即可；跑完用 check_bank1.py 验收。所有改动的余弦相似度影响已手工核算。
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

# ---- 新增选项 -------------------------------------------------------------
NEW_OPTS: dict[str, dict] = {
    "s04": {"t": "自己一个人去跑一趟，顺手冲一下这周的目标",
            "s": {"blink": 1.5, "wide": 1.5, "voltron": 1.0}},
    "s10": {"t": "顺便把冰箱清一遍，翻出几样能先处理掉的",
            "s": {"blink": 1.5, "wide": 1.5, "spells": 1.0}},
}

# ---- 轴向量覆盖 -----------------------------------------------------------
SET: dict[tuple[str, int], dict[str, float]] = {
    # voltron：三个选项补上，都是「自己扛 / 按自己的标准来」的语义
    ("s05", 1): {"aggro": 2.0, "voltron": 2.0},
    ("s07", 2): {"aggro": 2.0, "spells": 1.5, "voltron": 1.0},
    ("h1a3", 2): {"removal": 2.0, "ramp": 1.5, "voltron": 1.0},
    # stompy：补两处，都从偏「硬、不拐弯」的选项里取
    ("s07", 4): {"stompy": 2.0, "chaos": 1.0},
    ("s13", 4): {"chaos": 2.0, "stompy": 2.5},
    # spells
    ("s05", 3): {"tribal": 2.5, "counters": 1.0, "spells": 1.0},
    # enchant
    ("h1b2", 2): {"artifacts": 2.0, "ramp": 1.5, "enchant": 1.5},
    ("h1c2", 1): {"aggro": 2.0, "blink": 1.5, "enchant": 1.0},
    # grave
    ("h1b1", 4): {"stax": 1.5, "counters": 1.0, "grave": 1.0},
    # tribal
    ("h1b3", 2): {"grave": 2.0, "artifacts": 2.0, "tribal": 1.0},
    # clonesteal
    ("h1c1", 1): {"blink": 2.0, "drain": 1.5, "clonesteal": 1.5},
    ("h1c2", 4): {"counters": 2.0, "stax": 1.0, "clonesteal": 1.0},
    ("s16", 2): {"artifacts": 2.5, "voltron": 1.5, "clonesteal": 2.0},
    # politics
    ("h1b1", 1): {"removal": 1.5, "stax": 1.5, "politics": 1.5},
    ("s16", 4): {"politics": 2.0, "blink": 1.5, "clonesteal": 1.0},
}

# ---- 单轴增删（用来把过采样的轴腾出来）------------------------------------
DROP: list[tuple[str, int, str]] = [
    ("s07", 4, "stax"), ("s13", 2, "aggro"), ("s15", 2, "stax"), ("s16", 1, "stax"),
    ("h1c1", 4, "blink"), ("h1b1", 1, "blink"), ("h1c2", 3, "drain"), ("h1c3", 3, "blink"),
    ("s03", 4, "stax"), ("s04", 2, "drain"), ("s06", 2, "chaos"), ("s12", 3, "drain"),
    ("s01", 2, "artifacts"), ("s01", 3, "counters"), ("s01", 1, "politics"),
]
ADD: list[tuple[str, int, str, float]] = [
    ("h1c1", 4, "wide", 1.0),
]


def main() -> int:
    data = json.loads(BANK.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data["questions"]}

    for qid, opt in NEW_OPTS.items():
        opts = by_id[qid]["opts"]
        if not any(o["t"] == opt["t"] for o in opts):  # 幂等：不重复追加
            opts.append(dict(opt))

    for (qid, idx), vec in SET.items():
        by_id[qid]["opts"][idx - 1]["s"] = dict(vec)

    for qid, idx, axis in DROP:
        by_id[qid]["opts"][idx - 1]["s"].pop(axis, None)

    for qid, idx, axis, val in ADD:
        by_id[qid]["opts"][idx - 1]["s"][axis] = val

    BANK.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    hits: Counter = Counter()
    for q in data["questions"]:
        for o in q["opts"]:
            for a in o["s"]:
                hits[a] += 1
    print("配平后各轴引用数：")
    for a in AXES:
        print(f"  {a:<11} {hits.get(a, 0):>3}" + ("  ← 仍不足" if hits.get(a, 0) < 12 else ""))
    short = [a for a in AXES if hits.get(a, 0) < 12]
    print(f"\n题数 {len(data['questions'])}，选项 {sum(len(q['opts']) for q in data['questions'])} 个，"
          f"轴引用 {sum(hits.values())} 次，不足 12 的轴：{short or '无'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
