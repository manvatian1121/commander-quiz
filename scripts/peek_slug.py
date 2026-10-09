#!/usr/bin/env python3
"""查看某位主将的档案 slug 与 EDHREC 页面可达性。"""
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

name = sys.argv[1] if len(sys.argv) > 1 else "Kraum, Ludevic's Opus // Tymna the Weaver"
profiles = json.loads((DATA / "commander_profiles.json").read_text(encoding="utf-8"))
pool = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
card = next((c for c in pool["commanders"] if c["en"] == name), None)

print(f"主将：{name}")
print(f"  档案 slug = {profiles.get(name, {}).get('slug')!r}")
print(f"  套牌数 = {profiles.get(name, {}).get('num_decks')}")
if card:
    print(f"  常见强度 Bracket = {card['bracket']}  分布 {card['bracket_mix']}")
    print(f"  咸度 {card['salt']}  难度 {card['complexity']}  造价 {card['budget']}")

for slug in [profiles.get(name, {}).get("slug"),
             "kraum-ludevics-opus-tymna-the-weaver",
             "kraum-ludevic-s-opus-tymna-the-weaver"]:
    if not slug:
        continue
    url = f"https://json.edhrec.com/pages/commanders/{slug}.json"
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            payload = json.loads(response.read().decode("utf-8", "replace"))
        jd = (payload.get("container") or {}).get("json_dict") or {}
        lists = jd.get("cardlists") or []
        print(f"  [{slug}] 可达，cardlists {len(lists)} 组")
    except urllib.error.HTTPError as error:
        print(f"  [{slug}] HTTP {error.code}")
    except Exception as error:  # noqa: BLE001
        print(f"  [{slug}] {type(error).__name__}")
