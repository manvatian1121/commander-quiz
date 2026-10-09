"""第三轮：处理 API 里以「A // B」形式收录的牌，补全剩余中文名。"""
import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

BASE = "https://mtgch.com/api/v1"
DATA = pathlib.Path(ROOT / "data")
PATH = DATA / "_card_zh_3.json"
result = json.loads(PATH.read_text(encoding="utf-8"))


def auto(q):
    url = BASE + "/autocomplete/?" + urllib.parse.urlencode({"q": q, "view": "name"})
    req = urllib.request.Request(url, headers={"User-Agent": "dsh-mtg-agent/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


todo = {
    "Brazen Borrower": ["Brazen Borrower"],
    "Norman Osborn": ["Norman Osborn"],
    "Ojer Kaslem, Deepest Growth": ["Ojer Kaslem, Deepest Growth"],
    "Summon: Titan": ["Summon:", "Summon"],
    "Tergrid, God of Fright": ["Tergrid, God of Fright"],
    "Terra, Magical Adept": ["Terra, Magical Adept"],
}

for name, queries in todo.items():
    hit = None
    for q in queries:
        try:
            items = auto(q).get("items", [])
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {name} q={q!r}: {exc}")
            continue
        for it in items:
            n = str(it.get("name", "")).strip()
            if n.lower() == name.lower() or n.lower().startswith(name.lower() + " //"):
                hit = it
                break
        if not hit:
            print(f"  {name} q={q!r} 候选：{[(i.get('name'), i.get('translated_name')) for i in items][:8]}")
        if hit:
            break
        time.sleep(0.2)
    if hit:
        result[name] = {"zh": (hit.get("translated_name") or "").strip(), "name": hit.get("name")}
        print(f"  => {name} = {hit.get('translated_name')}  ({hit.get('name')})")
    time.sleep(0.2)

PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print("\n最终仍未命中：", [k for k, v in result.items() if not v["zh"]])
