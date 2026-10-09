# -*- coding: utf-8 -*-
r"""bank1 / bank2 / bank3 文字校对自检（对照 data/_proof_backup_bankN.json）

用法：python scripts/proof_check_123.py
退出码：0 = 6 项全过；1 = 有任一项不过
"""
import json
import math
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data")
BANKS = (1, 2, 3)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def cosine(a, b):
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(a.get(k, 0.0) ** 2 for k in keys))
    nb = math.sqrt(sum(b.get(k, 0.0) ** 2 for k in keys))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


results = []          # (检查项, 是否通过, 说明)
text_changes = []     # 实际改动（新 vs 旧），用于人工复核

# ---------- 0. 结构 & 编码 ----------
struct_ok = True
struct_note = []
cur = {}
old = {}
for b in BANKS:
    p_cur = os.path.join(DATA, f"bank{b}.json")
    p_old = os.path.join(DATA, f"_proof_backup_bank{b}.json")
    if not os.path.exists(p_old):
        struct_ok = False
        struct_note.append(f"bank{b}: 缺备份 {p_old}")
    try:
        with open(p_cur, "rb") as f:
            raw = f.read()
        raw.decode("utf-8")
        assert not raw.startswith(b"\xef\xbb\xbf"), "有 BOM"
        cur[b] = json.loads(raw.decode("utf-8"))
        old[b] = load(p_old)
    except Exception as e:  # noqa: BLE001
        struct_ok = False
        struct_note.append(f"bank{b}: {e}")
        continue
    if set(cur[b].keys()) != {"batch", "questions"}:
        struct_ok = False
        struct_note.append(f"bank{b}: 顶层键异常 {sorted(cur[b].keys())}")
    if cur[b].get("batch") != b:
        struct_ok = False
        struct_note.append(f"bank{b}: batch 字段={cur[b].get('batch')}")
    if not all(k in q for q in cur[b]["questions"] for k in ("id", "q", "opts")):
        struct_ok = False
        struct_note.append(f"bank{b}: 有题缺 id/q/opts")
results.append(("0. JSON 合法 / UTF-8 无 BOM / 顶层结构 {batch, questions}",
                struct_ok, "；".join(struct_note) if struct_note else "3 个文件全部通过"))

# ---------- 1. id 集合与顺序 ----------
ok1, note1 = True, []
for b in BANKS:
    a = [q["id"] for q in old[b]["questions"]]
    c = [q["id"] for q in cur[b]["questions"]]
    if a != c:
        ok1 = False
        note1.append(f"bank{b}: 顺序或集合不一致（旧 {len(a)} 个 / 新 {len(c)} 个）")
    else:
        note1.append(f"bank{b} {len(c)} 题一致")
results.append(("1. id 集合与顺序没变", ok1, "；".join(note1)))

# ---------- 2. next / goto ----------
ok2, note2 = True, []
goto_n = 0
for b in BANKS:
    for qo, qc in zip(old[b]["questions"], cur[b]["questions"]):
        if qo.get("next") != qc.get("next"):
            ok2 = False
            note2.append(f"bank{b} {qc['id']}: next {qo.get('next')} → {qc.get('next')}")
        for i, (oo, oc) in enumerate(zip(qo["opts"], qc["opts"])):
            if oo.get("goto") != oc.get("goto"):
                ok2 = False
                note2.append(f"bank{b} {qc['id']} 选项{chr(65+i)}: goto 变化")
            if oc.get("goto"):
                goto_n += 1
        # 顺带核对 protected 字段
        for f in ("sec", "kind", "multi"):
            if qo.get(f) != qc.get(f):
                ok2 = False
                note2.append(f"bank{b} {qc['id']}: {f} 变化")
results.append(("2. next / goto（及 sec/kind/multi）没变", ok2,
                f"{goto_n} 个 goto 全部一致" if ok2 else "；".join(note2)))

# ---------- 3. 每题选项数 ----------
ok3, note3 = True, []
dist = {}
for b in BANKS:
    for qo, qc in zip(old[b]["questions"], cur[b]["questions"]):
        dist[len(qc["opts"])] = dist.get(len(qc["opts"]), 0) + 1
        if len(qo["opts"]) != len(qc["opts"]):
            ok3 = False
            note3.append(f"bank{b} {qc['id']}: {len(qo['opts'])} → {len(qc['opts'])}")
        if not 3 <= len(qc["opts"]) <= 5:
            ok3 = False
            note3.append(f"bank{b} {qc['id']}: 选项数 {len(qc['opts'])} 越界")
results.append(("3. 每题选项数没变（且仍在 3~5）", ok3,
                f"分布 {dict(sorted(dist.items()))}" if ok3 else "；".join(note3)))

