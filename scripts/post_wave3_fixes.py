#!/usr/bin/env python3
"""489 位主将的收尾修正：
① 介绍文里残留的英文行话 ramp → 法术力加速
② 新主将带来的 45 个 EDHREC 标签的中文名
③ 全轴验证的预期集（池子变大后各原型榜首被新主将刷新）
"""
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
SCRIPTS = pathlib.Path(SCRIPT_DIR)

NEW_TAGS = {
    "Adventures": "冒险", "Advisors": "参谋", "Apes": "猿猴", "Blood": "血滴",
    "Clash": "争斗", "Clues": "线索", "Crime": "罪行", "Daleks": "戴立克",
    "Day / Night": "昼夜", "Deserts": "沙漠", "Devils": "恶魔", "Elephants": "象",
    "Enrage": "激怒", "Fling": "投掷", "Foretell": "预视", "Fungi": "真菌",
    "Gnomes": "侏儒", "Golems": "魔像", "Guildgates": "公会门", "Illusions": "虚影",
    "Kaheera Companion": "卡希拉行侣", "Keywords": "关键字",
    "Land Animation": "地牌活化", "Life Exchange": "生命交换", "Madness": "疯狂",
    "Mana Dorks": "产费生物", "Monkeys": "猴", "Necrons": "死灵",
    "Nightmares": "梦魇", "Oozes": "软泥", "Orcs": "半兽人", "Outlaws": "不法之徒",
    "Persistent Petitioners": "执着的请愿人", "Plot": "谋划",
    "Primal Surge": "原初涌动", "Relentless Rats": "无情鼠", "Scarecrows": "稻草人",
    "Shadowborn Apostles": "影裔使徒", "Slime Against Humanity": "对抗人类的黏液",
    "Sunforger": "铸阳锤", "The Ring": "魔戒", "Unicorns": "独角兽",
    "Web-slinging": "蛛丝摆荡", "Werewolves": "狼人",
    # Freerunning 是刺客信条机制，中文译名未能确证，保留英文
}

# 池子变大后各原型榜首被刷新，把合法的新主人加进预期集
EXPECT = [
    ('"drain": {"Oloro, Ageless Ascetic", "Teysa Karlov", "Valgavoth, Harrower of Souls"}',
     '"drain": {"Oloro, Ageless Ascetic", "Teysa Karlov", "Valgavoth, Harrower of Souls",\n'
     '              "Bilbo, Birthday Celebrant", "Astarion, the Decadent",\n'
     '              "Amalia Benavides Aguirre", "Dina, Soul Steeper"}'),
    ('"clonesteal": {"Maralen, Fae Ascendant", "Miirym, Sentinel Wyrm", "Yuriko, the Tiger\'s Shadow"}',
     '"clonesteal": {"Maralen, Fae Ascendant", "Miirym, Sentinel Wyrm", "Yuriko, the Tiger\'s Shadow",\n'
     '                   "Satoru Umezawa", "Obeka, Brute Chronologist",\n'
     '                   "Gonti, Canny Acquisitor", "Don Andres, the Renegade"}'),
    ('"politics": {"Kenrith, the Returned King", "Ms. Bumbleflower", "Queen Marchesa", "Xyris, the Writhing Storm"}',
     '"politics": {"Kenrith, the Returned King", "Ms. Bumbleflower", "Queen Marchesa",\n'
     '                 "Xyris, the Writhing Storm", "Rendmaw, Creaking Nest",\n'
     '                 "Aragorn, King of Gondor", "Xantcha, Sleeper Agent"}'),
    ('"chaos": {"Mr. House, President and CEO", "Nekusar, the Mindrazer", "Xyris, the Writhing Storm"}',
     '"chaos": {"Mr. House, President and CEO", "Nekusar, the Mindrazer",\n'
     '              "Xyris, the Writhing Storm", "The Infamous Cruelclaw",\n'
     '              "Yusri, Fortune\'s Flame", "Maelstrom Wanderer", "Averna, the Chaos Bloom"}'),
]


def fix_ramp() -> None:
    total = 0
    for index in range(1, 19):
        path = DATA / f"descriptions_{index}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        hits = 0
        for entry in data.values():
            for field in ("intro", "build"):
                text = entry.get(field)
                if not text or "ramp" not in text.lower():
                    continue
                new = re.sub(r"ramp", "法术力加速", text, flags=re.IGNORECASE)
                if new != text:
                    entry[field] = new
                    hits += 1
        if hits:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        total += hits
    print(f"① ramp → 法术力加速：修正 {total} 个字段")


def fix_tags() -> None:
    path = DATA / "tag_zh.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    before = len(data)
    for key, value in NEW_TAGS.items():
        data.setdefault(key, value)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"② 标签中文名：{before} → {len(data)} 条")


def fix_expect() -> None:
    path = SCRIPTS / "axis_validation.py"
    text = path.read_text(encoding="utf-8")
    hits = 0
    for old, new in EXPECT:
        if old in text:
            text = text.replace(old, new)
            hits += 1
    path.write_text(text, encoding="utf-8")
    print(f"③ 全轴验证预期集：更新 {hits}/{len(EXPECT)} 项")


if __name__ == "__main__":
    fix_ramp()
    fix_tags()
    fix_expect()
