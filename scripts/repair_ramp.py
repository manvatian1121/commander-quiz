#!/usr/bin/env python3
"""修复上一步的误替换。

`post_wave3_fixes.py` 用正则把正文里的 ramp 换成「法术力加速」时，
没有加词边界，结果把牌名里的 Ramp 片段也换了：
  Pramikon, Sky Rampart   → Pramikon, Sky 法术力加速art
  Rampaging Baloths       → 法术力加速aging Baloths
这里把所有「与拉丁字母相邻」的误替换还原，只保留真正独立的 ramp 被换掉的部分。
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
TERM = "法术力加速"


def repair(text: str) -> tuple[str, int]:
    fixed = 0
    # 后面紧跟拉丁字母 → 是词的一部分，还原成 Ramp（词首）
    new, n = re.subn(TERM + r"(?=[A-Za-z])", "Ramp", text)
    fixed += n
    text = new
    # 前面紧跟拉丁字母 → 词中，还原成 ramp
    new, n = re.subn(r"(?<=[A-Za-z])" + TERM, "ramp", text)
    fixed += n
    return new, fixed


def main() -> int:
    total = 0
    for index in range(1, 17):
        path = DATA / f"descriptions_{index}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        hits = 0
        for commander, entry in data.items():
            for field in ("intro", "build"):
                text = entry.get(field)
                if not text or TERM not in text:
                    continue
                new, n = repair(text)
                if n:
                    entry[field] = new
                    hits += n
                    print(f"  [{index}] {commander[:30]}.{field}：还原 {n} 处")
        if hits:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        total += hits
    print(f"\n✓ 共还原 {total} 处")

    # 复查：还有没有与拉丁字母相邻的
    leftover = []
    for index in range(1, 17):
        path = DATA / f"descriptions_{index}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for commander, entry in data.items():
            for field in ("intro", "build"):
                text = entry.get(field) or ""
                for match in re.finditer(r"[A-Za-z]" + TERM + r"|" + TERM + r"[A-Za-z]", text):
                    leftover.append((index, commander, field, match.group(0)))
    print(f"复查：仍与拉丁字母相邻的 {len(leftover)} 处")
    for item in leftover[:10]:
        print(f"  {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
