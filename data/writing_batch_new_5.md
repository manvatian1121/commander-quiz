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


## Narci, Fable Singer ｜ 寓言歌者娜尔提
- 颜色 WBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Bard
- 流行度：EDHREC 全时段第 427 位，约 6767 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.34 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：传纪、结界流、生命增益、坟场复活、吸取生命、衍生物
- 完整牌面：Lifelink
Whenever you sacrifice an enchantment, draw a card.
Whenever the final chapter ability of a Saga you control resolves, each opponent loses X life and you gain X life, where X is that Saga's mana value.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Binding the Old Gods（{2}{B}{G}｜Enchantment — Saga） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Destroy target nonland permanent an opponent controls. II — Search your libra
  2. Sythis, Harvest's Hand（{G}{W}｜Legendary Enchantment Creature — Nymph） — Whenever you cast an enchantment spell, you gain 1 life and draw a card.
  3. The Eldest Reborn（{4}{B}｜Enchantment — Saga） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Each opponent sacrifices a creature or planeswalker of their choice. II — Eac
  4. Satsuki, the Living Lore（{G}{W}｜Legendary Creature — Human Druid） — {T}: Put a lore counter on each Saga you control. Activate only as a sorcery. When Satsuki dies, choose up to one — • Return target Saga or enchantment creature you contr
  5. Elspeth Conquers Death（{3}{W}{W}｜Enchantment — Saga） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Exile target permanent an opponent controls with mana value 3 or greater. II 
  6. Sanctum Weaver（{1}{G}｜Enchantment Creature — Dryad） — {T}: Add X mana of any one color, where X is the number of enchantments you control.
