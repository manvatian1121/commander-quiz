#!/usr/bin/env python3
"""校验 tag_axis_map.json：覆盖全词表、轴名合法、权重合法。"""
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
AXES = {"aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"}
ALLOWED_WEIGHTS = {0.5, 1.0, 1.5, 2.0}


def main() -> int:
    vocab = []
    for line in (DATA / "tag_vocabulary.txt").read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split()
        if len(parts) >= 3:
            vocab.append(" ".join(parts[2:]))
    vocab_set = set(vocab)

    payload = json.loads((DATA / "tag_axis_map.json").read_text(encoding="utf-8"))
    mapped = payload.get("mapped") or {}
    ignored = payload.get("ignored") or {}

    problems = []
    for tag, weights in mapped.items():
        if not isinstance(weights, dict) or not weights:
            problems.append(f"'{tag}' 权重为空")
            continue
        for axis, value in weights.items():
            if axis not in AXES:
                problems.append(f"'{tag}' 含非法轴 '{axis}'")
            if value not in ALLOWED_WEIGHTS:
                problems.append(f"'{tag}.{axis}' 权重 {value} 不在允许集合")

    covered = set(mapped) | set(ignored)
    missing = sorted(vocab_set - covered)
    extra = sorted(covered - vocab_set)

    print(f"词表 {len(vocab_set)} 种 | mapped {len(mapped)} | ignored {len(ignored)} "
          f"| 合计 {len(covered)}")
    if missing:
        print(f"\n⚠ 未覆盖 {len(missing)} 种：")
        for tag in missing[:40]:
            print(f"  - {tag}")
    if extra:
        print(f"\n⚠ 多余（不在词表中）{len(extra)} 种：{extra[:20]}")
    if problems:
        print(f"\n⚠ 结构问题 {len(problems)} 处：")
        for item in problems[:30]:
            print(f"  - {item}")

    if not missing and not problems:
        print("\n✓ 映射表完整且合法")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
