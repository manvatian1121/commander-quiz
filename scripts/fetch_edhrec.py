#!/usr/bin/env python3
"""抓取 EDHREC JSON 端点并保存。"""
from __future__ import annotations

import json
import pathlib
import urllib.error
import urllib.request



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
OUT = pathlib.Path(ROOT / "data")
OUT.mkdir(parents=True, exist_ok=True)

CANDIDATES = [
    "commanders/year.json",
    "commanders/month.json",
    "commanders/week.json",
    "commanders/past-year.json",
    "commanders/all.json",
    "top/year.json",
    "top/month.json",
]


def grab(path: str):
    url = "https://json.edhrec.com/pages/" + path
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read()
    except urllib.error.HTTPError as error:
        print(f"[HTTP {error.code}] {url}")
        return None
    except Exception as error:  # noqa: BLE001
        print(f"[ERR {type(error).__name__}] {url} :: {error}")
        return None
    name = path.replace("/", "_")
    (OUT / name).write_bytes(raw)
    print(f"[OK {len(raw)}B] {url} -> {name}")
    return json.loads(raw.decode("utf-8", "replace"))


def walk(node, depth=0, max_depth=4):
    """打印 JSON 骨架，帮判断哪里是排名列表。"""
    pad = "  " * depth
    if depth > max_depth:
        return
    if isinstance(node, dict):
        for key, value in list(node.items())[:14]:
            kind = type(value).__name__
            if isinstance(value, (dict, list)):
                size = len(value)
                print(f"{pad}{key}: {kind}({size})")
                walk(value, depth + 1, max_depth)
            else:
                text = str(value)
                print(f"{pad}{key}: {text[:70]}")
    elif isinstance(node, list) and node:
        print(f"{pad}[0] sample:")
        walk(node[0], depth + 1, max_depth)


if __name__ == "__main__":
    for candidate in CANDIDATES:
        payload = grab(candidate)
        if payload and candidate == "commanders/year.json":
            print("--- skeleton of commanders/year.json ---")
            walk(payload, max_depth=3)
