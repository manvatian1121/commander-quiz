#!/usr/bin/env python3
"""探测 EDHREC 上的「拍档组合」与「身世组合」条目。

假设：EDHREC 把一对拍档当成一个独立条目（如 "Tymna the Weaver // Kraum,
Ludevic's Opus"），而本项目按单卡名推 slug，所以一条都找不到。
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

DIACRITICS = str.maketrans({"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
                            "ñ": "n", "û": "u", "ü": "u", "à": "a"})


def slugify(name: str) -> str:
    base = name.translate(DIACRITICS).replace("'", "").replace("\u2019", "")
    base = base.replace(",", "").replace(" // ", "-").replace(" ", "-").lower()
    base = re.sub(r"[^a-z0-9\-]", "", base)
    return re.sub(r"-+", "-", base).strip("-")


def probe(name: str):
    for slug in (slugify(name), slugify(name.split(" // ")[0]) + "-" + slugify(
            name.split(" // ")[1]) if " // " in name else None):
        if not slug:
            continue
        url = f"https://json.edhrec.com/pages/commanders/{slug}.json"
        req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                   "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                payload = json.loads(r.read().decode("utf-8", "replace"))
        except Exception:  # noqa: BLE001
            continue
        card = (payload.get("container") or {}).get("json_dict", {}).get("card") or {}
        if card.get("num_decks"):
            return card.get("name"), card.get("num_decks"), card.get("rank"), slug
        time.sleep(0.3)
    return None


CANDIDATES = [
    # 泛用拍档（任意组合）
    "Tymna the Weaver // Kraum, Ludevic's Opus",
    "Thrasios, Triton Hero // Tymna the Weaver",
    "Tymna the Weaver // Thrasios, Triton Hero",
    "Vial Smasher the Fierce // Thrasios, Triton Hero",
    "Kraum, Ludevic's Opus // Tymna the Weaver",
    "Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept",
    "Akiri, Line-Slinger // Bruse Tarl, Boorish Herder",
    "Livio, Oathsworn Sentinel // Ardenn, Intrepid Archaeologist",
    "Malcolm, Keen-Eyed Navigator // Breeches, Brazen Plunderer",
    "Kediss, Emberclaw Familiar // Ardenn, Intrepid Archaeologist",
    # 指定拍档
    "Kynaios and Tiro of Meletis",
    # 身世（Choose a Background）
    "Wilson, Refined Grizzly // Tavern Brawler",
    "Karlach, Fury of Avernus // Sword Coast Sailor",
    "Jaheira, Friend of the Forest // Guild Artisan",
    "Gale, Waterdeep Prodigy // Scion of Halaster",
    "Lae'zel, Vlaakith's Champion // Noble Heritage",
    "Shadowheart, Dark Justiciar // Haunted One",
    "Astarion, the Decadent // Agent of the Shadow Thieves",
    "Wyll, Blade of Frontiers // Candlekeep Sage",
    "Minthara, Merciless Soul // Cultist of the Absolute",
]

print(f"{'组合':<52} {'套牌数':>8} {'排名':>6}")
print("-" * 72)
hits = []
for name in CANDIDATES:
    r = probe(name)
    if r:
        n, decks, rank, slug = r
        print(f"  {n[:50]:<50} {decks:>8,} {str(rank):>6}")
        hits.append((n, decks, rank))
    else:
        print(f"  {name[:50]:<50} {'—':>8} {'—':>6}  （无档案）")
    time.sleep(0.3)

print(f"\n命中 {len(hits)}/{len(CANDIDATES)}")
if hits:
    hits.sort(key=lambda x: -x[1])
    print(f"套牌数最高：{hits[0][0]}（{hits[0][1]:,} 副）")
