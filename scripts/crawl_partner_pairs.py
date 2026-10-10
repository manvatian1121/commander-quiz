#!/usr/bin/env python3
"""用「相似主将」关系爬出热门拍档 / 身世组合。

全枚举要 4302 组 ×2 种顺序 ≈ 43 分钟，太慢。
改成从已知的热门组合出发爬 similar 字段——拍档之间往往互相推荐，
两三跳就能覆盖热门的那一批。
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"D:\万智\commander-quiz\data")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

DIACRITICS = str.maketrans({"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
                            "ñ": "n", "û": "u", "ü": "u", "à": "a", "â": "a"})

# 已知存在的组合（探针验过），两种顺序都放进来当种子
SEEDS = [
    "Kraum, Ludevic's Opus // Tymna the Weaver",
    "Thrasios, Triton Hero // Tymna the Weaver",
    "Rograkh, Son of Rohgahh // Silas Renn, Seeker Adept",
    "Akiri, Line-Slinger // Bruse Tarl, Boorish Herder",
    "Gale, Waterdeep Prodigy // Scion of Halaster",
    "Karlach, Fury of Avernus // Sword Coast Sailor",
    "Shadowheart, Dark Justiciar // Haunted One",
    "Lae'zel, Vlaakith's Champion // Noble Heritage",
    "Wilson, Refined Grizzly // Tavern Brawler",
    "Jaheira, Friend of the Forest // Guild Artisan",
    "Wyll, Blade of Frontiers // Candlekeep Sage",
]


def slugify(name: str) -> str:
    base = name.translate(DIACRITICS).replace("'", "").replace("\u2019", "")
    base = base.replace(",", "").replace(" // ", "-").replace(" ", "-").lower()
    base = re.sub(r"[^a-z0-9\-]", "", base)
    return re.sub(r"-+", "-", base).strip("-")


def fetch(slug: str):
    url = f"https://json.edhrec.com/pages/commanders/{slug}.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception:  # noqa: BLE001
        return None


def profile(payload):
    card = (payload.get("container") or {}).get("json_dict", {}).get("card") or {}
    if not card.get("num_decks"):
        return None
    return {"name": card.get("name"), "num_decks": card.get("num_decks"),
            "rank": card.get("rank"), "slug": card.get("slug"),
            "color_identity": card.get("color_identity")}


def main() -> int:
    seen: dict[str, dict] = {}
    queue = [(n, slugify(n)) for n in SEEDS]
    tried = set()

    for depth in range(3):
        nxt: list[tuple[str, str]] = []
        print(f"\n--- 第 {depth + 1} 轮：{len(queue)} 个待查 ---")
        for name, slug in queue:
            if slug in tried:
                continue
            tried.add(slug)
            payload = fetch(slug)
            if payload is None:
                time.sleep(0.3)
                continue
            prof = profile(payload)
            if prof and prof.get("name"):
                seen[prof["name"]] = prof
            for sim in (payload.get("similar") or []):
                if isinstance(sim, str) and "//" in sim:
                    nxt.append((sim, slugify(sim)))
            time.sleep(0.3)
        queue = [(n, s) for n, s in nxt if s not in tried]
        if not queue:
            break

    rows = sorted(seen.values(), key=lambda r: -(r["num_decks"] or 0))
    (DATA / "partner_candidates.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n=== 找到 {len(rows)} 个组合（含 // 的双主将条目）===")
    print(f"  {'组合':<54} {'套牌数':>8} {'排名':>6}  色")
    for r in rows[:30]:
        print(f"  {r['name'][:52]:<52} {r['num_decks']:>8,} "
              f"{str(r['rank']):>6}  {''.join(r['color_identity'] or [])}")

    over = [r for r in rows if r["num_decks"] >= 1000]
    print(f"\n套牌数 ≥1000 的：{len(over)} 个")
    for r in over:
        print(f"  {r['num_decks']:>7,}  {r['name']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
