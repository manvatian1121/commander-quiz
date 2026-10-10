#!/usr/bin/env python3
"""打印观察词在文案里的上下文，判断是行业术语还是正常用词。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
WORDS = sys.argv[1:] or ["引擎", "加速", "发现"]


def main() -> None:
    for word in WORDS:
        print(f"\n=== 「{word}」===")
        for index in range(1, 9):
            path = DATA / f"descriptions_{index}.json"
            if not path.exists():
                continue
            data = json.loads(path.read_text(encoding="utf-8"))
            for commander, entry in data.items():
                for field in ("intro", "build"):
                    text = entry.get(field) or ""
                    start = 0
                    while True:
                        idx = text.find(word, start)
                        if idx < 0:
                            break
                        print(f"  [{index}] {commander[:26]:<26} "
                              f"…{text[max(0, idx - 18):idx + 18]}…")
                        start = idx + len(word)


if __name__ == "__main__":
    main()
