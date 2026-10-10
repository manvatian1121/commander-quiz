# -*- coding: utf-8 -*-
"""修正 bank3.json / bank4.json 的两类选项设计缺陷（按 FIX_SPEC.md）。

修正一：缺「不在意」选项 —— 别人造成的不利处境 + 选项全是主动反应
修正二：正负选项配平 —— 倾向性问句，会/不会两组悬殊超过 3:2

做法：文本级精确替换（保住原文件的缩进 / 紧凑单行格式），只插入新选项，
不改题干、其它选项、轴得分、id、next、goto。
源文件是 data/_backup_bank3_prefix.json / _backup_bank4_prefix.json（改动前快照）。

Run:  python fix_bank34_options.py
"""
import json
import sys
from pathlib import Path



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

DATA = Path(ROOT / "data")
PAIRS = [
    ("bank3", DATA / "_backup_bank3_prefix.json", DATA / "bank3.json"),
    ("bank4", DATA / "_backup_bank4_prefix.json", DATA / "bank4.json"),
]

I8 = " " * 8    # option object level  (bank3 pretty-printed)
I10 = " " * 10  # "t" / "s" level
I12 = " " * 12  # axis level
I14 = " " * 14  # weight level
BANK4_INDENT = " " * 8  # bank4 options are one-liners inside the opts list


def pretty_opt(text, scores, trailing_comma=True):
    """bank3 风格：多行展开的 option 对象（含前导换行）。"""
    out = [f'\n{I8}{{', f'\n{I10}"t": {json.dumps(text, ensure_ascii=False)},', f'\n{I10}"s": {{']
    items = list(scores.items())
    for i, (a, w) in enumerate(items):
        comma = "," if i + 1 < len(items) else ""
        out.append(f'\n{I12}"{a}": {w:.1f}{comma}')
    out.append(f'\n{I10}}}')
    out.append(f'\n{I8}}}' + ("," if trailing_comma else ""))
    return "".join(out)


def compact_opt(text, scores, trailing_comma=True):
    """bank4 风格：单行紧凑的 option 对象。"""
    body = ", ".join(f'"{a}": {w:.1f}' for a, w in scores.items())
    tail = "," if trailing_comma else ""
    return (f'\n{BANK4_INDENT}{{"t": {json.dumps(text, ensure_ascii=False)}, '
            f'"s": {{{body}}}}}{tail}')


def anchor_for(text, scores):
    """bank3 风格：整段 option 对象原文，用于定位插入点（保留原打分，不带逗号）。"""
    out = [f'{I8}{{', f'\n{I10}"t": {json.dumps(text, ensure_ascii=False)},', f'\n{I10}"s": {{']
    items = list(scores.items())
    for i, (a, w) in enumerate(items):
        comma = "," if i + 1 < len(items) else ""
        out.append(f'\n{I12}"{a}": {w:.1f}{comma}')
    out.append(f'\n{I10}}}')
    out.append(f'\n{I8}}}')
    return "".join(out)


# (filekey, qid, 新选项文本, 新选项轴得分, 'after', 锚点选项原文, 锚点轴得分, 风格, 锚点 goto)
EDITS = [
    # ---------------- bank3 / social ----------------
    # 修正一：拼团被商家咬价（别人造成的处境），4 个选项全是主动应对
    ("bank3", "s35",
     '那就算了，这个价我就不买了',
     {"chaos": 2.0, "drain": 1.5}, 'after',
     '我来当团长，先把人凑齐，账我记着，最后按人均分',
     {"stax": 2.0, "wide": 1.5, "artifacts": 1.0}, 'pretty', None),

    # 修正一：室友堆碗（别人造成的处境），4 个选项全是主动应对
    ("bank3", "s36",
     '不在意，堆就堆着吧，我不着急用',
     {"drain": 1.5, "chaos": 1.0, "politics": 2.0}, 'after',
     '我洗了。但心里开始给他减分，减到零就搬走',
     {"drain": 2.0, "control": 1.5}, 'pretty', None),

    # 修正一：合买被别人多占（别人造成的处境），4 个选项全是主动应对
    ("bank3", "s42",
     '懒得算谁用多谁用少，反正买回来就是给大家用的',
     {"drain": 2.5, "chaos": 1.5, "stompy": 1.0}, 'after',
     '干脆再买一份自己用，省得争',
     {"artifacts": 2.0, "clonesteal": 1.5, "combo": 1.0}, 'pretty', None),

    # 修正一：你热情招呼的人回得越来越慢（别人造成的处境），4 个选项全是主动应对
    ("bank3", "s44",
     '回得慢就慢吧，我不往心里去，也不缺这一个朋友',
     {"chaos": 2.5, "politics": 1.0, "stompy": 2.0}, 'after',
     '不追了，把热情留给回得快的人',
     {"drain": 2.0, "control": 1.0}, 'pretty', None),

    # 修正一：朋友开口借钱（别人造成的处境），4 个选项全是主动决策
    ("bank3", "h3a2",
     '借了就借了，什么时候还我不惦记，真还不上也不去催',
     {"drain": 2.5, "chaos": 1.5, "grave": 1.5}, 'after',
     '换个说法，把我想要的包装成对他也有好处',
     {"clonesteal": 2.0, "politics": 2.0, "combo": 1.0}, 'pretty', None),

    # 修正一：排队被插队（别人造成的处境），4 个选项全是主动反应
    ("bank3", "h3b1",
     '笑一笑就过去了，几分钟的事，不往心里去',
     {"drain": 2.5, "chaos": 1.5, "stompy": 1.0}, 'after',
     '对他笑一下说「您先请」，然后记着这个人',
     {"chaos": 1.5, "grave": 2.5, "enchant": 1.0}, 'pretty', None),

    # 修正一：群里被人公开说难听话（别人造成的处境），4 个选项全是主动反应
    ("bank3", "h3b2",
     '看到那句话就翻过去了，该干嘛干嘛，不往心里去',
     {"drain": 3.0, "chaos": 1.5, "stompy": 1.0}, 'after',
     '拉几个关系好的人私下聊这事，让他们帮我说',
     {"politics": 2.5, "wide": 1.5, "tribal": 1.0}, 'pretty', None),

    # ---------------- bank4 / taste ----------------
    # 修正二：空墙怎么弄（会/不会 = 3:1），补一个「不弄」的少数派选项 → 3:2
    ("bank4", "s56",
     '先空着，不急着弄，什么时候有兴致了再说',
     {"drain": 2.0, "chaos": 1.5}, 'after',
     '去旧货市场扛一张别人不要的旧柜子回来，自己刷一遍漆',
     {"grave": 2.5, "removal": 1.5, "blink": 1.0}, 'compact', "h4c1"),
]


