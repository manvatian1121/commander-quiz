#!/usr/bin/env python3
"""bank4.json 自检（batch 4：主线 s49~s64 + 枢纽 s56 + 分支 h4a/h4b/h4c）。

跑法：python check_bank4.py
共 10 项检查，全部逐条打印 PASS/FAIL，末尾给总结。
"""
from __future__ import annotations

import json
import math
import pathlib
import re
import sys
from collections import Counter, deque



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(ROOT)
BANK = ROOT / "data" / "bank4.json"

AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]
COLORS = ["W", "U", "B", "R", "G"]
OK_WEIGHTS = {1.0, 1.5, 2.0, 2.5, 3.0}

MAINLINE = [f"s{i:02d}" for i in range(49, 65)]          # s49 ~ s64
BRANCHES = {c: [f"h4{c}{n}" for n in (1, 2, 3)] for c in "abc"}
EXPECTED_IDS = set(MAINLINE) | {q for v in BRANCHES.values() for q in v}
HUB = "s56"
HUB_GOTO = {"h4a1", "h4b1", "h4c1"}
BRANCH_RETURN = "s57"
EXTERNAL_NEXT = "s65"                                     # 交给 batch 5

# 轴 → 颜色（color pie 近似映射，用于第二口径的颜色覆盖统计）
AXIS_COLORS = {
    "aggro": ["R"], "voltron": ["W", "R"], "wide": ["W", "G"], "ramp": ["G"],
    "stompy": ["G"], "control": ["U"], "removal": ["W", "B"], "combo": ["U", "B"],
    "spells": ["U", "R"], "artifacts": ["U"], "enchant": ["W", "G"], "grave": ["B"],
    "tribal": ["G", "W"], "drain": ["B"], "stax": ["W", "B"], "clonesteal": ["U"],
    "politics": ["W", "U"], "chaos": ["R"], "counters": ["G", "U"], "blink": ["U", "W"],
}

# 万智牌术语黑名单（命中即失败）
BANNED = [
    "主将", "指挥官", "牌组", "套牌", "卡牌", "牌库", "手牌", "抽牌", "卡差",
    "咒语", "法术力", "法术", "瞬间", "结界", "灵气", "神器", "生物", "衍生",
    "永久物", "召唤", "铺场", "铺开场面", "反击", "坟场", "闪现", "触发",
    "指示物", "增殖", "偷取", "复制", "法术力费", "出场费", "费用", "色组",
    "双色", "五色", "万智", "Bracket", "EDH", "Commander", "地牌", "基本地",
    "回合", "对局", "竞技", "赛制", "起手", "场面", "铺场", "锁场",
]
# 需要人工判断的模糊词（只报告，不算失败）
SOFT = ["牌", "坟", "灵", "锁"]

state = {"pass": 0, "fail": 0, "notes": []}


def report(no: int, title: str, ok: bool, lines: list[str]) -> None:
    state["pass" if ok else "fail"] += 1
    print(f"\n[{no}] {'PASS' if ok else 'FAIL'}  {title}")
    for line in lines:
        print(f"      {line}")


