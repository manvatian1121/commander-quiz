#!/usr/bin/env python3
"""把草稿里的 {{English Name}} 占位替换成「中文名（English Name）」，落盘 descriptions_2.json。"""
from __future__ import annotations

import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
sys.stdout.reconfigure(encoding="utf-8")

from draft_descriptions_2 import CONTENT  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

DATA = pathlib.Path(ROOT / "data")
OUT = DATA / "descriptions_2.json"
PLACEHOLDER = re.compile(r"\{\{(.+?)\}\}")


def main() -> int:
    zh = json.loads((DATA / "card_zh_b2.json").read_text(encoding="utf-8"))
    data: dict[str, dict[str, str]] = {}
    missing: list[str] = []
    for commander, fields in CONTENT.items():
        entry: dict[str, str] = {}
        for key in ("tagline", "intro", "build"):
            text = fields[key]

            def sub(match: re.Match[str]) -> str:
                name = match.group(1)
                cn = zh.get(name, "")
                if not cn:
                    missing.append(name)
                    return name
                return f"{cn}（{name}）"

            entry[key] = PLACEHOLDER.sub(sub, text)
        data[commander] = entry

    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ 写入 {OUT}：{len(data)} 位主将")
    if missing:
        print(f"⚠ 没查到中文名的：{sorted(set(missing))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