def main():
    srcs = {}
    for key, backup, target in PAIRS:
        srcs[key] = {
            "backup": backup,
            "target": target,
            "text": backup.read_text(encoding="utf-8"),
        }

    log = []
    for key, qid, text, scores, where, anchor_text, anchor_scores, style, goto in EDITS:
        slot = srcs[key]
        txt = slot["text"]
        if style == "pretty":
            anchor = anchor_for(anchor_text, anchor_scores)
        else:
            body = ", ".join(f'"{a}": {w:.1f}' for a, w in anchor_scores.items())
            base = (f'{BANK4_INDENT}{{"t": {json.dumps(anchor_text, ensure_ascii=False)}, '
                    f'"s": {{{body}}}')
            tail = '}' if goto is None else f', "goto": "{goto}"}}'
            base += tail
            # 锚点旧选项不一定带逗号：两种写法都试，取唯一命中的那个
            cands = [base + ",", base]
            hits = [c for c in cands if txt.count(c) == 1]
            if not hits:
                raise SystemExit(f"[ABORT] {key} {qid}: compact anchor hits "
                                 f"{[txt.count(c) for c in cands]}")
            anchor = hits[0]
        if txt.count(anchor) != 1:
            raise SystemExit(f"[ABORT] {key} {qid}: anchor count = {txt.count(anchor)}")
        # 新选项排在被插入的那一条之后：锚点之后还有别的选项，新选项就需要逗号
        anchor_has_comma = anchor.rstrip().endswith(",")
        blob = (pretty_opt(text, scores, trailing_comma=anchor_has_comma) if style == "pretty"
                else compact_opt(text, scores, trailing_comma=anchor_has_comma))
        if where == "after":
            head = anchor if anchor_has_comma else anchor + ","
            txt = txt.replace(anchor, head + blob)
        else:
            # 新选项永远不是最后一项，必须带逗号
            assert blob.endswith(","), f"{key} {qid}: before-insert blob must keep its comma"
            txt = txt.replace(anchor, blob + anchor)
        slot["text"] = txt
        log.append(f"{key} {qid}: +1 option -> {text}   {scores}")

    # 先验证文本仍然合法 JSON，且改动只发生在 opts 上
    for key, slot in srcs.items():
        before = json.loads(slot["backup"].read_text(encoding="utf-8"))
        after = json.loads(slot["text"])
        assert before["batch"] == after["batch"]
        bids = [q["id"] for q in before["questions"]]
        aids = [q["id"] for q in after["questions"]]
        assert bids == aids, f"{key}: id order changed"
        for b, a in zip(before["questions"], after["questions"]):
            for f in ("q", "sec", "kind", "next"):
                assert b.get(f) == a.get(f), f"{key} {b['id']}: field {f} changed"
            bo = [o for o in b["opts"]]
            ao = [o for o in a["opts"]]
            # 旧选项必须原样保留（顺序不变），只是多了一个
            if len(ao) != len(bo) + 1 and len(ao) != len(bo):
                raise SystemExit(f"{key} {b['id']}: option count {len(bo)} -> {len(ao)}")
            keep = [o for o in ao if o["t"] in [x["t"] for x in bo]]
            assert len(keep) == len(bo), f"{key} {b['id']}: an old option disappeared"
            for o in ao:
                if o["t"] not in [x["t"] for x in bo]:
                    assert 1 <= len(o["s"]) <= 3, f"{key} {b['id']}: new option axes"
                    for w in o["s"].values():
                        assert w in (1.0, 1.5, 2.0, 2.5, 3.0), f"{key} {b['id']}: bad weight {w}"
                    assert len(o["t"]) > 6
            # goto 必须一致
            bg = [(i, o.get("goto")) for i, o in enumerate(bo) if "goto" in o]
            ag = [(o.get("goto")) for o in ao if "goto" in o]
            assert [g for _, g in bg] == ag, f"{key} {b['id']}: goto changed"

    for key, slot in srcs.items():
        slot["target"].write_text(slot["text"], encoding="utf-8")
        print(f"[write] {slot['target']}")

    print()
    for line in log:
        print("  " + line)
    print(f"\n{len(EDITS)} edits applied.")


if __name__ == "__main__":
    main()
