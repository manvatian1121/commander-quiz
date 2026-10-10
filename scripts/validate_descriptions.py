#!/usr/bin/env python3
"""校验介绍文：字段完整、字数达标、牌名必须属于该主将自己的搭配清单。"""
from __future__ import annotations

import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

# 英文专有名词片段
EN_PHRASE = re.compile(r"[A-Z][A-Za-z'\u2019\-]*(?:\s+(?:of|the|and|as|to|in|a)\s+)?"
                       r"(?:\s+[A-Z][A-Za-z'\u2019\-]*)*")
PAREN = re.compile(r"[（(]([^）)]*[A-Za-z][^）)]*)[）)]")
STOP_WORDS = {"of", "the", "and", "as", "to", "in", "a", "an", "or", "for"}

LEN_RULES = {"tagline": (1, 20), "intro": (70, 120), "build": (110, 170)}
TOLERANCE = {"tagline": 0.0, "intro": 0.20, "build": 0.20}

# 允许出现在正文里的非牌名英文（通用缩写等）
ALLOW_EXTRA_WORDS = {"edh", "mtg", "mv", "w", "u", "b", "r", "g", "c"}

# 明确禁止的吹强度 / 术语词汇
BANNED = ["最强", "上分神器", "无敌", "碾压一切", "必赢",
          "bracket", "edhrec", "voltron", "stax", "ramp", "引擎", "曲线"]

# 例外：这些词出现在牌名 / 角色名里是正当用法，不算吹强度。
# 例：「无敌松鼠妹（The Unbeatable Squirrel Girl）」是官方牌名；
#     「他就成了无敌浩克」指布鲁斯·班纳变身后的角色，不是在夸强度。
BANNED_ALLOW = ["无敌松鼠妹", "无敌浩克", "无敌钢铁侠", "无敌（",
                "龙形引擎瑞莫斯", "洞察引擎"]

# 这些英文不是牌名，是费用符号或通用写法，白名单校验时应先剥掉
NON_NAME_TOKENS = {"x", "a", "b"}   # name_words() 会转小写，这里也用小写


