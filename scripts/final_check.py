#!/usr/bin/env python3
"""核对两个搭档牌的最终值与原始值。"""
import json
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open(ROOT / "data" / "commander_zh.json", encoding="utf-8"))
rep = json.load(open(ROOT / "data" / "commander_zh_report.json", encoding="utf-8"))
raw = rep["raw_log"]

for k in ["Frodo, Adventurous Hobbit // Sam, Loyal Attendant",
          "Kraum, Ludevic's Opus // Tymna the Weaver"]:
    print("KEY:", k)
    print("   final:", repr(d[k]))
    print("   raw  :", json.dumps(raw.get(k), ensure_ascii=False))

print("\nstats:", rep["stats"])
print("regressions:", rep["regressions"])
print("keys:", len(d), "| non-empty:", sum(1 for v in d.values() if v))
print("any '//' in values:", any("//" in v for v in d.values()))
r = [e for e in rep["entries"] if e["zh"]]
print("entries with zh:", len(r), "| entries blank:", sum(1 for e in rep["entries"] if not e["zh"]))
