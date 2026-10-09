# -*- coding: utf-8 -*-
"""独立校验已写出的 tag_axis_map.json（不复用生成器逻辑）。"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
D = Path(ROOT / "data")
vocab = []
for ln in (D / "tag_vocabulary.txt").read_text(encoding="utf-8").splitlines():
    ln = ln.rstrip()
    if not ln.strip() or not ln.lstrip()[0].isdigit():
        continue
    vocab.append(re.match(r"^\s*(\d+)\s+(\d+)\s+(.+?)\s*$", ln).group(3))

j = json.loads((D / "tag_axis_map.json").read_text(encoding="utf-8"))
mapped, ignored = j["mapped"], j["ignored"]
AXES = {"aggro", "voltron", "wide", "ramp", "stompy", "control", "removal",
        "combo", "spells", "artifacts", "enchant", "grave", "tribal", "drain",
        "stax", "clonesteal", "politics", "chaos", "counters", "blink"}
W = {0.5, 1.0, 1.5, 2.0}

errs = []
if set(j) != {"mapped", "ignored"}:
    errs.append(f"顶层键异常: {sorted(j)}")
if len(mapped) + len(ignored) != len(vocab):
    errs.append(f"总数 {len(mapped)}+{len(ignored)} != {len(vocab)}")
if set(mapped) & set(ignored):
    errs.append(f"同时出现在两边: {sorted(set(mapped) & set(ignored))}")
for t in vocab:
    if t not in mapped and t not in ignored:
        errs.append(f"未覆盖: {t}")
for t in list(mapped) + list(ignored):
    if t not in set(vocab):
        errs.append(f"词表外标签: {t}")
for t, d in mapped.items():
    if not isinstance(d, dict) or not d:
        errs.append(f"{t}: 映射不是非空对象")
        continue
    if len(d) > 3:
        errs.append(f"{t}: {len(d)} 个轴 > 3")
    for a, w in d.items():
        if a not in AXES:
            errs.append(f"{t}: 未知轴 {a}")
        if w not in W:
            errs.append(f"{t}: 非法权重 {w}")
for t, r in ignored.items():
    if not isinstance(r, str) or len(r.strip()) < 4:
        errs.append(f"{t}: ignored 理由缺失")

cover = Counter(a for d in mapped.values() for a in d)
print(f"mapped {len(mapped)} / ignored {len(ignored)} / 词表 {len(vocab)}")
print(f"轴被引用次数: {dict(sorted(cover.items(), key=lambda kv: -kv[1]))}")
print("20 轴全部被引用" if len(cover) == 20 else f"缺轴: {AXES - set(cover)}")
print(f"最大轴数/标签: {max(len(d) for d in mapped.values())}")
if errs:
    print(f"\n[失败] {len(errs)} 处:")
    for e in errs[:40]:
        print("  -", e)
    raise SystemExit(1)
print("\n独立校验通过：404 全覆盖，无重复，权重/轴合法。")

print("\n抽样:")
for t in ["Goblins", "Tokens", "Aggro", "Storm", "Voltron", "Blink", "ETB",
          "Sacrifice", "Mill", "Voltron", "Combo", "Midrange", "Good Stuff",
          "Airbending", "Earthbending", "Summons", "Ninjutsu", "Plants"]:
    if t in mapped:
        print(f"  {t:<22} {mapped[t]}")
    else:
        print(f"  {t:<22} IGNORED: {ignored[t]}")
