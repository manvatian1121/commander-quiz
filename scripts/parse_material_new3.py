"""从 writing_batch_new_3.md 抽取 30 位主将与素材内所有牌名，生成素材索引 JSON。
同时统计牌名中文名覆盖率（复用项目内已有的 zh 词典）。
"""
import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

DATA = pathlib.Path(ROOT / "data")
SRC = DATA / "writing_batch_new_3.md"
OUT = DATA / "_material_new3_index.json"
OUT_NAMES = DATA / "_all_card_names_new3.json"

text = SRC.read_text(encoding="utf-8")
body = text.split("# 素材：30 位主将", 1)[1]

commander_re = re.compile(r"^## (.+?)\s*｜\s*(.+?)\s*$", re.M)
hits = list(commander_re.finditer(body))

commanders = []
for i, m in enumerate(hits):
    start = m.start()
    end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
    block = body[start:end]
    en = m.group(1).strip()
    zh = m.group(2).strip()

    lines = [ln.rstrip() for ln in block.splitlines()]
    meta = {}
    for ln in lines[:10]:
        if ln.startswith("- 颜色"):
            meta["colors"] = ln.split("｜")[0].replace("- 颜色", "").strip()
        if ln.startswith("- 流行度"):
            meta["popularity"] = ln.replace("- 流行度：", "").strip()
        if ln.startswith("- 常见强度档"):
            meta["tier"] = ln.replace("- 常见强度档", "").strip()
        if ln.startswith("- 社区标签"):
            meta["tags"] = ln.split("：", 1)[1].strip()
    oracle = block.split("- 完整牌面：", 1)[1]
    oracle = oracle.split("- **协同度最高的牌**")[0].strip()

    synergy = [s.strip() for s in re.findall(r"^\s+\d+\.\s+(.+?)（", block, re.M)]
    top = [s.strip() for s in re.findall(r"^\s+-\s+(.+?)（", block, re.M)]

    commanders.append({
        "en": en, "zh": zh, "meta": meta, "oracle": oracle,
        "synergy": synergy, "top": top,
        "whitelist": sorted(set(synergy) | set(top) | {en}),
    })

OUT.write_text(json.dumps(commanders, ensure_ascii=False, indent=2), encoding="utf-8")

all_names = sorted({n for c in commanders for n in c["whitelist"]})
OUT_NAMES.write_text(json.dumps(all_names, ensure_ascii=False, indent=2), encoding="utf-8")

# ---- 中文名覆盖 ----
zh_map = {}
for f in ("card_zh.json", "card_zh_b2.json", "card_zh_batch1.json"):
    p = DATA / f
    if not p.exists():
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    for k, v in d.items():
        if isinstance(v, dict):
            v = v.get("zh") or ""
        if isinstance(v, str) and v.strip():
            zh_map.setdefault(k, v.strip())
p = DATA / "_card_zh_3.json"
if p.exists():
    d = json.loads(p.read_text(encoding="utf-8"))
    for k, v in d.items():
        zh = (v or {}).get("zh") if isinstance(v, dict) else v
        if zh and str(zh).strip():
            zh_map.setdefault(k, str(zh).strip())

print(f"主将数：{len(commanders)}")
print(f"素材内唯一牌名数（含主将）：{len(all_names)}")
print(f"已有中文名词典条目：{len(zh_map)}")
missing = [n for n in all_names if n not in zh_map]
print(f"缺中文名：{len(missing)}")
for c in commanders:
    miss = [n for n in c["whitelist"] if n not in zh_map]
    print(f"  {c['en']} ｜ {c['zh']} ｜ 协同{len(c['synergy'])} 出场{len(c['top'])} ｜ 缺{len(miss)}: {miss}")
