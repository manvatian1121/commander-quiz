#!/usr/bin/env python3
"""检查「能当主将的非生物牌」（鹏洛客、神器、结界）有没有被漏掉。

Scryfall 的 is:commander 包含所有「牌面写明可当主将」的牌，
包括写了 "can be your commander" 的鹏洛客。这里把这类牌全查出来，
与现有主将池对比。
"""
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


def search(query: str, pages: int = 6):
    url = ("https://api.scryfall.com/cards/search?unique=cards&order=edhrec&q="
           + urllib.parse.quote(query))
    out = []
    while url and pages > 0:
        request = urllib.request.Request(
            url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                payload = json.loads(response.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as error:
            print(f"  查询失败 HTTP {error.code}")
            return out
        out.extend(payload.get("data", []))
        url = payload.get("next_page") if payload.get("has_more") else None
        pages -= 1
        time.sleep(0.2)
    return out


def main() -> None:
    pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    profiles = json.loads((DATA / "commander_profiles.json").read_text(encoding="utf-8"))
    in_pool = {c["en"] for c in pool["commanders"]}

    print("=== 能当主将的非生物牌（鹏洛客 / 神器 / 结界）===")
    cards = search("is:commander -t:creature")
    print(f"共 {len(cards)} 张\n")

    buckets: dict[str, list] = {}
    for card in cards:
        type_line = card.get("type_line") or ""
        if "Planeswalker" in type_line:
            key = "鹏洛客"
        elif "Artifact" in type_line:
            key = "神器"
        elif "Enchantment" in type_line:
            key = "结界"
        else:
            key = "其它"
        buckets.setdefault(key, []).append(card)

    for key, group in buckets.items():
        missing = [c for c in group if c["name"] not in in_pool
                   and c["name"].split(" // ")[0] not in in_pool]
        print(f"\n── {key}：共 {len(group)} 张，其中 {len(missing)} 张不在池中")
        for card in missing[:25]:
            profile = profiles.get(card["name"]) or {}
            decks = profile.get("num_decks")
            print(f"     {card['released_at']}  {card['name'][:40]:<40} "
                  f"{card.get('set_name', '')[:22]:<22} "
                  f"EDHREC {'无档案' if decks is None else str(decks) + ' 副'}")
        if len(missing) > 25:
            print(f"     …还有 {len(missing) - 25} 张")

    # 重点确认：提问里提到的那张
    print("\n=== 单独确认 ===")
    for probe in ["Jace, Multiverse Architect", "Jace, Vryn's Prodigy",
                  "Nissa, Leyline Tamer", "Dack Fayden, Helping Hand"]:
        card = next((c for c in cards if c["name"].startswith(probe.split(",")[0])
                     and probe.split(",")[0] in c["name"]), None)
        profile = profiles.get(probe) or {}
        print(f"  {probe}")
        print(f"    Scryfall 查到：{'是' if card else '否'}"
              f"{'（' + (card.get('type_line') or '') + '）' if card else ''}")
        print(f"    池中：{'在' if probe in in_pool else '不在'}"
              f"　EDHREC 套牌数：{profile.get('num_decks', '无档案')}")


if __name__ == "__main__":
    main()
