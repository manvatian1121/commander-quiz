"""从 writing_batch_3.md 抽取 36 位主将与素材内所有牌名，生成素材索引 JSON。"""
import json
import pathlib
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

SRC = pathlib.Path(ROOT / "data" / "writing_batch_3.md")
OUT = pathlib.Path(ROOT / "data" / "_material_3_index.json")

text = SRC.read_text(encoding="utf-8")
body = text.split("# 素材：36 位主将", 1)[1]

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
    oracle = block.split("- 完整牌面：", 1)[1].split("###", 1)[0]
    oracle = oracle.split("- **协同度最高的牌**")[0].strip()

    # 牌名：协同清单 "  1. Name（..." ；出场清单 "  - Name（..."
    synergy = re.findall(r"^\s+\d+\.\s+(.+?)（", block, re.M)
    top = re.findall(r"^\s+-\s+(.+?)（", block, re.M)

    commanders.append(
        {
            "en": en,
            "zh": zh,
            "meta": meta,
            "oracle": oracle,
            "synergy": synergy,
            "top": top,
            "whitelist": sorted(set(synergy) | set(top) | {en}),
        }
    )

OUT.write_text(json.dumps(commanders, ensure_ascii=False, indent=2), encoding="utf-8")

all_names = []
for c in commanders:
    all_names.extend(c["whitelist"])
all_names = sorted(set(all_names))
pathlib.Path(ROOT / "data" / "_all_card_names_3.json").write_text(
    json.dumps(all_names, ensure_ascii=False, indent=2), encoding="utf-8"
)

print(f"主将数：{len(commanders)}")
print(f"素材内唯一牌名数（含主将）：{len(all_names)}")
for c in commanders:
    print(f"  {c['en']} ｜ {c['zh']} ｜ 协同{len(c['synergy'])} 出场{len(c['top'])}")
