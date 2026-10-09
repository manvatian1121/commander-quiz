#!/usr/bin/env python3
"""为某一批素材里的搭配牌取官方中文名。

只做可判定的确定性匹配，匹配不上就留空，绝不猜。
用法：python fetch_card_zh_batch.py 2
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
BASE = "https://mtgch.com/api/v1"


def auto(query: str):
    url = BASE + "/autocomplete/?" + urllib.parse.urlencode({"q": query, "view": "name"})
    request = urllib.request.Request(
        url, headers={"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.loads(response.read().decode("utf-8", "replace"))


def pick(items: list[dict], query: str) -> str | None:
    for item in items:
        name = item.get("name") or ""
        zh = item.get("display_name") or item.get("translated_name") or ""
        if not zh:
            continue
        if name == query:
            return zh.split(" // ")[0].strip()
        if name.startswith(query + " //"):
            return zh.split(" // ")[0].strip()
    return None


def collect(batch: int) -> tuple[list[str], list[str]]:
    """从素材 md 抽出 (主将名, 搭配牌名)。"""
    path = DATA / f"writing_batch_{batch}.md"
    commanders: list[str] = []
    cards: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## ") and "｜" in line:
            commanders.append(line[3:].split("｜")[0].strip())
        m = re.match(r"^\s+(?:\d+\.|[-*])\s+(.+?)（", line)
        if m:
            cards.append(m.group(1).strip())
    return commanders, cards


def lookup(name: str) -> tuple[str, str]:
    for label, query in (("原名", name), ("逗号前", name.split(",")[0].strip())):
        if not query:
            continue
        try:
            items = (auto(query) or {}).get("items") or []
        except Exception as exc:  # noqa: BLE001
            print(f"    ! {name}: {exc}")
            time.sleep(1.0)
            continue
        if label == "原名":
            hit = pick(items, name)
        else:
            hit = None
            for item in items:
                candidate = item.get("name") or ""
                zh = item.get("display_name") or item.get("translated_name") or ""
                if zh and (candidate == query or candidate.startswith(query + ",")):
                    hit = zh.split(" // ")[0].strip()
                    break
        if hit:
            return hit, label
        time.sleep(0.15)
    return "", "未命中"


def main() -> int:
    batch = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    commanders, cards = collect(batch)
    names = sorted(set(cards))
    print(f"批次 {batch}：{len(commanders)} 位主将，{len(names)} 张去重搭配牌")

    out = DATA / f"card_zh_b{batch}.json"
    cache: dict[str, str] = {}
    if out.exists():
        cache = json.loads(out.read_text(encoding="utf-8"))

    methods = {"缓存": sum(1 for n in names if cache.get(n))}
    result: dict[str, str] = {}
    for index, name in enumerate(names, 1):
        if cache.get(name):
            result[name] = cache[name]
            continue
        zh, how = lookup(name)
        result[name] = zh
        methods[how] = methods.get(how, 0) + 1
        if index % 50 == 0:
            print(f"  ...{index}/{len(names)}  留空 {sum(1 for v in result.values() if not v)}")
            out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        time.sleep(0.15)

    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    blanks = sorted(n for n, v in result.items() if not v)
    print(f"\n✓ {out.name} 共 {len(result)} 张；方式 {methods}")
    print(f"⚠ 留空 {len(blanks)} 张：")
    for name in blanks:
        print(f"  - {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
