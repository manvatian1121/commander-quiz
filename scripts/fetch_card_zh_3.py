"""批量取素材内 345 个牌名的官方中文名（mtgch /autocomplete 精确匹配）。

匹配不上即留空，绝不猜测。结果写 _card_zh_3.json。
"""
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

BASE = "https://mtgch.com/api/v1"
DATA = pathlib.Path(ROOT / "data")
NAMES = json.loads((DATA / "_all_card_names_3.json").read_text(encoding="utf-8"))
OUT = DATA / "_card_zh_3.json"


def fetch(path: str, params: dict, timeout: int = 30):
    url = BASE + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "dsh-mtg-agent/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


result: dict[str, dict] = {}
misses: list[str] = []
errors: list[str] = []

for i, name in enumerate(NAMES, 1):
    got = None
    for attempt in range(3):
        try:
            payload = fetch("/autocomplete/", {"q": name, "view": "name"})
            items = payload.get("items", []) if isinstance(payload, dict) else []
            for it in items:
                if str(it.get("name", "")).strip().lower() == name.strip().lower():
                    got = it
                    break
            break
        except Exception as exc:  # noqa: BLE001
            if attempt == 2:
                errors.append(f"{name}: {exc}")
            time.sleep(0.8 * (attempt + 1))

    if got:
        result[name] = {
            "zh": (got.get("translated_name") or "").strip(),
            "name": got.get("name"),
        }
    else:
        result[name] = {"zh": "", "name": None}
        misses.append(name)

    if i % 25 == 0:
        print(f"  ... {i}/{len(NAMES)}  未命中 {len(misses)}", flush=True)
    time.sleep(0.1)

OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"完成：总 {len(NAMES)}，命中 {sum(1 for v in result.values() if v['zh'])}，"
      f"未命中 {len(misses)}，请求错误 {len(errors)}")
print("未命中清单：")
for m in misses:
    print("   -", m)
if errors:
    print("错误：")
    for e in errors:
        print("   !", e)
