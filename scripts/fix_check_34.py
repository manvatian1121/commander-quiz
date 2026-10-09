# -*- coding: utf-8 -*-
"""bank3.json / bank4.json 选项配平修正 —— 自检脚本（FIX_SPEC.md 第 1~7 条）。

对照基线：data/_backup_bank3_prefix.json / _backup_bank4_prefix.json（改动前快照）。

检查项：
  1. id 集合与修改前完全一致（顺序也一致）
  2. 所有 next / goto 没变
  3. 每题选项数 3~5
  4. 每个选项 1~3 个轴、权重 ∈ {1.0,1.5,2.0,2.5,3.0}
  5. 每题内两两选项余弦 < 0.85（报告全库最高的那一对及数值）
  6. 选项文本在题内不重复
  7. col 字段数量与修改前一致（bank4 应为 W/U/B/R/G 各 4 处）
另附：改动清单（题号 / 属于修正一还是二 / 改了什么）

Run:  python fix_check_34.py
报告写到 scripts/fix_check_34_report.txt (UTF-8)。
"""
import json
import math
import sys
from pathlib import Path

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

DATA = Path(ROOT / "data")
OUT_RPT = Path(SCRIPT_DIR / "fix_check_34_report.txt")

TARGETS = [
    ("bank3", DATA / "_backup_bank3_prefix.json", DATA / "bank3.json"),
    ("bank4", DATA / "_backup_bank4_prefix.json", DATA / "bank4.json"),
]

AXES = {
    "aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
    "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
    "clonesteal", "politics", "chaos", "counters", "blink",
}
WEIGHTS = {1.0, 1.5, 2.0, 2.5, 3.0}
COS_LIMIT = 0.85
COLORS = ["W", "U", "B", "R", "G"]

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


def cos(v1, v2):
    keys = set(v1) | set(v2)
    dot = sum(v1.get(k, 0.0) * v2.get(k, 0.0) for k in keys)
    n1 = math.sqrt(sum(v1.get(k, 0.0) ** 2 for k in keys))
    n2 = math.sqrt(sum(v2.get(k, 0.0) ** 2 for k in keys))
    return dot / (n1 * n2) if n1 and n2 else 0.0


