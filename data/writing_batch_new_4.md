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


## Bilbo, Birthday Celebrant ｜ 寿星比尔博
- 颜色 WBG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Halfling Rogue
- 流行度：EDHREC 全时段第 371 位，约 7540 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.16 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.32
- 社区标签：生命增益、衍生物、组合技、吸取生命、＋1/＋1 指示物、食品
- 完整牌面：If you would gain life, you gain that much life plus 1 instead.
{2}{W}{B}{G}, {T}, Exile Bilbo: Search your library for any number of creature cards, put them onto the battlefield, then shuffle. Activate only if you have 111 or more life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Soul Warden（{W}｜Creature — Human Cleric） — Whenever another creature enters, you gain 1 life.
  2. Essence Warden（{G}｜Creature — Elf Shaman） — Whenever another creature enters, you gain 1 life.
  3. Soul's Attendant（{W}｜Creature — Human Cleric） — Whenever another creature enters, you may gain 1 life.
  4. Cleric Class（{W}｜Enchantment — Class） — (Gain the next level as a sorcery to add its ability.) If you would gain life, you gain that much life plus 1 instead. {3}{W}: Level 2 Whenever you gain life, put a +1/+1
  5. Prosperous Innkeeper（{1}{G}｜Creature — Halfling Citizen） — When this creature enters, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.") Whenever another creature you control 
  6. Rhox Faithmender（{3}{W}｜Creature — Rhino Monk） — Lifelink (Damage dealt by this creature also causes you to gain that much life.) If you would gain life, you gain twice that much life instead.
- **出场率最高的牌**（大多数牌组都会放）
  - The Gaffer（{2}{W}｜Legendary Creature — Halfling Peasant） — At the beginning of each end step, if you gained 3 or more life this turn, draw a card.
  - Authority of the Consuls（{W}｜Enchantment） — Creatures your opponents control enter tapped. Whenever a creature an opponent controls enters, you gain 1 life.
  - Dina, Soul Steeper（{B}{G}｜Legendary Creature — Dryad Druid） — Whenever you gain life, each opponent loses 1 life. {1}, Sacrifice another creature: Dina gets +X/+0 until end of turn, where X is
  - Elas il-Kor, Sadistic Pilgrim（{W}{B}｜Legendary Creature — Phyrexian Kor Cleric） — Deathtouch Whenever another creature you control enters, you gain 1 life. Whenever another creature you control dies, each opponen


## Bruvac the Grandiloquent ｜ 浮夸的布鲁瓦
- 颜色 U ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Advisor
- 流行度：EDHREC 全时段第 372 位，约 7530 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 1.39 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $46.09
- 社区标签：磨牌、Persistent Petitioners、组合技、控制、Advisors、法术连发
- 完整牌面：If an opponent would mill one or more cards, they mill twice that many cards instead. (To mill a card, a player puts the top card of their library into their graveyard.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Maddening Cacophony（{1}{U}｜Sorcery） — Kicker {3}{U} Each opponent mills eight cards. If this spell was kicked, instead each opponent mills half their library, rounded up.
  2. Traumatize（{3}{U}{U}｜Sorcery） — Target player mills half their library, rounded down.
  3. Fractured Sanity（{U}{U}{U}｜Sorcery） — Each opponent mills fourteen cards. Cycling {1}{U} ({1}{U}, Discard this card: Draw a card.) When you cycle this card, each opponent mills four cards.
  4. Ruin Crab（{U}｜Creature — Crab） — Landfall — Whenever a land you control enters, each opponent mills three cards. (To mill a card, a player puts the top card of their library into their graveyard.)
  5. Cut Your Losses（{4}{U}{U}｜Sorcery） — Casualty 2 (As you cast this spell, you may sacrifice a creature with power 2 or greater. When you do, copy this spell and you may choose a new target for the copy.) Targ
  6. Memory Erosion（{1}{U}{U}｜Enchantment） — Whenever an opponent casts a spell, that player mills two cards.
- **出场率最高的牌**（大多数牌组都会放）
  - Sapphire Medallion（{2}｜Artifact） — Blue spells you cast cost {1} less to cast.
  - Propaganda（{2}{U}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  - Psychic Corrosion（{2}{U}｜Enchantment） — Whenever you draw a card, each opponent mills two cards.
  - The Mindskinner（{U}{U}{U}｜Legendary Enchantment Creature — Nightmare） — The Mindskinner can't be blocked. If a source you control would deal damage to an opponent, prevent that damage and each opponent 


## Ayula, Queen Among Bears ｜ 百熊女王阿育拉
- 颜色 G ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Bear
- 流行度：EDHREC 全时段第 373 位，约 7526 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.19 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $4.84
- 社区标签：熊、＋1/＋1 指示物、快攻、互斗、衍生物、加速
- 完整牌面：Whenever another Bear you control enters, choose one —
• Put two +1/+1 counters on target Bear.
• Target Bear you control fights target creature you don't control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Werebear（{1}{G}｜Creature — Human Bear Druid） — {T}: Add {G}. Threshold — This creature gets +3/+3 as long as there are seven or more cards in your graveyard.
  2. Mother Bear（{1}{G}｜Creature — Bear） — {3}{G}{G}, Exile this card from your graveyard: Create two 2/2 green Bear creature tokens. Activate only as a sorcery.
  3. Wilson, Refined Grizzly（{1}{G}｜Legendary Creature — Bear Warrior） — This spell can't be countered. Reach, vigilance, trample Ward {2} (Whenever this creature becomes the target of a spell or ability an opponent controls, counter it unless
  4. Ashcoat Bear（{1}{G}｜Creature — Bear） — Flash (You may cast this spell any time you could cast an instant.)
  5. Grizzly Bears（{1}{G}｜Creature — Bear） — 
  6. Owlbear Cub（{2}{G}｜Creature — Bird Bear） — Mama's Coming — Whenever this creature attacks a player who controls eight or more lands, look at the top eight cards of your library. You may put a creature card from am
- **出场率最高的牌**（大多数牌组都会放）
  - Goreclaw, Terror of Qal Sisma（{3}{G}｜Legendary Creature — Bear） — Creature spells you cast with power 4 or greater cost {2} less to cast. Whenever Goreclaw attacks, each creature you control with 
  - Runeclaw Bear（{1}{G}｜Creature — Bear） — 
  - Bear Cub（{1}{G}｜Creature — Bear） — 
  - Balduvian Bears（{1}{G}｜Creature — Bear） — 


## Kiora, Sovereign of the Deep ｜ 深洋君王奇奥拉
- 颜色 UG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Merfolk Noble
- 流行度：EDHREC 全时段第 375 位，约 7492 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.33 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.68
- 社区标签：海洋生物、加速、倾曳、爆费、大生物、中速
- 完整牌面：Vigilance, ward {3}
Whenever you cast a Kraken, Leviathan, Octopus, or Serpent spell from your hand, look at the top X cards of your library, where X is that spell's mana value. You may cast a spell with mana value less than X from among them without paying its mana cost. Put the rest on the bottom of your library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Slinn Voda, the Rising Deep（{6}{U}{U}｜Legendary Creature — Leviathan） — Kicker {1}{U} (You may pay an additional {1}{U} as you cast this spell.) When Slinn Voda enters, if it was kicked, return all creatures to their owners' hands except for 
  2. Arixmethes, Slumbering Isle（{2}{G}{U}｜Legendary Creature — Kraken） — Arixmethes enters tapped with five slumber counters on it. As long as Arixmethes has a slumber counter on it, it's a land. (It's not a creature.) Whenever you cast a spel
  3. Whelming Wave（{2}{U}{U}｜Sorcery） — Return all creatures to their owners' hands except for Krakens, Leviathans, Octopuses, and Serpents.
  4. Serpent of Yawning Depths（{4}{U}{U}｜Enchantment Creature — Serpent） — Krakens, Leviathans, Octopuses, and Serpents you control can't be blocked except by Krakens, Leviathans, Octopuses, and Serpents.
  5. Scourge of Fleets（{5}{U}{U}｜Creature — Kraken） — When this creature enters, return each creature your opponents control with toughness X or less to its owner's hand, where X is the number of Islands you control.
  6. Spawning Kraken（{5}{U}｜Creature — Kraken） — Whenever a Kraken, Leviathan, Octopus, or Serpent you control deals combat damage to a player, create a 9/9 blue Kraken creature token.
