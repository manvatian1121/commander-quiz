# -*- coding: utf-8 -*-
"""解析 4 份 writing_batch_new_*.md 素材，产出 descriptions_8 写作索引：
   { 主将英文名: { "zh": 主将中文名, "file": 来源, "cards": { 牌英文名: 中文名 or None } } }
中文名一律查 card_zh.json，查不到留 None。
"""
import io
import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

DATA = pathlib.Path(ROOT / "data")
OUT = pathlib.Path(SCRIPT_DIR / "_material_index_8.json")

zh_map = json.loads((DATA / "card_zh.json").read_text(encoding="utf-8"))

index = {}
order = []
miss_zh = []
for i in (1, 2, 3, 4):
    src = DATA / f"writing_batch_new_{i}.md"
    text = src.read_text(encoding="utf-8")
    cur = None
    for line in text.splitlines():
        m = re.match(r"^## (.+?) ｜ (.+?)\s*$", line)
        if m:
            en, zh = m.group(1).strip(), m.group(2).strip()
            cur = en
            index[en] = {"zh": zh_map.get(en), "zh_material": zh,
                         "file": src.name, "cards": {}}
            order.append(en)
            if en not in zh_map:
                miss_zh.append(("COMMANDER", en, zh))
            continue
        if cur is None:
            continue
        m = re.match(r"^(?:\d+\.|[-*])\s+(.+?)\uff08", line.strip())
        if not m:
            continue
        name = m.group(1).strip()
        if not name or name.startswith("**"):
            continue
        index[cur]["cards"][name] = zh_map.get(name)
        if name not in zh_map:
            miss_zh.append(("CARD", cur, name))

OUT.write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"主将 {len(order)} 位，写出 {OUT}")
for en in order:
    e = index[en]
    n_cards = len(e["cards"])
    zh_ok = sum(1 for v in e["cards"].values() if v)
    print(f"  {en:<40} zh={e['zh'] or '（无官方中文名）':<20} "
          f"{n_cards:>2} 张搭配牌（{zh_ok} 有中文名）")

print("\n缺中文名的条目：")
for kind, who, name in miss_zh:
    print(f"  [{kind}] {who} → {name}")
