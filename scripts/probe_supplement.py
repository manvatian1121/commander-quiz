#!/usr/bin/env python3
"""探测 EDHREC 单主将详情端点 + 更多榜单路径，用于验证补充名单的流行度。"""
from __future__ import annotations

import json
import pathlib
import sys
import urllib.error
import urllib.request

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

LIST_PATHS = [
    "commanders/past-2-years.json",
    "commanders/2-years.json",
    "commanders/decade.json",
    "commanders/alltime.json",
    "commanders/all-time.json",
]

# 补充候选：填补 Voltron / Blink / 控制 / 磨牌 / 结界 等原型缺口
SUPPLEMENT = [
    ("Sram, Senior Edificer", "sram-senior-edificer"),
    ("Brago, King Eternal", "brago-king-eternal"),
    ("Tergrid, God of Fright", "tergrid-god-of-fright"),
    ("Talrand, Sky Summoner", "talrand-sky-summoner"),
    ("Phenax, God of Deception", "phenax-god-of-deception"),
    ("Anikthea, Hand of Erebos", "anikthea-hand-of-erebos"),
    ("Light-Paws, Emperor's Voice", "light-paws-emperors-voice"),
    ("Yarok, the Desecrated", "yarok-the-desecrated"),
    ("Grand Arbiter Augustin IV", "grand-arbiter-augustin-iv"),
    ("Krenko, Tin Street Kingpin", "krenko-tin-street-kingpin"),
    ("Atraxa, Grand Unifier", "atraxa-grand-unifier"),
    ("Wyleth, Soul of Steel", "wyleth-soul-of-steel"),
    ("Muldrotha, the Gravetide", "muldrotha-the-gravetide"),
    ("Xenagos, God of Revels", "xenagos-god-of-revels"),
    ("Niv-Mizzet, Parun", "niv-mizzet-parun"),
    ("Kess, Dissident Mage", "kess-dissident-mage"),
]


def fetch(url: str):
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as error:
        return error.code, b""
    except Exception as error:  # noqa: BLE001
        return type(error).__name__, b""


def find_decks(node, found=None):
    """找 num_decks 字段。"""
    if found is None:
        found = []
    if isinstance(node, dict):
        if "num_decks" in node and "name" in node:
            found.append((node.get("name"), node.get("num_decks"), node.get("rank")))
        for value in node.values():
            find_decks(value, found)
    elif isinstance(node, list):
        for item in node:
            find_decks(item, found)
    return found


if __name__ == "__main__":
    print("=== 探测更多榜单路径 ===")
    for path in LIST_PATHS:
        status, body = fetch("https://json.edhrec.com/pages/" + path)
        print(f"[{status}] {path} {len(body)}B")

    print("\n=== 补充候选主将流行度（EDHREC 单卡页 num_decks）===")
    results = []
    for name, slug in SUPPLEMENT:
        status, body = fetch(f"https://json.edhrec.com/pages/commanders/{slug}.json")
        if status != 200:
            print(f"[{status}] {name}")
            results.append({"name": name, "slug": slug, "num_decks": None})
            continue
        payload = json.loads(body.decode("utf-8", "replace"))
        decks = find_decks(payload)
        top = max((d for d in decks if isinstance(d[1], int)), key=lambda d: d[1], default=None)
        print(f"[OK] {name:34s} num_decks={top[1] if top else '?'}  (页内命中 {len(decks)} 条)")
        results.append({"name": name, "slug": slug,
                        "num_decks": top[1] if top else None})
        (DATA / f"supp_{slug}.json").write_bytes(body)

    (DATA / "supplement_probe.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
