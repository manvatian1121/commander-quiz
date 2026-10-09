#!/usr/bin/env python3
"""实施校对后的全部裁决：量词、措辞、缺宾语、期限矛盾。

每一处都来自两个校对 agent 的「待裁量」清单，决定与理由记录在此。
"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

EDITS = [
    # (bank, 题号, 字段, 原文, 改后, 理由, 新的轴得分 or None)
    ("bank4", "s58", "q",
     "要买一把每天都要用的东西（键盘、耳机、炒锅），你怎么选？",
     "要买一件每天都要用的东西（键盘、耳机、炒锅），你怎么选？",
     "「一把耳机」「一把炒锅」量词错误；题干用「一件」，选项里跟改。", None),
    ("bank4", "s58", "opt",
     "直接上贵的那把，能用十年就不用第二把",
     "直接上贵的那个，能用十年就不用第二个",
     "同上，量词统一成「个」。", None),
    ("bank4", "s58", "opt",
     "最结实的那把，摔坏了算我输",
     "最结实的那个，摔坏了算我输",
     "同上，量词统一成「个」。", None),

    ("bank5", "h5a1", "opt",
     "马上找人再来一场，先把状态练热",
     "马上找人再来一场，先热热身",
     "「练热」不是常见搭配，改成「先热热身」。", None),

    ("bank1", "h1a2", "opt",
     "把时间记住，下次约他我提前半小时说",
     "记住了，下次约他我把时间说早半小时",
     "原句「提前半小时说」缺宾语、两种读法；本意是把约定时间说早半小时留缓冲，"
     "与 stax 2.5（自设规矩）一致，写清楚。", None),

    ("bank2", "s29", "opt",
     "不着急，先放着吧，隔几天翻出来弄两下，慢慢就磨完了",
     "不着急，先放着吧，拖到最后一天再一口气弄完",
     "题干是「三天后要交」，「隔几天」≥3 天与期限矛盾；改成「拖到最后一天」"
     "既保留「不在意/不慌」的落点，又不与期限冲突。",
     {"drain": 2.0, "chaos": 1.5}),
]


def main() -> int:
    changed = 0
    by_bank: dict[str, dict] = {}
    for bank in {e[0] for e in EDITS}:
        path = DATA / f"{bank}.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        by_bank[bank] = {"path": path, "payload": payload,
                         "by_id": {q["id"]: q for q in payload["questions"]}}

    for bank, qid, field, old, new, why, axes in EDITS:
        entry = by_bank[bank]
        q = entry["by_id"].get(qid)
        if not q:
            print(f"✗ 找不到 {bank}/{qid}")
            return 1
        if field == "q":
            if q["q"] != old:
                print(f"✗ {qid} 题干与预期不符：{q['q']!r}")
                return 1
            q["q"] = new
        else:
            target = next((o for o in q["opts"] if o["t"] == old), None)
            if target is None:
                print(f"✗ {qid} 找不到选项：{old!r}")
                return 1
            target["t"] = new
            if axes is not None:
                target["s"] = axes
        print(f"  [{bank}] {qid}：{old}")
        print(f"        → {new}")
        print(f"        理由：{why}")
        changed += 1

    for entry in by_bank.values():
        entry["path"].write_text(
            json.dumps(entry["payload"], ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✓ 共修改 {changed} 处")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
