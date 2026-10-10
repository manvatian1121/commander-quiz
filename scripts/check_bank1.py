#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bank1.json 自检脚本（batch 1 / life 日常节奏，25 题）。

九项检查：
  1. JSON 合法、id 唯一、题集完整
  2. 每题都有 next 字段
  3. 所有 goto 都指向存在的 id
  4. 从 s01 出发按 next/goto 走通：主线 s01→s16、三条分支各 3 题、分支回归 s09
  5. 每题选项 3~5 个，选项文本非空且两两不同
  6. 每个选项 1~3 个轴得分，权重只用 1.0/1.5/2.0/2.5/3.0
  7. 模糊度：同题内任意两个选项轴向量余弦相似度 < 0.85
  8. 20 个轴各被多少个选项引用，每个轴至少 12 个
  9. 选项与题干不出现万智牌术语（关键词扫描）

用法： python scripts/check_bank1.py
"""
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
BANK = DATA / "bank1.json"

AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]

LEGAL_WEIGHTS = {1.0, 1.5, 2.0, 2.5, 3.0}
COS_LIMIT = 0.85
MIN_AXIS_HITS = 12

MAINLINE = [f"s{i:02d}" for i in range(1, 17)]
HUB = "s08"
BRANCHES = {"h1a1": "h1a2", "h1a2": "h1a3", "h1a3": "s09",
            "h1b1": "h1b2", "h1b2": "h1b3", "h1b3": "s09",
            "h1c1": "h1c2", "h1c2": "h1c3", "h1c3": "s09"}
HUB_GOTOS = {"h1a1", "h1b1", "h1c1"}
EXPECTED_IDS = set(MAINLINE) | set(BRANCHES)

# 第 9 项：万智牌术语关键词（只收在中文里几乎不用于日常生活的词，避免误报）
FORBIDDEN = [
    "主将", "指挥官", "牌组", "卡组", "套牌", "组牌", "构筑", "备牌", "副牌",
    "咒语", "法术力", "法术", "瞬间", "传奇", "召唤", "衍生物",
    "铺场", "站场", "清场", "上场", "下场", "场面",
    "坟场", "坟墓场", "墓地", "生物", "灵气", "结界", "结附", "装备",
    "反击", "连击", "踢", "斩杀", "无限", "增殖", "指示物", "过牌", "抓牌", "抽牌",
    "地牌", "基本地", "法力", "回合", "先手", "后手", "起手", "手牌", "牌库",
    "血差", "吸血", "康", "清坟", "爆费",
]

problems: list[str] = []


def norm(vec: dict) -> dict:
    """L2 归一化后的 {axis: value}。"""
    length = math.sqrt(sum(v * v for v in vec.values()))
    if length == 0:
        return {}
    return {k: v / length for k, v in vec.items()}


def cosine(a: dict, b: dict) -> float:
    na, nb = norm(a), norm(b)
    shared = set(na) & set(nb)
    return sum(na[k] * nb[k] for k in shared)


def load() -> list[dict] | None:
    try:
        raw = BANK.read_text(encoding="utf-8")
        data = json.loads(raw)
    except FileNotFoundError:
        problems.append(f"文件不存在：{BANK}")
        return None
    except json.JSONDecodeError as exc:
        problems.append(f"JSON 不合法：{exc}")
        return None
    if not isinstance(data, dict) or "questions" not in data:
        problems.append("顶层结构必须是 {\"batch\": 1, \"questions\": [...]}")
        return None
    if data.get("batch") != 1:
        problems.append(f"batch 字段应为 1，实际 {data.get('batch')!r}")
    return data["questions"]


def check_1_ids(questions: list[dict]) -> None:
    print("【1】JSON 合法、id 唯一")
    ids = [q.get("id") for q in questions]
    dupes = [i for i, c in Counter(ids).items() if c > 1]
    if dupes:
        problems.append(f"[1] id 重复：{dupes}")
    if len(questions) != 25:
        problems.append(f"[1] 题数应为 25，实际 {len(questions)}")
    missing = sorted(EXPECTED_IDS - set(ids))
    extra = sorted(set(ids) - EXPECTED_IDS)
    if missing:
        problems.append(f"[1] 缺少题目：{missing}")
    if extra:
        problems.append(f"[1] 出现不属于 batch1 的题号：{extra}")
    bad_sec = [q["id"] for q in questions if q.get("sec") != "life"]
    if bad_sec:
        problems.append(f"[1] sec 应为 life：{bad_sec}")
    hub_kind = [q["id"] for q in questions if q.get("kind") == "hub"]
    if hub_kind != [HUB]:
        problems.append(f"[1] 枢纽题应为且仅为 {HUB}，实际 {hub_kind}")
    for q in questions:
        if not isinstance(q.get("q"), str) or not q.get("q", "").strip():
            problems.append(f"[1] {q.get('id')} 题干为空")
        if not isinstance(q.get("opts"), list):
            problems.append(f"[1] {q.get('id')} 缺少 opts 数组")
    print(f"      id 唯一 ✓  共 {len(questions)} 题，题号集合与 batch1 分工一致"
          f"（{'无缺无多' if not missing and not extra else '见问题'}）")
    print(f"      sec 全为 life ✓   枢纽题 {HUB} ✓")


def check_2_next(questions: list[dict]) -> None:
    print("\n【2】每题都有 next 字段")
    missing = [q["id"] for q in questions if "next" not in q]
    if missing:
        problems.append(f"[2] 缺少 next：{missing}")
    nulls = [q["id"] for q in questions if q.get("next") is None]
    if nulls != ["s16"]:
        problems.append(f"[2] 本 batch 只有 s16 允许 next=null，实际为 {nulls}")
    print(f"      25/25 题均有 next 字段 ✓   其中 next=null 的仅 {nulls}"
          f"（s16 是 batch1 最后一题；s17 属 batch2 的 bank2.json，故写 null）")


def check_3_goto(questions: list[dict]) -> None:
    print("\n【3】所有 goto 指向存在的 id")
    ids = {q["id"] for q in questions}
    total = 0
    bad = []
    for q in questions:
        for i, opt in enumerate(q["opts"], 1):
            if "goto" not in opt:
                continue
            total += 1
            if opt["goto"] not in ids:
                bad.append(f"{q['id']} 选项{i} → {opt['goto']}")
    if bad:
        problems.append(f"[3] 悬空 goto：{bad}")
    # 只有枢纽题的选项才允许带 goto
    stray = [q["id"] for q in questions if q["id"] != HUB
             and any("goto" in o for o in q["opts"])]
    if stray:
        problems.append(f"[3] 非枢纽题带 goto：{stray}")
    hub_opts = [o for q in questions if q["id"] == HUB for o in q["opts"]]
    hub_without = [i for i, o in enumerate(hub_opts, 1) if "goto" not in o]
    if hub_without:
        problems.append(f"[3] 枢纽题选项 {hub_without} 缺 goto")
    if {o["goto"] for o in hub_opts} != HUB_GOTOS:
        problems.append(f"[3] 枢纽 goto 目标应为 {HUB_GOTOS}，实际 {{o['goto'] for o in hub_opts}}")
    print(f"      {total} 个 goto 全部命中存在的 id ✓")
    print(f"      全部集中在枢纽题 {HUB} ✓，目标 {sorted(HUB_GOTOS)} ✓")


def check_4_walk(questions: list[dict]) -> None:
    print("\n【4】从 s01 出发按 next/goto 走通（主线 s01→s16、三条分支各 3 题、回归 s09）")
    by_id = {q["id"]: q for q in questions}
    paths: list[list[str]] = []
    bad_steps: list[str] = []

    def walk(start: str, path: list[str]) -> None:
        cur = start
        guard = 0
        while cur is not None:
            guard += 1
            if guard > 200:
                bad_steps.append(f"从 {start} 出发出现死循环")
                return
            if cur not in by_id:
                bad_steps.append(f"路径 {path[-1] if path else start} 指向不存在的 {cur}")
                return
            path.append(cur)
            node = by_id[cur]
            entry = next((o for o in node["opts"] if "goto" in o), None)
            if entry is not None:
                # 枢纽题：分别走每一条分支
                for opt in node["opts"]:
                    walk(opt["goto"], list(path))
                return
            cur = node.get("next")

    # 主线：每到枢纽就分叉
    walk("s01", [])

    # 另行逐条走三条分支，确认每条的走向
    def linear(start: str) -> list[str]:
        out, cur = [], start
        while cur and cur in by_id:
            out.append(cur)
            if cur == HUB:
                break
            cur = by_id[cur].get("next")
        return out

    # 完整可达性：从 s01 起，穷举
    reachable = set()
    frontier = ["s01"]
    while frontier:
        cur = frontier.pop()
        if cur in reachable or cur not in by_id:
            continue
        reachable.add(cur)
        node = by_id[cur]
        for opt in node["opts"]:
            if "goto" in opt:
                frontier.append(opt["goto"])
        if node.get("next"):
            frontier.append(node["next"])

    if bad_steps:
        problems.append(f"[4] 走链出错：{bad_steps}")

    for prefix, tail in (("h1a", "h1a3"), ("h1b", "h1b3"), ("h1c", "h1c3")):
        chain = [f"{prefix}1", f"{prefix}2", f"{prefix}3"]
        for idx, qid in enumerate(chain):
            node = by_id.get(qid)
            if node is None:
                problems.append(f"[4] 分支题缺失：{qid}")
                continue
            want = chain[idx + 1] if idx + 1 < len(chain) else "s09"
            got = node.get("next")
            if got != want:
                problems.append(f"[4] {qid}.next 应为 {want}，实际 {got}")
        print(f"      {chain[0]} → {chain[1]} → {chain[2]} →(next) s09 ✓")

    main_chain = []
    cur = "s01"
    while cur and cur != HUB:
        main_chain.append(cur)
        cur = by_id[cur].get("next")
    main_chain.append(HUB)
    hub_next = by_id[HUB].get("next")
    if hub_next != "s09":
        problems.append(f"[4] 枢纽 {HUB}.next 应为 s09，实际 {hub_next}")
    after = []
    cur = "s09"
    while cur:
        after.append(cur)
        cur = by_id[cur].get("next")
    expected_after = [f"s{i:02d}" for i in range(9, 17)]
    if after != expected_after:
        problems.append(f"[4] s09 之后的主线应为 {expected_after}，实际 {after}")

    missing_reach = sorted(EXPECTED_IDS - reachable)
    if missing_reach:
        problems.append(f"[4] 从 s01 不可达：{missing_reach}")

    print(f"      主线：{' → '.join(main_chain)} →(hub 分流)→ s09 → ... → s16 ✓")
    print(f"      s09 之后：{' → '.join(after)} ✓")
    print(f"      从 s01 可达 {len(reachable)}/25 题，缺失 {missing_reach or '无'} ✓")
    print(f"      单条实际作答路径长度：16 主线 + 3 分支 = 19 题 ✓")


def check_5_options(questions: list[dict]) -> None:
    print("\n【5】每题选项 3~5 个，文本非空且两两不同")
    bad = []
    bad_dup = []
    for q in questions:
        opts = q["opts"]
        if not 3 <= len(opts) <= 5:
            bad.append(f"{q['id']}({len(opts)}个)")
        texts = [o.get("t", "") for o in opts]
        for i, t in enumerate(texts, 1):
            if not isinstance(t, str) or not t.strip():
                bad.append(f"{q['id']} 选项{i} 文本为空")
        dupes = [t for t, c in Counter(texts).items() if c > 1]
        if dupes:
            bad_dup.append(f"{q['id']}: {dupes}")
    if bad:
        problems.append(f"[5] 选项数量/文本问题：{bad}")
    if bad_dup:
        problems.append(f"[5] 同题选项文本重复：{bad_dup}")
    sizes = Counter(len(q["opts"]) for q in questions)
    print(f"      选项数分布：{dict(sorted(sizes.items()))} ✓（全部落在 3~5）")
    print(f"      共 {sum(len(q['opts']) for q in questions)} 个选项，文本非空、题内两两不同 ✓")


def check_6_scores(questions: list[dict]) -> None:
    print("\n【6】每选项 1~3 个轴得分，权重只用 1.0/1.5/2.0/2.5/3.0")
    bad_count, bad_axis, bad_weight = [], [], []
    for q in questions:
        for i, opt in enumerate(q["opts"], 1):
            s = opt.get("s")
            if not isinstance(s, dict) or not s:
                bad_count.append(f"{q['id']} 选项{i} 没有轴得分")
                continue
            if not 1 <= len(s) <= 3:
                bad_count.append(f"{q['id']} 选项{i} 有 {len(s)} 个轴")
            for axis, val in s.items():
                if axis not in AXES:
                    bad_axis.append(f"{q['id']} 选项{i} 未知轴 '{axis}'")
                if val not in LEGAL_WEIGHTS:
                    bad_weight.append(f"{q['id']} 选项{i} {axis}={val}")
    if bad_count:
        problems.append(f"[6] 轴数量问题：{bad_count}")
    if bad_axis:
        problems.append(f"[6] 未知轴：{bad_axis}")
    if bad_weight:
        problems.append(f"[6] 非法权重：{bad_weight}")
    total_scores = sum(len(o["s"]) for q in questions for o in q["opts"])
    weights = Counter(v for q in questions for o in q["opts"] for v in o["s"].values())
    print(f"      共 {total_scores} 个轴打分，权重取值分布：{dict(sorted(weights.items()))} ✓")
    print(f"      未知轴 0 个，轴数超出 1~3 的选项 0 个 ✓")


def check_7_fuzzy(questions: list[dict]) -> None:
    print(f"\n【7】模糊度：同题内任意两个选项轴向量余弦相似度 < {COS_LIMIT}")
    worst = []
    violations = []
    for q in questions:
        opts = q["opts"]
        for i in range(len(opts)):
            for j in range(i + 1, len(opts)):
                sim = cosine(opts[i]["s"], opts[j]["s"])
                worst.append((sim, q["id"], i + 1, j + 1))
                if sim >= COS_LIMIT:
                    violations.append(
                        f"{q['id']} 选项{i + 1} ∩ 选项{j + 1} = {sim:.3f}\n"
                        f"      选项{i + 1}：{opts[i]['t']}\n"
                        f"              {opts[i]['s']}\n"
                        f"      选项{j + 1}：{opts[j]['t']}\n"
                        f"              {opts[j]['s']}"
                    )
    worst.sort(reverse=True)
    pairs = len(worst)
    if violations:
        problems.append(f"[7] {len(violations)} 组选项余弦 ≥ {COS_LIMIT}：\n    - " + "\n    - ".join(violations))
    print(f"      共比较 {pairs} 组选项对，超标 {len(violations)} 组 ✓" if not violations
          else f"      共比较 {pairs} 组，超标 {len(violations)} 组 ✗")
    print("      最接近阈值的 5 组（越低越安全）：")
    for sim, qid, i, j in worst[:5]:
        print(f"        {qid} 选项{i} vs 选项{j}：{sim:.3f}")


def check_8_axis_coverage(questions: list[dict]) -> Counter:
    print(f"\n【8】20 个轴各被多少个选项引用（每轴至少 {MIN_AXIS_HITS} 个）")
    hits: Counter = Counter()
    for q in questions:
        for opt in q["opts"]:
            for axis in opt["s"]:
                hits[axis] += 1
    weak = []
    for axis in AXES:
        count = hits.get(axis, 0)
        flag = "" if count >= MIN_AXIS_HITS else "  ← 不足"
        if count < MIN_AXIS_HITS:
            weak.append(f"{axis}({count})")
        print(f"      {axis:<11} {count:>3}  {'█' * count}{flag}")
    if weak:
        problems.append(f"[8] 覆盖不足 {MIN_AXIS_HITS} 的轴：{weak}")
        print(f"      ✗ {len(weak)} 个轴低于 {MIN_AXIS_HITS}：{weak}")
    else:
        print(f"      20/20 轴全部 ≥ {MIN_AXIS_HITS} ✓   最低 {min(hits.get(a, 0) for a in AXES)}，最高 {max(hits.get(a, 0) for a in AXES)}")
    return hits


def check_9_keywords(questions: list[dict]) -> None:
    print("\n【9】选项/题干不出现万智牌术语")
    found = []
    for q in questions:
        fields = [("题干", q.get("q", ""))] + [(f"选项{i}", o.get("t", "")) for i, o in enumerate(q["opts"], 1)]
        for label, text in fields:
            for kw in FORBIDDEN:
                if kw in text:
                    found.append(f"{q['id']} {label} 命中「{kw}」：{text}")
    if found:
        problems.append(f"[9] 命中万智牌术语 {len(found)} 处：{found}")
    print(f"      扫描 {len(FORBIDDEN)} 个关键词 × {len(questions)} 题（题干 + 全部选项）")
    print(f"      命中 {len(found)} 处 ✓" if not found else f"      命中 {len(found)} 处 ✗")


def main() -> int:
    questions = load()
    if questions is None:
        print("✗ 无法读取 bank1.json")
        for p in problems:
            print("  - " + p)
        return 1

    check_1_ids(questions)
    check_2_next(questions)
    check_3_goto(questions)
    check_4_walk(questions)
    check_5_options(questions)
    check_6_scores(questions)
    check_7_fuzzy(questions)
    hits = check_8_axis_coverage(questions)
    check_9_keywords(questions)

    print("\n" + "=" * 64)
    print(f"轴引用总计 {sum(hits.values())} 次，覆盖 {len([a for a in AXES if hits.get(a, 0) > 0])}/20 个轴")
    if problems:
        print(f"\n✗ 共 {len(problems)} 项未通过：")
        for item in problems:
            print("  - " + item)
        return 1
    print("\n✓ 九项自检全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
