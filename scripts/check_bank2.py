#!/usr/bin/env python3
"""batch2 (bank2.json) 自检：9 项检查，逐项打印结果。

用法：python check_bank2.py [--bank <path>]
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import pathlib
import re
import sys
from collections import Counter



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

DEFAULT_BANK = pathlib.Path(ROOT / "data" / "bank2.json")

AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]

WEIGHTS = {1.0, 1.5, 2.0, 2.5, 3.0}

# 主线 s17~s32（含枢纽 s24），分支 h2a*/h2b*/h2c*
MAINLINE = [f"s{n}" for n in range(17, 33)]
BRANCHES = {
    "a": ["h2a1", "h2a2", "h2a3"],
    "b": ["h2b1", "h2b2", "h2b3"],
    "c": ["h2c1", "h2c2", "h2c3"],
}

# 万智牌术语黑名单（选项里出现即违规）
MTG_TERMS = [
    "主将", "指挥官", "牌组", "套牌", "牌表", "手牌", "墓地", "坟场", "咒语", "法术",
    "瞬间", "巫术", "结界", "灵气", "神器", "装备", "生物", "衍生物", "铺场", "爆兵",
    "反击", "反制", "连锁", "组合技", "无限连", "法术力", "地牌", "基本地", "抽牌",
    "抓牌", "打脸", "踢脸", "生命值", "指示物", "增殖", "闪现", "偷取", "复制",
    "锁场", "弃牌", "磨牌", "万智", "MTG", "EDH", "cEDH", "Bracket", "tutor",
    "ramp", "aggro", "voltron", "combo", "stax", "blink", "tribal", "drain",
    "counter", "token", "mana", "land",
]

COS_LIMIT = 0.85
MIN_AXIS_REFS = 12


class Report:
    def __init__(self) -> None:
        self.fail = 0
        self.warn = 0

    def ok(self, item: str, detail: str = "") -> None:
        print(f"  [PASS] {item}" + (f" —— {detail}" if detail else ""))

    def bad(self, item: str, detail: str = "") -> None:
        self.fail += 1
        print(f"  [FAIL] {item}" + (f" —— {detail}" if detail else ""))

    def note(self, item: str, detail: str = "") -> None:
        self.warn += 1
        print(f"  [WARN] {item}" + (f" —— {detail}" if detail else ""))


def cosine(a: dict, b: dict) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(a.get(k, 0.0) ** 2 for k in keys))
    nb = math.sqrt(sum(b.get(k, 0.0) ** 2 for k in keys))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", default=str(DEFAULT_BANK))
    args = ap.parse_args()
    path = pathlib.Path(args.bank)

    rep = Report()
    print("=" * 72)
    print(f"bank2 自检 —— {path}")
    print("=" * 72)

    # ---------- 1. JSON 合法、id 唯一 ----------
    print("\n[1] JSON 合法性与 id 唯一性")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        rep.bad("JSON 解析", str(exc))
        return 1
    if not isinstance(data, dict) or "questions" not in data:
        rep.bad("顶层结构", "缺少 questions 字段")
        return 1
    qs = data["questions"]
    rep.ok("JSON 解析成功", f"{len(qs)} 题")
    ids = [q.get("id") for q in qs]
    dups = [i for i, c in Counter(ids).items() if c > 1]
    if dups:
        rep.bad("id 唯一", f"重复：{dups}")
    else:
        rep.ok("id 唯一", f"{len(ids)} 个 id 无重复")
    by_id = {q["id"]: q for q in qs}

    # ---------- 2. 每题都有 next ----------
    print("\n[2] 每题都有 next 字段")
    missing = [q.get("id") for q in qs if "next" not in q]
    if missing:
        rep.bad("next 字段", f"缺失：{missing}")
    else:
        rep.ok("next 字段", "全部存在（含枢纽题与分支题）")
    nulls = [q["id"] for q in qs if q.get("next") is None]
    if nulls:
        rep.note("next 为 null 的题", f"{nulls}（batch2 不应有 null，s80 才为 null）")

    # ---------- 3. goto 指向存在的 id ----------
    print("\n[3] 所有 goto 指向存在的 id")
    bad_goto = []
    goto_count = 0
    for q in qs:
        for i, o in enumerate(q["opts"]):
            if "goto" in o:
                goto_count += 1
                if o["goto"] not in by_id:
                    bad_goto.append(f"{q['id']}#{i + 1} -> {o['goto']}")
    if bad_goto:
        rep.bad("goto 目标", f"悬空：{bad_goto}")
    else:
        rep.ok("goto 目标", f"{goto_count} 个 goto 全部命中")

    # ---------- 4. 跳转链走通 ----------
    print("\n[4] 跳转链走通（主线 s17→s32、三条分支各 3 题、分支回归 s25）")
    problems4 = []
    EXTERNAL = {"s33", "s16"}  # 跨 batch 衔接点，不在本文件里

    def walk_next(start: str, stops: set[str]) -> list[str]:
        """只跟 next 往前走，遇到 stops 或域外 id 停下。"""
        seq, cur = [], start
        while cur is not None:
            seq.append(cur)
            if cur in stops or cur not in by_id or len(seq) > 200:
                break
            cur = by_id[cur].get("next")
        return seq

    def walk_answers(start: str, branch: str) -> list[str]:
        """模拟作答：枢纽题走 branch 指定的那条分支，其余跟 next。"""
        seq, cur = [], start
        while cur is not None:
            seq.append(cur)
            q = by_id.get(cur)
            if q is None:
                break
            goto = None
            if q.get("kind") == "hub":
                goto = next((o["goto"] for o in q["opts"]
                             if str(o.get("goto", "")).startswith(branch)), None)
            cur = goto or q.get("next")
            if len(seq) > 200:
                break
        return seq

    # 用户实际路径 = 主线前半 + 一条分支 + 主线后半
    expected_tail = MAINLINE[8:] + ["s33"]  # s25 … s32 → s33
    for key, chain in BRANCHES.items():
        got = walk_answers("s17", f"h2{key}")
        expect = MAINLINE[:8] + chain + expected_tail
        if got != expect:
            problems4.append(f"走 h2{key} 分支的完整路径不符：{got}")
    if not any("完整路径不符" in p for p in problems4):
        rep.ok("主线连通", "s17 → s23 → s24(枢纽) → 分支 → s25 → … → s32 → s33（三条路径皆通）")

    hub = by_id.get("s24", {})
    if hub.get("kind") != "hub":
        problems4.append("s24 缺少 kind=hub")
    hub_gotos = [o.get("goto") for o in hub.get("opts", [])]
    if sorted(hub_gotos) != ["h2a1", "h2b1", "h2c1"]:
        problems4.append(f"s24 的 goto 不是三个分支入口：{hub_gotos}")
    else:
        rep.ok("枢纽分流", "s24 → h2a1 / h2b1 / h2c1 三条不同分支")
    if not (3 <= len(hub.get("opts", [])) <= 5):
        problems4.append(f"s24 选项数 {len(hub.get('opts', []))} 超出 3~5")

    for key, chain in BRANCHES.items():
        got = walk_next(chain[0], stops={"s25"})
        if got != chain + ["s25"]:
            problems4.append(f"分支 {key} 链不符：{got}")
        else:
            rep.ok(f"分支 {key}", f"{chain[0]} → {chain[1]} → {chain[2]} → s25（回归点 s25）")
    # 分支入口必须由枢纽题指出、中间题 next 必须指向链内下一题
    for chain in BRANCHES.values():
        for a, b in zip(chain, chain[1:]):
            if by_id[a].get("next") != b:
                problems4.append(f"{a}.next 应为 {b}，实为 {by_id[a].get('next')}")
    if problems4:
        for p in problems4:
            rep.bad("跳转链", p)
    else:
        rep.ok("跳转链完整", "无断链、无环路")

    # ---------- 5. 选项 3~5 个、非空、两两不同 ----------
    print("\n[5] 选项数量 3~5、文本非空、两两不同")
    p5 = []
    for q in qs:
        opts = q.get("opts", [])
        if not (3 <= len(opts) <= 5):
            p5.append(f"{q['id']} 选项数 {len(opts)}")
        texts = [o.get("t", "").strip() for o in opts]
        for i, t in enumerate(texts):
            if not t:
                p5.append(f"{q['id']} 第 {i + 1} 个选项文本为空")
        for (i, a), (j, b) in itertools.combinations(enumerate(texts), 2):
            if a and a == b:
                p5.append(f"{q['id']} 选项 {i + 1} 与 {j + 1} 完全相同")
            elif a and b and (a in b or b in a) and min(len(a), len(b)) >= 6:
                rep.note("选项高度包含", f"{q['id']} 「{a}」/「{b}」")
    if p5:
        for p in p5:
            rep.bad("选项基本约束", p)
    else:
        n_opts = sum(len(q["opts"]) for q in qs)
        rep.ok("选项基本约束", f"{n_opts} 个选项全部合规、无重复文本")

    # ---------- 6. 每选项 1~3 个轴、权重合法 ----------
    print("\n[6] 每选项 1~3 个轴得分，权重只用 1.0/1.5/2.0/2.5/3.0")
    p6 = []
    for q in qs:
        for i, o in enumerate(q["opts"]):
            s = o.get("s") or {}
            tag = f"{q['id']}#{i + 1}"
            if not (1 <= len(s) <= 3):
                p6.append(f"{tag} 轴数 {len(s)}")
            for ax, w in s.items():
                if ax not in AXES:
                    p6.append(f"{tag} 未知轴 {ax}")
                if w not in WEIGHTS:
                    p6.append(f"{tag} 非法权重 {ax}={w}")
    if p6:
        for p in p6:
            rep.bad("轴得分格式", p)
    else:
        total_refs = sum(len(o.get("s") or {}) for q in qs for o in q["opts"])
        rep.ok("轴得分格式", f"{total_refs} 条轴引用全部合法")

    # ---------- 7. 模糊度：题内两两余弦 < 0.85 ----------
    print(f"\n[7] 模糊度检查：同题选项余弦相似度必须 < {COS_LIMIT}")
    p7 = []
    worst = (0.0, "", "")
    for q in qs:
        for (i, a), (j, b) in itertools.combinations(enumerate(q["opts"]), 2):
            c = cosine(a.get("s") or {}, b.get("s") or {})
            if c > worst[0]:
                worst = (c, f"{q['id']}#{i + 1}:{a['t'][:18]}", f"{q['id']}#{j + 1}:{b['t'][:18]}")
            if c >= COS_LIMIT:
                p7.append(f"{q['id']} 选项{i + 1}×选项{j + 1} cos={c:.3f}"
                          f"\n         A: {a['t']}  {a.get('s')}"
                          f"\n         B: {b['t']}  {b.get('s')}")
    if p7:
        for p in p7:
            rep.bad("余弦超标", p)
    else:
        n_pairs = sum(len(list(itertools.combinations(q["opts"], 2))) for q in qs)
        rep.ok("无模糊选项", f"{n_pairs} 对全部 < {COS_LIMIT}；最高 {worst[0]:.3f}"
                             f"（{worst[1]} × {worst[2]}）")

    # ---------- 8. 20 轴覆盖统计 ----------
    print(f"\n[8] 20 个轴各被多少个选项引用（下限 {MIN_AXIS_REFS}）")
    hits = Counter()
    for q in qs:
        for o in q["opts"]:
            for ax in (o.get("s") or {}):
                hits[ax] += 1
    weak = []
    for ax in AXES:
        c = hits.get(ax, 0)
        bar = "█" * c
        flag = "" if c >= MIN_AXIS_REFS else "  <-- 不足"
        print(f"      {ax:<11}{c:>4}  {bar}{flag}")
        if c < MIN_AXIS_REFS:
            weak.append(f"{ax}({c})")
    print(f"      总计 {sum(hits.values())} 条轴引用，均值 {sum(hits.values()) / len(AXES):.1f}/轴")
    if weak:
        rep.bad("轴覆盖不足", ", ".join(weak))
    else:
        rep.ok("轴覆盖达标", f"20 个轴全部 ≥ {MIN_AXIS_REFS}")

    # ---------- 9. 无万智牌术语 ----------
    print("\n[9] 选项/题干里不许出现万智牌术语（关键词扫描）")
    p9 = []
    for q in qs:
        blobs = [(f"{q['id']}.q", q["q"])] + [(f"{q['id']}#{i + 1}", o["t"])
                                              for i, o in enumerate(q["opts"])]
        for tag, text in blobs:
            low = text.lower()
            for term in MTG_TERMS:
                if term.lower() in low:
                    p9.append(f"{tag} 含术语「{term}」：{text}")
    if p9:
        for p in p9:
            rep.bad("术语扫描", p)
    else:
        rep.ok("术语扫描", f"{len(MTG_TERMS)} 个关键词 × {len(qs)} 题全部干净")

    # ---------- 汇总 ----------
    n_main = sum(1 for q in qs if re.fullmatch(r"s[0-9]+", q["id"]))
    n_branch = sum(1 for q in qs if q["id"].startswith("h2"))
    n_opts = sum(len(q["opts"]) for q in qs)
    print("\n" + "=" * 72)
    print(f"题数：{len(qs)}（主线 {n_main} + 分支 {n_branch}），选项 {n_opts} 个")
    if rep.fail:
        print(f"✗ 不通过：{rep.fail} 项失败，{rep.warn} 项提示")
        return 1
    print(f"✓ 9 项检查全部通过（{rep.warn} 项提示）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
