#!/usr/bin/env python3
"""拉平题库的轴权重：让每个玩法轴的总权重相等。

余弦相似度是尺度无关的，所以按轴整体缩放权重不改变任何选项的「方向」语义，
只改变各轴之间的话语权。

做法：以权重最小的轴为基准，把所有轴缩放到同一总量（只缩不放，
避免出现超过上限 3.0 的权重）。
"""
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
BANKS = ["bank1", "bank2", "bank3", "bank4", "bank5", "bankC", "bankE"]

APPLY = "--apply" in sys.argv


def main() -> int:
    totals: Counter = Counter()
    for bank in BANKS:
        path = DATA / f"{bank}.json"
        if not path.exists():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        for q in payload["questions"]:
            for opt in q["opts"]:
                for axis, weight in (opt.get("s") or {}).items():
                    totals[axis] += weight

    if not totals:
        print("✗ 没读到任何权重")
        return 1

    target = min(totals.values())
    scale = {axis: target / total for axis, total in totals.items()}

    print(f"目标：每个轴总权重 = {target:.1f}")
    print(f"\n  {'轴':<11} {'原总量':>8} {'缩放系数':>9}")
    for axis in sorted(totals, key=lambda a: -totals[a]):
        print(f"  {axis:<11} {totals[axis]:>8.1f} {scale[axis]:>9.3f}")

    if not APPLY:
        print("\n（预演模式，未写入。加 --apply 执行。）")
        return 0

    changed = 0
    for bank in BANKS:
        path = DATA / f"{bank}.json"
        if not path.exists():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        touched = 0
        for q in payload["questions"]:
            for opt in q["opts"]:
                scores = opt.get("s")
                if not scores:
                    continue
                new_scores = {}
                for axis, weight in scores.items():
                    value = round(weight * scale[axis], 2)
                    # 保留轴信号，下限 0.5；上限仍受 3.0 约束（缩放只减不增）
                    new_scores[axis] = max(0.5, min(3.0, value))
                if new_scores != scores:
                    opt["s"] = new_scores
                    touched += 1
        if touched:
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        changed += touched
        print(f"  {bank}.json：{touched} 个选项的权重已重算")

    # 复核
    after: Counter = Counter()
    for bank in BANKS:
        path = DATA / f"{bank}.json"
        if not path.exists():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        for q in payload["questions"]:
            for opt in q["opts"]:
                for axis, weight in (opt.get("s") or {}).items():
                    after[axis] += weight
    spread = max(after.values()) / min(after.values())
    print(f"\n✓ 重算 {changed} 个选项")
    print(f"  最高/最低轴的总权重比：{spread:.2f}（改前 "
          f"{max(totals.values()) / min(totals.values()):.2f}）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
