#!/usr/bin/env python3
"""广度题第二次重写：改成「超能力」框架，并补齐四色。

两个问题：
① 用户指出原来的「你有自己挺得意的一套本事，但它明显有块短板」太抽象，
   建议换成「如果你能挑一样超能力」或落在「处理事情的能力」上。
② 更严重的：广度刻度是 无色0.0 / 单色0.2 / 双色0.4 / 三色0.6 / 五色1.0，
   **缺了四色的 0.8**——四色主将（阿特拉克萨、布蕾娅、库瑙斯与提罗…）
   任何选项都匹配不到满分，最多只能拿到 0.9。只有 5 个选项装不下 6 档，
   所以把选项上限从 5 放宽到 6。

保留上一轮的核心：**每一边都要写出自己的代价**（单色承认盲区，四色/五色承认
「用起来麻烦」「宁可不精」），这样才是一个真正的选择而不是「越多越好」。
"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"ROOT\data")

NEW_Q = "给你一样超能力，你希望它是——"

NEW_OPTS = [
    {"t": "就一种，但强到极致；剩下的情况我另想办法",
     "s": {"control": 2.0, "voltron": 1.5}, "bw": 0.2},
    {"t": "两种正好互补，一样有短板，另一样能补上",
     "s": {"combo": 2.0, "counters": 1.0}, "bw": 0.4},
    {"t": "三种，互相配合着用，覆盖面就够我使了",
     "s": {"removal": 1.5, "blink": 1.5}, "bw": 0.6},
    {"t": "四种，尽量不留死角，用起来麻烦点也认了",
     "s": {"politics": 2.0, "stax": 1.0}, "bw": 0.8},
    {"t": "什么都会一点，宁可不精，也不想有做不到的事",
     "s": {"wide": 2.0, "clonesteal": 1.0}, "bw": 1.0},
    {"t": "不用超能力，我靠自己那套办法就够",
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
    labels = ["无色", "单色", "双色", "三色", "四色", "五色"]
    print(f"  {'选项':<4} {'广度':>6}  {'对应':<5}  文案")
    for opt in NEW_OPTS:
        bw = opt["bw"]
        idx = {0.0: 0, 0.2: 1, 0.4: 2, 0.6: 3, 0.8: 4, 1.0: 5}[bw]
        print(f"  {'ABCDEF'[NEW_OPTS.index(opt)]:<4} {bw:>6}  {labels[idx]:<5}  {opt['t']}")

    target["q"] = NEW_Q
    target["opts"] = NEW_OPTS
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    missing = [v for v in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0) if v not in [o["bw"] for o in NEW_OPTS]]
    print(f"\n✓ 已重写（6 个选项）")
    print(f"  广度刻度完整：{'是' if not missing else '缺 ' + str(missing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
