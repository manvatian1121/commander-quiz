#!/usr/bin/env python3
"""核对用户反馈的 9 处改动是否都进了成品 HTML。"""
from __future__ import annotations

import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)
html = (ROOT / "commander_quiz.html").read_text(encoding="utf-8")
md = (ROOT / "commander_quiz.md").read_text(encoding="utf-8")

# (说明, 必须出现的新文案, 必须消失的旧文案)
CHECKS = [
    ("图1 s04 加躺平选项",
     "在家躺着打游戏，一天不出门，饭都懒得做", None),
    ("图2 h1c3 加「不换」",
     "不换。我就接着玩这个，新的再好也提不起兴趣", None),
    ("图3 s19 改写 B",
     "先划一条硬底线：有一条指标绝不能让步，剩下的全凭顺眼",
     "干脆两台都买回来用一周，留顺手的那台"),
    ("图4 s24 B 改承受能力",
     "真砸了，我手上的钱和精力扛不扛得住",
     "最坏能坏到哪，我兜不兜得住"),
    ("图4 s24 C 改可逆性",
     "万一走错了，还能不能原样退回来",
     "万一走错了，我还能不能回来"),
    ("图5 s36 加直白要求",
     "直接跟他说，「你的碗，你自己洗」", None),
    ("图6 s45 加阴阳反击",
     "笑着把话扎回去，让他当着人下不来台", None),
    ("图7 s50 题干覆盖刷视频",
     "周末晚上窝在沙发上，你会点开哪一类？（长片、短视频都算）",
     "周末晚上打开电视，你会点开哪一类片子？"),
    ("图7 s50 加动画类",
     "动画、番剧这类，认准的那几部一直追下去", None),
    ("图8 s51 加有声书",
     "有声书、播客这类，听的是内容不是音乐", None),
    ("图9 c05 改通句子",
     "看跟谁玩。熟人局就随便打打，不熟的人我可不会留手",
     "看人下菜。跟熟人就随便玩，跟不熟的用"),
]

fail = 0
print("=== 九处反馈改动的落地核对 ===")
for label, must_have, must_gone in CHECKS:
    ok_html = must_have in html
    ok_md = must_have in md
    gone_ok = (must_gone is None) or (must_gone not in html and must_gone not in md)
    ok = ok_html and ok_md and gone_ok
    if not ok:
        fail += 1
    detail = f"HTML={'✓' if ok_html else '✗'} MD={'✓' if ok_md else '✗'}"
    if must_gone:
        detail += f" 旧文案已消失={'✓' if gone_ok else '✗'}"
    print(f"  {'✓' if ok else '✗'} {label:<22} {detail}")

print(f"\n=== 结构核对 ===")
raw = re.search(r'<script id="payload" type="application/json">(.*?)</script>',
                html, re.S).group(1).replace("<\\/", "</")
data = json.loads(raw)
qs = {q["id"]: q for q in data["quiz"]["questions"]}
for qid, want in [("s04", 6), ("h1c3", 5), ("s19", 5), ("s24", 3),
                  ("s36", 6), ("s45", 5), ("s50", 6), ("s51", 6), ("c05", 4)]:
    got = len(qs[qid]["opts"])
    ok = got == want
    if not ok:
        fail += 1
    print(f"  {'✓' if ok else '✗'} {qid}: {got} 个选项（预期 {want}）")

s24 = qs["s24"]
gotos = [o.get("goto") for o in s24["opts"]]
print(f"  {'✓' if gotos == ['h2a1', 'h2b1', 'h2c1'] else '✗'} s24 的三条分支：{gotos}")
c05 = qs["c05"]
print(f"  c05 的 cval 保留：{c05['opts'][1].get('cval')}")

print()
if fail:
    print(f"✗ {fail} 项未通过")
    sys.exit(1)
print("✓ 九处改动全部落地，结构无误")
