#!/usr/bin/env python3
"""比对：真 questions.json vs 由 before 题库重跑 merge 的结果 vs 由 after 题库重跑的结果。

目的：确认 data/questions.json（以及 commander_quiz.html）是否可以从 bank*.json 机械重建，
      从而给出「让改动上线」的确切命令。
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROBE = ROOT / "_scratch" / "_merge_probe"


def read(p: pathlib.Path) -> str:
    return p.read_text(encoding="utf-8")


def walk_diff(before, after, path=""):
    diffs = []
    if isinstance(before, dict) and isinstance(after, dict):
        for k in dict.fromkeys(list(before) + list(after)):
            if k not in before:
                diffs.append((f"{path}.{k}", None, after[k]))
            elif k not in after:
                diffs.append((f"{path}.{k}", before[k], None))
            else:
                diffs.extend(walk_diff(before[k], after[k], f"{path}.{k}"))
    elif isinstance(before, list) and isinstance(after, list):
        if len(before) != len(after):
            diffs.append((f"{path}.len", len(before), len(after)))
        for i, (b, a) in enumerate(zip(before, after)):
            diffs.extend(walk_diff(b, a, f"{path}[{i}]"))
    elif before != after:
        diffs.append((path, before, after))
    return diffs


real = ROOT / "data" / "questions.json"
pre = PROBE / "pre" / "data" / "questions.json"
post = PROBE / "post" / "data" / "questions.json"

for p in (real, pre, post):
    print(f"{p.relative_to(ROOT)}  exists={p.exists()}  bytes={p.stat().st_size if p.exists() else '-'}")

r, a, b = json.loads(read(real)), json.loads(read(pre)), json.loads(read(post))
print(f"\n题量: real={len(r['questions'])}  pre={len(a['questions'])}  post={len(b['questions'])}")
print(f"meta 相同(real vs pre): {r['meta'] == a['meta']}")
print(f"spine 相同(real vs pre): {r['spine'] == a['spine']}   quick 相同: {r['quick'] == a['quick']}")
print(f"**real questions.json == 由 before 题库重跑的结果: {r == a}**")

diffs = walk_diff(a, b, "questions")
ids = sorted({d[0].split("[")[0] for d in diffs})
qids = []
for d in diffs:
    # 定位属于哪道题
    for q in b["questions"]:
        pass
bmap = {q["id"]: q for q in b["questions"]}
amap = {q["id"]: q for q in a["questions"]}
changed_ids = [qid for qid in bmap if walk_diff(amap[qid], bmap[qid], qid)]
print(f"\nbefore-merge 与 after-merge 的差异题：{sorted(changed_ids)}")
print(f"差异字段总数：{len(diffs)}")
for qid in sorted(changed_ids):
    ds = walk_diff(amap[qid], bmap[qid], qid)
    print(f"  {qid}: {[x[0] for x in ds]}")

# 非题目部分（meta/spine/quick/sections/start）是否也变了
head = [k for k in r if k != "questions"]
print(f"\n非题目字段是否被重建改动：{ {k: (a[k] != b[k]) for k in head} }")
