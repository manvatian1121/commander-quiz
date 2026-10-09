# -*- coding: utf-8 -*-
"""查中文术语第三批：prowess / defender / discover / offspring / station / ward。"""
import json
import pathlib
import urllib.parse
import urllib.request

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

OUT = pathlib.Path(ROOT / "data" / "_term_probe3.txt")
BASE = "https://mtgch.com/api/v1"


def fetch(path, params=None, timeout=30):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"User-Agent": "dsh-mtg-agent/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


lines = []
for q in ["prowess", "defender", "discover", "offspring", "station", "ward"]:
    try:
        r = fetch("/blog/cr-search/", {"q": q})
        res = r.get("results", []) if isinstance(r, dict) else []
        lines.append(f"=== {q!r}: {len(res)} 条")
        for item in res[:3]:
            txt = json.dumps(item, ensure_ascii=False)
            # 只保留中英对照片段里含该词的部分
            for snip in (item.get("snippets") or [])[:2]:
                lines.append("    " + snip.replace("\n", " ")[:420])
    except Exception as exc:
        lines.append(f"=== {q!r} 失败: {exc}")

OUT.write_text("\n".join(lines), encoding="utf-8")
print("done")
