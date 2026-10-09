#!/usr/bin/env python3
"""统计注入中文名之后，有多少条介绍文超出了字数上限。"""
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
LIMITS = {"tagline": 20, "intro": 120, "build": 170}


def visible(text: str) -> int:
    return len(re.sub(r"\s+", "", text or ""))


over: list[tuple[str, str, int, int]] = []
for index in range(1, 9):
    path = DATA / f"descriptions_{index}.json"
    if not path.exists():
        continue
    data = json.loads(path.read_text(encoding="utf-8"))
    for commander, entry in data.items():
        for field, limit in LIMITS.items():
            text = entry.get(field) or ""
            length = visible(text)
            if length > limit:
                over.append((f"[{index}] {commander}", field, length, length - limit))

print(f"超出上限的条目：{len(over)} 处")
by_batch: dict[str, int] = {}
for source, field, length, excess in over:
    batch = source.split("]")[0] + "]"
    by_batch[batch] = by_batch.get(batch, 0) + 1
print(f"按批次：{by_batch}")
print(f"超出幅度：最大 {max((o[3] for o in over), default=0)} 字，"
      f"中位 {sorted(o[3] for o in over)[len(over) // 2] if over else 0} 字")
print("\n最严重的 20 条：")
for source, field, length, excess in sorted(over, key=lambda o: -o[3])[:20]:
    print(f"  {source:<44} {field:<7} {length:>4} 字（超 {excess}）")
