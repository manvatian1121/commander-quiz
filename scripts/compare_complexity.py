#!/usr/bin/env python3
"""对比新旧难度评分，检查误判是否修正、有无新的明显错误。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")


def main() -> None:
    old = {r["en"]: r for r in
           json.loads((DATA / "complexity_diagnosis.json").read_text(encoding="utf-8"))}
    payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    new = {c["en"]: c for c in payload["commanders"]}

    rows = []
    for name, card in new.items():
        before = (old.get(name) or {}).get("current")
        rows.append({
            "en": name, "zh": card["zh"],
            "before": before, "after": card["complexity"],
            "delta": card["complexity"] - (before or 0),
            "text": card.get("text_level"), "pilot": card.get("pilot_level"),
        })

    print("=== 变动最大的 16 位 ===")
    print(f"{'旧':>3} {'新':>3} {'牌面':>5} {'操作':>5}  主将")
    for row in sorted(rows, key=lambda r: -abs(r["delta"]))[:16]:
        arrow = "↑" if row["delta"] > 0 else "↓"
        print(f"{row['before']:>3} {row['after']:>3} {row['text']:>5} {row['pilot']:>5}  "
              f"{arrow} {row['zh']} / {row['en'][:34]}")

    print("\n=== 之前点名的问题主将 ===")
    probes = ["Wilhelt, the Rotcleaver", "Atraxa, Praetors' Voice",
              "Grand Arbiter Augustin IV", "Brago, King Eternal", "Krenko, Mob Boss",
              "The First Sliver", "Yarok, the Desecrated", "Muldrotha, the Gravetide",
              "Light-Paws, Emperor's Voice", "Zhulodok, Void Gorger"]
    for probe in probes:
        row = next((r for r in rows if r["en"] == probe), None)
        if row:
            print(f"  {row['zh']:<16} {row['before']}/5 → {row['after']}/5   "
                  f"（牌面 {row['text']}，操作 {row['pilot']}）")

    from collections import Counter
    print("\n=== 新旧分布 ===")
    print("  旧：" + " ".join(f"{k}档{v}" for k, v in sorted(
        Counter(r["before"] for r in rows if r["before"]).items())))
    print("  新：" + " ".join(f"{k}档{v}" for k, v in sorted(
        Counter(r["after"] for r in rows).items())))

    print("\n=== 新评分下最简单的 12 位（应该是真好上手的）===")
    for row in sorted(rows, key=lambda r: r["after"])[:12]:
        print(f"  {row['after']}/5  {row['zh']} / {row['en'][:32]}"
              f"  （牌面 {row['text']}，操作 {row['pilot']}）")

    print("\n=== 新评分下最难的 12 位 ===")
    for row in sorted(rows, key=lambda r: -r["after"])[:12]:
        print(f"  {row['after']}/5  {row['zh']} / {row['en'][:32]}"
              f"  （牌面 {row['text']}，操作 {row['pilot']}）")


if __name__ == "__main__":
    main()
