#!/usr/bin/env python3
"""按关键词在主将池里查找。用法：python lookup_commander.py 关键词1 [关键词2 ...]"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)
data = json.loads((ROOT / "data" / "commanders.json").read_text(encoding="utf-8"))
desc = json.loads((ROOT / "data" / "descriptions_1.json").read_text(encoding="utf-8"))
for i in (2, 3):
    desc.update(json.loads((ROOT / "data" / f"descriptions_{i}.json").read_text(encoding="utf-8")))
cards = json.loads((ROOT / "data" / "card_display.json").read_text(encoding="utf-8"))
card_zh = json.loads((ROOT / "data" / "card_zh.json").read_text(encoding="utf-8"))
tag_zh = json.loads((ROOT / "data" / "tag_zh.json").read_text(encoding="utf-8"))

queries = sys.argv[1:] or ["Wilhelt"]
pool = data["commanders"]
print(f"主将池共 {len(pool)} 位\n")

for query in queries:
    q = query.lower()
    hits = [c for c in pool
            if q in c["en"].lower() or q in (c["zh"] or "").lower() or q in c["id"].lower()]
    print(f"=== 搜索「{query}」→ 命中 {len(hits)} 位 ===")
    for card in hits:
        tagline = (desc.get(card["en"]) or {}).get("tagline", "")
        top_tags = "、".join(tag_zh.get(t, t) for t in card["top_tags"][:5])
        axes = sorted(card["vec"].items(), key=lambda kv: -kv[1])[:4]
        axis_zh = {"aggro": "快攻", "voltron": "主将单挑", "wide": "铺场", "ramp": "加速",
                   "stompy": "大生物", "control": "控制", "removal": "去除", "combo": "组合技",
                   "spells": "法术连发", "artifacts": "神器", "enchant": "结界", "grave": "坟场",
                   "tribal": "部落", "drain": "吸血", "stax": "锁场", "clonesteal": "偷取复制",
                   "politics": "政治", "chaos": "随机", "counters": "指示物", "blink": "闪现"}
        print(f"\n  ✓ 在池中：{card['zh']} / {card['en']}")
        print(f"     EDHREC 全时段第 {card['all_time_rank']} 位（约 {card['num_decks']} 副套牌）")
        print(f"     颜色 {card['colors']} ｜ {card['cmc']:g} 费 ｜ {card['type']}")
        print(f"     难度 {card['complexity']}/5 ｜ 造价 {card['budget']}/5 ｜ "
              f"咸度 {card['salt']} ｜ Bracket {card['bracket']}")
        print(f"     定位：{tagline}")
        entry = desc.get(card["en"]) or {}
        if entry.get("intro"):
            print(f"     介绍：{entry['intro']}")
        if entry.get("build"):
            print(f"     怎么组：{entry['build']}")
        print(f"     玩法轴：{[(axis_zh.get(a, a), v) for a, v in axes]}")
        print(f"     标签：{top_tags}")
        picks = (cards.get(card["en"]) or {}).get("synergy", [])[:5]
        print(f"     高协同牌：{'、'.join(card_zh.get(n) or n for n in picks)}")
    if not hits:
        print("  ✗ 不在主将池中")
    print()
