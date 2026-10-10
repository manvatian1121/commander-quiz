# -*- coding: utf-8 -*-
"""量每个「中文（English）」串的可见字符数，方便按字数配平。"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

S = """屈东英雄萨拉希洛斯（Thrasios, Triton Hero）
织命使堤谟娜（Tymna the Weaver）
封口（Silence）
五彩玛珂（Chrome Mox）
莲花瓣（Lotus Petal）
天堂鸟（Birds of Paradise）
虔诚德鲁伊（Devoted Druid）
塔萨的先知（Thassa's Oracle）
混沌之眼欧寇然（Okaun, Eye of Chaos）
智慧之眼岑斯莉（Zndrsplt, Eye of Wisdom）
喀勒克的拇指（Krark's Thumb）
酒馆恶棍（Tavern Scoundrel）
命运烈焰亚司利（Yusri, Fortune's Flame）
时间织联（Stitch in Time）
机缘（Chance Encounter）
罗噶之子罗噶克（Rograkh, Son of Rohgahh）
琥珀玛珂（Mox Amber）
春叶鼓（Springleaf Drum）
轮耕法（Crop Rotation）
盖亚的育苗地（Gaea's Cradle）
无畏考古家亚德恩（Ardenn, Intrepid Archaeologist）
巨锤（Colossus Hammer）
重铸乌锋（Blackblade Reforged）
净钢神圣武士（Puresteel Paladin）
资深建筑师斯勒姆（Sram, Senior Edificer）
流放之径（Path to Exile）
双手斧（Two-Handed Axe）
没有拇指的喀勒克（Krark, the Thumbless）
千面客逆岛（Sakashima of a Thousand Faces）
二元之声薇兰（Veyran, Voice of Duality）
泛音逸才（Harmonic Prodigy）
一夜暴富（Strike It Rich）
暴风窑艺家（Storm-Kiln Artist）
迅猛龙驯师欧文·格雷迪（Owen Grady, Raptor Trainer）
忠诚迅猛龙布鲁（Blue, Loyal Raptor）
帝王龙首领（Regisaur Alpha）
石英林粉碎兽（Quartzwood Crasher）
巨身迅猛龙（Hulking Raptor）
始饥戈厄塔（Ghalta, Primal Hunger）
始啸埃泰力（Etali, Primal Storm）
砸瓶女汉子（Vial Smasher the Fierce）
训练场（Training Grounds）
苗生谬思（Seedborn Muse）
忠犬义丸（Yoshimaru, Ever Faithful）
幻灭终时（Finale of Devastation）
空鲨骑手布雷林（Brallin, Skyshark Rider）
空鲨沙布拉兹（Shabraz, the Skyshark）
横财（Windfall）
无情劫掠（Faithless Looting）
烁角海贼（Glint-Horn Buccaneer）
狂搜乱寻（Frantic Search）
好奇（Curiosity）
奇想顽童皮儿（Pir, Imaginative Rascal）
奇妙伙伴大牙（Toothy, Imaginary Friend）
坚固鳞甲（Hardened Scales）
脑力激荡（Brainstorm）
菁华异变（Essence Flux）
实验室狂人（Laboratory Maniac）
深水城逸才盖尔（Gale, Waterdeep Prodigy）
海拉斯特的后裔（Scion of Halaster）
详加考虑（Consider）
洗清思想（Thought Scour）
看清真相（See the Truth）
监察长巴罗（Baral, Chief of Compliance）
火花替身（Spark Double）
机敏冒名客（Clever Impersonator）
历时挖掘（Dig Through Time）
宝船巡游（Treasure Cruise）
愚者末日泰维司刹特（Tevesh Szat, Doom of Fools）
魔法力库（Mana Vault）
意志之力（Force of Will）
躁乱风暴（Flusterstorm）
遭祟法师塞西莉（Cecily, Haunted Mage）
席嘉妲黜人奥塞姆（Othelm, Sigardian Outcast）
骑兵教士维诺格（Wernog, Rider's Chaplain）
长矛贤者逃兵索菲娜（Sophina, Spearsage Deserter）
慈祥符颂师哈吉德（Hargilde, Kindly Runechanter）
夜幕炼金术士比约纳（Bjorna, Nightfall Alchemist）
毁坏通牒（Ruinous Ultimatum）
谨慎的诺林（Norin the Wary）
阳鬃佣兽凯勒丝（Keleth, Sunmane Familiar）
烬爪佣兽柯迪斯（Kediss, Emberclaw Familiar）
禽绝地狱之怒卡莱琪（Karlach, Fury of Avernus）
剑湾水手（Sword Coast Sailor）
战斗主祭（Combat Celebrant）
蜥蜴双刀（Lizard Blades）
实战研究（Combat Research）
破相好手（Professional Face-Breaker）
暗夜法官影心（Shadowheart, Dark Justiciar）
溺往苦主（Haunted One）
葬望魔塔博锐（Taborax, Hope's Demise）
影仪祝祷士（Shadow-Rite Priest）
弃神僧侣（Priest of Forgotten Gods）
生体活祭（Victimize）"""


def count(s):
    return sum(1 for ch in s if not ch.isspace())


for line in S.splitlines():
    print(f"{count(line):>3}  {line}")
