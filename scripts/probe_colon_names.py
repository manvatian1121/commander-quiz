#!/usr/bin/env python3
"""探测带冒号牌名的中文匹配策略（确定性规则，不做相似匹配）。"""
from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
BASE = "https://mtgch.com/api/v1"

TARGETS = [
    "Sidequest: Raise a Chocobo",
    "Summon: Bahamut",
    "Summon: Fenrir",
    "Summon: Knights of Round",
    "Summon: Primal Odin",
    "Summon: Titan",
    "Summon: Yojimbo",
]


def auto(query: str):
    url = BASE + "/autocomplete/?" + urllib.parse.urlencode({"q": query, "view": "name"})
    request = urllib.request.Request(
        url, headers={"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.loads(response.read().decode("utf-8", "replace"))


def show(label: str, query: str) -> None:
    try:
        payload = auto(query)
    except Exception as error:  # noqa: BLE001
        print(f"  [{label}] q={query!r} -> 异常 {error}")
        return
    items = payload.get("items") or []
    print(f"  [{label}] q={query!r} -> {len(items)} 条")
    for item in items[:6]:
        print(f"      name={item.get('name')!r}  display_name={item.get('display_name')!r}")
    time.sleep(0.3)


for name in TARGETS[:3]:
    print(f"\n=== {name} ===")
    show("全名", name)
    if ":" in name:
        show("冒号后", name.split(":", 1)[1].strip())
    show("首单词", name.split(":")[0].strip())
