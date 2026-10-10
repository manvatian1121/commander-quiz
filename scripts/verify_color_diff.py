#!/usr/bin/env python3
"""逐字段比对 bank4.json 与备份：确认改动只落在四道题（q / opts[].t / s / col）。

跑法：python verify_color_diff.py
"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
CUR = ROOT / "data" / "bank4.json"
OLD = ROOT / "_scratch" / "data" / "_colorq_backup_bank4.json"
TARGETS = ["s49", "s59", "s60", "s62"]
POSITIONS = "ABCDE"


def walk(a, b, path, diffs):
    """a=新, b=旧；只收叶子差异。"""
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                diffs.append((f"{path}/{k}", "键存在性不同", None))
                continue
            walk(a[k], b[k], f"{path}/{k}", diffs)
        return
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            diffs.append((path, f"长度 {len(b)}→{len(a)}", None))
            return
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, f"{path}[{i}]", diffs)
        return
    if a != b:
        diffs.append((path, a, b))


def main() -> int:
    cur = json.loads(CUR.read_text(encoding="utf-8"))
    old = json.loads(OLD.read_text(encoding="utf-8"))
    diffs: list[tuple[str, object, object]] = []
    walk(cur, old, "", diffs)

    print("=" * 74)
    print(f"改动字段总数：{len(diffs)}")
    print("=" * 74)

    def owner(path: str) -> str:
        seg = path.split("/questions[")
        if len(seg) < 2:
            return "<非题目>"
        return f"#{seg[1].split(']')[0]}"

    by_q: Counter = Counter(owner(p) for p, _, _ in diffs)
    print("\n按题目编号分布（编号=questions 数组下标，0=s49 …）：")
    for k in sorted(by_q, key=lambda x: (x == "<非题目>", x)):
        print(f"  {k}: {by_q[k]} 个字段")

    non_target = [(p, a, b) for p, a, b in diffs
                  if p.split("/questions[")[1].split("]")[0]
                  not in {str(i) for i in range(len(cur["questions"]))
                          if cur["questions"][i]["id"] in TARGETS}]
    print(f"\n四道颜色题之外的字段改动：{len(non_target)}")
    for p, a, b in non_target[:20]:
        print(f"  {p}: {b!r} → {a!r}")

    # 只允许 q / opts[].t / opts[].s / opts[].col
    import re
    allow = re.compile(r"^/questions\[\d+\]/(q|opts\[\d+\]/(t|s(/[a-z]+)?|col(/[WUBRG])?))$")
    illegal = [(p, a, b) for p, a, b in diffs if not allow.match(p)]
    print(f"\n不在白名单（q / t / s / col）里的改动：{len(illegal)}")
    for p, a, b in illegal[:20]:
        print(f"  {p}: {b!r} → {a!r}")

    # 逐题摘要
    print("\n四道题逐题摘要：")
    new_by_id = {q["id"]: q for q in cur["questions"]}
    old_by_id = {q["id"]: q for q in old["questions"]}
    new_ids = [q["id"] for q in cur["questions"]]
    old_ids = [q["id"] for q in old["questions"]]
    for qid in TARGETS:
        n, o = new_by_id[qid], old_by_id[qid]
        n_diffs = [p for p, _, _ in diffs if f"/questions[{new_ids.index(qid)}]/" in p]
        print(f"\n  {qid}  位置 {old_ids.index(qid)}→{new_ids.index(qid)}"
              f"  next {o.get('next')!r}→{n.get('next')!r}  字段改动 {len(n_diffs)} 个")
        print(f"    旧题干：{o['q']}")
        print(f"    新题干：{n['q']}")
        for i, (no, oo) in enumerate(zip(n["opts"], o["opts"])):
            print(f"    {POSITIONS[i]} 旧：{oo['t']}  {oo['s']}  col={oo.get('col')}")
            print(f"      新：{no['t']}  {no['s']}  col={no.get('col')}")

    ok = not non_target and not illegal
    print("\n" + "=" * 74)
    print("结论：" + ("改动范围正确 ✓（只有四道题的 q / t / s / col）" if ok else "存在越界改动 ✗"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
