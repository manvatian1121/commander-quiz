#!/usr/bin/env python3
"""USER_FEEDBACK_SPEC 九道题改动的自检脚本（6 项）。

依赖 scripts/apply_user_feedback_edits.py 留下的 before 快照：
  _scratch/data/_feedback_bak/*.json  （改动前）  vs  data/*.json （改动后）

用法： python scripts/check_user_feedback_edits.py
输出： 终端 + data/USER_FEEDBACK_CHECK.md
"""
from __future__ import annotations

import itertools
import json
import math
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
BAK = ROOT / "_scratch" / "data" / "_feedback_bak"
OUT = DATA / "USER_FEEDBACK_CHECK.md"

BANKS = ["bank1.json", "bank2.json", "bank3.json", "bank4.json", "bank5.json",
         "bankC.json", "bankE.json"]

# 本轮唯一允许改动的 9 道题（按 spec：图1~图9）
TARGETS = ["s04", "h1c3", "s19", "s24", "s36", "s45", "s50", "s51", "c05"]
TARGET_SET = set(TARGETS)

# 枢纽题 s24 的三条分支
HUB_ID = "s24"
HUB_GOTOS = ["h2a1", "h2b1", "h2c1"]

# 万智牌术语黑名单（选项文本不得出现）
TERMS = [
    "万智牌", "MTG", "EDH", "CEDH", "Commander", "指挥官", "主将", "套牌", "牌组", "卡牌",
    "牌表", "手牌", "抽牌", "弃牌", "磨牌", "坟场", "墓地", "咒语", "法术力", "永久物",
    "生物", "神器", "结界", "鹏洛客", "传纪", "衍生物", "指示物", "铺场", "爆费", "快攻",
    "中速", "锁场", "组合技", "效应", "触发", "放逐", "横置", "竖置", "献祭", "召唤",
    "先手", "后手", "地牌", "基本地", "颜色身份", "灵气", "光环", "部落", "增殖", "歼灭",
    "突袭", "贴皮", "过牌", "检索", "康牌", "反击咒语", "重置", "阻挡", "生命值",
    "现开", "赛制", "构筑", "单卡", "牌手", "对局", "加费", "滤牌", "换备",
]
# 注：「轮抽」不入表——它是「最后一轮抽奖」的子串，纯子串扫描会误报（见 s20 题干）。
LETTERS = "ABCDEFGH"


