#!/usr/bin/env python3
"""校验新题库：结构、跳转链、可达性、无环、选项模糊度、轴覆盖、无万智术语。"""
from __future__ import annotations

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
COLORS = ["W", "U", "B", "R", "G"]
# 广度题的无色选项用 "C" 表达「想要无色主将」的偏好。
# 它不参与五色覆盖统计（无色不是五色之一），所以单独列出。
COLOR_EXTRA = ["C"]
CVALS = ["complex", "budget", "salt"]
# 权重经过轴平衡缩放后是连续值，不再是固定档位
W_MIN, W_MAX = 0.3, 3.0

# 禁止出现在性格题里的万智牌术语
JARGON = ["主将", "牌组", "套牌", "咒语", "铺场", "反击", "坟场", "生物", "法术力",
          "地牌", "结界", "神器", "衍生物", "指示物", "组合技", "万智", "卡牌",
          "牌库", "手牌", "召唤"]

AMBIGUITY_LIMIT = 0.85
MIN_AXIS_OPTIONS = 12
MIN_COLOR_OPTIONS = 4


def cosine(a: dict, b: dict) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(a.get(k, 0.0) ** 2 for k in keys))
    nb = math.sqrt(sum(b.get(k, 0.0) ** 2 for k in keys))
    return dot / (na * nb) if na and nb else 0.0


