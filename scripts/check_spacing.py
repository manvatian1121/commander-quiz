#!/usr/bin/env python3
"""检查介绍文里「中文（English）」两侧的空格残留。"""
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
PATTERN = re.compile(r".{6}（[A-Za-z][^）]*）.{6}")


def main() -> None:
    for fname in ["descriptions_4.json", "descriptions_5.json",
                  "descriptions_6.json", "descriptions_7.json"]:
        path = DATA / fname
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        samples, spaced = [], 0
        for entry in data.values():
            for field in ("intro", "build"):
                text = entry.get(field) or ""
                for match in PATTERN.finditer(text):
                    snippet = match.group(0)
                    if re.search(r"）\s", snippet) or re.search(r"\s（", snippet):
                        spaced += 1
                    if len(samples) < 3:
                        samples.append(snippet)
        print(f"\n{fname}：疑似空格残留 {spaced} 处")
        for snippet in samples:
            print(f"   {snippet!r}")


if __name__ == "__main__":
    main()
