#!/usr/bin/env python3
"""估算主将的「牌面理解成本」与「整套造价档位」。

理解成本只量**正文**（剔除括号里的提示文本）——提示文本是规则说明，
不该算进「这张牌好不好读」。操作负担由玩法轴决定，在 build_commanders.py 里合成。
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
    """去掉括号内的提示文本（含嵌套），返回（正文, 去掉的字符数）。"""
    if not text:
        return "", 0
    out: list[str] = []
    depth = 0
    removed = 0
    for char in text:
        if char == "(":
            depth += 1
            removed += 1
        elif char == ")" and depth > 0:
            depth -= 1
            removed += 1
        elif depth > 0:
            removed += 1
        else:
            out.append(char)
    return "".join(out), removed


def text_level(text: str, keywords: list[str] | None) -> tuple[float, dict]:
    """牌面理解成本（1 起，越大越难读）。"""
    body, removed = strip_reminder(text or "")
    triggers = body.count("Whenever") + body.count("At the beginning") + body.count("When ")
    activated = len(ACTIVATED.findall(body))
    choices = body.count("choose") + body.count("may")
    raw = len(body) / 110.0 + triggers * 0.55 + activated * 0.45 + choices * 0.28
    return 1.0 + raw * 0.55, {
        "raw_len": len(text or ""),
        "body_len": len(body),
        "removed": removed,
        "triggers": triggers,
        "activated": activated,
        "choices": choices,
        "keywords": len(keywords or []),
    }


def budget_from_price(price, bracket_mode: int) -> tuple[float, str]:
    try:
        value = float(price)
    except (TypeError, ValueError):
        value = 0.0
    if value < 1:
        base = 1.0
    elif value < 3:
        base = 2.0
    elif value < 8:
        base = 3.0
    elif value < 20:
        base = 4.0
    else:
        base = 5.0
    adjust = 1.0 if bracket_mode >= 4 else (-0.5 if bracket_mode <= 2 else 0.0)
    return max(1.0, min(5.0, base + adjust)), f"单价${value:.2f} 基准{base:.1f} B{bracket_mode} {adjust:+.1f}"


def bracket_mode(bracket_counts) -> int:
    if not bracket_counts:
        return 3
    return int(max(bracket_counts.items(), key=lambda kv: kv[1])[0])


def main() -> None:
    scry = json.loads((DATA / "commanders_scryfall.json").read_text(encoding="utf-8"))
    profiles = json.loads((DATA / "commander_profiles.json").read_text(encoding="utf-8"))

    lookup = {}
    for name, card in scry.items():
        lookup[name] = card
        lookup.setdefault(name.split(" // ")[0], card)
        lookup.setdefault(name.split(",")[0].strip(), card)

    rows = []
    for name, prof in profiles.items():
        card = lookup.get(name) or lookup.get(name.split(" // ")[0]) or {}
        level, detail = text_level(card.get("oracle_text"), card.get("keywords"))
        bmode = bracket_mode(prof.get("bracket_counts"))
        budget, why = budget_from_price(card.get("usd"), bmode)
        rows.append({
            "name": name,
            "text_level": round(level, 3),
            "text_detail": detail,
            "budget_raw": round(budget, 3),
            "budget_reason": why,
            "bracket_mode": bmode,
            "usd": card.get("usd"),
        })

    (DATA / "complexity_budget.json").write_text(
        json.dumps({r["name"]: r for r in rows}, ensure_ascii=False, indent=2),
        encoding="utf-8")

    levels = sorted(r["text_level"] for r in rows)
    print(f"牌面理解成本范围 {levels[0]:.2f} ~ {levels[-1]:.2f}，"
          f"中位 {levels[len(levels) // 2]:.2f}")
    removed = [r["text_detail"]["removed"] for r in rows]
    print(f"提示文本：平均去掉 {sum(removed) / len(removed):.0f} 字，最多 {max(removed)} 字")

    probes = ["Wilhelt, the Rotcleaver", "Atraxa, Praetors' Voice",
              "Grand Arbiter Augustin IV", "Brago, King Eternal", "Krenko, Mob Boss",
              "The First Sliver"]
    print("\n重点主将（仅牌面理解成本，操作负担待合成）：")
    for probe in probes:
        row = next((r for r in rows if r["name"] == probe), None)
        if row:
            d = row["text_detail"]
            print(f"  {probe[:34]:<34} {row['text_level']:.2f}  "
                  f"（正文 {d['body_len']} 字，去掉提示 {d['removed']} 字，"
                  f"触发 {d['triggers']}，起动 {d['activated']}）")


if __name__ == "__main__":
    main()
