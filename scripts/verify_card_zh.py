#!/usr/bin/env python3
"""独立复核中文牌名：搜索该牌的任意中文印刷版本，与 mtgch 的结果交叉验证。"""
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
SAMPLE = 40


def fetch(url: str):
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as error:
        return {"__err__": error.code}


def zh_printing(name: str):
    """找该牌任意一个中文印刷版本，返回 printed_name。"""
    query = f'!"{name}" lang:zhs'
    url = ("https://api.scryfall.com/cards/search?unique=cards&q="
           + urllib.parse.quote(query))
    payload = fetch(url)
    if "__err__" in payload:
        return None, payload["__err__"]
    for card in payload.get("data", []):
        printed = card.get("printed_name")
        if printed:
            return printed, None
    return None, "无中文印刷记录"


def main() -> None:
    zh = json.loads((DATA / "card_zh.json").read_text(encoding="utf-8"))
    named = [(n, v) for n, v in zh.items() if v]
    step = max(1, len(named) // SAMPLE)
    sample = named[::step][:SAMPLE]

    agree, mismatch, unavailable = 0, [], 0
    for name, mine in sample:
        official, error = zh_printing(name)
        if error:
            unavailable += 1
            time.sleep(0.15)
            continue
        if official == mine:
            agree += 1
        else:
            mismatch.append((name, mine, official))
            print(f"  ✗ {name}: 我方「{mine}」 vs Scryfall「{official}」")
        time.sleep(0.15)

    comparable = agree + len(mismatch)
    print(f"抽样 {len(sample)} 张：可比对 {comparable}，一致 {agree}，冲突 {len(mismatch)}，"
          f"无中文印刷 {unavailable}")
    if comparable:
        print(f"一致率 {agree / comparable * 100:.1f}%")
    for name, mine, official in mismatch:
        print(f"  冲突 {name}: 「{mine}」 vs 「{official}」")
    return 0 if not mismatch else 1


if __name__ == "__main__":
    raise SystemExit(main())
