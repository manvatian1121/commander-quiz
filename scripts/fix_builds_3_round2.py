"""第二轮回填：给 24 条汉字数偏短的 build 补一句收尾句，使其落入 110~170 区间。"""
import json
import pathlib
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
CJK = re.compile(r"[\u4e00-\u9fff]")

APPEND = {
    "Kotis, the Fangkeeper": "他一个人就能撑起整套牌的节奏。",
    "Ghyrson Starn, Kelermorph": "小伤害反而更狠。",
    "The First Sliver": "裂片妖之间还会互相加成。",
    "Kilo, Apogee Mind": "指示物攒得越多，收益越明显。",
    "Ragost, Deft Gastronaut": "神器越多，火力越猛。",
    "Norman Osborn": "正面偷牌长大，反面才是真正的杀手。",
    "Urtet, Remnant of Memnarch": "秘耳多了以后，横置产法术力也很划算。",
    "Captain N'ghathrod": "对手越挣扎，坟场越厚，你的场面越大。",
    "Omnath, Locus of Creation": "奖励拿满的回合，对手会很难受。",
    "Hope Estheim": "回血和磨牌其实是同一件事的两面。",
    "Voja, Jaws of the Conclave": "他一攻击，全队都跟着变大一截。",
    "High Perfect Morcant": "她的核心就是让对手的生物越用越废，自己的妖精越铺越多。",
    "Alela, Cunning Conqueror": "对手每回合都得提防你手里有招，节奏自然被你带着走。",
    "Magda, Brazen Outlaw": "五个宝物就能换一张大牌，收益非常高。",
    "Obeka, Splitter of Seconds": "多出来的维持越多，场上的牌触发得越勤。",
    "Sidar Jabari of Zhalfir": "骑士一波接一波，坟场就是你的第二手牌。",
    "Zinnia, Valley's Voice": "铺得越满她越大。",
    "Niv-Mizzet, Parun": "抽牌和伤害在他身上是同一件事。",
    "Brago, King Eternal": "每打中一次，场上的效果就再来一轮。",
    "Anikthea, Hand of Erebos": "坟场里的结界越多，你能复活的东西越多。",
    "Yarok, the Desecrated": "进场效果越多，这套牌越赚。",
    "Tergrid, God of Fright": "对手越舍不得牺牲，就越吃亏。",
    "Light-Paws, Emperor's Voice": "灵气一层层堆上去，她很快就能一个人打穿一路。",
    "Wyleth, Soul of Steel": "装备堆得越多，他打起来越轻松。",
}

for i in (1, 2, 3, 4):
    p = DATA / f"_part{i}_3.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    for k, tail in APPEND.items():
        if k in data:
            b = data[k]["build"]
            assert b.endswith("。"), k
            data[k]["build"] = b + tail
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"已追加收尾句 {len(APPEND)} 条")
for k, tail in APPEND.items():
    print(f"   {k:32s} +{len(CJK.findall(tail))} 汉字")