# ---------------------------------------------------------------- load
banks = {}
load_error = []
for key, backup, target in TARGETS:
    try:
        old = json.loads(backup.read_text(encoding="utf-8"))
        new = json.loads(target.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        load_error.append(f"{key}: {e}")
        continue
    banks[key] = {"old": old, "new": new, "path": target}

log("=" * 78)
log("bank3 / bank4 选项配平修正自检（FIX_SPEC.md）")
log("=" * 78)
for key, b in banks.items():
    log(f"{key}.json: {len(b['old']['questions'])} -> {len(b['new']['questions'])} questions, "
        f"batch={b['old']['batch']}->{b['new']['batch']}, path={b['path']}")
log()

if load_error:
    bad(0, "JSON 可解析", " | ".join(load_error))
    OUT_RPT.write_text("\n".join(report), encoding="utf-8")
    sys.exit(1)

# ---------------------------------------------------------------- 1. ids
prob1 = []
for key, b in banks.items():
    oid = [q["id"] for q in b["old"]["questions"]]
    nid = [q["id"] for q in b["new"]["questions"]]
    if oid != nid:
        prob1.append(f"{key}: {set(oid) ^ set(nid)} / order {oid != nid}")
if not prob1:
    ok(1, "id 集合与修改前完全一致",
       " | ".join(f"{k}: {len(b['new']['questions'])} ids 顺序一致" for k, b in banks.items()))
else:
    bad(1, "id 集合", " | ".join(prob1))

# ---------------------------------------------------------------- 2. next / goto
prob2 = []
goto_n_old = goto_n_new = 0
for key, b in banks.items():
    om = {q["id"]: q for q in b["old"]["questions"]}
    for q in b["new"]["questions"]:
        o = om[q["id"]]
        if o.get("next") != q.get("next"):
            prob2.append(f"{key} {q['id']}.next {o.get('next')} -> {q.get('next')}")
        og = [x.get("goto") for x in o["opts"] if "goto" in x]
        ng = [x.get("goto") for x in q["opts"] if "goto" in x]
        goto_n_old += len(og)
        goto_n_new += len(ng)
        if og != ng:
            prob2.append(f"{key} {q['id']}.goto {og} -> {ng}")
if not prob2:
    ok(2, "所有 next / goto 没变", f"goto 边数 {goto_n_old} -> {goto_n_new}（逐题有序比对通过）")
else:
    bad(2, "next / goto", " | ".join(prob2))

# ---------------------------------------------------------------- 3. option count
prob3 = []
hist = {}
for key, b in banks.items():
    for q in b["new"]["questions"]:
        n = len(q["opts"])
        hist[n] = hist.get(n, 0) + 1
        if not 3 <= n <= 5:
            prob3.append(f"{key} {q['id']} has {n} options")
if not prob3:
    ok(3, "每题选项数 3~5", f"题数 {sum(hist.values())}, 分布 {dict(sorted(hist.items()))}")
else:
    bad(3, "选项数 3~5", " | ".join(prob3))

# ---------------------------------------------------------------- 4. axes / weights
prob4 = []
new_opts = []
for key, b in banks.items():
    om = {q["id"]: q for q in b["old"]["questions"]}
    for q in b["new"]["questions"]:
        old_texts = {x["t"] for x in om[q["id"]]["opts"]}
        for o in q["opts"]:
            s = o.get("s", {})
            if not 1 <= len(s) <= 3:
                prob4.append(f"{key} {q['id']} [{o['t'][:14]}] {len(s)} axes")
            for a, w in s.items():
                if a not in AXES:
                    prob4.append(f"{key} {q['id']} [{o['t'][:14]}] unknown axis {a}")
                if w not in WEIGHTS:
                    prob4.append(f"{key} {q['id']} [{o['t'][:14]}] illegal weight {a}={w}")
            if o["t"] not in old_texts:
                new_opts.append((key, q["id"], o["t"], s))
if not prob4:
    ok(4, "每选项 1~3 轴、权重 ∈ {1.0,1.5,2.0,2.5,3.0}",
       f"新增选项 {len(new_opts)} 个全部合法")
else:
    bad(4, "轴 / 权重合法性", " | ".join(prob4))

# ---------------------------------------------------------------- 5. cosine
prob5 = []
all_cos = []
for key, b in banks.items():
    for q in b["new"]["questions"]:
        vs = [(o["t"], o["s"]) for o in q["opts"]]
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                c = cos(vs[i][1], vs[j][1])
                all_cos.append((c, key, q["id"], vs[i][0], vs[j][0]))
                if c >= COS_LIMIT:
                    prob5.append(f"{key} {q['id']} {c:.3f} [{vs[i][0][:16]}] x [{vs[j][0][:16]}]")
all_cos.sort(key=lambda z: -z[0])
top = all_cos[0]
if not prob5:
    ok(5, f"每题内两两选项余弦 < {COS_LIMIT}",
       f"{len(all_cos)} 对，全库最高 {top[0]:.4f} @ {top[1]} {top[2]} "
       f"[{top[3][:18]}] x [{top[4][:18]}]")
else:
    bad(5, f"余弦 < {COS_LIMIT}", " | ".join(prob5))
log()
log(f"       全库余弦最高的 5 对（含 bank3+bank4 共 {len(all_cos)} 对）:")
for c, key, qid, a, bb in all_cos[:5]:
    flag = "  <-- 超限" if c >= COS_LIMIT else ""
    log(f"         {c:.4f}  {key} {qid}  [{a[:22]}] x [{bb[:22]}]{flag}")
log()

# 新增选项与其同题其它选项的余弦（FIX_SPEC：新选项必须 < 0.85）
log("       新增选项 vs 同题其它选项的余弦:")
for key, qid, t, s in new_opts:
    b = banks[key]
    q = next(x for x in b["new"]["questions"] if x["id"] == qid)
    pairs = sorted(((cos(s, o["s"]), o["t"]) for o in q["opts"] if o["t"] != t), reverse=True)
    worst = pairs[0] if pairs else (0.0, "-")
    log(f"         {key} {qid} 新增[{t[:20]}]  最大 {worst[0]:.3f} vs [{worst[1][:20]}]")
log()

# ---------------------------------------------------------------- 6. duplicate texts
prob6 = []
for key, b in banks.items():
    for q in b["new"]["questions"]:
        texts = [o["t"].strip() for o in q["opts"]]
        if any(not t for t in texts):
            prob6.append(f"{key} {q['id']} 有空选项文本")
        if len(set(texts)) != len(texts):
            prob6.append(f"{key} {q['id']} 题内重复文本")
if not prob6:
    ok(6, "选项文本在题内不重复", f"{sum(len(q['opts']) for b in banks.values() for q in b['new']['questions'])} 个选项")
else:
    bad(6, "题内文本重复", " | ".join(prob6))

# ---------------------------------------------------------------- 7. col fields
prob7 = []
for key, b in banks.items():
    def col_counts(bank):
        cnt = {c: 0 for c in COLORS}
        total = 0
        questions = 0
        for q in bank["questions"]:
            has = False
            for o in q["opts"]:
                if "col" in o:
                    total += 1
                    has = True
                    for c, v in o["col"].items():
                        cnt[c] = cnt.get(c, 0) + 1
            if has:
                questions += 1
        return total, cnt, questions
    o_total, o_cnt, o_q = col_counts(b["old"])
    n_total, n_cnt, n_q = col_counts(b["new"])
    if o_total != n_total or o_cnt != n_cnt:
        prob7.append(f"{key}: total {o_total}->{n_total}, {o_cnt}->{n_cnt}")
    # 逐题核对 col 是否原样保留
    om = {q["id"]: q for q in b["old"]["questions"]}
    for q in b["new"]["questions"]:
        old_cols = [o.get("col") for o in om[q["id"]]["opts"] if "col" in o]
        new_cols = [o.get("col") for o in q["opts"] if "col" in o]
        if old_cols != new_cols:
            prob7.append(f"{key} {q['id']} col 序列变了: {old_cols} -> {new_cols}")
    log(f"       {key}: col 字段 {o_total} -> {n_total} 处，颜色题 {o_q} -> {n_q} 道，"
        f"分布 {dict(sorted(n_cnt.items())) if n_total else '（无）'}")
if not prob7:
    b4 = banks["bank4"]
    cnt = {c: 0 for c in COLORS}
    for q in b4["new"]["questions"]:
        for o in q["opts"]:
            for c in o.get("col", {}):
                cnt[c] += 1
    ok(7, "col 字段数量与修改前一致",
       f"bank4 W/U/B/R/G = " + " ".join(f"{c}:{cnt[c]}" for c in COLORS) +
       "；bank3 无 col 字段")
else:
    bad(7, "col 字段", " | ".join(prob7))

# ---------------------------------------------------------------- 改动清单
log()
log("=" * 78)
log("改动清单（逐条复核用）")
log("=" * 78)
why = {
    ("bank3", "s35"): ("修正一", "题干是商家咬死价（别人造成的处境），原 4 选项全是主动应对"
                                 "（磨价/干等/换链接/自己当团长），无「不在意」"),
    ("bank3", "s36"): ("修正一", "题干是室友堆碗占了水池（别人造成的处境），原 4 选项全是主动应对"
                                 "（立规矩/自己洗+减分/隔开/当面挤兑），无「不在意」"),
    ("bank3", "s42"): ("修正一", "题干是合买被对方多占（别人造成的处境），原 4 选项全是主动应对"
                                 "（对质/另买/下次不合买/记账分摊），无「不在意」"),
    ("bank3", "s44"): ("修正一", "题干是对方回得越来越慢（别人造成的处境），原 4 选项全是主动应对"
                                 "（追问/加劲/收回热情/换方式），无「不在意」"),
    ("bank3", "h3a2"): ("修正一", "题干含「让朋友还钱」（别人造成的处境），原 4 选项全是主动谈判术"
                                  "（写底线/谈交情/直给/包装），无「不在意」"),
    ("bank3", "h3b1"): ("修正一", "题干是被插队（FIX_SPEC 明列的处境），原 4 选项全是主动反应"
                                  "（叫住/找工作人员/挤回去/笑着但记账），无「不在意」"),
    ("bank3", "h3b2"): ("修正一", "题干是被人公开说难听话（别人造成的处境），原 4 选项全是主动反应"
                                  "（回击/换圈子/截图备着/叫人帮腔），无「不在意」"),
    ("bank4", "s56"): ("修正二", "倾向性问句「那面空墙你打算怎么弄？」，原 3 选项全是「弄」= 3:0，"
                                 "补一个「先空着」的少数派选项 → 3:2"),
}
for key, b in banks.items():
    om = {q["id"]: q for q in b["old"]["questions"]}
    for q in b["new"]["questions"]:
        oq = om[q["id"]]
        added = [o for o in q["opts"] if o["t"] not in {x["t"] for x in oq["opts"]}]
        removed = [o for o in oq["opts"] if o["t"] not in {x["t"] for x in q["opts"]}]
        if not added and not removed:
            continue
        pos = [x["id"] for x in b["old"]["questions"]].index(q["id"]) + 1
        kind, reason = why[(key, q["id"])]
        log(f"* {key} 第 {pos} 题 / {q['id']}  [{kind}]")
        log(f"    题干: {q['q']}")
        log(f"    依据: {reason}")
        if added:
            a = added[0]
            log(f"    改动: 新增第 {q['opts'].index(a)+1} 个选项 「{a['t']}」")
            log(f"          轴得分 {a['s']}；选项数 {len(oq['opts'])} -> {len(q['opts'])}")
            if "goto" in a or "col" in a:
                log(f"          （含 goto/col 字段: {[k for k in ('goto','col') if k in a]}）")
        for r in removed:
            log(f"    改动: 删除选项 「{r['t']}」")
        log()
per_bank = {}
for key, b in banks.items():
    om = {q["id"]: q for q in b["old"]["questions"]}
    n = sum(len([o for o in q["opts"] if o["t"] not in {x["t"] for x in om[q["id"]]["opts"]}])
            for q in b["new"]["questions"])
    per_bank[key] = n
total_new = sum(per_bank.values())
log(f"合计：bank3 改 {per_bank['bank3']} 处，bank4 改 {per_bank['bank4']} 处，共 {total_new} 处")

log()
log("=" * 78)
if fails:
    log(f"RESULT: FAIL ({len(fails)} 项)")
    for f in fails:
        log("  - " + f)
else:
    log("RESULT: 7/7 PASSED")
log("=" * 78)

OUT_RPT.write_text("\n".join(report), encoding="utf-8")
print(f"\n报告写入 {OUT_RPT}")
sys.exit(1 if fails else 0)