def main() -> int:
    raw = BANK.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except Exception as exc:  # noqa: BLE001
        print(f"[1] FAIL  JSON 解析失败：{exc}")
        return 1

    questions = data["questions"]
    by_id = {q["id"]: q for q in questions}

    # ---------------------------------------------------------------- 1
    ids = [q["id"] for q in questions]
    dup = [i for i, n in Counter(ids).items() if n > 1]
    missing = EXPECTED_IDS - set(ids)
    extra = set(ids) - EXPECTED_IDS
    ok1 = not dup and not missing and not extra and len(questions) == 25
    report(1, "JSON 合法 / id 唯一且为 s49~s64 + h4*9", ok1, [
        f"batch={data.get('batch')}  题数={len(questions)}（期望 25）",
        f"重复 id={dup or '无'}  缺失={sorted(missing) or '无'}  多余={sorted(extra) or '无'}",
    ])

    # ---------------------------------------------------------------- 2
    no_next = [q["id"] for q in questions if "next" not in q]
    null_next = [q["id"] for q in questions if q.get("next", "") is None]
    ok2 = not no_next
    report(2, "每题都有 next 字段", ok2, [
        f"缺 next 的题={no_next or '无'}（本 batch 无末题，故不应出现 null；实际 null={null_next or '无'}）",
    ])

    # ---------------------------------------------------------------- 3
    gotos = [(q["id"], o["goto"]) for q in questions for o in q["opts"] if "goto" in o]
    bad_goto = [(qid, g) for qid, g in gotos if g not in by_id]
    ok3 = not bad_goto
    report(3, "所有 goto 都指向存在的 id", ok3, [
        f"goto 总数={len(gotos)}（枢纽 s56 的 3 个选项 + 其余 {len(gotos) - 3} 个）",
        f"越界 goto={bad_goto or '无'}",
    ])

    # ---------------------------------------------------------------- 4
    lines4: list[str] = []
    ok4 = True
    # 4a 主线按 next 走通 s49 → s64 → s65（s65 属于 batch 5，只看衔接）
    walk, cur, guard = [], "s49", 0
    while cur in by_id and guard < 200:
        walk.append(cur)
        cur = by_id[cur].get("next")
        guard += 1
    expect_walk = MAINLINE
    if walk != expect_walk or cur != EXTERNAL_NEXT:
        ok4 = False
        lines4.append(f"✗ 主线链断裂：{' → '.join(walk)} 出口 next={cur}（期望 {EXTERNAL_NEXT}）")
    else:
        lines4.append(f"✓ 主线 next 链：{' → '.join(walk)} →(next) {cur}（{len(MAINLINE)} 题）")
    # 4b 三条分支各 3 题并回归 s57
    for letter, chain in BRANCHES.items():
        if chain[0] not in {o.get("goto") for o in by_id[HUB]["opts"]}:
            ok4 = False
            lines4.append(f"✗ 枢纽 s56 没有选项 goto {chain[0]}")
            continue
        seq, node = [], chain[0]
        for _ in chain:                       # 只走 3 步，第 4 跳必须是回归点
            seq.append(node)
            node = by_id[node].get("next")
        if seq != chain or node != BRANCH_RETURN:
            ok4 = False
            lines4.append(f"✗ 分支 {letter}：{seq} 结尾 next={node}（期望 {' → '.join(chain)} 结尾 {BRANCH_RETURN}）")
        else:
            lines4.append(f"✓ 分支 {letter}：{' → '.join(chain)} →(next) {BRANCH_RETURN}")
    # 4c 可达性：从 s49 出发，next + goto 能覆盖本 batch 全部 25 题
    seen, dq = {"s49"}, deque(["s49"])
    while dq:
        q = by_id.get(dq.popleft())
        if not q:
            continue
        targets = [o["goto"] for o in q["opts"] if "goto" in o]
        nxt = q.get("next")
        if nxt in by_id:
            targets.append(nxt)
        for t in targets:
            if t in by_id and t not in seen:
                seen.add(t)
                dq.append(t)
    unreachable = sorted(EXPECTED_IDS - seen)
    if unreachable:
        ok4 = False
    lines4.append(f"{'✓' if not unreachable else '✗'} 从 s49 可达 {len(seen)}/25 题，不可达={unreachable or '无'}")
    report(4, "跳转链：主线 + 三分支 + 分支回归 s57 + 全题可达", ok4, lines4)

    # ---------------------------------------------------------------- 5
    bad_opt = []
    for q in questions:
        opts = q["opts"]
        if not 3 <= len(opts) <= 5:
            bad_opt.append(f"{q['id']} 选项数={len(opts)}")
        texts = [o.get("t", "") for o in opts]
        if any(not t.strip() for t in texts):
            bad_opt.append(f"{q['id']} 有空选项")
        if len(set(texts)) != len(texts):
            bad_opt.append(f"{q['id']} 选项文本重复")
    ok5 = not bad_opt
    opt_total = sum(len(q["opts"]) for q in questions)
    report(5, "每题 3~5 个选项 / 文本非空 / 两两不同", ok5, [
        f"选项总数={opt_total}，各题选项数={' '.join(str(len(q['opts'])) for q in questions)}",
        f"问题={bad_opt or '无'}",
    ])

    # ---------------------------------------------------------------- 6
    bad_s = []
    ref_total = 0
    for q in questions:
        for i, o in enumerate(q["opts"], 1):
            s = o.get("s") or {}
            ref_total += len(s)
            if not 1 <= len(s) <= 3:
                bad_s.append(f"{q['id']} 选项{i} 轴数={len(s)}")
            for axis, w in s.items():
                if axis not in AXES:
                    bad_s.append(f"{q['id']} 选项{i} 未知轴 {axis}")
                if float(w) not in OK_WEIGHTS:
                    bad_s.append(f"{q['id']} 选项{i} 非法权重 {axis}={w}")
            for c, w in (o.get("col") or {}).items():
                if c not in COLORS:
                    bad_s.append(f"{q['id']} 选项{i} 未知颜色 {c}")
                if float(w) not in OK_WEIGHTS:
                    bad_s.append(f"{q['id']} 选项{i} 非法颜色权重 {c}={w}")
    ok6 = not bad_s
    report(6, "每选项 1~3 个轴，权重只用 1.0/1.5/2.0/2.5/3.0", ok6, [
        f"轴得分条目总数={ref_total}，平均每选项 {ref_total / opt_total:.2f} 个",
        f"问题={bad_s or '无'}",
    ])

    # ---------------------------------------------------------------- 7
    violations, worst = [], []
    for q in questions:
        opts = q["opts"]
        for i in range(len(opts)):
            for j in range(i + 1, len(opts)):
                a, b = opts[i].get("s") or {}, opts[j].get("s") or {}
                keys = set(a) | set(b)
                dot = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
                na = math.sqrt(sum(a.get(k, 0) ** 2 for k in keys))
                nb = math.sqrt(sum(b.get(k, 0) ** 2 for k in keys))
                cos = dot / (na * nb) if na and nb else 0.0
                # 交叉口径：把 col 也算进向量
                ca = dict(a, **{f"col:{k}": v for k, v in (opts[i].get("col") or {}).items()})
                cb = dict(b, **{f"col:{k}": v for k, v in (opts[j].get("col") or {}).items()})
                keys2 = set(ca) | set(cb)
                dot2 = sum(ca.get(k, 0) * cb.get(k, 0) for k in keys2)
                na2 = math.sqrt(sum(ca.get(k, 0) ** 2 for k in keys2))
                nb2 = math.sqrt(sum(cb.get(k, 0) ** 2 for k in keys2))
                cos2 = dot2 / (na2 * nb2) if na2 and nb2 else 0.0
                worst.append((max(cos, cos2), q["id"], i + 1, j + 1, cos, cos2))
                if cos >= 0.85 or cos2 >= 0.85:
                    violations.append((q["id"], i + 1, opts[i]["t"][:14], j + 1,
                                       opts[j]["t"][:14], round(cos, 3), round(cos2, 3)))
    worst.sort(reverse=True)
    ok7 = not violations
    report(7, "题内任意两选项轴向量余弦相似度 < 0.85", ok7, [
        f"超标组合={len(violations)}",
        *[f"✗ {v[0]} 选项{v[1]}「{v[2]}…」× 选项{v[3]}「{v[4]}…」 纯轴={v[5]} 含颜色={v[6]}"
          for v in violations],
        "最接近上限的 5 组（纯轴 / 含颜色）：",
        *[f"  {w[1]} 选项{w[2]}×{w[3]}  {w[4]:.3f} / {w[5]:.3f}" for w in worst[:5]],
    ])

    # ---------------------------------------------------------------- 8
    axis_hits: Counter = Counter()
    axis_examples: dict[str, list[str]] = {a: [] for a in AXES}
    for q in questions:
        for o in q["opts"]:
            for axis in (o.get("s") or {}):
                axis_hits[axis] += 1
                if len(axis_examples[axis]) < 4:
                    axis_examples[axis].append(q["id"])
    weak = [a for a in AXES if axis_hits.get(a, 0) < 12]
    ok8 = not weak
    report(8, "20 个轴各被 ≥12 个选项引用", ok8, [
        f"{a:<11}{axis_hits.get(a, 0):>3}  {' '.join(axis_examples[a])}"
        + ("" if axis_hits.get(a, 0) >= 12 else "   ← 不足")
        for a in AXES
    ] + [f"低于 12 的轴={weak or '无'}"])

    # ---------------------------------------------------------------- 9
    hits_hard, hits_soft = [], []
    for q in questions:
        for i, o in enumerate(q["opts"], 1):
            text = o.get("t", "")
            for w in BANNED:
                if w in text:
                    hits_hard.append(f"{q['id']} 选项{i} 命中「{w}」：{text}")
            for w in SOFT:
                if w in text:
                    hits_soft.append(f"{q['id']} 选项{i} 含「{w}」（需人工判断）：{text}")
        for w in BANNED:
            if w in q["q"]:
                hits_hard.append(f"{q['id']} 题干命中「{w}」：{q['q']}")
    ok9 = not hits_hard
    report(9, "选项/题干无万智牌术语（关键词扫描）", ok9, [
        f"扫描关键词 {len(BANNED)} 个：{'、'.join(BANNED[:12])}…（共 {len(BANNED)}）",
        f"硬命中={hits_hard or '无'}",
        f"软提示（通用词，人工判断）={hits_soft or '无'}",
    ])

    # ---------------------------------------------------------------- 10
    col_explicit: Counter = Counter()
    col_derived: Counter = Counter()
    col_examples: dict[str, list[str]] = {c: [] for c in COLORS}
    for q in questions:
        for o in q["opts"]:
            for c in (o.get("col") or {}):
                col_explicit[c] += 1
                if len(col_examples[c]) < 4:
                    col_examples[c].append(f"{q['id']}(标注)")
            implied = set()
            for axis in (o.get("s") or {}):
                implied.update(AXIS_COLORS.get(axis, []))
            for c in implied:
                col_derived[c] += 1
                if len(col_examples[c]) < 6:
                    col_examples[c].append(f"{q['id']}(由轴)")
    flat = {c: col_explicit.get(c, 0) for c in COLORS}
    weak_col = [c for c in COLORS if col_explicit.get(c, 0) < 4]
    weak_col2 = [c for c in COLORS if col_derived.get(c, 0) < 4]
    ok10 = not weak_col and not weak_col2
    report(10, "五种颜色各被 ≥4 个选项提及", ok10, [
        f"显式 col 标注口径：{json.dumps(flat, ensure_ascii=False)}",
        f"由轴推导口径（color pie 映射）：{json.dumps({c: col_derived.get(c, 0) for c in COLORS}, ensure_ascii=False)}",
        *[f"  {c}: 标注 {col_explicit.get(c, 0)} / 推导 {col_derived.get(c, 0)}  例：{'、'.join(col_examples[c][:6])}"
          for c in COLORS],
        f"不足（标注口径）={weak_col or '无'}  不足（推导口径）={weak_col2 or '无'}",
    ])

    # ------------------------------------------------------------------ 汇总
    print("\n" + "=" * 66)
    print(f"结果：{state['pass']} 项通过 / {state['fail']} 项失败")
    print(f"题数 {len(questions)}  选项 {opt_total}  轴得分条目 {ref_total}")
    print("全部通过 ✓" if state["fail"] == 0 else "存在失败项 ✗")
    return 0 if state["fail"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
