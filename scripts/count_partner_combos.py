#!/usr/bin/env python3
"""先数清楚：拍档与身世的组合规模有多大，决定怎么探。"""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")


def scryfall(query: str):
    url = ("https://api.scryfall.com/cards/search?unique=cards&order=edhrec&q="
           + urllib.parse.quote(query))
    out = []
    while url:
        req = urllib.request.Request(url, headers={
            "User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                payload = json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            print(f"  HTTP {e.code} for {query}")
            return out
        out.extend(payload.get("data", []))
        url = payload.get("next_page") if payload.get("has_more") else None
        time.sleep(0.15)
    return out


QUERIES = {
    "泛用拍档 Partner": 'is:commander oracle:"Partner" -oracle:"Partner with"',
    "指定拍档 Partner with": 'is:commander oracle:"Partner with"',
    "可挑身世 Choose a Background": 'is:commander oracle:"Choose a Background"',
    "身世牌 Background": 't:background',
    "永结同心 Friends forever": 'is:commander oracle:"Friends forever"',
    "博士旅伴 Doctor\'s companion": 'is:commander oracle:"Doctor\'s companion"',
}

counts = {}
for label, query in QUERIES.items():
    cards = scryfall(query)
    counts[label] = cards
    print(f"{label:<28} {len(cards):>4} 张")
    if cards and len(cards) <= 8:
        for c in cards:
            print(f"      {c['name']}")

n = {k: len(v) for k, v in counts.items()}
generic = n["泛用拍档 Partner"]
bg_cmd = n["可挑身世 Choose a Background"]
bg = n["身世牌 Background"]
ff = n["永结同心 Friends forever"]
doc = n["博士旅伴 Doctor's companion"]

print(f"\n=== 组合规模估算 ===")
print(f"  泛用拍档两两组合：{generic}×{generic - 1}/2 = {generic * (generic - 1) // 2}")
print(f"  身世组合：{bg_cmd}×{bg} = {bg_cmd * bg}")
print(f"  永结同心两两：{ff * (ff - 1) // 2}")
print(f"  博士旅伴 × 博士：{doc}×? ")
print(f"\n  合计约 {generic * (generic - 1) // 2 + bg_cmd * bg + ff * (ff - 1) // 2} 组，"
      f"每种顺序都试 → 再翻倍")

out = {
    "generic_partner": [c["name"] for c in counts["泛用拍档 Partner"]],
    "partner_with": [c["name"] for c in counts["指定拍档 Partner with"]],
    "choose_background": [c["name"] for c in counts["可挑身世 Choose a Background"]],
    "backgrounds": [c["name"] for c in counts["身世牌 Background"]],
    "friends_forever": [c["name"] for c in counts["永结同心 Friends forever"]],
    "doctors_companion": [c["name"] for c in counts["博士旅伴 Doctor's companion"]],
}
import pathlib
pathlib.Path(r"D:\万智\commander-quiz\data\partner_pool.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("\n已写出 data/partner_pool.json")
