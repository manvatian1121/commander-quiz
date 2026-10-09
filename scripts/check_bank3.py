# -*- coding: utf-8 -*-
"""Self-check for bank3.json (batch 3, section: social). 9 checks.

Run:  python check_bank3.py
Writes a readable report to check_bank3_report.txt (UTF-8).
"""
import json
import math
import sys
from pathlib import Path

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

BANK = Path(ROOT / "data" / "bank3.json")
OUT_RPT = Path(SCRIPT_DIR / "check_bank3_report.txt")

AXES = [
    "aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
    "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
    "clonesteal", "politics", "chaos", "counters", "blink",
]
WEIGHTS = {1.0, 1.5, 2.0, 2.5, 3.0}

# Opposite axis pairs: scoring both high in one option means a vague option.
OPPOSITE = [
    ("aggro", "control"), ("aggro", "drain"), ("aggro", "stax"), ("aggro", "blink"),
    ("chaos", "control"), ("chaos", "stax"), ("wide", "voltron"), ("ramp", "aggro"),
]

# Magic: The Gathering jargon blacklist.
MTG_TERMS = [
    "主将", "指挥官", "牌组", "套牌", "牌表", "卡牌", "卡组", "咒语", "法术力",
    "铺场", "反击", "坟场", "墓地", "生物", "结界", "灵气", "神器", "指示物",
    "回合", "法力", "手牌", "牌库", "抽牌", "抓牌", "召唤", "衍生物", "牺牲",
    "共鸣", "闪现", "警戒", "先攻", "死触", "thopter", "tutor", "commander",
    "mana", "deck",
]

FREQ_MIN = 12
COS_LIMIT = 0.85

MAIN = [f"s{i:02d}" for i in range(33, 49)]          # s33 .. s48
BRANCHES = {
    "a": ["h3a1", "h3a2", "h3a3"],
    "b": ["h3b1", "h3b2", "h3b3"],
    "c": ["h3c1", "h3c2", "h3c3"],
}
HUBS = ["s40"]
EXTERNAL_EXITS = {"s49"}   # lives in batch 4; referencing it is the intended seam

report = []
fails = []


def log(s=""):
    report.append(s)
    print(s)


def ok(n, title, detail=""):
    log(f"[PASS] {n}. {title}" + (f" -- {detail}" if detail else ""))


def bad(n, title, detail=""):
    fails.append(f"{n}. {title}: {detail}")
    log(f"[FAIL] {n}. {title}" + (f" -- {detail}" if detail else ""))


# ---------- 0. load ----------
try:
    data = json.loads(BANK.read_text(encoding="utf-8"))
    qs = data["questions"]
except Exception as e:  # noqa: BLE001
    print(f"[FAIL] 0. JSON not parseable: {e}")
    sys.exit(1)

by_id = {}
for q in qs:
    by_id[q["id"]] = q


def cos(v1, v2):
    keys = set(v1) | set(v2)
    dot = sum(v1.get(k, 0.0) * v2.get(k, 0.0) for k in keys)
    n1 = math.sqrt(sum(v1.get(k, 0.0) ** 2 for k in keys))
    n2 = math.sqrt(sum(v2.get(k, 0.0) ** 2 for k in keys))
    return dot / (n1 * n2) if n1 and n2 else 0.0


log("=" * 78)
log("bank3.json self-check (batch 3 / social)")
log("=" * 78)
log(f"questions: {len(qs)} (expected 25)")
log()

# ---------- 1. valid JSON, unique ids ----------
ids = [q["id"] for q in qs]
dup = sorted({i for i in ids if ids.count(i) > 1})
if len(qs) == 25 and not dup and len(by_id) == 25:
    ok(1, "valid JSON + unique ids", f"25 ids, batch={data.get('batch')}")
else:
    bad(1, "valid JSON + unique ids", f"count={len(qs)} dup={dup}")

# ---------- 2. every question has next ----------
miss_next = [q["id"] for q in qs if "next" not in q]
if not miss_next and by_id.get("s48", {}).get("next") == "s49":
    ok(2, "every question has a next field", "s48.next = s49")
else:
    bad(2, "every question has a next field",
        f"missing={miss_next} s48.next={by_id.get('s48', {}).get('next')}")

# ---------- 3. every goto resolves ----------
bad_goto = []
goto_n = 0
for q in qs:
    for o in q["opts"]:
        if "goto" in o:
            goto_n += 1
            if o["goto"] not in by_id:
                bad_goto.append((q["id"], o["goto"]))
