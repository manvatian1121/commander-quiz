#!/usr/bin/env python3
"""bank5.json 选项配平修正后的 8 项自检（对照修改前备份）。

用法：
    python fix_check_5.py
    python fix_check_5.py --bank <改后文件> --back <改前备份>

检查项（与任务书一致）：
  1. id 集合与修改前完全一致
  2. 所有 next / goto 没变
  3. 每题选项数 3~5
  4. 每个选项 1~3 个轴、权重 ∈ {1.0, 1.5, 2.0, 2.5, 3.0}
  5. 每题内两两选项余弦 < 0.85（列出全库最高的一对及数值）
  6. 选项文本在题内不重复
  7. s75~s80 的 multi 字段保持不变
  8. s70 枢纽题的 3 个 goto 不变

附加（不进退出码）：
  A. 逐字段全量 diff（确认除本次有意改动外没有任何其它变化）
  B. 极性统计（会/不会 等）→ 验证 4:1 已配平到 3:2
  C. 20 轴覆盖（QUESTION_SPEC 第 9 条要求每轴 ≥ 12 个选项）
  D. 同选项内反向双高权重（沿用 check_bank5_axes.py 口径）
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys
from collections import Counter



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

DATA = pathlib.Path(ROOT / "data")
AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]
WEIGHTS = {1.0, 1.5, 2.0, 2.5, 3.0}
MULTI_IDS = [f"s{n}" for n in range(75, 81)]
HUB_ID = "s70"

OPPOSED = [("aggro", "control"), ("aggro", "drain"), ("aggro", "stax"),
           ("chaos", "control"), ("chaos", "stax"), ("chaos", "ramp"),
           ("wide", "voltron"), ("wide", "stompy"), ("combo", "stompy"),
           ("blink", "aggro"), ("drain", "stompy"), ("politics", "stompy"),
           ("enchant", "chaos"), ("counters", "chaos")]

POLARITY_PREFIX = ["不会", "不是", "没有", "不喜欢", "会", "是", "有", "喜欢"]

FAIL: list[str] = []


def fail(item: str, msg: str) -> None:
    FAIL.append(f"[{item}] {msg}")


def cosine(a: dict, b: dict) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def load(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", default=str(DATA / "bank5.json"))
    ap.add_argument("--back", default=str(DATA / "bank5.json.bak"))
    args = ap.parse_args()

    bank_path, back_path = pathlib.Path(args.bank), pathlib.Path(args.back)
    print(f"改后文件：{bank_path}")
    print(f"改前备份：{back_path}")
    now, before = load(bank_path), load(back_path)
    q_now = now["questions"]
    q_before = before["questions"]
    by_now = {q["id"]: q for q in q_now}
    by_before = {q["id"]: q for q in q_before}

    print(f"batch：改后 {now.get('batch')} / 改前 {before.get('batch')}")
    print(f"题数：改后 {len(q_now)} / 改前 {len(q_before)}")
    print("=" * 68)

    # ---------------- 1. id 集合 ----------------
    ids_now, ids_before = [q["id"] for q in q_now], [q["id"] for q in q_before]
    same_set = set(ids_now) == set(ids_before)
    same_order = ids_now == ids_before
    print(f"[1] id 集合与修改前一致：{'✓' if same_set else '✗'}")
    print(f"    顺序也一致：{'✓' if same_order else '✗'}"
          f"{'' if same_order else f'  改后={ids_now}  改前={ids_before}'}")
    print(f"    集合：{len(ids_now)} 个，只多 = {sorted(set(ids_now) - set(ids_before))}，"
          f"只少 = {sorted(set(ids_before) - set(ids_now))}")
    if not same_set:
        fail("1", f"id 集合变化：多 {sorted(set(ids_now) - set(ids_before))}，"
                  f"少 {sorted(set(ids_before) - set(ids_now))}")
    if not same_order:
        fail("1", "id 顺序变化")

    # ---------------- 2. next / goto ----------------
    bad_next, bad_goto = [], []
    for qid in ids_before:
        if qid not in by_now:
            continue
        nb, nn = by_before[qid].get("next", "<缺>"), by_now[qid].get("next", "<缺>")
        if nb != nn:
            bad_next.append(f"{qid}: {nb!r} → {nn!r}")
        ob, on = by_before[qid]["opts"], by_now[qid]["opts"]
        if len(ob) != len(on):
            bad_goto.append(f"{qid}: 选项数 {len(ob)} → {len(on)}（逐个比对跳过）")
            continue
        for i, (a, b) in enumerate(zip(ob, on), 1):
            gb, gn = a.get("goto", "<无>"), b.get("goto", "<无>")
            if gb != gn:
                bad_goto.append(f"{qid} 选项{i}: goto {gb!r} → {gn!r}")
    total_links = len(ids_now)
    print(f"\n[2] next / goto 全部未变：{'✓' if not bad_next and not bad_goto else '✗'}")
    print(f"    next 比对 {total_links} 题，差异 {len(bad_next)} 处"
          f"{'：' + str(bad_next) if bad_next else ''}")
    print(f"    goto 比对 123 个选项位置，差异 {len(bad_goto)} 处"
          f"{'：' + str(bad_goto) if bad_goto else ''}")
    if bad_next:
        fail("2", f"next 变化 {bad_next}")
    if bad_goto:
        fail("2", f"goto 变化 {bad_goto}")

    # ---------------- 3. 选项数 ----------------
    counts = Counter(len(q["opts"]) for q in q_now)
    bad3 = [f"{q['id']}={len(q['opts'])}" for q in q_now if not 3 <= len(q["opts"]) <= 5]
    print(f"\n[3] 每题选项数 3~5：{'✓' if not bad3 else '✗ ' + str(bad3)}")
    print(f"    分布：{dict(sorted(counts.items()))}（题目 {len(q_now)}，选项合计 "
          f"{sum(len(q['opts']) for q in q_now)}）")
    if bad3:
        fail("3", f"选项数越界：{bad3}")

    # ---------------- 4. 轴数与权重 ----------------
    bad4 = []
    for q in q_now:
        for i, o in enumerate(q["opts"], 1):
            s = o.get("s") or {}
            if not 1 <= len(s) <= 3:
                bad4.append(f"{q['id']} 选项{i} 轴数 {len(s)}")
            for axis, w in s.items():
                if axis not in AXES:
                    bad4.append(f"{q['id']} 选项{i} 未知轴 {axis}")
                if w not in WEIGHTS:
                    bad4.append(f"{q['id']} 选项{i} 非法权重 {w}")
    print(f"\n[4] 每选项 1~3 轴、权重 ∈ {{1.0,1.5,2.0,2.5,3.0}}："
          f"{'✓' if not bad4 else '✗ ' + str(bad4)}")
    total_opts = sum(len(q["opts"]) for q in q_now)
    wc = Counter(w for q in q_now for o in q["opts"] for w in o["s"].values())
    print(f"    受检选项 {total_opts} 个，轴引用 {sum(wc.values())} 次；"
          f"权重分布 {dict(sorted(wc.items()))}")
    print(f"    本次改动的 s68 选项4：{by_now['s68']['opts'][3]['s']}（2 轴）")
    if bad4:
        fail("4", f"轴/权重非法：{bad4}")

    # ---------------- 5. 题内两两余弦 ----------------
    pairs: list[tuple[float, str]] = []
    over: list[tuple[float, str]] = []
    for q in q_now:
        opts = q["opts"]
        for i in range(len(opts)):
            for j in range(i + 1, len(opts)):
                c = cosine(opts[i]["s"], opts[j]["s"])
                tag = f"{q['id']} 选项{i + 1}×{j + 1}"
                pairs.append((c, tag))
                if c >= 0.85:
                    over.append((c, tag))
    pairs.sort(reverse=True)
    print(f"\n[5] 题内两两余弦 < 0.85：{'✓' if not over else '✗ ' + str([t for _, t in over])}")
    print(f"    受检 {len(pairs)} 组；**全库最高的一对：{pairs[0][1]}  cos={pairs[0][0]:.3f}**")
    print("    前 6 高：")
    for c, tag in pairs[:6]:
        print(f"      {'✗' if c >= 0.85 else '✓'} {tag:<22} cos={c:.3f}")
    if over:
        fail("5", f"{len(over)} 组余弦 ≥ 0.85：{[t for _, t in over]}")

    # ---------------- 6. 题内选项文本不重复 ----------------
    bad6 = []
    for q in q_now:
        texts = [o.get("t", "") for o in q["opts"]]
        if any(not t.strip() for t in texts):
            bad6.append(f"{q['id']} 有空选项")
        dup = [t for t, c in Counter(texts).items() if c > 1]
        if dup:
            bad6.append(f"{q['id']} 重复 {dup}")
    print(f"\n[6] 选项文本题内不重复：{'✓' if not bad6 else '✗ ' + str(bad6)}"
          f"（{total_opts} 个选项全查）")
    if bad6:
        fail("6", f"文本重复：{bad6}")

    # ---------------- 7. s75~s80 multi ----------------
    print("\n[7] s75~s80 的 multi 字段保持不变：")
    bad7 = []
    for qid in MULTI_IDS:
        mb, mn = by_before[qid].get("multi"), by_now[qid].get("multi")
        flag = "✓" if mb == mn else "✗"
        print(f"    {flag} {qid} multi {mb} → {mn}")
        if mb != mn:
            bad7.append(f"{qid}: {mb} → {mn}")
    print(f"    multi 全场: {[by_now[q]['multi'] for q in MULTI_IDS]}"
          f"（改前 {[by_before[q]['multi'] for q in MULTI_IDS]}）"
          f"  {'✓' if not bad7 else '✗'}")
    if bad7:
        fail("7", f"multi 变化：{bad7}")

    # ---------------- 8. s70 枢纽 goto ----------------
    gb = [o.get("goto") for o in by_before[HUB_ID]["opts"]]
    gn = [o.get("goto") for o in by_now[HUB_ID]["opts"]]
    ok8 = gb == gn and len(gn) == 3 and len(set(gn)) == 3 and None not in gn
    print(f"\n[8] s70 枢纽 3 个 goto 不变：{'✓' if ok8 else '✗'}")
    print(f"    改前 {gb}")
    print(f"    改后 {gn}   kind={by_now[HUB_ID].get('kind')!r}")
    if not ok8:
        fail("8", f"s70 goto 变化：{gb} → {gn}")

    # ---------------- 附加 A. 全量 diff ----------------
    print("\n" + "=" * 68)
    print("附加 A：逐字段全量 diff（改前 → 改后）")
    diffs: list[str] = []
    for qid in ids_before:
        if qid not in by_now:
            continue
        qb, qn = by_before[qid], by_now[qid]
        for field in ("sec", "q", "kind", "multi"):
            vb, vn = qb.get(field, "<缺>"), qn.get(field, "<缺>")
            if vb != vn:
                diffs.append(f"{qid}.{field}: {vb!r} → {vn!r}")
        ob, on = qb["opts"], qn["opts"]
        if len(ob) != len(on):
            diffs.append(f"{qid}.opts 数量: {len(ob)} → {len(on)}")
            continue
        for i, (a, b) in enumerate(zip(ob, on), 1):
            if a.get("t") != b.get("t"):
                diffs.append(f"{qid} 选项{i} 文本:\n      改前「{a.get('t')}」\n"
                             f"      改后「{b.get('t')}」")
            if a.get("s") != b.get("s"):
                diffs.append(f"{qid} 选项{i} 轴得分: {a.get('s')} → {b.get('s')}")
    if diffs:
        for d in diffs:
            print(f"    Δ {d}")
    else:
        print("    （无差异）")
    print(f"    合计差异条目：{len(diffs)}")
    expected_diff_items = 2  # s68 选项4 的文本 + 轴得分
    if len(diffs) != expected_diff_items:
        print(f"    ⚠ 预期只有 s68 选项4 的「文本 + 轴得分」共 {expected_diff_items} 条，"
              f"实际 {len(diffs)} 条")

    # ---------------- 附加 B. 极性统计 ----------------
    print("\n附加 B：选项极性统计（仅在选项以 会/不会 等开头时计数）")
    for q in q_now:
        tally: Counter = Counter()
        for o in q["opts"]:
            for p in POLARITY_PREFIX:
                if o["t"].startswith(p):
                    tally[p] += 1
                    break
        if sum(tally.values()) >= 3:
            pos = tally["会"] + tally["是"] + tally["有"] + tally["喜欢"]
            neg = tally["不会"] + tally["不是"] + tally["没有"] + tally["不喜欢"]
            print(f"    {q['id']}「{q['q']}」→ 正 {pos} : 负 {neg}"
                  f"   {'✓ 在 3:2 内' if pos <= 3 and neg >= 2 or neg <= 3 and pos >= 2 else '✗ 悬殊'}")
    s68 = by_now["s68"]["opts"]
    n_pos = sum(1 for o in s68 if o["t"].startswith("会"))
    n_neg = sum(1 for o in s68 if o["t"].startswith("不会"))
    print(f"    s68 明细：会 {n_pos} 个 / 不会 {n_neg} 个 → {n_pos}:{n_neg}"
          f"   {'✓' if n_pos <= 3 and n_neg >= 2 else '✗'}（题干：「{by_now['s68']['q']}」）")

    # ---------------- 附加 C. 20 轴覆盖 ----------------
    hits: Counter = Counter()
    for q in q_now:
        for o in q["opts"]:
            for axis in o["s"]:
                hits[axis] += 1
    weak = [f"{a}({hits.get(a, 0)})" for a in AXES if hits.get(a, 0) < 12]
    print(f"\n附加 C：20 轴覆盖（要求每轴 ≥ 12 个选项）："
          f"{'✓ 全部达标' if not weak else '✗ ' + str(weak)}")
    print("    " + "  ".join(f"{a}:{hits.get(a, 0)}" for a in AXES))

    # ---------------- 附加 D. 同选项内反向双高 ----------------
    opp = [f"{q['id']} 选项{i} {a}+{b} {o['s']}"
           for q in q_now for i, o in enumerate(q["opts"], 1)
           for a, b in OPPOSED
           if o["s"].get(a, 0) >= 2.0 and o["s"].get(b, 0) >= 2.0]
    print(f"\n附加 D：同选项内反向双高权重：{'✓ 0 处' if not opp else '✗ ' + str(opp)}")

    # ---------------- 汇总 ----------------
    print("\n" + "=" * 68)
    if FAIL:
        print(f"✗ 8 项自检未通过 {len(FAIL)} 项：")
        for f in FAIL:
            print(f"  {f}")
        return 1
    print("✓ 8 项自检全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
