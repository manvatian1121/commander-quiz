#!/usr/bin/env python3
"""给介绍文里的英文牌名补上官方中文名（中英并列），与早先的 110 篇格式统一。

写作代理出于「不凭记忆编造译名」的原则只写了英文；这里用 card_zh.json 里的
官方中文名做机械替换，不引入任何猜测。
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
TARGETS = [f"descriptions_{i}.json" for i in range(4, 17)]
FIELDS = ("intro", "build")
CJK = re.compile(r"[\u4e00-\u9fff]")


def main() -> int:
    card_zh = json.loads((DATA / "card_zh.json").read_text(encoding="utf-8"))
    display = json.loads((DATA / "card_display.json").read_text(encoding="utf-8"))

    total = 0
    report: list[str] = []

    for fname in TARGETS:
        path = DATA / fname
        if not path.exists():
            print(f"⚠ {fname} 尚未产出")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        changed_here = 0

        for commander, entry in data.items():
            picks = display.get(commander) or {}
            names = sorted(set((picks.get("synergy") or []) + (picks.get("popular") or [])),
                           key=len, reverse=True)
            for field in FIELDS:
                text = entry.get(field) or ""
                original = text
                for name in names:
                    zh = card_zh.get(name)
                    if not zh:
                        continue
                    # 长名先处理，避免短名把长名切开
                    out, pos = [], 0
                    while True:
                        idx = text.find(name, pos)
                        if idx < 0:
                            out.append(text[pos:])
                            break
                        before = text[max(0, idx - 2):idx]
                        # 已经是「中文（English）」形式就跳过。
                        # 注意：中文名可能以拉丁字母结尾（如「潘妮驾驭的SP//dr」），
                        # 所以这里只要求前一个字符是左括号，不再要求再往前是汉字。
                        if before.endswith("（"):
                            out.append(text[pos:idx + len(name)])
                        else:
                            out.append(text[pos:idx] + f"{zh}（{name}）")
                        pos = idx + len(name)
                    text = "".join(out)
                if text != original:
                    entry[field] = text
                    changed_here += 1
            if changed_here % 50 == 0:
                pass

        if changed_here:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        total += changed_here
        report.append(f"  {fname}: 修改 {changed_here} 个字段")
        print(f"  {fname}: 修改 {changed_here} 个字段")

    print(f"\n✓ 共修改 {total} 个字段")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
