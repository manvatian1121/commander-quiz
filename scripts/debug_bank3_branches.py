# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

qs = json.loads(Path(ROOT / "data" / "bank3.json").read_text(encoding="utf-8"))["questions"]
by_id = {q["id"]: q for q in qs}

print("hub s40 next =", by_id["s40"].get("next"))
for o in by_id["s40"]["opts"]:
    node, path = o.get("goto"), []
    for _ in range(3):
        if node not in by_id:
            path.append(str(node) + "(missing)")
            break
        path.append(node)
        node = by_id[node].get("next")
    print(f"goto={o.get('goto')!r:8} path={path}  back={bool(path) and path[-1] == 's41'}")

print()
for hid in ["h3a1", "h3a2", "h3a3", "h3b3", "h3c3"]:
    print(hid, "next =", by_id[hid].get("next"))
