#!/usr/bin/env python3
"""从各来源的候选里挑出最终要并入池子的新主将。"""
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

TARGET_ADD = int(sys.argv[1]) if len(sys.argv) > 1 else 90
COLOR_ORDER = "WUBRG"


def load(name: str, default):
    path = DATA / name
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def color_code(identity) -> str:
    if not identity:
        return "C"
    return "".join(c for c in COLOR_ORDER if c in identity) or "C"


def main() -> int:
    pool = load("commanders.json", {"commanders": []})
    profiles = load("commander_profiles.json", {})
    in_pool = {c["en"] for c in pool["commanders"]}

    merged: dict[str, dict] = {}
    for fname, source in (("new_candidates.json", "新主将"),
                          ("similar_candidates.json", "相似推荐")):
        for row in load(fname, []):
            name = row.get("edhrec_name") or row.get("name")
            if not name or name in in_pool:
                continue
            record = merged.setdefault(name, {"name": name, "sources": []})
            record["sources"].append(source)
            record["num_decks"] = max(record.get("num_decks") or 0, row.get("num_decks") or 0)
            record["rank"] = row.get("rank") or record.get("rank")
            record["released_at"] = row.get("released_at") or record.get("released_at")
            record["color_identity"] = row.get("color_identity") or record.get("color_identity")

    # 已经抓过档案、但没进池的也一并作为候选（早先抓过 151 份档案）
    for name, prof in profiles.items():
        if name in in_pool or name in merged:
            continue
        merged[name] = {
            "name": name, "sources": ["旧档案"],
            "num_decks": prof.get("num_decks") or 0,
            "rank": prof.get("all_time_rank") or prof.get("rank"),
            "released_at": None,
            "color_identity": prof.get("color_identity"),
        }

    rows = sorted(merged.values(), key=lambda r: -(r.get("num_decks") or 0))
    print(f"候选合计 {len(rows)} 位（已排除池内 {len(in_pool)} 位）")
    print(f"来源分布：{Counter(s for r in rows for s in r['sources'])}")

    picks = rows[:TARGET_ADD]
    print(f"\n选定新增 {len(picks)} 位")

    # 覆盖检查
    existing_colors = Counter(c["colors"] for c in pool["commanders"])
    added_colors = Counter(color_code(r.get("color_identity")) for r in picks)
    print(f"\n现有池颜色分布（前 8）：{existing_colors.most_common(8)}")
    print(f"新增颜色分布（前 8）：{added_colors.most_common(8)}")

    print(f"\n新增名单（按套牌数）：")
    for row in picks:
        print(f"  {row['num_decks']:>6} 副  #{str(row.get('rank')):>5}  "
              f"{color_code(row.get('color_identity')):<6} "
              f"{(row.get('released_at') or ''):<10} {row['name'][:40]}"
              f"   [{'/'.join(row['sources'])}]")

    (DATA / "new_pool_members.json").write_text(
        json.dumps([r["name"] for r in picks], ensure_ascii=False, indent=2),
        encoding="utf-8")
    print(f"\n已写出 new_pool_members.json（{len(picks)} 位）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
