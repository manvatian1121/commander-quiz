#!/usr/bin/env python3
"""核心诊断：评分引擎能不能区分「口味完全不同的人」？

做法：把偏好向量设成只含单一玩法轴（纯口味的人），看每种口味的榜首是谁。
如果 20 种口味的榜首都是同一批主将，说明引擎压根没有区分能力。
"""
from __future__ import annotations

import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, score_commanders  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

DATA = pathlib.Path(ROOT / "data")
AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]

NEUTRAL = {"complex": 3.5, "budget": 3.5, "salt": 3.0, "exp": 3}


def main() -> None:
    payload = load_commanders()
    by_name = {c["en"]: c for c in payload["commanders"]}

    print("=== 单一口味下的前五名 ===")
    seen: dict[str, list[str]] = {}
    for axis in AXES:
        pref = {axis: 1.0}
        results = score_commanders(payload, pref, {}, dict(NEUTRAL))
        top = [r["en"] for r in results[:5]]
        seen[axis] = top
        names = " | ".join(by_name[n]["zh"] for n in top)
        print(f"  {axis:<11} {names}")

    print("\n=== 重复度检查 ===")
    from collections import Counter
    counter = Counter(n for top in seen.values() for n in top)
    total = sum(len(v) for v in seen.values())
    print(f"  20 种口味 × 前五 = {total} 个位置，涉及 {len(counter)} 位不同主将")
    print(f"  出现最多的：")
    for name, count in counter.most_common(12):
        print(f"    {count:>2} 次  {by_name[name]['zh']}")

    print("\n=== 榜首重复度 ===")
    tops = Counter(v[0] for v in seen.values())
    print(f"  20 种口味的榜首由 {len(tops)} 位主将包办")
    for name, count in tops.most_common():
        print(f"    {count:>2} 种口味  {by_name[name]['zh']}")

    print("\n=== 区分度：同一口味下，第一与第五十名的余弦差 ===")
    for axis in ["politics", "combo", "tribal", "stax", "blink"]:
        results = score_commanders(payload, {axis: 1.0}, {}, dict(NEUTRAL))
        gap = results[0]["sim"] - results[49]["sim"]
        print(f"  {axis:<11} 第1名余弦 {results[0]['sim']:.4f}，"
              f"第50名 {results[49]['sim']:.4f}，差 {gap:.4f}")


if __name__ == "__main__":
    main()
