#!/usr/bin/env python3
"""导出题库内容，供颜色题改写时比对。"""
from __future__ import annotations

import json
import pathlib
import sys


# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"ROOT\data")


def dump(name: str, full: bool) -> None:
    doc = json.loads((DATA / name).read_text(encoding="utf-8"))
    qs = doc["questions"] if isinstance(doc, dict) else doc
    print(f"\n{'=' * 78}\n{name}  题数={len(qs)}  顶层键={list(doc.keys()) if isinstance(doc, dict) else 'list'}\n{'=' * 78}")
    for i, q in enumerate(qs):
        head = f"[{i:>3}] {q.get('id')}"
        if q.get("sec"):
            head += f" sec={q['sec']}"
        if q.get("kind"):
            head += f" kind={q['kind']}"
        if q.get("multi"):
            head += f" multi={q['multi']}"
        head += f" next={q.get('next', '<无>')!r}"
        print(head)
        print(f"      Q: {q.get('q')}")
        for j, opt in enumerate(q.get("opts", [])):
            letter = "ABCDE"[j] if j < 5 else f"#{j}"
            line = f"      {letter}. {opt.get('t')}"
            if opt.get("s"):
                line += f"   s={opt['s']}"
            if opt.get("col"):
                line += f"   col={opt['col']}"
            if opt.get("goto"):
                line += f"   goto={opt['goto']}"
            if opt.get("why") and full:
                line += f"   why={opt['why']}"
            print(line)


if __name__ == "__main__":
    import io
    buf = io.StringIO()
    _orig = sys.stdout
    sys.stdout = buf
    for bank in ["bank1.json", "bank2.json", "bank3.json", "bank4.json", "bank5.json"]:
        dump(bank, full=False)
    sys.stdout = _orig
    out = pathlib.Path(r"ROOT\_scratch\_cq_dump.txt")
    out.write_text(buf.getvalue(), encoding="utf-8")
    print(f"wrote {out} ({len(buf.getvalue().splitlines())} lines)")
