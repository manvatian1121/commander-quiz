#!/usr/bin/env python3
"""为 writing_batch_1 素材里出现的所有牌取官方中文名。只做确定性匹配，匹配不上留空。"""
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
SRC = DATA / "writing_batch_1.md"
OUT = DATA / "card_zh_batch1.json"
BASE = "https://mtgch.com/api/v1"


def collect_names(text: str) -> list[str]:
    names: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        m = re.match(r"^(?:\d+\.|[-*])\s+(.+?)\uff08", s)
        if not m:
            continue
        name = m.group(1).strip()
        if name.startswith("**") or name.startswith("("):
            continue
        if name not in names:
            names.append(name)
    # 主将名（## 标题）也一并查
    for m in re.finditer(r"^## (.+?) \uff5c", text, re.M):
        name = m.group(1).strip()
        if name not in names:
            names.append(name)
    return names


def auto(query: str):
    url = BASE + "/autocomplete/?" + urllib.parse.urlencode({"q": query, "view": "name"})
    req = urllib.request.Request(
        url, headers={"User-Agent": "dsh-mtg-agent/1.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def pick(items: list[dict], query: str) -> str | None:
    for item in items:
        name = item.get("name") or ""
        zh = item.get("translated_name") or item.get("display_name") or ""
        if not zh:
            continue
        if name == query:
            return zh.split(" // ")[0].strip()
        if name.startswith(query + " //"):
            return zh.split(" // ")[0].strip()
    return None


def lookup(name: str) -> tuple[str, str]:
    for label, query in (("原名", name), ("逗号前", name.split(",")[0].strip())):
        if not query:
            continue
        try:
            payload = auto(query)
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {name}: {exc}")
            time.sleep(1.0)
            continue
        items = payload.get("items") or []
        if label == "原名":
            hit = pick(items, name)
        else:
            hit = None
            for item in items:
                cand = item.get("name") or ""
                zh = item.get("translated_name") or item.get("display_name") or ""
                if zh and (cand == query or cand.startswith(query + ",")):
                    hit = zh.split(" // ")[0].strip()
                    break
        if hit:
            return hit, label
        time.sleep(0.25)
    return "", "未命中"


def main() -> int:
    names = collect_names(SRC.read_text(encoding="utf-8"))
    print(f"待查 {len(names)} 个牌名")
    result: dict[str, str] = {}
    methods: dict[str, str] = {}
    for i, name in enumerate(names, 1):
        zh, how = lookup(name)
        result[name] = zh
        methods[name] = how
        if i % 50 == 0:
            print(f"  ...{i}/{len(names)}")
        time.sleep(0.3)
    # 合并已有结果
    if OUT.exists():
        old = json.loads(OUT.read_text(encoding="utf-8"))
        old.update(result)
        result = old
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    blanks = sorted(n for n, v in result.items() if not v)
    print(f"完成，写入 {OUT}；未命中 {len(blanks)}")
    for n in blanks:
        print("  -", n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
