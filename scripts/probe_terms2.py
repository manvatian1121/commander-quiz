# -*- coding: utf-8 -*-
"""查中文术语第二批：menace / finality counter / 中文牌面。"""
import json
import pathlib
import urllib.parse
import urllib.request



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(ROOT / "data" / "_term_probe2.txt")
BASE = "https://mtgch.com/api/v1"


def fetch(path, params=None, timeout=30):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"User-Agent": "dsh-mtg-agent/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


lines = []


def log(*a):
    lines.append(" ".join(str(x) for x in a))


for q in ["finality", "menace", "威慑", "终结", "终结指示物 counter"]:
    try:
        r = fetch("/blog/cr-search/", {"q": q})
        res = r.get("results", []) if isinstance(r, dict) else []
        log(f"=== cr-search {q!r}: {len(res)} 条")
        for item in res[:4]:
            log("   ", json.dumps(item, ensure_ascii=False)[:700])
    except Exception as exc:
        log(f"=== cr-search {q!r} 失败: {exc}")

# 试几种单卡详情端点
for path, params in [
    ("/cards/ebf68793-22a2-4a59-9d37-6791584edca1", None),
    ("/card/ebf68793-22a2-4a59-9d37-6791584edca1", None),
    ("/cards/", {"id": "ebf68793-22a2-4a59-9d37-6791584edca1"}),
]:
    try:
        r = fetch(path, params)
        log(f"=== {path} {params}: ok")
        log("   ", json.dumps(r, ensure_ascii=False)[:1200])
    except Exception as exc:
        log(f"=== {path} {params} 失败: {exc}")

OUT.write_text("\n".join(lines), encoding="utf-8")
print("done", len(lines))
