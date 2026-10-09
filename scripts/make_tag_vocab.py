#!/usr/bin/env python3
"""汇总 EDHREC 全量玩法标签词表及其覆盖的主将数。"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")


def main() -> None:
    profiles = json.loads((DATA / "commander_profiles.json").read_text(encoding="utf-8"))
    vocab: Counter = Counter()
    total_count: Counter = Counter()
    for prof in profiles.values():
        for tag in prof.get("tag_counts") or []:
            vocab[tag["value"]] += 1
            total_count[tag["value"]] += tag["count"]

    lines = [f"{'主将数':>5} {'标签总票':>8}  标签"]
    for value, appearances in vocab.most_common():
        lines.append(f"{appearances:>5} {total_count[value]:>8}  {value}")
    text = "\n".join(lines)
    (DATA / "tag_vocabulary.txt").write_text(text, encoding="utf-8")
    print(f"标签种类 {len(vocab)}，写入 tag_vocabulary.txt")
    print(text[:3000])


if __name__ == "__main__":
    main()
