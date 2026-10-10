#!/usr/bin/env python3
"""生成候选主将可读摘要，供筛选与打标签。"""
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


def color_code(identity: list[str]) -> str:
    if not identity:
        return "C"
    return "".join(c for c in COLOR_ORDER if c in identity)


def build_lookup(scry: dict) -> dict:
    """键名归一化：EDHREC 名 → Scryfall 卡。处理 'A // B' 搭档/双面牌。"""
    lookup = dict(scry)
    for name, card in scry.items():
        head = name.split(" // ")[0]
        lookup.setdefault(head, card)
        core = head.split(",")[0].strip()
        lookup.setdefault(core, card)
    return lookup


def main() -> None:
    scry = json.loads((DATA / "commanders_scryfall.json").read_text(encoding="utf-8"))
    cands = json.loads((DATA / "edhrec_candidates.json").read_text(encoding="utf-8"))
    lookup = build_lookup(scry)

    lines = []
    missing = []
    for record in cands:
        full = record["name"]
        card = (lookup.get(full)
                or lookup.get(full.split(" // ")[0])
                or lookup.get(full.split(",")[0].strip()))
        if not card:
            missing.append(full)
            lines.append(f"### {full}  [数据缺失]\n")
            continue
        rank = record.get("year_rank", "-")
        text = " ".join((card["oracle_text"] or "").split())
        lines.append(
            f"### {record['name']}\n"
            f"- 年榜#{rank} 月度#{record.get('month_rank', '-')} 周榜#{record.get('week_rank', '-')}"
            f" | 套牌数 {record.get('year_decks', 0)}\n"
            f"- 颜色 {color_code(card['color_identity'])} | MV {card['cmc']} | {card['type_line']}\n"
            f"- 系列 {card['set_name']} ({card['released_at']}) | 参考价 ${card['usd']}\n"
            f"- 牌面 {text[:260]}\n")

    out = DATA / "candidates_digest.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"写入 {out}，{len(lines)} 条")
    if missing:
        print(f"⚠ 仍未命中 {len(missing)} 条：")
        for name in missing:
            print(f"  ✗ {name}")
    else:
        print("✓ 全部命中")


if __name__ == "__main__":
    main()
