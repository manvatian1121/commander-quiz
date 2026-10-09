# -*- coding: utf-8 -*-
"""检查本轮 27 位主将是否已在既有 descriptions_1~7 中出现过；顺带看「引擎」上下文。"""
import io
import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
IDX = json.loads(pathlib.Path(
    SCRIPT_DIR / "_material_index_8.json").read_text(encoding="utf-8"))
mine = list(IDX)

for i in range(1, 8):
    d = json.loads((DATA / f"descriptions_{i}.json").read_text(encoding="utf-8"))
    dup = [k for k in mine if k in d]
    if dup:
        print(f"descriptions_{i}.json 与本轮重复：{dup}")
    for k, e in d.items():
        for f in ("tagline", "intro", "build"):
            v = e.get(f) or ""
            if "引擎" in v:
                print(f"  [引擎] descriptions_{i}.json / {k} / {f}: …{v[max(0,v.find('引擎')-25):v.find('引擎')+25]}…")
print("\n本轮 27 位在全库中的重复检查完成")
