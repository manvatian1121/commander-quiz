#!/usr/bin/env python3
"""颜色题改写自检（对照备份 _colorq_backup_bank4.json）。

跑法：python check_color_questions.py

6 项硬检查：
  1. 四道题的 id、顺序、next 未变
  2. 每题 5 选项，每选项恰好 1 个颜色，同题内五色齐全
  3. 选项文本与题干里不含颜色词（红蓝黑白绿灰紫橙黄粉青金银褐棕）
  4. 每选项 1~3 轴、权重在 0.5~3.0
  5. 同题内两两轴向量余弦 < 0.85（报出最高的一对）
  6. 跨题轴复用：四道题各自主导轴 + 位置×主轴矩阵，确认没有「同一位置总是同一个轴」

附加项（不参与通过/失败，只报告）：
  A. 位置 × 颜色矩阵（同一列不该重复）
  B. 万智牌术语扫描（复用 check_bank4 的黑名单）
  C. bank4 逐轴引用数 vs 备份（不该跌破 12）
  D. 四道题的新选项文本与全库其它题目的重复情况
"""
from __future__ import annotations

import json
import math
import pathlib
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
BANK = DATA / "bank4.json"
BACKUP = ROOT / "_scratch" / "data" / "_colorq_backup_bank4.json"

TARGETS = ["s49", "s59", "s60", "s62"]
COLOR_WORDS = ["红", "蓝", "黑", "白", "绿", "灰", "紫", "橙", "黄", "粉",
               "青", "金", "银", "褐", "棕"]
COLOR_NAMES = {"W": "白", "U": "蓝", "B": "黑", "R": "红", "G": "绿"}
COLORS = ["W", "U", "B", "R", "G"]
POSITIONS = "ABCDE"
AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]

# 与 check_bank4.py 一致的黑名单（只做扫描，不重复它的判定）
BANNED = [
    "主将", "指挥官", "牌组", "套牌", "卡牌", "牌库", "手牌", "抽牌", "卡差",
    "咒语", "法术力", "法术", "瞬间", "结界", "灵气", "神器", "生物", "衍生",
    "永久物", "召唤", "铺场", "铺开场面", "反击", "坟场", "闪现", "触发",
    "指示物", "增殖", "偷取", "复制", "法术力费", "出场费", "费用", "色组",
    "双色", "五色", "万智", "Bracket", "EDH", "Commander", "地牌", "基本地",
    "回合", "对局", "竞技", "赛制", "起手", "场面", "锁场",
]

results: list[tuple[str, bool]] = []


def header(no: str, title: str) -> None:
    print(f"\n[{no}] {title}")


def verdict(no: str, title: str, ok: bool, lines: list[str]) -> None:
    header(no, title)
    print(f"      {'PASS' if ok else 'FAIL'}")
    for line in lines:
        print(f"      {line}")
    results.append((no, ok))


def vec(opt: dict) -> dict[str, float]:
    return dict(opt.get("s") or {})


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(a.get(k, 0.0) ** 2 for k in keys))
    nb = math.sqrt(sum(b.get(k, 0.0) ** 2 for k in keys))
    return dot / (na * nb) if na and nb else 0.0