def main() -> int:
    payload = json.loads((DATA / "questions.json").read_text(encoding="utf-8"))
    questions = payload["questions"]
    by_id = {q["id"]: q for q in questions}
    start = payload["start"]
    problems: list[str] = []
    warnings: list[str] = []

    print(f"题库 {len(questions)} 题，起始题 {start}")

    # --- 结构 ---
    ids = [q["id"] for q in questions]
    dupes = [i for i, n in Counter(ids).items() if n > 1]
    if dupes:
        problems.append(f"id 重复：{dupes}")

    for q in questions:
        if "next" not in q:
            problems.append(f"{q['id']} 缺 next 字段")
        nxt = q.get("next")
        if nxt and nxt not in by_id:
            problems.append(f"{q['id']}.next 指向不存在的 {nxt}")
        for opt in q["opts"]:
            goto = opt.get("goto")
            if goto and goto not in by_id:
                problems.append(f"{q['id']} 的选项 goto 指向不存在的 {goto}")
        if q.get("kind") in ("hub", "gate"):
            # 枢纽题允许部分选项不带 goto：那表示「这条路径不深入分支，直接走 next」。
            # 但至少要有一个分支入口，且所有分支题必须可达（由下面的可达性检查兜底）。
            if not any(o.get("goto") for o in q["opts"]):
                problems.append(f"枢纽题 {q['id']} 一个分支入口都没有")

    # --- 主线走通 ---
    spine, cursor, guard = [], start, 0
    while cursor and guard < 1000:
        spine.append(cursor)
        cursor = by_id[cursor].get("next") if cursor in by_id else None
        guard += 1
    if cursor:
        problems.append("主线没有终点（next 链条未以 null 结束），可能存在环")
    print(f"主线 {len(spine)} 题（{spine[0]} → {spine[-1]}）")

    # --- 可达性 ---
    reachable, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node in reachable or node not in by_id:
            continue
        reachable.add(node)
        q = by_id[node]
        outs = [o["goto"] for o in q["opts"] if o.get("goto")] or [q.get("next")]
        for t in outs:
            if t:
                stack.append(t)
    orphans = sorted(set(ids) - reachable)
    if orphans:
        problems.append(f"从起点走不到的孤立题 {len(orphans)} 道：{orphans[:10]}")

    # --- 环检测 ---
    WHITE, GREY, BLACK = 0, 1, 2
    color = {qid: WHITE for qid in ids}
    cycles: list[str] = []

    def visit(node: str, path: list[str]) -> None:
        if node not in by_id:
            return
        if color[node] == GREY:
            cycles.append(" → ".join(path + [node]))
            return
        if color[node] == BLACK:
            return
        color[node] = GREY
        q = by_id[node]
        outs = [o["goto"] for o in q["opts"] if o.get("goto")] or [q.get("next")]
        for t in outs:
            if t:
                visit(t, path + [node])
        color[node] = BLACK

    for qid in ids:
        if color[qid] == WHITE:
            visit(qid, [])
    if cycles:
        problems.append(f"存在环 {len(cycles)} 处（会导致死循环）：{cycles[:3]}")

    # --- 选项 ---
    axis_hits: Counter = Counter()
    color_hits: Counter = Counter()
    cval_hits: Counter = Counter()
    section_counts: Counter = Counter()
    ambiguous: list[str] = []

    for q in questions:
        section_counts[q.get("sec")] += 1
        opts = q["opts"]
        # 上限放到 7：广度题要覆盖 单色/双色/三色/四色/五色/无色 六档；
        # s50（周末看什么）在原有六类之外补一档「恐怖片」，六档不够装，故再放宽一档。
        # 放宽的只有条数上限：下限 3、每选项 1~3 轴、权重区间、
        # 同题两两余弦 < AMBIGUITY_LIMIT 都不放松——选项一多本来就更容易互相模糊，
        # 区分度由那条余弦阈值兜住，而不是靠压条数。
        if not (3 <= len(opts) <= 7):
            problems.append(f"{q['id']} 选项数 {len(opts)}（要求 3~7）")
        texts = [o["t"].strip() for o in opts]
        if any(not t for t in texts):
            problems.append(f"{q['id']} 有空选项")
        if len(set(texts)) != len(texts):
            problems.append(f"{q['id']} 有重复选项文本")

        for index, opt in enumerate(opts):
            scores = opt.get("s") or {}
            # 门槛题（gate）的选项只用来切换评分标准，天然没有轴得分
            is_gate = q.get("kind") == "gate"
            if not is_gate and not (1 <= len(scores) <= 3):
                problems.append(f"{q['id']} 选项{index + 1} 轴得分 {len(scores)} 个（要求 1~3）")
            if is_gate and len(scores) > 3:
                problems.append(f"{q['id']} 选项{index + 1} 轴得分超过 3 个")
            for axis, value in scores.items():
                if axis not in AXES:
                    problems.append(f"{q['id']} 选项{index + 1} 未知轴 '{axis}'")
                elif not (W_MIN <= value <= W_MAX):
                    problems.append(f"{q['id']} 选项{index + 1} 轴 {axis} "
                                    f"权重 {value} 超出 {W_MIN}~{W_MAX}")
                else:
                    axis_hits[axis] += 1
            for color in (opt.get("col") or {}):
                if color not in COLORS and color not in COLOR_EXTRA:
                    problems.append(f"{q['id']} 选项{index + 1} 未知颜色 '{color}'")
                elif color in COLORS:
                    color_hits[color] += 1
            for key in (opt.get("cval") or {}):
                if key not in CVALS:
                    problems.append(f"{q['id']} 选项{index + 1} 未知约束 '{key}'")
                else:
                    cval_hits[key] += 1

        for i in range(len(opts)):
            for j in range(i + 1, len(opts)):
                sim = cosine(opts[i].get("s") or {}, opts[j].get("s") or {})
                if sim >= AMBIGUITY_LIMIT:
                    ambiguous.append(
                        f"{q['id']} 「{opts[i]['t'][:14]}」↔「{opts[j]['t'][:14]}」相似度 {sim:.2f}")

    if ambiguous:
        problems.append(f"选项模糊（余弦 ≥ {AMBIGUITY_LIMIT}）{len(ambiguous)} 处：")
        problems.extend(f"    {item}" for item in ambiguous[:20])

    # --- 多选题位置 ---
    multi_ids = [q["id"] for q in questions if q.get("multi")]
    for q in questions:
        if q.get("multi") and not (2 <= q["multi"] <= 4):
            problems.append(f"{q['id']} multi={q['multi']}（要求 2~4）")
    spine_index = {qid: i for i, qid in enumerate(spine)}
    first_multi = min((spine_index.get(m, 0) for m in multi_ids), default=0)
    early = [m for m in multi_ids if spine_index.get(m, 0) < len(spine) - 12]
    if early:
        problems.append(f"多选题没放在最后：{early}")
    print(f"多选题 {len(multi_ids)} 道，最早出现在主线第 {first_multi + 1} 题"
          f"（主线共 {len(spine)} 题）")

    # --- 覆盖度 ---
    weak_axes = [a for a in AXES if axis_hits.get(a, 0) < MIN_AXIS_OPTIONS]
    if weak_axes:
        problems.append(f"以下轴覆盖不足（<{MIN_AXIS_OPTIONS} 个选项）："
                        f"{[(a, axis_hits.get(a, 0)) for a in weak_axes]}")
    weak_colors = [c for c in COLORS if color_hits.get(c, 0) < MIN_COLOR_OPTIONS]
    if weak_colors:
        problems.append(f"以下颜色覆盖不足（<{MIN_COLOR_OPTIONS}）："
                        f"{[(c, color_hits.get(c, 0)) for c in weak_colors]}")
    weak_cvals = [k for k in CVALS if cval_hits.get(k, 0) < 4]
    if weak_cvals:
        problems.append(f"以下约束覆盖不足（<4 个选项）：{weak_cvals}")

    # --- 术语扫描（经验节的题必然提到万智牌，跳过） ---
    jargon_hits = []
    for q in questions:
        if q.get("sec") == "exp":
            continue
        blob = q["q"] + " " + " ".join(o["t"] for o in q["opts"])
        for word in JARGON:
            if word in blob:
                jargon_hits.append(f"{q['id']} 出现「{word}」")
    if jargon_hits:
        problems.append(f"出现万智牌术语 {len(jargon_hits)} 处：")
        problems.extend(f"    {item}" for item in jargon_hits[:15])

    # --- 题量估算 ---
    memo: dict = {}

    def bounds(node):
        if not node or node not in by_id:
            return (0, 0)
        if node in memo:
            return memo[node]
        memo[node] = (1, 1)
        q = by_id[node]
        outs = [o["goto"] for o in q["opts"] if o.get("goto")] or [q.get("next")]
        lo, hi = 10 ** 6, 0
        for t in outs:
            a, b = bounds(t)
            lo, hi = min(lo, a), max(hi, b)
        if lo == 10 ** 6:
            lo = 0
        memo[node] = (1 + lo, 1 + hi)
        return memo[node]

    lo, hi = bounds(start)
    print(f"完整版实际作答 {lo}~{hi} 题")
    if lo != hi:
        warnings.append(f"不同分支长度不一致（{lo}~{hi}），进度条按最长路径估算")

    # --- 报告 ---
    print(f"\n各轴被多少选项引用（要求 ≥{MIN_AXIS_OPTIONS}）：")
    for axis in AXES:
        count = axis_hits.get(axis, 0)
        bar = "█" * min(40, count)
        flag = " " if count >= MIN_AXIS_OPTIONS else "✗"
        print(f"  {flag} {axis:<11} {count:>3} {bar}")
    print(f"\n颜色：{ {c: color_hits.get(c, 0) for c in COLORS} }")
    print(f"约束：{ {k: cval_hits.get(k, 0) for k in CVALS} }")
    print(f"分节：{dict(section_counts)}")

    print("\n" + "=" * 70)
    for item in warnings:
        print(f"⚠ {item}")
    if problems:
        print(f"✗ 发现 {len(problems)} 类问题：")
        for item in problems:
            print(f"  - {item}")
        return 1
    print("✓ 题库校验全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
