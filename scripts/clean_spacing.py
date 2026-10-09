#!/usr/bin/env python3
"""清理「中文（English）」两侧的空格残留（只动紧邻括号的那一个空格）。"""
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
PAREN = re.compile(r"（[A-Za-z][^）]*）")
CJK = re.compile(r"[\u4e00-\u9fff]")
TARGETS = ["descriptions_1.json", "descriptions_2.json", "descriptions_3.json",
           "descriptions_4.json", "descriptions_5.json",
           "descriptions_6.json", "descriptions_7.json"]


def clean(text: str) -> tuple[str, int]:
    fixed = 0
    out = text
    # ① 注入时在中文牌名前面留下的空格：「用 林地墓园（X）」→「用林地墓园（X）」
    out, n = re.subn(r"(?<=[\u4e00-\u9fff]) (?=[\u4e00-\u9fff]{2,12}（[A-Za-z])", "", out)
    fixed += n
    # ② 括号两侧的空格
    for _ in range(6):
        matches = list(PAREN.finditer(out))
        if not matches:
            break
        pieces, pos, changed = [], 0, False
        for match in matches:
            start, end = match.start(), match.end()
            # 括号前的空格：形如「用 林地墓园（X）」→ 去掉空格
            lead = start
            while lead > 0 and out[lead - 1] == " ":
                lead -= 1
            if lead < start and lead > 0 and CJK.match(out[lead - 1]):
                pieces.append(out[pos:lead])
                fixed += 1
                changed = True
            else:
                pieces.append(out[pos:start])
            pieces.append(out[start:end])
            # 括号后的空格：形如「（X） 让指示物」→ 去掉空格
            trail = end
            while trail < len(out) and out[trail] == " ":
                trail += 1
            if trail > end and trail < len(out) and CJK.match(out[trail]):
                fixed += 1
                changed = True
            else:
                pieces.append(out[end:trail])
            pos = trail
        pieces.append(out[pos:])
        out = "".join(pieces)
        if not changed:
            break
    return out, fixed


def main() -> int:
    total = 0
    for fname in TARGETS:
        path = DATA / fname
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        count = 0
        for entry in data.values():
            for field in ("intro", "build"):
                text = entry.get(field)
                if not text:
                    continue
                cleaned, fixed = clean(text)
                if fixed:
                    entry[field] = cleaned
                    count += fixed
        if count:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        total += count
        print(f"  {fname}: 清理 {count} 处")
    print(f"\n✓ 共清理 {total} 处空格")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
