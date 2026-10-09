#!/usr/bin/env python3
"""附加审查：禁忌词、英文残留、标点、编码、以及正文提到的牌是否属于该主将自己的清单。"""
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
JSON = DATA / "descriptions_2.json"
MD = DATA / "writing_batch_2.md"

BANNED = ["Bracket", "EDHREC", "咸度", "voltron", "Voltron", "stax", "ramp", "引擎", "曲线",
          "最强", "上分", "无敌", "！", "!"]
LATIN = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ'’.,\- 0-9]*[A-Za-zÀ-ÖØ-öø-ÿ0-9]")
HEAD = re.compile(r"^## (.+?) ｜ (.+)$")
CARD = re.compile(r"^\s+(?:\d+\.|[-*])\s+(.+?)（")

lists: dict[str, list[str]] = {}
current = None
for line in MD.read_text(encoding="utf-8").splitlines():
    h = HEAD.match(line)
    if h:
        current = h.group(1).strip()
        lists[current] = []
        continue
    if current:
        m = CARD.match(line)
        if m:
            lists[current].append(m.group(1).strip())

raw = JSON.read_bytes()
data = json.loads(raw.decode("utf-8"))

print("编码：UTF-8 无 BOM" if not raw.startswith(b"\xef\xbb\xbf") else "编码：⚠ 带 BOM")

print("\n--- 禁忌词 ---")
hits = 0
for key, entry in data.items():
    blob = " ".join(entry.values())
    for word in BANNED:
        if word in blob:
            hits += 1
            print(f"  ✗ {key} 出现「{word}」")
print("  无" if not hits else f"  共 {hits} 处")

print("\n--- 正文里所有英文片段（应全部是白名单牌名）---")
seen: dict[str, set[str]] = {}
for key, entry in data.items():
    for seq in LATIN.findall(" ".join(entry.values())):
        seq = seq.strip(" .,-")
        if sum(c.isalpha() for c in seq) < 2:
            continue
        seen.setdefault(seq, set()).add(key)
for seq, keys in sorted(seen.items()):
    ok = all(seq in lists[k] for k in keys)
    print(f"  {'OK ' if ok else '✗  '} {seq:<28} ← {', '.join(sorted(keys))}")
print(f"  共 {len(seen)} 个不同英文片段")

print("\n--- 长度分布 ---")
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
rows = []
for key, entry in data.items():
    rows.append((key, len(entry["tagline"]),
                 len(CJK.findall(entry["intro"])), len(entry["intro"]),
                 len(CJK.findall(entry["build"])), len(entry["build"])))
print(f"  tagline 总长      : {min(r[1] for r in rows)} ~ {max(r[1] for r in rows)}（上限 20）")
print(f"  intro  中文字数   : {min(r[2] for r in rows)} ~ {max(r[2] for r in rows)}（要求 70~120）")
print(f"  intro  总字符数   : {min(r[3] for r in rows)} ~ {max(r[3] for r in rows)}")
print(f"  build  中文字数   : {min(r[4] for r in rows)} ~ {max(r[4] for r in rows)}（要求 110~170）")
print(f"  build  总字符数   : {min(r[5] for r in rows)} ~ {max(r[5] for r in rows)}")
over = [r for r in rows if r[5] > 170]
print(f"  build 总长 >170 的条目：{len(over)}" + (f" → {[r[0] for r in over]}" if over else ""))

print("\n--- 每位主将提到的牌（须属于本主将自己的清单）---")
for key, entry in data.items():
    seqs = [s.strip(" .,-") for s in LATIN.findall(entry["build"])]
    seqs = [s for s in seqs if sum(c.isalpha() for c in s) >= 2]
    bad = [s for s in seqs if s not in lists[key]]
    print(f"  {key:<32} {'、'.join(seqs)}" + ("   ✗ " + str(bad) if bad else ""))
