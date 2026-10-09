# -*- coding: utf-8 -*-
"""把分段写的文案合并成 descriptions_1.json。"""
import importlib.util
import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

BASE = pathlib.Path(SCRIPT_DIR)
OUT = pathlib.Path(ROOT / "data" / "descriptions_1.json")
SRC = pathlib.Path(ROOT / "data" / "writing_batch_1.md")

parts = []
for i in range(1, 9):
    p = BASE / f"_desc_part{i}.py"
    if not p.exists():
        continue
    spec = importlib.util.spec_from_file_location(f"_desc_part{i}", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    parts.append(mod.PART)

merged: dict = {}
for part in parts:
    for k, v in part.items():
        merged[k] = v

text = SRC.read_text(encoding="utf-8")
commanders = re.findall(r"^## (.+?) ｜", text, re.M)
ordered = {c: merged[c] for c in commanders if c in merged}
for c in commanders:
    if c not in merged:
        print("缺失：", c)

OUT.write_text(json.dumps(ordered, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"写入 {OUT}：{len(ordered)} 条 / 期望 {len(commanders)}")
