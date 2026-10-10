#!/usr/bin/env python3
"""探测：用「首次印刷日期」找出新主将，避免被重印年份误导。
同时看看 similar 字段长什么样（能不能用来挖更深的名单）。"""
from __future__ import annotations

import json
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
UA = "dsh-mtg-agent/1.0"


def search(query: str, order: str = "edhrec"):
    url = ("https://api.scryfall.com/cards/search?unique=cards&order=" + order
           + "&q=" + urllib.parse.quote(query))
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            return json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as error:
        return {"__err__": error.code}


print("=== similar 字段内容 ===")
raw = json.loads((DATA / "supp_brago-king-eternal.json").read_text(encoding="utf-8"))
print(" ", raw.get("similar"))

print("\n=== 首次印刷在 2025-01-01 之后的主将 ===")
for since in ("2024-06-01", "2025-01-01"):
    payload = search(f"is:commander -is:reprint date>={since}")
    if "__err__" in payload:
        print(f"  {since}: 查询失败 {payload['__err__']}")
        continue
    total = payload.get("total_cards")
    print(f"\n  ── since {since}：共 {total} 位")
    for card in payload.get("data", [])[:25]:
        print(f"     {card.get('released_at')}  {card.get('name')[:42]:<42} "
              f"{card.get('set_name', '')[:28]}")
    time.sleep(0.2)
