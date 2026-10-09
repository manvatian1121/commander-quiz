import json
import math
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

DATA = ROOT / "data"

AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]


def vec(s):
    return [s.get(a, 0.0) for a in AXES]


def cos(s1, s2):
    v1, v2 = vec(s1), vec(s2)
    d = sum(a * b for a, b in zip(v1, v2))
    n1 = math.sqrt(sum(a * a for a in v1))
    n2 = math.sqrt(sum(b * b for b in v2))
    if n1 == 0 or n2 == 0:
        return 0.0
    return d / (n1 * n2)


def main():
    for name in ["bank1", "bank2"]:
        d = json.load(open(f"{DATA}\\{name}.json", encoding="utf-8"))
        print("#" * 70)
        print(f"### {name}  batch={d['batch']}  n={len(d['questions'])}")
        worst = (0, None)
        for q in d["questions"]:
            print("-" * 60)
            print(f"[{q['id']}] kind={q.get('kind','')} next={q.get('next')!r} :: {q['q']}")
            for i, o in enumerate(q["opts"]):
                g = f" goto={o['goto']}" if "goto" in o else ""
                print(f"   {i}: {o['t']}   {o['s']}{g}")
            for i in range(len(q["opts"])):
                for j in range(i + 1, len(q["opts"])):
                    c = cos(q["opts"][i]["s"], q["opts"][j]["s"])
                    if c >= 0.85:
                        print(f"   !! cos({i},{j})={c:.4f}")
                    if c > worst[0]:
                        worst = (c, (q["id"], i, j))
        print(f"### worst cos in {name}: {worst[0]:.4f} at {worst[1]}")


if __name__ == "__main__":
    main()