if not bad_goto:
    ok(3, "every goto resolves to an existing id", f"{goto_n} goto edges")
else:
    bad(3, "every goto resolves to an existing id", str(bad_goto))

# ---------- 4. the whole chain is walkable ----------
walk_errors = []
cur, seen_main, hops = "s33", [], 0
while cur is not None and hops < 500:
    hops += 1
    seen_main.append(cur)
    if cur in EXTERNAL_EXITS:
        break
    if cur not in by_id:
        walk_errors.append(f"main line references missing question {cur}")
        break
    if cur in HUBS:
        hub = by_id[cur]
        if hub.get("next") != "s41":
            walk_errors.append(f"{cur}.next should be s41, is {hub.get('next')}")
        gotos = [o.get("goto") for o in hub["opts"]]
        if any(g is None for g in gotos):
            walk_errors.append(f"{cur} has options without goto")
        if len(gotos) != len(set(gotos)):
            walk_errors.append(f"{cur} routes two options into the same entry: {gotos}")
        entries = {chain[0] for chain in BRANCHES.values()}
        if set(gotos) != entries:
            walk_errors.append(f"{cur} goto targets {gotos} != branch entries {sorted(entries)}")
        for bk, chain in BRANCHES.items():
            if chain[0] not in gotos:
                walk_errors.append(f"{cur} does not goto branch {bk} start {chain[0]} (got {gotos})")
            for i, hid in enumerate(chain):
                if hid not in by_id:
                    walk_errors.append(f"{hid} missing")
                    continue
                want = chain[i + 1] if i + 1 < len(chain) else "s41"
                if by_id[hid].get("next") != want:
                    walk_errors.append(f"{hid}.next should be {want}, is {by_id[hid].get('next')}")
        # every branch question must be reachable by following goto/next from the hub
        reach = set()
        frontier = list(gotos)
        while frontier:
            nid = frontier.pop()
            if nid in reach or nid not in by_id:
                continue
            reach.add(nid)
            if nid in EXTERNAL_EXITS:
                continue
            for t in [o.get("goto") for o in by_id[nid]["opts"] if o.get("goto")] or [by_id[nid].get("next")]:
                if t:
                    frontier.append(t)
        all_branch = {h for chain in BRANCHES.values() for h in chain}
        unreachable = sorted(all_branch - reach)
        if unreachable:
            walk_errors.append(f"branch questions unreachable from hub: {unreachable}")
    cur = by_id[cur].get("next")

expect_main = MAIN + ["s49"]
if seen_main != expect_main:
    walk_errors.append(f"main-line walk mismatch: {seen_main} != {expect_main}")

# branches: each hub option must lead through a 3-question chain that returns to s41
branch_paths = []
for o in by_id["s40"]["opts"]:
    node, path = o.get("goto"), []
    for _ in range(3):
        if node not in by_id:
            path.append(f"{node}(missing)")
            node = None
            break
        path.append(node)
        node = by_id[node].get("next")
    chain_ok = len(path) == 3 and path[-1] in by_id and by_id[path[-1]].get("next") == "s41"
    branch_paths.append((o["t"][:16] + "...", path, chain_ok))
    if not chain_ok:
        walk_errors.append(f"branch chain broken: {path} -> {node}")

if not walk_errors:
    ok(4, "chain walkable",
       "main " + " > ".join(seen_main) + " ; 3 branches x 3 hops back to s41")
else:
    bad(4, "chain walkable", " | ".join(walk_errors))

# ---------- 5. 3..5 options, non-empty and pairwise distinct ----------
opt_problems = []
opt_count = 0
for q in qs:
    n = len(q["opts"])
    opt_count += n
    if not (3 <= n <= 5):
        opt_problems.append(f"{q['id']} has {n} options")
    texts = [o["t"].strip() for o in q["opts"]]
    if any(not t for t in texts):
        opt_problems.append(f"{q['id']} has an empty option text")
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            if texts[i] == texts[j]:
                opt_problems.append(f"{q['id']} options {i+1}/{j+1} identical")
if not opt_problems:
    sizes = {}
    for q in qs:
        sizes[len(q["opts"])] = sizes.get(len(q["opts"]), 0) + 1
    ok(5, "3..5 options, non-empty and pairwise distinct",
       f"{opt_count} options, size histogram {dict(sorted(sizes.items()))}")
