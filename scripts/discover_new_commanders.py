#!/usr/bin/env python3
"""发现「新主将」：首次印刷在近期、且在 EDHREC 上真的有套牌数的指挥官。

思路：历史累计排名对新主将天然不利（它们没时间积累），所以换一条路——
先用 Scryfall 按「首次印刷日期」捞出所有新主将，再逐个查 EDHREC 的真实套牌数。
"""
from __future__ import annotations

import json
import pathlib
import re
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
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

SINCE = "2024-06-01"     # 首次印刷在此之后 = 新主将
RANK_CUTOFF = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
MIN_DECKS = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
OUT_NAME = sys.argv[3] if len(sys.argv) > 3 else "new_commander_candidates.json"


def scryfall_page(url: str):
    request = urllib.request.Request(
        url, headers={"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8", "replace"))


def collect_candidates() -> list[dict]:
    query = f"is:commander -is:reprint date>={SINCE}"
    url = ("https://api.scryfall.com/cards/search?unique=cards&order=edhrec&q="
           + urllib.parse.quote(query))
    cards: list[dict] = []
    while url:
        payload = scryfall_page(url)
        for card in payload.get("data", []):
            faces = card.get("card_faces") or []
            cards.append({
                "name": card["name"],
                "released_at": card.get("released_at"),
                "set_name": card.get("set_name"),
                "color_identity": card.get("color_identity"),
                "cmc": card.get("cmc"),
                "type_line": card.get("type_line"),
                "oracle_text": card.get("oracle_text") or "\n//\n".join(
                    f.get("oracle_text", "") for f in faces),
                "keywords": card.get("keywords"),
                "usd": (card.get("prices") or {}).get("usd"),
                "edhrec_rank": card.get("edhrec_rank"),
                "scryfall_uri": card.get("scryfall_uri"),
            })
        url = payload.get("next_page") if payload.get("has_more") else None
        print(f"    Scryfall 累计 {len(cards)} 位 …", flush=True)
        time.sleep(0.15)
    return cards


def slugify(name: str) -> str:
    """EDHREC 的 slug 规则：小写、非字母数字转连字符、去重连字符。"""
    base = name.split(" // ")[0]
    base = base.replace("'", "").replace("\u2019", "").replace(",", "")
    base = base.replace(" ", "-").lower()
    base = re.sub(r"[^a-z0-9\-]", "", base)
    return re.sub(r"-+", "-", base).strip("-")


def edhrec_profile(slug: str):
    url = f"https://json.edhrec.com/pages/commanders/{slug}.json"
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError:
        return None
    except Exception:  # noqa: BLE001
        return None
    card = (payload.get("container") or {}).get("json_dict", {}).get("card") or {}
    return {
        "edhrec_name": card.get("name"),
        "num_decks": card.get("num_decks"),
        "rank": card.get("rank"),
        "salt": card.get("salt"),
        "bracket_counts": payload.get("bracket_counts"),
        "tag_counts": payload.get("tag_counts"),
    }


def main() -> int:
    print(f"① 用 Scryfall 捞出首次印刷 ≥ {SINCE} 的主将")
    candidates = collect_candidates()
    print(f"   共 {len(candidates)} 位")

    ranked = [c for c in candidates
              if isinstance(c.get("edhrec_rank"), int) and c["edhrec_rank"] <= RANK_CUTOFF]
    ranked.sort(key=lambda c: c["edhrec_rank"])
    print(f"② 卡牌热度粗筛（EDHREC rank ≤ {RANK_CUTOFF}）：{len(ranked)} 位需要查 EDHREC")

    results: list[dict] = []
    failures = 0
    for index, card in enumerate(ranked, 1):
        slug = slugify(card["name"])
        profile = edhrec_profile(slug)
        if profile is None or not profile.get("num_decks"):
            failures += 1
            time.sleep(0.2)
            continue
        results.append({**card, "slug": slug, **profile})
        if index % 50 == 0:
            print(f"     …{index}/{len(ranked)}  已命中 {len(results)}", flush=True)
        time.sleep(0.28)

    keep = [r for r in results if r["num_decks"] >= MIN_DECKS]
    keep.sort(key=lambda r: -r["num_decks"])

    (DATA / OUT_NAME).write_text(
        json.dumps(keep, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n③ 有 EDHREC 档案的 {len(results)} 位，无档案/无套牌数 {failures} 位")
    print(f"④ 套牌数 ≥ {MIN_DECKS} 的：{len(keep)} 位")
    for row in keep[:35]:
        print(f"   {row['num_decks']:>6} 副  #{row['rank']:>4}  "
              f"{row['released_at']}  {row['name'][:40]}")
    print(f"\n已写出 {OUT_NAME}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
