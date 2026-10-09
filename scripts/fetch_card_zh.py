#!/usr/bin/env python3
"""为搭配牌取官方中文名。规则：只做可判定的确定性匹配，匹配不上就留空，绝不猜。"""
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
BASE = "https://mtgch.com/api/v1"


def auto(query: str):
    """调用 mtgch autocomplete。不传 view → 返回 display_name（中文名）。"""
    url = BASE + "/autocomplete/?" + urllib.parse.urlencode({"q": query, "view": "name"})
    request = urllib.request.Request(
        url, headers={"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.loads(response.read().decode("utf-8", "replace"))


def pick(items: list[dict], query: str) -> str | None:
    """只接受确定性匹配：精确同名，或「<查询名> // 背面」。"""
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


def lookup(name: str) -> tuple[str, str]:
    """返回 (中文名, 匹配方式)。匹配不上返回 ('', '未命中')。"""
    for label, query in (("原名", name), ("逗号前", name.split(",")[0].strip())):
        if not query:
            continue
        try:
            payload = auto(query)
        except Exception:  # noqa: BLE001
            time.sleep(1.0)
            continue
        items = payload.get("items") or []
        if label == "原名":
            hit = pick(items, name)
        else:
            # 退回逗号前主体时，要求命中项 name 恰为主体或以「主体,」开头
            hit = None
            for item in items:
                candidate = item.get("name") or ""
                zh = item.get("display_name") or item.get("translated_name") or ""
                if zh and (candidate == query or candidate.startswith(query + ",")):
                    hit = zh.split(" // ")[0].strip()
                    break
        if hit:
            return hit, label
        time.sleep(0.25)
    return "", "未命中"


def main() -> int:
    display = json.loads((DATA / "card_display.json").read_text(encoding="utf-8"))
    zh_path = DATA / "card_zh.json"
    existing = json.loads(zh_path.read_text(encoding="utf-8")) if zh_path.exists() else {}

    names = sorted({n for entry in display.values()
                    for n in (entry["synergy"] + entry["popular"])})
    todo = [n for n in names if n not in existing]
    print(f"展示牌共 {len(names)} 张，已查过 {len(names) - len(todo)} 张，待查 {len(todo)} 张")

    result: dict[str, str] = dict(existing)
    methods: dict[str, str] = {}
    for index, name in enumerate(todo, 1):
        zh, how = lookup(name)
        result[name] = zh
        methods[name] = how
        if index % 100 == 0:
            missing = sum(1 for v in methods.values() if v == "未命中")
            print(f"  ...{index}/{len(todo)}  本轮留空 {missing}", flush=True)
        time.sleep(0.28)

    zh_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    blanks = sorted(n for n, v in result.items() if not v)
    from collections import Counter
    print(f"\n✓ 累计 {len(result)} 张，本轮匹配方式：{dict(Counter(methods.values()))}")
    print(f"⚠ 留空 {len(blanks)} 张：")
    for name in blanks:
        print(f"  - {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