else:
    bad(5, "option count / text", " | ".join(opt_problems))

# ---------- 6. 1..3 axes per option, legal weights ----------
score_problems = []
for q in qs:
    for i, o in enumerate(q["opts"]):
        s = o.get("s", {})
        if not (1 <= len(s) <= 3):
            score_problems.append(f"{q['id']}#{i+1} has {len(s)} axes")
        for a, w in s.items():
            if a not in AXES:
                score_problems.append(f"{q['id']}#{i+1} unknown axis {a}")
            if w not in WEIGHTS:
                score_problems.append(f"{q['id']}#{i+1} illegal weight {a}={w}")
if not score_problems:
    ok(6, "1..3 axes per option, weights in 1.0/1.5/2.0/2.5/3.0", f"{opt_count} options")
else:
    bad(6, "axis scoring legality", " | ".join(score_problems))

contra = []
for q in qs:
    for i, o in enumerate(q["opts"]):
        for a, b in OPPOSITE:
            if o["s"].get(a, 0) >= 2.0 and o["s"].get(b, 0) >= 2.0:
                contra.append(f"{q['id']}#{i+1} {a}+{b} both >= 2.0")
if contra:
    log(f"       [WARN] opposite axes both high: {' | '.join(contra)}")
else:
    log("       [OK] no option scores two opposite axes >= 2.0")

# ---------- 7. cosine similarity < 0.85 within a question ----------
cos_over = []
cos_max, cos_max_at = 0.0, ""
checked = 0
for q in qs:
    vs = [(o["t"], o["s"]) for o in q["opts"]]
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            c = cos(vs[i][1], vs[j][1])
            checked += 1
            if c > cos_max:
                cos_max, cos_max_at = c, f"{q['id']} {vs[i][0][:14]} x {vs[j][0][:14]}"
            if c >= COS_LIMIT:
                cos_over.append({"id": q["id"], "a": vs[i][0], "b": vs[j][0], "cos": c,
                                 "va": vs[i][1], "vb": vs[j][1]})
if not cos_over:
    ok(7, f"ambiguity check: every intra-question pair < {COS_LIMIT}",
       f"{checked} pairs, max {cos_max:.4f} ({cos_max_at})")
else:
    detail = " | ".join(
        f"{x['id']} {x['cos']:.3f} [{x['a'][:18]}] vs [{x['b'][:18]}] {x['va']} / {x['vb']}"
        for x in sorted(cos_over, key=lambda z: -z["cos"])
    )
    bad(7, f"ambiguity check (limit {COS_LIMIT})", detail)

# ---------- 8. axis coverage ----------
freq = {a: 0 for a in AXES}
for q in qs:
    for o in q["opts"]:
        for a in o["s"]:
            freq[a] += 1
under = [a for a in AXES if freq[a] < FREQ_MIN]
log(f"[{'PASS' if not under else 'FAIL'}] 8. axis coverage (each axis >= {FREQ_MIN} options)")
log("       coverage table:")
for a in sorted(AXES, key=lambda x: (-freq[x], x)):
    log(f"         {a:<12}{freq[a]:>4}" + ("" if freq[a] >= FREQ_MIN else "   <-- under"))
if not under:
    ok(8, "axis coverage ok",
       f"min {min(freq.values())}, max {max(freq.values())}, total references {sum(freq.values())}")
else:
    bad(8, "axis coverage", f"under: {under}")

# ---------- 9. MTG jargon scan ----------
hits = []
for q in qs:
    for kind, t in [("q", q["q"])] + [("opt", o["t"]) for o in q["opts"]]:
        low = t.lower()
        for term in MTG_TERMS:
            if term.lower() in low:
                hits.append(f"{q['id']}({kind}) hit [{term}]")
if not hits:
    ok(9, "no MTG jargon", f"{len(MTG_TERMS)} keywords x {len(qs)} stems + {opt_count} options")
else:
    bad(9, "MTG jargon scan", " | ".join(hits))

# ---------- summary ----------
log()
log("=" * 78)
if fails:
    log(f"RESULT: FAIL ({9 - len({f.split('.')[0] for f in fails})}/9 passed)")
    for f in fails:
        log("  - " + f)
else:
    log("RESULT: 9/9 PASSED")
log("=" * 78)

OUT_RPT.write_text("\n".join(report), encoding="utf-8")
print(f"\nreport written to {OUT_RPT}")
sys.exit(1 if fails else 0)
