# -*- coding: utf-8 -*-
"""独立复检 + 全文打印（用于人工通读）。只读 descriptions_8.json 与素材。"""
import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

raw = (DATA / "descriptions_8.json").read_bytes()
print(f"文件大小 {len(raw)} 字节；BOM: {raw[:3] == b'\xef\xbb\xbf'}")
try:
    raw.decode("utf-8")
    print("UTF-8 解码：成功")
except UnicodeDecodeError as e:
    print("UTF-8 解码失败：", e)

data = json.loads(raw.decode("utf-8"))
commander_zh = json.loads((DATA / "commander_zh.json").read_text(encoding="utf-8"))

# 素材标题中文名 vs commander_zh.json
mismatch = []
for i in (1, 2, 3, 4):
    t = (DATA / f"writing_batch_new_{i}.md").read_text(encoding="utf-8")
    for en, zh in re.findall(r"^## (.+?) ｜ (.+?)\s*$", t, re.M):
        official = commander_zh.get(en.strip())
        if official and official != zh.strip():
            mismatch.append((en.strip(), zh.strip(), official))
print("\n素材标题中文名 与 commander_zh.json 不一致的条目：", mismatch or "无")

print(f"\n{'=' * 30} 全文（{len(data)} 条） {'=' * 30}")
for n, (k, e) in enumerate(data.items(), 1):
    print(f"\n[{n}] {k}")
    print(f"    tagline: {e['tagline']}")
    print(f"    intro  : {e['intro']}")
    print(f"    build  : {e['build']}")
