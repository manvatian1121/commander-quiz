#!/usr/bin/env python3
"""补丁：把 salt 约束正确挂到选项层，并补充咸度容忍度出题点。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
PATH = DATA / "questions.json"

PATCHES = {
    # 题目 id -> 每个选项的 salt 容忍值（1=完全受不了 5=就爱被讨厌）
    13: [1, 2, 5, 3],
    27: [1, 2, 4, 5],
    33: [1, 2, 4, 5],
    95: [4, 2, 3, 2],
}


def main() -> int:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    changed = 0
    for question in data["questions"]:
        qid = question["id"]
        # 先清掉误挂在题目层的 cval
        if "cval" in question:
            del question["cval"]
            changed += 1
        if qid in PATCHES:
            values = PATCHES[qid]
            if len(values) != len(question["opts"]):
                print(f"✗ Q{qid} 选项数 {len(question['opts'])} 与补丁 {len(values)} 不符")
                return 1
            for opt, value in zip(question["opts"], values):
                opt.setdefault("cval", {})["salt"] = value
                changed += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✓ 应用 {changed} 处修改")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