def main() -> int:
    cur = json.loads(BANK.read_text(encoding="utf-8"))["questions"]
    old = json.loads(BACKUP.read_text(encoding="utf-8"))["questions"]

    cur_ids = [q["id"] for q in cur]
    old_ids = [q["id"] for q in old]
    by_id = {q["id"]: q for q in cur}
    old_by_id = {q["id"]: q for q in old}

    print("=" * 78)
    print("颜色题改写自检：s49 / s59 / s60 / s62")
    print(f"当前文件 {BANK}")
    print(f"对照备份 {BACKUP}")
    print("=" * 78)

    # ------------------------------------------------------------------ 1
    pos_ok = all(cur_ids.index(i) == old_ids.index(i) for i in TARGETS)
    next_detail = []
    next_ok = True
    for qid in TARGETS:
        a, b = old_by_id[qid], by_id[qid]
        if a.get("next") != b.get("next"):
            next_ok = False
        next_detail.append(f"{qid}: 位置 {old_ids.index(qid)}→{cur_ids.index(qid)}  "
                           f"next {a.get('next')!r}→{b.get('next')!r}")
    sec_ok = all(old_by_id[i].get("sec") == by_id[i].get("sec") for i in TARGETS)
    keys_ok = all(list(old_by_id[i].keys()) == list(by_id[i].keys()) for i in TARGETS)
    verdict("1", "四道题 id / 顺序 / next / sec 未变", pos_ok and next_ok and sec_ok and keys_ok,
            next_detail + [
                f"整库 id 序列与备份完全一致：{cur_ids == old_ids}",
                f"题目字段集合未变（只有 q/t/s/col 被改）：{keys_ok}",
            ])

    # ------------------------------------------------------------------ 2
    bad: list[str] = []
    matrix: dict[str, dict[str, str]] = {}
    for qid in TARGETS:
        q = by_id[qid]
        opts = q["opts"]
        if len(opts) != 5:
            bad.append(f"{qid} 选项数={len(opts)}")
        seen: list[str] = []
        for i, o in enumerate(opts):
            col = o.get("col") or {}
            if len(col) != 1:
                bad.append(f"{qid} 选项{i + 1} col 键数={len(col)}（应恰好 1）")
                continue
            name, weight = next(iter(col.items()))
            if name not in COLORS:
                bad.append(f"{qid} 选项{i + 1} 未知颜色 {name}")
            if float(weight) != 2.0:
                bad.append(f"{qid} 选项{i + 1} 颜色权重={weight}（现状口径为 2.0）")
            seen.append(name)
        matrix[qid] = {POSITIONS[i]: c for i, c in enumerate(seen)}
        if sorted(seen) != sorted(COLORS):
            bad.append(f"{qid} 同题五色不齐：{seen}")
    verdict("2", "每题 5 选项 / 每选项恰好 1 色 / 同题 W U B R G 各一次", not bad,
            [f"{qid}: " + "  ".join(f"{POSITIONS[i]}={matrix[qid][POSITIONS[i]]}"
                                    for i in range(5)) for qid in TARGETS]
            + [f"问题={bad or '无'}"])

    # ------------------------------------------------------------------ 3
    hits: list[str] = []
    for qid in TARGETS:
        q = by_id[qid]
        for i, opt in enumerate(q["opts"]):
            for w in COLOR_WORDS:
                if w in opt["t"]:
                    hits.append(f"{qid} 选项{POSITIONS[i]} 命中「{w}」：{opt['t']}")
        for w in COLOR_WORDS:
            if w in q["q"]:
                hits.append(f"{qid} 题干命中「{w}」：{q['q']}")
    total_text = sum(len(by_id[q]["opts"]) for q in TARGETS) + len(TARGETS)
    verdict("3", f"题干与选项不含颜色词（扫 {len(COLOR_WORDS)} 个字）", not hits,
            [f"扫描文本数={total_text}（4 题干 + 20 选项）", f"命中={hits or '无'}"])

    # ------------------------------------------------------------------ 4
    bad4: list[str] = []
    entries = 0
    for qid in TARGETS:
        for i, opt in enumerate(by_id[qid]["opts"]):
            s = opt.get("s") or {}
            entries += len(s)
            if not 1 <= len(s) <= 3:
                bad4.append(f"{qid} 选项{POSITIONS[i]} 轴数={len(s)}")
            for axis, w in s.items():
                if axis not in AXES:
                    bad4.append(f"{qid} 选项{POSITIONS[i]} 未知轴 {axis}")
                if not 0.5 <= float(w) <= 3.0:
                    bad4.append(f"{qid} 选项{POSITIONS[i]} 权重越界 {axis}={w}")
    verdict("4", "每选项 1~3 轴 / 权重落在 0.5~3.0", not bad4,
            [f"20 个选项共 {entries} 条轴得分，平均 {entries / 20:.2f} 条/选项",
             f"权重集合={sorted({w for q in TARGETS for o in by_id[q]['opts'] for w in (o['s'] or {}).values()})}",
             f"问题={bad4 or '无'}"])

    # ------------------------------------------------------------------ 5
    worst: list[tuple[float, str, int, int]] = []
    viol: list[str] = []
    for qid in TARGETS:
        opts = by_id[qid]["opts"]
        for i in range(len(opts)):
            for j in range(i + 1, len(opts)):
                c = cosine(vec(opts[i]), vec(opts[j]))
                worst.append((c, qid, i, j))
                if c >= 0.85:
                    viol.append(f"{qid} {POSITIONS[i]}×{POSITIONS[j]} = {c:.3f}")
    worst.sort(reverse=True)
    detail = [f"最高的一对：{qid} 选项{POSITIONS[i]}（{by_id[qid]['opts'][i]['t'][:12]}…）"
              f" × 选项{POSITIONS[j]}（{by_id[qid]['opts'][j]['t'][:12]}…）  cos={c:.3f}"
              for c, qid, i, j in worst[:3]]
    detail.append("各题最高 cos：" + "  ".join(
        f"{qid}={max(c for c, q, _, _ in worst if q == qid):.3f}" for qid in TARGETS))
    verdict("5", "同题内两两轴向量余弦 < 0.85", not viol, detail + [f"超标={viol or '无'}"])

    # ------------------------------------------------------------------ 6
    per_pos: dict[str, list[tuple[str, str]]] = {p: [] for p in POSITIONS}
    lead_lines = []
    for qid in TARGETS:
        leads = []
        for i, opt in enumerate(by_id[qid]["opts"]):
            s = opt["s"]
            top = max(s.values())
            prim = [a for a, w in s.items() if w == top]
            leads.append("+".join(sorted(prim)))
            per_pos[POSITIONS[i]].append((qid, "+".join(sorted(prim))))
        lead_lines.append(f"{qid} 主导轴（按 A~E）：{'  '.join(f'{POSITIONS[i]}={leads[i]}' for i in range(5))}")
    pos_lines = []
    conflict = []
    for p in POSITIONS:
        seq = [x[1] for x in per_pos[p]]
        pos_lines.append(f"位置 {p}: " + "  ".join(f"{qid}→{ax}" for qid, ax in per_pos[p]))
        if len(set(seq)) != len(seq):
            conflict.append(f"位置 {p} 出现重复主轴：{seq}")
    verdict("6", "跨题：没有「同一位置总是同一个轴」", not conflict,
            lead_lines + pos_lines + [f"冲突={conflict or '无'}"])

    # ------------------------------------------------------------------ A
    col_lines, col_conflict = [], []
    for p in POSITIONS:
        seq = [matrix[qid][p] for qid in TARGETS]
        col_lines.append(f"位置 {p}: " + "  ".join(
            f"{qid}→{COLOR_NAMES[matrix[qid][p]]}" for qid in TARGETS))
        if len(set(seq)) != len(seq):
            col_conflict.append(f"位置 {p} 重复颜色 {seq}")
    print("\n[A] 位置 × 颜色矩阵（附带报告）")
    for line in col_lines:
        print(f"      {line}")
    print(f"      同一列重复颜色：{col_conflict or '无'}")
    for c in COLORS:
        slots = [f"{qid}{p}" for qid in TARGETS for p in POSITIONS if matrix[qid][p] == c]
        print(f"      {COLOR_NAMES[c]}({c})：{len(slots)} 次，落在 {', '.join(slots)}")

    # ------------------------------------------------------------------ B
    hits_b = []
    for qid in TARGETS:
        q = by_id[qid]
        for i, opt in enumerate(q["opts"]):
            for w in BANNED:
                if w in opt["t"]:
                    hits_b.append(f"{qid} 选项{POSITIONS[i]} 命中「{w}」：{opt['t']}")
        for w in BANNED:
            if w in q["q"]:
                hits_b.append(f"{qid} 题干命中「{w}」")
    print("\n[B] 万智牌术语扫描（附加）")
    print(f"      硬命中={hits_b or '无'}")

    # ------------------------------------------------------------------ C
    def axis_refs(qs):
        c = Counter()
        for q in qs:
            for o in q["opts"]:
                for a in (o.get("s") or {}):
                    c[a] += 1
        return c

    old_all, new_all = axis_refs(old), axis_refs(cur)
    four_old = axis_refs([old_by_id[q] for q in TARGETS])
    four_new = axis_refs([by_id[q] for q in TARGETS])
    drops = [f"{a}: {old_all[a]}→{new_all[a]}" for a in AXES if new_all[a] < old_all[a]]
    below = [a for a in AXES if new_all[a] < 12]
    print("\n[C] bank4 逐轴引用数（附加，检查 8 要求 ≥12）")
    print("      四道题自身贡献：" + "  ".join(f"{a}:{four_old[a]}→{four_new[a]}"
                                              for a in AXES if four_old[a] or four_new[a]))
    print(f"      全库下降的轴={drops or '无'}")
    print(f"      低于 12 的轴={below or '无'}")

    # ------------------------------------------------------------------ D
    others = {}
    for name in ["bank1", "bank2", "bank3", "bank5"]:
        for q in json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))["questions"]:
            for o in q["opts"]:
                others.setdefault(o["t"], []).append(q["id"])
    for q in cur:
        if q["id"] in TARGETS:
            continue
        for o in q["opts"]:
            others.setdefault(o["t"], []).append(q["id"])
    dupes = [f"{qid} 选项{POSITIONS[i]}「{o['t']}」与 {others.get(o['t'])} 相同"
             for qid in TARGETS for i, o in enumerate(by_id[qid]["opts"]) if o["t"] in others]
    print("\n[D] 新选项文本与全库其它题目的重复（附加）")
    print(f"      完全重复={dupes or '无'}")

    # ------------------------------------------------------------------ 汇总
    print("\n" + "=" * 78)
    passed = sum(1 for _, ok in results if ok)
    print(f"六项硬检查：{passed} 通过 / {len(results) - passed} 失败")
    for no, ok in results:
        print(f"  [{no}] {'PASS' if ok else 'FAIL'}")
    print("全部通过 ✓" if passed == len(results) else "存在失败项 ✗")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
