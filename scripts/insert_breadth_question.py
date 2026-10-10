#!/usr/bin/env python3
"""插入「广度题」：探测玩家想要几个颜色方向。

背景：现有四道颜色题每题只能给一个颜色，玩家永远答不出「我五色都喜欢」，
导致五色主将（池中最大的一档，31 位）进前三的比例只有 2.9%，仅为应得的一半。

这道题不直接问颜色，而是问「你想同时推几个方向」，映射到颜色数量：
  专注一件 → 单色 / 主次两件 → 双色 / 三件轮推 → 三色
  什么都想碰 → 五色 / 哪边都不站 → 无色

选项用新的 `bw` 字段（breadth weight，0~1）表达，不占用 `col`。
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"D:\万智\commander-quiz\data")
PATH = DATA / "bank4.json"

QUESTION = {
    "id": "s62b",
    "sec": "taste",
    "q": "手头同时堆着好几件事的时候，你最喜欢的状态是哪种？",
    "next": "s63",
    "opts": [
        {"t": "一次只留一件，做深做透，别的先搁着",
         "s": {"control": 2.0, "voltron": 1.5}, "bw": 0.2},
        {"t": "主攻一件，再养一件当退路",
         "s": {"combo": 2.0, "counters": 1.0}, "bw": 0.4},
        {"t": "三件换着推，哪件顺手先推哪件",
         "s": {"blink": 1.5, "politics": 1.5}, "bw": 0.6},
        {"t": "什么都想碰一点，不喜欢把自己框在一个方向上",
         "s": {"wide": 2.0, "clonesteal": 1.0}, "bw": 1.0},
        {"t": "哪一边都不想站，我自己那一套够用就行",
         "s": {"artifacts": 2.5, "stax": 1.0}, "bw": 0.0},
    ],
}


def main() -> int:
    payload = json.loads(PATH.read_text(encoding="utf-8"))
    questions = payload["questions"]
    ids = [q["id"] for q in questions]

    if "s62b" in ids:
        print("已存在 s62b，跳过插入")
        return 0

    index = ids.index("s62")
    if questions[index].get("next") != "s63":
        print(f"✗ s62.next 是 {questions[index].get('next')!r}，与预期不符")
        return 1

    questions[index]["next"] = "s62b"
    questions.insert(index + 1, QUESTION)
    PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"✓ 已在 s62 之后插入 s62b（bank4 现 {len(questions)} 题）")
    print(f"  跳转链：s62 -> s62b -> s63")
    print(f"\n题干：{QUESTION['q']}")
    for i, opt in enumerate(QUESTION["opts"]):
        print(f"  {'ABCDE'[i]}. {opt['t']}")
        print(f"       bw={opt['bw']}（{'无色' if opt['bw'] == 0 else str(round(opt['bw'] * 5)) + ' 个方向'}）"
              f"  轴={opt['s']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
