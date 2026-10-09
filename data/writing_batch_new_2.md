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


## Narset, Enlightened Exile ｜ 受启黜人娜尔施
- 颜色 WUR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Monk
- 流行度：EDHREC 全时段第 230 位，约 10473 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.78 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $7.68
- 社区标签：法术连发、灵技、衍生物、快攻、风暴、小牌抽
- 完整牌面：Creatures you control have prowess.
Whenever Narset attacks, exile target noncreature, nonland card with mana value less than Narset's power from a graveyard and copy it. You may cast the copy without paying its mana cost.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Monastery Mentor（{2}{W}｜Creature — Human Monk） — Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.) Whenever you cast a noncreature spell, create a 1/1 white Monk creature token
  2. Jeskai Ascendancy（{U}{R}{W}｜Enchantment） — Whenever you cast a noncreature spell, creatures you control get +1/+1 until end of turn. Untap those creatures. Whenever you cast a noncreature spell, you may draw a car
  3. Third Path Iconoclast（{U}{R}｜Creature — Human Monk） — Whenever you cast a noncreature spell, create a 1/1 colorless Soldier artifact creature token.
  4. Balmor, Battlemage Captain（{U}{R}｜Legendary Creature — Bird Wizard） — Flying Whenever you cast an instant or sorcery spell, creatures you control get +1/+0 and gain trample until end of turn.
  5. Kykar, Wind's Fury（{1}{U}{R}{W}｜Legendary Creature — Bird Wizard） — Flying Whenever you cast a noncreature spell, create a 1/1 white Spirit creature token with flying. Sacrifice a Spirit: Add {R}.
  6. Whirlwind of Thought（{1}{U}{R}{W}｜Enchantment） — Whenever you cast a noncreature spell, draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Ponder（{U}｜Sorcery） — Look at the top three cards of your library, then put them back in any order. You may shuffle. Draw a card.
  - Veyran, Voice of Duality（{1}{U}{R}｜Legendary Creature — Efreet Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, Veyran gets +1/+1 until end of turn. If you casting or copying 


