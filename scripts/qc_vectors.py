#!/usr/bin/env python3
"""向量质量检查：逐轴分布，找出「被归一化放大」的伪信号。"""
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
    payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    cmds = payload["commanders"]
    axes = payload["axes"]
    scales = payload["meta"]["axis_scale"]

    print(f"主将 {len(cmds)} 位，轴 {len(axes)} 个\n")
    problems = []
    for axis in axes:
        pairs = sorted(((c["vec"].get(axis, 0.0), c["en"]) for c in cmds), reverse=True)
        nonzero = [v for v, _ in pairs if v > 0]
        top = [(round(v, 2), n) for v, n in pairs[:3] if v > 0]
        saturated = sum(1 for v in nonzero if v >= 2.95)
        print(f"{axis:<11} 标定系数{scales[axis]:>8.4f} 非零{len(nonzero):>3}位 "
              f"满分{saturated:>2}位  最高: {top}")
        # 只有极少数主将有此信号、却有多个满分 → 归一化放大了噪声
        if len(nonzero) <= 8 and saturated >= 1:
            problems.append(f"{axis}：仅 {len(nonzero)} 位非零却有 {saturated} 位满分，疑似噪声放大")
        if saturated == 0 and len(nonzero) > 0:
            problems.append(f"{axis}：没有任何主将达到 3.0，标定可能过松")

    print("\n" + "=" * 70)
    if problems:
        print(f"⚠ {len(problems)} 处需要关注：")
        for item in problems:
            print(f"  - {item}")
    else:
        print("✓ 各轴分布正常")

    # 向量稀疏度
    sizes = sorted(len(c["vec"]) for c in cmds)
    print(f"\n每位主将的非零轴数量：最少 {sizes[0]}，中位 {sizes[len(sizes) // 2]}，最多 {sizes[-1]}")
    thin = [c["en"] for c in cmds if len(c["vec"]) < 4]
    if thin:
        print(f"⚠ 向量过薄（<4 轴）{len(thin)} 位：{thin}")


if __name__ == "__main__":
    main()
