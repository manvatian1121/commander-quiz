#!/usr/bin/env python3
"""扫描中文名注入造成的损坏：括号嵌套、主将名被替换。

起因：Omo, Queen of Vesuva 的介绍里，「Vesuva」既是主将名的一部分，
又是搭配牌清单里的一张牌，注入器把主将名也替换成了「维苏瓦（Vesuva）」。
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

# 形如「中文（English（中文（English））…」的嵌套括号
NESTED = re.compile(r"（[^（）]*（[^（）]*）[^（）]*）")


def main() -> None:
    hits: list[tuple[str, str, str, str]] = []
    for index in range(1, 9):
        path = DATA / f"descriptions_{index}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for commander, entry in data.items():
            for field in ("tagline", "intro", "build"):
                text = entry.get(field) or ""
                for match in NESTED.finditer(text):
                    hits.append((f"descriptions_{index}", commander, field, match.group(0)))

    print(f"括号嵌套：{len(hits)} 处")
    for source, commander, field, snippet in hits[:20]:
        print(f"  {source} / {commander} / {field}")
        print(f"      {snippet}")
    return


if __name__ == "__main__":
    main()
