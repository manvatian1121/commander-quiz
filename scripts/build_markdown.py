#!/usr/bin/env python3
"""生成 Markdown 文档版：题目全文 + 算分表 + 主将池（含介绍与建牌思路）。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)
DATA = ROOT / "data"

AXIS_ZH = {
    "aggro": "快攻压制", "voltron": "主将单挑", "wide": "铺场爆兵", "ramp": "加速爆费",
    "stompy": "大生物压制", "control": "控制反击", "removal": "精准互动", "combo": "组合技",
    "spells": "法术连发", "artifacts": "神器机械", "enchant": "结界灵气", "grave": "坟场复用",
    "tribal": "生物部落", "drain": "吸血消耗", "stax": "锁场剥夺", "clonesteal": "复制偷取",
    "politics": "政治博弈", "chaos": "随机搞事", "counters": "指示物增殖", "blink": "进场触发",
}
AXIS_DESC = {
    "aggro": "低费生物早早铺开，抢先手把人打死",
    "voltron": "把主将本人养成巨威胁，靠主将伤害取胜",
    "wide": "造一大堆小兵，人多打人少",
    "ramp": "疯狂找地加速，早早打出超大咒语",
    "stompy": "单只巨兽就够吓人，硬碰硬",
    "control": "反击咒语、清场，拖到后期靠资源优势赢",
    "removal": "点杀、拆神器结界，见招拆招",
    "combo": "找齐特定几张牌凑成无限连",
    "spells": "以瞬间法术为主，一回合连打多张",
    "artifacts": "神器、装备、载具为核心",
    "enchant": "结界、灵气、传纪为核心",
    "grave": "把牌送进坟场再反复捞回来用",
    "tribal": "围绕某个生物类别组牌",
    "drain": "生命差玩法，吸取对手生命慢慢磨死",
    "stax": "让对手做不了事：弃牌、锁地、加税",
    "clonesteal": "复制自己的牌或偷对手的牌来用",
    "politics": "谈判、结盟、君主、借刀杀人",
    "chaos": "骰子、赌博、混乱效应",
    "counters": "＋1/＋1 指示物、增殖、堆叠成长",
    "blink": "反复把生物闪现回场，重复触发进场异能",
}
CVAL_ZH = {"complex": "复杂度容忍", "budget": "预算档", "salt": "咸度容忍"}
LETTERS = "ABCDEFG"


def load_json(name: str, default=None):
    path = DATA / name
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def fmt_scores(opt: dict) -> str:
    bits = []
    for axis, value in sorted((opt.get("s") or {}).items(), key=lambda kv: -kv[1]):
        bits.append(f"{AXIS_ZH.get(axis, axis)}+{value:g}")
    for color, value in (opt.get("col") or {}).items():
        bits.append(f"色{color}+{value:g}")
    for key, value in (opt.get("cval") or {}).items():
        bits.append(f"{CVAL_ZH.get(key, key)}={value:g}")
    return "、".join(bits) if bits else "—"


def main() -> None:
    quiz = load_json("questions.json")
    payload = load_json("commanders.json")
    tag_zh = load_json("tag_zh.json", {})
    cmds = payload["commanders"]

    descriptions: dict[str, dict] = {}
    for index in range(1, 21):
        descriptions.update(load_json(f"descriptions_{index}.json", {}) or {})
    card_display = load_json("card_display.json", {})
    card_zh = load_json("card_zh.json", {})
    card_verified = load_json("card_verified.json", {})

    def card_label(name: str) -> str:
        zh = card_zh.get(name) or ""
        return f"{zh}（{name}）" if zh else name

    out: list[str] = []
    add = out.append

    add("# 你是哪种指挥官？— EDH 新人主将挑选测试")
    add("")
    add(f"> {len(quiz['questions'])} 道纯偏好题（无对错、无规则题）· 主将池 {len(cmds)} 位 · "
        "配套可交互网页 `commander_quiz.html`")
    add("")
    add("## 这是什么")
    add("")
    add("给刚接触万智牌、还不知道该玩哪个指挥官的新人用的挑选测试。")
    add("全程只问口味，不问规则——完全没玩过也能做完，做完得到 1 位主推主将 + 2 位备选，")
    add("每位都附基本介绍与建牌思路。")
    add("")
    add("**主将池怎么来的**：EDHREC 全时段最流行的 100 位主将，另加 10 位补齐玩法原型"
        "（闪现回场、灵气单挑、结界流、控制加税等 Top 100 覆盖薄弱的方向）。")
    add("")
    add("**玩法画像怎么来的**：用 EDHREC 社区对每位主将打的真实标签票数换算——"
        "例如「暴民头目克仑可」的标签是 Goblins 4847 票、Tokens 2613 票、Aggro 1834 票，"
        "除以它的总套牌数得到各玩法的渗透率，再映射到 20 个玩法轴上。")
    add("")
    add("**搭配牌怎么来的**：直接从 EDHREC 每位主将的牌组页抓取真实统计——"
        "「协同度高」= 专门为这位主将而来的人最多，「出场率高」= 大多数牌组都会放。"
        "不是凭印象推荐的。")
    add("")
    add("**没有用到的**：本测试不评估牌组强度。高分不等于强，只代表更合你口味。")
    add("")
    add("---")
    add("")
    add("## 怎么用")
    add("")
    add("| 方式 | 适合 | 做法 |")
    add("|---|---|---|")
    add("| 网页版（推荐） | 大多数新人 | 双击 `commander_quiz.html`，点选项，自动出结果 |")
    add("| 快速版 | 想先试试 | 网页首页选「快速版（39 题）」，5 分钟出结果 |")
    add("| 文档版 | 想打印 / 自己改 | 就是本文件，按第二节算分表手动算分，再翻第三节挑主将 |")
    add("")
    add("答题建议：**凭第一直觉选**，不要选「我应该会喜欢」的答案，选「我看到就想这么做」的答案。")
    add("")
    add("---")
    add("")

    # ---------- 题目 ----------
    add("## 一、题目")
    add("")
    add(f"共 {len(quiz['questions'])} 题，分 {len(quiz['sections'])} 个部分。")
    add("")
    sections: dict[str, list] = {}
    for question in quiz["questions"]:
        sections.setdefault(question["sec"], []).append(question)
    for section in quiz["sections"]:
        items = sections.get(section["id"], [])
        if not items:
            continue
        add(f"### {section['name']}（{len(items)} 题）")
        add("")
        add(f"*{section['intro']}*")
        add("")
        for question in items:
            multi = f"（可多选，最多 {question['multi']} 个）" if question.get("multi") else ""
            hub = "【枢纽题】" if question.get("kind") == "hub" else ""
            add(f"**{question['id']}. {hub}{question['q']}**{multi}")
            add("")
            for index, opt in enumerate(question["opts"]):
                goto = opt.get("goto")
                arrow = f"　→ 接着做 **{goto}**" if goto else ""
                add(f"- {LETTERS[index]}. {opt['t']}{arrow}")
            nxt = question.get("next")
            if not question.get("kind") == "hub":
                add("")
                add(f"*（答完接着做 {nxt}）*" if nxt else "*（答完即结束）*")
            add("")

    add("---")
    add("")

    # ---------- 算分表 ----------
    add("## 二、算分表")
    add("")
    add("每个选项对应若干玩法轴的加分。把所选选项的加分**累加**，得到你的玩法偏好向量；")
    add("得分最高的几个轴就是你的口味。")
    add("")
    add("### 2.1 逐题得分表")
    add("")
    add("| 题 | A | B | C | D | E |")
    add("|---|---|---|---|---|---|")
    for question in quiz["questions"]:
        cells = [fmt_scores(o) for o in question["opts"]]
        while len(cells) < 5:
            cells.append("")
        add(f"| {question['id']} | " + " | ".join(cells[:5]) + " |")
    add("")
    add("### 2.2 三个约束档位")
    add("")
    add("带 `复杂度容忍=` / `预算档=` / `咸度容忍=` 的选项不参与口味匹配，")
    add("而是取**所选选项的平均值**，用来把明显超出你承受范围的主将往下压。")
    add("")
    add("| 档位 | 含义 | 取值 |")
    add("|---|---|---|")
    add("| 复杂度容忍 | 你能接受多难记的主将 | 1 = 一眼就懂，5 = 越难越好 |")
    add("| 预算档 | 你打算投多少钱 | 1 = 极省，5 = 不在意预算 |")
    add("| 咸度容忍 | 你能接受多少「对手想打你」 | 1 = 完全受不了，5 = 就爱被讨厌 |")
    add("")
    add("### 2.3 20 个玩法轴")
    add("")
    add("| 轴 | 中文 | 含义 |")
    add("|---|---|---|")
    for axis, zh in AXIS_ZH.items():
        add(f"| `{axis}` | {zh} | {AXIS_DESC.get(axis, '')} |")
    add("")
    add("---")
    add("")

    # ---------- 主将池 ----------
    add(f"## 三、主将池（{len(cmds)} 位）")
    add("")
    add("### 3.1 速查表")
    add("")
    add("按流行度排序（`#` 为 EDHREC 全时段排名，越小越流行）。")
    add("")
    add("| # | 中文名 | 色 | MV | 难度 | 造价 | 咸度 | Bracket | 一句话 |")
    add("|---:|---|:--:|---:|:--:|:--:|:--:|:--:|---|")
    for card in sorted(cmds, key=lambda c: c["all_time_rank"] or 9999):
        tagline = (descriptions.get(card["en"]) or {}).get("tagline", "")
        add(f"| {card['all_time_rank']} | {card['zh']} | {card['colors']} | {card['cmc']:g} | "
            f"{card['complexity']} | {card['budget']} | {card['salt']:.2f} | {card['bracket']} | "
            f"{tagline} |")
    add("")
    add("### 3.2 逐位详解")
    add("")

    for card in sorted(cmds, key=lambda c: c["all_time_rank"] or 9999):
        name = card["en"]
        info = descriptions.get(name) or {}
        picks = card_display.get(name) or {"synergy": [], "popular": []}
        axes_top = sorted(card["vec"].items(), key=lambda kv: -kv[1])[:3]
        axes_text = "、".join(f"{AXIS_ZH.get(a, a)}" for a, _ in axes_top)
        verify = card_verified.get(name) or {}

        add(f"#### {card['all_time_rank']}. {card['zh']} / {name}")
        add("")
        if info.get("tagline"):
            add(f"**{info['tagline']}**")
            add("")
        add(f"- 颜色 {card['colors']} ｜ 法术力值 {card['cmc']:g} ｜ {card['type']}")
        add(f"- 流行度第 {card['all_time_rank']} 位（约 {card['num_decks']} 副套牌）｜ "
            f"上手难度 {card['complexity']}/5 ｜ 造价档位 {card['budget']}/5 ｜ "
            f"对手仇恨度 {card['salt']:.2f} ｜ 常见强度 Bracket {card['bracket']}")
        add(f"- 玩法倾向：{axes_text} ｜ 社区标签："
            f"{'、'.join(tag_zh.get(t, t) for t in card['top_tags'][:5])}")
        if card.get("text_level") is not None:
            add(f"- 难度拆解：牌面理解成本 {card['text_level']}/5（这张牌好不好读）"
                f"＋ 操作负担 {card['pilot_level']}/5（这套牌好不好开）"
                f"→ 综合 {card.get('difficulty')}")
        add("")
        if info.get("intro"):
            add(info["intro"])
            add("")
        if info.get("build"):
            add(f"**怎么组**：{info['build']}")
            add("")
        if picks["synergy"]:
            add("**高协同牌（EDHREC 实测，专门为它而来的人最多）**：" +
                "、".join(card_label(c) for c in picks["synergy"]))
            add("")
        if picks["popular"]:
            add("**通用件（大多数牌组都会放）**：" +
                "、".join(card_label(c) for c in picks["popular"]))
            add("")
        if verify.get("oracle_text"):
            add(f"> 主将牌面：{' '.join(verify['oracle_text'].split())[:220]}")
            add("")

    add("---")
    add("")
    add("## 四、数据来源与口径")
    add("")
    add("| 数据 | 来源 | 用途 |")
    add("|---|---|---|")
    add("| 主将流行度排名、套牌数 | EDHREC `json.edhrec.com/pages/commanders` | 决定主将池 |")
    add("| 玩法标签票数 | 同上，每张主将页的 `tag_counts` | 生成玩法向量 |")
    add("| 搭配牌协同度 / 出场率 | 同上，每张主将页的 `cardlists` | 建牌思路与推荐单卡 |")
    add("| 咸度 salt、Bracket 分布 | 同上 | 约束与展示 |")
    add("| 颜色身份、法术力值、牌面文字、价格 | Scryfall API | 复杂度/造价估算与核对 |")
    add("| 中文牌名 | mtgch.com autocomplete | 中英对照 |")
    add("")
    add("口径说明：")
    add("")
    add("- 抓取时间：2026-10-08。EDHREC 数据随玩家上传牌表实时变动，流行度排名会缓慢漂移。")
    add("- 玩法向量按轴做了归一化：每个轴的 95 分位映射到 3.0 满分，并设绝对下限，")
    add("  避免标签支持薄弱的轴（如「精准互动」只有 18 个标签指向）靠微小数值放大成满分。")
    add("- 匹配用的是**余弦相似度**（0.60 权重）+ 颜色契合（0.14）+ 流行度先验（0.08），")
    add("  再按复杂度 / 造价 / 咸度超限扣分。")
    add("- 极少数牌（7 张 Final Fantasy 系列牌，如 `Summon: Bahamut`）经 mtgch 与 Scryfall "
        "双重确认**没有官方中文印刷**，故文中保留英文名。")
    add("")
    add("---")
    add("")
    add("## 五、已知局限")
    add("")
    add("- **不是强度排名**。想要最强主将请直接看 cEDH 资料，本测试只匹配口味。")
    add("- **难度是估算值**，由两项合成：**牌面理解成本**（剔除括号内提示文本后的正文长度、")
    add("  触发式异能数、起动式异能数、可选数）与**操作负担**（该原型的规则交互与资源管理强度）。")
    add("  它是相对排名，不是绝对标准；扣分用的是连续值，五档只是四舍五入后的显示。")
    add("- **玩法标签有社区偏差**。EDHREC 标签由玩家打，热门套路标签更多；冷门但同样成立的玩法")
    add("  可能票数偏低，导致该主将的画像偏向主流玩法。")
    add("- **Top 100 之外的主将没进池**。如果你已经心仪某位非主流主将，本测试帮不上忙。")
    add("- 造价为**档位估算**，不是实际牌组价格；实际花费取决于你选哪些地牌与加速。")
    add("")

    path = ROOT / "commander_quiz.md"
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"✓ 写出 {path}（{path.stat().st_size / 1024:.0f} KB，{len(out)} 行）")
    print(f"  介绍文 {len(descriptions)} 篇 / 搭配牌 {len(card_display)} 组")


if __name__ == "__main__":
    main()
