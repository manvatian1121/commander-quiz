# -*- coding: utf-8 -*-
import importlib.util
import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(SCRIPT_DIR)


def count(s):
    return sum(1 for ch in s.replace("\n", "") if not ch.isspace())


for i in range(1, 9):
    p = BASE / f"_desc_part{i}.py"
    spec = importlib.util.spec_from_file_location(f"_desc_part{i}", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print(f"--- part{i}: {len(mod.PART)} 条")
    for k, v in mod.PART.items():
        print(f"    {count(v['tagline']):>2}/{count(v['intro']):>3}/{count(v['build']):>3}  {k}")

D = pathlib.Path(ROOT / "data" / "descriptions_1.json")
data = json.loads(D.read_text(encoding="utf-8"))
print("JSON:", len(data))
print("JSON Hakbal:", count(data["Hakbal of the Surging Soul"]["build"]))
print(repr(data["Hakbal of the Surging Soul"]["build"][:60]))
