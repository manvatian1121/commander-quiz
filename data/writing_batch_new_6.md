# 写作规范（务必先读）

你正在为一份「EDH 新人主将挑选测试」写结果页文案。测试做完后，用户会看到 3 位主将，
每位主将下面要有**一段基本介绍**和**一段组的简单思路**。你要写的就是这个。

## 读者是谁
刚接触万智牌、可能只打过几局的新人。他们不懂行话。
- 不要用「voltron」「stax」「ramp」「引擎」「曲线」这类术语；要用大白话。
- 提到牌名时，中英并列，例如「鬼怪战酋（Goblin Warchief）」。

## 每条要写三个字段

| 字段 | 内容 | 长度 |
|---|---|---|
| `tagline` | 一句话定位，让人一眼知道这套牌在干嘛 | **20 字以内** |
| `intro` | 基本介绍：这位主将是谁、这套牌想做什么、什么样的人会喜欢 | **70~120 字，2~3 句** |
| `build` | 组的简单思路：大致铺什么、靠什么赢、关键搭配怎么配合、新人要注意什么 | **110~170 字，3~4 句** |

## 硬性规则（违反即作废）

1. **只能提到素材里给你的牌名**。素材里的「协同度高」「出场率高」两个清单是真实数据。
   清单之外一张牌都不许提——不许凭记忆补充，哪怕你确定它很配。
2. **牌面事实必须与素材给的 oracle text 一致**。不确定某张牌干什么，就别描述它的具体效果，
   改成描述它在套牌里的作用（例如「帮你加速」）。
3. **不要编造数字**。不要写「大约 37 张地」这种没依据的数；要写就写
   「一半以上是地」「十几张加速」这类定性描述。
4. **不要吹强度**。这是一份口味匹配工具，不是强度榜。写「新手友好」「上手简单」可以，
   写「最强」「上分神器」不行。
5. **不要提 Bracket / EDHREC / 咸度这些后台指标的名字**，那是给你参考语气的，不是给用户看的。
   咸度高（>2.0）的主将可以说「这套牌会让对手有点难受，别在朋友局里第一次就掏出来」。
6. 语气：平实、具体、像老玩家在给新人讲，不要营销腔，不要感叹号堆砌。

## 输出格式

严格输出如下 JSON，key 必须是素材里的英文主将名（一字不差）：

```json
{
  "Krenko, Mob Boss": {
    "tagline": "鬼怪越铺越多，最后一波带走",
    "intro": "...",
    "build": "..."
  }
}
```

不要输出 Markdown 代码块以外的任何解释文字。不要遗漏任何一位主将。


---

# 素材：30 位主将


