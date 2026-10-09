#!/usr/bin/env python3
"""用 Scryfall 独立确认这几张牌是否有中文印刷。"""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = "dsh-mtg-agent/1.0"

TARGETS = [
    "Summon: Bahamut",
    "Summon: Titan",
    "Sidequest: Raise a Chocobo",
]


def fetch(url: str):
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as error:
        return {"__http_error__": error.code}


for name in TARGETS:
    quoted = urllib.parse.quote(name)
    print(f"\n=== {name} ===")
    base = fetch(f"https://api.scryfall.com/cards/named?exact={quoted}")
    if "__http_error__" in base:
        print(f"  英文查询失败 {base['__http_error__']}")
        continue
    print(f"  英文版: {base.get('name')}  系列={base.get('set_name')}  印刷={base.get('printed_name')}")
    sets = base.get("set")
    number = base.get("collector_number")
    # 该系列是否出过中文印刷
    zh = fetch(f"https://api.scryfall.com/cards/{sets}/{number}/zhs")
    if "__http_error__" in zh:
        print(f"  zhs 中文印刷: 不存在（HTTP {zh['__http_error__']}）")
    else:
        print(f"  zhs 中文印刷: {zh.get('printed_name')} / {zh.get('name')}")
    time.sleep(0.2)
