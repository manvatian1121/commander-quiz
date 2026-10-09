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


## Marneus Calgar ｜ 玛尔涅斯·寇卡尔
- 颜色 WUB ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Astartes Warrior
- 流行度：EDHREC 全时段第 101 位，约 17749 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.87 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：衍生物、组合技、牺牲流、中速、控制、抽牌
- 完整牌面：Double strike
Master Tactician — Whenever one or more tokens you control enter, draw a card.
Chapter Master — {6}: Create two 2/2 white Astartes Warrior creature tokens with vigilance.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Kambal, Profiteering Mayor（{1}{W}{B}｜Legendary Creature — Human Advisor） — Whenever one or more tokens your opponents control enter, for each of them, create a tapped token that's a copy of it. This ability triggers only once each turn. Whenever
  2. Nadir Kraken（{1}{U}{U}｜Creature — Kraken） — Whenever you draw a card, you may pay {1}. If you do, put a +1/+1 counter on this creature and create a 1/1 blue Tentacle creature token.
  3. Ultramarines Honour Guard（{3}{W}｜Creature — Astartes Warrior） — Squad {2} (As an additional cost to cast this spell, you may pay {2} any number of times. When this creature enters, create that many tokens that are copies of it.) Other
  4. Ashnod's Altar（{3}｜Artifact） — Sacrifice a creature: Add {C}{C}.
  5. Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  6. Space Marine Devastator（{3}{W}｜Creature — Astartes Warrior） — Squad {2} (As an additional cost to cast this spell, you may pay {2} any number of times. When this creature enters, create that many tokens that are copies of it.) Grav-
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Progress（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {U}. This artifact deals 1 damage to you.
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.
  - Talisman of Hierarchy（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {B}. This artifact deals 1 damage to you.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Etali, Primal Conqueror // Etali, Primal Sickness ｜ 始霸埃泰力
- 颜色 RG ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Elder Dinosaur // Legendary Creature — Phyrexian Elder Dinosaur
- 流行度：EDHREC 全时段第 107 位，约 17290 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 1.65 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $28.78
- 社区标签：复制、组合技、加速、快攻、偷取、毒侵
- 完整牌面：Trample
When Etali enters, each player exiles cards from the top of their library until they exile a nonland card. You may cast any number of spells from among the nonland cards exiled this way without paying their mana costs.
{9}{G/P}: Transform Etali. Activate only as a sorcery.
//
Trample, indestructible
Whenever Etali deals combat damage to a player, they get that many poison counters. (A player with ten or more poison counters loses the game.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Twinflame（{1}{R}｜Sorcery） — Strive — This spell costs {2}{R} more to cast for each target beyond the first. Choose any number of target creatures you control. For each of them, create a token that's
  2. Electroduplicate（{2}{R}｜Sorcery） — Create a token that's a copy of target creature you control, except it has haste and "At the beginning of the end step, sacrifice this token." Flashback {2}{R}{R} (You ma
  3. Cursed Mirror（{2}{R}｜Artifact） — {T}: Add {R}. As this artifact enters, you may have it become a copy of any creature on the battlefield until end of turn, except it has haste.
  4. Jaxis, the Troublemaker（{3}{R}｜Legendary Creature — Human Warrior） — {R}, {T}, Discard a card: Create a token that's a copy of another target creature you control. It gains haste and "When this token dies, draw a card." Sacrifice it at the
  5. Heat Shimmer（{2}{R}｜Sorcery） — Create a token that's a copy of target creature, except it has haste and "At the beginning of the end step, exile this token."
  6. Hellkite Courser（{4}{R}{R}｜Creature — Dragon） — Flying When this creature enters, you may put a commander you own from the command zone onto the battlefield. It gains haste. Return it to the command zone at the beginni
- **出场率最高的牌**（大多数牌组都会放）
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Molten Duplication（{1}{R}｜Sorcery） — Create a token that's a copy of target artifact or creature you control, except it's an artifact in addition to its other types. I
  - Rionya, Fire Dancer（{3}{R}{R}｜Legendary Creature — Human Wizard） — At the beginning of combat on your turn, create X tokens that are copies of another target creature you control, where X is one pl


## Fynn, the Fangbearer ｜ 持牙人芬恩
- 颜色 G ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Warrior
- 流行度：EDHREC 全时段第 117 位，约 16258 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 1.15 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.19
- 社区标签：毒侵、死触、快攻、增殖、＋1/＋1 指示物、加速
- 完整牌面：Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)
Whenever a creature you control with deathtouch deals combat damage to a player, that player gets two poison counters. (A player with ten or more poison counters loses the game.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ambush Viper（{1}{G}｜Creature — Snake） — Flash Deathtouch
  2. Infectious Bite（{1}{G}｜Instant） — Target creature you control deals damage equal to its power to target creature you don't control. Each opponent gets a poison counter.
  3. Fang of Shigeki（{G}｜Enchantment Creature — Snake Ninja） — Deathtouch
  4. Deadly Recluse（{1}{G}｜Creature — Spider） — Reach (This creature can block creatures with flying.) Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)
  5. Moss Viper（{G}｜Creature — Snake） — Deathtouch
  6. Hornet Queen（{4}{G}{G}{G}｜Creature — Insect） — Flying, deathtouch When this creature enters, create four 1/1 green Insect creature tokens with flying and deathtouch.
