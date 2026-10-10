#!/usr/bin/env python3
"""从 before 快照与当前题库生成逐题改动清单 data/USER_FEEDBACK_CHANGES.md。"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
BAK = ROOT / "_scratch" / "data" / "_feedback_bak"
OUT = DATA / "USER_FEEDBACK_CHANGES.md"
LETTERS = "ABCDEFGH"

# (图号, 反馈, 文件, id, 为什么这样改)
ITEMS = [
    ("图1", "缺一个「呆在家里打游戏或者躺着」的选项", "bank1.json", "s04",
     "新增 F，落在「低投入 / 自己待着 / 不折腾」：轴用 drain（不喜欢正面冲突、慢慢耗）+ control 0.5；"
     "与现有 5 个「出门 / 在家做事」选项的余弦全为 0。"),
    ("图2", "缺一个「不改变」的选项（B 只是嫌麻烦）", "bank1.json", "h1c3",
     "新增 E，写成无条件的「不换」：轴 grave（念旧、守着旧的）+ drain（不折腾、不正面冲突），"
     "与 B「太麻烦就不折腾」的条件式、D「两个一起玩」并列区分。"),
    ("图3", "B「两台都买回来用一周」不现实", "bank2.json", "s19",
     "按建议改成真实购买策略「先划一条硬底线……剩下的全凭顺眼」：轴由 wide/aggro/artifacts "
     "换成 stax（定规矩、定底线）+ enchant（顺眼、眼缘），与 A「参数表逐项比」的 artifacts/removal 完全分开。"),
    ("图4", "B 和 C 都在问「下行风险」，重复（枢纽题，只能改措辞）", "bank2.json", "s24",
     "B 改写成纯「承受能力」（我手上有多少钱和精力 = 资源够不够兜），C 改写成纯「可逆性」"
     "（能不能**原样**退回来）；两者轴与 goto 一律不动，所以题目的分流与计分完全不受影响。"),
    ("图5", "缺一个最直白的「你，把碗洗了」", "bank3.json", "s36",
     "新增 F 直白要求：「直接跟他说，「你的碗，你自己洗」」：轴 aggro（直来直去、先开口）+ "
     "removal（对症下药、把毛病点掉）。与 A 排值日表（制度化）、D 划清界限、E 当面阴阳都不同档。"),
    ("图6", "缺一个「阴阳怪气的反击」", "bank3.json", "s45",
     "新增 E：「笑着把话扎回去」：轴 politics（社交手段、谈判式报复）+ chaos（不按套路、出其不意）。"
     "因为 A 已经是正面硬刚，这一档刻意不给 aggro，避免和 A 撞轴。"),
    ("图7", "现代人更多刷视频；可以加动画类", "bank4.json", "s50",
     "① 题干从「打开电视…哪一类片子」改成「窝在沙发上…哪一类？（长片、短视频都算）」；"
     "② 新增 F「动画、番剧这类，认准的那几部一直追下去」：轴 tribal（对某个题材专一、成套追）+ "
     "enchant（好看、喜欢这种氛围），与 E「一口气连刷到凌晨」的量级追剧区分开。"),
    ("图8", "可以加有声小说 / 知识类音频", "bank4.json", "s51",
     "新增 F「有声书、播客这类，听的是内容不是音乐」：轴 ramp（囤信息、提前储备）+ counters（每天听一点、长期投入），"
     "与全是音乐的前 5 个选项余弦全为 0。"),
    ("图9", "B「看人下菜…跟不熟的就用」语句不通、成语贬义（约束题）", "bankC.json", "c05",
     "只改句子：「看跟谁玩。熟人局就随便打打，不熟的人我可不会留手」——去掉贬义成语、补全宾语"
     "（对不熟的人不留手），语义仍是「看对象决定用不用」。cval（salt 2）与轴（clonesteal 1.94）都不动，"
     "所以这一档的难度/咸度画像和得分分布完全不变。"),
]


def main() -> int:
    bm, am = {}, {}
    for p in BAK.glob("*.json"):
        for q in json.loads(p.read_text(encoding="utf-8")).get("questions", []):
            bm[q["id"]] = (p.name, q)
    for p in DATA.glob("*.json"):
        if p.name in {x[2] for x in ITEMS}:
            for q in json.loads(p.read_text(encoding="utf-8")).get("questions", []):
                am[q["id"]] = (p.name, q)

    lines = ["# 九道题的逐题改动清单（用户实测反馈）", "",
             "来源：`data/USER_FEEDBACK_SPEC.md`　before 快照：`_scratch/data/_feedback_bak/`", "",
             "> 说明：9 道题实际分布在 `bank1~bank4.json` 与 `bankC.json`（spec 里写的「都在 bank1.json」与文件不符，"
             "已按题目的真实归属改）。", ""]

    for fig, fb, fname, qid, why in ITEMS:
        fb_name, qb = bm[qid]
        fa_name, qa = am[qid]
        lines.append(f"## {fig} · `{qid}`　（{fa_name}）")
        lines.append("")
        lines.append(f"- 用户反馈：{fb}")
        lines.append(f"- 改动前：{len(qb['opts'])} 个选项　改动后：{len(qa['opts'])} 个选项")
        if qb["q"] != qa["q"]:
            lines.append(f"- 题干：`{qb['q']}`　→　`{qa['q']}`")
        lines.append("")
        lines.append("| 选项 | 旧文本 | 新文本 | 旧轴 | 新轴 |")
        lines.append("|---|---|---|---|---|")
        n = max(len(qb["opts"]), len(qa["opts"]))
        for i in range(n):
            ob = qb["opts"][i] if i < len(qb["opts"]) else None
            oa = qa["opts"][i] if i < len(qa["opts"]) else None
            old_t = f"**{ob['t']}**" if ob and (not oa or ob["t"] != oa["t"]) else (ob["t"] if ob else "（新增）")
            new_t = f"**{oa['t']}**" if oa and (not ob or ob["t"] != oa["t"]) else (oa["t"] if oa else "—")
            old_s = json.dumps(ob["s"], ensure_ascii=False) if ob else "—"
            new_s = json.dumps(oa["s"], ensure_ascii=False) if oa else "—"
            if ob and oa and ob["s"] == oa["s"]:
                old_s = new_s = new_s + "（不变）"
            lines.append(f"| {LETTERS[i]} | {old_t} | {new_t} | {old_s} | {new_s} |")
        lines.append("")
        lines.append(f"**为什么这样改**：{why}")
        lines.append("")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"✓ 写出 {OUT.relative_to(ROOT)}（{len(lines)} 行）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
