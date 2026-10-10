#!/usr/bin/env python3
"""为拍档 / 身世组合补齐牌面数据与中文名。

组合（"A // B"）在 Scryfall 里不是一张牌，在 mtgch 里也不是一个单卡，
所以 fetch 全部落空。正确做法是取两半的数据自己合成：
  颜色标识 = 两边并集　法术力值 = 两边相加　牌面文字 = 两段拼起来
  中文名   = 两边各自的官方中文名拼起来
"""
from __future__ import annotations

import json
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(r"D:\万智\commander-quiz\data")
UA = {"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"}
MTGCH = {"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"}
ORDER = "WUBRG"


def get(url, headers):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers),
                                    timeout=40) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception:  # noqa: BLE001
        return None


def scryfall_card(name: str):
    for endpoint in (f"/cards/named?exact={urllib.parse.quote(name)}",
                     f"/cards/named?fuzzy={urllib.parse.quote(name)}"):
        card = get("https://api.scryfall.com" + endpoint, UA)
        if card and card.get("name") and " // " not in card.get("name", ""):
            return card
    return None


def mtgch_zh(name: str) -> str:
    payload = get("https://mtgch.com/api/v1/autocomplete/?"
                  + urllib.parse.urlencode({"q": name, "view": "name"}), MTGCH)
    for item in (payload or {}).get("items") or []:
        cand = item.get("name") or ""
        zh = item.get("display_name") or item.get("translated_name") or ""
        if zh and (cand == name or cand.startswith(name + " //")):
            return zh.split(" // ")[0].strip()
    return ""


def main() -> int:
    members = json.loads((DATA / "new_pool_members.json").read_text(encoding="utf-8"))
    pairs = [n for n in members if " // " in n]
    scry = json.loads((DATA / "commanders_scryfall.json").read_text(encoding="utf-8"))
    zh = json.loads((DATA / "commander_zh.json").read_text(encoding="utf-8"))

    print(f"待合成 {len(pairs)} 组\n")
    done = 0
    for name in pairs:
        if name in scry and zh.get(name):
            continue
        left, right = name.split(" // ", 1)
        a, b = scryfall_card(left), scryfall_card(right)
        time.sleep(0.15)
        if not (a and b):
            print(f"  ✗ {name}：Scryfall 取不到 {'两半' if not (a and b) else ''}")
            continue

        ci = [c for c in ORDER
              if c in (a.get("color_identity") or []) or c in (b.get("color_identity") or [])]
        scry[name] = {
            "name": name,
            "mana_cost": (a.get("mana_cost") or "") + " // " + (b.get("mana_cost") or ""),
            "cmc": (a.get("cmc") or 0) + (b.get("cmc") or 0),
            "type_line": f"{a.get('type_line', '')} // {b.get('type_line', '')}",
            "oracle_text": f"{a.get('oracle_text', '')}\n//\n{b.get('oracle_text', '')}",
            "color_identity": ci,
            "keywords": sorted(set(a.get("keywords") or []) | set(b.get("keywords") or [])),
            "set": a.get("set"),
            "set_name": f"{a.get('set_name')} / {b.get('set_name')}",
            "released_at": max(a.get("released_at") or "", b.get("released_at") or ""),
            "edhrec_rank": min(x for x in (a.get("edhrec_rank"), b.get("edhrec_rank"))
                               if isinstance(x, int)) if any(
                isinstance(x, int) for x in (a.get("edhrec_rank"), b.get("edhrec_rank"))) else None,
            "usd": str(round(float(a.get("prices", {}).get("usd") or 0)
                             + float(b.get("prices", {}).get("usd") or 0), 2)),
            "commander_legal": "legal",
            "is_legendary_creature": True,
            "can_be_commander": True,
            "is_partner_pair": True,
        }

        za = zh.get(left) or mtgch_zh(left)
        time.sleep(0.28)
        zb = zh.get(right) or mtgch_zh(right)
        time.sleep(0.28)
        if za and zb:
            zh[name] = f"{za} // {zb}"
        done += 1
        flag = "✓" if (za and zb) else "△"
        print(f"  {flag} {name}")
        print(f"      颜色 {''.join(ci)}　法术力值 {scry[name]['cmc']:.0f}　"
              f"中文名 {zh.get(name) or '（缺）'}")

    (DATA / "commanders_scryfall.json").write_text(
        json.dumps(scry, ensure_ascii=False, indent=2), encoding="utf-8")
    (DATA / "commander_zh.json").write_text(
        json.dumps(zh, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n✓ 合成 {done} 组")
    missing = [n for n in pairs if not zh.get(n)]
    if missing:
        print(f"⚠ 仍缺中文名 {len(missing)} 组：")
        for n in missing:
            print(f"    {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
