#!/usr/bin/env python3
"""汇总 EDHREC 排名，输出候选主将清单。"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

DATA = pathlib.Path(ROOT / "data")


def find_ranked(node, found=None):
    if found is None:
        found = []
    if isinstance(node, dict):
        for value in node.values():
            find_ranked(value, found)
    elif isinstance(node, list):
        if node and all(isinstance(i, dict) and "rank" in i and "num_decks" in i for i in node[:3]):
            found.append(node)
        for item in node:
            find_ranked(item, found)
    return found


def load(filename: str):
    payload = json.loads((DATA / filename).read_text(encoding="utf-8"))
    groups = find_ranked(payload)
    return groups[0] if groups else []


if __name__ == "__main__":
    year = load("commanders_year.json")
    month = load("commanders_month.json")
    week = load("commanders_week.json")

    merged: dict[str, dict] = {}
    for label, group in (("year", year), ("month", month), ("week", week)):
        for entry in group:
            record = merged.setdefault(entry["name"], {"name": entry["name"], "slug": entry["slug"]})
            record[f"{label}_rank"] = entry["rank"]
            record[f"{label}_decks"] = entry["num_decks"]

    rows = sorted(merged.values(), key=lambda r: r.get("year_rank", 999))
    (DATA / "edhrec_candidates.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    for index, record in enumerate(rows):
        print(f"{index + 1:>4} {record.get('year_rank', '-'):>4} "
              f"{record.get('month_rank', '-'):>4} {record.get('week_rank', '-'):>4} "
              f"{record.get('year_decks', 0):>9}  {record['name']}")
    print(f"\n合计 {len(rows)} 位（年榜 {len(year)} / 月榜 {len(month)} / 周榜 {len(week)}）")
    print(f"已写入 edhrec_candidates.json")
