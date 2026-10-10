# -*- coding: utf-8 -*-
"""探查：本批 17 位拍档主将 + 清单内所有牌的 card_zh.json 中文名覆盖情况。"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(__file__).resolve().parent.parent / "data"

card_zh = json.loads((DATA / "card_zh.json").read_text(encoding="utf-8"))
commander_zh = json.loads((DATA / "commander_zh.json").read_text(encoding="utf-8"))

CARDS = """Silence|Thassa's Oracle|Devoted Druid|Flusterstorm|Chrome Mox|Lotus Petal|Birds of Paradise|Polluted Delta|Misty Rainforest|Flooded Strand
Krark's Thumb|Tavern Scoundrel|Yusri, Fortune's Flame|Stitch in Time|Chance Encounter|Fiery Gambit|Squee's Revenge|Krark, the Thumbless|Sulfur Falls|Planar Chaos
Mox Amber|Springleaf Drum|Gaea's Cradle|Crop Rotation|Mox Diamond|Breeding Pool|Scalding Tarn|Wooded Foothills
Colossus Hammer|Puresteel Paladin|Sram, Senior Edificer|Open the Armory|Masterwork of Ingenuity|Steelshaper's Gift|Blackblade Reforged|Akiri, Fearless Voyager|Clifftop Retreat|Path to Exile
Harmonic Prodigy|Veyran, Voice of Duality|Strike It Rich|Twinflame|Storm-Kiln Artist|Lightning Bolt|Archmage Emeritus|Shivan Reef
Cresting Mosasaurus|Ghalta, Primal Hunger|Earthshaker Dreadmaw|Hulking Raptor|Etali, Primal Storm|Quartzwood Crasher|Curious Altisaur|Garruk's Uprising|Regisaur Alpha|Hunting Velociraptor
Seedborn Muse|Force of Will|Training Grounds|Mystic Remora|Fierce Guardianship|Swan Song
Finale of Devastation|Windswept Heath
Windfall|Faithless Looting|Glint-Horn Buccaneer|Tolarian Winds|Curiosity|Frantic Search|Mystic Monastery|Rielle, the Everwise|Talisman of Creativity
Hardened Scales|Forgotten Ancient|Brainstorm|Simic Ascendancy|Essence Flux|Laboratory Maniac|Hinterland Harbor|Yavimaya Coast|Rejuvenating Springs
Consider|Thought Scour|See the Truth|Baral, Chief of Compliance|Sunken Hollow|Dark Ritual|Ponder
Phyrexian Metamorph|Dig Through Time|Clever Impersonator|Spark Double|Treasure Cruise|Glasspool Mimic|Blasphemous Act|Steam Vents|Watery Grave|Blood Crypt
Mana Vault
Elmar, Ulvenwald Informant|Wernog, Rider's Chaplain|Sophina, Spearsage Deserter|Hargilde, Kindly Runechanter|Bjorna, Nightfall Alchemist|Ruinous Ultimatum|Temple Garden
Norin the Wary|Mines of Moria|Flowering of the White Tree|Keleth, Sunmane Familiar|Kediss, Emberclaw Familiar|Minas Tirith|Eiganjo, Seat of the Empire|Sokenzan, Crucible of Defiance|Urza's Ruinous Blast
Two-Handed Axe|Combat Celebrant|Combat Research|Professional Face-Breaker|Lizard Blades|Izzet Signet
Taborax, Hope's Demise|Shadow-Rite Priest|Priest of Forgotten Gods|Doomed Necromancer|Twilight Diviner|Priest of Gix|Victimize|Ayara, First of Locthwain|Zulaport Cutthroat|Black Market"""

names = []
for line in CARDS.splitlines():
    for n in line.split("|"):
        n = n.strip()
        if n:
            names.append(n)
print(f"清单唯一牌名 {len(set(names))} 张")
miss = [n for n in names if n not in card_zh]
print(f"card_zh MISS {len(miss)}：")
for m in miss:
    print("   ", m)

PAIRS = [
    "Thrasios, Triton Hero // Tymna the Weaver",
    "Okaun, Eye of Chaos // Zndrsplt, Eye of Wisdom",
    "Rograkh, Son of Rohgahh // Thrasios, Triton Hero",
    "Ardenn, Intrepid Archaeologist // Rograkh, Son of Rohgahh",
    "Krark, the Thumbless // Sakashima of a Thousand Faces",
    "Owen Grady, Raptor Trainer // Blue, Loyal Raptor",
    "Thrasios, Triton Hero // Vial Smasher the Fierce",
    "Thrasios, Triton Hero // Yoshimaru, Ever Faithful",
    "Brallin, Skyshark Rider // Shabraz, the Skyshark",
    "Pir, Imaginative Rascal // Toothy, Imaginary Friend",
    "Gale, Waterdeep Prodigy // Scion of Halaster",
    "Sakashima of a Thousand Faces // Vial Smasher the Fierce",
    "Tevesh Szat, Doom of Fools // Thrasios, Triton Hero",
    "Cecily, Haunted Mage // Othelm, Sigardian Outcast",
    "Rograkh, Son of Rohgahh // Yoshimaru, Ever Faithful",
    "Karlach, Fury of Avernus // Sword Coast Sailor",
    "Shadowheart, Dark Justiciar // Haunted One",
]
print(f"\n组合主将 {len(PAIRS)} 组")
for p in PAIRS:
    a, b = [x.strip() for x in p.split(" // ")]
    print(f"  {p}")
    print(f"     card_zh[全名]={card_zh.get(p)!r}  commander_zh[全名]={commander_zh.get(p)!r}")
    print(f"     左: card_zh={card_zh.get(a)!r} / commander_zh={commander_zh.get(a)!r}")
    print(f"     右: card_zh={card_zh.get(b)!r} / commander_zh={commander_zh.get(b)!r}")
