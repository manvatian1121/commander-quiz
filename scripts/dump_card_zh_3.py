"""输出「英文 | 中文」对照清单（供写作时查名），并再试一次 Summon: Titan。"""
import json
import pathlib
import sys
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


if not result.get("Summon: Titan", {}).get("zh"):
    for q in ["Summon Ti", "Summon T", "Titan"]:
        try:
            items = auto(q).get("items", [])
        except Exception as exc:  # noqa: BLE001
            print("  !", q, exc)
            continue
        hit = [i for i in items if str(i.get("name", "")).startswith("Summon")]
        print(f"  q={q!r} -> {[(i.get('name'), i.get('translated_name')) for i in hit][:10]}")
        for i in items:
            if str(i.get("name", "")).strip().lower() == "summon: titan":
                result["Summon: Titan"] = {"zh": (i.get("translated_name") or "").strip(),
                                           "name": i.get("name")}
                print("  => Summon: Titan =", i.get("translated_name"))
                break
        if result.get("Summon: Titan", {}).get("zh"):
            break

PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

lines = [f"{en} | {v['zh']}" for en, v in sorted(result.items()) if v["zh"]]
(DATA / "_card_zh_3.txt").write_text("\n".join(lines), encoding="utf-8")
print(f"\n对照表已写出，命中 {len(lines)}/{len(result)}")
print("仍未命中：", [k for k, v in result.items() if not v["zh"]])
