#!/usr/bin/env python3
"""用 EDHREC 的「相似主将」关系挖出更多候选。

主将页里有个 similar 字段，列出 6 位玩法相近的主将。从现有池子出发爬一跳，
就能发现大量历史排名 101~200 的主将——这是拿不到完整排行列表时的替代发现路径。
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

MIN_DECKS = int(sys.argv[1]) if len(sys.argv) > 1 else 12000


def slugify(name: str) -> str:
    base = name.split(" // ")[0]
    base = base.replace("'", "").replace("\u2019", "").replace(",", "")
    base = base.replace(" ", "-").lower()
    base = re.sub(r"[^a-z0-9\-]", "", base)
    return re.sub(r"-+", "-", base).strip("-")


def fetch_page(slug: str):
    url = f"https://json.edhrec.com/pages/commanders/{slug}.json"
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8", "replace"))
    except Exception:  # noqa: BLE001
        return None


def profile_of(payload: dict):
    if not payload:
        return None
    card = (payload.get("container") or {}).get("json_dict", {}).get("card") or {}
    if not card.get("num_decks"):
        return None
    return {
        "edhrec_name": card.get("name"),
        "slug": card.get("slug"),
        "num_decks": card.get("num_decks"),
        "rank": card.get("rank"),
        "salt": card.get("salt"),
        "color_identity": card.get("color_identity"),
        "type_line": card.get("type_line"),
        "cmc": card.get("cmc"),
        "bracket_counts": payload.get("bracket_counts"),
        "tag_counts": payload.get("tag_counts"),
    }


def main() -> int:
    pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    profiles = json.loads((DATA / "commander_profiles.json").read_text(encoding="utf-8"))
    known = {c["en"] for c in pool["commanders"]}
    known_slugs = {p.get("slug") for p in profiles.values() if p.get("slug")}

    seeds = [p["slug"] for p in profiles.values()
             if p.get("slug") and p.get("name", p.get("edhrec_name")) in known]
    seeds = sorted(set(seeds))
    print(f"种子 {len(seeds)} 位现有主将，爬取它们的 similar 列表")

    neighbors: dict[str, str] = {}
    for index, slug in enumerate(seeds, 1):
        payload = fetch_page(slug)
        for name in (payload or {}).get("similar") or []:
            if isinstance(name, str) and slugify(name) not in known_slugs:
                neighbors[slugify(name)] = name
        if index % 25 == 0:
            print(f"   …{index}/{len(seeds)}  已发现 {len(neighbors)} 位新候选", flush=True)
        time.sleep(0.28)

    print(f"\n发现 {len(neighbors)} 位不在池中的候选，逐个查档案")

    found: list[dict] = []
    for index, (slug, name) in enumerate(sorted(neighbors.items()), 1):
        profile = profile_of(fetch_page(slug))
        if profile and profile["num_decks"] >= MIN_DECKS:
            found.append({**profile, "name": name, "slug": slug})
        if index % 50 == 0:
            print(f"   …{index}/{len(neighbors)}  已达门槛 {len(found)}", flush=True)
        time.sleep(0.28)

    found.sort(key=lambda r: -(r["num_decks"] or 0))
    (DATA / "similar_candidates.json").write_text(
        json.dumps(found, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n套牌数 ≥ {MIN_DECKS} 的：{len(found)} 位")
    for row in found[:45]:
        print(f"   {row['num_decks']:>6} 副  #{row['rank']:>4}  "
              f"{''.join(row['color_identity'] or []):<6} {row['edhrec_name']}")
    print(f"\n已写出 similar_candidates.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