- **出场率最高的牌**（大多数牌组都会放）
  - Hullbreaker Horror（{5}{U}{U}｜Creature — Kraken Horror） — Flash This spell can't be countered. Whenever you cast a spell, choose up to one — • Return target spell you don't control to its 
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Koma, Cosmos Serpent（{3}{G}{G}{U}{U}｜Legendary Creature — Serpent） — This spell can't be countered. At the beginning of each upkeep, create a 3/3 blue Serpent creature token named Koma's Coil. Sacrif
  - Aesi, Tyrant of Gyre Strait（{4}{G}{U}｜Legendary Creature — Serpent） — You may play an additional land on each of your turns. Landfall — Whenever a land you control enters, you may draw a card.


## Pramikon, Sky Rampart ｜ 天空堡垒帕米空
- 颜色 WUR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Wall
- 流行度：EDHREC 全时段第 376 位，约 7487 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.63 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：防御力核心、铁壁防守、守军、控制、鹏洛客、强制战斗
- 完整牌面：Flying, defender
As Pramikon enters, choose left or right.
Each player may attack only the nearest opponent in the chosen direction and planeswalkers controlled by that opponent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Propaganda（{2}{U}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  2. Ghostly Prison（{2}{W}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  3. Fog Bank（{1}{U}｜Creature — Wall） — Defender (This creature can't attack.) Flying Prevent all combat damage that would be dealt to and dealt by this creature.
  4. Wall of Denial（{1}{W}{U}｜Creature — Wall） — Defender, flying Shroud (This creature can't be the target of spells or abilities.)
  5. Crystal Barricade（{1}{W}｜Artifact Creature — Wall） — Defender (This creature can't attack.) You have hexproof. (You can't be the target of spells or abilities your opponents control.) Prevent all noncombat damage that would
  6. Wall of Omens（{1}{W}｜Creature — Wall） — Defender When this creature enters, draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Mystic Monastery（｜Land） — This land enters tapped. {T}: Add {U}, {R}, or {W}.
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.


## Ezuri, Claw of Progress ｜ 进展之爪伊祖黎
- 颜色 UG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Phyrexian Elf Warrior
- 流行度：EDHREC 全时段第 377 位，约 7419 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.74 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.68
- 社区标签：＋1/＋1 指示物、毒侵、快攻、衍生物、组合技、经验指示物
- 完整牌面：Whenever a creature you control with power 2 or less enters, you get an experience counter.
At the beginning of combat on your turn, put X +1/+1 counters on another target creature you control, where X is the number of experience counters you have.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Fathom Mage（{2}{G}{U}｜Creature — Human Wizard） — Evolve (Whenever a creature you control enters, if that creature has greater power or toughness than this creature, put a +1/+1 counter on this creature.) Whenever a +1/+
  2. Champion of Lambholt（{1}{G}{G}｜Creature — Human Warrior） — Creatures with power less than this creature's power can't block creatures you control. Whenever another creature you control enters, put a +1/+1 counter on this creature
  3. Thrummingbird（{1}{U}｜Creature — Phyrexian Bird Horror） — Flying Whenever this creature deals combat damage to a player, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind a
  4. Gyre Sage（{1}{G}｜Creature — Elf Druid） — Evolve (Whenever a creature you control enters, if that creature has greater power or toughness than this creature, put a +1/+1 counter on this creature.) {T}: Add {G} fo
  5. Cold-Eyed Selkie（{1}{G/U}{G/U}｜Creature — Merfolk Rogue） — Islandwalk (This creature can't be blocked as long as defending player controls an Island.) Whenever this creature deals combat damage to a player, you may draw that many
  6. Kami of Whispered Hopes（{2}{G}｜Creature — Spirit） — If one or more +1/+1 counters would be put on a permanent you control, that many plus one +1/+1 counters are put on that permanent instead. {T}: Add X mana of any one col
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Herald of Secret Streams（{3}{U}｜Creature — Merfolk Warrior） — Creatures you control with +1/+1 counters on them can't be blocked.
  - Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.


## Ayara, First of Locthwain ｜ 洛司温首领阿娅拉
- 颜色 B ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elf Noble
- 流行度：EDHREC 全时段第 378 位，约 7389 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.41 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $8.46
- 社区标签：牺牲流、生命增益、衍生物、吸取生命、虔诚、组合技
- 完整牌面：Whenever Ayara or another black creature you control enters, each opponent loses 1 life and you gain 1 life.
{T}, Sacrifice another black creature: Draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ophiomancer（{2}{B}｜Creature — Human Shaman） — At the beginning of each upkeep, if you control no Snakes, create a 1/1 black Snake creature token with deathtouch.
  2. Zulaport Cutthroat（{1}{B}｜Creature — Human Rogue Ally） — Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life.
  3. Jadar, Ghoulcaller of Nephalia（{1}{B}｜Legendary Creature — Human Wizard） — At the beginning of your end step, if you control no creatures with decayed, create a 2/2 black Zombie creature token with decayed. (It can't block. When it attacks, sacr
  4. Abhorrent Overlord（{5}{B}{B}｜Creature — Demon） — Flying When this creature enters, create a number of 1/1 black Harpy creature tokens with flying equal to your devotion to black. (Each {B} in the mana costs of permanent
  5. Endrek Sahr, Master Breeder（{4}{B}｜Legendary Creature — Human Wizard） — Whenever you cast a creature spell, create X 1/1 black Thrull creature tokens, where X is that spell's mana value. When you control seven or more Thrulls, sacrifice Endre
  6. Reassembling Skeleton（{1}{B}｜Creature — Skeleton Warrior） — {1}{B}: Return this card from your graveyard to the battlefield tapped.
- **出场率最高的牌**（大多数牌组都会放）
  - Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost thi
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.


## Azusa, Lost but Seeking ｜ 云游者梓纱
- 颜色 G ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Monk
- 流行度：EDHREC 全时段第 379 位，约 7386 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.91 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $12.45
- 社区标签：地牌核心、加速、地落、炸地、组合技、爆费
- 完整牌面：You may play two additional lands on each of your turns.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Courser of Kruphix（{1}{G}{G}｜Enchantment Creature — Centaur） — Play with the top card of your library revealed. You may play lands from the top of your library. Landfall — Whenever a land you control enters, you gain 1 life.
  2. Ramunap Excavator（{2}{G}｜Creature — Snake Cleric） — You may play lands from your graveyard.
  3. Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create a token that's a copy of this creature i
  4. Horn of Greed（{3}｜Artifact） — Whenever a player plays a land, that player draws a card.
  5. Oracle of Mul Daya（{3}{G}｜Creature — Elf Shaman） — You may play an additional land on each of your turns. Play with the top card of your library revealed. You may play lands from the top of your library.
  6. Avenger of Zendikar（{5}{G}{G}｜Creature — Elemental） — When this creature enters, create a 0/1 green Plant creature token for each land you control. Landfall — Whenever a land you control enters, you may put a +1/+1 counter o
- **出场率最高的牌**（大多数牌组都会放）
  - Rampaging Baloths（{4}{G}{G}｜Creature — Beast） — Trample Landfall — Whenever a land you control enters, create a 4/4 green Beast creature token.
  - Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  - Tireless Tracker（{2}{G}｜Creature — Human Scout） — Landfall — Whenever a land you control enters, investigate. (Create a Clue token. It's an artifact with "{2}, Sacrifice this token
  - Augur of Autumn（{1}{G}{G}｜Creature — Human Druid） — You may look at the top card of your library any time. You may play lands from the top of your library. Coven — As long as you con


## Laughing Jasper Flint ｜ 笑面客燧火贾斯珀
- 颜色 BR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Lizard Rogue
- 流行度：EDHREC 全时段第 384 位，约 7294 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.54 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.39
- 社区标签：偷取、宝物、Outlaws、放逐、Crime、快攻
- 完整牌面：Creatures you control but don't own are Mercenaries in addition to their other types.
At the beginning of your upkeep, exile the top X cards of target opponent's library, where X is the number of outlaws you control. Until end of turn, you may cast spells from among those cards, and mana of any type can be spent to cast those spells.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. At Knifepoint（{1}{B}{R}｜Enchantment） — During your turn, outlaws you control have first strike. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks are outlaws.) Whenever you commit a crime, create a 1/1 re
  2. Hellspur Posse Boss（{2}{R}{R}｜Creature — Lizard Rogue） — Other outlaws you control have haste. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks are outlaws.) When this creature enters, create two 1/1 red Mercenary creatur
  3. Vial Smasher, Gleeful Grenadier（{B}{R}｜Legendary Creature — Goblin Mercenary） — Whenever another outlaw you control enters, Vial Smasher deals 1 damage to target opponent. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks are outlaws.)
  4. Mari, the Killing Quill（{1}{B}{B}｜Legendary Creature — Vampire Assassin） — Whenever a creature an opponent controls dies, exile it with a hit counter on it. Assassins, Mercenaries, and Rogues you control have deathtouch and "Whenever this creatu
  5. Back in Town（{X}{2}{B}｜Sorcery） — Return X target outlaw creature cards from your graveyard to the battlefield. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks are outlaws.)
  6. Grenzo, Havoc Raiser（{R}{R}｜Legendary Creature — Goblin Rogue） — Whenever a creature you control deals combat damage to a player, choose one — • Goad target creature that player controls. • Exile the top card of that player's library. 
- **出场率最高的牌**（大多数牌组都会放）
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Shoot the Sheriff（{1}{B}｜Instant） — Destroy target non-outlaw creature. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks are outlaws. Everyone else is fair game
  - Rakish Crew（{2}{B}｜Enchantment） — When this enchantment enters, create a 1/1 red Mercenary creature token with "{T}: Target creature you control gets +1/+0 until en


## Grolnok, the Omnivore ｜ 全能噬蛙葛诺克
- 颜色 UG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Frog
- 流行度：EDHREC 全时段第 387 位，约 7268 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.47 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.55
- 社区标签：蛙、磨牌、自磨、＋1/＋1 指示物、组合技、放逐
- 完整牌面：Whenever a Frog you control attacks, mill three cards.
Whenever a permanent card is put into your graveyard from your library, exile it with a croak counter on it.
You may play lands and cast spells from among cards you own in exile with croak counters on them.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Spore Frog（{G}｜Creature — Frog） — Sacrifice this creature: Prevent all combat damage that would be dealt this turn.
  2. Poison Dart Frog（{1}{G}｜Creature — Frog） — Reach {T}: Add one mana of any color. {2}: This creature gains deathtouch until end of turn.
  3. Long River Lurker（{2}{U}｜Creature — Frog Scout） — Ward {1} Other Frogs you control have ward {1}. When this creature enters, target creature you control can't be blocked this turn. Whenever that creature deals combat dam
  4. Doc Aurlock, Grizzled Genius（{G}{U}｜Legendary Creature — Bear Druid） — Spells you cast from your graveyard or from exile cost {2} less to cast. Plotting cards from your hand costs {2} less.
  5. Rampant Frogantua（{2}{G}｜Creature — Frog） — Trample This creature gets +10/+10 for each player who has lost the game. Whenever this creature deals combat damage to a player, you may mill that many cards. Put any nu
  6. Froghemoth（{3}{G}{G}｜Creature — Frog Horror） — Trample, haste Whenever this creature deals combat damage to a player, exile up to that many target cards from their graveyard. Put a +1/+1 counter on this creature for e
- **出场率最高的牌**（大多数牌组都会放）
  - Frogify（{1}{U}｜Enchantment — Aura） — Enchant creature Enchanted creature loses all abilities and is a blue Frog creature with base power and toughness 1/1. (It loses a
  - Valley Mightcaller（{G}｜Creature — Frog Warrior） — Trample Whenever another Frog, Rabbit, Raccoon, or Squirrel you control enters, put a +1/+1 counter on this creature.
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Pond Prophet（{G/U}{G/U}｜Creature — Frog Advisor） — When this creature enters, draw a card.


## Yawgmoth, Thran Physician ｜ 索蓝医师约格莫夫
- 颜色 B ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Cleric
- 流行度：EDHREC 全时段第 388 位，约 7238 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 1.15 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $28.56
- 社区标签：牺牲流、－1/－1 指示物、组合技、坟场复活、牺牲、控制
- 完整牌面：Protection from Humans
Pay 1 life, Sacrifice another creature: Put a -1/-1 counter on up to one target creature and draw a card.
{B}{B}, Discard a card: Proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Nest of Scarabs（{2}{B}｜Enchantment） — Whenever you put one or more -1/-1 counters on a creature, create that many 1/1 black Insect creature tokens.
  2. Butcher Ghoul（{1}{B}｜Creature — Zombie） — Undying (When this creature dies, if it had no +1/+1 counters on it, return it to the battlefield under its owner's control with a +1/+1 counter on it.)
  3. Geralf's Messenger（{B}{B}{B}｜Creature — Zombie） — This creature enters tapped. When this creature enters, target opponent loses 2 life. Undying (When this creature dies, if it had no +1/+1 counters on it, return it to th
  4. Zulaport Cutthroat（{1}{B}｜Creature — Human Rogue Ally） — Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life.
  5. Pawn of Ulamog（{1}{B}{B}｜Creature — Vampire Shaman） — Whenever this creature or another nontoken creature you control dies, you may create a 0/1 colorless Eldrazi Spawn creature token. It has "Sacrifice this token: Add {C}."
  6. Ophiomancer（{2}{B}｜Creature — Human Shaman） — At the beginning of each upkeep, if you control no Snakes, create a 1/1 black Snake creature token with deathtouch.
- **出场率最高的牌**（大多数牌组都会放）
  - Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Pitiless Plunderer（{3}{B}｜Creature — Human Pirate） — Whenever another creature you control dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one ma


## Jhoira, Weatherlight Captain ｜ 晴空号船长尤依拉
- 颜色 UR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Artificer
- 流行度：EDHREC 全时段第 394 位，约 7156 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 0.72 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.40
- 社区标签：神器、风暴、组合技、史迹、零费神器流、抽牌
- 完整牌面：Whenever you cast a historic spell, draw a card. (Artifacts, legendaries, and Sagas are historic.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Etherium Sculptor（{1}{U}｜Artifact Creature — Vedalken Artificer） — Artifact spells you cast cost {1} less to cast.
  2. Foundry Inspector（{3}｜Artifact Creature — Construct） — Artifact spells you cast cost {1} less to cast.
  3. Enthusiastic Mechanaut（{U}{R}｜Artifact Creature — Goblin Artificer） — Flying Artifact spells you cast cost {1} less to cast.
  4. Mystic Forge（{4}｜Artifact） — You may look at the top card of your library any time. You may cast artifact spells and colorless spells from the top of your library. {T}, Pay 1 life: Exile the top card
  5. Tormod's Crypt（{0}｜Artifact） — {T}, Sacrifice this artifact: Exile target player's graveyard.
  6. Ornithopter（{0}｜Artifact Creature — Thopter） — Flying
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Creativity（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {R}. This artifact deals 1 damage to you.
  - Izzet Signet（{2}｜Artifact） — {1}, {T}: Add {U}{R}.
  - Everflowing Chalice（{0}｜Artifact） — Multikicker {2} (You may pay an additional {2} any number of times as you cast this spell.) This artifact enters with a charge cou
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.


## Kwain, Itinerant Meddler ｜ 漫游捣乱者快隐
- 颜色 WU ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Rabbit Wizard
- 流行度：EDHREC 全时段第 395 位，约 7148 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.25 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.43
- 社区标签：群体恩惠、换手牌、抽牌、控制、铁壁防守、组合技
- 完整牌面：{T}: Each player may draw a card, then each player who drew a card this way gains 1 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Howling Mine（{2}｜Artifact） — At the beginning of each player's draw step, if this artifact is untapped, that player draws an additional card.
  2. Dictate of Kruphix（{1}{U}{U}｜Enchantment） — Flash (You may cast this spell any time you could cast an instant.) At the beginning of each player's draw step, that player draws an additional card.
  3. Kami of the Crescent Moon（{U}{U}｜Legendary Creature — Spirit） — At the beginning of each player's draw step, that player draws an additional card.
  4. Temple Bell（{3}｜Artifact） — {T}: Each player draws a card.
  5. Laboratory Maniac（{2}{U}｜Creature — Human Wizard） — If you would draw a card while your library has no cards in it, you win the game instead.
  6. Folio of Fancies（{1}{U}｜Artifact — Book） — Players have no maximum hand size. {X}{X}, {T}: Each player draws X cards. {2}{U}, {T}: Each opponent mills cards equal to the number of cards in their hand.
- **出场率最高的牌**（大多数牌组都会放）
  - Prairie Stream（｜Land — Plains Island） — ({T}: Add {W} or {U}.) This land enters tapped unless you control two or more basic lands.
  - Propaganda（{2}{U}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Ghostly Prison（{2}{W}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.


## Wayta, Trainer Prodigy ｜ 驯龙逸才薇塔
- 颜色 WRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Warrior
- 流行度：EDHREC 全时段第 397 位，约 7120 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.2 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.39
- 社区标签：Enrage、恐龙、互斗、烧血、组合技、自伤
- 完整牌面：Haste
{2}{G}, {T}: Target creature you control fights another target creature. This ability costs {2} less to activate if it targets two creatures you control.
If a creature you control being dealt damage causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ripjaw Raptor（{2}{G}{G}｜Creature — Dinosaur） — Enrage — Whenever this creature is dealt damage, draw a card.
  2. Ranging Raptors（{2}{G}｜Creature — Dinosaur） — Enrage — Whenever this creature is dealt damage, you may search your library for a basic land card, put it onto the battlefield tapped, then shuffle.
  3. Brash Taunter（{4}{R}｜Creature — Goblin） — Indestructible Whenever this creature is dealt damage, it deals that much damage to target opponent. {2}{R}, {T}: This creature fights another target creature.
  4. Cacophodon（{3}{G}｜Creature — Dinosaur） — Enrage — Whenever this creature is dealt damage, untap target permanent.
  5. Rite of Passage（{2}{G}｜Enchantment） — Whenever a creature you control is dealt damage, put a +1/+1 counter on it. (It must survive the damage to get the counter.)
  6. Bellowing Aegisaur（{5}{W}｜Creature — Dinosaur） — Enrage — Whenever this creature is dealt damage, put a +1/+1 counter on each other creature you control.
- **出场率最高的牌**（大多数牌组都会放）
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.
  - Wrathful Raptors（{4}{R}｜Creature — Dinosaur） — Trample Whenever a Dinosaur you control is dealt damage, it deals that much damage to any target that isn't a Dinosaur.
  - Silverclad Ferocidons（{5}{R}{R}｜Creature — Dinosaur） — Enrage — Whenever this creature is dealt damage, each opponent sacrifices a permanent of their choice.
  - Marauding Raptor（{1}{R}｜Creature — Dinosaur） — Creature spells you cast cost {1} less to cast. Whenever another creature you control enters, this creature deals 2 damage to it. 


## Marisi, Breaker of the Coil ｜ 破围马力希
- 颜色 WRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Cat Warrior
- 流行度：EDHREC 全时段第 399 位，约 7097 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.76 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：强制战斗、快攻、猫、衍生物、＋1/＋1 指示物、锁场
- 完整牌面：Your opponents can't cast spells during combat.
Whenever a creature you control deals combat damage to a player, goad each creature that player controls. (Until your next turn, those creatures attack each combat if able and attack a player other than you if able.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Vengeful Ancestor（{2}{R}{R}｜Creature — Spirit Dragon） — Flying Whenever this creature enters or attacks, goad target creature. (Until your next turn, that creature attacks each combat if able and attacks a player other than yo
  2. Disrupt Decorum（{2}{R}{R}｜Sorcery） — Goad all creatures you don't control. (Until your next turn, those creatures attack each combat if able and attack a player other than you if able.)
  3. Mirri, Weatherlight Duelist（{1}{G}{W}｜Legendary Creature — Cat Warrior） — First strike Whenever Mirri attacks, each opponent can't block with more than one creature this combat. As long as Mirri is tapped, no more than one creature can attack y
  4. Ohran Frostfang（{3}{G}{G}｜Snow Creature — Snake） — Attacking creatures you control have deathtouch. Whenever a creature you control deals combat damage to a player, draw a card.
  5. Toski, Bearer of Secrets（{3}{G}｜Legendary Creature — Squirrel） — This spell can't be countered. Indestructible Toski attacks each combat if able. Whenever a creature you control deals combat damage to a player, draw a card.
  6. Aurelia, the Law Above（{3}{R}{W}｜Legendary Creature — Angel） — Flying, vigilance, haste Whenever a player attacks with three or more creatures, you draw a card. Whenever a player attacks with five or more creatures, Aurelia deals 3 d
- **出场率最高的牌**（大多数牌组都会放）
  - Jungle Shrine（｜Land） — This land enters tapped. {T}: Add {R}, {G}, or {W}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.


## Chishiro, the Shattered Blade ｜ 碎剑治郎
- 颜色 RG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Snake Samurai
- 流行度：EDHREC 全时段第 404 位，约 7026 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.39 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.90
- 社区标签：＋1/＋1 指示物、装备、灵气、衍生物、快攻、结界流
- 完整牌面：Whenever an Aura or Equipment you control enters, create a 2/2 red Spirit creature token with menace.
At the beginning of your end step, put a +1/+1 counter on each modified creature you control. (Equipment, Auras you control, and counters are modifications.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Bear Umbra（{2}{G}{G}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +2/+2 and has "Whenever this creature attacks, untap all lands you control." Umbra armor (If enchanted creature would be destroye
  2. Grumgully, the Generous（{1}{R}{G}｜Legendary Creature — Goblin Shaman） — Each other non-Human creature you control enters with an additional +1/+1 counter on it.
  3. Champion of Lambholt（{1}{G}{G}｜Creature — Human Warrior） — Creatures with power less than this creature's power can't block creatures you control. Whenever another creature you control enters, put a +1/+1 counter on this creature
  4. Akki Battle Squad（{5}{R}｜Creature — Goblin Samurai） — Whenever one or more modified creatures you control attack, untap all modified creatures you control. After this phase, there is an additional combat phase. This ability 
  5. Silkguard（{X}{G}｜Instant） — Put a +1/+1 counter on each of up to X target creatures you control. Auras, Equipment, and modified creatures you control gain hexproof until end of turn. (Equipment, Aur
  6. Snake Umbra（{2}{G}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 and has "Whenever this creature deals damage to an opponent, you may draw a card." Umbra armor (If enchanted creature would
- **出场率最高的牌**（大多数牌组都会放）
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Game Trail（｜Land） — As this land enters, you may reveal a Mountain or Forest card from your hand. If you don't, this land enters tapped. {T}: Add {R} 
  - Rhythm of the Wild（{1}{R}{G}｜Enchantment） — Creature spells you control can't be countered. Nontoken creatures you control have riot. (They enter with your choice of a +1/+1 
  - Forgotten Ancient（{3}{G}｜Creature — Elemental） — Whenever a player casts a spell, you may put a +1/+1 counter on this creature. At the beginning of your upkeep, you may move any n


## Astarion, the Decadent ｜ 颓废的阿斯代伦
- 颜色 WB ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Vampire Elf Rogue
- 流行度：EDHREC 全时段第 405 位，约 7006 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.36 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.71
- 社区标签：生命增益、吸血鬼、吸取生命、组合技、自伤、牺牲流
- 完整牌面：Deathtouch, lifelink
At the beginning of your end step, choose one —
• Feed — Target opponent loses life equal to the amount of life they lost this turn.
• Friends — You gain life equal to the amount of life you gained this turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sanguine Bond（{3}{B}{B}｜Enchantment） — Whenever you gain life, target opponent loses that much life.
  2. Exquisite Blood（{4}{B}｜Enchantment） — Whenever an opponent loses life, you gain that much life.
  3. Marauding Blight-Priest（{2}{B}｜Creature — Vampire Cleric） — Whenever you gain life, each opponent loses 1 life.
  4. Exsanguinate（{X}{B}{B}｜Sorcery） — Each opponent loses X life. You gain life equal to the life lost this way.
  5. Astarion's Thirst（{3}{B}｜Instant） — Exile target creature. Put X +1/+1 counters on a commander creature you control, where X is the power of the creature exiled this way.
  6. Indulging Patrician（{1}{W}{B}｜Creature — Vampire Noble） — Flying Lifelink (Damage dealt by this creature also causes you to gain that much life.) At the beginning of your end step, if you gained 3 or more life this turn, each op
- **出场率最高的牌**（大多数牌组都会放）
  - Vito, Thorn of the Dusk Rose（{2}{B}｜Legendary Creature — Vampire Cleric） — Whenever you gain life, target opponent loses that much life. {3}{B}{B}: Creatures you control gain lifelink until end of turn.
  - Mortify（{1}{W}{B}｜Instant） — Destroy target creature or enchantment.
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Orzhov Signet（{2}｜Artifact） — {1}, {T}: Add {W}{B}.


## Ruric Thar, the Unbowed ｜ 拒降者鲁瑞杂尔
- 颜色 RG ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Ogre Warrior
- 流行度：EDHREC 全时段第 407 位，约 7000 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.79 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.56
- 社区标签：快攻、烧血、Primal Surge、锁场、加速、群体折磨
- 完整牌面：Reach, vigilance
Ruric Thar attacks each combat if able.
Whenever a player casts a noncreature spell, Ruric Thar deals 6 damage to that player.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Somberwald Sage（{2}{G}｜Creature — Human Druid） — {T}: Add three mana of any one color. Spend this mana only to cast creature spells.
  2. Beast Whisperer（{2}{G}{G}｜Creature — Elf Druid） — Whenever you cast a creature spell, draw a card.
  3. Zhur-Taa Druid（{R}{G}｜Creature — Human Druid） — {T}: Add {G}. Whenever you tap this creature for mana, it deals 1 damage to each opponent.
  4. Reclamation Sage（{2}{G}｜Creature — Elf Shaman） — When this creature enters, you may destroy target artifact or enchantment.
  5. Manglehorn（{2}{G}｜Creature — Beast） — When this creature enters, you may destroy target artifact. Artifacts your opponents control enter tapped.
  6. Scytheclaw Raptor（{2}{R}｜Creature — Dinosaur） — Whenever a player casts a spell, if it's not their turn, this creature deals 4 damage to them.
- **出场率最高的牌**（大多数牌组都会放）
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Goblin Anarchomancer（{R}{G}｜Creature — Goblin Shaman） — Each spell you cast that's red or green costs {1} less to cast.
  - Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.


## The Mimeoplasm ｜ 拟生原浆
- 颜色 UBG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Ooze
- 流行度：EDHREC 全时段第 409 位，约 6998 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.75 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.28
- 社区标签：磨牌、坟场复活、＋1/＋1 指示物、自磨、坟场、Oozes
- 完整牌面：As The Mimeoplasm enters, you may exile two creature cards from graveyards. If you do, it enters as a copy of one of those cards with a number of additional +1/+1 counters on it equal to the power of the other card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Yargle and Multani（{3}{B}{B}{G}｜Legendary Creature — Frog Spirit Elemental） — 
  2. Buried Alive（{2}{B}｜Sorcery） — Search your library for up to three creature cards, put them into your graveyard, then shuffle.
  3. Lord of Extinction（{3}{B}{G}｜Creature — Elemental） — Lord of Extinction's power and toughness are each equal to the number of cards in all graveyards.
  4. Titanoth Rex（{7}{G}{G}｜Creature — Dinosaur Beast） — Trample Cycling {1}{G} ({1}{G}, Discard this card: Draw a card.) When you cycle this card, put a trample counter on target creature you control.
  5. Consuming Aberration（{3}{U}{B}｜Creature — Horror） — Consuming Aberration's power and toughness are each equal to the number of cards in your opponents' graveyards. Whenever you cast a spell, each opponent reveals cards fro
  6. Windfall（{2}{U}｜Sorcery） — Each player discards their hand, then draws cards equal to the greatest number of cards a player discarded this way.
- **出场率最高的牌**（大多数牌组都会放）
  - Opulent Palace（｜Land） — This land enters tapped. {T}: Add {B}, {G}, or {U}.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.


## Elenda, the Dusk Rose ｜ 暮影蔷薇依莲达
- 颜色 WB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Vampire Knight
- 流行度：EDHREC 全时段第 410 位，约 6976 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.28 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.71
- 社区标签：牺牲流、吸血鬼、生命增益、衍生物、＋1/＋1 指示物、牺牲
- 完整牌面：Lifelink
Whenever another creature dies, put a +1/+1 counter on Elenda.
When Elenda dies, create X 1/1 white Vampire creature tokens with lifelink, where X is Elenda's power.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Blade of the Bloodchief（{1}｜Artifact — Equipment） — Whenever a creature dies, put a +1/+1 counter on equipped creature. If equipped creature is a Vampire, put two +1/+1 counters on it instead. Equip {1}
  2. Cordial Vampire（{B}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, put a +1/+1 counter on each Vampire you control.
  3. Teysa Karlov（{2}{W}{B}｜Legendary Creature — Human Advisor） — If a creature dying causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time. Creature tokens you control have vigilance
  4. Cruel Celebrant（{W}{B}｜Creature — Vampire） — Whenever this creature or another creature or planeswalker you control dies, each opponent loses 1 life and you gain 1 life.
  5. Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  6. Viscera Seer（{B}｜Creature — Vampire Wizard） — Sacrifice a creature: Scry 1. (Look at the top card of your library. You may put that card on the bottom.)
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  - Orzhov Signet（{2}｜Artifact） — {1}, {T}: Add {W}{B}.
  - Tainted Field（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. Activate only if you control a Swamp.


## Juri, Master of the Revue ｜ 剧团业主裘里
- 颜色 BR ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Shaman
- 流行度：EDHREC 全时段第 412 位，约 6957 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.19 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.28
- 社区标签：宝物、牺牲、牺牲流、＋1/＋1 指示物、衍生物、烧血
- 完整牌面：Whenever you sacrifice a permanent, put a +1/+1 counter on Juri.
When Juri dies, it deals damage equal to its power to any target.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Fling（{1}{R}｜Instant） — As an additional cost to cast this spell, sacrifice a creature. Fling deals damage equal to the sacrificed creature's power to any target.
  2. Lagomos, Hand of Hatred（{1}{B}{R}｜Legendary Creature — Human Shaman） — At the beginning of combat on your turn, create a 2/1 red Elemental creature token with trample and haste. Sacrifice it at the beginning of the next end step. {T}: Search
  3. Mahadi, Emporium Master（{1}{B}{R}｜Legendary Creature — Devil） — At the beginning of your end step, create a Treasure token for each creature that died this turn. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any c
  4. Pitiless Plunderer（{3}{B}｜Creature — Human Pirate） — Whenever another creature you control dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")
  5. Impulsive Pilferer（{R}｜Creature — Goblin Pirate） — When this creature dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.") Encore {3}{R} ({3}{R}, Exile this card f
  6. Mayhem Devil（{1}{B}{R}｜Creature — Devil） — Whenever a player sacrifices a permanent, this creature deals 1 damage to any target.
- **出场率最高的牌**（大多数牌组都会放）
  - Deadly Dispute（{1}{B}｜Instant） — As an additional cost to cast this spell, sacrifice an artifact or creature. Draw two cards and create a Treasure token. (It's an 
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.
  - Viscera Seer（{B}｜Creature — Vampire Wizard） — Sacrifice a creature: Scry 1. (Look at the top card of your library. You may put that card on the bottom.)
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.


## Ixhel, Scion of Atraxa ｜ 亚崔夏赋使伊歇儿
- 颜色 WBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Phyrexian Angel
- 流行度：EDHREC 全时段第 413 位，约 6955 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.59 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.01
- 社区标签：毒侵、非瑞人、增殖、偷取、＋1/＋1 指示物、中速
- 完整牌面：Flying, vigilance, toxic 2
Corrupted — At the beginning of your end step, each opponent who has three or more poison counters exiles the top card of their library face down. You may look at and play those cards for as long as they remain exiled, and you may spend mana as though it were mana of any color to cast those spells.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Infectious Inquiry（{2}{B}｜Sorcery） — You draw two cards and you lose 2 life. Each opponent gets a poison counter.
  2. Vraska's Fall（{2}{B}｜Instant） — Each opponent sacrifices a creature or planeswalker of their choice and gets a poison counter.
  3. Contaminant Grafter（{4}{G}｜Creature — Phyrexian Druid） — Trample, toxic 1 Whenever one or more creatures you control deal combat damage to one or more players, proliferate. Corrupted — At the beginning of your end step, if an o
  4. Phyresis Outbreak（{2}{B}｜Sorcery） — Each opponent gets a poison counter. Then each creature your opponents control gets -1/-1 until end of turn for each poison counter its controller has.
  5. Vishgraz, the Doomhive（{2}{W}{B}{G}｜Legendary Creature — Phyrexian Insect） — Menace, toxic 1 (Players dealt combat damage by this creature also get a poison counter.) When Vishgraz enters, create three 1/1 colorless Phyrexian Mite artifact creatur
  6. Blightbelly Rat（{1}{B}｜Creature — Phyrexian Rat） — Toxic 1 (Players dealt combat damage by this creature also get a poison counter.) When this creature dies, proliferate. (Choose any number of permanents and/or players, t
- **出场率最高的牌**（大多数牌组都会放）
  - Karn's Bastion（｜Land） — {T}: Add {C}. {4}, {T}: Proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind 
  - Norn's Decree（{2}{W}｜Enchantment） — Whenever one or more creatures an opponent controls deal combat damage to you, that opponent gets a poison counter. Whenever a pla
  - Unnatural Restoration（{1}{G}｜Sorcery） — Return target permanent card from your graveyard to your hand. Proliferate. (Choose any number of permanents and/or players, then 
  - Venerated Rotpriest（{G}｜Creature — Phyrexian Druid） — Toxic 1 (Players dealt combat damage by this creature also get a poison counter.) Whenever a creature you control becomes the targ


## Karumonix, the Rat King ｜ 鼠王卡鲁蒙
- 颜色 B ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Phyrexian Rat
- 流行度：EDHREC 全时段第 414 位，约 6937 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.61 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.89
- 社区标签：老鼠、毒侵、鼠群、Relentless Rats、衍生物、快攻
- 完整牌面：Toxic 1 (Players dealt combat damage by this creature also get a poison counter.)
Other Rats you control have toxic 1.
When Karumonix enters, look at the top five cards of your library. You may reveal any number of Rat cards from among them and put the revealed cards into your hand. Put the rest on the bottom of your library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Blightbelly Rat（{1}{B}｜Creature — Phyrexian Rat） — Toxic 1 (Players dealt combat damage by this creature also get a poison counter.) When this creature dies, proliferate. (Choose any number of permanents and/or players, t
  2. Piper of the Swarm（{1}{B}｜Creature — Human Warlock） — Rats you control have menace. {1}{B}, {T}: Create a 1/1 black Rat creature token. {2}{B}{B}, {T}, Sacrifice three Rats: Gain control of target creature.
  3. Marrow-Gnawer（{3}{B}{B}｜Legendary Creature — Rat Rogue） — All Rats have fear. {T}, Sacrifice a Rat: Create X 1/1 black Rat creature tokens, where X is the number of Rats you control.
  4. Pack Rat（{1}{B}｜Creature — Rat） — Pack Rat's power and toughness are each equal to the number of Rats you control. {2}{B}, Discard a card: Create a token that's a copy of this creature.
  5. Ogre Slumlord（{3}{B}{B}｜Creature — Ogre Rogue） — Whenever another nontoken creature dies, you may create a 1/1 black Rat creature token. Rats you control have deathtouch.
  6. Ichor Rats（{1}{B}{B}｜Creature — Phyrexian Rat） — Infect (This creature deals damage to creatures in the form of -1/-1 counters and to players in the form of poison counters.) When this creature enters, each player gets 
- **出场率最高的牌**（大多数牌组都会放）
  - Lord Skitter, Sewer King（{2}{B}｜Legendary Creature — Rat Noble） — Whenever another Rat you control enters, exile up to one target card from an opponent's graveyard. At the beginning of combat on y
  - Infectious Inquiry（{2}{B}｜Sorcery） — You draw two cards and you lose 2 life. Each opponent gets a poison counter.
  - Typhoid Rats（{B}｜Creature — Rat） — Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)
  - Vraska's Fall（{2}{B}｜Instant） — Each opponent sacrifices a creature or planeswalker of their choice and gets a poison counter.


## Aminatou, the Fateshifter ｜ 矫命师阿米娜图
- 颜色 WUB ｜ 法术力值 3.0 ｜ 类型 Legendary Planeswalker — Aminatou
- 流行度：EDHREC 全时段第 415 位，约 6882 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.64 ｜ 上手难度 5/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $20.75
- 社区标签：闪现回场、控制、组合技、鹏洛客、牌库顶、进场触发
- 完整牌面：+1: Draw a card, then put a card from your hand on top of your library.
−1: Exile another target permanent you own, then return it to the battlefield under your control.
−6: Choose left or right. Each player gains control of all nonland permanents other than Aminatou controlled by the next player in the chosen direction.
Aminatou, the Fateshifter can be your commander.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Oath of Teferi（{3}{W}{U}｜Legendary Enchantment） — When Oath of Teferi enters, exile another target permanent you control. Return it to the battlefield under its owner's control at the beginning of the next end step. You 
  2. Felidar Guardian（{3}{W}｜Creature — Cat Beast） — When this creature enters, you may exile another target permanent you control, then return that card to the battlefield under its owner's control.
  3. Soulherder（{1}{W}{U}｜Creature — Spirit） — Whenever a creature is exiled from the battlefield, put a +1/+1 counter on this creature. At the beginning of your end step, you may exile another target creature you con
  4. Ephemerate（{W}｜Instant） — Exile target creature you control, then return it to the battlefield under its owner's control. Rebound (If you cast this spell from your hand, exile it as it resolves. A
  5. Peregrine Drake（{4}{U}｜Creature — Drake） — Flying When this creature enters, untap up to five lands.
  6. Panharmonicon（{4}｜Artifact） — If an artifact or creature entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
- **出场率最高的牌**（大多数牌组都会放）
  - Baleful Strix（{U}{B}｜Artifact Creature — Bird） — Flying, deathtouch When this creature enters, draw a card.
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Kambal, Profiteering Mayor ｜ 牟利镇长坎拔
- 颜色 WB ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Advisor
- 流行度：EDHREC 全时段第 416 位，约 6873 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.6 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.53
- 社区标签：衍生物、牺牲流、生命增益、吸取生命、群体恩惠、宝物
- 完整牌面：Whenever one or more tokens your opponents control enter, for each of them, create a tapped token that's a copy of it. This ability triggers only once each turn.
Whenever one or more tokens you control enter, each opponent loses 1 life and you gain 1 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Marching Duodrone（{2}｜Artifact Creature — Construct） — Whenever this creature attacks, each player creates a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")
  2. Mirkwood Bats（{3}{B}｜Creature — Bat） — Flying Whenever you create or sacrifice a token, each opponent loses 1 life.
  3. Bovine Intervention（{1}{W}｜Instant） — Destroy target artifact or creature. Its controller creates a 2/2 white Ox creature token.
  4. Hunted Horror（{B}{B}｜Creature — Horror） — Trample When this creature enters, target opponent creates two 3/3 green Centaur creature tokens with protection from black.
  5. Bennie Bracks, Zoologist（{3}{W}｜Legendary Creature — Elf Druid） — Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.) At the beginning of e
  6. Thalisse, Reverent Medium（{3}{W}{B}｜Legendary Creature — Human Cleric） — At the beginning of each end step, create X 1/1 white Spirit creature tokens with flying, where X is the number of tokens you created this turn.
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Elas il-Kor, Sadistic Pilgrim（{W}{B}｜Legendary Creature — Phyrexian Kor Cleric） — Deathtouch Whenever another creature you control enters, you gain 1 life. Whenever another creature you control dies, each opponen
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}


## Nahiri, Forged in Fury ｜ 怒火熔铸娜希丽
- 颜色 WR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Kor Artificer
- 流行度：EDHREC 全时段第 417 位，约 6868 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.46 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $8.04
- 社区标签：装备、快攻、主将单挑、神器、衍生物、神器共鸣
- 完整牌面：Affinity for Equipment (This spell costs {1} less to cast for each Equipment you control.)
Whenever an equipped creature you control attacks, exile the top card of your library. You may play that card this turn. You may cast Equipment spells this way without paying their mana costs.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Bladehold War-Whip（{1}{R}{W}｜Artifact — Equipment） — For Mirrodin! (When this Equipment enters, create a 2/2 red Rebel creature token, then attach this to it.) Equip abilities you activate of other Equipment cost {1} less t
  2. Puresteel Paladin（{W}{W}｜Creature — Human Knight） — Whenever an Equipment you control enters, you may draw a card. Metalcraft — Equipment you control have equip {0} as long as you control three or more artifacts.
  3. Nettlecyst（{3}｜Artifact — Equipment） — Living weapon (When this Equipment enters, create a 0/0 black Phyrexian Germ creature token, then attach this to it.) Equipped creature gets +1/+1 for each artifact and/o
  4. Sram, Senior Edificer（{1}{W}｜Legendary Creature — Dwarf Advisor） — Whenever you cast an Aura, Equipment, or Vehicle spell, draw a card.
  5. Kaldra Compleat（{7}｜Legendary Artifact — Equipment） — Living weapon Indestructible Equipped creature gets +5/+5 and has first strike, trample, indestructible, haste, and "Whenever this creature deals combat damage to a creat
  6. Akiri, Fearless Voyager（{1}{R}{W}｜Legendary Creature — Kor Warrior） — Whenever you attack a player with one or more equipped creatures, draw a card. {W}: You may unattach an Equipment from a creature you control. If you do, tap that creatur
- **出场率最高的牌**（大多数牌组都会放）
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Sigarda's Aid（{W}｜Enchantment） — You may cast Aura and Equipment spells as though they had flash. Whenever an Equipment you control enters, you may attach it to ta
  - Forge Anew（{2}{W}｜Enchantment） — When this enchantment enters, return target Equipment card from your graveyard to the battlefield. During your turn, you may activ
  - Bruenor Battlehammer（{2}{R}{W}｜Legendary Creature — Dwarf Warrior） — Each creature you control gets +2/+0 for each Equipment attached to it. You may pay {0} rather than pay the equip cost of the firs


## Yusri, Fortune's Flame ｜ 命运烈焰亚司利
- 颜色 UR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Efreet
- 流行度：EDHREC 全时段第 419 位，约 6846 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.39 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.33
- 社区标签：混乱、掷硬币、法术连发、组合技、抽牌、风暴
- 完整牌面：Flying
Whenever Yusri attacks, choose a number between 1 and 5. Flip that many coins. For each flip you win, draw a card. For each flip you lose, Yusri deals 2 damage to you. If you won five flips this way, you may cast spells from your hand this turn without paying their mana costs.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Tavern Scoundrel（{1}{R}｜Creature — Human Rogue） — Whenever you win a coin flip, create two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: Add one mana of any color.") {1}, {T}, Sacrifice another per
  2. Krark's Thumb（{2}｜Legendary Artifact） — If you would flip a coin, instead flip two coins and ignore one.
  3. Zndrsplt, Eye of Wisdom（{4}{U}｜Legendary Creature — Homunculus） — Partner with Okaun, Eye of Chaos (When this creature enters, target player may put Okaun into their hand from their library, then shuffle.) At the beginning of combat on 
  4. Chance Encounter（{2}{R}{R}｜Enchantment） — Whenever you win a coin flip, put a luck counter on this enchantment. At the beginning of your upkeep, if this enchantment has ten or more luck counters on it, you win th
  5. Stitch in Time（{1}{U}{R}｜Sorcery） — Flip a coin. If you win the flip, take an extra turn after this one.
  6. Okaun, Eye of Chaos（{4}{R}｜Legendary Creature — Cyclops Berserker） — Partner with Zndrsplt, Eye of Wisdom (When this creature enters, target player may put Zndrsplt into their hand from their library, then shuffle.) At the beginning of com
- **出场率最高的牌**（大多数牌组都会放）
  - Fiery Gambit（{2}{R}｜Sorcery） — Flip a coin until you lose a flip or choose to stop flipping. If you lose a flip, Fiery Gambit has no effect. If you win one or mo
  - Invert Polarity（{U}{U}{R}｜Instant） — Choose target spell, then flip a coin. If you win the flip, gain control of that spell and you may choose new targets for it. If y
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Krark, the Thumbless（{1}{R}｜Legendary Creature — Goblin Wizard） — Whenever you cast an instant or sorcery spell, flip a coin. If you lose the flip, return that spell to its owner's hand. If you wi


## The Locust God ｜ 蝗虫神
- 颜色 UR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — God
- 流行度：EDHREC 全时段第 421 位，约 6838 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.81 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $7.42
- 社区标签：换手牌、衍生物、抽牌、组合技、法术连发、烧血
- 完整牌面：Flying
Whenever you draw a card, create a 1/1 blue and red Insect creature token with flying and haste.
{2}{U}{R}: Draw a card, then discard a card.
When The Locust God dies, return it to its owner's hand at the beginning of the next end step.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  2. Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  3. Psychosis Crawler（{5}｜Artifact Creature — Phyrexian Horror） — Psychosis Crawler's power and toughness are each equal to the number of cards in your hand. Whenever you draw a card, each opponent loses 1 life.
  4. Whirlpool Warrior（{2}{U}｜Creature — Merfolk Warrior） — When this creature enters, shuffle the cards from your hand into your library, then draw that many cards. {R}, Sacrifice this creature: Each player shuffles the cards fro
  5. Teferi's Ageless Insight（{2}{U}{U}｜Legendary Enchantment） — If you would draw a card except the first one you draw in each of your draw steps, draw two cards instead.
  6. Tolarian Winds（{1}{U}｜Instant） — Discard all the cards in your hand, then draw that many cards.
- **出场率最高的牌**（大多数牌组都会放）
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  - Windfall（{2}{U}｜Sorcery） — Each player discards their hand, then draws cards equal to the greatest number of cards a player discarded this way.
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Izzet Signet（{2}｜Artifact） — {1}, {T}: Add {U}{R}.


## Brudiclad, Telchor Engineer ｜ 钛可工程师布迪凯
- 颜色 UR ｜ 法术力值 6.0 ｜ 类型 Legendary Artifact Creature — Phyrexian Artificer
- 流行度：EDHREC 全时段第 422 位，约 6821 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.36 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.32
- 社区标签：衍生物、神器、复制、宝物、组合技、增殖衍生物
- 完整牌面：Creature tokens you control have haste.
At the beginning of combat on your turn, create a 2/1 blue Phyrexian Myr artifact creature token. Then you may choose a token you control. If you do, each other token you control becomes a copy of that token.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Idol of Oblivion（{2}｜Artifact） — {T}: Draw a card. Activate only if you created a token this turn. {8}, {T}, Sacrifice this artifact: Create a 10/10 colorless Eldrazi creature token.
  2. Thopter Spy Network（{2}{U}{U}｜Enchantment） — At the beginning of your upkeep, if you control an artifact, create a 1/1 colorless Thopter artifact creature token with flying. Whenever one or more artifact creatures y
  3. Quasiduplicate（{1}{U}{U}｜Sorcery） — Create a token that's a copy of target creature you control. Jump-start (You may cast this card from your graveyard by discarding a card in addition to paying its other c
  4. Saheeli, Sublime Artificer（{1}{U/R}{U/R}｜Legendary Planeswalker — Saheeli） — Whenever you cast a noncreature spell, create a 1/1 colorless Servo artifact creature token. −2: Target artifact you control becomes a copy of another target artifact or 
  5. Cackling Counterpart（{1}{U}{U}｜Instant） — Create a token that's a copy of target creature you control. Flashback {5}{U}{U} (You may cast this card from your graveyard for its flashback cost. Then exile it.)
  6. Myr Battlesphere（{7}｜Artifact Creature — Myr Construct） — When this creature enters, create four 1/1 colorless Myr artifact creature tokens. Whenever this creature attacks, you may tap X untapped Myr you control. If you do, this
- **出场率最高的牌**（大多数牌组都会放）
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Izzet Signet（{2}｜Artifact） — {1}, {T}: Add {U}{R}.
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.
  - Third Path Iconoclast（{U}{R}｜Creature — Human Monk） — Whenever you cast a noncreature spell, create a 1/1 colorless Soldier artifact creature token.


## Emry, Lurker of the Loch ｜ 深湖潜妖艾莉
- 颜色 U ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Merfolk Wizard
- 流行度：EDHREC 全时段第 424 位，约 6803 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 0.47 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.64
- 社区标签：神器、组合技、磨牌、神器共鸣、风暴、坟场
- 完整牌面：Affinity for artifacts (This spell costs {1} less to cast for each artifact you control.)
When Emry enters, mill four cards.
{T}: Choose target artifact card in your graveyard. You may cast that card this turn. (You still pay its costs. Timing rules still apply.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mirran Spy（{2}{U}｜Creature — Drone） — Flying Whenever you cast an artifact spell, you may untap target creature.
  2. Etherium Sculptor（{1}{U}｜Artifact Creature — Vedalken Artificer） — Artifact spells you cast cost {1} less to cast.
  3. Mishra's Bauble（{0}｜Artifact） — {T}, Sacrifice this artifact: Look at the top card of target player's library. Draw a card at the beginning of the next turn's upkeep.
  4. Seat of the Synod（｜Artifact Land） — {T}: Add {U}.
  5. Aether Spellbomb（{1}｜Artifact） — {U}, Sacrifice this artifact: Return target creature to its owner's hand. {1}, Sacrifice this artifact: Draw a card.
  6. Foundry Inspector（{3}｜Artifact Creature — Construct） — Artifact spells you cast cost {1} less to cast.
- **出场率最高的牌**（大多数牌组都会放）
  - Darksteel Citadel（｜Artifact Land） — Indestructible {T}: Add {C}.
  - Sai, Master Thopterist（{2}{U}｜Legendary Creature — Human Artificer） — Whenever you cast an artifact spell, create a 1/1 colorless Thopter artifact creature token with flying. {1}{U}, Sacrifice two art
  - Fabricate（{2}{U}｜Sorcery） — Search your library for an artifact card, reveal it, put it into your hand, then shuffle.
  - Lotus Petal（{0}｜Artifact） — {T}, Sacrifice this artifact: Add one mana of any color.
