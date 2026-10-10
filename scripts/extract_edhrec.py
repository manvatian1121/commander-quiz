#!/usr/bin/env python3
"""从 EDHREC JSON 中提取主将排名列表。"""
from __future__ import annotations

import json
import pathlib



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
DATA = pathlib.Path(ROOT / "data")


def find_cardlists(node, found=None):
    """递归找形如 [{'name':...}, ...] 的列表。"""
    if found is None:
        found = []
    if isinstance(node, dict):
        for value in node.values():
            find_cardlists(value, found)
    elif isinstance(node, list):
        dicts = [item for item in node if isinstance(item, dict)]
        if dicts and any("name" in item for item in dicts):
            found.append(node)
        for item in node:
            find_cardlists(item, found)
    return found


def describe(name: str) -> None:
    path = DATA / name
    payload = json.loads(path.read_text(encoding="utf-8"))
    lists = find_cardlists(payload)
    print(f"\n{'=' * 78}\n{name}  -> {len(lists)} 个候选列表")
    for index, group in enumerate(lists):
        keys = sorted({key for item in group[:5] for key in item})
        print(f"  [{index}] len={len(group)} keys={keys}")
        sample = group[0]
        print(f"      sample: {json.dumps(sample, ensure_ascii=False)[:400]}")


if __name__ == "__main__":
    for filename in ["commanders_year.json", "commanders_month.json", "commanders_week.json"]:
        describe(filename)
