# -*- coding: utf-8 -*-
"""用真实 EDHREC 标签票数跑一遍，看几位知名主将的玩法向量是否符合直觉。"""
import json
import sys
from collections import Counter
from pathlib import Path

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
D = Path(ROOT / "data")
prof = json.loads((D / "commander_profiles.json").read_text(encoding="utf-8"))
amap = json.loads((D / "tag_axis_map.json").read_text(encoding="utf-8"))
mapped = amap["mapped"]

# 探查结构
if isinstance(prof, list):
    items = prof
elif isinstance(prof, dict):
    for k in ("commanders", "profiles", "data", "results"):
        if k in prof and isinstance(prof[k], (list, dict)):
            items = prof[k]
            break
    else:
        items = prof
print("profiles 类型:", type(prof).__name__, "样本数:", len(items))

if isinstance(items, dict):
    sample = next(iter(items.values()))
    names = list(items.items())
else:
    sample = items[0]
    names = [(i.get("name"), i) for i in items]
print("单条字段:", sorted(sample.keys())[:20] if isinstance(sample, dict) else type(sample))
tc = sample.get("tag_counts") if isinstance(sample, dict) else None
print("tag_counts 形态:", type(tc).__name__,
      (list(tc.items())[:3] if isinstance(tc, dict) else tc[:3] if isinstance(tc, list) else tc))


def vector(tag_counts):
    if isinstance(tag_counts, dict):
        pairs = tag_counts.items()
    else:  # list of {tag, count} 之类
        pairs = []
        for e in tag_counts or []:
            if isinstance(e, dict):
                pairs.append((e.get("value") or e.get("tag") or e.get("name"),
                              e.get("count") if e.get("count") is not None else e.get("value")))
            elif isinstance(e, (list, tuple)):
                pairs.append((e[0], e[1]))
    v = Counter()
    hit = miss = 0
    for tag, c in pairs:
        if tag in mapped:
            hit += 1
            for axis, w in mapped[tag].items():
                v[axis] += (c or 0) * w
        else:
            miss += 1
    v["_hit"] = hit
    v["_miss"] = miss
    return v


want = {"Krenko, Mob Boss", "Talrand, Sky Summoner", "Atraxa, Praetors' Voice",
        "Meren of Clan Nel Toth", "Brago, King Eternal", "Grand Arbiter Augustin IV",
        "Light-Paws, Emperor's Voice", "Xenagos, God of Revels", "Yarok, the Desecrated",
        "Niv-Mizzet, Parun", "Tergrid, God of Fright", "Wyleth, Soul of Steel",
        "Muldrotha, the Gravetide", "Phenax, God of Deception", "Sram, Senior Edificer"}
shown = 0
for name, row in names:
    if not isinstance(row, dict):
        continue
    nm = row.get("name") or name
    if nm not in want:
        continue
    tc = row.get("tag_counts")
    if not tc:
        print(f"\n{nm}: 无 tag_counts")
        continue
    v = vector(tc)
    hit, miss = v.pop("_hit", 0), v.pop("_miss", 0)
    tot = sum(v.values()) or 1
    top = v.most_common(6)
    print(f"\n{nm}  (标签 {len(tc)} 个, 命中 {hit}, 未映射 {miss})")
    print("   " + "  ".join(f"{a}={c}({100*c/tot:.0f}%)" for a, c in top))
    shown += 1
print(f"\n打印了 {shown} 位")
