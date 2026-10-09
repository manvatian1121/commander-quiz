#!/usr/bin/env python3
"""修回被「Plot → 谋划」误替换弄坏的牌名。

`Gollum, Patient Plotter` 里的 `Plot` 被替换成了「谋划」。
原因是替换没加词边界——和之前 ramp 把 `Sky Rampart` 弄坏是同一类错误。
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

# 与拉丁字母相邻的「谋划」= 误替换，还原成 Plot
BAD = re.compile(r"(?<=[A-Za-z])谋划|谋划(?=[A-Za-z])")


def main() -> int:
    total = 0
    for index in range(1, 17):
        path = DATA / f"descriptions_{index}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        hits = 0
        for commander, entry in data.items():
            for field in ("tagline", "intro", "build"):
                text = entry.get(field)
                if not text or "谋划" not in text:
                    continue
                new, n = BAD.subn("Plot", text)
                if n:
                    entry[field] = new
                    hits += n
                    print(f"  [{index}] {commander[:32]}.{field}：还原 {n} 处")
        if hits:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        total += hits
    print(f"\n✓ 共还原 {total} 处")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
