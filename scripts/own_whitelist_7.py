# -*- coding: utf-8 -*-
"""逐主将白名单校验：每条文案里提到的英文牌名，必须出现在**该主将自己**的
「协同度最高的牌 / 出场率最高的牌」清单里（或就是主将本人）。

比全局白名单更严：防止把 A 主将清单里的牌写到 B 主将身上。
"""
import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
SRC = DATA / "writing_batch_new_4.md"
OUT = DATA / "descriptions_7.json"

cur = None
own = {}
order = []
for line in SRC.read_text(encoding="utf-8").splitlines():
    m = re.match(r"^## (.+?) ｜", line)
    if m:
        cur = m.group(1).strip()
        own[cur] = {cur}
        order.append(cur)
        continue
    if cur is None:
        continue
    m = re.match(r"^(?:\d+\.|[-*])\s+(.+?)\uff08", line.strip())
    if m:
        n = m.group(1).strip()
        if n and not n.startswith("**"):
            own[cur].add(n)

data = json.loads(OUT.read_text(encoding="utf-8"))
bad = []
stats = []
for k in order:
    e = data[k]
    used = []
    for f in ("tagline", "intro", "build"):
        for m in re.finditer(r"（([A-Za-z][^（）]*?)）", e[f]):
            frag = m.group(1).strip()
            used.append(frag)
            if frag not in own[k]:
                bad.append((k, f, frag))
    stats.append((k, len(own[k]) - 1, len(used)))

print("逐主将白名单校验：", "通过" if not bad else "失败")
for b in bad:
    print("   ✗", b)
print("\n每条文案引用的牌数（清单容量 → 引用数）：")
for k, cap, n in stats:
    print(f"   {n} / {cap:<3} {k}")
print(f"\n合计引用 {sum(n for _, _, n in stats)} 处；每条平均 "
      f"{sum(n for _, _, n in stats) / len(stats):.2f} 处")