## Mister Negative ｜ 底片先生
- 颜色 WB ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Human Villain
- 流行度：EDHREC 全时段第 471 位，约 6127 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.82 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.72
- 社区标签：生命增益、自伤、闪现回场、Life Exchange、吸取生命、组合技
- 完整牌面：Vigilance, lifelink
Darkforce Inversion — When Mister Negative enters, you may exchange life totals with target opponent. If you lost life this way, draw that many cards.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ephemerate（{W}｜Instant） — Exile target creature you control, then return it to the battlefield under its owner's control. Rebound (If you cast this spell from your hand, exile it as it resolves. A
  2. Cloudshift（{W}｜Instant） — Exile target creature you control, then return that card to the battlefield under your control.
  3. Wall of Blood（{2}{B}｜Creature — Wall） — Defender (This creature can't attack.) Pay 1 life: This creature gets +1/+1 until end of turn.
  4. Children of Korlis（{W}｜Creature — Human Rebel Cleric） — Sacrifice this creature: You gain life equal to the life you've lost this turn. (Damage causes loss of life.)
  5. Tainted Remedy（{2}{B}｜Enchantment） — If an opponent would gain life, that player loses that much life instead.
  6. Teleportation Circle（{3}{W}｜Enchantment） — At the beginning of your end step, exile up to one target artifact or creature you control, then return that card to the battlefield under its owner's control.
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Hierarchy（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {B}. This artifact deals 1 damage to you.
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Anzrag, the Quake-Mole ｜ 地动鼹鼠安札格
- 颜色 RG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Mole God
- 流行度：EDHREC 全时段第 472 位，约 6117 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.6 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $7.22
- 社区标签：额外战斗、快攻、主将单挑、组合技、加速、装备
- 完整牌面：Whenever Anzrag becomes blocked, untap each creature you control. After this phase, there is an additional combat phase.
{3}{R}{R}{G}{G}: Anzrag must be blocked each combat this turn if able.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Roar of Challenge（{2}{G}｜Sorcery） — All creatures able to block target creature this turn do so. Ferocious — That creature gains indestructible until end of turn if you control a creature with power 4 or gr
  2. Irresistible Prey（{G}｜Sorcery） — Target creature must be blocked this turn if able. Draw a card.
  3. Anara, Wolvid Familiar（{3}{G}｜Legendary Creature — Wolf Beast） — During your turn, commanders you control have indestructible. (Effects that say "destroy" don't destroy them. A creature with indestructible can't be destroyed by damage.
  4. General Marhault Elsdragon（{2}{R}{G}｜Legendary Creature — Elf Warrior） — Whenever a creature you control becomes blocked, it gets +3/+3 until end of turn for each creature blocking it.
  5. Lure（{1}{G}{G}｜Enchantment — Aura） — Enchant creature All creatures able to block enchanted creature do so.
  6. You Look Upon the Tarrasque（{4}{G}｜Instant） — Choose one — • Run and Hide — Prevent all combat damage that would be dealt to you and creatures you control this turn. • Gather Your Courage — Target creature gets +5/+5
- **出场率最高的牌**（大多数牌组都会放）
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Goblin Anarchomancer（{R}{G}｜Creature — Goblin Shaman） — Each spell you cast that's red or green costs {1} less to cast.
  - Rhythm of the Wild（{1}{R}{G}｜Enchantment） — Creature spells you control can't be countered. Nontoken creatures you control have riot. (They enter with your choice of a +1/+1 
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 


## Imoti, Celebrant of Bounty ｜ 恩赐主祭依莫提
- 颜色 UG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Snake Druid
- 流行度：EDHREC 全时段第 473 位，约 6086 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.51 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.33
- 社区标签：倾曳、爆费、加速、额外回合、奥札奇、组合技
- 完整牌面：Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. Put the exiled cards on the bottom in a random order.)
Spells you cast with mana value 6 or greater have cascade.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess combat damage to the player or planeswalker
  2. Apex Devastator（{8}{G}{G}｜Creature — Chimera Hydra） — Cascade, cascade, cascade, cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it wit
  3. Thryx, the Sudden Storm（{3}{U}{U}｜Legendary Creature — Elemental Giant） — Flash (You may cast this spell any time you could cast an instant.) Flying Spells you cast with mana value 5 or greater cost {1} less to cast and can't be countered.
  4. Annoyed Altisaur（{5}{G}{G}｜Creature — Dinosaur） — Reach, trample Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying 
  5. Monstrous Vortex（{3}{G}｜Enchantment） — Whenever you cast a creature spell with power 5 or greater, discover X, where X is that spell's mana value. (Exile cards from the top of your library until you exile a no
  6. Brinelin, the Moon Kraken（{6}{U}{U}｜Legendary Creature — Kraken） — When Brinelin enters and whenever you cast a spell with mana value 6 or greater, you may return target nonland permanent to its owner's hand. Partner (You can have two co
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Yavimaya Coast（｜Land） — {T}: Add {C}. {T}: Add {G} or {U}. This land deals 1 damage to you.
  - Hullbreaker Horror（{5}{U}{U}｜Creature — Kraken Horror） — Flash This spell can't be countered. Whenever you cast a spell, choose up to one — • Return target spell you don't control to its 


## Gisa, the Hellraiser ｜ 狱尸唤师基沙
- 颜色 B ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Warlock
- 流行度：EDHREC 全时段第 475 位，约 6083 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.47 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.38
- 社区标签：僵尸、衍生物、Crime、牺牲流、坟场复活、控制
- 完整牌面：Ward—{2}, Pay 2 life.
Skeletons and Zombies you control get +1/+1 and have menace.
Whenever you commit a crime, create two tapped 2/2 blue and black Zombie Rogue creature tokens. This ability triggers only once each turn. (Targeting opponents, anything they control, and/or cards in their graveyards is a crime.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Death Baron（{1}{B}{B}｜Creature — Zombie Wizard） — Skeletons you control and other Zombies you control get +1/+1 and have deathtouch. (Any amount of damage they deal to a creature is enough to destroy it.)
  2. Cemetery Reaper（{1}{B}{B}｜Creature — Zombie） — Other Zombie creatures you control get +1/+1. {2}{B}, {T}: Exile target creature card from a graveyard. Create a 2/2 black Zombie creature token.
  3. Undead Augur（{B}{B}｜Creature — Zombie Wizard） — Whenever this creature or another Zombie you control dies, you draw a card and lose 1 life.
  4. Withered Wretch（{B}{B}｜Creature — Zombie Cleric） — {1}: Exile target card from a graveyard.
  5. Endless Ranks of the Dead（{2}{B}{B}｜Enchantment） — At the beginning of your upkeep, create X 2/2 black Zombie creature tokens, where X is half the number of Zombies you control, rounded down.
  6. Champion of the Perished（{B}｜Creature — Zombie） — Whenever another Zombie you control enters, put a +1/+1 counter on this creature.
- **出场率最高的牌**（大多数牌组都会放）
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Feed the Swarm（{1}{B}｜Sorcery） — Destroy target creature or enchantment an opponent controls. You lose life equal to that permanent's mana value.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost thi


## Felix Five-Boots ｜ 五靴菲利斯
- 颜色 UBG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Ooze Rogue
- 流行度：EDHREC 全时段第 475 位，约 6083 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.21 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：快攻、忍术、换手牌、＋1/＋1 指示物、偷取、装备
- 完整牌面：Menace, ward {2}
If a creature you control dealing combat damage to a player causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Trygon Predator（{1}{G}{U}｜Creature — Beast） — Flying Whenever this creature deals combat damage to a player, you may destroy target artifact or enchantment that player controls.
  2. Ohran Frostfang（{3}{G}{G}｜Snow Creature — Snake） — Attacking creatures you control have deathtouch. Whenever a creature you control deals combat damage to a player, draw a card.
  3. Bident of Thassa（{2}{U}{U}｜Legendary Enchantment Artifact） — Whenever a creature you control deals combat damage to a player, you may draw a card. {1}{U}, {T}: Creatures your opponents control attack this turn if able.
  4. Toski, Bearer of Secrets（{3}{G}｜Legendary Creature — Squirrel） — This spell can't be countered. Indestructible Toski attacks each combat if able. Whenever a creature you control deals combat damage to a player, draw a card.
  5. Glissa Sunslayer（{1}{B}{G}｜Legendary Creature — Phyrexian Zombie Elf） — First strike, deathtouch Whenever Glissa Sunslayer deals combat damage to a player, choose one — • You draw a card and lose 1 life. • Destroy target enchantment. • Remove
  6. Drana, Liberator of Malakir（{1}{B}{B}｜Legendary Creature — Vampire Ally） — Flying, first strike Whenever Drana deals combat damage to a player, put a +1/+1 counter on each attacking creature you control.
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Opulent Palace（｜Land） — This land enters tapped. {T}: Add {B}, {G}, or {U}.
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Drowned Catacomb（｜Land） — This land enters tapped unless you control an Island or a Swamp. {T}: Add {U} or {B}.


## Hapatra, Vizier of Poisons ｜ 司毒维齐尔哈芭恰
- 颜色 BG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Cleric
- 流行度：EDHREC 全时段第 477 位，约 6072 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.5 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.32
- 社区标签：－1/－1 指示物、衍生物、组合技、毒侵、牺牲流、蛇
- 完整牌面：Whenever Hapatra deals combat damage to a player, you may put a -1/-1 counter on target creature.
Whenever you put one or more -1/-1 counters on a creature, create a 1/1 green Snake creature token with deathtouch.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Nest of Scarabs（{2}{B}｜Enchantment） — Whenever you put one or more -1/-1 counters on a creature, create that many 1/1 black Insect creature tokens.
  2. Blowfly Infestation（{2}{B}｜Enchantment） — Whenever a creature dies, if it had a -1/-1 counter on it, put a -1/-1 counter on target creature.
  3. Obelisk Spider（{1}{B}{G}｜Creature — Spider） — Reach Whenever this creature deals combat damage to a creature, put a -1/-1 counter on that creature. Whenever you put one or more -1/-1 counters on a creature, each oppo
  4. Black Sun's Zenith（{X}{B}{B}｜Sorcery） — Put X -1/-1 counters on each creature. Shuffle Black Sun's Zenith into its owner's library.
  5. Devoted Druid（{1}{G}｜Creature — Elf Druid） — {T}: Add {G}. Put a -1/-1 counter on this creature: Untap this creature.
  6. Necroskitter（{1}{B}{B}｜Creature — Elemental） — Wither (This deals damage to creatures in the form of -1/-1 counters.) Whenever a creature an opponent controls with a -1/-1 counter on it dies, you may return that card 
- **出场率最高的牌**（大多数牌组都会放）
  - Contagion Clasp（{2}｜Artifact） — When this artifact enters, put a -1/-1 counter on target creature. {4}, {T}: Proliferate. (Choose any number of permanents and/or 
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  - Channeler Initiate（{1}{G}｜Creature — Human Druid） — When this creature enters, put three -1/-1 counters on target creature you control. {T}, Remove a -1/-1 counter from this creature
  - Generous Patron（{2}{G}｜Creature — Elf Advisor） — When this creature enters, support 2. (Put a +1/+1 counter on each of up to two other target creatures.) Whenever you put one or m


## Magnus the Red ｜ 红魔马格努斯
- 颜色 UR ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Demon Primarch
- 流行度：EDHREC 全时段第 479 位，约 6052 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.5 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $10.01
- 社区标签：法术连发、衍生物、X 咒语、风暴、烧血、组合技
- 完整牌面：Flying
Unearthly Power — Instant and sorcery spells you cast cost {1} less to cast for each creature token you control.
Blade of Magnus — Whenever Magnus the Red deals combat damage to a player, create a 3/3 red Spawn creature token.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Young Pyromancer（{1}{R}｜Creature — Human Shaman） — Whenever you cast an instant or sorcery spell, create a 1/1 red Elemental creature token.
  2. Third Path Iconoclast（{U}{R}｜Creature — Human Monk） — Whenever you cast a noncreature spell, create a 1/1 colorless Soldier artifact creature token.
  3. Song of Totentanz（{X}{R}｜Sorcery） — Create X 1/1 black Rat creature tokens with "This token can't block." Creatures you control gain haste until end of turn.
  4. Empty the Warrens（{3}{R}｜Sorcery） — Create two 1/1 red Goblin creature tokens. Storm (When you cast this spell, copy it for each spell cast before it this turn.)
  5. Finale of Revelation（{X}{U}{U}｜Sorcery） — Draw X cards. If X is 10 or more, instead shuffle your graveyard into your library, draw X cards, untap up to five lands, and you have no maximum hand size for the rest o
  6. Talrand, Sky Summoner（{2}{U}{U}｜Legendary Creature — Merfolk Wizard） — Whenever you cast an instant or sorcery spell, create a 2/2 blue Drake creature token with flying.
- **出场率最高的牌**（大多数牌组都会放）
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Storm-Kiln Artist（{3}{R}｜Creature — Dwarf Shaman） — This creature gets +1/+0 for each artifact you control. Magecraft — Whenever you cast or copy an instant or sorcery spell, create 
  - Talisman of Creativity（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {R}. This artifact deals 1 damage to you.
  - Archmage Emeritus（{2}{U}{U}｜Creature — Human Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, draw a card.


## Black Panther, Wakandan King ｜ 瓦坎达之王黑豹
- 颜色 WG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Noble Hero
- 流行度：EDHREC 全时段第 481 位，约 6028 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.6 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.29
- 社区标签：＋1/＋1 指示物、衍生物、地牌核心、生命增益、地落、加速
- 完整牌面：First strike
Survey the Realm — Whenever Black Panther or another creature you control enters, put a +1/+1 counter on target land you control.
Mine Vibranium — {3}: Move all +1/+1 counters from target land you control onto target creature. If one or more +1/+1 counters are moved this way, you gain that much life and draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Karn's Bastion（｜Land） — {T}: Add {C}. {4}, {T}: Proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
  2. Secure the Wastes（{X}{W}｜Instant） — Create X 1/1 white Warrior creature tokens.
  3. Primal Vigor（{4}{G}｜Enchantment） — If one or more tokens would be created, twice that many of those tokens are created instead. If one or more +1/+1 counters would be put on a creature, twice that many +1/
  4. Kami of Whispered Hopes（{2}{G}｜Creature — Spirit） — If one or more +1/+1 counters would be put on a permanent you control, that many plus one +1/+1 counters are put on that permanent instead. {T}: Add X mana of any one col
  5. Ashaya, Soul of the Wild（{3}{G}{G}｜Legendary Creature — Elemental） — Ashaya's power and toughness are each equal to the number of lands you control. Nontoken creatures you control are Forest lands in addition to their other types. (They're
  6. The Ozolith（{1}｜Legendary Artifact） — Whenever a creature you control leaves the battlefield, if it had counters on it, put those counters on The Ozolith. At the beginning of combat on your turn, if The Ozoli
- **出场率最高的牌**（大多数牌组都会放）
  - Heroic Intervention（{1}{G}｜Instant） — Permanents you control gain hexproof and indestructible until end of turn.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Kutzil, Malamet Exemplar（{1}{G}{W}｜Legendary Creature — Cat Warrior） — Your opponents can't cast spells during your turn. Whenever one or more creatures you control each with power greater than its bas
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.


## Amalia Benavides Aguirre ｜ 阿玛利亚贝纳维德阿格雷
- 颜色 WB ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Vampire Scout
- 流行度：EDHREC 全时段第 482 位，约 6023 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.31 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.42
- 社区标签：生命增益、坟场复活、牺牲流、＋1/＋1 指示物、吸血鬼、吸取生命
- 完整牌面：Ward—Pay 3 life.
Whenever you gain life, Amalia Benavides Aguirre explores. Then destroy all other creatures if its power is exactly 20. (To have this creature explore, reveal the top card of your library. Put that card into your hand if it's a land. Otherwise, put a +1/+1 counter on this creature, then put the card back or put it into your graveyard.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Soul Warden（{W}｜Creature — Human Cleric） — Whenever another creature enters, you gain 1 life.
  2. Soul's Attendant（{W}｜Creature — Human Cleric） — Whenever another creature enters, you may gain 1 life.
  3. Daxos, Blessed by the Sun（{W}{W}｜Legendary Enchantment Creature — Demigod） — Daxos's toughness is equal to your devotion to white. (Each {W} in the mana costs of permanents you control counts toward your devotion to white.) Whenever another creatu
  4. Lunarch Veteran（｜） — 
  5. Authority of the Consuls（{W}｜Enchantment） — Creatures your opponents control enter tapped. Whenever a creature an opponent controls enters, you gain 1 life.
  6. Case of the Uneaten Feast（{W}｜Enchantment — Case） — Whenever a creature you control enters, you gain 1 life. To solve — You've gained 5 or more life this turn. (If unsolved, solve at the beginning of your end step.) Solved
- **出场率最高的牌**（大多数牌组都会放）
  - Elas il-Kor, Sadistic Pilgrim（{W}{B}｜Legendary Creature — Phyrexian Kor Cleric） — Deathtouch Whenever another creature you control enters, you gain 1 life. Whenever another creature you control dies, each opponen
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.


## Arixmethes, Slumbering Isle ｜ 静眠岛屿阿力马昔斯
- 颜色 UG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Kraken
- 流行度：EDHREC 全时段第 483 位，约 6006 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.32 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.69
- 社区标签：海洋生物、加速、地牌核心、爆费、组合技、控制
- 完整牌面：Arixmethes enters tapped with five slumber counters on it.
As long as Arixmethes has a slumber counter on it, it's a land. (It's not a creature.)
Whenever you cast a spell, you may remove a slumber counter from Arixmethes.
{T}: Add {G}{U}.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Whelming Wave（{2}{U}{U}｜Sorcery） — Return all creatures to their owners' hands except for Krakens, Leviathans, Octopuses, and Serpents.
  2. Slinn Voda, the Rising Deep（{6}{U}{U}｜Legendary Creature — Leviathan） — Kicker {1}{U} (You may pay an additional {1}{U} as you cast this spell.) When Slinn Voda enters, if it was kicked, return all creatures to their owners' hands except for 
  3. Stormsurge Kraken（{3}{U}{U}｜Creature — Kraken） — Hexproof Lieutenant — As long as you control your commander, this creature gets +2/+2 and has "Whenever this creature becomes blocked, you may draw two cards."
  4. Scourge of Fleets（{5}{U}{U}｜Creature — Kraken） — When this creature enters, return each creature your opponents control with toughness X or less to its owner's hand, where X is the number of Islands you control.
  5. Kiora's Follower（{G}{U}｜Creature — Merfolk） — {T}: Untap another target permanent.
  6. Tromokratis（{5}{U}{U}｜Legendary Creature — Kraken） — Tromokratis has hexproof unless it's attacking or blocking. Tromokratis can't be blocked unless all creatures defending player controls block it. (If any creature that pl
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Growth Spiral（{G}{U}｜Instant） — Draw a card. You may put a land card from your hand onto the battlefield.
  - Simic Growth Chamber（｜Land） — This land enters tapped. When this land enters, return a land you control to its owner's hand. {T}: Add {G}{U}.
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 


## Arthur, Marigold Knight ｜ 金盏花骑士亚瑟
- 颜色 WUR ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Mouse Knight
- 流行度：EDHREC 全时段第 484 位，约 6005 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.69 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：闪现回场、快攻、进场触发、额外战斗、攻击触发、骑士
- 完整牌面：Haste
Whenever Arthur and at least one other creature attack, look at the top six cards of your library. You may put a creature card from among them onto the battlefield tapped and attacking. Put the rest on the bottom of your library in a random order. Return that creature to its owner's hand at end of combat.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Brago, King Eternal（{2}{W}{U}｜Legendary Creature — Spirit Noble） — Flying Whenever Brago deals combat damage to a player, exile any number of target nonland permanents you control, then return those cards to the battlefield under their o
  2. Dour Port-Mage（{1}{U}｜Creature — Frog Wizard） — Whenever one or more other creatures you control leave the battlefield without dying, draw a card. {1}{U}, {T}: Return another target creature you control to its owner's 
  3. Angel of the Ruins（{5}{W}{W}｜Artifact Creature — Angel） — Flying When this creature enters, exile up to two target artifacts and/or enchantments. Plainscycling {2} ({2}, Discard this card: Search your library for a Plains card, 
  4. Ephemerate（{W}｜Instant） — Exile target creature you control, then return it to the battlefield under its owner's control. Rebound (If you cast this spell from your hand, exile it as it resolves. A
  5. Éowyn, Fearless Knight（{2}{R}{W}｜Legendary Creature — Human Knight） — Haste When Éowyn enters, exile target creature an opponent controls with greater power. Legendary creatures you control gain protection from each of that creature's color
  6. Sun Titan（{4}{W}{W}｜Creature — Giant） — Vigilance Whenever this creature enters or attacks, you may return target permanent card with mana value 3 or less from your graveyard to the battlefield.
- **出场率最高的牌**（大多数牌组都会放）
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Mystic Monastery（｜Land） — This land enters tapped. {T}: Add {U}, {R}, or {W}.
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.


## Progenitus ｜ 祖神兽
- 颜色 WUBRG ｜ 法术力值 10.0 ｜ 类型 Legendary Creature — Hydra Avatar
- 流行度：EDHREC 全时段第 485 位，约 5993 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.38 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.08
- 社区标签：多头龙、＋1/＋1 指示物、加速、主将单挑、地牌核心、爆费
- 完整牌面：Protection from everything
If Progenitus would be put into a graveyard from anywhere, reveal Progenitus and shuffle it into its owner's library instead.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mirari's Wake（{3}{G}{W}｜Enchantment） — Creatures you control get +1/+1. Whenever you tap a land for mana, add one mana of any type that land produced.
  2. Finest Hour（{2}{G}{W}{U}｜Enchantment） — Exalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.) Whenever a creature you control attacks alone, if it's the first comb
  3. Fist of Suns（{3}｜Artifact） — You may pay {W}{U}{B}{R}{G} rather than pay the mana cost for spells you cast.
  4. Rafiq of the Many（{1}{G}{W}{U}｜Legendary Creature — Human Knight） — Exalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.) Whenever a creature you control attacks alone, it gains double strike
  5. Jodah, Archmage Eternal（{1}{U}{R}{W}｜Legendary Creature — Human Wizard） — Flying You may pay {W}{U}{B}{R}{G} rather than pay the mana cost for spells you cast.
  6. Leyline of Mutation（{2}{G}{G}｜Enchantment） — If this card is in your opening hand, you may begin the game with it on the battlefield. You may pay {W}{U}{B}{R}{G} rather than pay the mana cost for spells you cast.
- **出场率最高的牌**（大多数牌组都会放）
  - The World Tree（｜Land） — This land enters tapped. {T}: Add {G}. As long as you control six or more lands, lands you control have "{T}: Add one mana of any 
  - Rhythm of the Wild（{1}{R}{G}｜Enchantment） — Creature spells you control can't be countered. Nontoken creatures you control have riot. (They enter with your choice of a +1/+1 
  - Timeless Lotus（{5}｜Legendary Artifact） — Timeless Lotus enters tapped. {T}: Add {W}{U}{B}{R}{G}.
  - Faeburrow Elder（{1}{G}{W}｜Creature — Treefolk Druid） — Vigilance This creature gets +1/+1 for each color among permanents you control. {T}: For each color among permanents you control, 


## Massacre Girl, Known Killer ｜ 知名凶手杀戮女郎
- 颜色 B ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Assassin
- 流行度：EDHREC 全时段第 486 位，约 5993 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.54 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.58
- 社区标签：－1/－1 指示物、控制、牺牲流、毒侵、坟场复活、衍生物
- 完整牌面：Menace
Creatures you control have wither. (They deal damage to creatures in the form of -1/-1 counters.)
Whenever a creature an opponent controls dies, if its toughness was less than 1, draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Massacre Girl（{3}{B}{B}｜Legendary Creature — Human Assassin） — Menace When Massacre Girl enters, each other creature gets -1/-1 until end of turn. Whenever a creature dies this turn, each creature other than Massacre Girl gets -1/-1 
  2. Nest of Scarabs（{2}{B}｜Enchantment） — Whenever you put one or more -1/-1 counters on a creature, create that many 1/1 black Insect creature tokens.
  3. Blowfly Infestation（{2}{B}｜Enchantment） — Whenever a creature dies, if it had a -1/-1 counter on it, put a -1/-1 counter on target creature.
  4. Necroskitter（{1}{B}{B}｜Creature — Elemental） — Wither (This deals damage to creatures in the form of -1/-1 counters.) Whenever a creature an opponent controls with a -1/-1 counter on it dies, you may return that card 
  5. Black Sun's Zenith（{X}{B}{B}｜Sorcery） — Put X -1/-1 counters on each creature. Shuffle Black Sun's Zenith into its owner's library.
  6. Massacre Wurm（{3}{B}{B}{B}｜Creature — Phyrexian Wurm） — When this creature enters, creatures your opponents control get -2/-2 until end of turn. Whenever a creature an opponent controls dies, that player loses 2 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Tragic Slip（{B}｜Instant） — Target creature gets -1/-1 until end of turn. Morbid — That creature gets -13/-13 until end of turn instead if a creature died thi
  - Defile（{B}｜Instant） — Target creature gets -1/-1 until end of turn for each Swamp you control.
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Toxic Deluge（{2}{B}｜Sorcery） — As an additional cost to cast this spell, pay X life. All creatures get -X/-X until end of turn.


## Camellia, the Seedmiser ｜ 守种奴卡茉拉
- 颜色 BG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Squirrel Warlock
- 流行度：EDHREC 全时段第 487 位，约 5991 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.37 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.66
- 社区标签：衍生物、松鼠、食品、牺牲、＋1/＋1 指示物、牺牲流
- 完整牌面：Menace
Other Squirrels you control have menace.
Whenever you sacrifice one or more Foods, create a 1/1 green Squirrel creature token.
{2}, Forage: Put a +1/+1 counter on each other Squirrel you control. (To forage, exile three cards from your graveyard or sacrifice a Food.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Thornvault Forager（{1}{G}｜Creature — Squirrel Ranger） — {T}: Add {G}. {T}, Forage: Add two mana in any combination of colors. (To forage, exile three cards from your graveyard or sacrifice a Food.) {3}{G}, {T}: Search your lib
  2. Honored Dreyleader（{2}{G}｜Creature — Squirrel Warrior） — Trample When this creature enters, put a +1/+1 counter on it for each other Squirrel and/or Food you control. Whenever another Squirrel or Food you control enters, put a 
  3. Chatterfang, Squirrel General（{2}{G}｜Legendary Creature — Squirrel Warrior） — Forestwalk (This creature can't be blocked as long as defending player controls a Forest.) If one or more tokens would be created under your control, those tokens plus th
  4. Chitterspitter（{2}{G}｜Artifact） — At the beginning of your upkeep, you may sacrifice a token. If you do, put an acorn counter on this artifact. Squirrels you control get +1/+1 for each acorn counter on th
  5. Vinereap Mentor（{B}{G}｜Creature — Squirrel Druid） — When this creature enters or dies, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.")
  6. Valley Rotcaller（{1}{B}｜Creature — Squirrel Warlock） — Menace Whenever this creature attacks, each opponent loses X life and you gain X life, where X is the number of other Squirrels, Bats, Lizards, and Rats you control.
- **出场率最高的牌**（大多数牌组都会放）
  - Ravenous Squirrel（{B/G}｜Creature — Squirrel） — Whenever you sacrifice an artifact or creature, put a +1/+1 counter on this creature. {1}{B}{G}, Sacrifice an artifact or creature
  - Gilded Goose（{G}｜Creature — Bird） — Flying When this creature enters, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.") 
  - Peregrin Took（{2}{G}｜Legendary Creature — Halfling Citizen） — If one or more tokens would be created under your control, those tokens plus an additional Food token are created instead. (It's a
  - Hazel of the Rootbloom（{2}{B}{G}｜Legendary Creature — Squirrel Druid） — {T}, Pay 2 life, Tap X untapped tokens you control: Add X mana in any combination of colors. At the beginning of your end step, cr


## Davros, Dalek Creator ｜ 戴立克创造者戴沃斯
- 颜色 UBR ｜ 法术力值 4.0 ｜ 类型 Legendary Artifact Creature — Alien Scientist
- 流行度：EDHREC 全时段第 488 位，约 5982 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.76 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：神器、衍生物、Daleks、弃牌、烧血、龙之途径
- 完整牌面：Menace
At the beginning of your end step, create a 3/3 black Dalek artifact creature token with menace if an opponent lost 3 or more life this turn. Then each opponent who lost 3 or more life this turn faces a villainous choice — You draw a card, or that player discards a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Exterminate!（{2}{B}｜Sorcery） — Replicate—Tap an untapped Dalek you control. (When you cast this spell, copy it for each time you paid its replicate cost. You may choose new targets for the copies.) Des
  2. The Dalek Emperor（{5}{B}{R}｜Legendary Artifact Creature — Dalek） — Affinity for Daleks (This spell costs {1} less to cast for each Dalek you control.) Other Daleks you control have haste. At the beginning of combat on your turn, each opp
  3. Dalek Squadron（{2}{B}｜Artifact Creature — Dalek） — Menace Myriad (Whenever this creature attacks, for each opponent other than defending player, you may create a token copy that's tapped and attacking that player or a pla
  4. Dalek Drone（{3}{B}{B}｜Artifact Creature — Dalek） — Flying, menace Exterminate! — When this creature enters, destroy target creature an opponent controls. That player loses 3 life.
  5. Cult of Skaro（{1}{U}{B}{R}｜Legendary Artifact Creature — Dalek） — Whenever Cult of Skaro attacks, choose one at random — • Thay — Put a +1/+1 counter on each artifact creature you control. • Caan — Draw two cards. • Sec — Create a 3/3 b
  6. Cyberman Patrol（{2}｜Artifact Creature — Cyberman） — Artifact creatures you control have afflict 3. (Whenever a creature with afflict 3 becomes blocked, defending player loses 3 life.)
- **出场率最高的牌**（大多数牌组都会放）
  - Genesis of the Daleks（{4}{B}{B}｜Enchantment — Saga） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after IV.) I, II, III — Create a 3/3 black Dalek arti
  - Stormcarved Coast（｜Land） — This land enters tapped unless you control two or more other lands. {T}: Add {U} or {R}.
  - Crumbling Necropolis（｜Land） — This land enters tapped. {T}: Add {U}, {B}, or {R}.
  - Haunted Ridge（｜Land） — This land enters tapped unless you control two or more other lands. {T}: Add {B} or {R}.


## Averna, the Chaos Bloom ｜ 混沌之华阿韦纳
- 颜色 URG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elemental Shaman
- 流行度：EDHREC 全时段第 489 位，约 5972 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.32 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.34
- 社区标签：倾曳、地牌核心、地落、加速、混乱、风暴
- 完整牌面：As you cascade, you may put a land card from among the exiled cards onto the battlefield tapped. (Do this after the last card is exiled but before deciding whether to cast a nonland card.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Imoti, Celebrant of Bounty（{3}{G}{U}｜Legendary Creature — Snake Druid） — Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. 
  2. Aurora Phoenix（{4}{R}{R}｜Creature — Phoenix） — Flying Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana
  3. Bloodbraid Elf（{2}{R}{G}｜Creature — Elf Berserker） — Haste (This creature can attack and {T} as soon as it comes under your control.) Cascade (When you cast this spell, exile cards from the top of your library until you exi
  4. Maelstrom Wanderer（{5}{G}{U}{R}｜Legendary Creature — Elemental） — Creatures you control have haste. Cascade, cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You
  5. Apex Devastator（{8}{G}{G}｜Creature — Chimera Hydra） — Cascade, cascade, cascade, cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it wit
  6. Natural Reclamation（{4}{G}｜Instant） — Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. 
- **出场率最高的牌**（大多数牌组都会放）
  - Shardless Agent（{1}{G}{U}｜Artifact Creature — Human Rogue） — Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You ma
  - Etherium-Horn Sorcerer（{4}{U}{R}｜Artifact Creature — Minotaur Wizard Sorcerer） — {1}{U}{R}: Return this creature to its owner's hand. Cascade (When you cast this spell, exile cards from the top of your library u
  - Sakashima's Protege（{4}{U}{U}｜Creature — Shapeshifter） — Flash Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. 
  - Annoyed Altisaur（{5}{G}{G}｜Creature — Dinosaur） — Reach, trample Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that cos


## Rivaz of the Claw ｜ 龙爪利瓦兹
- 颜色 BR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Lizard Warlock
- 流行度：EDHREC 全时段第 490 位，约 5970 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.29 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.56
- 社区标签：龙、坟场复活、飞行、宝物、快攻、坟场
- 完整牌面：Menace
{T}: Add two mana in any combination of colors. Spend this mana only to cast Dragon creature spells.
Once during each of your turns, you may cast a Dragon creature spell from your graveyard.
Whenever you cast a Dragon creature spell from your graveyard, it gains "When this creature dies, exile it."
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Lathliss, Dragon Queen（{4}{R}{R}｜Legendary Creature — Dragon） — Flying Whenever another nontoken Dragon you control enters, create a 5/5 red Dragon creature token with flying. {1}{R}: Dragons you control get +1/+0 until end of turn.
  2. Bladewing the Risen（{3}{B}{B}{R}{R}｜Legendary Creature — Zombie Dragon） — Flying When Bladewing enters, you may return target Dragon permanent card from your graveyard to the battlefield. {B}{R}: Dragon creatures get +1/+1 until end of turn.
  3. Dragon Tempest（{1}{R}｜Enchantment） — Whenever a creature you control with flying enters, it gains haste until end of turn. Whenever a Dragon you control enters, it deals X damage to any target, where X is th
  4. Crux of Fate（{3}{B}{B}｜Sorcery） — Choose one — • Destroy all Dragon creatures. • Destroy all non-Dragon creatures.
  5. Dragonlord's Servant（{1}{R}｜Creature — Goblin Shaman） — Dragon spells you cast cost {1} less to cast.
  6. Dragonspeaker Shaman（{1}{R}{R}｜Creature — Human Barbarian Shaman） — Dragon spells you cast cost {2} less to cast.
- **出场率最高的牌**（大多数牌组都会放）
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Ganax, Astral Hunter（{4}{R}｜Legendary Creature — Dragon） — Flying Whenever Ganax or another Dragon you control enters, create a Treasure token. (It's an artifact with "{T}, Sacrifice this t
  - Faithless Looting（{R}｜Sorcery） — Draw two cards, then discard two cards. Flashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then 
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.


## Tasha, the Witch Queen ｜ 巫后塔莎
- 颜色 UB ｜ 法术力值 5.0 ｜ 类型 Legendary Planeswalker — Tasha
- 流行度：EDHREC 全时段第 491 位，约 5966 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.49 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.87
- 社区标签：偷取、磨牌、放逐、控制、法术连发、衍生物
- 完整牌面：Whenever you cast a spell you don't own, create a 3/3 black Demon creature token.
+1: Draw a card. For each opponent, exile up to one target instant or sorcery card from that player's graveyard and put a page counter on it.
−3: You may cast a spell from among cards in exile with page counters on them without paying its mana cost.
Tasha, the Witch Queen can be your commander.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Thief of Sanity（{1}{U}{B}｜Creature — Specter） — Flying Whenever this creature deals combat damage to a player, look at the top three cards of that player's library, exile one of them face down, then put the rest into t
  2. Siphon Insight（{U}{B}｜Instant） — Look at the top two cards of target opponent's library. Exile one of them face down and put the other on the bottom of that library. You may play the exiled card for as l
  3. Cunning Rhetoric（{2}{B}｜Enchantment） — Whenever an opponent attacks you and/or one or more planeswalkers you control, exile the top card of that player's library. You may play that card for as long as it remai
  4. Gonti, Lord of Luxury（{2}{B}{B}｜Legendary Creature — Aetherborn Rogue） — Deathtouch When Gonti enters, look at the top four cards of target opponent's library, exile one of them face down, then put the rest on the bottom of that library in a r
  5. Hostage Taker（{2}{U}{B}｜Creature — Human Pirate） — When this creature enters, exile another target creature or artifact until this creature leaves the battlefield. You may cast that card for as long as it remains exiled, 
  6. Memory Plunder（{U/B}{U/B}{U/B}{U/B}｜Instant） — You may cast target instant or sorcery card from an opponent's graveyard without paying its mana cost.
- **出场率最高的牌**（大多数牌组都会放）
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Dimir Signet（{2}｜Artifact） — {1}, {T}: Add {U}{B}.
  - Drowned Catacomb（｜Land） — This land enters tapped unless you control an Island or a Swamp. {T}: Add {U} or {B}.
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.


## Karlov of the Ghost Council ｜ 鬼影议会的卡洛夫
- 颜色 WB ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Spirit Advisor
- 流行度：EDHREC 全时段第 492 位，约 5962 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.4 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $14.28
- 社区标签：生命增益、＋1/＋1 指示物、主将单挑、组合技、吸取生命、控制
- 完整牌面：Whenever you gain life, put two +1/+1 counters on Karlov.
{W}{B}, Remove six +1/+1 counters from Karlov: Exile target creature.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Soul Warden（{W}｜Creature — Human Cleric） — Whenever another creature enters, you gain 1 life.
  2. Soul's Attendant（{W}｜Creature — Human Cleric） — Whenever another creature enters, you may gain 1 life.
  3. Authority of the Consuls（{W}｜Enchantment） — Creatures your opponents control enter tapped. Whenever a creature an opponent controls enters, you gain 1 life.
  4. Kambal, Consul of Allocation（{1}{W}{B}｜Legendary Creature — Human Advisor） — Whenever an opponent casts a noncreature spell, that player loses 2 life and you gain 2 life.
  5. Auriok Champion（{W}{W}｜Creature — Human Cleric） — Protection from black and from red Whenever another creature enters, you may gain 1 life.
  6. Suture Priest（{1}{W}｜Creature — Phyrexian Cleric） — Whenever another creature you control enters, you may gain 1 life. Whenever a creature an opponent controls enters, you may have that player lose 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Vito, Thorn of the Dusk Rose（{2}{B}｜Legendary Creature — Vampire Cleric） — Whenever you gain life, target opponent loses that much life. {3}{B}{B}: Creatures you control gain lifelink until end of turn.


## Baral, Chief of Compliance ｜ 监察长巴罗
- 颜色 U ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Wizard
- 流行度：EDHREC 全时段第 494 位，约 5953 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 1.06 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $4.66
- 社区标签：反击咒语、控制、法术连发、组合技、抽牌、法师
- 完整牌面：Instant and sorcery spells you cast cost {1} less to cast.
Whenever a spell or ability you control counters a spell, you may draw a card. If you do, discard a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Rewind（{2}{U}{U}｜Instant） — Counter target spell. Untap up to four lands.
  2. Unwind（{2}{U}｜Instant） — Counter target noncreature spell. Untap up to three lands.
  3. Disallow（{1}{U}{U}｜Instant） — Counter target spell, activated ability, or triggered ability. (Mana abilities can't be targeted.)
  4. Mana Leak（{1}{U}｜Instant） — Counter target spell unless its controller pays {3}.
  5. Talrand, Sky Summoner（{2}{U}{U}｜Legendary Creature — Merfolk Wizard） — Whenever you cast an instant or sorcery spell, create a 2/2 blue Drake creature token with flying.
  6. Guile（{3}{U}{U}{U}｜Creature — Elemental Incarnation） — This creature can't be blocked except by three or more creatures. If a spell or ability you control would counter a spell, instead exile that spell and you may play that 
- **出场率最高的牌**（大多数牌组都会放）
  - Sapphire Medallion（{2}｜Artifact） — Blue spells you cast cost {1} less to cast.
  - Mystic Sanctuary（｜Land — Island） — ({T}: Add {U}.) This land enters tapped unless you control three or more other Islands. When this land enters untapped, you may pu
  - Archmage Emeritus（{2}{U}{U}｜Creature — Human Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, draw a card.
  - An Offer You Can't Refuse（{U}｜Instant） — Counter target noncreature spell. Its controller creates two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: 


## Hamza, Guardian of Arashin ｜ 阿拉辛守护者哈姆札
- 颜色 WG ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Elephant Warrior
- 流行度：EDHREC 全时段第 495 位，约 5948 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.29 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.32
- 社区标签：＋1/＋1 指示物、快攻、衍生物、Elephants、加速、组合技
- 完整牌面：This spell costs {1} less to cast for each creature you control with a +1/+1 counter on it.
Creature spells you cast cost {1} less to cast for each creature you control with a +1/+1 counter on it.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Inspiring Call（{2}{G}｜Instant） — Draw a card for each creature you control with a +1/+1 counter on it. Those creatures gain indestructible until end of turn. (Damage and effects that say "destroy" don't 
  2. Armorcraft Judge（{3}{G}｜Creature — Elf Artificer） — When this creature enters, draw a card for each creature you control with a +1/+1 counter on it.
  3. Rishkar, Peema Renegade（{2}{G}｜Legendary Creature — Elf Druid） — When Rishkar enters, put a +1/+1 counter on each of up to two target creatures. Each creature you control with a counter on it has "{T}: Add {G}."
  4. Mikaeus, the Lunarch（{X}{W}｜Legendary Creature — Human Cleric） — Mikaeus enters with X +1/+1 counters on it. {T}: Put a +1/+1 counter on Mikaeus. {T}, Remove a +1/+1 counter from Mikaeus: Put a +1/+1 counter on each other creature you 
  5. Good-Fortune Unicorn（{1}{G}{W}｜Creature — Unicorn） — Whenever another creature you control enters, put a +1/+1 counter on that creature.
  6. Abzan Falconer（{2}{W}｜Creature — Human Soldier） — Outlast {W} ({W}, {T}: Put a +1/+1 counter on this creature. Outlast only as a sorcery.) Each creature you control with a +1/+1 counter on it has flying.
- **出场率最高的牌**（大多数牌组都会放）
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Forgotten Ancient（{3}{G}｜Creature — Elemental） — Whenever a player casts a spell, you may put a +1/+1 counter on this creature. At the beginning of your upkeep, you may move any n
  - Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  - Kutzil, Malamet Exemplar（{1}{G}{W}｜Legendary Creature — Cat Warrior） — Your opponents can't cast spells during your turn. Whenever one or more creatures you control each with power greater than its bas


## Bre of Clan Stoutarm ｜ 勇臂族的碧莉
- 颜色 WR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Giant Warrior
- 流行度：EDHREC 全时段第 496 位，约 5943 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.27
- 社区标签：生命增益、巨人、快攻、＋1/＋1 指示物、飞行、放逐
- 完整牌面：{1}{W}, {T}: Another target creature you control gains flying and lifelink until end of turn.
At the beginning of your end step, if you gained life this turn, exile cards from the top of your library until you exile a nonland card. You may cast that card without paying its mana cost if the spell's mana value is less than or equal to the amount of life you gained this turn. Otherwise, put it into your hand.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. The Wind Crystal（{2}{W}{W}｜Legendary Artifact） — White spells you cast cost {1} less to cast. If you would gain life, you gain twice that much life instead. {4}{W}{W}, {T}: Creatures you control gain flying and lifelink
  2. Exemplar of Light（{2}{W}{W}｜Creature — Angel） — Flying Whenever you gain life, put a +1/+1 counter on this creature. Whenever you put one or more +1/+1 counters on this creature, draw a card. This ability triggers only
  3. Haliya, Guided by Light（{2}{W}｜Legendary Creature — Human Soldier） — Whenever Haliya or another creature or artifact you control enters, you gain 1 life. At the beginning of your end step, draw a card if you've gained 3 or more life this t
  4. Soul Warden（{W}｜Creature — Human Cleric） — Whenever another creature enters, you gain 1 life.
  5. Rhox Faithmender（{3}{W}｜Creature — Rhino Monk） — Lifelink (Damage dealt by this creature also causes you to gain that much life.) If you would gain life, you gain twice that much life instead.
  6. Cleric Class（{W}｜Enchantment — Class） — (Gain the next level as a sorcery to add its ability.) If you would gain life, you gain that much life plus 1 instead. {3}{W}: Level 2 Whenever you gain life, put a +1/+1
- **出场率最高的牌**（大多数牌组都会放）
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Battlefield Forge（｜Land） — {T}: Add {C}. {T}: Add {R} or {W}. This land deals 1 damage to you.
  - Talisman of Conviction（{2}｜Artifact） — {T}: Add {C}. {T}: Add {R} or {W}. This artifact deals 1 damage to you.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t


## Jinnie Fay, Jetmir's Second ｜ 杰米尔副手金妮斐
- 颜色 WRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elf Druid
- 流行度：EDHREC 全时段第 497 位，约 5934 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.22 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.75
- 社区标签：衍生物、猫、快攻、宝物、狗、＋1/＋1 指示物
- 完整牌面：If you would create one or more tokens, you may instead create that many 2/2 green Cat creature tokens with haste or that many 3/1 green Dog creature tokens with vigilance.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Artifact Mutation（{R}{G}｜Instant） — Destroy target artifact. It can't be regenerated. Create X 1/1 green Saproling creature tokens, where X is that artifact's mana value.
  2. Jetmir, Nexus of Revels（{1}{R}{G}{W}｜Legendary Creature — Cat Demon） — Creatures you control get +1/+0 and have vigilance as long as you control three or more creatures. Creatures you control also get +1/+0 and have trample as long as you co
  3. Aura Mutation（{G}{W}｜Instant） — Destroy target enchantment. Create X 1/1 green Saproling creature tokens, where X is that enchantment's mana value.
  4. Gala Greeters（{1}{G}｜Creature — Elf Druid） — Alliance — Whenever another creature you control enters, choose one that hasn't been chosen this turn — • Put a +1/+1 counter on this creature. • Create a tapped Treasure
  5. Grand Crescendo（{X}{W}{W}｜Instant） — Create X 1/1 green and white Citizen creature tokens. Creatures you control gain indestructible until end of turn.
  6. Rabble Rousing（{4}{W}｜Enchantment） — Hideaway 5 (When this enchantment enters, look at the top five cards of your library, exile one face down, then put the rest on the bottom in a random order.) Whenever yo
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Jetmir's Garden（｜Land — Mountain Forest Plains） — ({T}: Add {R}, {G}, or {W}.) This land enters tapped. Cycling {3} ({3}, Discard this card: Draw a card.)
  - Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.


## Ashling, Rekindled // Ashling, Rimebound ｜ 复炎灰儿
- 颜色 UR ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Elemental Sorcerer // Legendary Creature — Elemental Wizard
- 流行度：EDHREC 全时段第 498 位，约 5927 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.62
- 社区标签：法术连发、加速、爆费、烧血、倾曳、复制
- 完整牌面：Whenever this creature enters or transforms into Ashling, Rekindled, you may discard a card. If you do, draw a card.
At the beginning of your first main phase, you may pay {U}. If you do, transform Ashling.
//
Whenever this creature transforms into Ashling, Rimebound and at the beginning of your first main phase, add two mana of any one color. Spend this mana only to cast spells with mana value 4 or greater.
At the beginning of your first main phase, you may pay {R}. If you do, transform Ashling.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Hedron Archive（{4}｜Artifact） — {T}: Add {C}{C}. {2}, {T}, Sacrifice this artifact: Draw two cards.
  2. Thran Dynamo（{4}｜Artifact） — {T}: Add {C}{C}{C}.
  3. Sunbird's Invocation（{5}{R}｜Enchantment） — Whenever you cast a spell from your hand, reveal the top X cards of your library, where X is that spell's mana value. You may cast a spell with mana value X or less from 
  4. Tanufel Rimespeaker（{3}{U}｜Creature — Elemental Wizard） — Whenever you cast a spell with mana value 4 or greater, draw a card.
  5. Stonespeaker Crystal（{4}｜Artifact） — {T}: Add {C}{C}. {2}, {T}, Sacrifice this artifact: Exile any number of target players' graveyards. Draw a card.
  6. Aminatou's Augury（{6}{U}{U}｜Sorcery） — Exile the top eight cards of your library. You may put a land card from among them onto the battlefield. Until end of turn, for each nonland card type, you may cast a spe
- **出场率最高的牌**（大多数牌组都会放）
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Big Score（{3}{R}｜Instant） — As an additional cost to cast this spell, discard a card. Draw two cards and create two Treasure tokens. (They're artifacts with "
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.
  - Cascade Bluffs（｜Land） — {T}: Add {C}. {U/R}, {T}: Add {U}{U}, {U}{R}, or {R}{R}.


## Loot, Exuberant Explorer ｜ 兴奋探险家烂宝
- 颜色 G ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Beast Noble
- 流行度：EDHREC 全时段第 500 位，约 5916 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.59 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.15
- 社区标签：地落、地牌核心、加速、＋1/＋1 指示物、爆费、大生物
- 完整牌面：You may play an additional land on each of your turns.
{4}{G}{G}, {T}: Look at the top six cards of your library. You may reveal a creature card with mana value less than or equal to the number of lands you control from among them and put it onto the battlefield. Put the rest on the bottom in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Rampaging Baloths（{4}{G}{G}｜Creature — Beast） — Trample Landfall — Whenever a land you control enters, create a 4/4 green Beast creature token.
  2. Avenger of Zendikar（{5}{G}{G}｜Creature — Elemental） — When this creature enters, create a 0/1 green Plant creature token for each land you control. Landfall — Whenever a land you control enters, you may put a +1/+1 counter o
  3. Augur of Autumn（{1}{G}{G}｜Creature — Human Druid） — You may look at the top card of your library any time. You may play lands from the top of your library. Coven — As long as you control three or more creatures with differ
  4. Mossborn Hydra（{2}{G}｜Creature — Elemental Hydra） — Trample (This creature can deal excess combat damage to the player or planeswalker it's attacking.) This creature enters with a +1/+1 counter on it. Landfall — Whenever a
  5. Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create a token that's a copy of this creature i
  6. Cultivator Colossus（{4}{G}{G}{G}｜Creature — Plant Beast） — Trample Cultivator Colossus's power and toughness are each equal to the number of lands you control. When this creature enters, you may put a land card from your hand ont
- **出场率最高的牌**（大多数牌组都会放）
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess com
  - Heroic Intervention（{1}{G}｜Instant） — Permanents you control gain hexproof and indestructible until end of turn.


## Anim Pakal, Thousandth Moon ｜ 千月统帅阿妮帕卡
- 颜色 WR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Soldier
- 流行度：EDHREC 全时段第 501 位，约 5912 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.38 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.18
- 社区标签：衍生物、＋1/＋1 指示物、快攻、神器、烧血、Gnomes
- 完整牌面：Whenever you attack with one or more non-Gnome creatures, put a +1/+1 counter on Anim Pakal, then create X 1/1 colorless Gnome artifact creature tokens that are tapped and attacking, where X is the number of +1/+1 counters on Anim Pakal.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Rosie Cotton of South Lane（{2}{W}｜Legendary Creature — Halfling Peasant） — When Rosie Cotton enters, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.") Whenever you create a token, put a +1/+1 counter
  2. Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  3. Luminarch Aspirant（{1}{W}｜Creature — Human Cleric） — At the beginning of combat on your turn, put a +1/+1 counter on target creature you control.
  4. Losheel, Clockwork Scholar（{2}{W}｜Legendary Creature — Elephant Artificer） — Prevent all combat damage that would be dealt to attacking artifact creatures you control. Whenever one or more artifact creatures you control enter, draw a card. This ab
  5. Arabella, Abandoned Doll（{R}{W}｜Legendary Artifact Creature — Toy） — Whenever Arabella attacks, it deals X damage to each opponent and you gain X life, where X is the number of creatures you control with power 2 or less.
  6. Reckless Fireweaver（{1}{R}｜Creature — Human Artificer） — Whenever an artifact you control enters, this creature deals 1 damage to each opponent.
- **出场率最高的牌**（大多数牌组都会放）
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Warleader's Call（{1}{R}{W}｜Enchantment） — Creatures you control get +1/+1. Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}


## Mizzix of the Izmagnus ｜ 伊捷首法师米捷兹
- 颜色 UR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Goblin Wizard
- 流行度：EDHREC 全时段第 502 位，约 5886 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.77 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.10
- 社区标签：法术连发、X 咒语、风暴、组合技、烧血、咒语复制
- 完整牌面：Whenever you cast an instant or sorcery spell with mana value greater than the number of experience counters you have, you get an experience counter.
Instant and sorcery spells you cast cost {1} less to cast for each experience counter you have.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Tezzeret's Gambit（{3}{U/P}｜Sorcery） — ({U/P} can be paid with either {U} or 2 life.) Draw two cards, then proliferate. (Choose any number of permanents and/or players, then give each another counter of each k
  2. Flux Channeler（{2}{U}｜Creature — Human Wizard） — Whenever you cast a noncreature spell, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
  3. Comet Storm（{X}{R}{R}｜Instant） — Multikicker {1} (You may pay an additional {1} any number of times as you cast this spell.) Choose any target, then choose another target for each time this spell was kic
  4. Mystic Retrieval（{3}{U}｜Sorcery） — Return target instant or sorcery card from your graveyard to your hand. Flashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then exile it
  5. Reiterate（{1}{R}{R}｜Instant） — Buyback {3} (You may pay an additional {3} as you cast this spell. If you do, put this card into your hand as it resolves.) Copy target instant or sorcery spell. You may 
  6. Experimental Augury（{1}{U}｜Instant） — Look at the top three cards of your library. Put one of them into your hand and the rest on the bottom of your library in any order. Proliferate. (Choose any number of pe
- **出场率最高的牌**（大多数牌组都会放）
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Izzet Signet（{2}｜Artifact） — {1}, {T}: Add {U}{R}.
  - Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.
  - Storm-Kiln Artist（{3}{R}｜Creature — Dwarf Shaman） — This creature gets +1/+0 for each artifact you control. Magecraft — Whenever you cast or copy an instant or sorcery spell, create 


## Atarka, World Render ｜ 灭世龙王安塔卡
- 颜色 RG ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Dragon
- 流行度：EDHREC 全时段第 503 位，约 5884 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.42 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.47
- 社区标签：龙、飞行、快攻、加速、烧血、额外战斗
- 完整牌面：Flying, trample
Whenever a Dragon you control attacks, it gains double strike until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Dragon Tempest（{1}{R}｜Enchantment） — Whenever a creature you control with flying enters, it gains haste until end of turn. Whenever a Dragon you control enters, it deals X damage to any target, where X is th
  2. Dragonspeaker Shaman（{1}{R}{R}｜Creature — Human Barbarian Shaman） — Dragon spells you cast cost {2} less to cast.
  3. Dragonlord's Servant（{1}{R}｜Creature — Goblin Shaman） — Dragon spells you cast cost {1} less to cast.
  4. Haven of the Spirit Dragon（｜Land） — {T}: Add {C}. {T}: Add one mana of any color. Spend this mana only to cast a Dragon creature spell. {2}, {T}, Sacrifice this land: Return target Dragon creature card or U
  5. Savage Ventmaw（{4}{R}{G}｜Creature — Dragon） — Flying Whenever this creature attacks, add {R}{R}{R}{G}{G}{G}. Until end of turn, you don't lose this mana as steps and phases end.
  6. Dragon's Hoard（{3}｜Artifact） — Whenever a Dragon you control enters, put a gold counter on this artifact. {T}, Remove a gold counter from this artifact: Draw a card. {T}: Add one mana of any color.
- **出场率最高的牌**（大多数牌组都会放）
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Drakuseth, Maw of Flames（{4}{R}{R}{R}｜Legendary Creature — Dragon） — Flying Whenever Drakuseth attacks, Drakuseth deals 4 damage to any target and 3 damage to each of up to two other targets.
  - Scourge of Valkas（{2}{R}{R}{R}｜Creature — Dragon） — Flying Whenever this creature or another Dragon you control enters, it deals X damage to any target, where X is the number of Drag


## General Ferrous Rokiric ｜ 费罗洛基理将军
- 颜色 WR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Soldier
- 流行度：EDHREC 全时段第 505 位，约 5868 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.07 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.41
- 社区标签：衍生物、快攻、多色核心、神器、史迹、Golems
- 完整牌面：Hexproof from monocolored
Whenever you cast a multicolored spell, create a 4/4 red and white Golem artifact creature token.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Justice Strike（{R}{W}｜Instant） — Target creature deals damage to itself equal to its power.
  2. Balefire Liege（{2}{R/W}{R/W}{R/W}｜Creature — Spirit Horror） — Other red creatures you control get +1/+1. Other white creatures you control get +1/+1. Whenever you cast a red spell, this creature deals 3 damage to target player or pl
  3. Lightning Helix（{R}{W}｜Instant） — Lightning Helix deals 3 damage to any target and you gain 3 life.
  4. Legion's Initiative（{R}{W}｜Enchantment） — Red creatures you control get +1/+0. White creatures you control get +0/+1. {R}{W}, Exile this enchantment: Exile all creatures you control. At the beginning of the next 
  5. Neyali, Suns' Vanguard（{2}{R}{W}｜Legendary Creature — Human Rebel） — Attacking tokens you control have double strike. Whenever one or more tokens you control attack a player, exile the top card of your library. During any turn you attacked
  6. Rip Apart（{R}{W}｜Sorcery） — Choose one — • Rip Apart deals 3 damage to target creature or planeswalker. • Destroy target artifact or enchantment.
- **出场率最高的牌**（大多数牌组都会放）
  - Boros Charm（{R}{W}｜Instant） — Choose one — • Boros Charm deals 4 damage to target player or planeswalker. • Permanents you control gain indestructible until end
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Blade Historian（{R/W}{R/W}{R/W}{R/W}｜Creature — Human Cleric） — Attacking creatures you control have double strike.
  - Deflecting Palm（{R}{W}｜Instant） — The next time a source of your choice would deal damage to you this turn, prevent that damage. If damage is prevented this way, De


## Emmara, Soul of the Accord ｜ 协音之魂艾玛拉
- 颜色 WG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Elf Cleric
- 流行度：EDHREC 全时段第 508 位，约 5819 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.18 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.33
- 社区标签：衍生物、＋1/＋1 指示物、横置／重置、生命增益、增殖衍生物、快攻
- 完整牌面：Whenever Emmara becomes tapped, create a 1/1 white Soldier creature token with lifelink.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Holdout Settlement（｜Land） — {T}: Add {C}. ({C} represents colorless mana.) {T}, Tap an untapped creature you control: Add one mana of any color.
  2. March of the Multitudes（{X}{G}{W}{W}｜Instant） — Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.) Create X 1/1 white So
  3. Jaspera Sentinel（{G}｜Creature — Elf Rogue） — Reach {T}, Tap an untapped creature you control: Add one mana of any color.
  4. Harvest Season（{2}{G}｜Sorcery） — Search your library for up to X basic land cards, where X is the number of tapped creatures you control, put those cards onto the battlefield tapped, then shuffle.
  5. Idol of Oblivion（{2}｜Artifact） — {T}: Draw a card. Activate only if you created a token this turn. {8}, {T}, Sacrifice this artifact: Create a 10/10 colorless Eldrazi creature token.
  6. Hour of Reckoning（{4}{W}{W}{W}｜Sorcery） — Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.) Destroy all nontoken 
- **出场率最高的牌**（大多数牌组都会放）
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Champion of Lambholt（{1}{G}{G}｜Creature — Human Warrior） — Creatures with power less than this creature's power can't block creatures you control. Whenever another creature you control ente
  - Fortified Village（｜Land） — As this land enters, you may reveal a Forest or Plains card from your hand. If you don't, this land enters tapped. {T}: Add {G} or
