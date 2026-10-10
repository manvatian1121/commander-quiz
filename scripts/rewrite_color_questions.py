#!/usr/bin/env python3
"""改写 bank4.json 里的 4 道颜色题（s49 / s59 / s60 / s62）。

只碰这四道题的 `q` 与每个选项的 `t` / `s` / `col`：
id、sec、next、题目顺序、其它 21 道题一律不动。

设计（详见 data/COLOR_Q_SPEC.md）：
    四道题考察颜色的四个不同侧面，且颜色在 A~E 五个位置上的排列是错开的
    （同一列不出现重复颜色），彻底消除「同一位置总是同一个颜色/轴」的问题。

    位置    Q1(s49)   Q2(s59)   Q3(s60)   Q4(s62)
    A        U         W         B         R
    B        B         R         G         U
    C        G         B         U         W
    D        W         U         R         G
    E        R         G         W         B

用法：
    python rewrite_color_questions.py            # 预演，不写文件
    python rewrite_color_questions.py --apply    # 实际写入
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
BANK = ROOT / "data" / "bank4.json"
BACKUP = ROOT / "_scratch" / "data" / "_colorq_backup_bank4.json"

APPLY = "--apply" in sys.argv

# ---------------------------------------------------------------- 新内容
# ① s49：怎么对待过去（怀旧 / 记录 / 纪念 / 翻篇）
S49 = {
    "q": "有件事对你挺重要（搬去新城市、换掉一份工作、跟谁分开），"
         "已经过去好几年了。现在每到那一天，你一般会？",
    "opts": [
        ("把当时的照片、聊天记录、写下的东西翻出来，按年份归到一处，标清楚是哪一年",
         {"control": 2.0, "artifacts": 1.5, "grave": 1.0}, "U"),
        ("不跟任何人提，也不主动去翻，但心里一直记着这件事",
         {"drain": 2.0, "grave": 1.0}, "B"),
        ("把当年一起的人叫出来吃一顿，一年凑一次，一次都没断过",
         {"tribal": 2.0, "counters": 1.0}, "G"),
        ("还是老规矩：那一天去同一个地方、做同一件事，年年如此",
         {"stax": 1.5, "enchant": 1.5}, "W"),
        ("那一天跟平常没什么两样，早翻篇了，该干嘛干嘛",
         {"chaos": 2.5}, "R"),
    ],
}

# ② s59：拿到新东西的第一反应（求知 / 上手 / 收好 / 先用旧的 / 慢养）
S59 = {
    "q": "新买的东西到了，箱子就摆在桌上。接下来你多半会？",
    "opts": [
        ("拆完先把附件、保修卡收回盒里，一件不落，往后要用随时能翻出来",
         {"stax": 1.5, "blink": 1.0, "ramp": 1.0}, "W"),
        ("插上电就用，说明书扔一边，坏了再说",
         {"aggro": 2.0, "spells": 1.5}, "R"),
        ("先用旧的，新的原封放着——旧的彻底不能用了再拆",
         {"grave": 2.5}, "B"),
        ("先把说明书翻完，再找拆解视频看看里头是怎么运作的",
         {"combo": 2.0, "control": 1.5}, "U"),
        ("不急着一次用透，先摆到顺手的位置天天用，越用越合手，顺手把耗材备上",
         {"enchant": 1.5, "counters": 1.0, "ramp": 1.0}, "G"),
    ],
}

# ③ s60：面对规则和约束（遵守 / 弄清 / 绕开 / 无视 / 顺应）
S60 = {
    "q": "碰上一条你觉得不合理、可它就在那儿管着你的规定，你一般会？",
    "opts": [
        ("不跟它硬顶。先找一条它管不到的路，把该备的备好，再绕过去把事办了",
         {"combo": 1.5, "ramp": 1.0, "drain": 1.0}, "B"),
        ("先看周围大多数人怎么办——大家都不当回事，我也不当回事",
         {"wide": 2.0, "tribal": 1.5}, "G"),
        ("先去找定这条规定的人，或者翻出它的出处，弄清楚它到底在管什么",
         {"clonesteal": 2.0, "control": 1.0}, "U"),
        ("懒得研究，先做了再说，真有人拦我再讲",
         {"aggro": 2.0, "chaos": 1.5}, "R"),
        ("规定怎么写就怎么做；有人不照做，我还会提醒他一句",
         {"stax": 2.0, "politics": 1.0}, "W"),
    ],
}

# ④ s62：在群体里的位置（组织者 / 观察者 / 独行者 / 先动手的 / 管东西的）
S62 = {
    "q": "一群人凑在一起弄同一件事，做上几周，你在里面自然就成了——",
    "opts": [
        ("先动手的那个：别人还在商量，我已经开工了，出了岔子我先上",
         {"aggro": 2.0, "voltron": 1.5}, "R"),
        ("先不急着说话的那个：谁跟谁熟、谁说了算，我看清楚了才开口",
         {"control": 2.0, "politics": 1.0}, "U"),
        ("张罗的那个：时间、分工我来定，人我来拢",
         {"wide": 2.0, "politics": 1.5}, "W"),
        ("管东西的那个：水、吃的、备用的我提前备齐，缺了再一点点补上",
         {"ramp": 2.0, "wide": 1.0, "counters": 1.0}, "G"),
        ("不站队也不抱团的那个：自己那份做好就行，别来安排我的时间",
         {"drain": 2.0, "stax": 1.0}, "B"),
    ],
}

NEW = {"s49": S49, "s59": S59, "s60": S60, "s62": S62}


def main() -> int:
    payload = json.loads(BANK.read_text(encoding="utf-8"))
    questions = payload["questions"]

    before = {q["id"]: (q["q"], q.get("next"), len(q["opts"])) for q in questions}

    for q in questions:
        spec = NEW.get(q["id"])
        if not spec:
            continue
        if len(q["opts"]) != 5:
            print(f"✗ {q['id']} 选项数不是 5（{len(q['opts'])}），拒绝改写")
            return 1
        q["q"] = spec["q"]
        for opt, (text, scores, color) in zip(q["opts"], spec["opts"]):
            opt["t"] = text
            opt["s"] = scores
            opt["col"] = {color: 2.0}

    # 复核：只改了该改的字段
    after = {q["id"]: (q["q"], q.get("next"), len(q["opts"])) for q in questions}
    if set(before) != set(after):
        print("✗ 题目集合发生变化")
        return 1
    for qid in before:
        if before[qid][1] != after[qid][1] or before[qid][2] != after[qid][2]:
            print(f"✗ {qid} 的 next 或选项数被改动")
            return 1
    changed = [qid for qid in before if before[qid][0] != after[qid][0]]
    print(f"题干改动：{changed}（期望 ['s49', 's59', 's60', 's62']）")
    for qid in ["s49", "s59", "s60", "s62"]:
        print(f"  {qid}: next={after[qid][1]!r} 选项数={after[qid][2]}")

    if not APPLY:
        print("\n（预演模式，未写入。加 --apply 执行。）")
        return 0

    if not BACKUP.exists():
        print(f"✗ 没找到备份 {BACKUP}，拒绝写入")
        return 1
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    BANK.write_text(text, encoding="utf-8")
    print(f"\n✓ 已写入 {BANK}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
