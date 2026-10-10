"""自检脚本：commander-quiz 题库「选项设计缺陷」修正（bank1 / bank2）

对应任务：修正一（缺「不在意」选项）、修正二（正负选项配平）。
对照物：data/_backup_bank1.json、data/_backup_bank2.json（修改前的原件）。

逐项检查：
  1. id 集合（含顺序）与修改前完全一致
  2. 所有 next / goto 没变
  3. 每题选项数 3~5
  4. 每个选项 1~3 个轴、权重 ∈ {1.0, 1.5, 2.0, 2.5, 3.0}
  5. 每题内两两选项余弦 < 0.85（并报告全库最高的一对及数值）
  6. 选项文本在题内不重复
另附：
  A. 修正二 的极性配平复核（改动前 → 改动后）
  B. 被改题目的最高余弦一对（改前 → 改后）
  C. 轴覆盖变化（并标出低于 bank 门槛 12 的轴 —— 见报告的「已知代价」）
  D. 改动清单（逐条：题号 / 修正类型 / 改了什么 / 为什么），由备份与现文件的结构化 diff 生成，
     并反向校验「除这些选项外没有任何其它改动」。
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
FILES = [("bank1", DATA / "bank1.json", DATA / "_backup_bank1.json"),
         ("bank2", DATA / "bank2.json", DATA / "_backup_bank2.json")]

WEIGHTS = {1.0, 1.5, 2.0, 2.5, 3.0}
AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]
COVER_FLOOR = 12   # check_bank2.py / QUESTION_SPEC §9 的单库轴覆盖门槛

FIX_LOG = {
    "h2a3": ("修正二", "题干「选完之后，你还会回头改吗？」是典型的会/不会倾向性问句。原有「会」4 个、「不会」1 个（4:1，超过 3:2）。按规范改多数派里语义最重复的那一个：原（隔三差五复盘一次，看看还能怎么优化）与（过一阵子会再拿出来重新试一次）同属「回头再弄一遍」（本題余弦最高的一对也正是这两条，cos=0.3185），故替换前者，改写为「不会」方向；改后「会」3 : 「不会」2 = 3:2。"),
    "s27": ("修正一", "题干「公司给你换了一套全新的系统，没人教，下周就要用」是别人/外部造成的、对你不利的处境；五个选项（自己摸/看教程/直接开干/问同事/搭模板）全是主动应对，没有任何「没往心里去 / 无所谓 / 随它去」。选项已满 5 个，须替换语义最重复的那一个：原（周末自己摸，每个按钮点一遍，界面也调成自己顺眼的）与（先搭一套自己的模板，以后所有活都套这个）同属「自己动手把系统变成我的」，且是本題余弦最高的一对（cos=0.4867），故替换前者。新选项的 enchant 1.0 对应「用两天自然就顺了」（信慢慢变好）。"),
    "s29": ("修正一", "题干「老板丢给你一个你完全没做过的任务，三天后要交」是外部强加的不利处境；五个选项全是主动应对，没有「不在意」落点。选项已满 5 个，须替换语义最重复的那一个：原（先做个粗糙版本，再一轮轮改）与（直接上手，边做边想，错了我再改）是同一个策略（先动手、边做边修），故替换前者，且保留后者可保住本題「快」的一端。新选项的 blink 1.0 = 「隔几天翻出来弄两下」（把同一件事反复捡起来），enchant 1.0 = 「慢慢就磨完了」（信慢慢变好）。"),
    "s30": ("修正一", "题干「三件急事同时压过来：客户在催、同事等你回话、自己的活还没动」是别人造成的不利处境；五个选项全是主动排序/处理，没有「不在意」。选项已满 5 个，须替换语义最重复的那一个：原（先重新定一遍三件事的截止时间，按我的表来）与（先把三件事写在便签上贴墙，做完一张撕一张）同属「把三件事列成一张表来管」（前者明说「按我的表来」）——本題所有两两余弦都 ≤0.29，重复性靠语义判断；保留便签那一条更具体，同时保住「挑最容易清掉」与「三件一起推」两端。新选项的 counters 1.0 = 「照旧一天天慢慢来」（长期投入、慢慢变强）。"),
    "h2c2": ("修正一", "题干「有人当面指出你选错了」是别人造成的、对你不利的处境（被否定）；五个选项全是主动反应（听/自己重推/当场认/翻账/存档），没有「无所谓 / 没往心里去」。选项已满 5 个，须替换语义最重复的那一个：原（先翻出当初的记录，看看是谁的建议）与（先把它收着，说不定哪天还能用上这段经验）同属「翻旧账 / 留存过去」，正是本題余弦最高的一对（cos=0.64）；保留后者是因为它的 counters 轴在本題唯一，前者的 politics 轴已由（先听他说完）承载。"),
    "s31": ("修正二", "题干末句「他问你要不要来」是会/不会倾向性问句。按去/不去分组：去 3 个（值 / 先兼职做 / 只干擅长的那块）、不去 1 个（不想动），3:1 超过 3:2。按规范改多数派里语义最重复的那一个：原（跟他讲清楚：我只干我擅长的那块，别的别找我）与（能不能先兼职做，别把现在的工作辞了）同属「有限参与、保住退路」，故改写为「不去」方向；改后 去 2 : 不去 2。新选项的 stax 1.5 对应「迟早要出事」（讨厌意外、不想被卷进失控的局）。"),
}

# 修正二 的极性分组：qid -> (A组名, B组名, A/B 在「改前」的下标, A/B 在「改后」的下标)
POLARITY = {
    "h2a3": ("会（还会回头改）", "不会", ([1, 2, 3, 4], [0]), ([1, 3, 4], [0, 2])),
    "s31": ("去（进这个项目）", "不去", ([0, 2, 4], [1]), ([0, 2], [1, 4])),
}


def vec(s):
    return [float(s.get(a, 0.0)) for a in AXES]


def cos(s1, s2):
    v1, v2 = vec(s1), vec(s2)
    n1 = math.sqrt(sum(x * x for x in v1))
    n2 = math.sqrt(sum(x * x for x in v2))
    if n1 == 0 or n2 == 0:
        return 0.0
    return sum(a * b for a, b in zip(v1, v2)) / (n1 * n2)


def opt_sig(o):
    return (o["t"], tuple(sorted((k, float(v)) for k, v in o["s"].items())), o.get("goto"))


def top_pair(q):
    best = (-1.0, None)
    for i in range(len(q["opts"])):
        for j in range(i + 1, len(q["opts"])):
            c = cos(q["opts"][i]["s"], q["opts"][j]["s"])
            if c > best[0]:
                best = (c, (i, j))
    return best


def main():
    problems, notes = [], []
    changed_all = []
    worst_global = (-1.0, None)

    for name, cur_p, old_p in FILES:
        cur = json.loads(cur_p.read_text(encoding="utf-8"))
        old = json.loads(old_p.read_text(encoding="utf-8"))
        cqs, oqs = cur["questions"], old["questions"]

        print("=" * 78)
        print(f"### {name}.json  batch={cur['batch']}（改前 {old['batch']}）  题数 {len(cqs)}（改前 {len(oqs)}）")
        if cur["batch"] != old["batch"]:
            problems.append(f"{name}: batch 号被改动")

        ids_same = [q["id"] for q in cqs] == [q["id"] for q in oqs]
        if not ids_same:
            problems.append(f"{name}: id 集合或顺序被改动")
        if len(cqs) != len(oqs):
            problems.append(f"{name}: 题数被改动")
        print("[检查1] id 集合与顺序一致：", "是 ✅" if ids_same and len(cqs) == len(oqs) else "否 ❌")

        next_bad, goto_bad, other_bad, changed = [], [], [], []
        for cq, oq in zip(cqs, oqs):
            qid = cq["id"]
            if cq.get("next") != oq.get("next"):
                next_bad.append((qid, oq.get("next"), cq.get("next")))
            if cq.get("q") != oq.get("q"):
                other_bad.append(f"{qid}: 题干被改动")
            if cq.get("sec") != oq.get("sec") or cq.get("kind") != oq.get("kind"):
                other_bad.append(f"{qid}: sec/kind 被改动")
            co, oo = cq["opts"], oq["opts"]
            if len(co) != len(oo):
                other_bad.append(f"{qid}: 选项数被改动（{len(oo)}→{len(co)}）")
                continue
            for i, (a, b) in enumerate(zip(co, oo)):
                if a.get("goto") != b.get("goto"):
                    goto_bad.append((qid, i, b.get("goto"), a.get("goto")))
                if opt_sig(a) != opt_sig(b):
                    changed.append((qid, i, b, a))
                    changed_all.append((name, qid, f"opt{i}", b["t"], a["t"], dict(b["s"]), dict(a["s"])))
        print("[检查2] next 无变化：", "是 ✅" if not next_bad else f"否 ❌ {next_bad}")
        print("[检查2] goto 无变化：", "是 ✅" if not goto_bad else f"否 ❌ {goto_bad}")
        if next_bad or goto_bad:
            problems.append(f"{name}: next/goto 被改动")
        print("[检查2附件] 题干/sec/kind/选项数：", "全部未变 ✅" if not other_bad else f"❌ {other_bad}")
        if other_bad:
            problems.append(f"{name}: " + "; ".join(other_bad))
        print(f"[附件] 本文件改动处：{len(changed)} 个选项" + ("" if changed else "（未改动）"))

        cnt_bad, axis_bad, weight_bad, dup_bad = [], [], [], []
        for q in cqs:
            qid, opts = q["id"], q["opts"]
            if not (3 <= len(opts) <= 5):
                cnt_bad.append((qid, len(opts)))
            texts = [o["t"] for o in opts]
            if len(set(texts)) != len(texts):
                dup_bad.append(qid)
            for i, o in enumerate(opts):
                s = o["s"]
                if not (1 <= len(s) <= 3):
                    axis_bad.append((qid, i, len(s)))
                for k, v in s.items():
                    if k not in AXES:
                        axis_bad.append((qid, i, f"未知轴 {k}"))
                    if float(v) not in WEIGHTS:
                        weight_bad.append((qid, i, k, v))
        print("\n[检查3] 每题选项数 3~5：", "全部通过 ✅" if not cnt_bad else f"❌ {cnt_bad}")
        print("[检查4] 每选项 1~3 个轴：", "全部通过 ✅" if not axis_bad else f"❌ {axis_bad}")
        print("[检查4] 权重 ∈ {1.0,1.5,2.0,2.5,3.0}：", "全部通过 ✅" if not weight_bad else f"❌ {weight_bad}")
        print("[检查6] 选项文本题内不重复：", "全部通过 ✅" if not dup_bad else f"❌ {dup_bad}")
        for cond, msg in ((cnt_bad, "选项数越界"), (axis_bad, "轴数/轴名异常"),
                          (weight_bad, "权重非法"), (dup_bad, "题内文本重复")):
            if cond:
                problems.append(f"{name}: {msg} {cond}")

        file_worst = (-1.0, None)
        bad_pairs = []
        for q in cqs:
            for i in range(len(q["opts"])):
                for j in range(i + 1, len(q["opts"])):
                    c = cos(q["opts"][i]["s"], q["opts"][j]["s"])
                    if c > file_worst[0]:
                        file_worst = (c, (q["id"], i, j, q["opts"][i]["t"], q["opts"][j]["t"]))
                    if c > worst_global[0]:
                        worst_global = (c, (name, q["id"], i, j, q["opts"][i]["t"], q["opts"][j]["t"]))
                    if c >= 0.85:
                        bad_pairs.append((q["id"], i, j, round(c, 4)))
        print("[检查5] 题内两两余弦 < 0.85：", "全部通过 ✅" if not bad_pairs else f"❌ {bad_pairs}")
        print(f"         本文件最高一对：cos={file_worst[0]:.4f}（题 {file_worst[1][0]} 选项{file_worst[1][1]}/{file_worst[1][2]}）")
        print(f"           「{file_worst[1][3]}」 vs 「{file_worst[1][4]}」")
        if bad_pairs:
            problems.append(f"{name}: 余弦越界 {bad_pairs}")

        print("\n--- 本文件改动清单 ---")
        if not changed:
            print("  （无：未命中修正一 / 修正二）")
        for qid, i, o, n in changed:
            kind = FIX_LOG.get(qid, ("未登记", ""))[0]
            print(f"  · {qid} 选项{i}  [{kind}]")
            print(f"      旧：{o['t']}   {json.dumps(o['s'], ensure_ascii=False)}")
            print(f"      新：{n['t']}   {json.dumps(n['s'], ensure_ascii=False)}")

    # ---------------- 汇总 ----------------
    print("\n" + "=" * 78)
    print("### 改动处统计")
    per_file = {}
    for name, qid, idx, ot, nt, os_, ns in changed_all:
        per_file.setdefault(name, []).append(qid)
    for name, _, _ in FILES:
        lst = per_file.get(name, [])
        print(f"  {name}.json：{len(lst)} 处" + (f"  -> {lst}" if lst else "  -> 无命中，未改动"))

    print("\n### 逐条改动清单（题号 / 修正类型 / 改了什么 / 为什么）")
    if not changed_all:
        print("（无）")
    for name, qid, idx, ot, nt, os_, ns in changed_all:
        kind, why = FIX_LOG.get(qid, ("未登记", ""))
        print(f"\n[{qid}]  {name}.json {idx}  —— {kind}")
        print(f"  旧选项：{ot}   {json.dumps(os_, ensure_ascii=False)}")
        print(f"  新选项：{nt}   {json.dumps(ns, ensure_ascii=False)}")
        print(f"  为什么：{why}")
    unlogged = [q for _, q, _, _, _, _, _ in changed_all if q not in FIX_LOG]
    if unlogged:
        problems.append(f"改动清单未登记：{unlogged}")

    print("\n### 全库最高余弦（bank1 + bank2，共 50 题）")
    print(f"  cos={worst_global[0]:.4f}  {worst_global[1][0]}.json 题 {worst_global[1][1]} 选项{worst_global[1][2]}/{worst_global[1][3]}")
    print(f"    「{worst_global[1][4]}」 vs 「{worst_global[1][5]}」")

    bank2_cur = json.loads((DATA / "bank2.json").read_text(encoding="utf-8"))
    bank2_old = json.loads((DATA / "_backup_bank2.json").read_text(encoding="utf-8"))
    cur_by_id = {q["id"]: q for q in bank2_cur["questions"]}
    old_by_id = {q["id"]: q for q in bank2_old["questions"]}

    print("\n### 附加复核 A：修正二 极性配平（改动前 → 改动后）")
    for qid, (la, lb, g_old, g_new) in POLARITY.items():
        for tag, by_id, (ga, gb) in (("改前", old_by_id, g_old), ("改后", cur_by_id, g_new)):
            q = by_id[qid]
            na, nb = len(ga), len(gb)
            ratio = max(na, nb) / max(1, min(na, nb))
            print(f"  [{qid}] {tag}（共 {len(q['opts'])} 个选项）：{la}={na}  {lb}={nb}  "
                  f"比例 {max(na, nb)}:{min(na, nb)} = {ratio:.2f} -> "
                  f"{'≤3:2 合格 ✅' if ratio <= 1.5 else '超过 3:2 ❌ 需配平'}")
            for i, o in enumerate(q["opts"]):
                grp = la if i in ga else (lb if i in gb else "中性/未分组")
                print(f"        {i} [{grp}] {o['t']}")

    print("\n### 附加复核 B：被改题目的最高余弦一对（改前 → 改后；←改 = 本次被替换的选项）")
    replaced = {}
    for _n, qid, idx, *_ in changed_all:
        replaced.setdefault(qid, []).append(int(idx.replace("opt", "")))
    for qid in sorted(replaced):
        for tag, by_id in (("改前", old_by_id), ("改后", cur_by_id)):
            q = by_id[qid]
            c, (i, j) = top_pair(q)
            mark = "  ←改" if tag == "改前" and (i in replaced[qid] or j in replaced[qid]) else ""
            print(f"  [{qid}] {tag}：cos={c:.4f}  选项{i}「{q['opts'][i]['t']}」 vs 选项{j}「{q['opts'][j]['t']}」{mark}")

    print("\n### 附加复核 C：轴覆盖（bank1+bank2 共 50 题；每轴被多少选项引用）")
    def coverage(banks):
        cnt = {a: 0 for a in AXES}
        for d in banks:
            for q in d["questions"]:
                for o in q["opts"]:
                    for k in o["s"]:
                        cnt[k] += 1
        return cnt
    old_banks = [json.loads((DATA / "_backup_bank1.json").read_text(encoding="utf-8")), bank2_old]
    cur_banks = [json.loads((DATA / "bank1.json").read_text(encoding="utf-8")), bank2_cur]
    cov_old, cov_cur = coverage(old_banks), coverage(cur_banks)
    for a in AXES:
        delta = "" if cov_old[a] == cov_cur[a] else f"   （{cov_old[a]} → {cov_cur[a]}）"
        print(f"  {a:<11}{cov_cur[a]}{delta}")

    print("\n### 附加复核 C2：bank2 单库轴覆盖 vs 门槛 12（check_bank2.py 的口径）")
    def cov_one(d):
        cnt = {a: 0 for a in AXES}
        for q in d["questions"]:
            for o in q["opts"]:
                for k in o["s"]:
                    cnt[k] += 1
        return cnt
    c_old, c_new = cov_one(bank2_old), cov_one(bank2_cur)
    low_old = sorted(a for a in AXES if c_old[a] < COVER_FLOOR)
    low_new = sorted(a for a in AXES if c_new[a] < COVER_FLOOR)
    print(f"  改前低于 {COVER_FLOOR} 的轴：{low_old if low_old else '无（全部 ≥' + str(COVER_FLOOR) + '）'}")
    print(f"  改后低于 {COVER_FLOOR} 的轴：{low_new if low_new else '无'}")
    print("  改前/改后逐轴（bank2 单库）：")
    for a in AXES:
        mark = " ⚠" if c_new[a] < COVER_FLOOR else ""
        print(f"    {a:<11}{c_old[a]:>4} → {c_new[a]:>4}{mark}")
    if low_new:
        notes.append(
            "bank2 单库有 " + str(len(low_new)) + " 个轴的引用数从 12 降到 11（" + ", ".join(low_new) +
            "），低于 check_bank2.py / QUESTION_SPEC §9 的单库门槛 12。原因是「选项已满 5 个时必须替换掉一个」"
            "会连带移走该选项的轴引用，而 bank2 原本恰好卡在 12 没有余量；voltron 与 ramp 在最常被判定为重复的"
            "那几个选项里都出现，无法用「不在意」类新选项补回。这属于本次修正的已知代价（不在任务的 6 项自检内），"
            "若要恢复门槛，需在 bank2 别处另补 1~3 个带这些轴的选项（超出「只做两类修正」的范围）。")

    print("\n### 汇总")
    if problems:
        print("  ❌ 存在问题：")
        for p in problems:
            print("    -", p)
        return 1
    print("  ✅ 6 项自检全部通过；除上面登记的改动外，两个文件没有任何其它变化。")
    for n in notes:
        print("  ⚠ 附注（非 6 项自检内容）：", n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