# ---------- 4. 轴得分键集合 + 值 ----------
ok4, note4 = True, []
val_diffs = []
for b in BANKS:
    for qo, qc in zip(old[b]["questions"], cur[b]["questions"]):
        for i, (oo, oc) in enumerate(zip(qo["opts"], qc["opts"])):
            so, sc = oo.get("s", {}), oc.get("s", {})
            if set(so) != set(sc):
                ok4 = False
                note4.append(f"bank{b} {qc['id']} {chr(65+i)}: 轴键 {sorted(so)} → {sorted(sc)}")
            if so != sc:
                val_diffs.append(f"bank{b} {qc['id']} {chr(65+i)}: {so} → {sc}")
            if not 1 <= len(sc) <= 3 or any(v not in (1.0, 1.5, 2.0, 2.5, 3.0) for v in sc.values()):
                ok4 = False
                note4.append(f"bank{b} {qc['id']} {chr(65+i)}: 轴格式异常 {sc}")
note4s = "轴键集合全部一致；轴值也无任何改动" if not val_diffs else "轴键一致，但轴值有改动：" + "；".join(val_diffs)
results.append(("4. 每选项轴得分键集合没变（附轴值核对）", ok4 and not val_diffs, note4s))

# ---------- 5. 题内选项文本两两不同 ----------
ok5, note5 = True, []
for b in BANKS:
    for qc in cur[b]["questions"]:
        ts = [o["t"].strip() for o in qc["opts"]]
        if any(not t for t in ts):
            ok5 = False
            note5.append(f"bank{b} {qc['id']}: 有空选项")
        if len(set(ts)) != len(ts):
            ok5 = False
            dup = [t for t in set(ts) if ts.count(t) > 1]
            note5.append(f"bank{b} {qc['id']}: 重复 {dup}")
n_opt = sum(len(q["opts"]) for b in BANKS for q in cur[b]["questions"])
results.append(("5. 题内选项文本两两不同（且非空）", ok5,
                f"{n_opt} 个选项全查无重复" if ok5 else "；".join(note5)))

# ---------- 6. 题内两两轴向量余弦 < 0.85 ----------
ok6, note6 = True, []
worst_old, worst_new = (0.0, ""), (0.0, "")
for b in BANKS:
    for qo, qc in zip(old[b]["questions"], cur[b]["questions"]):
        for tag, q, store in (("旧", qo, "old"), ("新", qc, "new")):
            for i in range(len(q["opts"])):
                for j in range(i + 1, len(q["opts"])):
                    c = cosine(q["opts"][i].get("s", {}), q["opts"][j].get("s", {}))
                    if c >= 0.85:
                        ok6 = False
                        note6.append(f"bank{b} {q['id']} {chr(65+i)}×{chr(65+j)} {tag} cos={c:.4f}")
                    if store == "old" and c > worst_old[0]:
                        worst_old = (c, f"bank{b} {q['id']} {chr(65+i)}×{chr(65+j)}")
                    if store == "new" and c > worst_new[0]:
                        worst_new = (c, f"bank{b} {q['id']} {chr(65+i)}×{chr(65+j)}")
results.append(("6. 题内两两轴向量余弦 < 0.85", ok6,
                f"改前最高 {worst_old[0]:.4f}（{worst_old[1]}）→ 改后最高 {worst_new[0]:.4f}（{worst_new[1]}）"))

# ---------- 文本改动台账 ----------
for b in BANKS:
    for qo, qc in zip(old[b]["questions"], cur[b]["questions"]):
        if qo["q"] != qc["q"]:
            text_changes.append(f"bank{b} {qc['id']} 题干：{qo['q']} → {qc['q']}")
        for i, (oo, oc) in enumerate(zip(qo["opts"], qc["opts"])):
            if oo["t"] != oc["t"]:
                text_changes.append(f"bank{b} {qc['id']} 选项{chr(65+i)}：{oo['t']} → {oc['t']}")

# ---------- 输出 ----------
print("=" * 78)
print("bank1 / bank2 / bank3 文字校对自检  （对照 data/_proof_backup_bankN.json）")
print("=" * 78)
for name, ok, note in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"        {note}")
print("-" * 78)
print(f"本轮文本改动 {len(text_changes)} 处：")
for t in text_changes or ["（无）"]:
    print("   ·", t)
print("-" * 78)
failed = [n for n, ok, _ in results if not ok]
print("结论：", "全部通过（0 项 FAIL）" if not failed else f"FAIL {len(failed)} 项：" + " / ".join(failed))
sys.exit(1 if failed else 0)
