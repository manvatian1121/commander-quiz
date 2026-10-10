#!/usr/bin/env python3
"""全轴验证：为每个玩法轴构造「极端偏好」答案集，检查推荐落点是否是该原型的旗舰主将。"""
from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from engine import load_commanders, load_quiz, score_commanders, tally  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

DATA = pathlib.Path(ROOT / "data")

AXIS_ZH = {
    "aggro": "快攻压制", "voltron": "主将单挑", "wide": "铺场爆兵", "ramp": "加速爆费",
    "stompy": "大生物压制", "control": "控制反击", "removal": "精准互动", "combo": "组合技",
    "spells": "法术连发", "artifacts": "神器机械", "enchant": "结界灵气", "grave": "坟场复用",
    "tribal": "生物部落", "drain": "吸血消耗", "stax": "锁场剥夺", "clonesteal": "复制偷取",
    "politics": "政治博弈", "chaos": "随机搞事", "counters": "指示物增殖", "blink": "进场触发",
}

# 每个轴「最该出现」的旗舰主将（人工预期，用于检查匹配是否离谱）
EXPECTED = {
    "aggro": {"Krenko, Mob Boss", "Zurgo Stormrender", "Xenagos, God of Revels",
              "Imodane, the Pyrohammer", "Anzrag, the Quake-Mole",
              "Black Waltz No. 3", "Tifa, Martial Artist"},
    "voltron": {"Cloud, Ex-SOLDIER", "Light-Paws, Emperor's Voice", "Wyleth, Soul of Steel"},
    "wide": {"Krenko, Mob Boss", "Zurgo Stormrender", "Zinnia, Valley's Voice",
             "Shroofus Sproutsire", "The Unbeatable Squirrel Girl",
             "Baylen, the Haymaker", "Finneas, Ace Archer"},
    "ramp": {"Zhulodok, Void Gorger", "Zaxara, the Exemplary", "Kinnan, Bonder Prodigy",
             "Tifa Lockhart", "Toph, the First Metalbender",
             "Szarel, Genesis Shepherd", "Tannuk, Memorial Ensign",
             "Loot, Exuberant Explorer", "Tatyova, Benthic Druid",
             "Azusa, Lost but Seeking", "Toph, Earthbending Master"},
    "stompy": {"Gishath, Sun's Avatar", "Zhulodok, Void Gorger", "Pantlaza, Sun-Favored",
               "Ghalta, Primal Hunger", "Eshki, Temur's Roar",
               "Doran, Besieged by Time", "Tifa, Martial Artist"},
    "control": {"Talrand, Sky Summoner", "Y'shtola, Night's Blessed", "Grand Arbiter Augustin IV"},
    "removal": {"Queen Marchesa", "High Perfect Morcant", "Kelsien, the Plague",
                "Auntie Ool, Cursewretch", "Massacre Girl, Known Killer",
                "Fynn, the Fangbearer", "Ezio Auditore da Firenze"},
    "combo": {"Niv-Mizzet, Parun", "Fire Lord Azula", "Kinnan, Bonder Prodigy",
              "Sisay, Weatherlight Captain", "Breya, Etherium Shaper",
              "Atla Palani, Nest Tender", "Shorikai, Genesis Engine",
              "Noctis, Prince of Lucis", "Emry, Lurker of the Loch",
              "Jhoira, Weatherlight Captain", "Thranduil, the Elvenking"},
    "spells": {"Vivi Ornitier", "Talrand, Sky Summoner", "Niv-Mizzet, Parun",
               "Judith, Carnage Connoisseur", "Kuja, Genome Sorcerer",
               "Elsha, Threefold Master", "Bria, Riptide Rogue", "Iroh, Grand Lotus"},
    "artifacts": {"Urza, Lord High Artificer", "Breya, Etherium Shaper", "Shorikai, Genesis Engine"},
    "enchant": {"Light-Paws, Emperor's Voice", "Tom Bombadil", "Eriette of the Charmed Apple",
                "Anikthea, Hand of Erebos"},
    "grave": {"Muldrotha, the Gravetide", "Meren of Clan Nel Toth", "Teysa Karlov"},
    "tribal": {"Wilhelt, the Rotcleaver", "Lathril, Blade of the Elves", "Voja, Jaws of the Conclave",
               "Giada, Font of Hope", "Arahbo, Roar of the World",
               "Rat King, Verminister", "Wick, the Whorled Mind"},
    "drain": {"Teysa Karlov", "Oloro, Ageless Ascetic", "Valgavoth, Harrower of Souls",
              "Bilbo, Birthday Celebrant", "Astarion, the Decadent",
              "Amalia Benavides Aguirre", "Dina, Soul Steeper"},
    "stax": {"Tergrid, God of Fright", "Grand Arbiter Augustin IV", "Nekusar, the Mindrazer"},
    "clonesteal": {"Miirym, Sentinel Wyrm", "Maralen, Fae Ascendant", "Yuriko, the Tiger's Shadow",
                   "Satoru Umezawa", "Obeka, Brute Chronologist",
                   "Gonti, Canny Acquisitor", "Don Andres, the Renegade"},
    "politics": {"Queen Marchesa", "Ms. Bumbleflower", "Kenrith, the Returned King",
                 "Xyris, the Writhing Storm", "Rendmaw, Creaking Nest",
                 "Aragorn, King of Gondor", "Xantcha, Sleeper Agent"},
    "chaos": {"Mr. House, President and CEO", "Nekusar, the Mindrazer",
              "Xyris, the Writhing Storm", "The Infamous Cruelclaw",
              "Yusri, Fortune's Flame", "Maelstrom Wanderer", "Averna, the Chaos Bloom"},
    "counters": {"Atraxa, Praetors' Voice", "Tidus, Yuna's Guardian", "The Wise Mothman"},
    "blink": {"Brago, King Eternal", "Yarok, the Desecrated", "Pantlaza, Sun-Favored",
              "Katara, the Fearless", "Delney, Streetwise Lookout",
              "Ashling, the Limitless", "Minthara, Merciless Soul"},
}


