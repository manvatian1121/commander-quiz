# -*- coding: utf-8 -*-
"""把素材索引打印成便于写作的清单：主将 → 搭配牌（中文（English）可用字符串）。"""
import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
IDX = json.loads(pathlib.Path(
    SCRIPT_DIR / "_material_index_8.json").read_text(encoding="utf-8"))

for en, e in IDX.items():
    zh = e["zh"] or e["zh_material"]
    print(f"\n### {en} ｜ {zh}  [{e['file']}]")
    for c, cz in e["cards"].items():
        print(f"    {cz or '(无中文名)':<18} （{c}）")
