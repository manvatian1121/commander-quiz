#!/usr/bin/env python3
"""交付前最终核对：确认 HTML 内嵌数据完整、与源数据一致。"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from collections import Counter



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)

html = (ROOT / "commander_quiz.html").read_text(encoding="utf-8")
match = re.search(r'<script id="payload" type="application/json">(.*?)</script>',
                  html, re.S)
if not match:
    print("✗ HTML 中找不到 payload")
    raise SystemExit(1)
data = json.loads(match.group(1).replace("<\\/", "</"))

source = json.loads((ROOT / "data" / "commanders.json").read_text(encoding="utf-8"))
cmds = data["commanders"]

print("=== 内嵌数据 ===")
print(f"  题目 {len(data['quiz']['questions'])} 道 / 主将 {len(cmds)} 位 / "
      f"玩法轴 {len(data['axes'])} 个")
print(f"  介绍文 {len(data.get('descriptions', {}))} 篇 / "
      f"搭配牌数据 {len(data.get('cardDisplay', {}))} 组 / "
      f"牌张信息 {len(data.get('cardInfo', {}))} 张")
print(f"  中文名缺失：主将 {sum(1 for c in cmds if not c['zh'])} 位 / "
      f"搭配牌 {sum(1 for v in data.get('cardInfo', {}).values() if not v['zh'])} 张（无中文印刷）")
print(f"  与源数据一致：{len(cmds) == len(source['commanders'])}")
print(f"  文件大小：{(ROOT / 'commander_quiz.html').stat().st_size / 1024:.0f} KB")

print("\n=== 内容自检 ===")
bad = []
for card in cmds:
    entry = data["descriptions"].get(card["en"])
    if not entry or not all(entry.get(k) for k in ("tagline", "intro", "build")):
        bad.append(card["en"])
    picks = data["cardDisplay"].get(card["en"]) or {}
    if not picks.get("synergy"):
        bad.append(f"{card['en']} (无搭配牌)")
print(f"  内容缺失：{len(bad)} 处" + (f" -> {bad[:6]}" if bad else "（全部齐全）"))

print("\n=== 流行度前 2 位示例 ===")
for card in sorted(cmds, key=lambda c: c["all_time_rank"])[:2]:
    entry = data["descriptions"][card["en"]]
    picks = data["cardDisplay"][card["en"]]
    print(f"\n  #{card['all_time_rank']} {card['zh']} / {card['en']}  [{card['colors']}]")
    print(f"     定位：{entry['tagline']}")
    print(f"     介绍：{entry['intro']}")
    print(f"     怎么组：{entry['build']}")
    names = "、".join(data["cardInfo"][n]["zh"] or n for n in picks["synergy"][:4])
    print(f"     高协同牌：{names}")

print("\n=== 分布 ===")
print("  复杂度：" + " ".join(
    f"{k}档{v}" for k, v in sorted(Counter(c["complexity"] for c in cmds).items())))
print("  颜色数：" + " ".join(
    f"{k}色{v}" for k, v in sorted(Counter(len(c["colors"]) for c in cmds).items())))
print(f"  覆盖 EDHREC 全时段 Top 100："
      f"{sum(1 for c in cmds if (c['all_time_rank'] or 9999) <= 100)} 位，"
      f"另有 {sum(1 for c in cmds if (c['all_time_rank'] or 9999) > 100)} 位原型补位")
