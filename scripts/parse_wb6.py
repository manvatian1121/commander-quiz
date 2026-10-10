# -*- coding: utf-8 -*-
"""解析 writing_batch_new_6.md：抽取每位主将的白名单牌名 + 官方中文名。

输出：
  data/_wb6_whitelist.json  {主将: {"zh": 主将中文名, "cards": [英文牌名...], "cards_zh": {英文: 中文}}}
并在 stdout 打印每位主将的清单与缺中文名的卡。
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

BASE = pathlib.Path(ROOT)
DATA = BASE / "data"
MD = DATA / "writing_batch_new_6.md"
CARD_ZH = DATA / "card_zh.json"

HEAD_LINE = re.compile(r"^## (.+?) ｜ (.+?)\s*$")
CARD_LINE = re.compile(r"^\s+(?:\d+\.|[-*])\s+(.+?)（")


def main() -> int:
    zh_map: dict[str, str] = json.loads(CARD_ZH.read_text(encoding="utf-8"))

    out: dict[str, dict] = {}
    cur: str | None = None
    for line in MD.read_text(encoding="utf-8").splitlines():
        head = HEAD_LINE.match(line)
        if head:
            cur = head.group(1).strip()
            out[cur] = {"zh": head.group(2).strip(), "cards": []}
            continue
        if cur is None:
            continue
        m = CARD_LINE.match(line)
        if m:
            name = m.group(1).strip()
            if name and name not in out[cur]["cards"]:
                out[cur]["cards"].append(name)

    missing_all: list[tuple[str, str]] = []
    for cmd, info in out.items():
        info["cards_zh"] = {}
        for n in info["cards"]:
            z = zh_map.get(n)
            if z:
                info["cards_zh"][n] = z
            else:
                missing_all.append((cmd, n))

    (DATA / "_wb6_whitelist.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"主将数：{len(out)}")
    for i, (cmd, info) in enumerate(out.items(), 1):
        print(f"\n{i:>2}. {cmd} ｜ {info['zh']}  (社区中文名 from material)"
              f"   清单 {len(info['cards'])} 张")
        for n in info["cards"]:
            z = info["cards_zh"].get(n, "")
            print(f"      {'✓' if z else '✗'} {n}{('  →  ' + z) if z else ''}")
    print(f"\n缺中文名 {len(missing_all)} 处：")
    for cmd, n in missing_all:
        print(f"   {cmd} :: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
