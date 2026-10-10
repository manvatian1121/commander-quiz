#!/usr/bin/env python3
"""无色选项：广度拉到与单色同档（0.2），并给它独立的 "C" 颜色偏好。

这样「档位拉平」与「候选不混」两件事同时成立：
  - 广度 0.2 = 单色同档，不再把无色当作「比一种颜色更极端」
  - 无色主将的色相分只看 "C"，没选过无色的人 C=0，拿不到无色的色相分
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"D:\万智\commander-quiz\data")

OLD_T = "不用超能力，我靠自己那套办法就够"


def main() -> int:
    path = DATA / "bank4.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    target = next((q for q in payload["questions"] if q["id"] == "s62b"), None)
    if target is None:
        print("✗ 找不到 s62b")
        return 1

    hit = False
    for opt in target["opts"]:
        if opt["t"] == OLD_T:
            opt["bw"] = 0.2                 # 0.0 → 0.2，与单色同档
            opt["col"] = {"C": 2}           # 独立的无色偏好
            print(f"  {opt['t']}")
            print(f"    bw: 0.0 → 0.2（与单色同档）")
            print(f"    col: 无 → {{'C': 2}}（无色主将只认这个）")
            hit = True
    if not hit:
        print(f"✗ 找不到选项：{OLD_T!r}")
        return 1

    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n改后六档：")
    for i, opt in enumerate(target["opts"]):
        col = opt.get("col") or {}
        colstr = f"  col={col}" if col else ""
        print(f"  {'ABCDEF'[i]}. bw={opt['bw']:<4} {opt['t']}{colstr}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