def build_answers(quiz: dict, axis: str, top_k: int = 1) -> dict[int, int]:
    """每题选该轴得分最高的若干选项。"""
    answers: dict[int, int] = {}
    for question in quiz["questions"]:
        scored = []
        for index, opt in enumerate(question["opts"]):
            value = (opt.get("s") or {}).get(axis, 0.0)
            if value > 0:
                scored.append((value, index))
        if not scored:
            continue
        scored.sort(reverse=True)
        if question.get("multi"):
            answers[question["id"]] = [i for _, i in scored[:question["multi"]]]
        else:
            answers[question["id"]] = scored[0][1] if top_k == 1 else scored[0][1]
    return answers


def main() -> int:
    quiz = load_quiz()
    payload = load_commanders()
    hits, misses = 0, []

    for axis in AXIS_ZH:
        answers = build_answers(quiz, axis)
        pref, colors, cons = tally(quiz, answers)
        results = score_commanders(payload, pref, colors, cons)
        top5 = [r["en"] for r in results[:5]]
        top1 = top5[0]
        ok = top1 in EXPECTED[axis] or bool(set(top5) & EXPECTED[axis])
        hits += 1 if ok else 0
        mark = "✓" if ok else "✗"
        print(f"{mark} {axis:<11}{AXIS_ZH[axis]:<7} → {' | '.join(n[:26] for n in top5[:3])}")
        if not ok:
            misses.append(f"{axis} 前五无预期主将（预期 {sorted(EXPECTED[axis])}，实得 {top5}）")

    print(f"\n{'=' * 70}\n命中 {hits}/{len(AXIS_ZH)} 个轴")
    if misses:
        print(f"\n⚠ 需人工复核 {len(misses)} 处：")
        for item in misses:
            print(f"  - {item}")
    return 0 if not misses else 1


if __name__ == "__main__":
    raise SystemExit(main())
