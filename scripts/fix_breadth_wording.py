#!/usr/bin/env python3
"""修广度题 s62b 的两处措辞问题。

① B「主攻一件，再养一件当退路」——「养」搭配不当：
   「养」的宾语需要是长期喂养才能成长的东西（孩子、花、账号），「一件事」不是；
   而且「养一件当退路」读着像「养备胎」，量词的指代会从「事」漂到「对象」。
   A 用的是「留一件」，同一个量词不该换动词。

② E「哪一边都不想站」——题干问的是「好几件事」，「边」在题干里没有指代对象，
   读起来答非所问。改成落在「事」上。
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"D:\万智\commander-quiz\data")

FIXES = [
    ("主攻一件，再养一件当退路",
     "主攻一件，另一件捎带着做",
     "「养」搭配不当且易读成「养备胎」；「捎带着做」直接点出「一主一次」"),
    ("哪一边都不想站，我自己那一套够用就行",
     "哪件都不想长期挂着，缺什么到时候现搭",
     "题干说的是「事」，「边」没有指代对象；改成落在「事」上，仍表达「不靠现成框架」"),
]


def main() -> int:
    path = DATA / "bank4.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    target = next((q for q in payload["questions"] if q["id"] == "s62b"), None)
    if target is None:
        print("✗ 找不到 s62b")
        return 1

    print(f"题干：{target['q']}\n")
    changed = 0
    for old, new, why in FIXES:
        hit = False
        for opt in target["opts"]:
            if opt["t"] == old:
                opt["t"] = new
                print(f"  {old}")
                print(f"  → {new}")
                print(f"    理由：{why}\n")
                changed += 1
                hit = True
        if not hit:
            print(f"✗ 找不到：{old!r}")
            return 1

    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ 修正 {changed} 处，改后全题：")
    for i, opt in enumerate(target["opts"]):
        print(f"  {'ABCDE'[i]}. {opt['t']}　（bw={opt['bw']}）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
