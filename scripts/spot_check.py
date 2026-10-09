#!/usr/bin/env python3
"""抽查介绍文质量。用法：python spot_check.py <文件编号> [条目数]"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")


def main() -> None:
    index = sys.argv[1] if len(sys.argv) > 1 else "2"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    path = DATA / f"descriptions_{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    print(f"# {path.name} —— {len(data)} 条\n")
    for i, (name, entry) in enumerate(data.items()):
        if i >= limit:
            break
        print(f"── {name}")
        print(f"   定位：{entry.get('tagline')}")
        print(f"   介绍：{entry.get('intro')}")
        print(f"   怎么组：{entry.get('build')}")
        print()


if __name__ == "__main__":
    main()
