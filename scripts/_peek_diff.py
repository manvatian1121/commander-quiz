# -*- coding: utf-8 -*-
"""比较 rebuild 结果与打补丁后的版本是否一致。"""
import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path(ROOT / "data")
a = json.loads((D / "descriptions_1.json").read_text(encoding="utf-8"))
b = json.loads((D / "_desc_backup.json").read_text(encoding="utf-8"))
diff = [k for k in b if a.get(k) != b.get(k)]
print("差异条目：", diff or "无（rebuild 与补丁版一致）")
for k in diff:
    for f in ("tagline", "intro", "build"):
        if a[k][f] != b[k][f]:
            print(f"  {k}/{f}\n    A: {a[k][f]}\n    B: {b[k][f]}")
