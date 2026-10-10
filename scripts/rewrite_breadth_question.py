#!/usr/bin/env python3
"""按「接受短板 vs 补短板」重写广度题。

用户指出的问题：原来把「颜色数量」映射成「同时推几件事」，这两者不是一回事。
真正的维度是——你愿不愿意为了更全面，承担更麻烦的代价：

  单色 = 接受短板，换简单直接（绕开它就行）
  双色 = 补一个短板（绿跳费缺抓牌，就加蓝）
  三色 = 缺什么补什么，凑成一套互相兜底的
  五色 = 什么都想会一点，代价是样样不精、还要花精力协调
  无色 = 不按现成路数来，自己另琢磨一套

关键在于**两边都在付代价**（单色付出短板，五色付出「不精」和协调成本），
原版只写了「想要几个」，没写出选择的分量。

同时调整选项的玩法轴，让轴与新的文案对得上（原 C/D 的轴与新文案背离）。
"""
from __future__ import annotations

import json
import pathlib
import sys


# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"ROOT\data")

NEW_Q = "你有自己挺得意的一套本事，但它明显有块短板。你一般会怎么办？"

NEW_OPTS = [
    {"t": "短板就短板，把得意的那块做到最好，绕开它就行",
     "s": {"control": 2.0, "voltron": 1.5}, "bw": 0.2},
    {"t": "再学一样正好能补上的，两样搭着来",
     "s": {"combo": 2.0, "counters": 1.0}, "bw": 0.4},
    {"t": "缺什么补什么，凑成一套能互相兜底的",
     "s": {"removal": 1.5, "blink": 1.5}, "bw": 0.6},
    {"t": "什么都想会一点，宁可都不精，也不想有明显短板",
     "s": {"wide": 2.0, "politics": 1.0}, "bw": 1.0},
    {"t": "不照着现成的路数来，我自己另琢磨一套",
     "s": {"artifacts": 2.5, "stax": 1.0}, "bw": 0.0},
]


def main() -> int:
    path = DATA / "bank4.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    target = next((q for q in payload["questions"] if q["id"] == "s62b"), None)
    if target is None:
        print("✗ 找不到 s62b")
        return 1

    print(f"旧题干：{target['q']}")
    print(f"新题干：{NEW_Q}\n")
    for i, (old, new) in enumerate(zip(target["opts"], NEW_OPTS)):
        print(f"  {'ABCDE'[i]}. {old['t']}")
        print(f"     → {new['t']}")
        print(f"       bw={new['bw']}　轴 {old['s']} → {new['s']}\n")

    target["q"] = NEW_Q
    target["opts"] = NEW_OPTS
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("✓ 已重写")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
