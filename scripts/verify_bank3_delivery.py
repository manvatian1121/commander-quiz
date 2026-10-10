# -*- coding: utf-8 -*-
"""交付前最终核对：结构、字段、编码、题号范围、每题选项数。"""
import json
import sys
from pathlib import Path



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

P = Path(ROOT / "data" / "bank3.json")
raw = P.read_bytes()
text = raw.decode("utf-8")          # 若为非法 UTF-8 或带 BOM 会在这里暴露
data = json.loads(text)
qs = data["questions"]

print("file bytes      :", len(raw))
print("UTF-8 BOM       :", raw[:3] == b"\xef\xbb\xbf")
print("top-level keys  :", list(data.keys()))
print("batch           :", data["batch"])
print("questions       :", len(qs))

ids = [q["id"] for q in qs]
main = [i for i in ids if i.startswith("s")]
branch = [i for i in ids if i.startswith("h")]
print("main ids        :", f"{main[0]}..{main[-1]}", f"({len(main)} 题)")
print("branch ids      :", branch, f"({len(branch)} 题)")

expect = [f"s{i}" for i in range(33, 49)] + \
         [f"h3{a}{n}" for a in "abc" for n in (1, 2, 3)]
print("id set matches  :", sorted(ids) == sorted(expect))

secs = {q.get("sec") for q in qs}
print("sec values      :", secs, "| all social:", secs == {"social"})

hubs = [q["id"] for q in qs if q.get("kind") == "hub"]
print("hub             :", hubs)

opt_stats = {}
for q in qs:
    opt_stats.setdefault(len(q["opts"]), []).append(q["id"])
print("option counts   :", {k: len(v) for k, v in sorted(opt_stats.items())})
for k, v in sorted(opt_stats.items()):
    if k != 4:
        print(f"   {k}-option questions: {v}")

missing_next = [q["id"] for q in qs if "next" not in q]
print("missing next    :", missing_next or "none")
print("s48.next        :", qs[-1]["next"], "| s48 id:", qs[-1]["id"])

goto_edges = [(q["id"], o["goto"]) for q in qs for o in q["opts"] if "goto" in o]
print("goto edges      :", goto_edges)

# 分支链回归点
print("branch chain tails:",
      {hid: next(x for x in qs if x["id"] == hid)["next"]
       for hid in ["h3a3", "h3b3", "h3c3"]})
