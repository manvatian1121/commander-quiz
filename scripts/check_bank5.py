#!/usr/bin/env python3
"""bank5.json 自检（10 项）。

用法： python check_bank5.py
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

BANK = pathlib.Path(ROOT / "data" / "bank5.json")

AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]

WEIGHTS = {1.0, 1.5, 2.0, 2.5, 3.0}

MAINLINE = [f"s{n}" for n in range(65, 81)]
BRANCHES = {"h5a": ["h5a1", "h5a2", "h5a3"],
            "h5b": ["h5b1", "h5b2", "h5b3"],
            "h5c": ["h5c1", "h5c2", "h5c3"]}
EXPECTED_IDS = MAINLINE + [q for chain in BRANCHES.values() for q in chain]

SEC_MAP = {**{f"s{n}": "mind" for n in range(65, 71)},
           **{q: "mind" for chain in BRANCHES.values() for q in chain},
           **{f"s{n}": "money" for n in range(71, 75)},
           **{f"s{n}": "pick" for n in range(75, 81)}}

# 万智牌术语关键词（第九项检查）。只扫题干与选项文本。
MTG_TERMS = [
    "主将", "牌", "咒语", "咒", "铺场", "反击", "坟场", "坟", "生物", "法术力", "法力",
    "神器", "结界", "灵气", "衍生物", "指示物", "地牌", "基本地", "召唤", "回合", "抽牌",
    "手牌", "卡牌", "套牌", "卡组", "组牌", "打牌", "出牌", "过牌", "留牌", "万智",
    "EDH", "Commander", "commander", "Token", "token", "复制", "偷取", "无限", "连锁",
    "场上", "战场", "生命值", "召唤师", "献祭", "牺牲", "法术", "魔力", "结界师",
]

FINDINGS: list[tuple[str, str]] = []   # (检查项, 说明)


def note(check: str, msg: str) -> None:
    FINDINGS.append((check, msg))


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def main() -> int:
    # ---- 1. JSON 合法 + id 唯一 ----
    raw = BANK.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"[1] ✗ JSON 非法：{exc}")
        return 1
    questions = data.get("questions", [])
    by_id = {q.get("id"): q for q in questions}
    ids = [q.get("id") for q in questions]
    dup = [i for i, c in Counter(ids).items() if c > 1]
    missing = [i for i in EXPECTED_IDS if i not in by_id]
    extra = [i for i in ids if i not in EXPECTED_IDS]
    ok1 = not dup and not missing and not extra
    print(f"[1] JSON 合法 ✓  题数 {len(questions)}   batch={data.get('batch')}")
    print(f"    id 唯一：{'✓' if not dup else '✗ ' + str(dup)}；"
          f"题号齐全：{'✓' if not missing and not extra else f'✗ 缺 {missing} 多 {extra}'}")
    if dup:
        note("1", f"id 重复：{dup}")
    if missing or extra:
        note("1", f"题号与 QUESTION_MAP 不符：缺 {missing}，多 {extra}")
    if data.get("batch") != 5:
        note("1", f"batch 字段应为 5，实际 {data.get('batch')}")

    # ---- 2. 每题都有 next，s80 为 null ----
    bad_next = [q["id"] for q in questions if "next" not in q]
    print(f"\n[2] next 字段：{'✓ 全部具备' if not bad_next else '✗ 缺失 ' + str(bad_next)}")
    print(f"    s80.next = {by_id.get('s80', {}).get('next')!r} "
          f"{'✓' if by_id.get('s80', {}).get('next', 'X') is None else '✗'}")
    if bad_next:
        note("2", f"缺 next：{bad_next}")
    if by_id.get("s80", {}).get("next", "X") is not None:
        note("2", "s80 的 next 必须是 null")

    # ---- 3. goto 指向存在的 id ----
    bad_goto = []
    for q in questions:
        for i, o in enumerate(q["opts"], 1):
            g = o.get("goto")
            if g is not None and g not in by_id:
                bad_goto.append(f"{q['id']} 选项{i} → {g}")
    print(f"\n[3] goto 目标：{'✓ 全部有效' if not bad_goto else '✗ ' + str(bad_goto)}")
    if bad_goto:
        note("3", f"goto 指向不存在的 id：{bad_goto}")

    # ---- 4. 走通主线 + 三条分支 ----
    print("\n[4] 跳转链走通：")
    walk_problems: list[str] = []

    # 4a 主线（忽略 goto，按 next 走）
    trail, cur, guard = [], "s65", 0
    while cur is not None and guard < 200:
        guard += 1
        if cur not in by_id:
            walk_problems.append(f"主线断链：{cur} 不存在")
            break
        trail.append(cur)
        cur = by_id[cur].get("next")
    if trail != MAINLINE:
        walk_problems.append(f"主线路径异常：{trail}")
    print(f"    主线：{' → '.join(trail)}  ({'✓' if trail == MAINLINE else '✗'})")

    # 4b 枢纽约束
    hub = by_id.get("s70", {})
    hub_gotos = [o.get("goto") for o in hub.get("opts", [])]
    if hub.get("kind") != "hub":
        walk_problems.append("s70 缺 kind=hub")
    if sorted(x for x in hub_gotos if x) != sorted(c[0] for c in BRANCHES.values()):
        walk_problems.append(f"s70 的 goto 未覆盖三条分支入口：{hub_gotos}")
    if len(hub_gotos) != 3 or len(set(hub_gotos)) != 3:
        walk_problems.append("s70 应为 3 个选项、各 goto 一条不同分支")
    print(f"    s70 枢纽：{hub_gotos}  kind={hub.get('kind')!r} "
          f"{'✓' if not walk_problems else '✗'}")

    # 4c 三条分支各 3 题并回归 s71
    for name, chain in BRANCHES.items():
        entry = [o.get("goto") for o in hub.get("opts", []) if o.get("goto") == chain[0]]
        path, cur, guard = [], chain[0], 0
        while cur is not None and guard < 50:
            guard += 1
            if cur not in by_id:
                path.append(f"{cur}(不存在)")
                break
            path.append(cur)
            nxt = by_id[cur].get("next")
            if nxt in chain:          # 仍在同一条分支链上
                cur = nxt
                continue
            break
        last_next = by_id.get(chain[-1], {}).get("next")
        ok = path == chain and last_next == "s71" and bool(entry)
        print(f"    {name}：{' → '.join(path)} →(next) {last_next}  "
              f"{'✓' if ok else '✗'}")
        if not ok:
            walk_problems.append(f"{name} 链异常：{path} 末端 next={last_next}")

    if walk_problems:
        note("4", "; ".join(walk_problems))

    # ---- 5. 选项 3~5 个 / 文本非空 / 两两不同 ----
    print("\n[5] 选项数量与文本：")
    bad5 = []
    for q in questions:
        opts = q["opts"]
        if not (3 <= len(opts) <= 5):
            bad5.append(f"{q['id']} 选项数 {len(opts)}")
        texts = [o.get("t", "") for o in opts]
        if any(not t.strip() for t in texts):
            bad5.append(f"{q['id']} 有空选项")
        if len(set(texts)) != len(texts):
            dups = [t for t, c in Counter(texts).items() if c > 1]
            bad5.append(f"{q['id']} 选项重复 {dups}")
    counts = Counter(len(q["opts"]) for q in questions)
    print(f"    选项数分布：{dict(sorted(counts.items()))}  "
          f"{'✓' if not bad5 else '✗ ' + str(bad5)}")
    if bad5:
        note("5", "; ".join(bad5))

    # ---- 6. 每选项 1~3 轴 / 权重合法 ----
    print("\n[6] 轴得分数量与权重：")
    bad6 = []
    for q in questions:
        for i, o in enumerate(q["opts"], 1):
            s = o.get("s") or {}
            if not (1 <= len(s) <= 3):
                bad6.append(f"{q['id']} 选项{i} 轴数 {len(s)}")
            for axis, w in s.items():
                if axis not in AXES:
                    bad6.append(f"{q['id']} 选项{i} 未知轴 {axis}")
                if w not in WEIGHTS:
                    bad6.append(f"{q['id']} 选项{i} 非法权重 {w}")
    print(f"    {'✓ 全部合法（1~3 轴，权重 ∈ 1.0/1.5/2.0/2.5/3.0）' if not bad6 else '✗ ' + str(bad6)}")
    if bad6:
        note("6", "; ".join(bad6))

    # ---- 7. 题内选项余弦相似度 < 0.85 ----
    print("\n[7] 模糊度检查（题内两两余弦 < 0.85）：")
    worst: list[tuple[float, str]] = []
    over: list[tuple[float, str]] = []
    for q in questions:
        opts = q["opts"]
        for i in range(len(opts)):
            for j in range(i + 1, len(opts)):
                c = cosine(opts[i]["s"], opts[j]["s"])
                tag = f"{q['id']} 选项{i + 1}×{j + 1}"
                worst.append((c, tag))
                if c >= 0.85:
                    over.append((c, tag))
    worst.sort(reverse=True)
    print("    相似度最高的 6 组：")
    for c, tag in worst[:6]:
        flag = "✗" if c >= 0.85 else "✓"
        print(f"      {flag} {tag}  cos={c:.3f}")
    if over:
        print(f"    ✗ 超标 {len(over)} 组：")
        for c, tag in over:
            print(f"      - {tag} cos={c:.3f}")
        note("7", f"{len(over)} 组选项余弦 ≥ 0.85：{[t for _, t in over]}")
    else:
        print(f"    ✓ 全部 {len(worst)} 组均 < 0.85")

    # ---- 8. 20 轴覆盖（每个轴 ≥ 12 个选项）----
    print("\n[8] 20 个玩法轴的选项覆盖：")
    hits: Counter = Counter()
    for q in questions:
        for o in q["opts"]:
            for axis in o["s"]:
                hits[axis] += 1
    weak = []
    for axis in AXES:
        n = hits.get(axis, 0)
        bar = "█" * n
        flag = "✓" if n >= 12 else "✗"
        print(f"    {flag} {axis:<11} {n:>3} {bar}")
        if n < 12:
            weak.append(f"{axis}({n})")
    total_refs = sum(hits.values())
    print(f"    合计引用 {total_refs} 次，最少 {min(hits.get(a, 0) for a in AXES)} 次")
    if weak:
        note("8", f"覆盖不足 12 个选项的轴：{weak}")

    # ---- 9. 不许出现万智牌术语 ----
    print("\n[9] 万智牌术语扫描：")
    term_hits = []
    for q in questions:
        fields = [("题干", q["q"])] + [(f"选项{i}", o["t"]) for i, o in enumerate(q["opts"], 1)]
        for where, text in fields:
            for term in MTG_TERMS:
                if term in text:
                    term_hits.append(f"{q['id']} {where} 命中「{term}」：{text}")
    if term_hits:
        for line in term_hits:
            print(f"    ✗ {line}")
        note("9", f"{len(term_hits)} 处术语命中")
    else:
        print("    ✓ 题干与选项均未命中术语关键词")

    # ---- 10. s75~s80 多选题 ----
    print("\n[10] s75~s80 多选题：")
    bad10 = []
    for n in range(75, 81):
        q = by_id.get(f"s{n}", {})
        m = q.get("multi")
        ok = isinstance(m, int) and 2 <= m <= 4
        print(f"    {'✓' if ok else '✗'} s{n} multi={m}（{len(q.get('opts', []))} 个选项）")
        if not ok:
            bad10.append(f"s{n} multi={m}")
        if q.get("sec") != "pick":
            bad10.append(f"s{n} sec={q.get('sec')} 应为 pick")
    if bad10:
        note("10", "; ".join(bad10))

    # ---- sec 归属核对（附加）----
    sec_bad = [f"{q['id']}:{q.get('sec')}≠{SEC_MAP[q['id']]}" for q in questions
               if q.get("sec") != SEC_MAP.get(q["id"])]
    if sec_bad:
        note("附加", f"sec 与 QUESTION_MAP 不符：{sec_bad}")
        print(f"\n[附加] ✗ sec 不符：{sec_bad}")
    else:
        print("\n[附加] ✓ 全部 25 题的 sec 与 QUESTION_MAP 一致")

    # ---- 汇总 ----
    print("\n" + "=" * 62)
    if FINDINGS:
        print(f"✗ 未通过 {len(FINDINGS)} 项：")
        for check, msg in FINDINGS:
            print(f"  [{check}] {msg}")
        return 1
    print("✓ 10 项自检全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
