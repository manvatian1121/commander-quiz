#!/usr/bin/env python3
"""生成紧凑筛选总表：一行一位主将。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
COLOR_ORDER = "WUBRG"


def color_code(identity) -> str:
    if not identity:
        return "C"
    if isinstance(identity, str):
        identity = list(identity)
    return "".join(c for c in COLOR_ORDER if c in identity)


def top_tags(tag_counts, limit=4) -> str:
    if not tag_counts:
        return "-"
    ordered = sorted(tag_counts, key=lambda t: -(t.get("count") or 0))[:limit]
    return " ".join(f"{t['value']}({t['count']})" for t in ordered)


def bracket_shape(bracket_counts) -> str:
    if not bracket_counts:
        return "-"
    total = sum(bracket_counts.values()) or 1
    parts = [f"B{k}:{bracket_counts[k] * 100 // total}%"
             for k in sorted(bracket_counts) if bracket_counts[k] / total >= 0.15]
    return " ".join(parts)


def main() -> None:
    profiles = json.loads((DATA / "commander_profiles.json").read_text(encoding="utf-8"))
    cands = {c["name"]: c for c in json.loads(
        (DATA / "edhrec_candidates.json").read_text(encoding="utf-8"))}

    rows = []
    for name, prof in profiles.items():
        cand = cands.get(name, {})
        rows.append({
            "name": name,
            "year_rank": cand.get("year_rank", 9999),
            "all_time_rank": prof.get("all_time_rank") or 99999,
            "num_decks": prof.get("num_decks") or 0,
            "salt": round(prof.get("salt") or 0, 2),
            "colors": color_code(prof.get("color_identity") or []),
            "cmc": prof.get("cmc"),
            "tags": top_tags(prof.get("tag_counts")),
            "brackets": bracket_shape(prof.get("bracket_counts")),
        })

    rows.sort(key=lambda r: (r["year_rank"], r["all_time_rank"]))
    (DATA / "curation_table.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [f"{'#':>3} {'年':>4} {'历':>5} {'套牌':>6} {'咸':>5} {'色':>5} {'MV':>3} "
             f"{'Bracket':<22} 名称 | 标签"]
    for index, row in enumerate(rows, 1):
        year = row["year_rank"] if row["year_rank"] < 9999 else "-"
        lines.append(
            f"{index:>3} {str(year):>4} {row['all_time_rank']:>5} {row['num_decks']:>6} "
            f"{row['salt']:>5} {row['colors']:>5} {str(row['cmc']):>3} {row['brackets']:<22} "
            f"{row['name']} | {row['tags']}")
    text = "\n".join(lines)
    (DATA / "curation_report.txt").write_text(text, encoding="utf-8")
    print("写入 curation_report.txt")
    print(text)


if __name__ == "__main__":
    main()
