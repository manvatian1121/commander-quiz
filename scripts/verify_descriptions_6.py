# -*- coding: utf-8 -*-
"""独立复核（不复用 draft 脚本的索引）：直接从素材 md 重新抽主将名与牌名清单，
再与 descriptions_6.json 对照。"""
import json
import pathlib
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

DATA = pathlib.Path(ROOT / "data")
md = (DATA / "writing_batch_new_3.md").read_text(encoding="utf-8")
body = md.split("# 素材：30 位主将", 1)[1]

blocks = re.split(r"^## ", body, flags=re.M)[1:]
commanders = []
for b in blocks:
    lines = b.splitlines()
    head = lines[0]
    en = head.split("｜")[0].strip()
    zh = head.split("｜")[1].strip() if "｜" in head else ""
    cards = re.findall(r"^\s+(?:\d+\.|-)\s+(.+?)（", b, re.M)
    commanders.append((en, zh, [c.strip() for c in cards]))

data = json.loads((DATA / "descriptions_6.json").read_text(encoding="utf-8"))

print(f"素材主将数：{len(commanders)}   JSON 条目数：{len(data)}")
print("key 顺序与素材一致：", [c[0] for c in commanders] == list(data))

PAIR = re.compile(r"([^（）()]{1,12})[（(]([A-Za-z][^）)]*)[）)]")
total_mentions = 0
bad = []
dupe_zh = []
for en, zh, cards in commanders:
    own = set(cards) | {en}
    entry = data[en]
    blob = " ".join(entry[f] for f in ("tagline", "intro", "build"))
    for cn, name in PAIR.findall(blob):
        total_mentions += 1
        if name not in own:
            bad.append((en, name))
    # 中文名一致性：同一英文名在同一主将条里应只有一种中文写法
    seen = {}
    for cn, name in PAIR.findall(blob):
        if name in seen and seen[name] != cn:
            dupe_zh.append((en, name, seen[name], cn))
        seen[name] = cn

print(f"牌名提及总数：{total_mentions}")
print(f"清单外的牌名：{len(bad)} {bad if bad else '✓'}")
print(f"同一牌名中文写法冲突：{len(dupe_zh)} {dupe_zh if dupe_zh else '✓'}")

# 中文名字典反查
zhmap = json.loads((DATA / "_card_zh_new3.json").read_text(encoding="utf-8"))
mismatch = []
for en, zh, cards in commanders:
    entry = data[en]
    blob = " ".join(entry[f] for f in ("tagline", "intro", "build"))
    for cn, name in PAIR.findall(blob):
        official = (zhmap.get(name) or {}).get("zh")
        if official and not cn.endswith(official):
            mismatch.append((en, name, cn, official))
print(f"与 API 官方中文名不一致：{len(mismatch)} {mismatch if mismatch else '✓'}")

# 编码确认
raw = (DATA / "descriptions_6.json").read_bytes()
print(f"文件字节数：{len(raw)}  BOM：{raw[:3] == b'\xef\xbb\xbf'}  可解析：✓")
