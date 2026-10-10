#!/usr/bin/env python3
"""扩池后的三处收尾修正：
① 补充新主将带来的 33 个 EDHREC 标签的中文名
② 校验器的「无敌」误报：它出现在牌名/角色名里，不是吹强度
③ 全轴验证的预期集：池子变大后，各原型榜首被新主将刷新，把合法的新主人加进去
"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

# ① 标签中文名
NEW_TAGS = {
    "Artificers": "神器师", "Assassins": "刺客", "Beasts": "野兽",
    "Coin Flip": "掷硬币", "Constructs": "组构体", "Dragon's Approach": "龙之途径",
    "Experience Counters": "经验指示物", "Hare Apparent": "兔群", "Haste": "敏捷",
    "Heroes": "英雄", "Impulse Draw": "冲动抽牌", "Kithkin": "洁英",
    "Lessons": "课程", "Lhurgoyfs": "噬物怪", "Lizards": "蜥蜴", "Mice": "小鼠",
    "Monks": "僧侣", "Myriad": "万千", "Obosh Companion": "欧波什行侣",
    "Otters": "水獭", "Prowess": "灵技", "Rat Colony": "鼠群", "Reach": "延势",
    "Robots": "机器人", "Rooms": "房间", "Saprolings": "腐生物",
    "Sea Creatures": "海洋生物", "Spacecraft": "太空船", "Speed": "速度",
    "Tyranids": "泰伦", "Villainous Choice": "邪恶抉择", "Warp": "跃迁",
    # Freerunning 是刺客信条系列的机制，中文译名未能确证，保留英文以免猜错
}


def fix_tags() -> None:
    path = DATA / "tag_zh.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    before = len(data)
    for key, value in NEW_TAGS.items():
        data.setdefault(key, value)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"① 标签中文名：{before} → {len(data)} 条")


def fix_validator() -> None:
    path = pathlib.Path(SCRIPT_DIR / "validate_descriptions.py")
    text = path.read_text(encoding="utf-8")
    old = '''# 明确禁止的吹强度 / 术语词汇
BANNED = ["最强", "上分神器", "无敌", "碾压一切", "必赢",
          "bracket", "edhrec", "voltron", "stax", "ramp", "引擎", "曲线"]'''
    new = '''# 明确禁止的吹强度 / 术语词汇
BANNED = ["最强", "上分神器", "无敌", "碾压一切", "必赢",
          "bracket", "edhrec", "voltron", "stax", "ramp", "引擎", "曲线"]

# 例外：这些词出现在牌名 / 角色名里是正当用法，不算吹强度。
# 例：「无敌松鼠妹（The Unbeatable Squirrel Girl）」是官方牌名；
#     「他就成了无敌浩克」指布鲁斯·班纳变身后的角色，不是在夸强度。
BANNED_ALLOW = ["无敌松鼠妹", "无敌浩克", "无敌钢铁侠", "无敌（"]'''
    if old in text:
        path.write_text(text.replace(old, new), encoding="utf-8")
        print("② 校验器：已加入「无敌」的牌名/角色名例外")
    else:
        print("② 校验器：未找到 BANNED 定义，跳过")


def fix_expectations() -> None:
    path = pathlib.Path(SCRIPT_DIR / "axis_validation.py")
    text = path.read_text(encoding="utf-8")
    pairs = [
        ('"wide": {"Krenko, Mob Boss", "Zurgo Stormrender", "Zinnia, Valley\'s Voice"},',
         '"wide": {"Krenko, Mob Boss", "Zurgo Stormrender", "Zinnia, Valley\'s Voice",\n'
         '             "Shroofus Sproutsire", "The Unbeatable Squirrel Girl",\n'
         '             "Baylen, the Haymaker", "Finneas, Ace Archer"},'),
        ('"ramp": {"Zhulodok, Void Gorger", "Zaxara, the Exemplary", "Kinnan, Bonder Prodigy"},',
         '"ramp": {"Zhulodok, Void Gorger", "Zaxara, the Exemplary", "Kinnan, Bonder Prodigy",\n'
         '             "Tifa Lockhart", "Toph, the First Metalbender",\n'
         '             "Szarel, Genesis Shepherd", "Tannuk, Memorial Ensign"},'),
        ('"stompy": {"Gishath, Sun\'s Avatar", "Zhulodok, Void Gorger", "Pantlaza, Sun-Favored"},',
         '"stompy": {"Gishath, Sun\'s Avatar", "Zhulodok, Void Gorger", "Pantlaza, Sun-Favored",\n'
         '               "Ghalta, Primal Hunger", "Eshki, Temur\'s Roar",\n'
         '               "Doran, Besieged by Time", "Tifa, Martial Artist"},'),
        ('"spells": {"Vivi Ornitier", "Talrand, Sky Summoner", "Niv-Mizzet, Parun"},',
         '"spells": {"Vivi Ornitier", "Talrand, Sky Summoner", "Niv-Mizzet, Parun",\n'
         '               "Judith, Carnage Connoisseur", "Kuja, Genome Sorcerer",\n'
         '               "Elsha, Threefold Master", "Bria, Riptide Rogue", "Iroh, Grand Lotus"},'),
    ]
    hits = 0
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new)
            hits += 1
    path.write_text(text, encoding="utf-8")
    print(f"③ 全轴验证预期集：更新 {hits}/4 项")


if __name__ == "__main__":
    fix_tags()
    fix_validator()
    fix_expectations()
