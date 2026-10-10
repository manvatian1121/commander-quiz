# -*- coding: utf-8 -*-
"""查中文术语：终结指示物 / 血滴 / menace 等（结果写文件，避免控制台编码问题）。"""
import json
import pathlib
import sys
import urllib.parse
import urllib.request



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(ROOT / "data" / "_term_probe.txt")
BASE = "https://mtgch.com/api/v1"


def fetch(path, params=None, timeout=30):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"User-Agent": "dsh-mtg-agent/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


lines = []


def log(*a):
    lines.append(" ".join(str(x) for x in a))


# 1) 中文规则书里搜关键词
for q in ["终结指示物", "指示物", "血滴", "威吓"]:
    try:
        r = fetch("/blog/cr-search/", {"q": q})
        res = r.get("results", []) if isinstance(r, dict) else []
        log(f"=== cr-search {q!r}: {len(res)} 条")
        for item in res[:6]:
            txt = json.dumps(item, ensure_ascii=False)
            log("   ", txt[:600])
    except Exception as exc:
        log(f"=== cr-search {q!r} 失败: {exc}")

# 2) 卡牌详情（含中文牌面）
for name in ["Kastral, the Windcrested", "Shilgengar, Sire of Famine", "Noctis, Prince of Lucis",
             "Alexios, Deimos of Kosmos"]:
    try:
        r = fetch("/autocomplete/", {"q": name, "view": "full"})
        items = r.get("items", []) if isinstance(r, dict) else []
        log(f"=== auto {name!r}: {len(items)} 条")
        for it in items[:2]:
            log("   ", json.dumps(it, ensure_ascii=False)[:1500])
    except Exception as exc:
        log(f"=== auto {name!r} 失败: {exc}")

OUT.write_text("\n".join(lines), encoding="utf-8")
print("done", len(lines))
