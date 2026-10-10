#!/usr/bin/env python3
"""匹配引擎原型：答案 → 主将推荐。用于在移植到 HTML 前验证推荐质量。

用法:
    python engine.py --answers answers.json      # 显式答案文件
    python engine.py --profile aggro             # 内置合成画像，用于冒烟测试
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

DEFAULTS = {"complex": 3.0, "budget": 3.0, "salt": 3.0}

# 接触时长 → 整套评分标准的切换参数。做法与旧版测试里那道「你是完全的新手吗」一脉相承：
# 新人收紧难度容忍、抬高流行度权重（更容易找到资料）、压住高强度档位。
EXP_PROFILE = {
    1: {"name": "完全新人", "complex_cap": 2.4, "pop_mul": 1.35, "bracket_target": 2.0, "p_bracket": 0.025},
    2: {"name": "玩过万智牌，没打过指挥官", "complex_cap": 3.2, "pop_mul": 1.2, "bracket_target": 2.7, "p_bracket": 0.038},
    3: {"name": "打过一段时间指挥官", "complex_cap": 4.2, "pop_mul": 1.0, "bracket_target": 3.6, "p_bracket": 0.054},
    4: {"name": "老手", "complex_cap": 5.0, "pop_mul": 0.85, "bracket_target": 4.6, "p_bracket": 0.07},
}

# salt 容忍档位(1-5) → 可接受的 EDHREC 咸度上限
SALT_THRESHOLD = {1: 0.6, 2: 1.0, 3: 1.4, 4: 2.0, 5: 3.2}


def salt_cap_for(tolerance: float) -> float:
    """把连续的咸度容忍度插值成上限值。

    这里刻意用线性插值而不是「四舍五入取整档」：取整会让 Python 的
    round()（四舍六入五成双）和 JS 的 Math.round()（五入）在 x.5 处分叉，
    导致两个引擎算出不同结果；插值同时也消除了档位边界的跳变。
    """
    value = min(5.0, max(1.0, float(tolerance)))
    low = int(value)
    high = min(5, low + 1)
    frac = value - low
    return SALT_THRESHOLD[low] * (1.0 - frac) + SALT_THRESHOLD[high] * frac

# 综合评分权重
W_SIM = 0.60        # 玩法向量余弦相似度
W_COLOR = 0.14      # 颜色契合（内部再拆成「哪几个色」与「要几个色」两项）
# 颜色契合度内部拆分：
#   color_match   = 主将各色与玩家颜色偏好的平均吻合度
#   breadth_match = 玩家想要的色数 与 主将实际色数 的接近程度
# 只用 color_match 的话，「想要五色」的玩家永远拿不到五色主将——公式要除以颜色数，
# 五色主将天然吃亏。实测五色主将进前三的比例只有应得的一半，故拆出广度项。
#
# 为什么总权重仍是 0.14：参数扫描显示提高到 0.20 确实能让「想要五色的人拿到五色」
# 从 6.7% 升到 10.0%，但玩法命中率会从 42.7% 掉到 37.7%。这套测试的核心是玩法匹配，
# 用 5 个百分点的玩法准确率换 3 个百分点的颜色准确率不划算，所以改为在 0.14 的
# 预算内对半分，让广度信号吃到最大份额，同时不动玩法项。
W_COLOR_MATCH = 0.50
W_BREADTH_MATCH = 0.50
W_POPULAR = 0.08    # 流行度先验（新人更容易找到资料）
P_COST = 0.055      # 难度超出容忍度，每级扣分
P_BUDGET = 0.050    # 造价超出预算，每级扣分
P_BRACKET = 0.025    # 与目标档位的偏离（双向：太高太低都扣）
P_SALT = 0.10       # 咸度超出容忍度，每点扣分


def load_quiz():
    return json.loads((DATA / "questions.json").read_text(encoding="utf-8"))


def load_commanders():
    return json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))


def tally(quiz: dict, answers: dict[int, int]):
    """把答案汇总成偏好向量 + 约束档位 + 颜色倾向。

    返回的 constraints 里额外带一个 `exp`（接触万智牌的时长，1~4），
    它不参与平均，而是切换整套评分标准（见 EXP_PROFILE）。
    """
    pref: dict[str, float] = {}
    expected: dict[str, float] = {}
    colors: dict[str, float] = {}
    constraints: dict[str, list[float]] = {k: [] for k in DEFAULTS}
    breadth_values: list[float] = []
    exp_level = None

    for question in quiz["questions"]:
        qid = question["id"]
        if qid not in answers:
            continue
        chosen = answers[qid]
        indices = chosen if isinstance(chosen, list) else [chosen]

        # 「期望值」：这一题如果随便答，平均会拿到的向量。
        # 多选题按实际选了几项等比放大。
        opts = question["opts"]
        if opts:
            share = len(indices) / len(opts)
            for opt in opts:
                for axis, value in (opt.get("s") or {}).items():
                    expected[axis] = expected.get(axis, 0.0) + value * share

        for index in indices:
            if not isinstance(index, int) or index >= len(question["opts"]):
                raise ValueError(f"Q{qid} 选项下标越界：{index}")
            opt = question["opts"][index]
            for axis, value in (opt.get("s") or {}).items():
                pref[axis] = pref.get(axis, 0.0) + value
            for color, value in (opt.get("col") or {}).items():
                colors[color] = colors.get(color, 0.0) + value
            for key, value in (opt.get("cval") or {}).items():
                constraints[key].append(float(value))
            if opt.get("bw") is not None:
                breadth_values.append(float(opt["bw"]))
            if opt.get("exp"):
                exp_level = int(opt["exp"])

    # 只保留「这个人与平均答题者的差异」。
    # 140 多道题的选项向量累加起来，「人人都有的共同分量」会远大于个人口味，
    # 结果是所有人的偏好向量彼此相似度高达 0.6~0.9，推荐被少数「居中」的主将垄断。
    # 减去期望值后，比的就是这个人独特在哪。
    centered = {axis: pref.get(axis, 0.0) - expected.get(axis, 0.0)
                for axis in set(pref) | set(expected)}

    resolved = {}
    for key, values in constraints.items():
        resolved[key] = sum(values) / len(values) if values else DEFAULTS[key]
    resolved["exp"] = exp_level or 3
    # 玩家想要的色数（0 = 无色，1.0 = 五色）。没答到广度题时取 0.5（两色，最常见）。
    resolved["breadth"] = (sum(breadth_values) / len(breadth_values)
                           if breadth_values else 0.5)
    return centered, colors, resolved


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(a.get(k, 0.0) ** 2 for k in keys))
    nb = math.sqrt(sum(b.get(k, 0.0) ** 2 for k in keys))
    return dot / (na * nb) if na and nb else 0.0


def score_commanders(payload: dict, pref, colors, constraints):
    commanders = payload["commanders"]
    max_decks = max((c.get("num_decks") or 1) for c in commanders)
    max_color = max(colors.values()) if colors else 0.0
    # 接触时长决定整套评分标准：新人收紧难度容忍、抬高流行度权重、压住高强度档位
    exp_level = int(constraints.get("exp", 3))
    profile = EXP_PROFILE.get(exp_level, EXP_PROFILE[3])
    complex_tol = min(constraints["complex"], profile["complex_cap"])
    pop_weight = W_POPULAR * profile["pop_mul"]
    player_breadth = float(constraints.get("breadth", 0.5))
    results = []

    for card in commanders:
        sim = cosine(pref, card["vec"])

        # 无色主将的处理（两件事分开）：
        # ① 广度上拉到 0.2，与单色同档——「零种颜色」不该比「一种颜色」更极端，
        #   两者在构筑上都是「一条资源线，不用调色」。
        # ② 但候选池不混：无色的匹配走独立的 "C" 偏好（来自广度题的无色选项），
        #   没选过无色的人 C=0，无色主将拿不到色相分，也就不会被推给他们。
        card_colors = card["colors"]
        if card_colors == "C":
            card_breadth = 0.2
            color_match = (colors.get("C", 0.0) / max_color) if max_color else 0.0
        else:
            card_breadth = len(card_colors) / 5.0
            color_match = 0.5 if max_color == 0 else (
                sum(colors.get(c, 0.0) for c in card_colors)
                / (max_color * len(card_colors)))
        # 广度吻合度用平方衰减：差一档从 1.0 掉到 0.64，差两档只剩 0.36。
        # 线性衰减下「差一档」只损失 0.2（换算到总分 0.014），压不过玩法项。
        breadth_gap = abs(player_breadth - card_breadth)
        breadth_match = (1.0 - breadth_gap) ** 2
        affinity = W_COLOR_MATCH * color_match + W_BREADTH_MATCH * breadth_match

        popularity = math.log10(max(1, card.get("num_decks") or 1)) / math.log10(max_decks)

        # 难度扣分用连续值（difficulty），五档只用于显示，避免相邻档位差一跳就是一大截
        pen_cost = max(0.0, card.get("difficulty", card["complexity"]) - complex_tol) * P_COST
        pen_budget = max(0.0, card["budget"] - constraints["budget"]) * P_BUDGET
        salt_cap = salt_cap_for(constraints["salt"])
        pen_salt = max(0.0, card["salt"] - salt_cap) * P_SALT
        # 强度档位：新人被高 Bracket 主将劝退，老手不受限
        # 目标档位与权重都随经验上移：新人被拉向低强度，老手被拉向高强度。
        # 原来只对「超过上限」扣分，老手上限是 5 所以永远不扣分、
        # 高强度也没有加分——结果就是对强度完全无感。
        bracket_pen = abs(int(card.get("bracket", 3))
                          - profile["bracket_target"]) * profile["p_bracket"]
        # 玩家明确想搞事时，咸度反而是加分项
        salt_bonus = 0.05 * card["salt"] if constraints["salt"] >= 4.0 else 0.0

        total = (W_SIM * sim + W_COLOR * affinity + pop_weight * popularity
                 - pen_cost - pen_budget - pen_salt - bracket_pen + salt_bonus)

        results.append({
            "en": card["en"], "zh": card["zh"], "colors": card["colors"],
            "score": total, "sim": sim, "affinity": affinity, "popularity": popularity,
            "pen": {"cost": pen_cost, "budget": pen_budget, "salt": pen_salt,
                    "bracket": bracket_pen},
            "complexity": card["complexity"], "budget": card["budget"],
            "salt": card["salt"], "bracket": card["bracket"],
            "exp": exp_level, "exp_name": profile["name"],
            "tags": card["top_tags"][:4],
            "top_vec": sorted(card["vec"].items(), key=lambda kv: -kv[1])[:4],
        })

    results.sort(key=lambda r: -r["score"])
    return results


def report(pref, colors, constraints, results, limit=10):
    print(f"\n约束档位：复杂度容忍 {constraints['complex']:.1f} / "
          f"预算档 {constraints['budget']:.1f} / 咸度容忍 {constraints['salt']:.1f}")
    top_pref = sorted(pref.items(), key=lambda kv: -kv[1])[:8]
    print(f"最强烈的玩法偏好：{top_pref}")
    print(f"颜色倾向：{sorted(colors.items(), key=lambda kv: -kv[1])}")
    print(f"\n{'排名':<4}{'总分':>7}{'相似':>7}{'颜色':>7}{'流行':>7}  "
          f"{'复杂':>4}{'造价':>4}{'咸度':>6}  主将")
    for index, row in enumerate(results[:limit], 1):
        name = f"{row['en']}" + (f" / {row['zh']}" if row["zh"] else "")
        print(f"{index:<4}{row['score']:>7.3f}{row['sim']:>7.3f}{row['affinity']:>7.2f}"
              f"{row['popularity']:>7.2f}  {row['complexity']:>4}{row['budget']:>4}"
              f"{row['salt']:>6.2f}  [{row['colors']}] {name}")
        print(f"       触发轴：{row['top_vec']}  标签：{row['tags']}")


SYNTHETIC = {
    # 每个画像：轴 → 想要的强度
    "aggro": {"aggro": 3, "wide": 2, "tribal": 2, "stompy": 1},
    "control": {"control": 3, "spells": 2, "removal": 1.5},
    "enchant": {"enchant": 3, "voltron": 2, "counters": 1.5},
    "grave": {"grave": 3, "drain": 2, "tribal": 1},
    "combo": {"combo": 3, "spells": 1.5},
    "blink": {"blink": 3, "control": 1.5},
    "voltron": {"voltron": 3, "artifacts": 2},
    "stax": {"stax": 3, "control": 1.5},
    "politics": {"politics": 3, "chaos": 1.5, "drain": 1},
    "ramp": {"ramp": 3, "stompy": 2},
    "chaos": {"chaos": 3, "clonesteal": 1.5},
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--answers")
    parser.add_argument("--profile")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    quiz = load_quiz()
    payload = load_commanders()

    if args.answers:
        raw = json.loads(pathlib.Path(args.answers).read_text(encoding="utf-8"))
        answers = dict(raw)   # 题号是字符串（s01 / h1a2 / c03），不要转 int
        pref, colors, constraints = tally(quiz, answers)
    elif args.profile:
        if args.profile not in SYNTHETIC:
            print(f"未知画像，可选：{list(SYNTHETIC)}")
            return 1
        pref = dict(SYNTHETIC[args.profile])
        colors, constraints = {}, dict(DEFAULTS)
    else:
        # 冒烟测试：跑全部合成画像
        for name, pref in SYNTHETIC.items():
            print(f"\n{'=' * 84}\n【画像】{name}")
            results = score_commanders(payload, dict(pref), {}, dict(DEFAULTS))
            report(pref, {}, dict(DEFAULTS), results, limit=5)
        return 0

    results = score_commanders(payload, pref, colors, constraints)
    report(pref, colors, constraints, results, limit=args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