- **出场率最高的牌**（大多数牌组都会放）
  - Jukai Naturalist（{G}{W}｜Enchantment Creature — Human Monk） — Lifelink Enchantment spells you cast cost {1} less to cast.
  - Enchantress's Presence（{2}{G}｜Enchantment） — Whenever you cast an enchantment spell, draw a card.
  - Setessan Champion（{2}{G}｜Creature — Human Warrior） — Constellation — Whenever an enchantment you control enters, put a +1/+1 counter on this creature and draw a card.
  - The Cruelty of Gix（{3}{B}{B}｜Enchantment — Saga） — Read ahead (Choose a chapter and start with that many lore counters. Add one after your draw step. Skipped chapters don't trigger.


## Ivy, Gleeful Spellthief ｜ 欢笑窃咒客艾薇
- 颜色 UG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Faerie Rogue
- 流行度：EDHREC 全时段第 428 位，约 6766 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.57 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.74
- 社区标签：灵气、突变、复制、结界流、主将单挑、咒语复制
- 完整牌面：Flying
Whenever a player casts a spell that targets only a single creature other than Ivy, you may copy that spell. The copy targets Ivy. (A copy of an Aura spell becomes a token.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Stormchaser Drake（{1}{U}｜Creature — Drake） — Flying Whenever this creature becomes the target of a spell you control, draw a card.
  2. Shielding Plax（{2}{G/U}｜Enchantment — Aura） — ({G/U} can be paid with either {G} or {U}.) Enchant creature When this Aura enters, draw a card. Enchanted creature can't be the target of spells or abilities your oppone
  3. Season of Growth（{1}{G}｜Enchantment） — Whenever a creature you control enters, scry 1. (Look at the top card of your library. You may put that card on the bottom.) Whenever you cast a spell that targets a crea
  4. Vesuvan Duplimancy（{3}{U}｜Enchantment） — Whenever you cast a spell that targets only a single artifact or creature you control, create a token that's a copy of that artifact or creature, except it's not legendar
  5. Combat Research（{U}｜Enchantment — Aura） — Enchant creature Enchanted creature has "Whenever this creature deals combat damage to a player, draw a card." As long as enchanted creature is legendary, it gets +1/+1 a
  6. Snake Umbra（{2}{G}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 and has "Whenever this creature deals damage to an opponent, you may draw a card." Umbra armor (If enchanted creature would
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Ancestral Mask（{2}{G}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +2/+2 for each other enchantment on the battlefield.
  - Curiosity（{U}｜Enchantment — Aura） — Enchant creature Whenever enchanted creature deals damage to an opponent, you may draw a card.
  - Gemrazer（{3}{G}｜Creature — Beast） — Mutate {1}{G}{G} (If you cast this spell for its mutate cost, put it over or under target non-Human creature you own. They mutate 


## Don Andres, the Renegade ｜ 变节军将唐安德烈
- 颜色 UBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Vampire Pirate
- 流行度：EDHREC 全时段第 429 位，约 6765 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.09 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.43
- 社区标签：偷取、宝物、海盗、放逐、控制、Outlaws
- 完整牌面：Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types.
Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ramirez DePietro, Pillager（{2}{U}{B}｜Legendary Creature — Human Pirate） — When Ramirez DePietro enters, you lose 2 life and create two Treasure tokens. Whenever one or more Pirates you control deal combat damage to a player, exile the top card 
  2. Hostage Taker（{2}{U}{B}｜Creature — Human Pirate） — When this creature enters, exile another target creature or artifact until this creature leaves the battlefield. You may cast that card for as long as it remains exiled, 
  3. Laughing Jasper Flint（{1}{B}{R}｜Legendary Creature — Lizard Rogue） — Creatures you control but don't own are Mercenaries in addition to their other types. At the beginning of your upkeep, exile the top X cards of target opponent's library,
  4. Thief of Sanity（{1}{U}{B}｜Creature — Specter） — Flying Whenever this creature deals combat damage to a player, look at the top three cards of that player's library, exile one of them face down, then put the rest into t
  5. Breeches, Brazen Plunderer（{3}{R}｜Legendary Creature — Goblin Pirate） — Menace Whenever one or more Pirates you control deal damage to your opponents, exile the top card of each of those opponents' libraries. You may play those cards this tur
  6. Malcolm, Keen-Eyed Navigator（{2}{U}｜Legendary Creature — Siren Pirate） — Flying Whenever one or more Pirates you control deal damage to your opponents, you create a Treasure token for each opponent dealt damage. (It's an artifact with "{T}, Sa
- **出场率最高的牌**（大多数牌组都会放）
  - Crumbling Necropolis（｜Land） — This land enters tapped. {T}: Add {U}, {B}, or {R}.
  - Etali, Primal Storm（{4}{R}{R}｜Legendary Creature — Elder Dinosaur） — Whenever Etali attacks, exile the top card of each player's library, then you may cast any number of spells from among those cards
  - Coercive Recruiter（{4}{R}｜Creature — Orc Pirate） — Whenever this creature or another Pirate you control enters, gain control of target creature until end of turn. Untap that creatur
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.


## Peter Parker // Amazing Spider-Man ｜ 彼得·帕克
- 颜色 WUG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Scientist Hero // Legendary Creature — Spider Human Hero
- 流行度：EDHREC 全时段第 432 位，约 6727 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.69 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.08
- 社区标签：传奇、史迹、Web-slinging、＋1/＋1 指示物、加速、衍生物
- 完整牌面：When Peter Parker enters, create a 2/1 green Spider creature token with reach.
{1}{G}{W}{U}: Transform Peter Parker. Activate only as a sorcery.
//
Vigilance, reach
Each legendary spell you cast that's one or more colors has web-slinging {G}{W}{U}. (You may cast a spell for its web-slinging cost if you also return a tapped creature you control to its owner's hand.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Absolute Virtue（{6}{W}{U}｜Legendary Creature — Avatar Warrior） — This spell can't be countered. Flying You have protection from each of your opponents. (You can't be dealt damage, enchanted, or targeted by anything controlled by your o
  2. Spider-Sense（{1}{U}｜Instant） — Web-slinging {U} (You may cast this spell for {U} if you also return a tapped creature you control to its owner's hand.) Counter target instant spell, sorcery spell, or t
  3. Urza's Ruinous Blast（{4}{W}｜Legendary Sorcery） — (You may cast a legendary sorcery only if you control a legendary creature or planeswalker.) Exile all nonland permanents that aren't legendary.
  4. Relic of Legends（{3}｜Artifact） — {T}: Add one mana of any color. Tap an untapped legendary creature you control: Add one mana of any color.
  5. Urban Retreat（｜Land） — This land enters tapped. {T}: Add {G}, {W}, or {U}. {2}, Return a tapped creature you control to its owner's hand: Put this card from your hand onto the battlefield. Acti
  6. Spectacular Spider-Man（{1}{W}｜Legendary Creature — Spider Human Hero） — Flash {1}: Spectacular Spider-Man gains flying until end of turn. {1}, Sacrifice Spectacular Spider-Man: Creatures you control gain hexproof and indestructible until end 
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Chulane, Teller of Tales（{2}{G}{W}{U}｜Legendary Creature — Human Druid） — Vigilance Whenever you cast a creature spell, draw a card, then you may put a land card from your hand onto the battlefield. {3}, 


## Aang, at the Crossroads // Aang, Destined Savior ｜ 身处十字路口的安昂
- 颜色 WUG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Avatar Ally // Legendary Creature — Avatar Ally
- 流行度：EDHREC 全时段第 434 位，约 6711 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 5/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.50
- 社区标签：闪现回场、复制、组合技、＋1/＋1 指示物、地牌核心、伙伴
- 完整牌面：Flying
When Aang enters, look at the top five cards of your library. You may put a creature card with mana value 4 or less from among them onto the battlefield. Put the rest on the bottom of your library in a random order.
When another creature you control leaves the battlefield, transform Aang at the beginning of the next upkeep.
//
Flying
Land creatures you control have vigilance.
At the beginning of combat on your turn, earthbend 2. (Target land you control becomes a 0/0 creature with haste that's still a land. Put two +1/+1 counters on it. When it dies or is exiled, return it to the battlefield tapped.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Katara, the Fearless（{G}{W}{U}｜Legendary Creature — Human Warrior Ally） — If a triggered ability of an Ally you control triggers, that ability triggers an additional time.
  2. Starfield Vocalist（{3}{U}｜Creature — Human Bard） — If a permanent entering the battlefield causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time. Warp {1}{U} (You may c
  3. Restoration Angel（{3}{W}｜Creature — Angel） — Flash Flying When this creature enters, you may exile target non-Angel creature you control, then return that card to the battlefield under your control.
  4. Felidar Guardian（{3}{W}｜Creature — Cat Beast） — When this creature enters, you may exile another target permanent you control, then return that card to the battlefield under its owner's control.
  5. Ephemerate（{W}｜Instant） — Exile target creature you control, then return it to the battlefield under its owner's control. Rebound (If you cast this spell from your hand, exile it as it resolves. A
  6. Chameleon, Master of Disguise（{3}{U}｜Legendary Creature — Human Shapeshifter Villain） — You may have Chameleon enter as a copy of a creature you control, except his name is Chameleon, Master of Disguise. Mayhem {2}{U} (You may cast this card from your gravey
- **出场率最高的牌**（大多数牌组都会放）
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Spark Double（{3}{U}｜Creature — Illusion） — You may have this creature enter as a copy of a creature or planeswalker you control, except it enters with an additional +1/+1 co


## Karametra, God of Harvests ｜ 丰收神卡拉美特拉
- 颜色 WG ｜ 法术力值 5.0 ｜ 类型 Legendary Enchantment Creature — God
- 流行度：EDHREC 全时段第 435 位，约 6710 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.34 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.19
- 社区标签：地落、地牌核心、加速、衍生物、结界流、＋1/＋1 指示物
- 完整牌面：Indestructible
As long as your devotion to green and white is less than seven, Karametra isn't a creature.
Whenever you cast a creature spell, you may search your library for a Forest or Plains card, put it onto the battlefield tapped, then shuffle.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  2. Rampaging Baloths（{4}{G}{G}｜Creature — Beast） — Trample Landfall — Whenever a land you control enters, create a 4/4 green Beast creature token.
  3. Beast Whisperer（{2}{G}{G}｜Creature — Elf Druid） — Whenever you cast a creature spell, draw a card.
  4. Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create a token that's a copy of this creature i
  5. Tireless Provisioner（{2}{G}｜Creature — Elf Scout） — Landfall — Whenever a land you control enters, create a Food token or a Treasure token. (Food is an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life." Treas
  6. Avenger of Zendikar（{5}{G}{G}｜Creature — Elemental） — When this creature enters, create a 0/1 green Plant creature token for each land you control. Landfall — Whenever a land you control enters, you may put a +1/+1 counter o
- **出场率最高的牌**（大多数牌组都会放）
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Avacyn's Pilgrim（{G}｜Creature — Human Monk） — {T}: Add {W}.
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Delney, Streetwise Lookout ｜ 街头监哨德雷尼
- 颜色 W ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Scout
- 流行度：EDHREC 全时段第 436 位，约 6693 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.81 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $34.50
- 社区标签：衍生物、闪现回场、生命增益、小牌抽、小生物、快攻
- 完整牌面：Creatures you control with power 2 or less can't be blocked by creatures with power 3 or greater.
If a triggered ability of a creature you control with power 2 or less triggers, that ability triggers an additional time.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Dusk // Dawn（{2}{W}{W} // {3}{W}{W}｜Sorcery // Sorcery） — 
  2. The Battle of Bywater（{1}{W}{W}｜Sorcery） — Destroy all creatures with power 3 or greater. Then create a Food token for each creature you control. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 
  3. Enduring Innocence（{1}{W}{W}｜Enchantment Creature — Sheep Glimmer） — Lifelink Whenever one or more other creatures you control with power 2 or less enter, draw a card. This ability triggers only once each turn. When Enduring Innocence dies
  4. Raise the Past（{2}{W}{W}｜Sorcery） — Return all creature cards with mana value 2 or less from your graveyard to the battlefield.
  5. Assemble the Players（{1}{W}｜Enchantment） — You may look at the top card of your library any time. Once each turn, you may cast a creature spell with power 2 or less from the top of your library.
  6. Hare Apparent（{1}{W}｜Creature — Rabbit Noble） — When this creature enters, create a number of 1/1 white Rabbit creature tokens equal to the number of other creatures you control named Hare Apparent. A deck can have any
- **出场率最高的牌**（大多数牌组都会放）
  - Pearl Medallion（{2}｜Artifact） — White spells you cast cost {1} less to cast.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Oketra's Monument（{3}｜Legendary Artifact） — White creature spells you cast cost {1} less to cast. Whenever you cast a creature spell, create a 1/1 white Warrior creature toke
  - Welcoming Vampire（{2}{W}｜Creature — Vampire） — Flying Whenever one or more other creatures you control with power 2 or less enter, draw a card. This ability triggers only once e


## Imodane, the Pyrohammer ｜ 烈焰锤依莫丹
- 颜色 R ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Knight
- 流行度：EDHREC 全时段第 437 位，约 6686 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.14 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.36
- 社区标签：烧血、法术连发、快攻、组合技、群体折磨、X 咒语
- 完整牌面：Whenever an instant or sorcery spell you control that targets only a single creature deals damage to that creature, Imodane deals that much damage to each opponent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Shivan Meteor（{3}{R}{R}｜Sorcery） — Shivan Meteor deals 13 damage to target creature. Suspend 2—{1}{R}{R} (Rather than cast this card from your hand, you may pay {1}{R}{R} and exile it with two time counter
  2. Flame Slash（{R}｜Sorcery） — Flame Slash deals 4 damage to target creature.
  3. Spitting Earth（{1}{R}｜Sorcery） — Spitting Earth deals damage to target creature equal to the number of Mountains you control.
  4. Lightning Axe（{R}｜Instant） — As an additional cost to cast this spell, discard a card or pay {5}. Lightning Axe deals 5 damage to target creature.
  5. Stonesplitter Bolt（{X}{R}｜Instant） — Bargain (You may sacrifice an artifact, enchantment, or token as you cast this spell.) Stonesplitter Bolt deals X damage to target creature or planeswalker. If this spell
  6. Electrodominance（{X}{R}{R}｜Instant） — Electrodominance deals X damage to any target. You may cast a spell with mana value X or less from your hand without paying its mana cost.
- **出场率最高的牌**（大多数牌组都会放）
  - Lightning Bolt（{R}｜Instant） — Lightning Bolt deals 3 damage to any target.
  - Abrade（{1}{R}｜Instant） — Choose one — • Abrade deals 3 damage to target creature. • Destroy target artifact.
  - Ruby Medallion（{2}｜Artifact） — Red spells you cast cost {1} less to cast.
  - Guttersnipe（{2}{R}｜Creature — Goblin Shaman） — Whenever you cast an instant or sorcery spell, this creature deals 2 damage to each opponent.


## Zur, Eternal Schemer ｜ 永世阴谋家祖尔
- 颜色 WUB ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Wizard
- 流行度：EDHREC 全时段第 439 位，约 6669 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.61 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $4.25
- 社区标签：结界流、生命增益、控制、铁壁防守、中速、锁场
- 完整牌面：Flying
Enchantment creatures you control have deathtouch, lifelink, and hexproof.
{1}{W}: Target non-Aura enchantment you control becomes a creature in addition to its other types and has base power and base toughness each equal to its mana value.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Inquisitive Glimmer（{W}{U}｜Enchantment Creature — Fox Glimmer） — Enchantment spells you cast cost {1} less to cast. Unlock costs you pay cost {1} less.
  2. Mesa Enchantress（{1}{W}{W}｜Creature — Human Druid） — Whenever you cast an enchantment spell, you may draw a card.
  3. Enduring Curiosity（{2}{U}{U}｜Enchantment Creature — Cat Glimmer） — Flash Whenever a creature you control deals combat damage to a player, draw a card. When Enduring Curiosity dies, if it was a creature, return it to the battlefield under
  4. Enduring Tenacity（{2}{B}{B}｜Enchantment Creature — Snake Glimmer） — Whenever you gain life, target opponent loses that much life. When Enduring Tenacity dies, if it was a creature, return it to the battlefield under its owner's control. I
  5. Soaring Lightbringer（{4}{W}｜Enchantment Creature — Bird Glimmer） — Flying Other enchantment creatures you control have flying. Whenever you attack a player, create a 1/1 white Glimmer enchantment creature token that's tapped and attackin
  6. Starfield Mystic（{1}{W}｜Creature — Human Cleric） — Enchantment spells you cast cost {1} less to cast. Whenever an enchantment you control is put into a graveyard from the battlefield, put a +1/+1 counter on this creature.
- **出场率最高的牌**（大多数牌组都会放）
  - Hall of Heliod's Generosity（｜Legendary Land） — {T}: Add {C}. {1}{W}, {T}: Put target enchantment card from your graveyard on top of your library.
  - Sphere of Safety（{4}{W}｜Enchantment） — Creatures can't attack you or planeswalkers you control unless their controller pays {X} for each of those creatures, where X is t
  - Entity Tracker（{2}{U}｜Creature — Human Scout） — Flash Eerie — Whenever an enchantment you control enters and whenever you fully unlock a Room, draw a card.
  - Demon of Fate's Design（{4}{B}{B}｜Enchantment Creature — Demon） — Flying, trample Once during each of your turns, you may cast an enchantment spell by paying life equal to its mana value rather th


## Dr. Madison Li ｜ 麦蒂森·黎博士
- 颜色 WUR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Scientist
- 流行度：EDHREC 全时段第 442 位，约 6622 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.19 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：能量、神器、组合技、衍生物、坟场复活、＋1/＋1 指示物
- 完整牌面：Whenever you cast an artifact spell, you get {E} (an energy counter).
{T}, Pay {E}: Target creature gets +1/+0 and gains trample and haste until end of turn.
{T}, Pay {E}{E}{E}: Draw a card.
{T}, Pay {E}{E}{E}{E}{E}: Return target artifact card from your graveyard to the battlefield tapped.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Electrosiphon（{U}{U}{R}｜Instant） — Counter target spell. You get an amount of {E} (energy counters) equal to its mana value.
  2. Liberty Prime, Recharged（{2}{U}{R}{W}｜Legendary Artifact Creature — Robot） — Vigilance, trample, haste Whenever Liberty Prime attacks or blocks, sacrifice it unless you pay {E}{E} (two energy counters). {2}, {T}, Sacrifice an artifact: You get {E}
  3. Automated Assembly Line（{1}{W}｜Artifact） — Whenever one or more artifact creatures you control deal combat damage to a player, you get {E} (an energy counter). Pay {E}{E}{E}: Create a tapped 3/3 colorless Robot ar
  4. HELIOS One（｜Land） — {T}: Add {C}. {1}, {T}: You get {E} (an energy counter). {3}, {T}, Pay X {E}, Sacrifice this land: Destroy target nonland permanent with mana value X. Activate only as a 
  5. Assaultron Dominator（{1}{R}｜Artifact Creature — Robot） — When this creature enters, you get {E}{E} (two energy counters). Whenever an artifact creature you control attacks, you may pay {E}. If you do, put your choice of a +1/+1
  6. Gonti's Aether Heart（{6}｜Legendary Artifact） — Whenever Gonti's Aether Heart or another artifact you control enters, you get {E}{E} (two energy counters). Pay eight {E}, Exile Gonti's Aether Heart: Take an extra turn 
- **出场率最高的牌**（大多数牌组都会放）
  - Mystic Monastery（｜Land） — This land enters tapped. {T}: Add {U}, {R}, or {W}.
  - Dispatch（{W}｜Instant） — Tap target creature. Metalcraft — If you control three or more artifacts, exile that creature.
  - Izzet Generatorium（{U}{R}｜Artifact） — If you would get one or more {E} (energy counters), you get that many plus one {E} instead. {T}: Draw a card. Activate only if you
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.


## Sorin of House Markov // Sorin, Ravenous Neonate ｜ 马可夫家族的索霖
- 颜色 WB ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Noble // Legendary Planeswalker — Sorin
- 流行度：EDHREC 全时段第 443 位，约 6616 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.26 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $4.30
- 社区标签：生命增益、吸取生命、吸血鬼、组合技、牺牲流、自伤
- 完整牌面：Lifelink
Extort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.)
At the beginning of each of your postcombat main phases, if you gained 3 or more life this turn, exile Sorin, then return him to the battlefield transformed under his owner's control.
//
Extort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.)
+2: Create a Food token.
−1: Sorin deals damage equal to the amount of life you gained this turn to any target.
−6: Gain control of target creature. It becomes a Vampire in addition to its other types. Put a lifelink counter on it if you control a white permanent other than that creature or Sorin.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Vito, Thorn of the Dusk Rose（{2}{B}｜Legendary Creature — Vampire Cleric） — Whenever you gain life, target opponent loses that much life. {3}{B}{B}: Creatures you control gain lifelink until end of turn.
  2. Exsanguinate（{X}{B}{B}｜Sorcery） — Each opponent loses X life. You gain life equal to the life lost this way.
  3. Soul Warden（{W}｜Creature — Human Cleric） — Whenever another creature enters, you gain 1 life.
  4. Sanguine Bond（{3}{B}{B}｜Enchantment） — Whenever you gain life, target opponent loses that much life.
  5. Blind Obedience（{1}{W}｜Enchantment） — Extort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.) Artifacts and creatures your opponents control e
  6. Sorin, Vengeful Bloodlord（{2}{W}{B}｜Legendary Planeswalker — Sorin） — During your turn, creatures and planeswalkers you control have lifelink. +2: Sorin deals 1 damage to target player or planeswalker. −X: Return target creature card with m
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Talisman of Hierarchy（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {B}. This artifact deals 1 damage to you.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Aragorn, King of Gondor ｜ 刚铎国王阿拉贡
- 颜色 WUR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Noble
- 流行度：EDHREC 全时段第 444 位，约 6598 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.63 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.61
- 社区标签：君主、人类、快攻、衍生物、铁壁防守、额外战斗
- 完整牌面：Vigilance, lifelink
When Aragorn enters, you become the monarch.
Whenever Aragorn attacks, up to one target creature can't block this turn. If you're the monarch, creatures can't block this turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Faramir, Steward of Gondor（{1}{W}{U}｜Legendary Creature — Human Noble） — Whenever a legendary creature you control with mana value 4 or greater enters, you become the monarch. At the beginning of your end step, if you're the monarch, create tw
  2. Champions of Minas Tirith（{5}{W}｜Creature — Human Soldier） — When this creature enters, you become the monarch. At the beginning of combat on each opponent's turn, if you're the monarch, that opponent may pay {X}, where X is the nu
  3. Éomer, King of Rohan（{3}{R}{W}｜Legendary Creature — Human Noble） — Double strike Éomer enters with a +1/+1 counter on it for each other Human you control. When Éomer enters, target player becomes the monarch. Éomer deals damage equal to 
  4. Éowyn, Shieldmaiden（{2}{U}{R}{W}｜Legendary Creature — Human Knight） — First strike At the beginning of combat on your turn, if another Human entered the battlefield under your control this turn, create two 2/2 red Human Knight creature toke
  5. Forth Eorlingas!（{X}{R}{W}｜Sorcery） — Create X 2/2 red Human Knight creature tokens with trample and haste. Whenever one or more creatures you control deal combat damage to one or more players this turn, you 
  6. Prince Imrahil the Fair（{W}{U}｜Legendary Creature — Human Noble） — Whenever you draw your second card each turn, create a 1/1 white Human Soldier creature token.
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.


## The Emperor of Palamecia // The Lord Master of Hell ｜ 帕拉美奇亚皇帝
- 颜色 UR ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Noble Wizard // Legendary Creature — Demon Noble Wizard
- 流行度：EDHREC 全时段第 446 位，约 6569 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.48 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.30
- 社区标签：法术连发、烧血、自磨、磨牌、坟场、＋1/＋1 指示物
- 完整牌面：{T}: Add {U} or {R}. Spend this mana only to cast a noncreature spell.
Whenever you cast a noncreature spell, if at least four mana was spent to cast it, put a +1/+1 counter on The Emperor of Palamecia. Then if it has three or more +1/+1 counters on it, transform it.
//
Starfall — Whenever The Lord Master of Hell attacks, it deals X damage to each opponent, where X is the number of noncreature, nonland cards in your graveyard.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Traumatize（{3}{U}{U}｜Sorcery） — Target player mills half their library, rounded down.
  2. Cut Your Losses（{4}{U}{U}｜Sorcery） — Casualty 2 (As you cast this spell, you may sacrifice a creature with power 2 or greater. When you do, copy this spell and you may choose a new target for the copy.) Targ
  3. Pirate's Pillage（{3}{R}｜Sorcery） — As an additional cost to cast this spell, discard a card. Draw two cards and create two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: Add one mana 
  4. Unexpected Windfall（{2}{R}{R}｜Instant） — As an additional cost to cast this spell, discard a card. Draw two cards and create two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: Add one mana 
  5. Big Score（{3}{R}｜Instant） — As an additional cost to cast this spell, discard a card. Draw two cards and create two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: Add one mana 
  6. Hedron Archive（{4}｜Artifact） — {T}: Add {C}{C}. {2}, {T}, Sacrifice this artifact: Draw two cards.
- **出场率最高的牌**（大多数牌组都会放）
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.
  - Frostboil Snarl（｜Land） — As this land enters, you may reveal an Island or Mountain card from your hand. If you don't, this land enters tapped. {T}: Add {U}
  - Stormcarved Coast（｜Land） — This land enters tapped unless you control two or more other lands. {T}: Add {U} or {R}.


## Heliod, the Radiant Dawn // Heliod, the Warped Eclipse ｜ 曙光耀辉赫利欧德
- 颜色 WU ｜ 法术力值 4.0 ｜ 类型 Legendary Enchantment Creature — God // Legendary Enchantment Creature — Phyrexian God
- 流行度：EDHREC 全时段第 447 位，约 6545 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.45 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.49
- 社区标签：换手牌、群体恩惠、控制、组合技、抽牌、X 咒语
- 完整牌面：When Heliod enters, return target enchantment card that isn't a God from your graveyard to your hand.
{3}{U/P}: Transform Heliod. Activate only as a sorcery. ({U/P} can be paid with either {U} or 2 life.)
//
You may cast spells as though they had flash.
Spells you cast cost {1} less to cast for each card your opponents have drawn this turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Prosperity（{X}{U}｜Sorcery） — Each player draws X cards.
  2. Vision Skeins（{1}{U}｜Instant） — Each player draws two cards.
  3. Windfall（{2}{U}｜Sorcery） — Each player discards their hand, then draws cards equal to the greatest number of cards a player discarded this way.
  4. Day's Undoing（{2}{U}｜Sorcery） — Each player shuffles their hand and graveyard into their library, then draws seven cards. If it's your turn, end the turn. (Exile all spells and abilities from the stack,
  5. Even the Score（{X}{U}{U}{U}｜Instant） — This spell costs {U}{U}{U} less to cast if an opponent has drawn four or more cards this turn. Draw X cards.
  6. Words of Wisdom（{1}{U}｜Instant） — You draw two cards, then each other player draws a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Progress（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {U}. This artifact deals 1 damage to you.
  - Azorius Signet（{2}｜Artifact） — {1}, {T}: Add {W}{U}.
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Maha, Its Feathers Night ｜ 蔽夜飞羽玛哈
- 颜色 B ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Elemental Bird
- 流行度：EDHREC 全时段第 449 位，约 6521 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 1.58 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $21.20
- 社区标签：－1/－1 指示物、控制、弃牌、群体折磨、牺牲流、组合技
- 完整牌面：Flying, trample
Ward—Discard a card.
Creatures your opponents control have base toughness 1.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Kaervek, the Spiteful（{2}{B}{B}｜Legendary Creature — Human Warlock） — Other creatures get -1/-1.
  2. Night of Souls' Betrayal（{2}{B}{B}｜Legendary Enchantment） — All creatures get -1/-1.
  3. Massacre Girl, Known Killer（{2}{B}{B}｜Legendary Creature — Human Assassin） — Menace Creatures you control have wither. (They deal damage to creatures in the form of -1/-1 counters.) Whenever a creature an opponent controls dies, if its toughness w
  4. Gruesome Realization（{1}{B}{B}｜Sorcery） — Choose one — • You draw two cards and you lose 2 life. • Creatures your opponents control get -1/-1 until end of turn.
  5. Massacre Wurm（{3}{B}{B}{B}｜Creature — Phyrexian Wurm） — When this creature enters, creatures your opponents control get -2/-2 until end of turn. Whenever a creature an opponent controls dies, that player loses 2 life.
  6. Black Sun's Zenith（{X}{B}{B}｜Sorcery） — Put X -1/-1 counters on each creature. Shuffle Black Sun's Zenith into its owner's library.
- **出场率最高的牌**（大多数牌组都会放）
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Crypt Ghast（{3}{B}｜Creature — Spirit） — Extort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.) Whenever
  - Morbid Opportunist（{2}{B}｜Creature — Human Rogue） — Whenever one or more other creatures die, draw a card. This ability triggers only once each turn.


## Slimefoot, the Stowaway ｜ 寄舱客黏足
- 颜色 BG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Fungus
- 流行度：EDHREC 全时段第 450 位，约 6488 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.22 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.27
- 社区标签：腐生物、衍生物、牺牲流、Fungi、牺牲、组合技
- 完整牌面：Whenever a Saproling you control dies, Slimefoot deals 1 damage to each opponent and you gain 1 life.
{4}: Create a 1/1 green Saproling creature token.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Utopia Mycon（{G}｜Creature — Fungus） — At the beginning of your upkeep, put a spore counter on this creature. Remove three spore counters from this creature: Create a 1/1 green Saproling creature token. Sacrif
  2. Deathspore Thallid（{1}{B}｜Creature — Zombie Fungus） — At the beginning of your upkeep, put a spore counter on this creature. Remove three spore counters from this creature: Create a 1/1 green Saproling creature token. Sacrif
  3. Nemata, Primeval Warden（{2}{B}{G}｜Legendary Creature — Treefolk） — Reach If a creature an opponent controls would die, exile it instead. When you do, create a 1/1 green Saproling creature token. {G}, Sacrifice a Saproling: Nemata gets +2
  4. Sporemound（{3}{G}{G}｜Creature — Fungus） — Landfall — Whenever a land you control enters, create a 1/1 green Saproling creature token.
  5. Mycoloth（{3}{G}{G}｜Creature — Fungus） — Devour 2 (As this creature enters, you may sacrifice any number of creatures. It enters with twice that many +1/+1 counters on it.) At the beginning of your upkeep, creat
  6. Tendershoot Dryad（{4}{G}｜Creature — Dryad） — Ascend (If you control ten or more permanents, you get the city's blessing for the rest of the game.) At the beginning of each upkeep, create a 1/1 green Saproling creatu
- **出场率最高的牌**（大多数牌组都会放）
  - Fungal Plots（{1}{G}｜Enchantment） — {1}{G}, Exile a creature card from your graveyard: Create a 1/1 green Saproling creature token. Sacrifice two Saprolings: You gain
  - Saproling Symbiosis（{3}{G}｜Sorcery） — You may cast this spell as though it had flash if you pay {2} more to cast it. (You may cast it any time you could cast an instant
  - Fungal Rebirth（{2}{G}｜Instant） — Return target permanent card from your graveyard to your hand. If a creature died this turn, create two 1/1 green Saproling creatu
  - Verdant Force（{5}{G}{G}{G}｜Creature — Elemental） — At the beginning of each upkeep, create a 1/1 green Saproling creature token.


## Tasigur, the Golden Fang ｜ 金牙塔西格
- 颜色 UBG ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Human Shaman
- 流行度：EDHREC 全时段第 453 位，约 6457 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.17 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.25
- 社区标签：诞生荚、组合技、控制、磨牌、坟场复活、中速
- 完整牌面：Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)
{2}{G/U}{G/U}: Mill two cards, then return a nonland card of an opponent's choice from your graveyard to your hand.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Neoform（{G}{U}｜Sorcery） — As an additional cost to cast this spell, sacrifice a creature. Search your library for a creature card with mana value equal to 1 plus the sacrificed creature's mana val
  2. Eldritch Evolution（{1}{G}{G}｜Sorcery） — As an additional cost to cast this spell, sacrifice a creature. Search your library for a creature card with mana value X or less, where X is 2 plus the sacrificed creatu
  3. Nezahal, Primal Tide（{5}{U}{U}｜Legendary Creature — Elder Dinosaur） — This spell can't be countered. You have no maximum hand size. Whenever an opponent casts a noncreature spell, draw a card. Discard three cards: Exile Nezahal. Return it t
  4. Deathrite Shaman（{B/G}｜Creature — Elf Shaman） — {T}: Exile target land card from a graveyard. Add one mana of any color. (Activate only as an instant.) {B}, {T}: Exile target instant or sorcery card from a graveyard. E
  5. Birthing Pod（{3}{G/P}｜Artifact） — ({G/P} can be paid with either {G} or 2 life.) {1}{G/P}, {T}, Sacrifice a creature: Search your library for a creature card with mana value equal to 1 plus the sacrificed
  6. Culling Ritual（{2}{B}{G}｜Sorcery） — Destroy each nonland permanent with mana value 2 or less. Add {B} or {G} for each permanent destroyed this way.
- **出场率最高的牌**（大多数牌组都会放）
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Polluted Delta（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for an Island or Swamp card, put it onto the battlefield, then shuffle.


## Mr. Foxglove ｜ 狐袜先生
- 颜色 WUG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Fox Rogue
- 流行度：EDHREC 全时段第 454 位，约 6451 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.21 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：换手牌、抽牌、加速、群体恩惠、优质单卡堆、闪现回场
- 完整牌面：Lifelink
Whenever Mr. Foxglove attacks, draw cards equal to the number of cards in defending player's hand minus the number of cards in your hand. If you didn't draw cards this way, you may put a creature card from your hand onto the battlefield.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Reconnaissance（{W}｜Enchantment） — {0}: Remove target attacking creature you control from combat and untap it. (If you activate during end of combat, the creature will untap after it deals combat damage.)
  2. Kodama of the East Tree（{4}{G}{G}｜Legendary Creature — Spirit） — Reach Whenever another permanent you control enters, if it wasn't put onto the battlefield with this ability, you may put a permanent card with equal or lesser mana value
  3. Nezahal, Primal Tide（{5}{U}{U}｜Legendary Creature — Elder Dinosaur） — This spell can't be countered. You have no maximum hand size. Whenever an opponent casts a noncreature spell, draw a card. Discard three cards: Exile Nezahal. Return it t
  4. Storvald, Frost Giant Jarl（{4}{G}{W}{U}｜Legendary Creature — Giant） — Ward {3} Other creatures you control have ward {3}. Whenever Storvald enters or attacks, choose one or both — • Target creature has base power and toughness 7/7 until end
  5. Ghalta, Stampede Tyrant（{5}{G}{G}{G}｜Legendary Creature — Elder Dinosaur） — Trample When Ghalta enters, put any number of creature cards from your hand onto the battlefield.
  6. Avacyn, Angel of Hope（{5}{W}{W}{W}｜Legendary Creature — Angel） — Flying, vigilance, indestructible Other permanents you control have indestructible.
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Seaside Citadel（｜Land） — This land enters tapped. {T}: Add {G}, {W}, or {U}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.


## Minn, Wily Illusionist ｜ 老成幻术师珉恩
- 颜色 U ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Gnome Wizard
- 流行度：EDHREC 全时段第 455 位，约 6446 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.31 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $9.38
- 社区标签：换手牌、Illusions、抽牌、衍生物、控制、小牌抽
- 完整牌面：Whenever you draw your second card each turn, create a 1/1 blue Illusion creature token with "This token gets +1/+0 for each other Illusion you control."
Whenever an Illusion you control dies, you may put a permanent card with mana value less than or equal to that creature's power from your hand onto the battlefield.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Perilous Research（{1}{U}｜Instant） — Draw two cards, then sacrifice a permanent.
  2. Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  3. Abjure（{U}｜Instant） — As an additional cost to cast this spell, sacrifice a blue permanent. Counter target spell.
  4. Tetsuko Umezawa, Fugitive（{1}{U}｜Legendary Creature — Human Rogue） — Creatures you control with power or toughness 1 or less can't be blocked.
  5. Phantasmal Image（{1}{U}｜Creature — Illusion） — You may have this creature enter as a copy of any creature on the battlefield, except it's an Illusion in addition to its other types and it has "When this creature becom
  6. Teferi's Ageless Insight（{2}{U}{U}｜Legendary Enchantment） — If you would draw a card except the first one you draw in each of your draw steps, draw two cards instead.
- **出场率最高的牌**（大多数牌组都会放）
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  - Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.
  - Sapphire Medallion（{2}｜Artifact） — Blue spells you cast cost {1} less to cast.
  - Mystic Sanctuary（｜Land — Island） — ({T}: Add {U}.) This land enters tapped unless you control three or more other Islands. When this land enters untapped, you may pu


## Karn, Legacy Reforged ｜ 神兵重铸卡恩
- 颜色 C ｜ 法术力值 5.0 ｜ 类型 Legendary Artifact Creature — Golem
- 流行度：EDHREC 全时段第 456 位，约 6438 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.5 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $19.77
- 社区标签：神器、组合技、加速、爆费、神器共鸣、史迹
- 完整牌面：Karn's power and toughness are each equal to the greatest mana value among artifacts you control.
At the beginning of your upkeep, add {C} for each artifact you control. This mana can't be spent to cast nonartifact spells. Until end of turn, you don't lose this mana as steps and phases end.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Darksteel Forge（{9}｜Artifact） — Artifacts you control have indestructible. (Effects that say "destroy" don't destroy them. Artifact creatures with indestructible can't be destroyed by damage.)
  2. Karn, Living Legacy（{4}｜Legendary Planeswalker — Karn） — +1: Create a tapped Powerstone token. (It's an artifact with "{T}: Add {C}. This mana can't be spent to cast a nonartifact spell.") −1: Pay any amount of mana. Look at th
  3. Mycosynth Golem（{11}｜Artifact Creature — Golem） — Affinity for artifacts (This spell costs {1} less to cast for each artifact you control.) Artifact creature spells you cast have affinity for artifacts. (They cost {1} le
  4. Darksteel Colossus（{11}｜Artifact Creature — Golem） — Trample (This creature can deal excess combat damage to the player or planeswalker it's attacking.) Indestructible (Damage and effects that say "destroy" don't destroy th
  5. Lodestone Golem（{4}｜Artifact Creature — Golem） — Nonartifact spells cost {1} more to cast.
  6. Foundry Inspector（{3}｜Artifact Creature — Construct） — Artifact spells you cast cost {1} less to cast.
- **出场率最高的牌**（大多数牌组都会放）
  - Forsaken Monument（{5}｜Legendary Artifact） — Colorless creatures you control get +2/+2. Whenever you tap a permanent for {C}, add an additional {C}. Whenever you cast a colorl
  - Urza's Mine（｜Land — Urza's Mine） — {T}: Add {C}. If you control an Urza's Power-Plant and an Urza's Tower, add {C}{C} instead.
  - Urza's Tower（｜Land — Urza's Tower） — {T}: Add {C}. If you control an Urza's Mine and an Urza's Power-Plant, add {C}{C}{C} instead.
  - Urza's Power Plant（｜Land — Urza's Power-Plant） — {T}: Add {C}. If you control an Urza's Mine and an Urza's Tower, add {C}{C} instead.


## Nelly Borca, Impulsive Accuser ｜ 冲动控官内莉博卡
- 颜色 WR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Detective
- 流行度：EDHREC 全时段第 457 位，约 6406 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.7 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：强制战斗、铁壁防守、借力打力、控制、政治、群体恩惠
- 完整牌面：Vigilance
Whenever Nelly Borca attacks, suspect target creature. Then goad all suspected creatures. (A suspected creature has menace and can't block.)
Whenever one or more creatures an opponent controls deal combat damage to one or more of your opponents, you and the controller of those creatures each draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Disrupt Decorum（{2}{R}{R}｜Sorcery） — Goad all creatures you don't control. (Until your next turn, those creatures attack each combat if able and attack a player other than you if able.)
  2. Hot Pursuit（{1}{R}｜Enchantment） — When this enchantment enters, suspect target creature an opponent controls. As long as this enchantment remains on the battlefield, that creature is also goaded. At the b
  3. Vengeful Ancestor（{2}{R}{R}｜Creature — Spirit Dragon） — Flying Whenever this creature enters or attacks, goad target creature. (Until your next turn, that creature attacks each combat if able and attacks a player other than yo
  4. Take the Bait（{2}{R}{W}｜Instant） — Cast this spell only during combat on an opponent's turn. Prevent all combat damage that would be dealt to you and planeswalkers you control this turn. Untap all attackin
  5. Spectacular Showdown（{1}{R}｜Sorcery） — Put a double strike counter on target creature, then goad each creature that had a double strike counter put on it this way. (Until your next turn, those creatures attack
  6. Duelist's Heritage（{2}{W}｜Enchantment） — Whenever one or more creatures attack, you may have target attacking creature gain double strike until end of turn.
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Conviction（{2}｜Artifact） — {T}: Add {C}. {T}: Add {R} or {W}. This artifact deals 1 damage to you.
  - Curse of Opulence（{R}｜Enchantment — Aura Curse） — Enchant player Whenever enchanted player is attacked, create a Gold token. Each opponent attacking that player does the same. (A G
  - Deflecting Palm（{R}{W}｜Instant） — The next time a source of your choice would deal damage to you this turn, prevent that damage. If damage is prevented this way, De
  - Gisela, Blade of Goldnight（{4}{R}{W}{W}｜Legendary Creature — Angel） — Flying, first strike If a source would deal damage to an opponent or a permanent an opponent controls, that source deals double th


## Beorn the Fierce ｜ 凶猛的贝奥恩
- 颜色 G ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Bear Shapeshifter Warrior
- 流行度：EDHREC 全时段第 459 位，约 6342 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $4.42
- 社区标签：熊、＋1/＋1 指示物、加速、快攻、衍生物、大生物
- 完整牌面：Trample
Other Bears you control get +2/+2.
At the beginning of combat on your turn, put a trample counter on up to one target creature you control. It becomes a Bear in addition to its other types. Then if you control three or more Bears, draw two cards.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ayula, Queen Among Bears（{1}{G}｜Legendary Creature — Bear） — Whenever another Bear you control enters, choose one — • Put two +1/+1 counters on target Bear. • Target Bear you control fights target creature you don't control.
  2. Goreclaw, Terror of Qal Sisma（{3}{G}｜Legendary Creature — Bear） — Creature spells you cast with power 4 or greater cost {2} less to cast. Whenever Goreclaw attacks, each creature you control with power 4 or greater gets +1/+1 and gains 
  3. Wilson, Refined Grizzly（{1}{G}｜Legendary Creature — Bear Warrior） — This spell can't be countered. Reach, vigilance, trample Ward {2} (Whenever this creature becomes the target of a spell or ability an opponent controls, counter it unless
  4. Werebear（{1}{G}｜Creature — Human Bear Druid） — {T}: Add {G}. Threshold — This creature gets +3/+3 as long as there are seven or more cards in your graveyard.
  5. Dancing from Dark to Dawn（{3}{G}{G}｜Enchantment） — Whenever you cast a creature spell, put X +1/+1 counters on target creature you control, where X is that spell's mana value. Landfall — Whenever a land you control enters
  6. Gigantic Big Bear（{5}{G}{G}｜Creature — Bear） — This spell can't be countered. Hexproof, haste
- **出场率最高的牌**（大多数牌组都会放）
  - Studious First-Year（｜） — 
  - The Earth King（{3}{G}｜Legendary Creature — Human Noble Ally） — When The Earth King enters, create a 4/4 green Bear creature token. Whenever one or more creatures you control with power 4 or gre
  - Little Bear（{2}{G}｜Creature — Bear） — Flash When this creature enters, untap another target creature you control. If that creature is a Bear, put a +1/+1 counter on it.
  - Owlbear Cub（{2}{G}｜Creature — Bird Bear） — Mama's Coming — Whenever this creature attacks a player who controls eight or more lands, look at the top eight cards of your libr


## Selvala, Heart of the Wilds ｜ 荒野之心塞瓦拉
- 颜色 G ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elf Scout
- 流行度：EDHREC 全时段第 459 位，约 6376 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 0.83 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.49
- 社区标签：加速、组合技、大生物、爆费、快攻、＋1/＋1 指示物
- 完整牌面：Whenever another creature enters, its controller may draw a card if its power is greater than each other creature's power.
{G}, {T}: Add X mana in any combination of colors, where X is the greatest power among creatures you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess combat damage to the player or planeswalker
  2. Staff of Domination（{3}｜Artifact） — {1}: Untap this artifact. {2}, {T}: You gain 1 life. {3}, {T}: Untap target creature. {4}, {T}: Tap target creature. {5}, {T}: Draw a card.
  3. Quirion Ranger（{G}｜Creature — Elf Ranger） — Return a Forest you control to its owner's hand: Untap target creature. Activate only once each turn.
  4. Wirewood Lodge（｜Land） — {T}: Add {C}. {G}, {T}: Untap target Elf.
  5. Umbral Mantle（{3}｜Artifact — Equipment） — Equipped creature has "{3}, {Q}: This creature gets +2/+2 until end of turn." ({Q} is the untap symbol.) Equip {0}
  6. Scryb Ranger（{1}{G}｜Creature — Faerie Ranger） — Flash Flying, protection from blue Return a Forest you control to its owner's hand: Untap target creature. Activate only once each turn.
- **出场率最高的牌**（大多数牌组都会放）
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Fyndhorn Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Rishkar's Expertise（{4}{G}{G}｜Sorcery） — Draw cards equal to the greatest power among creatures you control. You may cast a spell with mana value 5 or less from your hand 


## Ratadrabik of Urborg ｜ 乌尔博格的拉塔札比
- 颜色 WB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Zombie Wizard
- 流行度：EDHREC 全时段第 464 位，约 6293 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.51 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.77
- 社区标签：传奇、牺牲流、衍生物、坟场复活、组合技、牺牲
- 完整牌面：Vigilance, ward {2}
Other Zombies you control have vigilance.
Whenever another legendary creature you control dies, create a token that's a copy of that creature, except it's not legendary and it's a 2/2 black Zombie in addition to its other colors and types.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Teysa Karlov（{2}{W}{B}｜Legendary Creature — Human Advisor） — If a creature dying causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time. Creature tokens you control have vigilance
  2. Relic of Legends（{3}｜Artifact） — {T}: Add one mana of any color. Tap an untapped legendary creature you control: Add one mana of any color.
  3. Boromir, Warden of the Tower（{2}{W}｜Legendary Creature — Human Soldier） — Vigilance Whenever an opponent casts a spell, if no mana was spent to cast it, counter that spell. Sacrifice Boromir: Creatures you control gain indestructible until end 
  4. Gandalf the White（{3}{W}{W}｜Legendary Creature — Avatar Wizard） — Flash You may cast legendary spells and artifact spells as though they had flash. If a legendary permanent or an artifact entering or leaving the battlefield causes a tri
  5. Samwise the Stouthearted（{1}{W}｜Legendary Creature — Halfling Peasant） — Flash When Samwise enters, choose up to one target permanent card in your graveyard that was put there from the battlefield this turn. Return it to your hand. Then the Ri
  6. Nasty End（{1}{B}｜Instant） — As an additional cost to cast this spell, sacrifice a creature. Draw two cards. If the sacrificed creature was legendary, draw three cards instead.
- **出场率最高的牌**（大多数牌组都会放）
  - Elas il-Kor, Sadistic Pilgrim（{W}{B}｜Legendary Creature — Phyrexian Kor Cleric） — Deathtouch Whenever another creature you control enters, you gain 1 life. Whenever another creature you control dies, each opponen
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Aeve, Progenitor Ooze ｜ 流浆先祖艾夫
- 颜色 G ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Ooze
- 流行度：EDHREC 全时段第 465 位，约 6257 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.39 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.35
- 社区标签：＋1/＋1 指示物、Oozes、风暴、衍生物、Slime Against Humanity、加速
- 完整牌面：Storm (When you cast this spell, copy it for each spell cast before it this turn. Copies become tokens.)
Aeve isn't legendary if it's a token.
Aeve enters with a +1/+1 counter on it for each other Ooze you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Biowaste Blob（{2}{G}{G}｜Creature — Ooze） — Oozes you control get +1/+1. At the beginning of your upkeep, if you control a commander, create a token that's a copy of this creature.
  2. Biogenic Ooze（{3}{G}{G}｜Creature — Ooze） — When this creature enters, create a 2/2 green Ooze creature token. At the beginning of your end step, put a +1/+1 counter on each Ooze you control. {1}{G}{G}{G}: Create a
  3. Slime Against Humanity（{2}{G}｜Sorcery） — Create a 0/0 green Ooze creature token with trample. Put X +1/+1 counters on it, where X is two plus the total number of cards you own in exile and in your graveyard that
  4. Predator Ooze（{G}{G}{G}｜Creature — Ooze） — Indestructible (Damage and effects that say "destroy" don't destroy this creature.) Whenever this creature attacks, put a +1/+1 counter on it. Whenever a creature dealt d
  5. Oran-Rief Ooze（{2}{G}｜Creature — Ooze） — When this creature enters, put a +1/+1 counter on target creature you control. Whenever this creature attacks, put a +1/+1 counter on each attacking creature with a +1/+1
  6. Green Slime（{2}{G}｜Creature — Ooze） — Flash When this creature enters, counter target activated or triggered ability from an artifact or enchantment source. If a permanent's ability is countered this way, des
- **出场率最高的牌**（大多数牌组都会放）
  - Emerald Medallion（{2}｜Artifact） — Green spells you cast cost {1} less to cast.
  - Scavenging Ooze（{1}{G}｜Creature — Ooze） — {G}: Exile target card from a graveyard. If it was a creature card, put a +1/+1 counter on this creature and you gain 1 life.
  - Acidic Slime（{3}{G}{G}｜Creature — Ooze） — Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.) When this creature enters, destroy target arti
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 


## Narset, Enlightened Master ｜ 悟道大师娜尔施
- 颜色 WUR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Human Monk
- 流行度：EDHREC 全时段第 466 位，约 6239 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 1.64 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.60
- 社区标签：额外回合、额外战斗、法术连发、鹏洛客、主将单挑、组合技
- 完整牌面：First strike, hexproof
Whenever Narset attacks, exile the top four cards of your library. Until end of turn, you may cast noncreature spells from among those cards without paying their mana costs.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Omniscience（{7}{U}{U}{U}｜Enchantment） — You may cast spells from your hand without paying their mana costs.
  2. Time Stretch（{8}{U}{U}｜Sorcery） — Target player takes two extra turns after this one.
  3. Beacon of Tomorrows（{6}{U}{U}｜Sorcery） — Target player takes an extra turn after this one. Shuffle Beacon of Tomorrows into its owner's library.
  4. Nexus of Fate（{5}{U}{U}｜Instant） — Take an extra turn after this one. If Nexus of Fate would be put into a graveyard from anywhere, reveal Nexus of Fate and shuffle it into its owner's library instead.
  5. Temporal Mastery（{5}{U}{U}｜Sorcery） — Take an extra turn after this one. Exile Temporal Mastery. Miracle {1}{U} (You may cast this card for its miracle cost when you draw it if it's the first card you drew th
  6. Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
- **出场率最高的牌**（大多数牌组都会放）
  - Steam Vents（｜Land — Island Mountain） — ({T}: Add {U} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Talisman of Creativity（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {R}. This artifact deals 1 damage to you.
  - Talisman of Progress（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {U}. This artifact deals 1 damage to you.


## Nine-Fingers Keene ｜ 九指姬恩
- 颜色 UBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Rogue
- 流行度：EDHREC 全时段第 467 位，约 6216 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.26 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.30
- 社区标签：地牌核心、Guildgates、加速、地落、主将单挑、组合技
- 完整牌面：Menace
Ward—Pay 9 life.
Whenever Nine-Fingers Keene deals combat damage to a player, look at the top nine cards of your library. You may put a Gate card from among them onto the battlefield. Then if you control nine or more Gates, put the rest into your hand. Otherwise, put the rest on the bottom of your library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Gond Gate（｜Land — Gate） — Gates you control enter untapped. {T}: Add {C}. {T}: Add one mana of any color that a Gate you control could produce.
  2. Manor Gate（｜Land — Gate） — This land enters tapped. As this land enters, choose a color other than green. {T}: Add {G} or one mana of the chosen color.
  3. Black Dragon Gate（｜Land — Gate） — This land enters tapped. As this land enters, choose a color other than black. {T}: Add {B} or one mana of the chosen color.
  4. Sea Gate（｜Land — Gate） — This land enters tapped. As this land enters, choose a color other than blue. {T}: Add {U} or one mana of the chosen color.
  5. Baldur's Gate（｜Legendary Land — Gate） — {T}: Add {C}. {2}, {T}: Add X mana of any one color, where X is the number of other Gates you control.
  6. Basilisk Gate（｜Land — Gate） — {T}: Add {C}. {2}, {T}: Target creature gets +X/+X until end of turn, where X is the number of Gates you control. Activate only as a sorcery.
- **出场率最高的牌**（大多数牌组都会放）
  - Simic Guildgate（｜Land — Gate） — This land enters tapped. {T}: Add {G} or {U}.
  - Golgari Guildgate（｜Land — Gate） — This land enters tapped. {T}: Add {B} or {G}.
  - Dimir Guildgate（｜Land — Gate） — This land enters tapped. {T}: Add {U} or {B}.
  - Heap Gate（｜Land — Gate） — {T}: Add {C}. {1}, {T}: Add one mana of any color. {1}, {T}, Tap an untapped Gate you control: Create a Treasure token. (It's an a


## Syr Konrad, the Grim ｜ 冷酷孔纳德爵士
- 颜色 B ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Knight
- 流行度：EDHREC 全时段第 468 位，约 6205 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.93 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.78
- 社区标签：磨牌、坟场复活、牺牲流、坟场、自磨、组合技
- 完整牌面：Whenever another creature dies, or a creature card is put into a graveyard from anywhere other than the battlefield, or a creature card leaves your graveyard, Syr Konrad deals 1 damage to each opponent.
{1}{B}: Each player mills a card. (They each put the top card of their library into their graveyard.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mindcrank（{2}｜Artifact） — Whenever an opponent loses life, that player mills that many cards. (Damage causes loss of life.)
  2. Tortured Existence（{B}｜Enchantment） — {B}, Discard a creature card: Return target creature card from your graveyard to your hand.
  3. Mesmeric Orb（{2}｜Artifact） — Whenever a permanent becomes untapped, that permanent's controller mills a card.
  4. Reassembling Skeleton（{1}{B}｜Creature — Skeleton Warrior） — {1}{B}: Return this card from your graveyard to the battlefield tapped.
  5. Morality Shift（{5}{B}{B}｜Sorcery） — Exchange your graveyard and library. Then shuffle your library.
  6. Millikin（{2}｜Artifact Creature — Construct） — {T}, Mill a card: Add {C}. (Activate only as an instant. To mill a card, put the top card of your library into your graveyard.)
- **出场率最高的牌**（大多数牌组都会放）
  - Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost thi
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  - Plaguecrafter（{2}{B}｜Creature — Human Shaman） — When this creature enters, each player sacrifices a creature or planeswalker of their choice. Each player who can't discards a car


## Kelsien, the Plague ｜ 疫病凯鑫
- 颜色 WBR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Assassin
- 流行度：EDHREC 全时段第 469 位，约 6200 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.8 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.50
- 社区标签：装备、死触、经验指示物、主将单挑、控制、点伤
- 完整牌面：Vigilance, haste
Kelsien gets +1/+1 for each experience counter you have.
{T}: Kelsien deals 1 damage to target creature you don't control. When that creature dies this turn, you get an experience counter.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Basilisk Collar（{1}｜Artifact — Equipment） — Equipped creature has deathtouch and lifelink. (Any amount of damage it deals to a creature is enough to destroy it. Damage dealt by this creature also causes you to gain
  2. Rune of Mortality（{1}{B}｜Enchantment — Aura Rune） — Enchant permanent When this Aura enters, draw a card. As long as enchanted permanent is a creature, it has deathtouch. As long as enchanted permanent is an Equipment, it 
  3. Minthara, Merciless Soul（{2}{W}{B}｜Legendary Creature — Elf Cleric） — Minthara has ward {X}, where X is the number of experience counters you have. At the beginning of your end step, if a permanent you controlled left the battlefield this t
  4. Otharri, Suns' Glory（{3}{R}{W}｜Legendary Creature — Phoenix） — Flying, lifelink, haste Whenever Otharri attacks, you get an experience counter. Then create a 2/2 red Rebel creature token that's tapped and attacking for each experienc
  5. Vorpal Sword（{B}｜Artifact — Equipment） — Equipped creature gets +2/+0 and has deathtouch. {5}{B}{B}{B}: Until end of turn, this Equipment gains "Whenever equipped creature deals combat damage to a player, that p
  6. Gorgon's Head（{1}｜Artifact — Equipment） — Equipped creature has deathtouch. Equip {2}
- **出场率最高的牌**（大多数牌组都会放）
  - Morbid Opportunist（{2}{B}｜Creature — Human Rogue） — Whenever one or more other creatures die, draw a card. This ability triggers only once each turn.
  - Mari, the Killing Quill（{1}{B}{B}｜Legendary Creature — Vampire Assassin） — Whenever a creature an opponent controls dies, exile it with a hit counter on it. Assassins, Mercenaries, and Rogues you control h
  - Nomad Outpost（｜Land） — This land enters tapped. {T}: Add {R}, {W}, or {B}.
  - Drumbellower（{2}{W}｜Creature — Spirit） — Flying Untap all creatures you control during each other player's untap step.


## The Reaper, King No More ｜ 夺命枉者
- 颜色 BRG ｜ 法术力值 6.0 ｜ 类型 Legendary Artifact Creature — Scarecrow
- 流行度：EDHREC 全时段第 470 位，约 6195 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.55
- 社区标签：－1/－1 指示物、偷取、控制、组合技、坟场复活、毒侵
- 完整牌面：When The Reaper enters, put a -1/-1 counter on each of up to two target creatures.
Whenever a creature an opponent controls with a -1/-1 counter on it dies, you may put that card onto the battlefield under your control. Do this only once each turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Blowfly Infestation（{2}{B}｜Enchantment） — Whenever a creature dies, if it had a -1/-1 counter on it, put a -1/-1 counter on target creature.
  2. The Scorpion God（{3}{B}{R}｜Legendary Creature — God） — Whenever a creature with a -1/-1 counter on it dies, draw a card. {1}{B}{R}: Put a -1/-1 counter on another target creature. When The Scorpion God dies, return it to its 
  3. Necroskitter（{1}{B}{B}｜Creature — Elemental） — Wither (This deals damage to creatures in the form of -1/-1 counters.) Whenever a creature an opponent controls with a -1/-1 counter on it dies, you may return that card 
  4. Hapatra, Vizier of Poisons（{B}{G}｜Legendary Creature — Human Cleric） — Whenever Hapatra deals combat damage to a player, you may put a -1/-1 counter on target creature. Whenever you put one or more -1/-1 counters on a creature, create a 1/1 
  5. Black Sun's Zenith（{X}{B}{B}｜Sorcery） — Put X -1/-1 counters on each creature. Shuffle Black Sun's Zenith into its owner's library.
  6. Massacre Girl, Known Killer（{2}{B}{B}｜Legendary Creature — Human Assassin） — Menace Creatures you control have wither. (They deal damage to creatures in the form of -1/-1 counters.) Whenever a creature an opponent controls dies, if its toughness w
- **出场率最高的牌**（大多数牌组都会放）
  - Ignoble Hierarch（{G}｜Creature — Goblin Shaman） — Exalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.) {T}: Add {B}, {R}, or {G}.
  - Dread Tiller（{1}{B}{G}｜Artifact Creature — Scarecrow） — When this creature enters, put a -1/-1 counter on target creature. Whenever a creature with a -1/-1 counter on it dies, you may pu
  - Kulrath Knight（{3}{B/R}{B/R}｜Creature — Elemental Knight） — Flying Wither (This deals damage to creatures in the form of -1/-1 counters.) Creatures your opponents control with counters on th
  - Everlasting Torment（{2}{B/R}｜Enchantment） — Players can't gain life. Damage can't be prevented. All damage is dealt as though its source had wither. (A source with wither dea
