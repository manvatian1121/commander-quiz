#!/usr/bin/env python3
"""构建最终主将数据集：玩法向量（来自 EDHREC 真实标签）+ 复杂度 + 造价 + 中文名。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

AXES = ["aggro", "voltron", "wide", "ramp", "stompy", "control", "removal", "combo",
        "spells", "artifacts", "enchant", "grave", "tribal", "drain", "stax",
        "clonesteal", "politics", "chaos", "counters", "blink"]
COLOR_ORDER = "WUBRG"

# 原型补位（EDHREC 全时段 Top 100 之外，但经过流行度验证；补齐 Blink/Voltron/结界/控制等原型缺口）
SUPPLEMENTS = [
    "Brago, King Eternal",          # 15275 副 — 闪现/进场触发
    "Yarok, the Desecrated",        # 13289 副 — 闪现/双倍触发
    "Anikthea, Hand of Erebos",     # 13362 副 — 结界/坟场
    "Light-Paws, Emperor's Voice",  # 12435 副 — 灵气单挑
    "Grand Arbiter Augustin IV",    # 14128 副 — 控制/加税
    "Tergrid, God of Fright",       # 12822 副 — 弃牌/牺牲剥夺
    "Talrand, Sky Summoner",        #  7028 副 — 法术连发（新人友好）
    "Xenagos, God of Revels",       #  8685 副 — 大生物/额外战斗（新人友好）
    "Niv-Mizzet, Parun",            # 15658 副 — 法术连发/组合技
    "Wyleth, Soul of Steel",        #  2696 副 — 装备单挑（预组主将）
]

# 「整套牌好不好开」的每轴负担权重（0=几乎不用动脑，1=规则交互/资源管理很重）
# 依据：该原型是否要求追踪隐藏信息、算数、记住大量静止式效应、或理解规则细节。
PILOT_WEIGHTS = {
    "blink": 0.95,       # 放逐再回场是全新物件，触发顺序与堆叠容易出错
    "combo": 0.90,       # 要找线、算费用、注意打断点
    "clonesteal": 0.85,  # 要追踪复制品与被偷的牌
    "stax": 0.85,        # 要记住一堆静止式限制，还要评估威胁与桌面政治
    "spells": 0.65,      # 连续施放要排序，风暴还要数数
    "counters": 0.60,    # 增殖要算每种指示物的数量
    "grave": 0.60,       # 坟场是第二手牌，要追踪资源
    "control": 0.60,     # 威胁评估、留费、把握反击时机
    "politics": 0.50,
    "artifacts": 0.45,
    "removal": 0.40,
    "enchant": 0.40,
    "drain": 0.35,
    "ramp": 0.35,
    "chaos": 0.35,
    "tribal": 0.30,
    "voltron": 0.30,
    "wide": 0.30,
    "stompy": 0.25,
    "aggro": 0.25,
}

TEXT_WEIGHT = 0.58   # 牌面理解成本占最终难度评分的权重
PILOT_WEIGHT = 0.42  # 操作负担占最终难度评分的权重


def pilot_burden(vec: dict[str, float]) -> tuple[float, float]:
    """由玩法向量算「操作负担」。返回（1~5 档位, 0~1 原始值）。"""
    if not vec:
        return 3.0, 0.5
    total = sum(vec.values())
    weighted = sum(value * PILOT_WEIGHTS.get(axis, 0.5) for axis, value in vec.items())
    raw = weighted / total if total else 0.5
    return 1.0 + 4.0 * raw, raw


def percentile_map(values: list[float], levels: int = 5) -> list[int]:
    """把一组数值按百分位映射成 1..levels 的整数。"""
    ordered = sorted(values)
    total = len(ordered)
    result = []
    for value in values:
        rank = sum(1 for item in ordered if item <= value)
        bucket = min(levels, max(1, -(-rank * levels // total)))
        result.append(bucket)
    return result


def percentile_scores(values: list[float]) -> list[float]:
    """连续百分位（0~1），用于让扣分平滑变化，避免相近主将被分档边界劈开。"""
    ordered = sorted(values)
    total = len(ordered)
    result = []
    for value in values:
        below = sum(1 for item in ordered if item < value)
        upto = sum(1 for item in ordered if item <= value)
        result.append((below + upto) / 2.0 / total)
    return result


def main() -> int:
    profiles = json.loads((DATA / "commander_profiles.json").read_text(encoding="utf-8"))
    scry = json.loads((DATA / "commanders_scryfall.json").read_text(encoding="utf-8"))
    cb = json.loads((DATA / "complexity_budget.json").read_text(encoding="utf-8"))
    zh_path = DATA / "commander_zh.json"
    zh = json.loads(zh_path.read_text(encoding="utf-8")) if zh_path.exists() else {}
    map_path = DATA / "tag_axis_map.json"
    if not map_path.exists():
        print("✗ 缺少 tag_axis_map.json，子代理尚未产出")
        return 1
    tag_map = json.loads(map_path.read_text(encoding="utf-8"))["mapped"]

    lookup = {}
    for name, card in scry.items():
        lookup[name] = card
        lookup.setdefault(name.split(" // ")[0], card)
        lookup.setdefault(name.split(",")[0].strip(), card)

    # 花名册：优先用显式名单（pool_roster.json），否则退回「全时段 Top 100 + 补位」
    roster_path = DATA / "pool_roster.json"
    if roster_path.exists():
        roster = json.loads(roster_path.read_text(encoding="utf-8"))
        roster = [n for n in roster if n in profiles]
        missing_roster = [n for n in json.loads(roster_path.read_text(encoding="utf-8"))
                          if n not in profiles]
        if missing_roster:
            print(f"  ⚠ 花名册里有 {len(missing_roster)} 位缺档案，已跳过："
                  f"{missing_roster[:6]}")
    else:
        top100 = sorted(profiles.items(),
                        key=lambda kv: kv[1].get("all_time_rank") or 99999)[:100]
        roster = [name for name, _ in top100]
        for name in SUPPLEMENTS:
            if name not in roster:
                roster.append(name)

    missing_profile = [n for n in roster if n not in profiles]
    if missing_profile:
        print(f"✗ 以下主将缺少 EDHREC 档案：{missing_profile}")
        return 1

    # --- 玩法向量：标签票数 / 总套牌数 = 该玩法的渗透率，再乘轴权重 ---
    raw_vectors: dict[str, dict[str, float]] = {}
    for name in roster:
        prof = profiles[name]
        decks = prof.get("num_decks") or 1
        vector: dict[str, float] = {}
        for tag in prof.get("tag_counts") or []:
            weights = tag_map.get(tag["value"])
            if not weights:
                continue
            share = (tag.get("count") or 0) / decks
            for axis, weight in weights.items():
                vector[axis] = vector.get(axis, 0.0) + share * weight
        raw_vectors[name] = vector

    # 按轴标定：各轴 95 分位映射到 3.0，避免不同轴量纲差异。
    # 同时设绝对下限 FLOOR：标签支持薄弱的轴（如 removal 只有 18 个标签指向）
    # 不能靠极小的原始值被放大成满分，否则会产出「噪声信号」。
    FLOOR = 0.012   # ≈ 1% 的社区标签渗透率 × 权重 1.0
    axis_scale: dict[str, float] = {}
    for axis in AXES:
        values = sorted(v[axis] for v in raw_vectors.values() if v.get(axis, 0) > 0)
        if not values:
            axis_scale[axis] = FLOOR
            continue
        index = min(len(values) - 1, int(len(values) * 0.95))
        axis_scale[axis] = max(values[index] / 3.0, FLOOR)

    commanders = []
    for name in roster:
        prof = profiles[name]
        card = lookup.get(name) or lookup.get(name.split(" // ")[0]) or {}
        vector = {}
        for axis, value in raw_vectors[name].items():
            score = min(3.0, value / axis_scale[axis])
            if score >= 0.25:
                vector[axis] = round(score, 2)
        identity = card.get("color_identity") or list(prof.get("color_identity") or [])
        if isinstance(identity, str):
            identity = list(identity)
        brackets = prof.get("bracket_counts") or {}
        total_b = sum(brackets.values()) or 1
        commanders.append({
            "id": prof.get("slug") or name.lower().replace(" ", "-"),
            "en": name,
            "zh": zh.get(name, ""),
            "colors": "".join(c for c in COLOR_ORDER if c in identity) or "C",
            "cmc": card.get("cmc"),
            "type": card.get("type_line"),
            "vec": vector,
            "bracket": max(brackets.items(), key=lambda kv: kv[1])[0] if brackets else "3",
            "bracket_mix": {k: round(v / total_b, 2) for k, v in sorted(brackets.items())},
            "salt": round(prof.get("salt") or 0, 2),
            "all_time_rank": prof.get("all_time_rank"),
            "num_decks": prof.get("num_decks"),
            "usd": card.get("usd"),
            "top_tags": [t["value"] for t in sorted(
                prof.get("tag_counts") or [], key=lambda t: -(t.get("count") or 0))[:6]],
        })

    # 难度评分 = 牌面理解成本 + 操作负担，再按百分位映射到 1..5
    difficulty_raw: list[float] = []
    for commander in commanders:
        info = cb.get(commander["en"]) or {}
        text_level = info.get("text_level", 2.5)
        pilot_level, pilot_raw = pilot_burden(commander["vec"])
        combined = TEXT_WEIGHT * text_level + PILOT_WEIGHT * pilot_level
        commander["text_level"] = round(text_level, 2)
        commander["pilot_level"] = round(pilot_level, 2)
        commander["pilot_raw"] = round(pilot_raw, 3)
        difficulty_raw.append(combined)

    for commander, pct in zip(commanders, percentile_scores(difficulty_raw)):
        commander["difficulty"] = round(1.0 + 4.0 * pct, 2)   # 连续值：用于扣分
        commander["complexity"] = max(1, min(5, round(1.0 + 4.0 * pct)))  # 整数：用于显示

    budgets = [(cb.get(c["en"]) or {}).get("budget_raw", 3.0) for c in commanders]
    for commander, level in zip(commanders, percentile_map(budgets)):
        commander["budget"] = level

    payload = {
        "meta": {
            "source": "EDHREC (json.edhrec.com) + Scryfall API",
            "roster_rule": "EDHREC 全时段 Top 100 + 10 位原型补位",
            "axis_scale": {k: round(v, 5) for k, v in axis_scale.items()},
            "count": len(commanders),
        },
        "axes": AXES,
        "commanders": commanders,
    }
    (DATA / "commanders.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"✓ 写出 {len(commanders)} 位主将")
    no_zh = [c["en"] for c in commanders if not c["zh"]]
    no_vec = [c["en"] for c in commanders if not c["vec"]]
    print(f"  无中文名：{len(no_zh)}")
    print(f"  空向量：{len(no_vec)}")
    if no_vec:
        for name in no_vec:
            print(f"    ✗ {name}")
    print("\n抽样检查：")
    for name in ["Krenko, Mob Boss", "Light-Paws, Emperor's Voice", "Brago, King Eternal",
                 "Y'shtola, Night's Blessed", "Grand Arbiter Augustin IV"]:
        card = next((c for c in commanders if c["en"] == name), None)
        if card:
            top = sorted(card["vec"].items(), key=lambda kv: -kv[1])[:5]
            print(f"  {name} [{card['colors']}] 复杂度{card['complexity']} 造价{card['budget']} "
                  f"咸度{card['salt']}")
            print(f"     {top}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
