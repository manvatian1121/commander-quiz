# -*- coding: utf-8 -*-
"""一次性调整草稿里的断句（intro 3 句 / build 3 句），保持字数不变。"""
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
P = pathlib.Path(SCRIPT_DIR / "draft_descriptions_6.py")
text = P.read_text(encoding="utf-8")

PAIRS = [
    # build：把引出句的「：」改成「。」，凑够 3 句
    ("正好给主将凑能力；坟场里躺着{Devoted Druid}时", "正好给主将凑能力。坟场里躺着{Devoted Druid}时"),
    ("整套牌几乎都是伙伴生物，一进场就给你东西：{South Pole Voyager}", "整套牌几乎都是伙伴生物，一进场就给你东西。{South Pole Voyager}"),
    ("核心是让牌反复进出坟场：{Faithless Looting}", "核心是让牌反复进出坟场。{Faithless Looting}"),
    ("关键是把神器生物的攻击力做大：{Steel Overseer}", "关键是把神器生物的攻击力做大。{Steel Overseer}"),
    ("牌表大半是便宜又能点目标的瞬间和法术：{Prismari Command}", "牌表大半是便宜又能点目标的瞬间和法术。{Prismari Command}"),
    ("核心是磨牌本身：{Ruin Crab}", "核心是磨牌本身。{Ruin Crab}"),
    ("主动牺牲地，再从坟场一次全捞回来：{Zuran Orb}", "主动牺牲地，再从坟场一次全捞回来。{Zuran Orb}"),
    ("你能掌控的是挂在他身上的装备：{The Spear of Leonidas}", "你能掌控的是挂在他身上的装备。{The Spear of Leonidas}"),
    ("找装备的牌尤其重要：{Stoneforge Mystic}", "找装备的牌尤其重要。{Stoneforge Mystic}"),
    ("因为它们能放两次：{Ponder}", "因为它们能放两次。{Ponder}"),
    ("牺牲的来源要够多：{Korvold, Fae-Cursed King}", "牺牲的来源要够多。{Korvold, Fae-Cursed King}"),
    # intro：合并最后两句，回到 3 句
    ("它们同时还变成吸血鬼。喜欢天使", "它们同时还变成吸血鬼，喜欢天使"),
    ("冲了就得面对你的场面。喜欢把整桌", "冲了就得面对你的场面，喜欢把整桌"),
    ("中的换大的。喜欢攒零件的玩家会喜欢他。", "中的换大的，喜欢攒零件的玩家会喜欢他。"),
    ("坟场等于第二个手牌。喜欢反复利用同一张牌的玩家会喜欢他。", "坟场等于第二个手牌，喜欢反复利用同一张牌的玩家会喜欢他。"),
    ("就越省钱。喜欢赌一把", "就越省钱，喜欢赌一把"),
]

for old, new in PAIRS:
    cnt = text.count(old)
    if cnt != 1:
        print(f"✗ 匹配 {cnt} 次：{old[:30]}")
        raise SystemExit(1)
    text = text.replace(old, new)

P.write_text(text, encoding="utf-8")
print(f"✓ 完成 {len(PAIRS)} 处断句调整")
