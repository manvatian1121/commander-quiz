# -*- coding: utf-8 -*-
"""proof_check_45CE.py —— bank4 / bank5 / bankC / bankE 校对自检

对照 _proof_bak/ 下的改动前快照，逐项检查：
  1  id 集合与顺序      2  next / goto      3  每题选项数
  4  每个选项的轴得分键集合（s 的键；附带检查 col/cval/exp 键）
  5  题内选项文本两两不同
  6  题内两两选项「轴向量」（仅 s）余弦 < 0.85（另打印最大余弦）
  7  bank4 col 字段数量（W/U/B/R/G 各 4）
  8  bank5 s75~s80 的 multi 值

另有两项附加体检：其余字段（kind/multi/sec/col/cval/exp）逐题不变；文本改动清单。
用法: python proof_check_45CE.py
"""
import sys, json, math
from pathlib import Path
from itertools import combinations

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

DATA = Path(ROOT / "data")
BAK = DATA / "_proof_bak"
FILES = ["bank4.json", "bank5.json", "bankC.json", "bankE.json"]
COS_LIMIT = 0.85

fails, warns = [], []


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def qmap(data):
    return {q["id"]: q for q in data["questions"]}


def axis(opt):
    """轴向量：只看 s（轴得分）。col/cval/exp 不是轴。"""
    return dict(opt.get("s") or {})


def cos(a, b):
    keys = set(a) | set(b)
    num = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
    da = math.sqrt(sum(a.get(k, 0) ** 2 for k in keys))
    db = math.sqrt(sum(b.get(k, 0) ** 2 for k in keys))
    if da == 0 or db == 0:
        return None            # 含空向量：无轴可比
    return num / (da * db)


print("=" * 76)
print("proof_check_45CE —— 校对自检（对照 _proof_bak/ 改动前快照）")
print("=" * 76)

for name in FILES:
    cur, bak = load(DATA / name), load(BAK / name)
    cqs, bqs = cur["questions"], bak["questions"]
    c_ids = [q["id"] for q in cqs]
    b_ids = [q["id"] for q in bqs]
    print(f"\n### {name}  batch={cur.get('batch')!r}  题数={len(cqs)}")

    # 0. 顶层字段
    if set(cur) != set(bak):
        fails.append(f"{name}: 顶层字段变化 {set(bak)} -> {set(cur)}")

    # 1. id 集合与顺序
    ok1 = c_ids == b_ids
    print(f"  [1] id 集合与顺序: {'OK' if ok1 else 'FAIL'}")
    if not ok1:
        fails.append(f"{name}: id 顺序/集合变化 {b_ids} -> {c_ids}")

    cm, bm = qmap(cur), qmap(bak)
    maxcos_overall = (None, None, -1)

    for bq in bqs:
        q = cm[bq["id"]]
        qid = bq["id"]
        co, bo = q["opts"], bq["opts"]

        # 2. next / goto
        if q.get("next") != bq.get("next"):
            fails.append(f"{qid}: next {bq.get('next')!r} -> {q.get('next')!r}")
        for i, (c, b) in enumerate(zip(co, bo)):
            if c.get("goto") != b.get("goto"):
                fails.append(f"{qid}{chr(65+i)}: goto {b.get('goto')!r} -> {c.get('goto')!r}")

        # 3. 选项数
        if len(co) != len(bo):
            fails.append(f"{qid}: 选项数 {len(bo)} -> {len(co)}")

        # 4. 轴得分键集合（逐位置比较）
        for i, (c, b) in enumerate(zip(co, bo)):
            if set(axis(c)) != set(axis(b)):
                fails.append(f"{qid}{chr(65+i)}: 轴键 {sorted(axis(b))} -> {sorted(axis(c))}")
            if axis(c) != axis(b):
                warns.append(f"{qid}{chr(65+i)}: 轴值变化 {axis(b)} -> {axis(c)}")
            for f in ("col", "cval"):        # dict 型
                if set(c.get(f) or {}) != set(b.get(f) or {}):
                    fails.append(f"{qid}{chr(65+i)}: {f} 键变化 "
                                 f"{sorted(b.get(f) or {})} -> {sorted(c.get(f) or {})}")
                elif (c.get(f) or {}) != (b.get(f) or {}):
                    warns.append(f"{qid}{chr(65+i)}: {f} 值变化")
            if c.get("exp") != b.get("exp"):    # int 型（门槛题）
                fails.append(f"{qid}{chr(65+i)}: exp {b.get('exp')!r} -> {c.get('exp')!r}")
        # 其余字段（kind / multi / sec）
        for f in ("kind", "multi", "sec"):
            if q.get(f) != bq.get(f):
                fails.append(f"{qid}: {f} {bq.get(f)!r} -> {q.get(f)!r}")

        # 5. 题内选项文本两两不同
        texts = [o["t"] for o in co]
        dups = {t for t in texts if texts.count(t) > 1}
        if dups:
            fails.append(f"{qid}: 选项文本重复 {sorted(dups)}")

        # 6. 两两轴向量余弦 < 0.85
        vs = [axis(o) for o in co]
        for i, j in combinations(range(len(co)), 2):
            c = cos(vs[i], vs[j])
            if c is None:
                if not vs[i] and not vs[j]:
                    warns.append(f"{qid}{chr(65+i)}-{chr(65+j)}: 双方都无轴得分（如门槛题），余弦不适用")
                continue
            if c > maxcos_overall[2]:
                maxcos_overall = (qid, f"{chr(65+i)}-{chr(65+j)}", c)
            if c >= COS_LIMIT:
                fails.append(f"{qid}{chr(65+i)}-{chr(65+j)}: 余弦 {c:.3f} >= {COS_LIMIT}")

    if maxcos_overall[2] >= 0:
        print(f"  [6] 轴向量余弦: 最大 {maxcos_overall[2]:.3f} "
              f"({maxcos_overall[0]} {maxcos_overall[1]})，阈值 {COS_LIMIT}")

    # 文本改动清单
    diffs = []
    for bq in bqs:
        q = cm[bq["id"]]
        if q["q"] != bq["q"]:
            diffs.append(f"    {bq['id']}.q : {bq['q']}  ->  {q['q']}")
        for i, (c, b) in enumerate(zip(q["opts"], bq["opts"])):
            if c["t"] != b["t"]:
                diffs.append(f"    {bq['id']}{chr(65+i)}.t: {b['t']}  ->  {c['t']}")
    print(f"  [文本改动] {len(diffs)} 处")
    for d in diffs:
        print(d)

    ids_sec_ok = all(q.get("sec") == b.get("sec") for q, b in zip(cqs, bqs))
    print(f"  [2/3/4/5] next·goto·选项数·轴键: {'OK' if not fails else '见 FAIL 汇总'}"
          f"   sec 不变: {'OK' if ids_sec_ok else 'FAIL'}")

