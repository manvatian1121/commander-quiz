# -*- coding: utf-8 -*-
"""生成 descriptions_14.json。

牌名一律通过 N(主将, 英文名) 注入：中文名从 data/card_zh.json 查，
查不到就只写英文（绝不手写译名）。所有英文名必须在 material 的该主将清单内。
"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

BASE = pathlib.Path(ROOT)
DATA = BASE / "data"
WL = json.loads((DATA / "_wb6_whitelist.json").read_text(encoding="utf-8"))
ZH = json.loads((DATA / "card_zh.json").read_text(encoding="utf-8"))

MISSING_ZH: list[str] = []


def N(cmd: str, en: str) -> str:
    """中英并列牌名；无官方中文名时只给英文。"""
    allowed = WL[cmd]["cards"]
    if en not in allowed:
        raise KeyError(f"{cmd} 的清单里没有这张牌：{en}")
    z = ZH.get(en)
    if not z:
        MISSING_ZH.append(f"{cmd} :: {en}")
        return en
    return f"{z}（{en}）"


def C(cmd: str) -> str:
    """主将自己的中英并列名（中文名取自素材标题）。"""
    return f"{WL[cmd]['zh']}（{cmd}）"


C1 = "Mister Negative"
C2 = "Anzrag, the Quake-Mole"
C3 = "Imoti, Celebrant of Bounty"
C4 = "Gisa, the Hellraiser"
C5 = "Felix Five-Boots"
C6 = "Hapatra, Vizier of Poisons"
C7 = "Magnus the Red"
C8 = "Black Panther, Wakandan King"
C9 = "Amalia Benavides Aguirre"
C10 = "Arixmethes, Slumbering Isle"
C11 = "Arthur, Marigold Knight"
C12 = "Progenitus"
C13 = "Massacre Girl, Known Killer"
C14 = "Camellia, the Seedmiser"
C15 = "Davros, Dalek Creator"
C16 = "Averna, the Chaos Bloom"
C17 = "Rivaz of the Claw"
C18 = "Tasha, the Witch Queen"
C19 = "Karlov of the Ghost Council"
C20 = "Baral, Chief of Compliance"
C21 = "Hamza, Guardian of Arashin"
C22 = "Bre of Clan Stoutarm"
C23 = "Jinnie Fay, Jetmir's Second"
C24 = "Ashling, Rekindled // Ashling, Rimebound"
C25 = "Loot, Exuberant Explorer"
C26 = "Anim Pakal, Thousandth Moon"
C27 = "Mizzix of the Izmagnus"
C28 = "Atarka, World Render"
C29 = "General Ferrous Rokiric"
C30 = "Emmara, Soul of the Accord"

CONTENT: dict[str, dict[str, str]] = {}


def add(cmd: str, tagline: str, intro: str, build: str) -> None:
    CONTENT[cmd] = {"tagline": tagline, "intro": intro, "build": build}


add(
    C1,
    "跟对手换血，换完还能抽牌",
    f"{C(C1)}是白黑双色的七费生物，打人时能顺手回一点血。它进场时可以和一位对手交换双方的生命总数；如果你因此少了血，就抓等量的牌。喜欢慢慢攒法术力、用一把大手牌翻盘的人会喜欢它。",
    f"重点在反复用它进场那一下：{N(C1, 'Ephemerate')}和{N(C1, 'Cloudshift')}都能让它先离场再回来，交换生命和抓牌就能再来一次；{N(C1, 'Children of Korlis')}能把你这一回合掉的血一次补回来。{N(C1, 'Talisman of Hierarchy')}这类产费牌帮忙凑齐七费。新人注意：它很贵，前期先专心铺地。",
)

add(
    C2,
    "逼对手来挡，挡住就再打一轮",
    f"{C(C2)}是红绿双色的四费生物。只要它被挡住，你所有生物就重新站起来，而且这一回合还会多出一次战斗；它自己也能花费用强迫对手来挡。喜欢一轮接一轮进攻、不想慢下来的人会喜欢它。",
    f"套牌里要放够逼对手阻挡的牌：{N(C2, 'Roar of Challenge')} 这类牌能让对手非挡不可，主将一被挡住就能重置全场、多打一轮。{N(C2, 'Rhythm of the Wild')}让你的生物不能被反击、进场还能选一个加成，{N(C2, 'Garruk\'s Uprising')}给全队践踏。新人注意：多打的几轮会耗光对手的阻挡者，自己也要留够法术力。",
)

add(
    C3,
    "大咒语自带连锁，一波接一波",
    f"{C(C3)}是蓝绿双色的五费生物。它自己会从牌库顶一路往下翻，翻到一张更便宜的牌就免费放出来；你放的六费以上大咒语也一样。喜欢越打越大、白拿的东西越滚越多的人会喜欢它。",
    f"先铺好法术力，然后开始放大的：{N(C3, 'Ghalta, Primal Hunger')}和{N(C3, 'Hullbreaker Horror')}这类大生物一进场，就顺带免费翻出更便宜的一张。{N(C3, 'Garruk\'s Uprising')}给全队践踏。新人注意：翻出来的是牌库顶的随机牌，别指望每次都翻到想要的那张。",
)

add(
    C4,
    "僵尸越堆越多，主将还护得紧",
    f"{C(C4)}是黑色的五费主将。她让你场上的骷髅和僵尸都更大一点、更难挡住；只要你针对对手做了点小动作，就会多出两只僵尸。喜欢堆一大群僵尸、慢慢淹过去的人会喜欢它。",
    f"主流是僵尸群：{N(C4, 'Death Baron')}给骷髅和僵尸再加一层强化，{N(C4, 'Undead Augur')}在你自己的僵尸死掉时帮你抓牌，{N(C4, 'Gray Merchant of Asphodel')}一次把对手的血削掉一大截。{N(C4, 'Jet Medallion')}让你的黑色咒语更便宜。新人注意：主将有守护，但别让它单独待在前排。",
)

add(
    C5,
    "打到人，触发的东西全算两遍",
    f"{C(C5)}是蓝黑绿三色的五费生物，自己有威慑和守护。它的本事是：只要你的生物打到对手、触发了你场上永久物的异能，那个异能就会再触发一次。喜欢用一串小好处慢慢把优势堆起来的人会喜欢它。",
    f"关键是那些打到人就有好处的牌：{N(C5, 'Ohran Frostfang')}和{N(C5, 'Bident of Thassa')}都能在生物打中对手时抓牌，有主将在，一次就是两张；{N(C5, 'Toski, Bearer of Secrets')}也一样。{N(C5, 'Hinterland Harbor')}这类地负责把三色凑齐。新人注意：打不到人就什么都不会发生。",
)

add(
    C6,
    "放一个指示物，就多一条蛇",
    f"{C(C6)}是黑绿双色的两费生物，打中对手时能让一个生物变小。每次你往某个生物身上放这种变小的指示物，就会多一条带死触的小蛇。喜欢用一堆小蛇慢慢磨、看对手生物一点点变小的人会喜欢它。",
    f"铺场路线是放指示物换蛇：{N(C6, 'Black Sun\'s Zenith')}一次给全场生物都放上指示物，转头就是一片蛇；{N(C6, 'Blowfly Infestation')}让指示物在生物死后一个个传下去；{N(C6, 'Necroskitter')}能把对手带着指示物死掉的生物捡回来自己用。新人注意：主将自己也是蛇的来源，别忘了让它去攻击。",
)

add(
    C7,
    "衍生物越多，法术越便宜",
    f"{C(C7)}是蓝红双色的五费生物，自己会飞。你场上的衍生物越多，你放的瞬间和法术就越便宜；它打中对手也能造出一个衍生物。喜欢一口气放很多小咒语、用一片衍生物压过去的人会喜欢它。",
    f"先铺造衍生物的牌：{N(C7, 'Song of Totentanz')}和{N(C7, 'Empty the Warrens')}能一次堆出一片，之后你的瞬间和法术就越放越便宜。{N(C7, 'Archmage Emeritus')}在你放或复制这类咒语时抓牌，{N(C7, 'Storm-Kiln Artist')}帮你产法术力。新人注意：这些衍生物本身很弱，别拿它们去挡大生物。",
)

add(
    C8,
    "把地当仓库，攒够了搬到生物上",
    f"{C(C8)}是白绿双色的两费主将。有生物进场，它就往你的一块地上放一个 +1/+1 指示物；攒够了再花三点法术力，一次全搬到某个生物身上。喜欢慢慢积累、然后一次爆发的人会喜欢它。",
    f"铺场的关键是不断有生物进场：{N(C8, 'Secure the Wastes')}能一次造出一小队战士，每只都给地加指示物；{N(C8, 'Kami of Whispered Hopes')}让每次放指示物都多一个。把指示物搬到生物上时还会回血抓牌，{N(C8, 'The Ozolith')}能在生物离场时保住这些指示物。新人注意：主将自己不擅长大打出手，前期别让它单独冲。",
)

add(
    C9,
    "一加血就探索，攒到二十清场",
    f"{C(C9)}是白黑双色的两费主将。每次你回血，她都会探索一次：是地就进手，否则自己变大一点。等她的力量刚好到二十，其他生物全被清掉。喜欢边回血边养大一只生物的人会喜欢它。",
    f"铺一堆有生物进场就回血的小家伙：{N(C9, 'Soul Warden')}和{N(C9, 'Soul\'s Attendant')}负责持续回血，主将就持续变大。{N(C9, 'Authority of the Consuls')}让对手的生物进场时都得横着，同时还在给你加血。新人注意：对手想动她就得先付三点血，但前期别指望她替你挡。",
)

add(
    C10,
    "先当一块地产费，睡醒就变大怪",
    f"{C(C10)}是蓝绿双色的四费主将。刚出场时它就是一块地，能产两点法术力；你每放一个咒语就能去掉一个睡眠指示物，睡够了就变成大海怪。喜欢前期不缺法术力的人会喜欢它。",
    f"前期它就是一块地，{N(C10, 'Growth Spiral')}这类咒语既能帮你多放一块地，本身也算放了一个咒语，可以顺手把它叫醒得更快。{N(C10, 'Garruk\'s Uprising')}给全队践踏，大海怪就算被小生物挡住也照样打到对手。新人注意：睡着的时候它不是生物，别指望它去挡。",
)

add(
    C11,
    "每次进攻都白拉一个帮手",
    f"{C(C11)}是白蓝红三色的五费主将，自带敏捷，出场就能打。只要它和别的生物一起进攻，就免费从牌库顶翻出一个生物跟着打；战斗结束它回手，下次还能再来。喜欢每次进攻都多一个打手的人会喜欢它。",
    f"{N(C11, 'Dour Port-Mage')}在生物离场回手时帮你抓牌，正好配上亚瑟每回合把打手送回手上；{N(C11, 'Sun Titan')}被拉进场时就在攻击，能立刻从坟场带回一张小永久物。{N(C11, 'Angel of the Ruins')}被拉进来时能顺手放逐神器或结界。新人注意：一定要凑够两只以上的进攻者，效果才会启动。",
)

add(
    C12,
    "十费的巨兽，几乎没人动得了它",
    f"{C(C12)}是五色的十费主将，很难被伤到、指到或挡住；就算它要进坟场，也会先回到牌库。整套牌就是想办法尽快凑出十点法术力，把它放出来。喜欢大后期、养一只谁都处理不掉的大兽的人会喜欢它。",
    f"全部重心都在法术力：{N(C12, 'Mirari\'s Wake')}让每块地多产一点，{N(C12, 'Faeburrow Elder')}在中期一次能产好几点。{N(C12, 'Fist of Suns')}让你付五个颜色各一就能把它放出来，省下五点；{N(C12, 'The World Tree')}在场时你的地能产任意颜色。新人注意：放它之前你会一直在铺地，要有耐心。",
)

add(
    C13,
    "把对手生物全变小，死了就抽牌",
    f"{C(C13)}是黑色的四费主将，自己有威慑。你所有生物造成的伤害都变成 -1/-1 指示物，把对手的生物越打越小；它们被减到 0 或更低而死时，你还能抓一张牌。喜欢控场磨光对手的人会喜欢它。",
    f"{N(C13, 'Black Sun\'s Zenith')}一次给全场生物放上一堆 -1/-1 指示物，被清掉的对手生物还能让主将帮你抓上几张牌；{N(C13, 'Blowfly Infestation')}让指示物在生物死后继续传下去，{N(C13, 'Necroskitter')}能把对手带指示物死掉的生物捡回来。新人注意：这套牌偏慢，要多留几手应对，别把自己摊空。",
)

add(
    C14,
    "松鼠越生越多，吃了食物就变强",
    f"{C(C14)}是黑绿双色的三费主将，它自己和别的松鼠都有威慑。每当你牺牲一个食物，就多一只松鼠；它还能觅食，让其他松鼠都变大。喜欢养一大群松鼠、看它们一起冲过去的人会喜欢它。",
    f"铺场全靠食物和松鼠：{N(C14, 'Gilded Goose')}和{N(C14, 'Peregrin Took')}不断给你塞食物，{N(C14, 'Chitterspitter')}让松鼠整体变大，{N(C14, 'Chatterfang, Squirrel General')}造衍生物时还会多出一批。新人注意：牺牲食物是好事，别舍不得；强化要点在自己身上，记得留法术力。",
)

add(
    C15,
    "逼对手掉血，掉够就多一个戴立克",
    f"{C(C15)}是蓝黑红三色的四费主将，自己带威慑。只要让对手一回合掉三点以上血，回合结束就能造出一个戴立克，还逼对手选：要么让你抓一张牌，要么自己弃一张牌。喜欢烧血又让对手手牌变少的人会喜欢它。",
    f"套牌里几乎都是能顺手打血的神器生物，{N(C15, 'Exterminate!')} 之类的牌负责清掉挡路的生物；每回合结束时造出的戴立克本身就是神器生物，{N(C15, 'Genesis of the Daleks')} 能一次铺出一队。{N(C15, 'Crumbling Necropolis')}这类三色地保证法术力不缺。新人注意：一定要在回合结束前让对手掉到三点血，不然这回合什么都不会发生。",
)

add(
    C16,
    "翻牌翻到的地，直接铺进场",
    f"{C(C16)}是蓝红绿三色的三费主将。你放那些会倾曳的牌时，会从牌库顶一路翻出一张更便宜的牌免费放出来；阿韦纳让你能把翻到的地也直接放进场。喜欢越打越顺、地越铺越多的人会喜欢它。",
    f"整套牌都围着倾曳转：{N(C16, 'Maelstrom Wanderer')}一次翻两张，{N(C16, 'Bloodbraid Elf')} 和 {N(C16, 'Apex Devastator')} 也都是这类牌，每翻一次就可能免费多铺一块地。新人注意：翻出来的地是横着进场的，当回合不能用；倾曳翻出来的是随机牌，翻到大牌就赚，翻到小牌也别失望。",
)

add(
    C17,
    "从坟场里一条条放龙出来",
    f"{C(C17)}是黑红双色的三费主将，带威慑。它能一次产两点只能用来放龙的法术力，而且每回合都能从坟场里再放一条龙出来。喜欢大龙一条接一条、把坟场也当资源用的人会喜欢它。",
    f"先用{N(C17, 'Faithless Looting')}把龙丢进坟场，再用主将把它们请回场上；{N(C17, 'Lathliss, Dragon Queen')}会让每一条新龙都带出一条龙，{N(C17, 'Dragon Tempest')}则在龙进场时打对手一下。新人注意：从坟场放出来的龙死后会被放逐，别指望再用第二次。",
)

add(
    C18,
    "用对手的牌，打对手的人",
    f"{C(C18)}是蓝黑双色的五费主将。她加忠诚就能抓一张牌，并把对手坟场里的瞬间或法术放逐、记上一笔；之后可以不付费用直接放出那些牌。放不是自己的牌时，还会多一个恶魔。喜欢借对手的牌反打的人会喜欢它。",
    f"核心是拿对手牌库和坟场里的东西：{N(C18, 'Hostage Taker')}先把对手的一个生物或神器借过来，{N(C18, 'Thief of Sanity')} 和 {N(C18, 'Gonti, Lord of Luxury')} 则把对手牌库顶的牌拿走放逐。{N(C18, 'Dimir Signet')}帮你更快凑到五点。新人注意：她不擅长正面硬拼，前期要多留应对手段。",
)

add(
    C19,
    "回一次血就长大，攒够就放逐",
    f"{C(C19)}是白黑双色的两费主将。你每次回血，它就多两个 +1/+1 指示物；攒够六个，再付一白一黑两点法术力，就能把对手一个生物放逐掉。喜欢一边回血一边攒个随时能用的解场手段的人会喜欢它。",
    f"铺一堆有生物进场就回血的小家伙：{N(C19, 'Soul Warden')}和{N(C19, 'Soul\'s Attendant')}让每次进场都算数，{N(C19, 'Vito, Thorn of the Dusk Rose')}把回血直接变成对手掉血。新人注意：放逐要花掉六个指示物，别急着用，留着对付最麻烦的那只。",
)

add(
    C20,
    "盯着对手的手，关键时候拦一手",
    f"{C(C20)}是蓝色的两费主将。你放的瞬间和法术都更便宜；每当你反击掉对手一个咒语，就能抓一张再弃一张，等于顺手把牌筛一遍。喜欢盯着对手的动作、在关键时刻出手阻拦的人会喜欢它。",
    f"套牌里放一批反击咒语：{N(C20, 'An Offer You Can\'t Refuse')}只花一点蓝就能挡下对手的非生物咒语，是便宜好用的选择。{N(C20, 'Archmage Emeritus')}在你放或复制瞬间、法术时抓牌，{N(C20, 'Sapphire Medallion')}让蓝色咒语更便宜。新人注意：反击要用在真正要紧的牌上，别看到什么都拦。",
)

add(
    C21,
    "指示物越多，大生物越便宜",
    f"{C(C21)}是白绿双色的六费主将。带 +1/+1 指示物的生物越多，它和你之后放的生物都越便宜。先铺一群小生物撒上指示物，大生物就会越来越便宜。喜欢场面越铺越大的人会喜欢它。",
    f"{N(C21, 'Hardened Scales')}让每次放指示物都多一个，{N(C21, 'Forgotten Ancient')}会随着每次有人放咒语不断攒指示物，还能转给别人。{N(C21, 'Inspiring Call')}能让你场上的生物全部不灭，同时按指示物的数量抓一把牌。新人注意：前期先铺小的、把指示物撒开，主将别急着放。",
)

add(
    C22,
    "回血越多，白拿的牌越大",
    f"{C(C22)}是红白双色的四费主将。她能让另一个生物暂时会飞、还能吸血；回合结束时，如果你这回合回过血，就从牌库顶往下翻牌，翻到的牌够便宜就能直接免费放出来。喜欢回血换大牌这套循环的人会喜欢它。",
    f"{N(C22, 'The Wind Crystal')}让你回的血翻倍，{N(C22, 'Rhox Faithmender')}也一样；{N(C22, 'Soul Warden')}负责每回合稳定回一点。回血越多，回合结束能免费放出来的牌就越大。新人注意：这回合要是没回血，主将的异能什么都不会发生，所以要让回血变成习惯。",
)

add(
    C23,
    "所有衍生物都变成猫或狗",
    f"{C(C23)}是红白绿三色的三费主将。本来该造出来的各种衍生物，你都可以改成 2/2 带敏捷的猫，或者 3/1 带警戒的狗。喜欢铺得快、进攻凶的人会喜欢它。",
    f"套牌里几乎每张牌都在造衍生物：{N(C23, 'Grand Crescendo')}一次造出一片，{N(C23, 'Impact Tremors')}让每个进场的小家伙都顺手打对手一点，{N(C23, 'Jetmir, Nexus of Revels')}在你生物够多时给全队加成。新人注意：敏捷的猫能当回合就冲上去，警戒的狗更适合留下来挡，什么时候用哪种要想一下。",
)

add(
    C24,
    "来回翻面，大咒语越放越顺",
    f"复炎灰儿（Ashling, Rekindled）是蓝红双色的两费双面主将。一面在你翻面或进场时帮你换一张手牌；翻到另一面，它会给你两点只能用来放四费以上咒语的法术力。花红蓝各一点就能来回翻，大咒语越放越顺。",
    f"两条路配合得很好：{N(C24, 'Thran Dynamo')}一次产三点无色法术力，帮你在前期凑够四点；{N(C24, 'Sunbird\'s Invocation')}在你放咒语时从牌库顶翻牌，正好放大的；{N(C24, 'Big Score')}既能抓牌又能造宝物。新人注意：翻面要花钱，别每一轮都翻，攒够想放的牌再切。",
)

add(
    C25,
    "地铺得越多，免费生物越大",
    f"{C(C25)}是绿色的三费主将。它让你每回合能多放一块地，还能花六点法术力，从牌库顶六张里直接免费放出一个费用不超过你地数量的生物。喜欢一块块铺地、再换成大家伙的人会喜欢它。",
    f"铺地本身就是收益：{N(C25, 'Llanowar Elves')}帮你多产法术力，{N(C25, 'Avenger of Zendikar')}和{N(C25, 'Rampaging Baloths')}每放一块地就造出一批衍生物，{N(C25, 'Scute Swarm')}更是越铺越多。新人注意：地越多，主将能免费放出的生物越大，所以前期别舍不得放地。",
)

add(
    C26,
    "打得越多，侏儒衍生物越多",
    f"{C(C26)}是红白双色的三费主将。只要你带着真的生物进攻（侏儒衍生物不算），它就先攒一个 +1/+1 指示物，然后造出等量的 1/1 神器生物衍生物，跟着一起打。喜欢越打人越多的人会喜欢它。",
    f"用一群便宜的小生物先开打，主将指示物越多，造的侏儒就越多：{N(C26, 'Rosie Cotton of South Lane')}在你造衍生物时顺手放指示物，{N(C26, 'Impact Tremors')}让每个进场的小家伙都打对手一点。新人注意：衍生物是横着进场直接参战的，但别把它们当长期防线。",
)

add(
    C27,
    "经验攒起来，法术越放越便宜",
    f"{C(C27)}是蓝红双色的四费主将。你放比现有经验指示物更大的瞬间或法术，就多一个经验指示物；经验越多，之后所有瞬间和法术都越便宜。喜欢先小打小闹、后面法术几乎免费的人会喜欢它。",
    f"{N(C27, 'Tezzeret\'s Gambit')}抓两张牌还能增殖，帮你把经验指示物攒得更快；{N(C27, 'Storm-Kiln Artist')}在你放或复制瞬间、法术时造宝物，帮你付那些越来越大的咒语；{N(C27, 'Frantic Search')}换牌的同时还能重置三块地。新人注意：先用便宜的法术把经验攒起来，别一开始就想放大招。",
)

add(
    C28,
    "每条龙进攻都打两倍伤害",
    f"{C(C28)}是红绿双色的七费主将，自己会飞、有践踏。它的好处很简单：你场上任何一条龙进攻，都会获得连击，一下顶两下。喜欢攒一群大龙、直接压过去的人会喜欢它。",
    f"龙的费用是最大的问题，{N(C28, 'Dragonspeaker Shaman')}和{N(C28, 'Dragonlord\'s Servant')}都能让龙更便宜；{N(C28, 'Dragon Tempest')}在你龙进场时打对手一下，还能让它们当回合就有行动力。新人注意：前期都在铺法术力，别急着放主将；龙被清掉一次就很难追回来。",
)

add(
    C29,
    "放一张双色牌，就多一个魔像",
    f"{C(C29)}是红白双色的三费主将，对手的单色招数拿它没办法。你每放一张双色咒语，就会多一个 4/4 的红白魔像。喜欢手牌几乎全是双色牌、每次出手都能带点东西的人会喜欢它。",
    f"整套牌几乎都该是红白双色牌：{N(C29, 'Boros Charm')}能一次给全队不灭，{N(C29, 'Deflecting Palm')}把对手的一次大伤害原样送回去。{N(C29, 'Blade Historian')}让所有进攻的生物都获得连击，正好和一堆 4/4 魔像配得上。新人注意：只放双色牌，看到同色的单色好牌先忍住。",
)

add(
    C30,
    "横置一次，就多一个士兵",
    f"{C(C30)}是白绿双色的两费主将。她只要被横置，就会造出一个 1/1 带系命的士兵，所以拿她去产法术力、或者帮忙付咒语的费用，都是在白拿人。喜欢地面越铺越宽的人会喜欢它。",
    f"{N(C30, 'Holdout Settlement')}和{N(C30, 'Jaspera Sentinel')}都能横置生物来产任意颜色的法术力，每横一次就多一个士兵；{N(C30, 'Champion of Lambholt')}在你生物进场时不断变大，越大对手越挡不住。新人注意：前期尽量每回合都找机会横置她一次，别让她闲着。",
)


def count(s: str) -> int:
    return sum(1 for ch in s if not ch.isspace())


def main() -> int:
    out = {}
    for cmd, fields in CONTENT.items():
        out[cmd] = fields
    if set(out) != set(WL):
        print("!! key 不一致：缺", sorted(set(WL) - set(out)), "多", sorted(set(out) - set(WL)))
        return 1
    order = list(WL)
    out = {k: out[k] for k in order}
    path = DATA / "descriptions_14.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"已写入 {path}")
    print(f"条目数 {len(out)}")

    bad = 0
    for cmd, f in out.items():
        t, i, b = count(f["tagline"]), count(f["intro"]), count(f["build"])
        flags = []
        if t > 20:
            flags.append(f"tagline 超 {t}")
        if not (70 <= i <= 120):
            flags.append(f"intro {i} 越界")
        if not (110 <= b <= 170):
            flags.append(f"build {b} 越界")
        if flags:
            bad += 1
        print(f"  {'✗' if flags else '✓'} {cmd:<44} t={t:>3} i={i:>3} b={b:>3}  {'；'.join(flags)}")
    print(f"\n越界条目：{bad}")
    print(f"缺中文名的引用（{len(set(MISSING_ZH))} 处）：")
    for m in sorted(set(MISSING_ZH)):
        print("   ", m)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
