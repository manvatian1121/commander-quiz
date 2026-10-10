import json
import sys
from pathlib import Path



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = Path(ROOT / "data")
AX = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
      "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
      "clonesteal", "politics", "chaos", "counters", "blink"]


def cov(p):
    d = json.loads(Path(p).read_text(encoding="utf-8"))
    c = {a: 0 for a in AX}
    for q in d["questions"]:
        for o in q["opts"]:
            for k in o["s"]:
                c[k] += 1
    return c


o = cov(DATA / "_backup_bank2.json")
n = cov(DATA / "bank2.json")
print("axis        改前  改后   差   低于12")
bad = []
for a in AX:
    flag = "YES" if n[a] < 12 else ""
    if n[a] < 12:
        bad.append(f"{a}({n[a]})")
    print(f"{a:<11}{o[a]:>4}{n[a]:>6}{n[a] - o[a]:>5}   {flag}")
print("低于 12 的轴：", bad if bad else "无")