## Raffine, Scheming Seer ｜ 卜策魔拉斐茵
- 颜色 WUB ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Sphinx Demon
- 流行度：EDHREC 全时段第 235 位，约 10346 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.36 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $7.07
- 社区标签：坟场复活、＋1/＋1 指示物、弃牌、换手牌、刺探、快攻
- 完整牌面：Flying, ward {1}
Whenever you attack, target attacking creature connives X, where X is the number of attacking creatures. (Draw X cards, then discard X cards. Put a +1/+1 counter on that creature for each nonland card discarded this way.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Archfiend of Ifnir（{3}{B}{B}｜Creature — Demon） — Flying Whenever you cycle or discard another card, put a -1/-1 counter on each creature your opponents control. Cycling {2} ({2}, Discard this card: Draw a card.)
  2. Reanimate（{B}｜Sorcery） — Put target creature card from a graveyard onto the battlefield under your control. You lose life equal to that card's mana value.
  3. Animate Dead（{1}{B}｜Enchantment — Aura） — Enchant creature card in a graveyard When this Aura enters, if it's on the battlefield, it loses "enchant creature card in a graveyard" and gains "enchant creature put on
  4. Ledger Shredder（{1}{U}｜Creature — Bird Advisor） — Flying Whenever a player casts their second spell each turn, this creature connives. (Draw a card, then discard a card. If you discarded a nonland card, put a +1/+1 count
  5. Victimize（{2}{B}｜Sorcery） — Choose two target creature cards in your graveyard. Sacrifice a creature. If you do, return the chosen cards to the battlefield tapped.
  6. Adeline, Resplendent Cathar（{1}{W}{W}｜Legendary Creature — Human Knight） — Vigilance Adeline's power is equal to the number of creatures you control. Whenever you attack, for each opponent, create a 1/1 white Human creature token that's tapped a
- **出场率最高的牌**（大多数牌组都会放）
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Raffine's Tower（｜Land — Plains Island Swamp） — ({T}: Add {W}, {U}, or {B}.) This land enters tapped. Cycling {3} ({3}, Discard this card: Draw a card.)


## Ojer Axonil, Deepest Might // Temple of Power ｜ 深邃勇力安雄理尊神
- 颜色 R ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — God // Land
- 流行度：EDHREC 全时段第 236 位，约 10331 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.73 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $24.12
- 社区标签：烧血、法术连发、快攻、群体折磨、点伤、锁场
- 完整牌面：Trample
If a red source you control would deal an amount of noncombat damage less than Ojer Axonil's power to an opponent, that source deals damage equal to Ojer Axonil's power instead.
When Ojer Axonil dies, return it to the battlefield tapped and transformed under its owner's control.
//
(Transforms from Ojer Axonil, Deepest Might.)
{T}: Add {R}.
{2}{R}, {T}: Transform this land. Activate only if red sources you controlled dealt 4 or more noncombat damage this turn and only as a sorcery.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Firebrand Archer（{1}{R}｜Creature — Human Archer） — Whenever you cast a noncreature spell, this creature deals 1 damage to each opponent.
  2. Thermo-Alchemist（{1}{R}｜Creature — Human Shaman） — Defender {T}: This creature deals 1 damage to each opponent. Whenever you cast an instant or sorcery spell, untap this creature.
  3. Kessig Flamebreather（{1}{R}｜Creature — Human Shaman） — Whenever you cast a noncreature spell, this creature deals 1 damage to each opponent.
  4. Tectonic Hazard（{R}｜Sorcery） — Tectonic Hazard deals 1 damage to each opponent and each creature they control.
  5. End the Festivities（{R}｜Sorcery） — End the Festivities deals 1 damage to each opponent and each creature and planeswalker they control.
  6. Manabarbs（{3}{R}｜Enchantment） — Whenever a player taps a land for mana, this enchantment deals 1 damage to that player.
- **出场率最高的牌**（大多数牌组都会放）
  - Ruby Medallion（{2}｜Artifact） — Red spells you cast cost {1} less to cast.
  - Coruscation Mage（{1}{R}｜Creature — Otter Wizard） — Offspring {2} (You may pay an additional {2} as you cast this spell. If you do, when this creature enters, create a 1/1 token copy
  - Fiery Confluence（{2}{R}{R}｜Sorcery） — Choose three. You may choose the same mode more than once. • Fiery Confluence deals 1 damage to each creature. • Fiery Confluence 
  - Grapeshot（{1}{R}｜Sorcery） — Grapeshot deals 1 damage to any target. Storm (When you cast this spell, copy it for each spell cast before it this turn. You may 


## Vihaan, Goldwaker ｜ 醒金师威翰
- 颜色 WBR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Dwarf Warlock
- 流行度：EDHREC 全时段第 239 位，约 10263 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.07 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：宝物、衍生物、神器、牺牲流、快攻、Outlaws
- 完整牌面：Other outlaws you control have vigilance and haste. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks are outlaws.)
At the beginning of combat on your turn, you may have Treasures you control become 3/3 Construct Assassin artifact creatures in addition to their other types until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mahadi, Emporium Master（{1}{B}{R}｜Legendary Creature — Devil） — At the beginning of your end step, create a Treasure token for each creature that died this turn. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any c
  2. Xorn（{2}{R}｜Creature — Elemental） — If you would create one or more Treasure tokens, instead create those tokens plus an additional Treasure token.
  3. Olivia, Opulent Outlaw（{1}{R}{W}{B}｜Legendary Creature — Vampire Assassin） — Flying, lifelink Whenever one or more outlaws you control deal combat damage to a player, create a Treasure token. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks 
  4. Pitiless Plunderer（{3}{B}｜Creature — Human Pirate） — Whenever another creature you control dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")
  5. Mari, the Killing Quill（{1}{B}{B}｜Legendary Creature — Vampire Assassin） — Whenever a creature an opponent controls dies, exile it with a hit counter on it. Assassins, Mercenaries, and Rogues you control have deathtouch and "Whenever this creatu
  6. Blood Money（{5}{B}{B}｜Sorcery） — Destroy all creatures. For each nontoken creature destroyed this way, you create a tapped Treasure token.
- **出场率最高的牌**（大多数牌组都会放）
  - Deadly Dispute（{1}{B}｜Instant） — As an additional cost to cast this spell, sacrifice an artifact or creature. Draw two cards and create a Treasure token. (It's an 
  - Professional Face-Breaker（{2}{R}｜Creature — Human Warrior） — Menace Whenever one or more creatures you control deal combat damage to a player, create a Treasure token. Sacrifice a Treasure: E
  - Big Score（{3}{R}｜Instant） — As an additional cost to cast this spell, discard a card. Draw two cards and create two Treasure tokens. (They're artifacts with "
  - Lotho, Corrupt Shirriff（{W}{B}｜Legendary Creature — Halfling Rogue） — Whenever a player casts their second spell each turn, you lose 1 life and create a Treasure token. (It's an artifact with "{T}, Sa


## The Gitrog Monster ｜ 噬人蛙怪
- 颜色 BG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Frog Horror
- 流行度：EDHREC 全时段第 243 位，约 10127 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.88 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.52
- 社区标签：地牌核心、挖掘、组合技、坟场、地落、加速
- 完整牌面：Deathtouch
At the beginning of your upkeep, sacrifice The Gitrog Monster unless you sacrifice a land.
You may play an additional land on each of your turns.
Whenever one or more land cards are put into your graveyard from anywhere, draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Dakmor Salvage（｜Land） — This land enters tapped. {T}: Add {B}. Dredge 2 (If you would draw a card, you may mill two cards instead. If you do, return this card from your graveyard to your hand.)
  2. Ramunap Excavator（{2}{G}｜Creature — Snake Cleric） — You may play lands from your graveyard.
  3. Crop Rotation（{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for a land card, put that card onto the battlefield, then shuffle.
  4. Life from the Loam（{1}{G}｜Sorcery） — Return up to three target land cards from your graveyard to your hand. Dredge 3 (If you would draw a card, you may mill three cards instead. If you do, return this card f
  5. Sylvan Safekeeper（{G}｜Creature — Human Wizard） — Sacrifice a land: Target creature you control gains shroud until end of turn. (It can't be the target of spells or abilities.)
  6. Icetill Explorer（{2}{G}{G}｜Creature — Insect Scout） — You may play an additional land on each of your turns. You may play lands from your graveyard. Landfall — Whenever a land you control enters, mill a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Assassin's Trophy（{B}{G}｜Instant） — Destroy target permanent an opponent controls. Its controller may search their library for a basic land card, put it onto the batt
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Verdant Catacombs（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Swamp or Forest card, put it onto the battlefield, then shuffle.
  - Harrow（{2}{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for up to two basic land cards, put them onto the 


## Lord Windgrace ｜ 风华领主
- 颜色 BRG ｜ 法术力值 5.0 ｜ 类型 Legendary Planeswalker — Windgrace
- 流行度：EDHREC 全时段第 245 位，约 10110 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.71 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：地牌核心、地落、加速、炸地、衍生物、坟场
- 完整牌面：+2: Discard a card, then draw a card. If a land card is discarded this way, draw an additional card.
−3: Return up to two target land cards from your graveyard to the battlefield.
−11: Destroy up to six target nonland permanents, then create six 2/2 green Cat Warrior creature tokens with forestwalk.
Lord Windgrace can be your commander.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. The Gitrog Monster（{3}{B}{G}｜Legendary Creature — Frog Horror） — Deathtouch At the beginning of your upkeep, sacrifice The Gitrog Monster unless you sacrifice a land. You may play an additional land on each of your turns. Whenever one 
  2. Ramunap Excavator（{2}{G}｜Creature — Snake Cleric） — You may play lands from your graveyard.
  3. Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  4. Azusa, Lost but Seeking（{2}{G}｜Legendary Creature — Human Monk） — You may play two additional lands on each of your turns.
  5. Avenger of Zendikar（{5}{G}{G}｜Creature — Elemental） — When this creature enters, create a 0/1 green Plant creature token for each land you control. Landfall — Whenever a land you control enters, you may put a +1/+1 counter o
  6. Splendid Reclamation（{3}{G}｜Sorcery） — Return all land cards from your graveyard to the battlefield tapped.
- **出场率最高的牌**（大多数牌组都会放）
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Omnath, Locus of Rage（{3}{R}{R}{G}{G}｜Legendary Creature — Elemental） — Landfall — Whenever a land you control enters, create a 5/5 red and green Elemental creature token. Whenever Omnath or another Ele
  - Crop Rotation（{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for a land card, put that card onto the battlefiel
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Jetmir, Nexus of Revels ｜ 欢宴魔杰米尔
- 颜色 WRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Cat Demon
- 流行度：EDHREC 全时段第 252 位，约 9901 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.89 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $9.52
- 社区标签：衍生物、快攻、猫、锁场小兵、＋1/＋1 指示物、锁场
- 完整牌面：Creatures you control get +1/+0 and have vigilance as long as you control three or more creatures.
Creatures you control also get +1/+0 and have trample as long as you control six or more creatures.
Creatures you control also get +1/+0 and have double strike as long as you control nine or more creatures.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Adeline, Resplendent Cathar（{1}{W}{W}｜Legendary Creature — Human Knight） — Vigilance Adeline's power is equal to the number of creatures you control. Whenever you attack, for each opponent, create a 1/1 white Human creature token that's tapped a
  2. Artifact Mutation（{R}{G}｜Instant） — Destroy target artifact. It can't be regenerated. Create X 1/1 green Saproling creature tokens, where X is that artifact's mana value.
  3. Aura Mutation（{G}{W}｜Instant） — Destroy target enchantment. Create X 1/1 green Saproling creature tokens, where X is that enchantment's mana value.
  4. Krenko, Tin Street Kingpin（{2}{R}｜Legendary Creature — Goblin） — Whenever Krenko attacks, put a +1/+1 counter on it, then create a number of 1/1 red Goblin creature tokens equal to Krenko's power.
  5. Grand Crescendo（{X}{W}{W}｜Instant） — Create X 1/1 green and white Citizen creature tokens. Creatures you control gain indestructible until end of turn.
  6. March of the Multitudes（{X}{G}{W}{W}｜Instant） — Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.) Create X 1/1 white So
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Jetmir's Garden（｜Land — Mountain Forest Plains） — ({T}: Add {R}, {G}, or {W}.) This land enters tapped. Cycling {3} ({3}, Discard this card: Draw a card.)
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Kutzil, Malamet Exemplar（{1}{G}{W}｜Legendary Creature — Cat Warrior） — Your opponents can't cast spells during your turn. Whenever one or more creatures you control each with power greater than its bas


## Rocco, Cabaretti Caterer ｜ 乐舞会主厨罗孔
- 颜色 WRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elf Druid
- 流行度：EDHREC 全时段第 253 位，约 9896 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.61 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.23
- 社区标签：诞生荚、组合技、闪现回场、工具箱、烧血、衍生物
- 完整牌面：When Rocco enters, if you cast it, you may search your library for a creature card with mana value X or less, put it onto the battlefield, then shuffle.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Wirewood Symbiote（{G}｜Creature — Insect） — Return an Elf you control to its owner's hand: Untap target creature. Activate only once each turn.
  2. Eternal Witness（{1}{G}{G}｜Creature — Human Shaman） — When this creature enters, you may return target card from your graveyard to your hand.
  3. Norin the Wary（{R}｜Legendary Creature — Human Warrior） — When a player casts a spell or a creature attacks, exile Norin. Return it to the battlefield under its owner's control at the beginning of the next end step.
  4. Avacyn's Pilgrim（{G}｜Creature — Human Monk） — {T}: Add {W}.
  5. Welcoming Vampire（{2}{W}｜Creature — Vampire） — Flying Whenever one or more other creatures you control with power 2 or less enter, draw a card. This ability triggers only once each turn.
  6. Gala Greeters（{1}{G}｜Creature — Elf Druid） — Alliance — Whenever another creature you control enters, choose one that hasn't been chosen this turn — • Put a +1/+1 counter on this creature. • Create a tapped Treasure
- **出场率最高的牌**（大多数牌组都会放）
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Sacred Foundry（｜Land — Mountain Plains） — ({T}: Add {R} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.


## Nicol Bolas, the Ravager // Nicol Bolas, the Arisen ｜ 烈龙尼可波拉斯
- 颜色 UBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Elder Dragon // Legendary Planeswalker — Bolas
- 流行度：EDHREC 全时段第 254 位，约 9895 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.77 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $17.44
- 社区标签：鹏洛客、控制、弃牌、坟场复活、组合技、龙
- 完整牌面：Flying
When Nicol Bolas enters, each opponent discards a card.
{4}{U}{B}{R}: Exile Nicol Bolas, then return him to the battlefield transformed under his owner's control. Activate only as a sorcery.
//
+2: Draw two cards.
−3: Nicol Bolas deals 10 damage to target creature or planeswalker.
−4: Put target creature or planeswalker card from a graveyard onto the battlefield under your control.
−12: Exile all but the bottom card of target player's library.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Nicol Bolas, Dragon-God（{U}{B}{B}{B}{R}｜Legendary Planeswalker — Bolas） — Nicol Bolas has all loyalty abilities of all other planeswalkers on the battlefield. +1: You draw a card. Each opponent exiles a card from their hand or a permanent they 
  2. Nicol Bolas, God-Pharaoh（{4}{U}{B}{R}｜Legendary Planeswalker — Bolas） — +2: Target opponent exiles cards from the top of their library until they exile a nonland card. Until end of turn, you may cast that card without paying its mana cost. +1
  3. Nicol Bolas, Planeswalker（{4}{U}{B}{B}{R}｜Legendary Planeswalker — Bolas） — +3: Destroy target noncreature permanent. −2: Gain control of target creature. −9: Nicol Bolas deals 7 damage to target player or planeswalker. That player or that planes
  4. The Eldest Reborn（{4}{B}｜Enchantment — Saga） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Each opponent sacrifices a creature or planeswalker of their choice. II — Eac
  5. Deliver Unto Evil（{2}{B}｜Sorcery） — Choose up to four target cards in your graveyard. If you control a Bolas planeswalker, return those cards to your hand. Otherwise, an opponent chooses two of them. Leave 
  6. Nicol Bolas, the Deceiver（{5}{U}{B}{R}｜Legendary Planeswalker — Bolas） — +3: Each opponent loses 3 life unless that player sacrifices a nonland permanent of their choice or discards a card. −3: Destroy target creature. Draw a card. −11: Nicol 
- **出场率最高的牌**（大多数牌组都会放）
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Steam Vents（｜Land — Island Mountain） — ({T}: Add {U} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Blood Crypt（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.


## Omnath, Locus of Mana ｜ 魔力核欧那斯
- 颜色 G ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elemental
- 流行度：EDHREC 全时段第 255 位，约 9771 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.5 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $4.16
- 社区标签：加速、爆费、主将单挑、地牌核心、妖精、＋1/＋1 指示物
- 完整牌面：You don't lose unspent green mana as steps and phases end.
Omnath gets +1/+1 for each unspent green mana you have.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mana Reflection（{4}{G}{G}｜Enchantment） — If you tap a permanent for mana, it produces twice as much of that mana instead.
  2. Doubling Cube（{2}｜Artifact） — {3}, {T}: Double the amount of each type of unspent mana you have.
  3. Wilderness Reclamation（{3}{G}｜Enchantment） — At the beginning of your end step, untap all lands you control.
  4. Seedborn Muse（{3}{G}{G}｜Creature — Spirit） — Untap all permanents you control during each other player's untap step.
  5. Nyxbloom Ancient（{4}{G}{G}{G}｜Enchantment Creature — Elemental） — Trample If you tap a permanent for mana, it produces three times as much of that mana instead.
  6. Selvala, Heart of the Wilds（{1}{G}{G}｜Legendary Creature — Elf Scout） — Whenever another creature enters, its controller may draw a card if its power is greater than each other creature's power. {G}, {T}: Add X mana in any combination of colo
- **出场率最高的牌**（大多数牌组都会放）
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Fyndhorn Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Nissa, Who Shakes the World（{3}{G}{G}｜Legendary Planeswalker — Nissa） — Whenever you tap a Forest for mana, add an additional {G}. +1: Put three +1/+1 counters on up to one target noncreature land you c


## Chulane, Teller of Tales ｜ 说书人楚兰
- 颜色 WUG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Druid
- 流行度：EDHREC 全时段第 258 位，约 9719 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.25 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.44
- 社区标签：组合技、地牌核心、加速、地落、闪现回场、抽牌
- 完整牌面：Vigilance
Whenever you cast a creature spell, draw a card, then you may put a land card from your hand onto the battlefield.
{3}, {T}: Return target creature you control to its owner's hand.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Shrieking Drake（{U}｜Creature — Drake） — Flying When this creature enters, return a creature you control to its owner's hand.
  2. Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  3. Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  4. Whitemane Lion（{1}{W}｜Creature — Cat） — Flash When this creature enters, return a creature you control to its owner's hand.
  5. Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  6. Tatyova, Benthic Druid（{3}{G}{U}｜Legendary Creature — Merfolk Druid） — Landfall — Whenever a land you control enters, you gain 1 life and draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Roxanne, Starfall Savant ｜ 落星学者罗珊妮
- 颜色 RG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Cat Druid
- 流行度：EDHREC 全时段第 259 位，约 9631 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.47 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.21
- 社区标签：宝物、衍生物、神器、烧血、加速、快攻
- 完整牌面：Whenever Roxanne enters or attacks, create a tapped colorless artifact token named Meteorite with "When this token enters, it deals 2 damage to any target" and "{T}: Add one mana of any color."
Whenever you tap an artifact token for mana, add one mana of any type that artifact token produced.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Second Harvest（{2}{G}{G}｜Instant） — For each token you control, create a token that's a copy of that permanent.
  2. Panharmonicon（{4}｜Artifact） — If an artifact or creature entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
  3. Reckless Fireweaver（{1}{R}｜Creature — Human Artificer） — Whenever an artifact you control enters, this creature deals 1 damage to each opponent.
  4. For the Common Good（{X}{X}{G}｜Sorcery） — Create X tokens that are copies of target token you control. Then tokens you control gain indestructible until your next turn. You gain 1 life for each token you control.
  5. Parallel Lives（{3}{G}｜Enchantment） — If an effect would create one or more tokens under your control, it creates twice that many of those tokens instead.
  6. Blade of Selves（{2}｜Artifact — Equipment） — Equipped creature has myriad. (Whenever it attacks, for each opponent other than defending player, you may create a token copy that's tapped and attacking that player or 
- **出场率最高的牌**（大多数牌组都会放）
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Rootbound Crag（｜Land） — This land enters tapped unless you control a Mountain or a Forest. {T}: Add {R} or {G}.
  - Goblin Anarchomancer（{R}{G}｜Creature — Goblin Shaman） — Each spell you cast that's red or green costs {1} less to cast.
  - Big Score（{3}{R}｜Instant） — As an additional cost to cast this spell, discard a card. Draw two cards and create two Treasure tokens. (They're artifacts with "


## Shalai and Hallar ｜ 莎黎与贺拉尔
- 颜色 WRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Angel Elf
- 流行度：EDHREC 全时段第 261 位，约 9606 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.36 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.51
- 社区标签：＋1/＋1 指示物、烧血、组合技、快攻、生命增益、中速
- 完整牌面：Flying, vigilance
Whenever one or more +1/+1 counters are put on a creature you control, Shalai and Hallar deals that much damage to target opponent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Forgotten Ancient（{3}{G}｜Creature — Elemental） — Whenever a player casts a spell, you may put a +1/+1 counter on this creature. At the beginning of your upkeep, you may move any number of +1/+1 counters from this creatu
  2. Managorger Hydra（{2}{G}｜Creature — Hydra） — Trample Whenever a player casts a spell, put a +1/+1 counter on this creature.
  3. Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  4. Inspiring Call（{2}{G}｜Instant） — Draw a card for each creature you control with a +1/+1 counter on it. Those creatures gain indestructible until end of turn. (Damage and effects that say "destroy" don't 
  5. Kami of Whispered Hopes（{2}{G}｜Creature — Spirit） — If one or more +1/+1 counters would be put on a permanent you control, that many plus one +1/+1 counters are put on that permanent instead. {T}: Add X mana of any one col
  6. Kalonian Hydra（{3}{G}{G}｜Creature — Hydra） — Trample This creature enters with four +1/+1 counters on it. Whenever this creature attacks, double the number of +1/+1 counters on each creature you control.
- **出场率最高的牌**（大多数牌组都会放）
  - Gavony Township（｜Land） — {T}: Add {C}. {2}{G}{W}, {T}: Put a +1/+1 counter on each creature you control.
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Branching Evolution（{2}{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, twice that many +1/+1 counters are put on that creature inst
  - Jungle Shrine（｜Land） — This land enters tapped. {T}: Add {R}, {G}, or {W}.


## Queza, Augur of Agonies ｜ 苦痛占师桂莎
- 颜色 WUB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Octopus Advisor
- 流行度：EDHREC 全时段第 263 位，约 9540 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 0.53 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.30
- 社区标签：换手牌、抽牌、生命增益、组合技、控制、吸取生命
- 完整牌面：Whenever you draw a card, target opponent loses 1 life and you gain 1 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Psychosis Crawler（{5}｜Artifact Creature — Phyrexian Horror） — Psychosis Crawler's power and toughness are each equal to the number of cards in your hand. Whenever you draw a card, each opponent loses 1 life.
  2. Marauding Blight-Priest（{2}{B}｜Creature — Vampire Cleric） — Whenever you gain life, each opponent loses 1 life.
  3. Peer into the Abyss（{4}{B}{B}{B}｜Sorcery） — Target player draws cards equal to half the number of cards in their library and loses half their life. Round up each time.
  4. Teferi's Ageless Insight（{2}{U}{U}｜Legendary Enchantment） — If you would draw a card except the first one you draw in each of your draw steps, draw two cards instead.
  5. Drogskol Reaver（{5}{W}{U}｜Creature — Spirit） — Flying Double strike (This creature deals both first-strike and regular combat damage.) Lifelink (Damage dealt by this creature also causes you to gain that much life.) W
  6. Laboratory Maniac（{2}{U}｜Creature — Human Wizard） — If you would draw a card while your library has no cards in it, you win the game instead.
- **出场率最高的牌**（大多数牌组都会放）
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  - Windfall（{2}{U}｜Sorcery） — Each player discards their hand, then draws cards equal to the greatest number of cards a player discarded this way.
  - Arcane Sanctum（｜Land） — This land enters tapped. {T}: Add {W}, {U}, or {B}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t


## Dina, Soul Steeper ｜ 浸灵迪娜
- 颜色 BG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Dryad Druid
- 流行度：EDHREC 全时段第 264 位，约 9496 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.4 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.29
- 社区标签：生命增益、牺牲流、吸取生命、组合技、衍生物、牺牲
- 完整牌面：Whenever you gain life, each opponent loses 1 life.
{1}, Sacrifice another creature: Dina gets +X/+0 until end of turn, where X is the sacrificed creature's power.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Marauding Blight-Priest（{2}{B}｜Creature — Vampire Cleric） — Whenever you gain life, each opponent loses 1 life.
  2. Essence Warden（{G}｜Creature — Elf Shaman） — Whenever another creature enters, you gain 1 life.
  3. Mortality Spear（{2}{B}{G}｜Instant） — This spell costs {2} less to cast if you gained life this turn. Destroy target nonland permanent.
  4. Deathgreeter（{B}｜Creature — Human Shaman） — Whenever another creature dies, you may gain 1 life.
  5. Prosperous Innkeeper（{1}{G}｜Creature — Halfling Citizen） — When this creature enters, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.") Whenever another creature you control 
  6. Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Jungle Hollow（｜Land） — This land enters tapped. When this land enters, you gain 1 life. {T}: Add {B} or {G}.
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Zulaport Cutthroat（{1}{B}｜Creature — Human Rogue Ally） — Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life.
  - Llanowar Wastes（｜Land） — {T}: Add {C}. {T}: Add {B} or {G}. This land deals 1 damage to you.


## Jodah, Archmage Eternal ｜ 永世大法师裘达
- 颜色 WUBRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Wizard
- 流行度：EDHREC 全时段第 267 位，约 9466 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.01 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.99
- 社区标签：爆费、优质单卡堆、倾曳、加速、传奇、组合技
- 完整牌面：Flying
You may pay {W}{U}{B}{R}{G} rather than pay the mana cost for spells you cast.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Omniscience（{7}{U}{U}{U}｜Enchantment） — You may cast spells from your hand without paying their mana costs.
  2. Fist of Suns（{3}｜Artifact） — You may pay {W}{U}{B}{R}{G} rather than pay the mana cost for spells you cast.
  3. Ruinous Ultimatum（{R}{R}{W}{W}{W}{B}{B}｜Sorcery） — Destroy all nonland permanents your opponents control.
  4. Apex Devastator（{8}{G}{G}｜Creature — Chimera Hydra） — Cascade, cascade, cascade, cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it wit
  5. Conflux（{3}{W}{U}{B}{R}{G}｜Sorcery） — Search your library for a white card, a blue card, a black card, a red card, and a green card. Reveal those cards, put them into your hand, then shuffle.
  6. Genesis Ultimatum（{G}{G}{U}{U}{U}{R}{R}｜Sorcery） — Look at the top five cards of your library. Put any number of permanent cards from among them onto the battlefield and the rest into your hand. Exile Genesis Ultimatum.
- **出场率最高的牌**（大多数牌组都会放）
  - Faeburrow Elder（{1}{G}{W}｜Creature — Treefolk Druid） — Vigilance This creature gets +1/+1 for each color among permanents you control. {T}: For each color among permanents you control, 
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Maelstrom Wanderer（{5}{G}{U}{R}｜Legendary Creature — Elemental） — Creatures you control have haste. Cascade, cascade (When you cast this spell, exile cards from the top of your library until you e
  - Timeless Lotus（{5}｜Legendary Artifact） — Timeless Lotus enters tapped. {T}: Add {W}{U}{B}{R}{G}.


## Tatyova, Benthic Druid ｜ 深洋德鲁伊塔托娃
- 颜色 UG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Merfolk Druid
- 流行度：EDHREC 全时段第 268 位，约 9444 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.82 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.28
- 社区标签：地牌核心、地落、加速、组合技、中速、衍生物
- 完整牌面：Landfall — Whenever a land you control enters, you gain 1 life and draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Azusa, Lost but Seeking（{2}{G}｜Legendary Creature — Human Monk） — You may play two additional lands on each of your turns.
  2. Rampaging Baloths（{4}{G}{G}｜Creature — Beast） — Trample Landfall — Whenever a land you control enters, create a 4/4 green Beast creature token.
  3. Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  4. Harrow（{2}{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for up to two basic land cards, put them onto the battlefield, then shuffle.
  5. Tireless Provisioner（{2}{G}｜Creature — Elf Scout） — Landfall — Whenever a land you control enters, create a Food token or a Treasure token. (Food is an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life." Treas
  6. Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create a token that's a copy of this creature i
- **出场率最高的牌**（大多数牌组都会放）
  - Simic Growth Chamber（｜Land） — This land enters tapped. When this land enters, return a land you control to its owner's hand. {T}: Add {G}{U}.
  - Growth Spiral（{G}{U}｜Instant） — Draw a card. You may put a land card from your hand onto the battlefield.
  - Avenger of Zendikar（{5}{G}{G}｜Creature — Elemental） — When this creature enters, create a 0/1 green Plant creature token for each land you control. Landfall — Whenever a land you contr
  - Explore（{1}{G}｜Sorcery） — You may play an additional land this turn. Draw a card.


## Mirko, Obsessive Theorist ｜ 偏执理论家梅可
- 颜色 UB ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Vampire Detective
- 流行度：EDHREC 全时段第 271 位，约 9348 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.65 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：坟场复活、牌库顶、刺探、复制、坟场、＋1/＋1 指示物
- 完整牌面：Flying, vigilance
Whenever you surveil, put a +1/+1 counter on Mirko.
At the beginning of your end step, you may return target creature card with power less than Mirko's from your graveyard to the battlefield with a finality counter on it. (If it would die, exile it instead.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Doom Whisperer（{3}{B}{B}｜Creature — Nightmare Demon） — Flying, trample Pay 2 life: Surveil 2. (Look at the top two cards of your library, then put any number of them into your graveyard and the rest on top of your library in 
  2. Unshakable Tail（{2}{B}｜Creature — Zombie Detective） — When this creature enters and at the beginning of your upkeep, surveil 1. Whenever one or more creature cards are put into your graveyard from your library, investigate. 
  3. Sinister Starfish（{1}{B}｜Creature — Starfish） — {T}: Surveil 1. (Look at the top card of your library. You may put it into your graveyard.)
  4. Otherworldly Gaze（{U}｜Instant） — Surveil 3. (Look at the top three cards of your library, then put any number of them into your graveyard and the rest on top of your library in any order.) Flashback {1}{
  5. Case of the Shifting Visage（{1}{U}{U}｜Enchantment — Case） — At the beginning of your upkeep, surveil 1. To solve — There are fifteen or more cards in your graveyard. (If unsolved, solve at the beginning of your end step.) Solved —
  6. Pile On（{3}{B}｜Instant） — Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.) Destroy target creatu
- **出场率最高的牌**（大多数牌组都会放）
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Consider（{U}｜Instant） — Surveil 1. (Look at the top card of your library. You may put it into your graveyard.) Draw a card.
  - Reanimate（{B}｜Sorcery） — Put target creature card from a graveyard onto the battlefield under your control. You lose life equal to that card's mana value.
  - Tainted Isle（｜Land） — {T}: Add {C}. {T}: Add {U} or {B}. Activate only if you control a Swamp.


## The Mycotyrant ｜ 智蕈暴君
- 颜色 BG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elder Fungus
- 流行度：EDHREC 全时段第 275 位，约 9272 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.27 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.35
- 社区标签：磨牌、衍生物、自磨、挖掘、Fungi、坟场复活
- 完整牌面：Trample
The Mycotyrant's power and toughness are each equal to the number of creatures you control that are Fungi and/or Saprolings.
At the beginning of your end step, create X 1/1 black Fungus creature tokens with "This token can't block," where X is the number of times you descended this turn. (You descend each time a permanent card is put into your graveyard from anywhere.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Skull Prophet（{B}{G}｜Creature — Human Druid） — {T}: Add {B} or {G}. {T}: Mill two cards. (Put the top two cards of your library into your graveyard.)
  2. Mycoloth（{3}{G}{G}｜Creature — Fungus） — Devour 2 (As this creature enters, you may sacrifice any number of creatures. It enters with twice that many +1/+1 counters on it.) At the beginning of your upkeep, creat
  3. Golgari Grave-Troll（{4}{G}｜Creature — Troll Skeleton） — This creature enters with a +1/+1 counter on it for each creature card in your graveyard. {1}, Remove a +1/+1 counter from this creature: Regenerate this creature. Dredge
  4. Cankerbloom（{1}{G}｜Creature — Phyrexian Fungus） — {1}, Sacrifice this creature: Choose one — • Destroy target artifact. • Destroy target enchantment. • Proliferate. (Choose any number of permanents and/or players, then g
  5. Nyx Weaver（{1}{B}{G}｜Enchantment Creature — Spider） — Reach At the beginning of your upkeep, mill two cards. (Put the top two cards of your library into your graveyard.) {1}{B}{G}, Exile this creature: Return target card fro
  6. Insidious Roots（{B}{G}｜Enchantment） — Creature tokens you control have "{T}: Add one mana of any color." Whenever one or more creature cards leave your graveyard, create a 0/1 green Plant creature token, then
- **出场率最高的牌**（大多数牌组都会放）
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Mirkwood Bats（{3}{B}｜Creature — Bat） — Flying Whenever you create or sacrifice a token, each opponent loses 1 life.
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  - Syr Konrad, the Grim（{3}{B}{B}｜Legendary Creature — Human Knight） — Whenever another creature dies, or a creature card is put into a graveyard from anywhere other than the battlefield, or a creature


## Hazezon, Shaper of Sand ｜ 塑砂师哈泽忠
- 颜色 WRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Warrior
- 流行度：EDHREC 全时段第 278 位，约 9252 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.53 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.29
- 社区标签：地牌核心、衍生物、Deserts、地落、加速、炸地
- 完整牌面：Desertwalk (This creature can't be blocked as long as defending player controls a Desert.)
You may play Desert lands from your graveyard.
Whenever a Desert you control enters, create two 1/1 red, green, and white Sand Warrior creature tokens.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Hashep Oasis（｜Land — Desert） — {T}: Add {C}. {T}, Pay 1 life: Add {G}. {1}{G}{G}, {T}, Sacrifice a Desert: Target creature gets +3/+3 until end of turn. Activate only as a sorcery.
  2. Desert of the Indomitable（｜Land — Desert） — This land enters tapped. {T}: Add {G}. Cycling {1}{G} ({1}{G}, Discard this card: Draw a card.)
  3. Desert of the True（｜Land — Desert） — This land enters tapped. {T}: Add {W}. Cycling {1}{W} ({1}{W}, Discard this card: Draw a card.)
  4. Ramunap Ruins（｜Land — Desert） — {T}: Add {C}. {T}, Pay 1 life: Add {R}. {2}{R}{R}, {T}, Sacrifice a Desert: This land deals 2 damage to each opponent.
  5. Shefet Dunes（｜Land — Desert） — {T}: Add {C}. {T}, Pay 1 life: Add {W}. {2}{W}{W}, {T}, Sacrifice a Desert: Creatures you control get +1/+1 until end of turn. Activate only as a sorcery.
  6. Desert of the Fervent（｜Land — Desert） — This land enters tapped. {T}: Add {R}. Cycling {1}{R} ({1}{R}, Discard this card: Draw a card.)
- **出场率最高的牌**（大多数牌组都会放）
  - Creosote Heath（｜Land — Desert） — This land enters tapped. When this land enters, it deals 1 damage to target opponent. {T}: Add {G} or {W}.
  - Dunes of the Dead（｜Land — Desert） — {T}: Add {C}. When this land is put into a graveyard from the battlefield, create a 2/2 black Zombie creature token.
  - Bristling Backwoods（｜Land — Desert） — This land enters tapped. When this land enters, it deals 1 damage to target opponent. {T}: Add {R} or {G}.
  - Dune Chanter（{2}{G}｜Creature — Plant Druid） — Reach Lands you control and land cards you own that aren't on the battlefield are Deserts in addition to their other types. Lands 


## Reaper King ｜ 夺命王者
- 颜色 WUBRG ｜ 法术力值 10.0 ｜ 类型 Legendary Artifact Creature — Scarecrow
- 流行度：EDHREC 全时段第 281 位，约 9231 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.9 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $12.81
- 社区标签：Scarecrows、神器、变形兽、闪现回场、炸地、控制
- 完整牌面：({2/W} can be paid with any two mana or with {W}. This card's mana value is 10.)
Other Scarecrow creatures you control get +1/+1.
Whenever another Scarecrow you control enters, destroy target permanent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Scuttlemutt（{3}｜Artifact Creature — Scarecrow） — {T}: Add one mana of any color. {T}: Target creature becomes the color or colors of your choice until end of turn.
  2. Scarecrone（{3}｜Artifact Creature — Scarecrow） — {1}, Sacrifice a Scarecrow: Draw a card. {4}, {T}: Return target artifact creature card from your graveyard to the battlefield.
  3. Oasis Gardener（{3}｜Artifact Creature — Scarecrow） — When this creature enters, you gain 2 life. {T}: Add one mana of any color.
  4. Scaretiller（{4}｜Artifact Creature — Scarecrow） — Whenever this creature becomes tapped, choose one — • You may put a land card from your hand onto the battlefield tapped. • Return target land card from your graveyard to
  5. Panharmonicon（{4}｜Artifact） — If an artifact or creature entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
  6. Heap Doll（{1}｜Artifact Creature — Scarecrow） — Sacrifice this creature: Exile target card from a graveyard.
- **出场率最高的牌**（大多数牌组都会放）
  - Maskwood Nexus（{4}｜Artifact） — Creatures you control are every creature type. The same is true for creature spells you control and creature cards you own that ar
  - Realmwalker（{2}{G}｜Creature — Shapeshifter） — Changeling (This card is every creature type.) As this creature enters, choose a creature type. You may look at the top card of yo
  - Wild-Field Scarecrow（{3}｜Artifact Creature — Scarecrow） — Defender {2}, Sacrifice this creature: Search your library for up to two basic land cards, reveal them, put them into your hand, t
  - Reflections of Littjara（{4}{U}｜Enchantment） — As this enchantment enters, choose a creature type. Whenever you cast a spell of the chosen type, copy that spell. (A copy of a pe


## Marvo, Deep Operative ｜ 深洋密探玛沃
- 颜色 UB ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Octopus Rogue
- 流行度：EDHREC 全时段第 282 位，约 9154 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.13 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：牌库顶、爆费、海洋生物、Clash、控制、复制
- 完整牌面：Whenever Marvo attacks, clash with defending player. (Each clashing player reveals the top card of their library, then puts that card on their choice of the top or bottom. A player wins if their card had a greater mana value.)
Whenever you win a clash, draw a card. Then you may cast a spell from your hand with mana value 8 or less without paying its mana cost.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Research the Deep（{1}{U}｜Sorcery） — Draw a card. Clash with an opponent. If you win, return Research the Deep to its owner's hand. (Each clashing player reveals the top card of their library, then puts that
  2. One with the Multiverse（{6}{U}{U}｜Enchantment） — You may look at the top card of your library any time. You may play lands and cast spells from the top of your library. Once during each of your turns, you may cast a spe
  3. Revive the Fallen（{1}{B}｜Sorcery） — Return target creature card from a graveyard to its owner's hand. Clash with an opponent. If you win, return Revive the Fallen to its owner's hand. (Each clashing player 
  4. Whirlpool Whelm（{1}{U}｜Instant） — Clash with an opponent, then return target creature to its owner's hand. If you win, you may put that creature on top of its owner's library instead. (Each clashing playe
  5. Hoarder's Greed（{3}{B}｜Sorcery） — You lose 2 life and draw two cards, then clash with an opponent. If you win, repeat this process. (Each clashing player reveals the top card of their library, then puts t
  6. Scattering Stroke（{2}{U}{U}｜Instant） — Counter target spell. Clash with an opponent. If you win, at the beginning of your next main phase, you may add an amount of {C} equal to that spell's mana value. (Each c
- **出场率最高的牌**（大多数牌组都会放）
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Dimir Signet（{2}｜Artifact） — {1}, {T}: Add {U}{B}.
  - Lantern of Insight（{1}｜Artifact） — Players play with the top card of their libraries revealed. {T}, Sacrifice this artifact: Target player shuffles.


## Norin the Wary ｜ 谨慎的诺林
- 颜色 R ｜ 法术力值 1.0 ｜ 类型 Legendary Creature — Human Warrior
- 流行度：EDHREC 全时段第 283 位，约 9143 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.8 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $19.48
- 社区标签：烧血、混乱、闪现回场、进场触发、群体折磨、衍生物
- 完整牌面：When a player casts a spell or a creature attacks, exile Norin. Return it to the battlefield under its owner's control at the beginning of the next end step.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Genesis Chamber（{2}｜Artifact） — Whenever a nontoken creature enters, if this artifact is untapped, that creature's controller creates a 1/1 colorless Myr artifact creature token.
  2. Tome of Legends（{2}｜Artifact — Book） — This artifact enters with a page counter on it. Whenever your commander enters or attacks, put a page counter on this artifact. {1}, {T}, Remove a page counter from this 
  3. Witty Roastmaster（{2}{R}｜Creature — Devil Citizen） — Alliance — Whenever another creature you control enters, this creature deals 1 damage to each opponent.
  4. Rose Room Treasurer（{3}{R}｜Creature — Ogre Warrior） — Alliance — Whenever another creature you control enters, create a Treasure token if this is the first or second time this ability has resolved this turn. Otherwise, you m
  5. Molten Gatekeeper（{2}{R}｜Artifact Creature — Golem） — Whenever another creature you control enters, this creature deals 1 damage to each opponent. Unearth {R} ({R}: Return this card from your graveyard to the battlefield. It
  6. Panharmonicon（{4}｜Artifact） — If an artifact or creature entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
- **出场率最高的牌**（大多数牌组都会放）
  - Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  - Purphoros, God of the Forge（{3}{R}｜Legendary Enchantment Creature — God） — Indestructible As long as your devotion to red is less than five, Purphoros isn't a creature. Whenever another creature you contro
  - Torbran, Thane of Red Fell（{1}{R}{R}{R}｜Legendary Creature — Dwarf Noble） — If a red source you control would deal damage to an opponent or a permanent an opponent controls, it deals that much damage plus 2
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.


## Gargos, Vicious Watcher ｜ 卫护恶龙加戈斯
- 颜色 G ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Hydra
- 流行度：EDHREC 全时段第 284 位，约 9139 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.47 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.20
- 社区标签：＋1/＋1 指示物、多头龙、X 咒语、加速、快攻、互斗
- 完整牌面：Vigilance
Hydra spells you cast cost {4} less to cast.
Whenever a creature you control becomes the target of a spell, Gargos fights up to one target creature you don't control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Voracious Hydra（{X}{G}{G}｜Creature — Hydra） — Trample This creature enters with X +1/+1 counters on it. When this creature enters, choose one — • Double the number of +1/+1 counters on this creature. • This creature 
  2. Managorger Hydra（{2}{G}｜Creature — Hydra） — Trample Whenever a player casts a spell, put a +1/+1 counter on this creature.
  3. Kalonian Hydra（{3}{G}{G}｜Creature — Hydra） — Trample This creature enters with four +1/+1 counters on it. Whenever this creature attacks, double the number of +1/+1 counters on each creature you control.
  4. Hungering Hydra（{X}{G}｜Creature — Hydra） — This creature enters with X +1/+1 counters on it. This creature can't be blocked by more than one creature. Whenever this creature is dealt damage, put that many +1/+1 co
  5. Lifeblood Hydra（{X}{G}{G}{G}｜Creature — Hydra） — Trample This creature enters with X +1/+1 counters on it. When this creature dies, you gain life and draw cards equal to its power.
  6. Hydra Omnivore（{4}{G}{G}｜Creature — Hydra） — Whenever this creature deals combat damage to an opponent, it deals that much damage to each other opponent.
- **出场率最高的牌**（大多数牌组都会放）
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Primordial Hydra（{X}{G}{G}｜Creature — Hydra） — This creature enters with X +1/+1 counters on it. At the beginning of your upkeep, double the number of +1/+1 counters on this cre
  - Steelbane Hydra（{X}{G}{G}｜Creature — Turtle Hydra） — This creature enters with X +1/+1 counters on it. {2}{G}, Remove a +1/+1 counter from this creature: Destroy target artifact or en
  - Genesis Hydra（{X}{G}{G}｜Creature — Plant Hydra） — When you cast this spell, reveal the top X cards of your library. You may put a nonland permanent card with mana value X or less f


## Athreos, God of Passage ｜ 渡亡神雅睿欧斯
- 颜色 WB ｜ 法术力值 3.0 ｜ 类型 Legendary Enchantment Creature — God
- 流行度：EDHREC 全时段第 287 位，约 9114 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.59 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $15.33
- 社区标签：牺牲流、Shadowborn Apostles、生命增益、坟场复活、恶魔、牺牲
- 完整牌面：Indestructible
As long as your devotion to white and black is less than seven, Athreos isn't a creature.
Whenever another creature you own dies, return it to your hand unless target opponent pays 3 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Shadowborn Apostle（{B}｜Creature — Human Cleric） — A deck can have any number of cards named Shadowborn Apostle. {B}, Sacrifice six creatures named Shadowborn Apostle: Search your library for a Demon creature card, put it
  2. Edgewalker（{1}{W}{B}｜Creature — Human Cleric） — Cleric spells you cast cost {W}{B} less to cast. This effect reduces only the amount of colored mana you pay. (For example, if you cast a Cleric spell with mana cost {1}{
  3. Immortal Servitude（{X}{W/B}{W/B}{W/B}｜Sorcery） — Return each creature card with mana value X from your graveyard to the battlefield.
  4. Razaketh, the Foulblooded（{5}{B}{B}{B}｜Legendary Creature — Demon） — Flying, trample Pay 2 life, Sacrifice another creature: Search your library for a card, put that card into your hand, then shuffle.
  5. Thrumming Stone（{5}｜Legendary Artifact） — Spells you cast have ripple 4. (Whenever you cast a spell, you may reveal the top four cards of your library. You may cast spells with the same name as that spell from am
  6. Harvester of Souls（{4}{B}{B}｜Creature — Demon） — Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.) Whenever another nontoken creature dies, you may draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}


## Toxrill, the Corrosive ｜ 腐蚀蝓怪陀袭力
- 颜色 UB ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Slug Horror
- 流行度：EDHREC 全时段第 288 位，约 9074 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 2.19 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $17.56
- 社区标签：－1/－1 指示物、控制、群体折磨、毒侵、衍生物、增殖
- 完整牌面：At the beginning of each end step, put a slime counter on each creature you don't control.
Creatures you don't control get -1/-1 for each slime counter on them.
Whenever a creature you don't control with a slime counter on it dies, create a 1/1 black Slug creature token.
{U}{B}, Sacrifice a Slug: Draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sludge Monster（{3}{U}{U}｜Creature — Horror） — Whenever this creature enters or attacks, put a slime counter on up to one other target creature. Non-Horror creatures with slime counters on them lose all abilities and 
  2. Maha, Its Feathers Night（{3}{B}{B}｜Legendary Creature — Elemental Bird） — Flying, trample Ward—Discard a card. Creatures your opponents control have base toughness 1.
  3. Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  4. Massacre Wurm（{3}{B}{B}{B}｜Creature — Phyrexian Wurm） — When this creature enters, creatures your opponents control get -2/-2 until end of turn. Whenever a creature an opponent controls dies, that player loses 2 life.
  5. Thrummingbird（{1}{U}｜Creature — Phyrexian Bird Horror） — Flying Whenever this creature deals combat damage to a player, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind a
  6. Mass Diminish（{1}{U}｜Sorcery） — Until your next turn, creatures target player controls have base power and toughness 1/1. Flashback {3}{U} (You may cast this card from your graveyard for its flashback c
- **出场率最高的牌**（大多数牌组都会放）
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Dimir Signet（{2}｜Artifact） — {1}, {T}: Add {U}{B}.
  - Drowned Catacomb（｜Land） — This land enters tapped unless you control an Island or a Swamp. {T}: Add {U} or {B}.


## Arna Kennerüd, Skycaptain ｜ 空骑士队长亚娜肯吕德
- 颜色 WUB ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Knight
- 流行度：EDHREC 全时段第 289 位，约 9018 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.42 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.41
- 社区标签：装备、灵气、主将单挑、＋1/＋1 指示物、衍生物、神器
- 完整牌面：Flying, lifelink
Ward—Discard a card.
Whenever a modified creature you control attacks, double the number of each kind of counter on it. Then for each nontoken permanent attached to it, create a token that's a copy of that permanent attached to that creature.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sram, Senior Edificer（{1}{W}｜Legendary Creature — Dwarf Advisor） — Whenever you cast an Aura, Equipment, or Vehicle spell, draw a card.
  2. Puresteel Paladin（{W}{W}｜Creature — Human Knight） — Whenever an Equipment you control enters, you may draw a card. Metalcraft — Equipment you control have equip {0} as long as you control three or more artifacts.
  3. Danitha Capashen, Paragon（{2}{W}｜Legendary Creature — Human Knight） — First strike, vigilance, lifelink Aura and Equipment spells you cast cost {1} less to cast.
  4. All That Glitters（{1}{W}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 for each artifact and/or enchantment you control.
  5. Nettlecyst（{3}｜Artifact — Equipment） — Living weapon (When this Equipment enters, create a 0/0 black Phyrexian Germ creature token, then attach this to it.) Equipped creature gets +1/+1 for each artifact and/o
  6. Thran Power Suit（{2}｜Artifact — Equipment） — Equipped creature gets +1/+1 for each Aura and Equipment attached to it and has ward {2}. (Whenever equipped creature becomes the target of a spell or ability an opponent
- **出场率最高的牌**（大多数牌组都会放）
  - Mantle of the Ancients（{3}{W}{W}｜Enchantment — Aura） — Enchant creature you control When this Aura enters, return any number of target Aura and/or Equipment cards from your graveyard to
  - Arcane Sanctum（｜Land） — This land enters tapped. {T}: Add {W}, {U}, or {B}.
  - Ardenn, Intrepid Archaeologist（{2}{W}｜Legendary Creature — Kor Scout） — At the beginning of combat on your turn, you may attach any number of Auras and Equipment you control to target permanent or playe
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.


## Raggadragga, Goreguts Boss ｜ 蛮血帮首脑拉噶达噶
- 颜色 RG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Boar
- 流行度：EDHREC 全时段第 290 位，约 9011 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.25 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.24
- 社区标签：加速、快攻、爆费、组合技、X 咒语、Mana Dorks
- 完整牌面：Each creature you control with a mana ability gets +2/+2.
Whenever a creature you control with a mana ability attacks, untap it.
Whenever you cast a spell, if at least seven mana was spent to cast it, untap target creature. It gets +7/+7 and gains trample until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Viridian Joiner（{2}{G}｜Creature — Elf Druid） — {T}: Add an amount of {G} equal to this creature's power.
  2. Marwyn, the Nurturer（{2}{G}｜Legendary Creature — Elf Druid） — Whenever another Elf you control enters, put a +1/+1 counter on Marwyn. {T}: Add an amount of {G} equal to Marwyn's power.
  3. Leyline of Abundance（{2}{G}{G}｜Enchantment） — If this card is in your opening hand, you may begin the game with it on the battlefield. Whenever you tap a creature for mana, add an additional {G}. {6}{G}{G}: Put a +1/
  4. Ruby, Daring Tracker（{R}{G}｜Legendary Creature — Human Scout） — Haste (This creature can attack and {T} as soon as it comes under your control.) Whenever Ruby attacks while you control a creature with power 4 or greater, Ruby gets +2/
  5. Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  6. Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
- **出场率最高的牌**（大多数牌组都会放）
  - Fyndhorn Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Rhythm of the Wild（{1}{R}{G}｜Enchantment） — Creature spells you control can't be countered. Nontoken creatures you control have riot. (They enter with your choice of a +1/+1 
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Beast Whisperer（{2}{G}{G}｜Creature — Elf Druid） — Whenever you cast a creature spell, draw a card.


## Minsc & Boo, Timeless Heroes ｜ 历时英雄明斯克与布布
- 颜色 RG ｜ 法术力值 4.0 ｜ 类型 Legendary Planeswalker — Minsc
- 流行度：EDHREC 全时段第 292 位，约 9006 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.54 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.04
- 社区标签：＋1/＋1 指示物、快攻、Fling、加速、烧血、大生物
- 完整牌面：When Minsc & Boo enters and at the beginning of your upkeep, you may create Boo, a legendary 1/1 red Hamster creature token with trample and haste.
+1: Put three +1/+1 counters on up to one target creature with trample or haste.
−2: Sacrifice a creature. When you do, Minsc & Boo deals X damage to any target, where X is that creature's power. If the sacrificed creature was a Hamster, draw X cards.
Minsc & Boo, Timeless Heroes can be your commander.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Taurean Mauler（{2}{R}｜Creature — Shapeshifter） — Changeling (This card is every creature type.) Whenever an opponent casts a spell, you may put a +1/+1 counter on this creature.
  2. Forgotten Ancient（{3}{G}｜Creature — Elemental） — Whenever a player casts a spell, you may put a +1/+1 counter on this creature. At the beginning of your upkeep, you may move any number of +1/+1 counters from this creatu
  3. Branching Evolution（{2}{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, twice that many +1/+1 counters are put on that creature instead.
  4. Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  5. Managorger Hydra（{2}{G}｜Creature — Hydra） — Trample Whenever a player casts a spell, put a +1/+1 counter on this creature.
  6. Fling（{1}{R}｜Instant） — As an additional cost to cast this spell, sacrifice a creature. Fling deals damage equal to the sacrificed creature's power to any target.
- **出场率最高的牌**（大多数牌组都会放）
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Goblin Anarchomancer（{R}{G}｜Creature — Goblin Shaman） — Each spell you cast that's red or green costs {1} less to cast.
  - Rootbound Crag（｜Land） — This land enters tapped unless you control a Mountain or a Forest. {T}: Add {R} or {G}.
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.


## Myrel, Shield of Argive ｜ 阿基夫之盾穆雷尔
- 颜色 W ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Soldier
- 流行度：EDHREC 全时段第 293 位，约 8995 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.91 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $18.61
- 社区标签：士兵、衍生物、快攻、＋1/＋1 指示物、锁场、人类
- 完整牌面：During your turn, your opponents can't cast spells or activate abilities of artifacts, creatures, or enchantments.
Whenever Myrel attacks, create X 1/1 colorless Soldier artifact creature tokens, where X is the number of Soldiers you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Valiant Veteran（{1}{W}｜Creature — Kor Soldier） — Other Soldiers you control get +1/+1. {3}{W}{W}, Exile this card from your graveyard: Put a +1/+1 counter on each Soldier you control.
  2. Captain of the Watch（{4}{W}{W}｜Creature — Human Soldier） — Vigilance (Attacking doesn't cause this creature to tap.) Other Soldier creatures you control get +1/+1 and have vigilance. When this creature enters, create three 1/1 wh
  3. Field Marshal（{1}{W}{W}｜Creature — Human Soldier） — Other Soldier creatures get +1/+1 and have first strike. (They deal combat damage before creatures without first strike.)
  4. Daru Warchief（{2}{W}{W}｜Creature — Human Soldier） — Soldier spells you cast cost {1} less to cast. Soldier creatures you control get +1/+2.
  5. Bastion Protector（{2}{W}｜Creature — Human Soldier） — Commander creatures you control get +2/+2 and have indestructible.
  6. Odric, Master Tactician（{2}{W}{W}｜Legendary Creature — Human Soldier） — First strike (This creature deals combat damage before creatures without first strike.) Whenever Odric and at least three other creatures attack, you choose which creatur
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Pearl Medallion（{2}｜Artifact） — White spells you cast cost {1} less to cast.
  - Mentor of the Meek（{2}{W}｜Creature — Human Soldier） — Whenever another creature you control with power 2 or less enters, you may pay {1}. If you do, draw a card.
  - Keeper of the Accord（{3}{W}｜Creature — Human Soldier） — At the beginning of each opponent's end step, if that player controls more creatures than you, create a 1/1 white Soldier creature
