#!/usr/bin/env python3
"""为主将池生成「难懂指数」诊断报告，找出估算方法与人工判断冲突的地方。

难度估算 = 牌面理解成本（这张牌好不好读）
         + 操作负担（这套牌好不好开）
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

ACTIVATED = re.compile(r"\{[^}]*\}\s*[^:]*:")


def strip_reminder(text: str) -> tuple[str, int]:
    """去掉括号内的提示文本（reminder text），返回（正文, 被去掉的字符数）。"""
    if not text:
        return "", 0
    out, depth, removed = [], 0, 0
    for char in text:
        if char == "(":
            depth += 1
            removed += 1
        elif char == ")":
            depth = max(0, depth - 1)
            removed += 1
        elif depth == 0:
            out.append(char)
        else:
            removed += 1
    return "".join(out), removed


def main() -> None:
    scry = json.loads((DATA / "commanders_scryfall.json").read_text(encoding="utf-8"))
    payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))

    lookup = {}
    for name, card in scry.items():
        lookup[name] = card
        lookup.setdefault(name.split(" // ")[0], card)
        lookup.setdefault(name.split(",")[0].strip(), card)

    rows = []
    for entry in payload["commanders"]:
        card = lookup.get(entry["en"]) or lookup.get(entry["en"].split(" // ")[0]) or {}
        raw_text = card.get("oracle_text") or ""
        body, removed = strip_reminder(raw_text)
        rows.append({
            "en": entry["en"], "zh": entry["zh"],
            "current": entry["complexity"],
            "raw_len": len(raw_text),
            "body_len": len(body),
            "removed": removed,
            "removed_pct": round(removed / len(raw_text) * 100, 1) if raw_text else 0,
            "vec": entry["vec"],
        })

    rows.sort(key=lambda r: -r["removed_pct"])
    print("=== 提示文本占比最高的 20 位（这些最可能被高估）===")
    print(f"{'占比':>6} {'原长':>5} {'正文':>5} {'现难度':>6}  主将")
    for row in rows[:20]:
        print(f"{row['removed_pct']:>5.1f}% {row['raw_len']:>5} {row['body_len']:>5} "
              f"{row['current']:>6}  {row['zh']} / {row['en']}")

    print("\n=== 提示文本占比最低的 12 位（这些最可能被低估）===")
    for row in rows[-12:]:
        print(f"{row['removed_pct']:>5.1f}% {row['raw_len']:>5} {row['body_len']:>5} "
              f"{row['current']:>6}  {row['zh']} / {row['en']}")

    # 人工判断与当前估算明显冲突的主将（抽查用）
    PROBES = ["Wilhelt, the Rotcleaver", "Atraxa, Praetors' Voice",
              "Grand Arbiter Augustin IV", "Krenko, Mob Boss", "Muldrotha, the Gravetide",
              "Niv-Mizzet, Parun", "Light-Paws, Emperor's Voice", "Y'shtola, Night's Blessed"]
    print("\n=== 重点主将诊断 ===")
    for probe in PROBES:
        row = next((r for r in rows if r["en"] == probe), None)
        if not row:
            continue
        axes = sorted(row["vec"].items(), key=lambda kv: -kv[1])[:4]
        print(f"\n  {row['zh']} / {row['en']}  现难度 {row['current']}/5")
        print(f"    牌面 {row['raw_len']} 字，其中提示文本 {row['removed']} 字"
              f"（{row['removed_pct']}%），正文仅 {row['body_len']} 字")
        print(f"    主要玩法轴：{[(a, v) for a, v in axes]}")

    (DATA / "complexity_diagnosis.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n已写出 complexity_diagnosis.json（{len(rows)} 位）")


if __name__ == "__main__":
    main()
