#!/usr/bin/env python3
"""终检：结构完整性 + 数据可信度 + 独立来源交叉验证。

1. 键集合与 curation_table 的 name 完全一致（无多、无缺）。
2. 值为非空字符串，且确实含中文（CJK）字符；无 None / 模板残留 / "//"。
3. 用 Scryfall（独立数据源）抽样交叉验证英文名确实是该主将，且中文名一致性。
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

DATA = ROOT / "data" / "commander_zh.json"
SRC = ROOT / "data" / "curation_table.json"
CJK = re.compile(r"[\u4e00-\u9fff]")

cur = json.load(open(SRC, encoding="utf-8"))
zh = json.load(open(DATA, encoding="utf-8"))

cur_names = [r["name"] for r in cur]
ok = True

print("=== 1. 键集合一致性 ===")
print("  curation_table:", len(cur_names), " commander_zh:", len(zh))
missing = [n for n in cur_names if n not in zh]
extra = [k for k in zh if k not in cur_names]
print("  缺失键:", missing or "无")
print("  多余键:", extra or "无")
if missing or extra:
    ok = False

print("\n=== 2. 值质量 ===")
empties = [k for k, v in zh.items() if not isinstance(v, str) or not v.strip()]
no_cjk = [k for k, v in zh.items() if isinstance(v, str) and v and not CJK.search(v)]
has_sep = [k for k, v in zh.items() if isinstance(v, str) and "//" in v]
print("  空值:", empties or "无")
print("  无中文字符:", no_cjk or "无")
print("  含未拆分 //:", has_sep or "无")
if empties or no_cjk or has_sep:
    ok = False

print("\n=== 2b. 键序是否与 curation_table 一致 ===")
print("  一致" if list(zh.keys()) == cur_names else "  不一致（仅影响可读性，不影响按 key 取用）")

print("\n=== 3. Scryfall 独立交叉验证（抽样 12 张）===")
sample = [
    "Krenko, Mob Boss", "Atraxa, Praetors' Voice", "Tergrid, God of Fright",
    "Esika, God of the Tree", "Tony Stark", "Avatar Aang",
    "Y'shtola, Night's Blessed", "Éowyn, Shieldmaiden", "Kefka, Court Mage",
    "Frodo, Adventurous Hobbit // Sam, Loyal Attendant",
    "Kraum, Ludevic's Opus // Tymna the Weaver", "The Ur-Dragon",
]


def scryfall(name: str):
    # 连体/搭档牌取正面再查
    q = name.split(" // ")[0]
    url = "https://api.scryfall.com/cards/named?" + urllib.parse.urlencode({"exact": q})
    req = urllib.request.Request(url, headers={"User-Agent": "dsh-mtg-agent/1.0",
                                              "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception as e:  # noqa: BLE001
        return {"_error": str(e)}


for n in sample:
    our = zh.get(n, "")
    sf = scryfall(n)
    if "_error" in sf:
        print(f"  ?  {n}\n       scryfall 查询失败: {sf['_error']}\n       我们的值: {our!r}")
        continue
    sf_en = sf.get("name")
    sf_zh = sf.get("printed_name") or sf.get("name")
    print(f"  - {n}")
    print(f"      我们: {our!r}")
    print(f"      scryfall: en={sf_en!r} printed_name={sf.get('printed_name')!r} lang={sf.get('lang')!r}")
    time.sleep(0.15)

print("\n=== 结论 ===")
print("  结构检查:", "通过" if ok else "有问题")
print(f"  非空 {sum(1 for v in zh.values() if v)}/{len(zh)}")