- **出场率最高的牌**（大多数牌组都会放）
  - Evolution Sage（{2}{G}｜Creature — Elf Druid） — Landfall — Whenever a land you control enters, proliferate. (Choose any number of permanents and/or players, then give each anothe
  - Nightshade Dryad（{1}{G}｜Creature — Dryad） — Deathtouch {T}: Add {C}. {T}: Add one mana of any color.
  - Wasteland Viper（{G}｜Creature — Snake） — Deathtouch Bloodrush — {G}, Discard this card: Target attacking creature gets +1/+2 and gains deathtouch until end of turn.
  - Tajuru Blightblade（{G}｜Creature — Elf Rogue） — Deathtouch


## Tovolar, Dire Overlord // Tovolar, the Midnight Scourge ｜ 怖狼首领托瓦拉
- 颜色 RG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Werewolf // Legendary Creature — Werewolf
- 流行度：EDHREC 全时段第 120 位，约 15930 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.38 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.40
- 社区标签：Werewolves、快攻、狼、Day / Night、额外战斗、衍生物
- 完整牌面：Whenever a Wolf or Werewolf you control deals combat damage to a player, draw a card.
At the beginning of your upkeep, if you control three or more Wolves and/or Werewolves, it becomes night. Then transform any number of Human Werewolves you control.
Daybound
//
Whenever a Wolf or Werewolf you control deals combat damage to a player, draw a card.
{X}{R}{G}: Target Wolf or Werewolf you control gets +X/+0 and gains trample until end of turn.
Nightbound
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Kessig Naturalist（｜） — 
  2. Tovolar's Huntmaster（｜） — 
  3. Immerwolf（{1}{R}{G}｜Creature — Wolf） — Intimidate (This creature can't be blocked except by artifact creatures and/or creatures that share a color with it.) Each other creature you control that's a Wolf or a W
  4. Outland Liberator（｜） — 
  5. Mayor of Avabruck（｜） — 
  6. Howlpack Piper（｜） — 
- **出场率最高的牌**（大多数牌组都会放）
  - Huntmaster of the Fells（｜） — 
  - Avabruck Caretaker（｜） — 
  - Full Moon's Rise（{1}{G}｜Enchantment） — Werewolf creatures you control get +1/+0 and have trample. Sacrifice this enchantment: Regenerate all Werewolf creatures you contr
  - Scorned Villager（｜） — 


## Be'lakor, the Dark Master ｜ 黑暗之主比拉克尔
- 颜色 UBR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Demon Noble
- 流行度：EDHREC 全时段第 124 位，约 15660 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.24 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：恶魔、闪现回场、烧血、坟场复活、复制、飞行
- 完整牌面：Flying
Prince of Chaos — When Be'lakor enters, you draw X cards and you lose X life, where X is the number of Demons you control.
Lord of Torment — Whenever another Demon you control enters, it deals damage equal to its power to any target.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Herald of Slaanesh（{2}{R}｜Creature — Demon） — Locus of Slaanesh — Demon spells you cast cost {2} less to cast. Other Demons you control have haste.
  2. Bloodthirster（{5}{R}｜Creature — Demon） — Flying, trample Whenever this creature deals combat damage to a player, untap it. After this phase, there is an additional combat phase. This creature can't attack a play
  3. Kardur, Doomscourge（{2}{B}{R}｜Legendary Creature — Demon Berserker） — When Kardur enters, until your next turn, creatures your opponents control attack each combat if able and attack a player other than you if able. Whenever an attacking cr
  4. Rakdos, Lord of Riots（{B}{B}{R}{R}｜Legendary Creature — Demon） — You can't cast Rakdos unless an opponent lost life this turn. Flying, trample Creature spells you cast cost {1} less to cast for each 1 life your opponents have lost this
  5. Rakdos, the Showstopper（{4}{B}{R}｜Legendary Creature — Demon） — Flying, trample When Rakdos enters, flip a coin for each creature that isn't a Demon, Devil, or Imp. Destroy each creature whose coin comes up tails.
  6. Archfiend of Depravity（{3}{B}{B}｜Creature — Demon） — Flying At the beginning of each opponent's end step, that player chooses up to two creatures they control, then sacrifices the rest.
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.
  - Talisman of Indulgence（{2}｜Artifact） — {T}: Add {C}. {T}: Add {B} or {R}. This artifact deals 1 damage to you.
  - Crumbling Necropolis（｜Land） — This land enters tapped. {T}: Add {U}, {B}, or {R}.
  - Great Unclean One（{4}{B}｜Creature — Demon） — Reverberating Summons — At the beginning of your end step, each opponent loses 2 life. Then for each opponent who has less life th


## Lord of the Nazgûl ｜ 那兹古尔领主
- 颜色 UB ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Wraith Noble
- 流行度：EDHREC 全时段第 128 位，约 15242 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.39 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.87
- 社区标签：法术连发、幽灵、衍生物、小牌抽、控制、＋1/＋1 指示物
- 完整牌面：Flying
Wraiths you control have protection from Ring-bearers.
Whenever you cast an instant or sorcery spell, create a 3/3 black Wraith creature token with menace. Then if you control nine or more Wraiths, Wraiths you control have base power and toughness 9/9 until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Nazgûl（{2}{B}｜Creature — Wraith Knight） — Deathtouch When this creature enters, the Ring tempts you. Whenever the Ring tempts you, put a +1/+1 counter on each Wraith you control. A deck can have up to nine cards 
  2. Birthday Escape（{U}｜Sorcery） — Draw a card. The Ring tempts you.
  3. Call of the Ring（{1}{B}｜Enchantment） — At the beginning of your upkeep, the Ring tempts you. Whenever you choose a creature as your Ring-bearer, you may pay 2 life. If you do, draw a card.
  4. Witch-king of Angmar（{3}{B}{B}｜Legendary Creature — Wraith Noble） — Flying Whenever one or more creatures deal combat damage to you, each opponent sacrifices a creature of their choice that dealt combat damage to you this turn. The Ring t
  5. Ringsight（{1}{U}{B}｜Sorcery） — The Ring tempts you. Search your library for a card that shares a color with a legendary creature you control, reveal it, put it into your hand, then shuffle.
  6. Opt（{U}｜Instant） — Scry 1. (Look at the top card of your library. You may put that card on the bottom.) Draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Drowned Catacomb（｜Land） — This land enters tapped unless you control an Island or a Swamp. {T}: Add {U} or {B}.
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.


## Kibo, Uktabi Prince ｜ 乌克塔比王子奇博
- 颜色 RG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Monkey Noble
- 流行度：EDHREC 全时段第 132 位，约 14947 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.43 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $9.03
- 社区标签：＋1/＋1 指示物、Apes、神器、Monkeys、群体恩惠、衍生物
- 完整牌面：{T}: Each player creates a colorless artifact token named Banana with "{T}, Sacrifice this token: Add {R} or {G}. You gain 2 life."
Whenever an artifact an opponent controls is put into a graveyard from the battlefield, put a +1/+1 counter on each creature you control that's an Ape or a Monkey.
Whenever Kibo attacks, defending player sacrifices an artifact of their choice.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Viridian Revel（{1}{G}{G}｜Enchantment） — Whenever an artifact is put into an opponent's graveyard from the battlefield, you may draw a card.
  2. Gorilla Shaman（{R}｜Creature — Ape Shaman） — {X}{X}{1}: Destroy target noncreature artifact with mana value X.
  3. Silverback Elder（{2}{G}{G}{G}｜Creature — Ape Shaman） — Whenever you cast a creature spell, choose one — • Destroy target artifact or enchantment. • Look at the top five cards of your library. You may put a land card from amon
  4. Uktabi Orangutan（{2}{G}｜Creature — Ape） — When this creature enters, destroy target artifact.
  5. Kogla, the Titan Ape（{3}{G}{G}{G}｜Legendary Creature — Ape） — When Kogla enters, it fights up to one target creature you don't control. Whenever Kogla attacks, destroy target artifact or enchantment defending player controls. {1}{G}
  6. Gearbane Orangutan（{2}{R}｜Creature — Ape） — Reach When this creature enters, choose one — • Destroy up to one target artifact. • Sacrifice an artifact. If you do, put two +1/+1 counters on this creature.
- **出场率最高的牌**（大多数牌组都会放）
  - Vandalblast（{R}｜Sorcery） — Destroy target artifact you don't control. Overload {4}{R} (You may cast this spell for its overload cost. If you do, change "targ
  - Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  - Kogla and Yidaro（{2}{R}{R}{G}{G}｜Legendary Creature — Ape Dinosaur Turtle） — When Kogla and Yidaro enters, choose one — • It gains trample and haste until end of turn. • It fights target creature you don't c
  - Scrounging Bandar（{1}{G}｜Creature — Cat Monkey） — This creature enters with two +1/+1 counters on it. At the beginning of your upkeep, you may move any number of +1/+1 counters fro


## Marrow-Gnawer ｜ 啮骨牙
- 颜色 B ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Rat Rogue
- 流行度：EDHREC 全时段第 141 位，约 14352 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.58 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $31.51
- 社区标签：鼠群、老鼠、衍生物、快攻、Relentless Rats、牺牲流
- 完整牌面：All Rats have fear.
{T}, Sacrifice a Rat: Create X 1/1 black Rat creature tokens, where X is the number of Rats you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Piper of the Swarm（{1}{B}｜Creature — Human Warlock） — Rats you control have menace. {1}{B}, {T}: Create a 1/1 black Rat creature token. {2}{B}{B}, {T}, Sacrifice three Rats: Gain control of target creature.
  2. Pack Rat（{1}{B}｜Creature — Rat） — Pack Rat's power and toughness are each equal to the number of Rats you control. {2}{B}, Discard a card: Create a token that's a copy of this creature.
  3. Karumonix, the Rat King（{1}{B}{B}｜Legendary Creature — Phyrexian Rat） — Toxic 1 (Players dealt combat damage by this creature also get a poison counter.) Other Rats you control have toxic 1. When Karumonix enters, look at the top five cards o
  4. Rat Colony（{1}{B}｜Creature — Rat） — This creature gets +1/+0 for each other Rat you control. A deck can have any number of cards named Rat Colony.
  5. Ogre Slumlord（{3}{B}{B}｜Creature — Ogre Rogue） — Whenever another nontoken creature dies, you may create a 1/1 black Rat creature token. Rats you control have deathtouch.
  6. Swarmyard（｜Land） — {T}: Add {C}. {T}: Regenerate target Insect, Rat, Spider, or Squirrel. (The next time it would be destroyed this turn, instead tap it, remove it from combat, and heal all
- **出场率最高的牌**（大多数牌组都会放）
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Lord Skitter, Sewer King（{2}{B}｜Legendary Creature — Rat Noble） — Whenever another Rat you control enters, exile up to one target card from an opponent's graveyard. At the beginning of combat on y
  - Bontu's Monument（{3}｜Legendary Artifact） — Black creature spells you cast cost {1} less to cast. Whenever you cast a creature spell, each opponent loses 1 life and you gain 
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.


## Feather, the Redeemed ｜ 复耀飞羽
- 颜色 WR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Angel
- 流行度：EDHREC 全时段第 159 位，约 13487 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.9 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.06
- 社区标签：法术连发、Sunforger、主将单挑、快攻、小牌抽、烧血
- 完整牌面：Flying
Whenever you cast an instant or sorcery spell that targets a creature you control, exile that card instead of putting it into your graveyard as it resolves. If you do, return it to your hand at the beginning of the next end step.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Defiant Strike（{W}｜Instant） — Target creature gets +1/+0 until end of turn. Draw a card.
  2. Shelter（{1}{W}｜Instant） — Target creature you control gains protection from the color of your choice until end of turn. Draw a card.
  3. Expedite（{R}｜Instant） — Target creature gains haste until end of turn. Draw a card.
  4. Zada, Hedron Grinder（{3}{R}｜Legendary Creature — Goblin Ally） — Whenever you cast an instant or sorcery spell that targets only Zada, copy that spell for each other creature you control that the spell could target. Each copy targets a
  5. Fists of Flame（{1}{R}｜Instant） — Draw a card. Until end of turn, target creature gains trample and gets +1/+0 for each card you've drawn this turn. (A creature with trample can deal excess combat damage 
  6. Gods Willing（{W}｜Instant） — Target creature you control gains protection from the color of your choice until end of turn. (It can't be blocked, targeted, dealt damage, enchanted, or equipped by anyt
- **出场率最高的牌**（大多数牌组都会放）
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Storm-Kiln Artist（{3}{R}｜Creature — Dwarf Shaman） — This creature gets +1/+0 for each artifact you control. Magecraft — Whenever you cast or copy an instant or sorcery spell, create 
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Young Pyromancer（{1}{R}｜Creature — Human Shaman） — Whenever you cast an instant or sorcery spell, create a 1/1 red Elemental creature token.


## Jon Irenicus, Shattered One ｜ 破碎之人琼艾瑞尼卡斯
- 颜色 UB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Elf Wizard
- 流行度：EDHREC 全时段第 170 位，约 12985 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.78 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.35
- 社区标签：赠予、强制战斗、控制、大生物、群体折磨、毒侵
- 完整牌面：At the beginning of your end step, target opponent gains control of up to one target creature you control. Put two +1/+1 counters on it and tap it. It's goaded for the rest of the game and it gains "This creature can't be sacrificed." (It attacks each combat if able and attacks a player other than you if able.)
Whenever a creature you own but don't control attacks, you draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Flesh Reaver（{1}{B}｜Creature — Phyrexian Horror） — Whenever this creature deals damage to a creature or opponent, this creature deals that much damage to you.
  2. Abyssal Persecutor（{2}{B}{B}｜Creature — Demon） — Flying, trample You can't win the game and your opponents can't lose the game.
  3. Demonic Taskmaster（{2}{B}｜Creature — Demon） — Flying At the beginning of your upkeep, sacrifice a creature other than this creature.
  4. Archfiend of the Dross（{2}{B}{B}｜Creature — Phyrexian Demon） — Flying This creature enters with four oil counters on it. At the beginning of your upkeep, remove an oil counter from this creature. Then if it has no oil counters on it,
  5. Rotting Regisaur（{2}{B}｜Creature — Zombie Dinosaur） — At the beginning of your upkeep, discard a card.
  6. Ebon Drake（{2}{B}｜Creature — Drake） — Flying Whenever a player casts a spell, you lose 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Propaganda（{2}{U}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  - Dimir Signet（{2}｜Artifact） — {1}, {T}: Add {U}{B}.
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.


## Tivit, Seller of Secrets ｜ 密报商棣维特
- 颜色 WUB ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Sphinx Rogue
- 流行度：EDHREC 全时段第 172 位，约 12940 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 1.25 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $7.80
- 社区标签：神器、控制、组合技、政治、额外回合、闪现回场
- 完整牌面：Flying, ward {3}
Council's dilemma — Whenever Tivit enters or deals combat damage to a player, starting with you, each player votes for evidence or bribery. For each evidence vote, investigate. For each bribery vote, create a Treasure token.
While voting, you may vote an additional time. (The votes can be for different choices or for the same choice.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Time Sieve（{U}{B}｜Artifact） — {T}, Sacrifice five artifacts: Take an extra turn after this one.
  2. Academy Manufactor（{3}｜Artifact Creature — Assembly-Worker） — If you would create a Clue, Food, or Treasure token, instead create one of each.
  3. Displacer Kitten（{3}{U}｜Creature — Cat Beast） — Avoidance — Whenever you cast a noncreature spell, exile up to one target nonland permanent you control, then return that card to the battlefield under its owner's contro
  4. Illusion of Choice（{U}｜Instant） — You choose how each player votes this turn. Draw a card.
  5. Brago's Representative（{2}{W}｜Creature — Human Advisor） — While voting, you get an additional vote. (The votes can be for different choices or for the same choice.)
  6. Council's Judgment（{1}{W}{W}｜Sorcery） — Will of the council — Starting with you, each player votes for a nonland permanent you don't control. Exile each permanent with the most votes or tied for most votes.
- **出场率最高的牌**（大多数牌组都会放）
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.


## Yurlok of Scorch Thrash ｜ 焰击族的尤洛克
- 颜色 BRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Lizard Shaman
- 流行度：EDHREC 全时段第 176 位，约 12779 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.82 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.30
- 社区标签：烧血、群体折磨、群体恩惠、加速、爆费、X 咒语
- 完整牌面：Vigilance
A player losing unspent mana causes that player to lose that much life.
{1}, {T}: Each player adds {B}{R}{G}.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mana Flare（{2}{R}｜Enchantment） — Whenever a player taps a land for mana, that player adds one mana of any type that land produced.
  2. Citadel of Pain（{2}{R}｜Enchantment） — At the beginning of each player's end step, this enchantment deals X damage to that player, where X is the number of untapped lands they control.
  3. Heartbeat of Spring（{2}{G}｜Enchantment） — Whenever a player taps a land for mana, that player adds one mana of any type that land produced.
  4. Overabundance（{1}{R}{G}｜Enchantment） — Whenever a player taps a land for mana, that player adds one mana of any type that land produced, and this enchantment deals 1 damage to the player.
  5. Zhur-Taa Ancient（{3}{R}{G}｜Creature — Beast） — Whenever a player taps a land for mana, that player adds one mana of any type that land produced.
  6. Belbe, Corrupted Observer（{B}{G}｜Legendary Creature — Phyrexian Zombie Elf） — At the beginning of each postcombat main phase, the active player adds {C}{C} for each of your opponents who lost life this turn. (Damage causes loss of life.)
- **出场率最高的牌**（大多数牌组都会放）
  - Manabarbs（{3}{R}｜Enchantment） — Whenever a player taps a land for mana, this enchantment deals 1 damage to that player.
  - Horizon Stone（{5}｜Artifact） — If you would lose unspent mana, that mana becomes colorless instead.
  - Magus of the Vineyard（{G}｜Creature — Human Wizard） — At the beginning of each player's first main phase, that player adds {G}{G}.
  - Exsanguinate（{X}{B}{B}｜Sorcery） — Each opponent loses X life. You gain life equal to the life lost this way.


## Hylda of the Icy Crown ｜ 寒冰冠希尔妲
- 颜色 WU ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Warlock
- 流行度：EDHREC 全时段第 179 位，约 12615 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.58 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.54
- 社区标签：控制、横置／重置、衍生物、雪境、＋1/＋1 指示物、锁场
- 完整牌面：Whenever you tap an untapped creature an opponent controls, you may pay {1}. When you do, choose one —
• Create a 4/4 white and blue Elemental creature token.
• Put a +1/+1 counter on each creature you control.
• Scry 2, then draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Hylda's Crown of Winter（{3}｜Legendary Artifact） — {1}, {T}: Tap target creature. This ability costs {1} less to activate during your turn. {3}, Sacrifice Hylda's Crown of Winter: Draw a card for each tapped creature your
  2. Sharae of Numbing Depths（{2}{W}{U}｜Legendary Creature — Merfolk Wizard） — When Sharae enters, tap target creature an opponent controls and put a stun counter on it. (If a permanent with a stun counter would become untapped, remove one from it i
  3. Verity Circle（{2}{U}｜Enchantment） — Whenever a creature an opponent controls becomes tapped, if it isn't being declared as an attacker, you may draw a card. {4}{U}: Tap target creature without flying.
  4. Blustersquall（{U}｜Instant） — Tap target creature you don't control. Overload {3}{U} (You may cast this spell for its overload cost. If you do, change "target" in its text to "each.")
  5. Court Street Denizen（{2}{W}｜Creature — Human Soldier） — Whenever another white creature you control enters, tap target creature an opponent controls.
  6. Opposition（{2}{U}{U}｜Enchantment） — Tap an untapped creature you control: Tap target artifact, creature, or land.
- **出场率最高的牌**（大多数牌组都会放）
  - Solitary Sanctuary（{2}{W}｜Enchantment） — When this enchantment enters, tap target creature an opponent controls and put a stun counter on it. (If a permanent with a stun c
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Dreamshackle Geist（{1}{U}{U}｜Creature — Spirit） — Flying At the beginning of combat on your turn, choose up to one — • Tap target creature. • Target creature doesn't untap during i
  - Citadel Siege（{2}{W}{W}｜Enchantment） — As this enchantment enters, choose Khans or Dragons. • Khans — At the beginning of combat on your turn, put two +1/+1 counters on 


## Zedruu the Greathearted ｜ 至善赛特鲁
- 颜色 WUR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Minotaur Monk
- 流行度：EDHREC 全时段第 180 位，约 12571 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.94 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.42
- 社区标签：赠予、混乱、群体恩惠、控制、铁壁防守、生命增益
- 完整牌面：At the beginning of your upkeep, you gain X life and draw X cards, where X is the number of permanents you own that your opponents control.
{U}{R}{W}: Target opponent gains control of target permanent you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Humble Defector（{1}{R}｜Creature — Human Rogue） — {T}: Draw two cards. Target opponent gains control of this creature. Activate only during your turn.
  2. Nine Lives（{1}{W}{W}｜Enchantment） — Hexproof If a source would deal damage to you, prevent that damage and put an incarnation counter on this enchantment. When there are nine or more incarnation counters on
  3. Role Reversal（{U}{U}{R}｜Sorcery） — Exchange control of two target permanents that share a permanent type.
  4. Pendant of Prosperity（{3}｜Artifact） — This artifact enters under the control of an opponent of your choice. {2}, {T}: Draw a card, then you may put a land card from your hand onto the battlefield. This artifa
  5. Bazaar Trader（{1}{R}｜Creature — Goblin） — {T}: Target player gains control of target artifact, creature, or land you control.
  6. Akroan Horse（{4}｜Artifact Creature — Horse） — Defender When this creature enters, an opponent gains control of it. At the beginning of your upkeep, each opponent creates a 1/1 white Soldier creature token.
- **出场率最高的牌**（大多数牌组都会放）
  - Mystic Monastery（｜Land） — This land enters tapped. {T}: Add {U}, {R}, or {W}.
  - Propaganda（{2}{U}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  - Ghostly Prison（{2}{W}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  - Hithlain Rope（{2}｜Artifact） — This artifact can't be sacrificed. {1}, {T}: Search your library for a basic land card, put it onto the battlefield tapped, then s


## Arahbo, Roar of the World ｜ 震世吼阿拉博
- 颜色 WG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Cat Avatar
- 流行度：EDHREC 全时段第 196 位，约 11925 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.71 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：猫、Kaheera Companion、＋1/＋1 指示物、装备、快攻、衍生物
- 完整牌面：Eminence — At the beginning of combat on your turn, if Arahbo is in the command zone or on the battlefield, another target Cat you control gets +3/+3 until end of turn.
Whenever another Cat you control attacks, you may pay {1}{G}{W}. If you do, it gains trample and gets +X/+X until end of turn, where X is its power.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Regal Caracal（{3}{W}{W}｜Creature — Cat） — Other Cats you control get +1/+1 and have lifelink. (Damage dealt by those creatures also causes you to gain that much life.) When this creature enters, create two 1/1 wh
  2. Feline Sovereign（{2}{G}｜Creature — Cat） — Other Cats you control get +1/+1 and have protection from Dogs. Whenever one or more Cats you control deal combat damage to a player, destroy up to one target artifact or
  3. Mirri, Weatherlight Duelist（{1}{G}{W}｜Legendary Creature — Cat Warrior） — First strike Whenever Mirri attacks, each opponent can't block with more than one creature this combat. As long as Mirri is tapped, no more than one creature can attack y
  4. Arahbo, the First Fang（{2}{W}｜Legendary Creature — Cat Avatar） — Other Cats you control get +1/+1. Whenever Arahbo or another nontoken Cat you control enters, create a 1/1 white Cat creature token.
  5. King of the Pride（{2}{W}｜Creature — Cat） — Other Cats you control get +2/+1.
  6. Pride Sovereign（{2}{G}｜Creature — Cat） — This creature gets +1/+1 for each other Cat you control. {W}, {T}, Exert this creature: Create two 1/1 white Cat creature tokens with lifelink. (An exerted creature won't
- **出场率最高的牌**（大多数牌组都会放）
  - Kutzil, Malamet Exemplar（{1}{G}{W}｜Legendary Creature — Cat Warrior） — Your opponents can't cast spells during your turn. Whenever one or more creatures you control each with power greater than its bas
  - Leonin Warleader（{2}{W}{W}｜Creature — Cat Soldier） — Whenever this creature attacks, create two 1/1 white Cat creature tokens with lifelink that are tapped and attacking.
  - Qasali Slingers（{4}{G}｜Creature — Cat Warrior） — Reach Whenever this creature or another Cat you control enters, you may destroy target artifact or enchantment.
  - Brimaz, King of Oreskos（{1}{W}{W}｜Legendary Creature — Cat Soldier） — Vigilance Whenever Brimaz attacks, create a 1/1 white Cat Soldier creature token with vigilance that's attacking. Whenever Brimaz 


## Thalia and The Gitrog Monster ｜ 莎利雅与噬人蛙怪
- 颜色 WBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Frog Horror
- 流行度：EDHREC 全时段第 197 位，约 11877 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.01 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.03
- 社区标签：地牌核心、地落、衍生物、锁场、锁场小兵、加速
- 完整牌面：First strike, deathtouch
You may play an additional land on each of your turns.
Creatures and nonbasic lands your opponents control enter tapped.
Whenever Thalia and The Gitrog Monster attacks, sacrifice a creature or land, then draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ramunap Excavator（{2}{G}｜Creature — Snake Cleric） — You may play lands from your graveyard.
  2. The Gitrog Monster（{3}{B}{G}｜Legendary Creature — Frog Horror） — Deathtouch At the beginning of your upkeep, sacrifice The Gitrog Monster unless you sacrifice a land. You may play an additional land on each of your turns. Whenever one 
  3. Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create a token that's a copy of this creature i
  4. Conduit of Worlds（{2}{G}{G}｜Artifact） — You may play lands from your graveyard. {T}: Choose target nonland permanent card in your graveyard. If you haven't cast a spell this turn, you may cast that card. If you
  5. The Necrobloom（{1}{W}{B}{G}｜Legendary Creature — Plant） — Landfall — Whenever a land you control enters, create a 0/1 green Plant creature token. If you control seven or more lands with different names, create a 2/2 black Zombie
  6. Titania, Protector of Argoth（{3}{G}{G}｜Legendary Creature — Elemental） — When Titania enters, return target land card from your graveyard to the battlefield. Whenever a land you control is put into a graveyard from the battlefield, create a 5/
- **出场率最高的牌**（大多数牌组都会放）
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Windswept Heath（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Plains card, put it onto the battlefield, then shuffle.


## Derevi, Empyrial Tactician ｜ 穹光策士德蕾薇
- 颜色 WUG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Bird Wizard
- 流行度：EDHREC 全时段第 198 位，约 11823 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 1.42 ｜ 上手难度 5/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：诞生荚、组合技、飞行、闪现回场、鸟、锁场
- 完整牌面：Flying
When Derevi enters and whenever a creature you control deals combat damage to a player, you may tap or untap target permanent.
{1}{G}{W}{U}: Put Derevi onto the battlefield from the command zone.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Bloom Tender（{1}{G}｜Creature — Elf Druid） — Vivid — {T}: For each color among permanents you control, add one mana of that color.
  2. Emiel the Blessed（{2}{W}{W}｜Legendary Creature — Unicorn） — {3}: Exile another target creature you control, then return it to the battlefield under its owner's control. Whenever another creature you control enters, you may pay {G/
  3. Faeburrow Elder（{1}{G}{W}｜Creature — Treefolk Druid） — Vigilance This creature gets +1/+1 for each color among permanents you control. {T}: For each color among permanents you control, add one mana of that color.
  4. Mockingbird（{X}{U}｜Creature — Bird Bard） — Flying You may have this creature enter as a copy of any creature on the battlefield with mana value less than or equal to the amount of mana spent to cast this creature,
  5. Delney, Streetwise Lookout（{2}{W}｜Legendary Creature — Human Scout） — Creatures you control with power 2 or less can't be blocked by creatures with power 3 or greater. If a triggered ability of a creature you control with power 2 or less tr
  6. Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
- **出场率最高的牌**（大多数牌组都会放）
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Windswept Heath（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Plains card, put it onto the battlefield, then shuffle.


## Ovika, Enigma Goliath ｜ 谜样巨身兽欧威卡
- 颜色 UR ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Phyrexian Nightmare
- 流行度：EDHREC 全时段第 201 位，约 11674 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.47 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.25
- 社区标签：衍生物、法术连发、神器、鬼怪、烧血、加速
- 完整牌面：Flying
Ward—{3}, Pay 3 life.
Whenever you cast a noncreature spell, create X 1/1 red Phyrexian Goblin creature tokens, where X is the mana value of that spell. They gain haste until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  2. Shared Animosity（{2}{R}｜Enchantment） — Whenever a creature you control attacks, it gets +1/+0 until end of turn for each other attacking creature that shares a creature type with it.
  3. Distant Melody（{3}{U}｜Sorcery） — Choose a creature type. Draw a card for each permanent you control of that type.
  4. Skirk Prospector（{R}｜Creature — Goblin） — Sacrifice a Goblin: Add {R}.
  5. Heraldic Banner（{3}｜Artifact） — As this artifact enters, choose a color. Creatures you control of the chosen color get +1/+0. {T}: Add one mana of the chosen color.
  6. Hedron Archive（{4}｜Artifact） — {T}: Add {C}{C}. {2}, {T}, Sacrifice this artifact: Draw two cards.
- **出场率最高的牌**（大多数牌组都会放）
  - Izzet Signet（{2}｜Artifact） — {1}, {T}: Add {U}{R}.
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Talisman of Creativity（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {R}. This artifact deals 1 damage to you.
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.


## Saruman, the White Hand ｜ 白手萨茹曼
- 颜色 UBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Avatar Wizard
- 流行度：EDHREC 全时段第 203 位，约 11621 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.3 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.79
- 社区标签：法术连发、聚兵、僵尸、衍生物、＋1/＋1 指示物、Orcs
- 完整牌面：Whenever you cast a noncreature spell, amass Orcs X, where X is that spell's mana value. (Put X +1/+1 counters on an Army you control. It's also an Orc. If you don't control an Army, create a 0/0 black Orc Army creature token first.)
Goblins and Orcs you control have ward {2}.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Orcish Siegemaster（{2}{R}｜Creature — Orc Soldier） — Trample Other Orcs and Goblins you control have trample. Whenever this creature attacks, it gets +X/+0 until end of turn, where X is the greatest power among creatures yo
  2. Summons of Saruman（{X}{U}{R}｜Sorcery） — Amass Orcs X. Mill X cards. You may cast an instant or sorcery spell with mana value X or less from among them without paying its mana cost. (To amass Orcs X, put X +1/+1
  3. Treason of Isengard（{2}{U}｜Sorcery） — Put up to one target instant or sorcery card from your graveyard on top of your library. Amass Orcs 2. (To amass Orcs 2, put two +1/+1 counters on an Army you control. It
  4. Foray of Orcs（{3}{R}｜Sorcery） — Amass Orcs 2. When you do, Foray of Orcs deals X damage to target creature an opponent controls, where X is the amassed Army's power. (To amass Orcs 2, put two +1/+1 coun
  5. Saruman's Trickery（{1}{U}{U}｜Instant） — Counter target spell. Amass Orcs 1. (Put a +1/+1 counter on an Army you control. It's also an Orc. If you don't control an Army, create a 0/0 black Orc Army creature toke
  6. Barad-dûr（｜Legendary Land） — Barad-dûr enters tapped unless you control a legendary creature. {T}: Add {B}. {X}{X}{B}, {T}: Amass Orcs X. Activate only if a creature died this turn.
- **出场率最高的牌**（大多数牌组都会放）
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Crumbling Necropolis（｜Land） — This land enters tapped. {T}: Add {U}, {B}, or {R}.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.


## Umbris, Fear Manifest ｜ 恐惧身影乌蔽袭
- 颜色 UB ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Nightmare Horror
- 流行度：EDHREC 全时段第 204 位，约 11560 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.14 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $12.17
- 社区标签：惊惧兽、放逐、磨牌、Nightmares、主将单挑、控制
- 完整牌面：Umbris gets +1/+1 for each card your opponents own in exile.
Whenever Umbris or another Nightmare or Horror you control enters, target opponent exiles cards from the top of their library until they exile a land card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Tasha's Hideous Laughter（{1}{U}{U}｜Sorcery） — Each opponent exiles cards from the top of their library until that player has exiled cards with total mana value 20 or greater.
  2. Leyline of the Void（{2}{B}{B}｜Enchantment） — If this card is in your opening hand, you may begin the game with it on the battlefield. If a card would be put into an opponent's graveyard from anywhere, exile it inste
  3. Ashiok, Nightmare Muse（{3}{U}{B}｜Legendary Planeswalker — Ashiok） — +1: Create a 2/3 blue and black Nightmare creature token with "Whenever this token attacks or blocks, each opponent exiles the top two cards of their library." −3: Return
  4. Captain N'ghathrod（{3}{U}{B}｜Legendary Creature — Horror Pirate） — Horrors you control have menace. Whenever a Horror you control deals combat damage to a player, that player mills that many cards. At the beginning of your end step, choo
  5. Spellskite（{2}｜Artifact Creature — Phyrexian Horror） — {U/P}: Change a target of target spell or ability to this creature. ({U/P} can be paid with either {U} or 2 life.)
  6. Ashiok, Dream Render（{1}{U/B}{U/B}｜Legendary Planeswalker — Ashiok） — Spells and abilities your opponents control can't cause their controller to search their library. −1: Target player mills four cards. Then exile each opponent's graveyard
- **出场率最高的牌**（大多数牌组都会放）
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Grazilaxx, Illithid Scholar（{1}{U}{U}｜Legendary Creature — Horror） — Whenever a creature you control becomes blocked, you may return it to its owner's hand. Whenever one or more creatures you control
  - Maddening Cacophony（{1}{U}｜Sorcery） — Kicker {3}{U} Each opponent mills eight cards. If this spell was kicked, instead each opponent mills half their library, rounded u
  - Uchuulon（{3}{B}｜Creature — Crab Ooze Horror） — Uchuulon's power is equal to the number of Crabs, Oozes, and/or Horrors you control. Horrific Symbiosis — At the beginning of your


## Orvar, the All-Form ｜ 万形归一欧瓦尔
- 颜色 U ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Shapeshifter
- 流行度：EDHREC 全时段第 207 位，约 11497 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.83 ｜ 上手难度 5/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.14
- 社区标签：复制、组合技、小牌抽、法术连发、控制、衍生物
- 完整牌面：Changeling
Whenever you cast an instant or sorcery spell, if it targets one or more other permanents you control, create a token that's a copy of one of those permanents.
When a spell or ability an opponent controls causes you to discard this card, create a token that's a copy of target permanent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mind Games（{U}｜Instant） — Buyback {2}{U} (You may pay an additional {2}{U} as you cast this spell. If you do, put this card into your hand as it resolves.) Tap target artifact, creature, or land.
  2. Thermal Flux（{U}｜Instant） — Choose one — • Target nonsnow permanent becomes snow until end of turn. • Target snow permanent isn't snow until end of turn. Draw a card at the beginning of the next tur
  3. Dream's Grip（{U}｜Instant） — Choose one — • Tap target permanent. • Untap target permanent. Entwine {1} (Choose both if you pay the entwine cost.)
  4. Twiddle（{U}｜Instant） — You may tap or untap target artifact, creature, or land.
  5. Hidden Strings（{1}{U}｜Sorcery） — You may tap or untap target permanent, then you may tap or untap another target permanent. Cipher (Then you may exile this spell card encoded on a creature you control. W
  6. Vesuvan Duplimancy（{3}{U}｜Enchantment） — Whenever you cast a spell that targets only a single artifact or creature you control, create a token that's a copy of that artifact or creature, except it's not legendar
- **出场率最高的牌**（大多数牌组都会放）
  - Mystic Sanctuary（｜Land — Island） — ({T}: Add {U}.) This land enters tapped unless you control three or more other Islands. When this land enters untapped, you may pu
  - Sapphire Medallion（{2}｜Artifact） — Blue spells you cast cost {1} less to cast.
  - Archmage Emeritus（{2}{U}{U}｜Creature — Human Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, draw a card.
  - Archaeomancer（{2}{U}{U}｜Creature — Human Wizard） — When this creature enters, return target instant or sorcery card from your graveyard to your hand.


## Veyran, Voice of Duality ｜ 二元之声薇兰
- 颜色 UR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Efreet Wizard
- 流行度：EDHREC 全时段第 211 位，约 11391 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.73 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.62
- 社区标签：法术连发、风暴、烧血、咒语复制、小牌抽、组合技
- 完整牌面：Magecraft — Whenever you cast or copy an instant or sorcery spell, Veyran gets +1/+1 until end of turn.
If you casting or copying an instant or sorcery spell causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Guttersnipe（{2}{R}｜Creature — Goblin Shaman） — Whenever you cast an instant or sorcery spell, this creature deals 2 damage to each opponent.
  2. Archmage Emeritus（{2}{U}{U}｜Creature — Human Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, draw a card.
  3. Storm-Kiln Artist（{3}{R}｜Creature — Dwarf Shaman） — This creature gets +1/+0 for each artifact you control. Magecraft — Whenever you cast or copy an instant or sorcery spell, create a Treasure token. (It's an artifact with
  4. Expressive Iteration（{U}{R}｜Sorcery） — Look at the top three cards of your library. Put one of them into your hand, put one of them on the bottom of your library, and exile one of them. You may play the exiled
  5. Harmonic Prodigy（{1}{R}｜Creature — Human Wizard） — Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.) If a triggered ability of a Shaman or another Wizard you control triggers, th
  6. Opt（{U}｜Instant） — Scry 1. (Look at the top card of your library. You may put that card on the bottom.) Draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Ponder（{U}｜Sorcery） — Look at the top three cards of your library, then put them back in any order. You may shuffle. Draw a card.
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.


## Gonti, Canny Acquisitor ｜ 精明占徒贡提
- 颜色 UBG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Aetherborn Rogue
- 流行度：EDHREC 全时段第 212 位，约 11342 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.59 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.60
- 社区标签：偷取、放逐、不可阻挡、浪客、中速、快攻
- 完整牌面：Spells you cast but don't own cost {1} less to cast.
Whenever one or more creatures you control deal combat damage to a player, look at the top card of that player's library, then exile it face down. You may play that card for as long as it remains exiled, and mana of any type can be spent to cast that spell.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Thief of Sanity（{1}{U}{B}｜Creature — Specter） — Flying Whenever this creature deals combat damage to a player, look at the top three cards of that player's library, exile one of them face down, then put the rest into t
  2. Slither Blade（{U}｜Creature — Snake Rogue） — This creature can't be blocked.
  3. Doc Aurlock, Grizzled Genius（{G}{U}｜Legendary Creature — Bear Druid） — Spells you cast from your graveyard or from exile cost {2} less to cast. Plotting cards from your hand costs {2} less.
  4. Felix Five-Boots（{2}{B}{G}{U}｜Legendary Creature — Ooze Rogue） — Menace, ward {2} If a creature you control dealing combat damage to a player causes a triggered ability of a permanent you control to trigger, that ability triggers an ad
  5. Triton Shorestalker（{U}｜Creature — Merfolk Rogue） — This creature can't be blocked.
  6. Brainstealer Dragon（{5}{B}{B}｜Creature — Dragon Horror） — Flying At the beginning of your end step, exile the top card of each opponent's library. You may play those cards for as long as they remain exiled. If you cast a spell t
- **出场率最高的牌**（大多数牌组都会放）
  - Baleful Strix（{U}{B}｜Artifact Creature — Bird） — Flying, deathtouch When this creature enters, draw a card.
  - Villainous Wealth（{X}{B}{G}{U}｜Sorcery） — Target opponent exiles the top X cards of their library. You may cast any number of spells with mana value X or less from among th
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.


## Child of Alara ｜ 阿拉若之子
- 颜色 WUBRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Avatar
- 流行度：EDHREC 全时段第 214 位，约 11177 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 1.23 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.52
- 社区标签：地牌核心、Guildgates、神、加速、控制、虔诚
- 完整牌面：Trample
When Child of Alara dies, destroy all nonland permanents. They can't be regenerated.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Thespian's Stage（｜Land） — {T}: Add {C}. {2}, {T}: This land becomes a copy of target land, except it has this ability.
  2. Azusa, Lost but Seeking（{2}{G}｜Legendary Creature — Human Monk） — You may play two additional lands on each of your turns.
  3. Golgari Guildgate（｜Land — Gate） — This land enters tapped. {T}: Add {B} or {G}.
  4. Selesnya Guildgate（｜Land — Gate） — This land enters tapped. {T}: Add {G} or {W}.
  5. Simic Guildgate（｜Land — Gate） — This land enters tapped. {T}: Add {G} or {U}.
  6. Gruul Guildgate（｜Land — Gate） — This land enters tapped. {T}: Add {R} or {G}.
- **出场率最高的牌**（大多数牌组都会放）
  - The World Tree（｜Land） — This land enters tapped. {T}: Add {G}. As long as you control six or more lands, lands you control have "{T}: Add one mana of any 
  - Azorius Guildgate（｜Land — Gate） — This land enters tapped. {T}: Add {W} or {U}.
  - Dimir Guildgate（｜Land — Gate） — This land enters tapped. {T}: Add {U} or {B}.
  - Maze's End（｜Land） — This land enters tapped. {T}: Add {C}. {3}, {T}, Return this land to its owner's hand: Search your library for a Gate card, put it


## Sliver Overlord ｜ 裂片妖大王
- 颜色 WUBRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Sliver Mutant
- 流行度：EDHREC 全时段第 217 位，约 11063 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.27 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $38.69
- 社区标签：裂片妖、组合技、快攻、工具箱、衍生物、倾曳
- 完整牌面：{3}: Search your library for a Sliver card, reveal that card, put it into your hand, then shuffle.
{3}: Gain control of target Sliver. (This effect lasts indefinitely.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Gemhide Sliver（{1}{G}｜Creature — Sliver） — All Slivers have "{T}: Add one mana of any color."
  2. Sliver Hivelord（{W}{U}{B}{R}{G}｜Legendary Creature — Sliver） — Sliver creatures you control have indestructible. (Damage and effects that say "destroy" don't destroy them.)
  3. Manaweft Sliver（{1}{G}｜Creature — Sliver） — Sliver creatures you control have "{T}: Add one mana of any color."
  4. Cloudshredder Sliver（{R}{W}｜Creature — Sliver） — Sliver creatures you control have flying and haste.
  5. Crystalline Sliver（{W}{U}｜Creature — Sliver） — All Slivers have shroud. (They can't be the targets of spells or abilities.)
  6. Harmonic Sliver（{1}{G}{W}｜Creature — Sliver） — All Slivers have "When this permanent enters, destroy target artifact or enchantment."
- **出场率最高的牌**（大多数牌组都会放）
  - Sliver Legion（{W}{U}{B}{R}{G}｜Legendary Creature — Sliver） — All Sliver creatures get +1/+1 for each other Sliver on the battlefield.
  - Quick Sliver（{1}{G}｜Creature — Sliver） — Flash Any player may cast Sliver spells as though they had flash.
  - Galerider Sliver（{U}｜Creature — Sliver） — Sliver creatures you control have flying.
  - The First Sliver（{W}{U}{B}{R}{G}｜Legendary Creature — Sliver） — Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You ma


## Dihada, Binder of Wills ｜ 缚志师迪哈达
- 颜色 WBR ｜ 法术力值 4.0 ｜ 类型 Legendary Planeswalker — Dihada
- 流行度：EDHREC 全时段第 218 位，约 11061 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.68 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $13.26
- 社区标签：传奇、坟场复活、史迹、组合技、宝物、快攻
- 完整牌面：+2: Up to one target legendary creature gains vigilance, lifelink, and indestructible until your next turn.
−3: Reveal the top four cards of your library. Put any number of legendary cards from among them into your hand and the rest into your graveyard. Create a Treasure token for each card put into your graveyard this way.
−11: Gain control of all nonland permanents until end of turn. Untap them. They gain haste until end of turn.
Dihada, Binder of Wills can be your commander.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Shanid, Sleepers' Scourge（{1}{R}{W}{B}｜Legendary Creature — Human Knight） — Menace Other legendary creatures you control have menace. Whenever you play a legendary land or cast a legendary spell, you draw a card and you lose 1 life.
  2. Primevals' Glorious Rebirth（{5}{W}{B}｜Legendary Sorcery） — (You may cast a legendary sorcery only if you control a legendary creature or planeswalker.) Return all legendary permanent cards from your graveyard to the battlefield.
  3. Urza's Ruinous Blast（{4}{W}｜Legendary Sorcery） — (You may cast a legendary sorcery only if you control a legendary creature or planeswalker.) Exile all nonland permanents that aren't legendary.
  4. Odric, Lunarch Marshal（{3}{W}｜Legendary Creature — Human Soldier） — At the beginning of each combat, creatures you control gain first strike until end of turn if a creature you control has first strike. The same is true for flying, deatht
  5. Shizo, Death's Storehouse（｜Legendary Land） — {T}: Add {B}. {B}, {T}: Target legendary creature gains fear until end of turn. (It can't be blocked except by artifact creatures and/or black creatures.)
  6. Cadric, Soul Kindler（{2}{R}{W}｜Legendary Creature — Dwarf Wizard） — The "legend rule" doesn't apply to tokens you control. Whenever another nontoken legendary permanent you control enters, you may pay {1}. If you do, create a token that's
- **出场率最高的牌**（大多数牌组都会放）
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Nomad Outpost（｜Land） — This land enters tapped. {T}: Add {R}, {W}, or {B}.
  - Battlefield Forge（｜Land） — {T}: Add {C}. {T}: Add {R} or {W}. This land deals 1 damage to you.


## Ziatora, the Incinerator ｜ 焚炎魔齐朵拉
- 颜色 BRG ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Demon Dragon
- 流行度：EDHREC 全时段第 221 位，约 10951 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.35 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.67
- 社区标签：宝物、牺牲、烧血、牺牲流、Fling、坟场复活
- 完整牌面：Flying
At the beginning of your end step, you may sacrifice another creature. When you do, Ziatora deals damage equal to that creature's power to any target and you create three Treasure tokens.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Riveteers Ascendancy（{B}{R}{G}｜Enchantment） — Whenever you sacrifice a creature, you may return target creature card with lesser mana value from your graveyard to the battlefield tapped. Do this only once each turn.
  2. Yargle and Multani（{3}{B}{B}{G}｜Legendary Creature — Frog Spirit Elemental） — 
  3. Phytotitan（{4}{G}{G}｜Creature — Plant Elemental） — When this creature dies, return it to the battlefield tapped under its owner's control at the beginning of their next upkeep.
  4. Mr. Orfeo, the Boulder（{1}{B}{R}{G}｜Legendary Creature — Rhino Warrior） — Whenever you attack, double target creature's power until end of turn.
  5. Daemogoth Titan（{B/G}{B/G}{B/G}{B/G}｜Creature — Demon） — Whenever this creature attacks or blocks, sacrifice a creature.
  6. Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess combat damage to the player or planeswalker
- **出场率最高的牌**（大多数牌组都会放）
  - Ignoble Hierarch（{G}｜Creature — Goblin Shaman） — Exalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.) {T}: Add {B}, {R}, or {G}.
  - Ziatora's Proving Ground（｜Land — Swamp Mountain Forest） — ({T}: Add {B}, {R}, or {G}.) This land enters tapped. Cycling {3} ({3}, Discard this card: Draw a card.)
  - Savage Lands（｜Land） — This land enters tapped. {T}: Add {B}, {R}, or {G}.
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.


## Clavileño, First of the Blessed ｜ 受福众首克莱维诺
- 颜色 WB ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Vampire Cleric
- 流行度：EDHREC 全时段第 223 位，约 10747 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.36 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.72
- 社区标签：吸血鬼、生命增益、牺牲流、衍生物、牺牲、快攻
- 完整牌面：Whenever you attack, target attacking Vampire that isn't a Demon becomes a Demon in addition to its other types. It gains "When this creature dies, draw a card and create a tapped 4/3 white and black Vampire Demon creature token with flying."
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Cordial Vampire（{B}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, put a +1/+1 counter on each Vampire you control.
  2. Mavren Fein, Dusk Apostle（{2}{W}｜Legendary Creature — Vampire Cleric） — Whenever one or more nontoken Vampires you control attack, create a 1/1 white Vampire creature token with lifelink.
  3. Master of Dark Rites（{B}｜Creature — Vampire Cleric） — {T}, Sacrifice another creature: Add {B}{B}{B}. Spend this mana only to cast Vampire, Cleric, and/or Demon spells.
  4. Indulgent Aristocrat（{B}｜Creature — Vampire Noble） — Lifelink {2}, Sacrifice a creature: Put a +1/+1 counter on each Vampire you control.
  5. Legion Lieutenant（{W}{B}｜Creature — Vampire Knight） — Other Vampires you control get +1/+1.
  6. Olivia's Wrath（{4}{B}｜Sorcery） — Each non-Vampire creature gets -X/-X until end of turn, where X is the number of Vampires you control.
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Elenda, the Dusk Rose（{2}{W}{B}｜Legendary Creature — Vampire Knight） — Lifelink Whenever another creature dies, put a +1/+1 counter on Elenda. When Elenda dies, create X 1/1 white Vampire creature toke
  - Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  - Charismatic Conqueror（{1}{W}｜Creature — Vampire Soldier） — Vigilance Whenever an artifact or creature an opponent controls enters untapped, they may tap that permanent. If they don't, you c


## Ob Nixilis, Captive Kingpin ｜ 受困魔头欧尼希兹
- 颜色 BR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Demon
- 流行度：EDHREC 全时段第 224 位，约 10730 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.76 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $15.39
- 社区标签：组合技、烧血、＋1/＋1 指示物、风暴、群体折磨、点伤
- 完整牌面：Flying, trample
Whenever one or more opponents each lose exactly 1 life, put a +1/+1 counter on Ob Nixilis. Exile the top card of your library. Until your next end step, you may play that card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Kederekt Parasite（{B}｜Creature — Horror） — Whenever an opponent draws a card, if you control a red permanent, you may have this creature deal 1 damage to that player.
  2. Unstable Amulet（{1}{R}｜Artifact） — When this artifact enters, you get {E}{E} (two energy counters). Whenever you cast a spell from anywhere other than your hand, this artifact deals 1 damage to each oppone
  3. Razorkin Needlehead（{R}{R}｜Creature — Human Assassin） — This creature has first strike during your turn. Whenever an opponent draws a card, this creature deals 1 damage to them.
  4. Prosper, Tome-Bound（{2}{B}{R}｜Legendary Creature — Tiefling Warlock） — Deathtouch Mystic Arcanum — At the beginning of your end step, exile the top card of your library. Until the end of your next turn, you may play that card. Pact Boon — Wh
  5. Kessig Flamebreather（{1}{R}｜Creature — Human Shaman） — Whenever you cast a noncreature spell, this creature deals 1 damage to each opponent.
  6. Grapeshot（{1}{R}｜Sorcery） — Grapeshot deals 1 damage to any target. Storm (When you cast this spell, copy it for each spell cast before it this turn. You may choose new targets for the copies.)
- **出场率最高的牌**（大多数牌组都会放）
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Talisman of Indulgence（{2}｜Artifact） — {T}: Add {C}. {T}: Add {B} or {R}. This artifact deals 1 damage to you.
  - Blood Crypt（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Coruscation Mage（{1}{R}｜Creature — Otter Wizard） — Offspring {2} (You may pay an additional {2} as you cast this spell. If you do, when this creature enters, create a 1/1 token copy


## Rakdos, Lord of Riots ｜ 暴动之王拉铎司
- 颜色 BR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Demon
- 流行度：EDHREC 全时段第 227 位，约 10618 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.46 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.67
- 社区标签：烧血、快攻、恶魔、群体折磨、奥札奇、组合技
- 完整牌面：You can't cast Rakdos unless an opponent lost life this turn.
Flying, trample
Creature spells you cast cost {1} less to cast for each 1 life your opponents have lost this turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Spear Spewer（{R}｜Creature — Goblin Warrior） — Defender {T}: This creature deals 1 damage to each player.
  2. Thermo-Alchemist（{1}{R}｜Creature — Human Shaman） — Defender {T}: This creature deals 1 damage to each opponent. Whenever you cast an instant or sorcery spell, untap this creature.
  3. Stormfist Crusader（{B}{R}｜Creature — Human Knight） — Menace At the beginning of your upkeep, each player draws a card and loses 1 life.
  4. Cryptolith Fragment（｜） — 
  5. Rune-Scarred Demon（{5}{B}{B}｜Creature — Demon） — Flying When this creature enters, search your library for a card, put it into your hand, then shuffle.
  6. Creeping Bloodsucker（{1}{B}｜Creature — Vampire） — At the beginning of your upkeep, this creature deals 1 damage to each opponent. You gain life equal to the damage dealt this way.
- **出场率最高的牌**（大多数牌组都会放）
  - Rakdos Charm（{B}{R}｜Instant） — Choose one — • Exile target player's graveyard. • Destroy target artifact. • Each creature deals 1 damage to its controller.
  - Rakdos Signet（{2}｜Artifact） — {1}, {T}: Add {B}{R}.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.
