# -*- coding: utf-8 -*-
"""生成 descriptions_17.json —— 17 位「拍档 / 身世」组合主将的 3 字段文案。

输出：data/descriptions_17.json
顺带：data/partner_component_zh.json（组合主将两半的中文名，
      供逐主将白名单 / 中英并列自检使用；素材标题里的中文名是权威来源）

字数按「去掉空白后的可见字符数」计（中文字、英文字母、括号、标点各算 1）。
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(__file__).resolve().parent.parent / "data"

# ---------------- 素材标题里的组合主将中英名（权威来源） ----------------
SRC = [DATA / f"writing_batch_new_{i}.md" for i in (1, 2, 3, 4, 5, 6)]
pairs = []  # (english_full, zh_full)
seen = set()
for src in SRC:
    for line in src.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## (.+?) ｜ (.+?)\s*$", line)
        if m:
            en, zh = m.group(1).strip(), m.group(2).strip()
            if en in seen:
                continue
            seen.add(en)
            pairs.append((en, zh))

component_zh = {}   # 两半英文名 -> 中文名
for en, zh in pairs:
    parts_en = [p.strip() for p in en.split(" // ")]
    parts_zh = [p.strip() for p in zh.split(" // ")]
    assert len(parts_en) == len(parts_zh), (en, zh)
    for a, b in zip(parts_en, parts_zh):
        component_zh[a] = b
(DATA / "partner_component_zh.json").write_text(
    json.dumps(component_zh, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"素材组合主将 {len(pairs)} 组；两半中文名 {len(component_zh)} 条")

# ---------------- 文案 ----------------
D = {}

D["Thrasios, Triton Hero // Tymna the Weaver"] = {
    "tagline": "两位主将一起上场，先把牌和地堆起来",
    "intro": "屈东英雄萨拉希洛斯（Thrasios, Triton Hero）和织命使堤谟娜（Tymna the Weaver）同为主将，四色齐全。一个花四点法术力就能翻牌换资源，一个连上对手几点血就顺手抽牌，靠这两点慢慢攒优势，喜欢掌控局面的人会喜欢。",
    "build": "先把地铺开，封口（Silence）、五彩玛珂（Chrome Mox）能让你更早出招；天堂鸟（Birds of Paradise）和虔诚德鲁伊（Devoted Druid）既产费也能顶上。真正结束游戏的是塔萨的先知（Thassa's Oracle），把图书馆翻空就赢。新手注意：花样多，前几局容易手忙脚乱。",
}

D["Okaun, Eye of Chaos // Zndrsplt, Eye of Wisdom"] = {
    "tagline": "两位主将一起赌硬币，赢一把涨一波",
    "intro": "混沌之眼欧寇然（Okaun, Eye of Chaos）和智慧之眼岑斯莉（Zndrsplt, Eye of Wisdom）都是主将。掷硬币赢了，欧寇然的力量就翻倍，岑斯莉让你抽一张；喀勒克的拇指（Krark's Thumb）能把胜率抬高不少。",
    "build": "酒馆恶棍（Tavern Scoundrel）、时间织联（Stitch in Time）都会额外掷硬币，赢来的宝物正好把地拉齐，也让两位主将更早出场；机缘（Chance Encounter）攒够幸运指示物还能直接获胜。新手注意：硬币不看情面，连输几把是常事，先接受这一点。",
}

D["Rograkh, Son of Rohgahh // Thrasios, Triton Hero"] = {
    "tagline": "零费主将先站场，三色一起铺地抽牌",
    "intro": "罗噶之子罗噶克（Rograkh, Son of Rohgahh）和屈东英雄萨拉希洛斯（Thrasios, Triton Hero）同时当主将，蓝绿红三色。罗噶克能免费上场，本身先攻、威慑、践踏；萨拉希洛斯负责铺地和抽牌，想又快又灵活的人会喜欢。",
    "build": "两位主将本身就是资源：琥珀玛珂（Mox Amber）和春叶鼓（Springleaf Drum）靠主将产费，轮耕法（Crop Rotation）能直接翻出盖亚的育苗地（Gaea's Cradle），一回合凑出很多法术力，再让萨拉希洛斯反复翻牌把地铺满。新手注意：前期先把产费的牌摆稳。",
}

D["Ardenn, Intrepid Archaeologist // Rograkh, Son of Rohgahh"] = {
    "tagline": "免费贴装备，小个子主将砍出大数字",
    "intro": "无畏考古家亚德恩（Ardenn, Intrepid Archaeologist）和罗噶之子罗噶克（Rograkh, Son of Rohgahh）同为主将，红白双色。罗噶克能免费上场，亚德恩每次战斗前都能免费贴上去，省下的费用全变成伤害。",
    "build": "罗噶克先站场，巨锤（Colossus Hammer）和重铸乌锋（Blackblade Reforged）交到他手上，亚德恩免费贴上去，直接打出大伤害。净钢神圣武士（Puresteel Paladin）和资深建筑师斯勒姆（Sram, Senior Edificer）帮你抽牌。新手注意：主将被打回主将区，装备要重贴。",
}

D["Krark, the Thumbless // Sakashima of a Thousand Faces"] = {
    "tagline": "法术复制个没完，两位主将一起掷硬币",
    "intro": "没有拇指的喀勒克（Krark, the Thumbless）和千面客逆岛（Sakashima of a Thousand Faces）同为主将。你放瞬间或法术都要掷硬币，赢了就把它再复制一份，逆岛则让你摆脱传奇规则，喜欢连发法术的人合适。",
    "build": "复制出来的喀勒克越多，同一个法术被复制的次数就越夸张，二元之声薇兰（Veyran, Voice of Duality）和泛音逸才（Harmonic Prodigy）能让这些触发再多来一遍。一夜暴富（Strike It Rich）和暴风窑艺家（Storm-Kiln Artist）负责铺宝物。新手注意：硬币输了法术就回手，容错低。",
}

D["Owen Grady, Raptor Trainer // Blue, Loyal Raptor"] = {
    "tagline": "两只恐龙主将，把指示物传来传去",
    "intro": "迅猛龙驯师欧文·格雷迪（Owen Grady, Raptor Trainer）和忠诚迅猛龙布鲁（Blue, Loyal Raptor）同为主将，蓝绿红三色。欧文能放上警戒、威慑、践踏三类指示物，布鲁让后来的恐龙也各带一个，想正面压过去的人会喜欢。",
    "build": "两位主将分工很清楚：先用欧文给布鲁放上想要的指示物，之后再出帝王龙首领（Regisaur Alpha）、石英林粉碎兽（Quartzwood Crasher）这些恐龙，它们一进场就自带那些好处；始饥戈厄塔（Ghalta, Primal Hunger）用来结束游戏。新手注意：先出哪只恐龙会决定整套的节奏。",
}

D["Thrasios, Triton Hero // Vial Smasher the Fierce"] = {
    "tagline": "一个负责铺地抽牌，一个随手丢伤害",
    "intro": "屈东英雄萨拉希洛斯（Thrasios, Triton Hero）和砸瓶女汉子（Vial Smasher the Fierce）都是主将，四色齐全。前者每回合都能铺地抓牌；她则在你每回合开头那个咒语上随机让对手挨伤害。",
    "build": "两位主将配合很顺：她打出的伤害等于那个咒语的法术力值，所以尽量放费用高的牌。训练场（Training Grounds）让萨拉希洛斯的翻牌更省钱，一轮能多翻几次；苗生谬思（Seedborn Muse）让它在对手回合也能接着翻。新手注意：她打谁不由你决定。",
}

D["Thrasios, Triton Hero // Yoshimaru, Ever Faithful"] = {
    "tagline": "传奇牌一张张进，狗越来越大",
    "intro": "屈东英雄萨拉希洛斯（Thrasios, Triton Hero）和忠犬义丸（Yoshimaru, Ever Faithful）都是主将。你放一个传奇永久物，义丸就多一个指示物；萨拉希洛斯负责抽牌铺地。这套牌什么都往传奇上靠，喜欢慢热的人合适。",
    "build": "节奏是：先用萨拉希洛斯把地和牌都铺开，同时出传奇牌给义丸加指示物。训练场（Training Grounds）让萨拉希洛斯的翻牌更省，琥珀玛珂（Mox Amber）和盖亚的育苗地（Gaea's Cradle）就很够用；幻灭终时（Finale of Devastation）把义丸放大。新手注意：传奇牌要一张张放。",
}

D["Brallin, Skyshark Rider // Shabraz, the Skyshark"] = {
    "tagline": "两位主将一起换手牌，越换对面越疼",
    "intro": "空鲨骑手布雷林（Brallin, Skyshark Rider）和空鲨沙布拉兹（Shabraz, the Skyshark）同为主将。你每弃一张牌，布雷林就变大一格并对每个对手造成一点伤害；你每抽一张牌，沙布拉兹就变大并回血，喜欢磨的人合适。",
    "build": "两位主将各管一头：横财（Windfall）和丧信掠夺（Faithless Looting）让你一次弃掉很多牌，布雷林就打出一片伤害；烁角海贼（Glint-Horn Buccaneer）也有同样的弃牌伤害。狂搜乱寻（Frantic Search）和好奇（Curiosity）负责不停抽牌，把沙布拉兹养大。新手注意：要算着弃牌和抽牌的数量。",
}

D["Pir, Imaginative Rascal // Toothy, Imaginary Friend"] = {
    "tagline": "两位主将搭一份指示物，越攒越大",
    "intro": "奇想顽童皮儿（Pir, Imaginative Rascal）和奇妙伙伴大牙（Toothy, Imaginary Friend）同为主将。皮儿让指示物多放一个，之后大牙每抽一张牌就长大一点，被赶走时还能把攒下的指示物换成手牌。",
    "build": "两位主将一起上：皮儿把指示物加成一份，坚固鳞甲（Hardened Scales）再叠一层，抽一次牌大牙都能大两格，比单放一个主将划算得多。脑力激荡（Brainstorm）和菁华异变（Essence Flux）让你一边抽牌一边把它弹回来再放下。实验室狂人（Laboratory Maniac）用来结束游戏。",
}

D["Gale, Waterdeep Prodigy // Scion of Halaster"] = {
    "tagline": "坟场当第二手牌，法术一张接一张",
    "intro": "深水城逸才盖尔（Gale, Waterdeep Prodigy）和海拉斯特的后裔（Scion of Halaster）同为主将，蓝黑双色。盖尔让你先放一个瞬间或法术后，再从坟场放另一类牌；后裔则让你的抽牌顺带筛选牌库。",
    "build": "两位主将的分工是：后裔每次抽牌时先看两张、挑一张进坟场，盖尔再把这些进坟场的牌捡回来放一遍，同一个咒语能反复利用。详加考虑（Consider）、洗清思想（Thought Scour）、看清真相（See the Truth）负责往坟场里塞牌，监察长巴罗（Baral, Chief of Compliance）让法术更便宜。",
}

D["Sakashima of a Thousand Faces // Vial Smasher the Fierce"] = {
    "tagline": "复制一堆主将，每次出牌都掉血",
    "intro": "千面客逆岛（Sakashima of a Thousand Faces）和砸瓶女汉子（Vial Smasher the Fierce）同为主将，蓝黑红三色。逆岛能变成场上别的永久物，还能同时留好几份；她则在你每回合第一个咒语时随机让对手掉血。",
    "build": "两位主将一起用讲究顺序：先用逆岛复制场上的她，这样每回合第一个咒语会触发好几遍伤害。火花替身（Spark Double）和机敏冒名客（Clever Impersonator）能再补上几份复制品，历时挖掘（Dig Through Time）和宝船巡游（Treasure Cruise）用来找牌。新手注意：复制前要确认场上有值得复制的东西。",
}

D["Tevesh Szat, Doom of Fools // Thrasios, Triton Hero"] = {
    "tagline": "一位主将抽牌，一位主将忙着铺地",
    "intro": "愚者末日泰维司刹特（Tevesh Szat, Doom of Fools）和屈东英雄萨拉希洛斯（Thrasios, Triton Hero）同为主将。刹特能生出小衍生物，也能吃掉别的东西换手牌；萨拉希洛斯把地往场上放，喜欢慢慢攒牌的人会喜欢。",
    "build": "两位主将各管一头：刹特生出的小衍生物正好当祭品，配合五彩玛珂（Chrome Mox）、魔法力库（Mana Vault）这类快速产费的牌，能更早把萨拉希洛斯放上场，再用地牌和抽牌把资源堆起来。意志之力（Force of Will）负责在关键时刻挡住对手。新手注意：刹特的大招要攒很久。",
}

D["Cecily, Haunted Mage // Othelm, Sigardian Outcast"] = {
    "tagline": "手牌越攒越多，倒下的还能再回来",
    "intro": "遭祟法师塞西莉（Cecily, Haunted Mage）和席嘉妲黜人奥塞姆（Othelm, Sigardian Outcast）同时当主将，五色齐全。塞西莉把手牌上限拉到十一张，攻击时还能白放法术；奥塞姆能把这个回合倒下的生物拉回来。",
    "build": "两位主将配合起来像一条流水线：先用骑兵教士维诺格（Wernog, Rider's Chaplain）、长矛贤者逃兵索菲娜（Sophina, Spearsage Deserter）、慈祥符颂师哈吉德（Hargilde, Kindly Runechanter）铺出线索，再用毁坏通牒（Ruinous Ultimatum）清场。新手注意：手牌要攒到十一张以上。",
}

D["Rograkh, Son of Rohgahh // Yoshimaru, Ever Faithful"] = {
    "tagline": "小主将配小狗，传奇牌一张张往外放",
    "intro": "罗噶之子罗噶克（Rograkh, Son of Rohgahh）和忠犬义丸（Yoshimaru, Ever Faithful）同为主将，红白双色。罗噶克能免费上场，本身先攻、威慑、践踏；你每放一个传奇永久物，义丸就多一个指示物，喜欢快攻的人会喜欢。",
    "build": "两位主将都很便宜，第一回合就能一起站场，接着一张张出传奇牌给义丸加指示物。谨慎的诺林（Norin the Wary）每次都自己走掉再回来，触发得很频繁；阳鬃佣兽凯勒丝（Keleth, Sunmane Familiar）和烬爪佣兽柯迪斯（Kediss, Emberclaw Familiar）让主将打得更狠。新手注意：主将便宜也就脆，别让它空手站着。",
}

D["Karlach, Fury of Avernus // Sword Coast Sailor"] = {
    "tagline": "两位主将一起多打一轮，谁也挡不住",
    "intro": "禽绝地狱之怒卡莱琪（Karlach, Fury of Avernus）和剑湾水手（Sword Coast Sailor）同为主将，蓝红双色。卡莱琪让你每回合多打一轮，水手让主将去打血最少的人时无法被阻挡，喜欢连打的人会喜欢。",
    "build": "两位主将的思路就是多打一轮、并且保证打得进去。战斗主祭（Combat Celebrant）能再多加一轮攻击，双手斧（Two-Handed Axe）和实战研究（Combat Research）让主将打得更痛、顺手抽牌。新手注意：多一轮攻击对手也多一轮反击。",
}

D["Shadowheart, Dark Justiciar // Haunted One"] = {
    "tagline": "两位主将一起牺牲，倒下的全都回来",
    "intro": "暗夜法官影心（Shadowheart, Dark Justiciar）和溺往苦主（Haunted One）同为主将，纯黑。影心能牺牲生物换手牌，换到的张数看那个生物的力量；苦主让主将被打横时变强，死后还能回来一次。",
    "build": "两位主将的分工是：溺往苦主（Haunted One）让影心被打横就能加攻击力；影心再把该牺牲的生物换成手牌。葬望魔塔博锐（Taborax, Hope's Demise）、影仪祝祷士（Shadow-Rite Priest）、弃神僧侣（Priest of Forgotten Gods）都在支撑这套，生体活祭（Victimize）负责把它们拉回来。",
}
# ---------------- 落盘 ----------------
out = DATA / "descriptions_17.json"
out.write_text(json.dumps(D, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

material = [en for en, _ in pairs]
print(f"\n写入 {out}：{len(D)} 条")
print("缺：", [m for m in material if m not in D], " 多：", [k for k in D if k not in material])


def count(s):
    return sum(1 for ch in s if not ch.isspace())


bad = []
for m in material:
    e = D[m]
    t, i, b = count(e["tagline"]), count(e["intro"]), count(e["build"])
    flag = []
    if t > 20:
        flag.append("T超标")
    if not (70 <= i <= 120):
        flag.append("I超标")
    if not (110 <= b <= 170):
        flag.append("B超标")
    if flag:
        bad.append((m, t, i, b, flag))
    print(f"  T{t:>3} I{i:>4} B{b:>4}  {'OK' if not flag else flag}  {m}")
print("\n超标：", len(bad))
for x in bad:
    print("   ", x)