def visible_len(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def name_words(name: str) -> set[str]:
    return {w.lower() for w in re.findall(r"[A-Za-z'\u2019\-]+", name)}


def add_faces(target: set[str], name: str, verified: dict) -> None:
    """把牌名及其各面名（双面牌 / 分体牌的 A // B）都加进允许集合。"""
    target.add(name)
    full = (verified.get(name) or {}).get("name") or name
    for face in full.split(" // "):
        target.add(face.strip())
    for face in name.split(" // "):
        target.add(face.strip())


def main() -> int:
    payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    roster = [c["en"] for c in payload["commanders"]]
    display = json.loads((DATA / "card_display.json").read_text(encoding="utf-8"))
    verified = json.loads((DATA / "card_verified.json").read_text(encoding="utf-8"))
    # 主将自身的官方全名（含双面牌背面），用于放行「世界树神埃西卡 // 虹彩桥」这类写法
    scry = json.loads((DATA / "commanders_scryfall.json").read_text(encoding="utf-8"))
    commander_full: dict[str, str] = {}
    for key, card in scry.items():
        commander_full[key] = card.get("name") or key
        commander_full.setdefault(key.split(" // ")[0], card.get("name") or key)

    merged: dict[str, dict] = {}
    for index in range(1, 21):
        path = DATA / f"descriptions_{index}.json"
        if path.exists():
            merged.update(json.loads(path.read_text(encoding="utf-8")))

    problems: list[str] = []
    warnings: list[str] = []

    missing = [n for n in roster if n not in merged]
    extra = [n for n in merged if n not in roster]
    if missing:
        problems.append(f"缺介绍文 {len(missing)} 位：{missing}")
    if extra:
        problems.append(f"多出非花名册条目 {len(extra)}：{extra}")

    # 全局白名单（含所有主将名），用于兜底
    global_names = set()
    for entry in display.values():
        global_names.update(entry["synergy"])
        global_names.update(entry["popular"])
    global_names.update(roster)
    global_words = {w for name in global_names for w in name_words(name)} | ALLOW_EXTRA_WORDS

    bad_lens: list[str] = []
    foreign_cards: list[tuple[str, str]] = []
    unknown_english: list[tuple[str, str]] = []
    banned_hits: list[tuple[str, str, str]] = []
    char_stats: dict[str, list[int]] = {k: [] for k in LEN_RULES}

    for commander, entry in merged.items():
        own = display.get(commander) or {"synergy": [], "popular": []}
        own_names: set[str] = set()
        for card in own["synergy"] + own["popular"]:
            add_faces(own_names, card, verified)
        full = commander_full.get(commander, commander)
        for face in full.split(" // "):
            own_names.add(face.strip())
        own_names.add(commander)
        own_words = {w for name in own_names for w in name_words(name)}
        own_words |= ALLOW_EXTRA_WORDS

        for field, (low, high) in LEN_RULES.items():
            text = (entry.get(field) or "").strip()
            if not text:
                problems.append(f"{commander} 的 {field} 为空")
                continue
            length = visible_len(text)
            char_stats[field].append(length)
            allowed_high = high * (1 + TOLERANCE[field])
            if length < low or length > allowed_high:
                bad_lens.append(f"{commander}.{field}＝{length} 字（要求 {low}~{high}）")

        blob = " ".join(str(entry.get(f) or "") for f in ("tagline", "intro", "build"))

        # 校验 1：括号里的英文必须是本主将自己的搭配牌
        for group in PAREN.findall(blob):
            text = group.strip()
            if text in own_names or text == commander:
                continue
            words = {w for w in name_words(text)} - NON_NAME_TOKENS
            outside = words - own_words
            if not outside:
                continue
            if text in global_names:
                foreign_cards.append((commander, text))
            else:
                unknown_english.append((commander, text))

        # 校验 2：正文里裸露的英文片段必须属于本主将清单
        for phrase in EN_PHRASE.findall(blob):
            phrase = phrase.strip()
            if not phrase or phrase == commander or phrase in own_names:
                continue
            words = {w for w in name_words(phrase)} - STOP_WORDS - NON_NAME_TOKENS
            outside = words - own_words
            if not outside:
                continue
            if phrase in global_names:
                foreign_cards.append((commander, phrase))
            elif len(phrase.split()) >= 1 and any(w in global_words for w in words):
                continue
            else:
                unknown_english.append((commander, phrase))

        # 校验 3：禁忌词（先把牌名/角色名里的正当用法剥掉，避免误报）
        scanned = blob
        for allowed in BANNED_ALLOW:
            scanned = scanned.replace(allowed, "")
        low_blob = scanned.lower()
        for word in BANNED:
            # 纯英文词必须按词边界匹配：否则 Sky Rampart / Rampaging Baloths /
            # Rampant Growth 里的 "ramp" 会被误报成行话。
            if word.isascii():
                if re.search(r"\b" + re.escape(word.lower()) + r"\b", low_blob):
                    banned_hits.append((commander, word, ""))
            elif word.lower() in low_blob:
                banned_hits.append((commander, word, ""))

    if bad_lens:
        warnings.append(f"字数超出建议区间 {len(bad_lens)} 处：")
        warnings.extend(f"    {item}" for item in bad_lens[:15])
    if foreign_cards:
        problems.append(f"引用了别的主将的搭配牌 {len(foreign_cards)} 处：")
        for commander, name in foreign_cards[:15]:
            problems.append(f"    {commander} → 「{name}」")
    if unknown_english:
        problems.append(f"白名单外的英文片段 {len(unknown_english)} 处：")
        for commander, name in unknown_english[:15]:
            problems.append(f"    {commander} → 「{name}」")
    if banned_hits:
        problems.append(f"禁忌词 {len(banned_hits)} 处：")
        for commander, word, _ in banned_hits[:15]:
            problems.append(f"    {commander} → 「{word}」")

    print(f"介绍文 {len(merged)} 篇 / 花名册 {len(roster)} 位")
    for field, values in char_stats.items():
        if values:
            ordered = sorted(values)
            print(f"  {field:<8} 字数 {ordered[0]}~{ordered[-1]}，中位 {ordered[len(ordered) // 2]}")

    print("\n" + "=" * 66)
    for item in warnings:
        print(f"⚠ {item}")
    if problems:
        print(f"✗ 发现 {len(problems)} 类问题：")
        for item in problems:
            print(f"  - {item}")
        return 1
    print("✓ 介绍文校验通过（牌名全部属于本主将自己的搭配清单）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
