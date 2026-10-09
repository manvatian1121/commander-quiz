# -*- coding: utf-8 -*-
"""检查 151 位主将的全部标签里，未映射的究竟是哪些 —— 应当全部是 ignored 名单。"""
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
mapped, ignored = amap["mapped"], amap["ignored"]

allt, unmapped = Counter(), Counter()
for row in prof.values():
    for e in row.get("tag_counts") or []:
        t = e.get("value")
        allt[t] += 1
        if t not in mapped:
            unmapped[t] += 1

print(f"151 位主将共触及 {len(allt)} 种标签（词表 404 种）")
print(f"未映射标签 {len(unmapped)} 种，出现总次数 {sum(unmapped.values())}")
notignored = {t: c for t, c in unmapped.items() if t not in ignored}
print(f"\n未在 ignored 名单里的未映射标签: {len(notignored)}")
for t, c in sorted(notignored.items(), key=lambda kv: -kv[1]):
    print(f"  {t:<28} 出现在 {c} 位主将")
print("\nignored 名单里实际被用到的:")
for t, c in sorted(unmapped.items(), key=lambda kv: -kv[1]):
    print(f"  {t:<28} {c} 位")
print("\n词表里从未出现的标签数:", 404 - len(allt))
