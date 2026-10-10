"""补取 11 个未命中的中文名（改写查询词），并抽样打印已有映射供人工核对。"""
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

RETRY = {
    "Brazen Borrower": ["Brazen Borrower", "Borrower"],
    "Norman Osborn": ["Norman Osborn", "Osborn", "Norman"],
    "Ojer Kaslem, Deepest Growth": ["Ojer Kaslem", "Kaslem"],
    "Summon: Bahamut": ["Bahamut"],
    "Summon: Fenrir": ["Fenrir"],
    "Summon: Knights of Round": ["Knights of Round"],
    "Summon: Primal Odin": ["Primal Odin"],
    "Summon: Titan": ["Summon Titan", "Titan"],
    "Summon: Yojimbo": ["Yojimbo"],
    "Tergrid, God of Fright": ["Tergrid", "God of Fright"],
    "Terra, Magical Adept": ["Terra, Magical Adept", "Magical Adept"],
}


def auto(q):
    url = BASE + "/autocomplete/?" + urllib.parse.urlencode({"q": q, "view": "name"})
    req = urllib.request.Request(url, headers={"User-Agent": "dsh-mtg-agent/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


for name, queries in RETRY.items():
    found = None
    for q in queries:
        try:
            items = auto(q).get("items", [])
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {name} <- q={q!r}: {exc}")
            time.sleep(0.5)
            continue
        for it in items:
            if str(it.get("name", "")).strip().lower() == name.strip().lower():
                found = it
                break
        print(f"  {name} <- q={q!r}: {[i.get('name') for i in items][:6]}")
        if found:
            break
        time.sleep(0.15)
    if found:
        result[name] = {"zh": (found.get("translated_name") or "").strip(), "name": found.get("name")}
        print(f"  => {name} = {found.get('translated_name')}")
    time.sleep(0.15)

PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

print("\n仍未命中：", [k for k, v in result.items() if not v["zh"]])
print("\n抽样核对（每 12 个抽 1 个）：")
for i, (en, v) in enumerate(sorted(result.items())):
    if i % 12 == 0:
        print(f"   {en:38s} = {v['zh']}")
