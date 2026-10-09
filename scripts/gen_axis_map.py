# -*- coding: utf-8 -*-
"""tag_vocabulary.txt -> tag_axis_map.json

用法: python gen_axis_map.py [--write]
自检: 词表 x 映射表 双向 diff，必须 404 全覆盖。
约束: 权重只用 0.5/1.0/1.5/2.0；每标签 <=3 个轴；轴 id 必须在 20 轴内。
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

DATA = Path(ROOT / "data")
VOCAB = DATA / "tag_vocabulary.txt"
OUT = DATA / "tag_axis_map.json"

AXES = {
    "aggro", "voltron", "wide", "ramp", "stompy", "control", "removal",
    "combo", "spells", "artifacts", "enchant", "grave", "tribal", "drain",
    "stax", "clonesteal", "politics", "chaos", "counters", "blink",
}
WEIGHTS = {0.5, 1.0, 1.5, 2.0}
T = 2.0

# ==================================================== 部落类别 -> tribal 2.0
# 值 = 附加轴（tribal 2.0 由代码补齐）
TRIBAL = {
    "Goblins": {"wide": 1.0, "aggro": 0.5},
    "Elves": {"ramp": 1.0},
    "Zombies": {"grave": 1.0},
    "Dragons": {"stompy": 1.0},
    "Merfolk": {"counters": 0.5},
    "Vampires": {"drain": 1.0},
    "Angels": {"wide": 0.5},
    "Dinosaurs": {"stompy": 1.0},
    "Slivers": {"wide": 0.5, "counters": 0.5},
    "Myr": {"artifacts": 1.0},
    "Cats": {"wide": 0.5},
    "Dogs": {"counters": 0.5},
    "Knights": {"aggro": 0.5},
    "Wizards": {"spells": 0.5},
    "Faeries": {"control": 0.5},
    "Horrors": {"grave": 0.5},
    "Sphinxes": {"control": 0.5},
    "Dwarves": {"artifacts": 0.5},
    "Bears": {"stompy": 0.5},
    "Birds": {"aggro": 0.5},
    "Elementals": {"blink": 0.5},
    "Squirrels": {"wide": 1.0},
    "Hydras": {"counters": 1.0},
    "Gods": {"enchant": 0.5},
    "Frogs": {"wide": 0.5},
    "Mutants": {"counters": 0.5},
    "Wolves": {"stompy": 0.5},
    "Treefolk": {"stompy": 0.5},
    "Rabbits": {"wide": 1.0},
    "Humans": {"aggro": 0.5},
    "Allies": {"blink": 0.5},
    "Ninjas": {"clonesteal": 0.5},
    "Villains": {"removal": 0.5},
    "Spirits": {"blink": 0.5},
    "Phyrexians": {"counters": 1.0},
    "Demons": {"stompy": 0.5},
    "Soldiers": {"wide": 1.0},
    "Warriors": {"aggro": 0.5},
    "Clerics": {"drain": 0.5},
    "Beasts": {"stompy": 0.5},
    "Rats": {"wide": 0.5},
    "Insects": {"wide": 0.5},
    "Constructs": {"artifacts": 1.0},
    "Saboteurs": {"aggro": 0.5},
    "Praetors": {"stax": 0.5},
    "Druids": {"ramp": 1.0},
    "Wraiths": {"drain": 0.5},
    "Relentless Rats": {"wide": 1.0},
    "Saprolings": {"wide": 1.0},
    "Rogues": {"grave": 0.5},
    "Rat Colony": {"wide": 1.0},
    "Pirates": {"clonesteal": 0.5},
    "Whales": {},
    "Sea Creatures": {},
    "Heroes": {"voltron": 0.5},
    "Assassins": {"removal": 0.5},
    "Oozes": {"counters": 0.5},
    "Giants": {"stompy": 1.0},
    "Advisors": {"politics": 0.5},
    "Shadowborn Apostles": {"combo": 0.5},
    "Spiders": {"stompy": 0.5},
    "Robots": {"artifacts": 1.0},
    "Blood": {"drain": 0.5},
    "Golems": {"stompy": 0.5},
    "Hare Apparent": {"wide": 1.0},
    "Samurai": {"voltron": 0.5},
    "Thopters": {"wide": 1.0, "artifacts": 0.5},
    "Wurms": {"stompy": 1.0},
    "Horses": {"aggro": 0.5},
    "Outlaws": {"removal": 0.5},
    "Shamans": {"ramp": 0.5},
    "Snakes": {"counters": 0.5},
    "Towns": {},
    "Goats": {"wide": 0.5},
    "Fungi": {"counters": 0.5},
    "Nightmares": {"drain": 0.5},
    "Avatars": {"stompy": 0.5},
    "Halflings": {"counters": 0.5},
    "Lizards": {"aggro": 0.5},
    "Otters": {"spells": 0.5},
    "Turtles": {"control": 0.5},
    "Werewolves": {"stompy": 0.5},
    "Tyranids": {"counters": 0.5},
    "Bats": {"drain": 0.5},
    "Elders": {"aggro": 0.5},
    "Apes": {"stompy": 0.5},
    "Crabs": {"control": 0.5},
    "Time Lords": {"chaos": 0.5},
    "Foxes": {"aggro": 0.5},
    "Archers": {"removal": 0.5},
    "Orcs": {"aggro": 0.5},
    "Devils": {"drain": 0.5},
    "Unicorns": {"aggro": 0.5},
    "Cybermen": {"counters": 0.5},
    "Drakes": {"aggro": 0.5},
    "Daleks": {"drain": 0.5},
    "Mice": {"aggro": 0.5},
    "Raccoons": {"counters": 0.5},
    "Tempest Hawk": {"aggro": 0.5},
    "Gnomes": {"artifacts": 0.5},
    "Phoenixes": {"aggro": 0.5},
    "Sharks": {"aggro": 0.5},
    "Griffins": {"aggro": 0.5},
    "Pegasi": {"aggro": 0.5},
    "Servos": {"wide": 1.0, "artifacts": 0.5},
    "Toys": {"artifacts": 0.5},
    "Astartes": {"aggro": 0.5},
    "Nobles": {},
    "Berserkers": {"aggro": 0.5},
    "Minions": {"aggro": 0.5},
    "Moonfolk": {"ramp": 0.5},
    "Necrons": {"grave": 0.5},
    "Kithkin": {"wide": 0.5},
    "Minotaurs": {"aggro": 0.5},
    "Detectives": {"removal": 0.5},
    "Lhurgoyfs": {"grave": 1.0},
    "Templar Knights": {"aggro": 0.5},
    "Mercenaries": {"removal": 0.5},
    "Scarecrows": {"artifacts": 0.5},
    "Monkeys": {"aggro": 0.5},
    "Rebels": {"removal": 0.5},
    "Specters": {"stax": 0.5},
    "Illusions": {"chaos": 0.5},
    "Cephalids": {},
    "Atogs": {"grave": 0.5},
    "Fractals": {"counters": 0.5},
    "Bards": {"politics": 0.5},
    "Elephants": {"stompy": 0.5},
    "Barbarians": {"aggro": 0.5},
    "Monks": {"spells": 0.5},
    "Crocodiles": {"aggro": 0.5},
    "Shades": {"drain": 0.5},
    "Symbiotes": {"counters": 0.5},
    "Ogres": {"stompy": 0.5},
    "Hippos": {"stompy": 0.5},
    "Kor": {"voltron": 0.5},
    "Satyrs": {"aggro": 0.5},
    "Kavu": {"aggro": 0.5},
    "Artificers": {"artifacts": 1.0},
    "Eldrazi": {"stompy": 1.0, "ramp": 0.5},
    "Books": {},
    "Clues": {"artifacts": 0.5},
    "Party": {"politics": 0.5},
    "Myriad": {"wide": 1.0},
    "Spacecraft": {"artifacts": 0.5},
}

# ==================================================== 非部落映射
MAPPED = {
    # ---------- 定义级 2.0 ----------
    "Tokens": {"wide": 2.0},
    "Voltron": {"voltron": 2.0},
    "Blink": {"blink": 2.0},
    "Stax": {"stax": 2.0},
    "Prison": {"stax": 2.0},
    "Hatebears": {"stax": 2.0},
    "Reanimator": {"grave": 2.0},
    "Graveyard": {"grave": 2.0},
    "Dredge": {"grave": 2.0},
    "Spellslinger": {"spells": 2.0},
    "Enchantress": {"enchant": 2.0},
    "Artifacts": {"artifacts": 2.0},
    "Stompy": {"stompy": 2.0},
    "Big Mana": {"ramp": 2.0},
    "Go Wide": {"wide": 2.0},
    "Lifedrain": {"drain": 2.0},
    "Clones": {"clonesteal": 2.0},
    "Politics": {"politics": 2.0},
    "Chaos": {"chaos": 2.0},
    "Coin Flip": {"chaos": 2.0},
    "Die Roll": {"chaos": 2.0},
    "Proliferate": {"counters": 2.0},
    "+1/+1 Counters": {"counters": 2.0},
    "Doomsday": {"combo": 2.0},
    "Rube Goldberg": {"combo": 2.0},

    # ---------- 快攻 / 铺场 / 大生物 ----------
    "Populate": {"wide": 2.0},
    "Aggro": {"aggro": 1.5, "wide": 0.5},
    "Weenies": {"aggro": 1.5, "wide": 1.0},
    "Zoo": {"aggro": 1.5, "stompy": 0.5},
    "Extra Combats": {"aggro": 1.5},
    "Speed": {"aggro": 1.0},
    "Attack Triggers": {"aggro": 1.0},
    "Infect": {"counters": 1.5, "aggro": 1.0},
    "Burn": {"aggro": 1.0, "spells": 1.0},
    "Anthems": {"wide": 1.0},
    "Squad": {"wide": 1.0},
    "Offspring": {"wide": 1.0},
    "Amass": {"wide": 1.0, "counters": 0.5},
    "Summons": {"ramp": 1.0, "stompy": 0.5},
    "Toughness Matters": {"stompy": 1.0},
    "Power Matters": {"stompy": 1.0},
    "Earthbending": {"ramp": 1.0, "counters": 1.0, "aggro": 0.5},
    "Enrage": {"stompy": 0.5},
    "Mutate": {"counters": 1.0, "stompy": 0.5},
    "Devoid": {"stompy": 0.5},
    "Freerunning": {"aggro": 0.5},
    "Battles": {"aggro": 0.5},
    "Land Animation": {"ramp": 0.5, "aggro": 0.5},
    "Fling": {"aggro": 0.5, "combo": 0.5},
    "Web-slinging": {"aggro": 0.5, "voltron": 0.5},
    "Lure": {"removal": 0.5, "stompy": 0.5},
    "Self-Destruct": {"combo": 0.5, "aggro": 0.5},

    # ---------- 主将单挑 / 结界灵气 ----------
    "Equipment": {"voltron": 1.5, "artifacts": 1.0},
    "Auras": {"enchant": 1.5, "voltron": 1.0},
    "Stoneblade": {"voltron": 1.5, "artifacts": 0.5},
    "Modified Creatures": {"counters": 1.0, "voltron": 0.5},
    "Exalted": {"voltron": 1.0},
    "Unblockable": {"voltron": 1.0, "aggro": 0.5},
    "Sunforger": {"voltron": 1.0, "removal": 0.5},
    "Indestructible": {"voltron": 0.5},
    "The Ring": {"counters": 0.5, "voltron": 0.5},
    "Sagas": {"enchant": 1.5},
    "Shrines": {"enchant": 1.5},
    "Rooms": {"enchant": 1.0},
    "Storied": {"enchant": 0.5},

    # ---------- 加速 ----------
    "Ramp": {"ramp": 1.5},
    "Landfall": {"ramp": 1.5},
    "Lands Matter": {"ramp": 1.5},
    "Mana Rocks": {"ramp": 1.5, "artifacts": 1.0},
    "Tron": {"ramp": 1.5},
    "Explore": {"ramp": 1.5},
    "Mana Dorks": {"ramp": 1.5},
    "Treasure": {"ramp": 1.0, "artifacts": 1.0},
    "Multicolor Matters": {"ramp": 1.0, "spells": 0.5},
    "Devotion": {"ramp": 0.5, "counters": 0.5},
    "Snow": {"ramp": 0.5},
    "Guildgates": {"ramp": 0.5},
    "Deserts": {"ramp": 0.5},
    "Caves": {"ramp": 0.5},

    # ---------- 神器机械 ----------
    "Vehicles": {"artifacts": 1.5},
    "Affinity": {"artifacts": 1.5},
    "Cheerios": {"artifacts": 1.5, "spells": 0.5},
    "Modular": {"artifacts": 1.5, "counters": 1.0},
    "Charge Counters": {"counters": 1.5, "artifacts": 0.5},
    "Food": {"artifacts": 1.0, "drain": 0.5},
    "Craft": {"artifacts": 1.0},
    "Improvise": {"artifacts": 1.0},
    "Incubate": {"counters": 1.0, "artifacts": 0.5},
    "Bobbleheads": {"artifacts": 1.0},
    "Waterbending": {"artifacts": 1.0, "ramp": 0.5},
    "Energy": {"artifacts": 0.5, "counters": 0.5},
    "Job Select": {"artifacts": 0.5},
    "Historic": {"artifacts": 0.5, "enchant": 0.5},
    "Value Vintage": {"combo": 0.5, "artifacts": 0.5},

    # ---------- 控制 / 互动 / 锁场 ----------
    "Control": {"control": 1.5},
    "Counterspells": {"control": 1.5},
    "Blue Moon": {"control": 1.5, "stax": 0.5},
    "Pillow Fort": {"control": 1.0, "stax": 1.0},
    "Defenders": {"control": 1.0},
    "Creatureless": {"control": 1.0, "spells": 0.5},
    "Planeswalkers": {"control": 1.0, "counters": 0.5},
    "Turbo Fog": {"stax": 1.5, "control": 0.5},
    "Rock": {"control": 1.0, "ramp": 0.5},
    "Extra Turns": {"control": 1.0, "combo": 0.5},
    "Hand Size": {"control": 0.5},
    "Color Hack": {"control": 0.5},
    "European Highlander": {"control": 0.5},
    "Premodern": {"control": 0.5},
    "Old School": {"stax": 0.5, "control": 0.5},
    "Flash": {"control": 0.5},
    "Fight": {"removal": 1.0},
    "Bounce": {"removal": 1.0},
    "Exile": {"removal": 1.0},
    "Pingers": {"drain": 1.0, "removal": 1.0},
    "Aikido": {"politics": 1.0, "removal": 1.0},
    "Deathtouch": {"removal": 0.5},
    "Crime": {"removal": 0.5, "clonesteal": 0.5},
    "-1/-1 Counters": {"counters": 1.5, "removal": 0.5},
    "Discard": {"stax": 1.5},
    "Wheels": {"stax": 1.0, "chaos": 0.5},
    "Land Destruction": {"stax": 1.5},
    "Stun": {"stax": 1.0},
    "Annihilator": {"stompy": 1.0, "stax": 0.5},
    "Curses": {"enchant": 1.5, "stax": 0.5},
    "Self-Discard": {"grave": 1.0, "stax": 0.5},
    "Hellbent": {"stax": 0.5, "aggro": 0.5},

    # ---------- 组合技 / 法术连发 ----------
    "Combo": {"combo": 1.5},
    "Storm": {"spells": 1.5, "combo": 1.0},
    "Eggs": {"combo": 1.5, "artifacts": 1.0},
    "Ad Nauseam": {"combo": 1.5},
    "Glass Cannon": {"combo": 1.5, "aggro": 0.5},
    "Primal Surge": {"combo": 1.5, "stompy": 0.5},
    "Spell Copy": {"spells": 1.5, "combo": 1.0},
    "All Spells": {"spells": 1.5},
    "Paradigm": {"spells": 1.0, "combo": 0.5},
    "Cascade": {"spells": 1.0, "combo": 1.0},
    "Discover": {"spells": 1.0, "combo": 0.5},
    "Birthing Pod": {"combo": 1.0},
    "Extra Upkeeps": {"combo": 1.0, "blink": 0.5},
    "Tap / Untap": {"combo": 1.0},
    "Time Counters": {"combo": 1.0},
    "Turbo": {"combo": 1.0, "spells": 0.5},
    "Prowess": {"spells": 1.0},
    "Cantrips": {"spells": 1.0},
    "X Spells": {"ramp": 1.0, "spells": 1.0},
    "Modal Spells": {"spells": 1.0},
    "Heroic": {"spells": 1.0, "voltron": 0.5},
    "Firebending": {"spells": 1.0, "aggro": 0.5},
    "Flashback": {"grave": 1.0, "spells": 0.5},
    "Retrace": {"spells": 1.0, "grave": 0.5},
    "Cycling": {"combo": 0.5, "grave": 0.5},
    "Suspend": {"spells": 0.5, "combo": 0.5},
    "Sneak Attack": {"clonesteal": 1.0, "combo": 0.5},
    "Topdeck": {"control": 0.5, "combo": 0.5},
    "Plot": {"spells": 0.5},
    "Prepared": {"spells": 0.5},
    "Foretell": {"spells": 0.5},
    "Adventures": {"spells": 0.5},
    "Impulse Draw": {"spells": 0.5, "chaos": 0.5},
    "Arcane": {"spells": 0.5},
    "Lessons": {"spells": 0.5},
    "Convoke": {"wide": 1.0, "spells": 0.5},

    # ---------- 坟场 ----------
    "Self-Mill": {"grave": 1.5},
    "Mill": {"grave": 1.5, "stax": 1.0},
    "Sacrifice": {"grave": 1.5, "drain": 0.5},
    "Surveil": {"grave": 1.0},
    "Delirium": {"grave": 1.0},
    "Looting": {"grave": 1.0},
    "Madness": {"grave": 1.0, "chaos": 0.5},
    "Exploit": {"grave": 1.0, "drain": 0.5},
    "Mayhem": {"grave": 0.5, "chaos": 0.5},
    "Descend": {"grave": 0.5},
    "Connive": {"counters": 1.0, "grave": 0.5},
    "Skeletons": {"tribal": 2.0, "grave": 0.5},

    # ---------- 进场触发 ----------
    "ETB": {"blink": 1.5},
    "Evoke": {"blink": 1.0},
    "LTB Effects": {"blink": 1.0, "grave": 0.5},
    "Airbending": {"removal": 1.0, "blink": 0.5},
    "Phasing": {"control": 0.5, "blink": 0.5},
    "Warp": {"blink": 0.5, "spells": 0.5},

    # ---------- 指示物 ----------
    "Counters Matter": {"counters": 1.5},
    "Rad Counters": {"counters": 1.5, "drain": 0.5},
    "Oil Counters": {"counters": 1.5, "drain": 0.5},
    "Bloodthirst": {"counters": 1.0, "aggro": 0.5},
    "Sunburst": {"counters": 1.0, "artifacts": 0.5},
    "Level Up": {"counters": 1.0},
    "Spore Counters": {"counters": 1.0, "wide": 0.5},
    "Experience Counters": {"counters": 1.0},
    "Power-up": {"counters": 1.0},
    "Increment": {"counters": 1.0},
    "Blight": {"counters": 1.0, "drain": 0.5},

    # ---------- 吸血消耗 ----------
    "Aristocrats": {"drain": 1.5, "grave": 1.0},
    "Group Slug": {"drain": 1.5},
    "Lifegain": {"drain": 1.0, "counters": 0.5},
    "Self-Damage": {"chaos": 0.5, "drain": 0.5},

    # ---------- 复制偷取 ----------
    "Theft": {"clonesteal": 1.5},
    "Shapeshifters": {"clonesteal": 1.5, "tribal": 0.5},
    "Polymorph": {"clonesteal": 1.0, "combo": 0.5},
    "Morph": {"chaos": 0.5, "clonesteal": 0.5},

    # ---------- 政治 ----------
    "Monarch": {"politics": 1.5},
    "Voting": {"politics": 1.5},
    "Group Hug": {"politics": 1.5},
    "Donate": {"politics": 1.0, "chaos": 0.5},
    "Forced Combat": {"politics": 1.0, "aggro": 0.5},
    "Villainous Choice": {"politics": 1.0, "chaos": 0.5},
    "Dungeon": {"combo": 0.5, "politics": 0.5},

    # ---------- 随机搞事 ----------
    "Attractions": {"chaos": 1.5},
    "Stickers": {"chaos": 1.5},
    "Planechase": {"chaos": 1.5},
    "Unnatural": {"chaos": 0.5},
    "Day / Night": {"chaos": 0.5},
    "Custom Cards": {"chaos": 0.5},
    "Paradox": {"chaos": 0.5},

    # ---------- 其它机械 / 模组 ----------
    "Ninjutsu": {"tribal": 1.0, "clonesteal": 0.5},
    "Plants": {"tribal": 2.0, "counters": 0.5},
    "Empower Jace": {"spells": 0.5},
    "Dandan": {"tribal": 2.0},
    "Power": {"stompy": 0.5},
    "Delver": {"spells": 1.0, "aggro": 0.5},
    "Type Hack": {"tribal": 1.0},
    "Persistent Petitioners": {"tribal": 1.5, "grave": 0.5},
    "Slime Against Humanity": {"tribal": 1.0, "wide": 0.5},
    "Dragon's Approach": {"tribal": 1.0, "spells": 1.0},
    "Umori Companion": {"combo": 0.5},
    "Keruga Companion": {"ramp": 0.5},
    "Gyruda Companion": {"grave": 0.5},
    "Jegantha Companion": {"ramp": 0.5},
    "Obosh Companion": {"aggro": 0.5},
    "Kaheera Companion": {"tribal": 0.5},
    "Zirda Companion": {"combo": 0.5},
    "Lurrus Companion": {"grave": 0.5},
}

IGNORED = {
    "Midrange": "泛用强度标签，151/151 主将全有，不指向任一玩法原型",
    "Good Stuff": "纯泛用，无玩法指向",
    "Card Draw": "通用资源动作，任何玩法都需要，不区分原型",
    "Commander Matters": "EDH 结构本身（人人都靠主将），不区分玩法",
    "Toolbox": "泛用「按需找答案」描述，横跨 control/removal/tribal",
    "Tempo": "泛用节奏标签，介于 aggro 与 control 之间，不构成原型",
    "Legends": "只描述牌张超类别（传奇），非玩法",
    "Activated Abilities": "只描述异能大类，几乎所有主将都有",
    "Triggered Abilities": "只描述异能大类，几乎所有主将都有",
    "Keywords": "泛用关键词集合，无具体玩法指向",
    "Vanilla": "白板生物，说明不了玩法",
    "Flying": "只描述生物关键词，不构成玩法原型",
    "Haste": "关键词，本身无玩法指向",
    "Menace": "关键词，无玩法指向",
    "Reach": "关键词，无玩法指向",
    "Skulk": "关键词，无玩法指向",
    "Horsemanship": "关键词（近似飞行），无玩法指向",
    "Landwalk": "关键词，无玩法指向",
    "Sneak": "关键词（潜袭类），玩法指向不明",
    "Banding": "关键字（联合阻挡），现代牌几乎不用，无玩法指向",
    "Life Exchange": "单卡效应描述（交换生命），非玩法原型",
    "Transform": "只描述牌张正反两面的状态，无玩法指向",
    "Miracles": "关键词（奇迹），触发不稳定，无固定玩法指向",
    "Kicker": "关键词（增幅），几乎所有系列都有，无玩法指向",
    "Scry": "通用占卜/牌库筛选，任何玩法都会用，不区分原型",
    "Cid": "主将人物名标签（非生物类别），玩法指向不明",
    "Repartee": "能力词（CR 207.2c，无独立规则义），玩法指向不明",
    "Opus": "能力词（CR 207.2c，无独立规则义），玩法指向不明",
}


def build():
    mapped = {}
    for tag, extra in TRIBAL.items():
        d = {"tribal": T}
        d.update(extra)
        mapped[tag] = d
    ov = set(mapped) & set(MAPPED)
    if ov:
        raise SystemExit(f"部落表与非部落表冲突: {sorted(ov)}")
    mapped.update(MAPPED)
    ov = set(mapped) & set(IGNORED)
    if ov:
        raise SystemExit(f"mapped/ignored 冲突: {sorted(ov)}")
    return mapped, dict(IGNORED)


def load_vocab():
    tags = []
    for ln in VOCAB.read_text(encoding="utf-8").splitlines():
        ln = ln.rstrip()
        if not ln.strip() or not ln.lstrip()[0].isdigit():
            continue
        m = re.match(r"^\s*(\d+)\s+(\d+)\s+(.+?)\s*$", ln)
        if not m:
            raise SystemExit(f"无法解析词表行: {ln!r}")
        tags.append(m.group(3))
    return tags


def main():
    vocab = load_vocab()
    mapped, ignored = build()
    print(f"词表: {len(vocab)} 个标签")

    missing = [t for t in vocab if t not in mapped and t not in ignored]
    extra = [t for t in list(mapped) + list(ignored) if t not in set(vocab)]
    fail = False
    if missing:
        fail = True
        print(f"[失败] 词表中未覆盖 {len(missing)} 个: {missing}")
    if extra:
        fail = True
        print(f"[失败] 映射表存在词表外标签 {len(extra)} 个: {sorted(extra)}")

    bad = []
    for tag, d in mapped.items():
        if not d:
            bad.append((tag, "空映射"))
        if len(d) > 3:
            bad.append((tag, f"{len(d)} 个轴 >3"))
        for axis, w in d.items():
            if axis not in AXES:
                bad.append((tag, f"未知轴 {axis}"))
            if w not in WEIGHTS:
                bad.append((tag, f"非法权重 {w}"))
    if bad:
        fail = True
        print(f"[失败] 取值非法 {len(bad)} 处: {bad}")

    total = len(mapped) + len(ignored)
    ok = (not fail) and total == len(vocab)
    print(f"总计 {len(vocab)} / mapped {len(mapped)} / ignored {len(ignored)} "
          f"/ 和 {total} -> {'自检通过' if ok else '自检失败'}")

    cover, wt = Counter(), Counter()
    for d in mapped.values():
        for a, w in d.items():
            cover[a] += 1
            wt[a] += w
    print("\n轴覆盖（标签数 / 权重和）:")
    for a in sorted(AXES, key=lambda x: -cover[x]):
        print(f"  {a:<12} {cover[a]:>4}  {wt[a]:>7.1f}")
    zero = [a for a in AXES if cover[a] == 0]
    if zero:
        print(f"[警告] 无标签指向的轴: {zero}")

    if not ok:
        raise SystemExit(1)

    if "--write" in sys.argv:
        payload = {
            "mapped": {t: mapped[t] for t in vocab if t in mapped},
            "ignored": {t: ignored[t] for t in vocab if t in ignored},
        }
        assert len(payload["mapped"]) + len(payload["ignored"]) == len(vocab)
        OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
        print(f"\n已写出 {OUT}")


if __name__ == "__main__":
    main()