# 7. bank4 col 计数
b4 = load(DATA / "bank4.json")
b4b = load(BAK / "bank4.json")
cnt, cntb = {}, {}
for q in b4["questions"]:
    for o in q["opts"]:
        for k in (o.get("col") or {}):
            cnt[k] = cnt.get(k, 0) + 1
for q in b4b["questions"]:
    for o in q["opts"]:
        for k in (o.get("col") or {}):
            cntb[k] = cntb.get(k, 0) + 1
ok7 = cnt == cntb
print(f"\n### [7] bank4 col 数量: {cnt} (改前 {cntb}) -> {'OK' if ok7 else 'FAIL'}")
if not ok7:
    fails.append(f"bank4: col 数量 {cntb} -> {cnt}")

# 8. bank5 multi
b5 = load(DATA / "bank5.json")
b5b = load(BAK / "bank5.json")
m, mb = {}, {}
for q in b5["questions"]:
    if q.get("multi") is not None:
        m[q["id"]] = q["multi"]
for q in b5b["questions"]:
    if q.get("multi") is not None:
        mb[q["id"]] = q["multi"]
target = ["s75", "s76", "s77", "s78", "s79", "s80"]
ok8 = all(m.get(k) == mb.get(k) for k in target) and set(m) == set(mb)
print(f"### [8] bank5 multi: {m} (改前 {mb}) -> {'OK' if ok8 else 'FAIL'}")
if not ok8:
    fails.append(f"bank5: multi {mb} -> {m}")

print("\n" + "=" * 76)
if fails:
    print(f"结果: FAIL {len(fails)} 项")
    for f in fails:
        print("  ✗", f)
else:
    print("结果: 全部 8 项检查通过 ✓")
if warns:
    print(f"\n提示 {len(warns)} 项（不影响判定）:")
    for w in warns[:20]:
        print("  -", w)
    if len(warns) > 20:
        print(f"  ...（共 {len(warns)} 项）")
print("=" * 76)
sys.exit(1 if fails else 0)