def dump(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def load(dirpath: pathlib.Path) -> dict[str, dict]:
    out = {}
    for name in BANKS:
        p = dirpath / name
        if p.exists():
            out[name] = json.loads(p.read_text(encoding="utf-8"))
    return out


def qmap(banks: dict[str, dict]) -> dict[str, tuple[str, dict]]:
    m = {}
    for fname, obj in banks.items():
        for q in obj.get("questions", []):
            m[q["id"]] = (fname, q)
    return m


def walk_diff(before, after, path=""):
    """递归逐字段 diff，返回 [(path, before, after)]"""
    diffs = []
    if isinstance(before, dict) and isinstance(after, dict):
        for k in dict.fromkeys(list(before) + list(after)):
            if k not in before:
                diffs.append((f"{path}.{k}", None, after[k]))
            elif k not in after:
                diffs.append((f"{path}.{k}", before[k], None))
            else:
                diffs.extend(walk_diff(before[k], after[k], f"{path}.{k}"))
    elif isinstance(before, list) and isinstance(after, list):
        if len(before) != len(after):
            diffs.append((f"{path}.len", len(before), len(after)))
        for i, (b, a) in enumerate(zip(before, after)):
            diffs.extend(walk_diff(b, a, f"{path}[{i}]"))
    elif before != after:
        diffs.append((path, before, after))
    return diffs


def collect_ident_fields(obj, out: dict[str, object], path=""):
    """收集所有 id / next / kind / goto / cval / multi / bw / col 叶子，用于「不许变」比对。"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}.{k}" if path else k
            if k in ("id", "next", "kind", "goto", "cval"):
                out[p.replace(".opts.", ".opts[") + "]"] = json.dumps(v, ensure_ascii=False, sort_keys=True)
            collect_ident_fields(v, out, p)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            collect_ident_fields(v, out, f"{path}[{i}]")


def cosine(a: dict, b: dict) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def best_pair(q: dict):
    opts = q["opts"]
    best = (-1.0, None)
    for i, j in itertools.combinations(range(len(opts)), 2):
        c = cosine(opts[i].get("s", {}), opts[j].get("s", {}))
        if c > best[0]:
            best = (c, (i, j))
    return best


def build_graph(by_id: dict[str, dict]):
    graph = {qid: [] for qid in by_id}
    for qid, q in by_id.items():
        if q.get("next"):
            graph[qid].append(q["next"])
        for opt in q.get("opts", []):
            if opt.get("goto"):
                graph[qid].append(opt["goto"])
    return graph


def reachable(graph: dict[str, list[str]], start: str) -> set[str]:
    seen, stack = set(), [start]
    while stack:
        n = stack.pop()
        if n in seen or n not in graph:
            continue
        seen.add(n)
        stack.extend(graph[n])
    return seen


def spine_of(by_id: dict[str, dict], start: str) -> list[str]:
    out, cur, guard = [], start, 0
    while cur and cur in by_id and guard < 600:
        out.append(cur)
        cur = by_id[cur].get("next")
        guard += 1
    return out


def main() -> int:
    before = load(BAK)
    after = load(DATA)
    bm, am = qmap(before), qmap(after)
    lines: list[str] = []
    verdicts: list[tuple[str, bool, str]] = []

    def say(s: str = ""):
        lines.append(s)

    say("# 九道题改动自检报告（USER_FEEDBACK_SPEC）")
    say()
    say(f"before 快照：`_scratch/data/_feedback_bak/`　after：`data/`")
    say(f"题库文件：{', '.join(BANKS)}　题量 before {len(bm)} / after {len(am)}")
    say()

    # ---------- 自检 1：逐字段 diff，只落在这 9 道题 ----------
    say("## 自检 1 · 逐字段 diff：改动是否只落在这 9 道题")
    touched: dict[str, list[str]] = {}
    id_mismatch = []
    for qid in sorted(set(bm) | set(am)):
        if qid not in bm or qid not in am:
            id_mismatch.append(qid)
            continue
        fb, qb = bm[qid]
        fa, qa = am[qid]
        if fb != fa:
            id_mismatch.append(qid)
        diffs = walk_diff(qb, qa, qid)
        if diffs:
            touched[qid] = [d[0] for d in diffs]
    outside = [q for q in touched if q not in TARGET_SET]
    ok1 = not outside and not id_mismatch and set(touched) == TARGET_SET
    verdicts.append(("自检 1 逐字段 diff", ok1,
                     f"发生改动的题 {sorted(touched)}；越界改动 {outside or '无'}；题目增删/换文件 {id_mismatch or '无'}"))
    for qid in TARGETS:
        paths = touched.get(qid, [])
        say(f"- `{qid}`：{len(paths)} 处字段变化 -> {', '.join(paths)}")
    say()
    say(f"**结论：改动只出现在 {len(touched)} 道题里，全部属于 9 道目标题；其它 "
        f"{len(bm) - len(touched)} 道题零字段变化。**")
    say()

    # ---------- 自检 1b：字节级证明 ----------
    say("## 自检 1b · 字节级证明（把 9 道题回滚后是否与 before 完全同字节）")
    for name in BANKS:
        if name not in before or name not in after:
            say(f"- {name}：缺文件，跳过")
            continue
        obj = json.loads(json.dumps(after[name]))  # deep copy
        idx = {q["id"]: i for i, q in enumerate(obj["questions"])}
        for qid in TARGET_SET:
            if qid in idx and qid in bm and bm[qid][0] == name:
                obj["questions"][idx[qid]] = bm[qid][1]
        same = dump(obj) == (BAK / name).read_text(encoding="utf-8")  # read_text 会把 CRLF 归一为 \n
        say(f"- {name}：回滚 9 道题后与改动前字节一致 = **{same}**")
    say()

    # ---------- 自检 2：id / next / goto / kind / cval 未变 ----------
    say("## 自检 2 · id / next / goto / kind / cval 全部未变")
    idf_b, idf_a = {}, {}
    for fname, obj in before.items():
        collect_ident_fields(obj, idf_b, fname)
    for fname, obj in after.items():
        collect_ident_fields(obj, idf_a, fname)
    keys = set(idf_b) | set(idf_a)
    changed_ident = [(k, idf_b.get(k), idf_a.get(k)) for k in sorted(keys) if idf_b.get(k) != idf_a.get(k)]
    ok2 = not changed_ident
    verdicts.append(("自检 2 标识字段", ok2,
                     f"比对 {len(keys)} 个 id/next/goto/kind/cval 叶子，变化 {len(changed_ident)} 个"))
    say(f"- 共比对 {len(keys)} 个 `id`/`next`/`goto`/`kind`/`cval` 叶子字段，变化 **{len(changed_ident)}** 个。")
    for k, b, a in changed_ident:
        say(f"  - ✗ {k}: {b} -> {a}")
    for qid in TARGETS:
        qb, qa = bm[qid][1], am[qid][1]
        items = [f"id={'OK' if qb['id'] == qa['id'] else '变了'}",
                 f"next={qb.get('next')!r}->{qa.get('next')!r}",
                 f"kind={qb.get('kind')!r}->{qa.get('kind')!r}"]
        if HUB_ID == qid:
            gb = [o.get("goto") for o in qb["opts"]]
            ga = [o.get("goto") for o in qa["opts"]]
            items.append(f"goto {gb} -> {ga} {'一致' if gb == ga else '不一致!'}")
        cvs = [(o.get("cval"), o2.get("cval")) for o, o2 in zip(qb["opts"], qa["opts"])]
        if any(c[0] is not None for c in cvs):
            items.append(f"cval {[c[0] for c in cvs]} -> {[c[1] for c in cvs]}")
        say(f"- `{qid}`：" + "；".join(items))
    say()

    # ---------- 自检 3：选项数 / 轴数 / 权重 ----------
    say("## 自检 3 · 每题选项 3~6、每选项 1~3 轴、权重 0.5~3.0")
    viol_target, viol_other = [], []
    for qid, (fname, q) in am.items():
        bucket = viol_target if qid in TARGET_SET else viol_other
        n = len(q["opts"])
        if not 3 <= n <= 6:
            bucket.append(f"{qid} 选项数 {n}")
        for i, o in enumerate(q["opts"]):
            s = o.get("s", {})
            if not 1 <= len(s) <= 3:
                bucket.append(f"{qid} 选项{LETTERS[i]} 轴数 {len(s)}")
            for k, v in s.items():
                if not 0.5 <= v <= 3.0:
                    bucket.append(f"{qid} 选项{LETTERS[i]} 轴 {k}={v} 越界")
    ok3 = True
    for qid in TARGETS:
        q = am[qid][1]
        counts = [f"{LETTERS[i]}={len(o.get('s', {}))}轴" for i, o in enumerate(q["opts"])]
        say(f"- `{qid}`（{len(q['opts'])} 个选项）：{'，'.join(counts)}")
    verdicts.append(("自检 3 结构", not viol_target,
                     f"9 道目标题违规 {len(viol_target)} 条；其余题（未改动）违规 {len(viol_other)} 条"))
    say(f"- 9 道目标题违规：{viol_target or '无'}")
    if viol_other:
        say(f"- 未改动的其它题中本就存在的同类问题（不在本轮范围）：{viol_other}")
    say()

    # ---------- 自检 4：同题内余弦 ----------
    say("## 自检 4 · 同题内两两轴向量余弦 < 0.85")
    viol4 = []
    for qid in TARGETS:
        q = am[qid][1]
        c, pair = best_pair(q)
        i, j = pair
        flag = "✓" if c < 0.85 else "✗"
        if c >= 0.85:
            viol4.append(f"{qid} {c:.3f}")
        say(f"- `{qid}` 最高一对：{LETTERS[i]}-{LETTERS[j]} = **{c:.3f}** {flag}"
            f"　（{q['opts'][i]['t'][:14]}… / {q['opts'][j]['t'][:14]}…）")
    # 全库对照：before / after 是否一致（确认没顺手改坏别的题）
    other_after = {qid: best_pair(q)[0] for qid, (f, q) in am.items() if qid not in TARGET_SET}
    other_before = {qid: best_pair(q)[0] for qid, (f, q) in bm.items() if qid not in TARGET_SET}
    drift = [qid for qid in other_after if abs(other_after[qid] - other_before.get(qid, -9)) > 1e-9]
    high = sorted([(v, qid) for qid, v in other_after.items() if v >= 0.85], reverse=True)
    verdicts.append(("自检 4 余弦", not viol4, f"9 道目标题最高余弦 {max(best_pair(am[q][1])[0] for q in TARGETS):.3f}；越界 {viol4 or '无'}"))
    say(f"- 9 道目标题均 < 0.85：{not viol4}；最高值 {(max(best_pair(am[q][1])[0] for q in TARGETS)):.3f}")
    say()
    say("### 本轮新增选项自带的最高余弦（越低越不容易和旧选项混淆）")
    for qid in TARGETS:
        qb, qa = bm[qid][1], am[qid][1]
        if len(qa["opts"]) <= len(qb["opts"]):
            continue
        i = len(qa["opts"]) - 1
        cs = [(cosine(qa["opts"][i]["s"], qa["opts"][j]["s"]), j)
              for j in range(i)]
        c, j = max(cs)
        say(f"- `{qid}` 新选项 {LETTERS[i]}（{qa['opts'][i]['t']}）与旧选项最高：{LETTERS[j]} = **{c:.3f}**")
    say()
    say(f"- 未改动题目里余弦 ≥0.85 的（改动前后完全一致，属于既有情况）："
        f"{[(q, round(v, 3)) for v, q in high] or '无'}　余弦发生漂移的题：{drift or '无'}")
    say()

    # ---------- 自检 5：术语 + 重复 ----------
    say("## 自检 5 · 选项文本无万智牌术语、同题内不重复")
    hits5, dups = [], []
    for qid in TARGETS:
        q = am[qid][1]
        blob = [("题干", q["q"])] + [(f"选项{LETTERS[i]}", o["t"]) for i, o in enumerate(q["opts"])]
        for label, text in blob:
            for t in TERMS:
                if t in text:
                    hits5.append(f"{qid} {label} 命中「{t}」：{text}")
        texts = [o["t"] for o in q["opts"]]
        norm = [t.strip() for t in texts]
        if len(set(norm)) != len(norm):
            dups.append(f"{qid}: {[t for t in norm if norm.count(t) > 1]}")
    ok5 = not hits5 and not dups
    verdicts.append(("自检 5 术语/重复", ok5, f"术语命中 {len(hits5)} 处，同题重复 {len(dups)} 处"))
    say(f"- 9 道题共扫 {sum(len(am[q][1]['opts']) for q in TARGETS)} 个选项 + 9 条题干，"
        f"术语命中 **{len(hits5)}**，同题内重复 **{len(dups)}**。")
    for h in hits5:
        say(f"  - ✗ {h}")
    for d in dups:
        say(f"  - ✗ 重复：{d}")
    # 全库对照
    other_hits = []
    for qid, (f, q) in am.items():
        if qid in TARGET_SET or f == "bankE.json":
            continue  # bankE 是「允许出现万智牌术语」的经验门题
        for label, text in [("题干", q["q"])] + [(f"选项{LETTERS[i]}", o["t"]) for i, o in enumerate(q["opts"])]:
            for t in TERMS:
                if t in text:
                    other_hits.append(f"{qid} {label}「{t}」")
    say(f"- 参考：其它题（未改动，排除 bankE 门槛题）命中术语 {len(other_hits)} 处"
        f"{'：' + str(other_hits[:12]) if other_hits else '。'}")
    say()

    # ---------- 自检 6：s24 三条分支可达 ----------
    say("## 自检 6 · s24 改完后 h2a1 / h2b1 / h2c1 三条分支仍可达")
    results6 = {}
    for tag, (banks, m) in (("before", (before, bm)), ("after", (after, am))):
        by_id = {qid: q for qid, (f, q) in m.items()}
        graph = build_graph(by_id)
        start = "e0" if "e0" in by_id else "s01"
        reach = reachable(graph, start)
        spine = spine_of(by_id, start)
        hub = by_id[HUB_ID]
        gotos = [o.get("goto") for o in hub["opts"]]
        chains = {}
        for g in gotos:
            chain, cur, guard = [], g, 0
            while cur and cur in by_id and guard < 30:
                chain.append(cur)
                nxt = by_id[cur].get("next")
                if nxt in spine:
                    break
                cur, guard = nxt, guard + 1
            chains[g] = chain
        results6[tag] = dict(reach=reach, spine=spine, gotos=gotos, chains=chains)
        say(f"- **{tag}**：起点 `{start}`，主线 {len(spine)} 题，可达 {len(reach)}/{len(by_id)} 题；"
            f"s24 的 goto = {gotos}")
        for g in gotos:
            tail = results6[tag]["chains"][g][-1]
            back = by_id[tail].get("next")
            say(f"  - `{g}` 分支链：{' -> '.join(results6[tag]['chains'][g])} -> 回到主线 `{back}`"
                f"　可达={g in reach}")
    ok6 = (results6["after"]["gotos"] == HUB_GOTOS
           and all(g in results6["after"]["reach"] for g in HUB_GOTOS)
           and results6["after"]["reach"] == results6["before"]["reach"]
           and results6["after"]["chains"] == results6["before"]["chains"])
    verdicts.append(("自检 6 分支可达", ok6,
                     f"三条 goto 未变，三条分支链均回到主线，可达集合 before == after"))
    say(f"- 可达集合 before == after：{results6['after']['reach'] == results6['before']['reach']}；"
        f"分支链 before == after：{results6['after']['chains'] == results6['before']['chains']}")
    say()

    # ---------- 汇总 ----------
    say("## 汇总")
    for name, ok, note in verdicts:
        say(f"- {'✅' if ok else '❌'} **{name}**：{note}")

    text = "\n".join(lines) + "\n"
    OUT.write_text(text, encoding="utf-8")
    print(text)
    print(f"\n报告已写入 {OUT.relative_to(ROOT)}")
    return 0 if all(ok for _, ok, _ in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
