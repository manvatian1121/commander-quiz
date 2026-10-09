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


## Scion of the Ur-Dragon ｜ 太初龙后裔
- 颜色 WUBRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Dragon Avatar
- 流行度：EDHREC 全时段第 509 位，约 5814 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.92 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $7.79
- 社区标签：龙、坟场复活、组合技、工具箱、飞行、优质单卡堆
- 完整牌面：Flying
{2}: Search your library for a Dragon permanent card and put it into your graveyard. If you do, Scion of the Ur-Dragon becomes a copy of that card until end of turn. Then shuffle.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Colossal Grave-Reaver（{6}{B}{G}｜Creature — Dragon） — Flying Whenever this creature enters or attacks, mill three cards. Whenever one or more creature cards are put into your graveyard from your library, put one of them onto
  2. Bladewing the Risen（{3}{B}{B}{R}{R}｜Legendary Creature — Zombie Dragon） — Flying When Bladewing enters, you may return target Dragon permanent card from your graveyard to the battlefield. {B}{R}: Dragon creatures get +1/+1 until end of turn.
  3. Reanimate（{B}｜Sorcery） — Put target creature card from a graveyard onto the battlefield under your control. You lose life equal to that card's mana value.
  4. Dragon Tempest（{1}{R}｜Enchantment） — Whenever a creature you control with flying enters, it gains haste until end of turn. Whenever a Dragon you control enters, it deals X damage to any target, where X is th
  5. Animate Dead（{1}{B}｜Enchantment — Aura） — Enchant creature card in a graveyard When this Aura enters, if it's on the battlefield, it loses "enchant creature card in a graveyard" and gains "enchant creature put on
  6. Crux of Fate（{3}{B}{B}｜Sorcery） — Choose one — • Destroy all Dragon creatures. • Destroy all non-Dragon creatures.
- **出场率最高的牌**（大多数牌组都会放）
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Miirym, Sentinel Wyrm（{3}{G}{U}{R}｜Legendary Creature — Dragon Spirit） — Flying, ward {2} Whenever another nontoken Dragon you control enters, create a token that's a copy of it, except the token isn't l
  - Verdant Catacombs（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Swamp or Forest card, put it onto the battlefield, then shuffle.
  - Bloodstained Mire（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Swamp or Mountain card, put it onto the battlefield, then shuffle.


## Rhys the Redeemed ｜ 复耀黎兹
- 颜色 WG ｜ 法术力值 1.0 ｜ 类型 Legendary Creature — Elf Warrior
- 流行度：EDHREC 全时段第 510 位，约 5810 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.31 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.72
- 社区标签：衍生物、妖精、增殖衍生物、＋1/＋1 指示物、加速、快攻
- 完整牌面：{2}{G/W}, {T}: Create a 1/1 green and white Elf Warrior creature token.
{4}{G/W}{G/W}, {T}: For each creature token you control, create a token that's a copy of that creature.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Parallel Lives（{3}{G}｜Enchantment） — If an effect would create one or more tokens under your control, it creates twice that many of those tokens instead.
  2. Elvish Archdruid（{1}{G}{G}｜Creature — Elf Druid） — Other Elf creatures you control get +1/+1. {T}: Add {G} for each Elf you control.
  3. Priest of Titania（{1}{G}｜Creature — Elf Druid） — {T}: Add {G} for each Elf on the battlefield.
  4. Imperious Perfect（{2}{G}｜Creature — Elf Warrior） — Other Elves you control get +1/+1. {G}, {T}: Create a 1/1 green Elf Warrior creature token.
  5. Anointed Procession（{3}{W}｜Enchantment） — If an effect would create one or more tokens under your control, it creates twice that many of those tokens instead.
  6. Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
- **出场率最高的牌**（大多数牌组都会放）
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Sunpetal Grove（｜Land） — This land enters tapped unless you control a Forest or a Plains. {T}: Add {G} or {W}.


## Jarad, Golgari Lich Lord ｜ 葛加理巫妖领主贾雷
- 颜色 BG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Zombie Elf
- 流行度：EDHREC 全时段第 512 位，约 5801 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.29 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $9.92
- 社区标签：坟场复活、坟场、挖掘、磨牌、自磨、牺牲
- 完整牌面：Jarad gets +1/+1 for each creature card in your graveyard.
{1}{B}{G}, Sacrifice another creature: Each opponent loses life equal to the sacrificed creature's power.
Sacrifice a Swamp and a Forest: Return this card from your graveyard to your hand.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Lord of Extinction（{3}{B}{G}｜Creature — Elemental） — Lord of Extinction's power and toughness are each equal to the number of cards in all graveyards.
  2. Splinterfright（{2}{G}｜Creature — Elemental） — Trample Splinterfright's power and toughness are each equal to the number of creature cards in your graveyard. At the beginning of your upkeep, mill two cards. (Put the t
  3. Old Stickfingers（{X}{B}{G}｜Legendary Creature — Horror） — When you cast this spell, reveal cards from the top of your library until you reveal X creature cards. Put all creature cards revealed this way into your graveyard, then 
  4. Skull Prophet（{B}{G}｜Creature — Human Druid） — {T}: Add {B} or {G}. {T}: Mill two cards. (Put the top two cards of your library into your graveyard.)
  5. Golgari Grave-Troll（{4}{G}｜Creature — Troll Skeleton） — This creature enters with a +1/+1 counter on it for each creature card in your graveyard. {1}, Remove a +1/+1 counter from this creature: Regenerate this creature. Dredge
  6. Nighthowler（{1}{B}{B}｜Enchantment Creature — Horror） — Bestow {2}{B}{B} (If you cast this card for its bestow cost, it's an Aura spell with enchant creature. It becomes a creature again if it's not attached.) This creature an
- **出场率最高的牌**（大多数牌组都会放）
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Sakura-Tribe Elder（{1}{G}｜Creature — Snake Shaman） — Sacrifice this creature: Search your library for a basic land card, put that card onto the battlefield tapped, then shuffle.
  - Eternal Witness（{1}{G}{G}｜Creature — Human Shaman） — When this creature enters, you may return target card from your graveyard to your hand.
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Anje Falkenrath ｜ 安姬伐肯纳
- 颜色 BR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Vampire
- 流行度：EDHREC 全时段第 513 位，约 5801 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.25 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：Madness、弃牌、组合技、坟场复活、自弃、循环
- 完整牌面：Haste
{T}, Discard a card: Draw a card.
Whenever you discard a card, if it has madness, untap Anje Falkenrath.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Big Game Hunter（{1}{B}{B}｜Creature — Human Rebel Assassin） — When this creature enters, destroy target creature with power 4 or greater. It can't be regenerated. Madness {B} (If you discard this card, discard it into exile. When yo
  2. Call to the Netherworld（{B}｜Sorcery） — Return target black creature card from your graveyard to your hand. Madness {0} (If you discard this card, discard it into exile. When you do, cast it for its madness cos
  3. Dark Withering（{4}{B}{B}｜Instant） — Destroy target nonblack creature. Madness {B} (If you discard this card, discard it into exile. When you do, cast it for its madness cost or put it into your graveyard.)
  4. Grave Scrabbler（{3}{B}｜Creature — Zombie） — Madness {1}{B} (If you discard this card, discard it into exile. When you do, cast it for its madness cost or put it into your graveyard.) When this creature enters, if i
  5. Fiery Temper（{1}{R}{R}｜Instant） — Fiery Temper deals 3 damage to any target. Madness {R} (If you discard this card, discard it into exile. When you do, cast it for its madness cost or put it into your gra
  6. Terminal Agony（{2}{B}{R}｜Sorcery） — Destroy target creature. Madness {B}{R} (If you discard this card, discard it into exile. When you do, cast it for its madness cost or put it into your graveyard.)
- **出场率最高的牌**（大多数牌组都会放）
  - Avacyn's Judgment（{1}{R}｜Sorcery） — Madness {X}{R} (If you discard this card, discard it into exile. When you do, cast it for its madness cost or put it into your gra
  - Gorgon Recluse（{3}{B}{B}｜Creature — Gorgon） — Whenever this creature blocks or becomes blocked by a nonblack creature, destroy that creature at end of combat. Madness {B}{B} (I
  - Anje's Ravager（{2}{R}｜Creature — Vampire Berserker） — This creature attacks each combat if able. Whenever this creature attacks, discard your hand, then draw three cards. Madness {1}{R
  - Murderous Compulsion（{1}{B}｜Sorcery） — Destroy target tapped creature. Madness {1}{B} (If you discard this card, discard it into exile. When you do, cast it for its madn


## Olivia, Opulent Outlaw ｜ 奢华狂徒奥莉薇亚
- 颜色 WBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Vampire Assassin
- 流行度：EDHREC 全时段第 514 位，约 5796 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.19 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.42
- 社区标签：宝物、＋1/＋1 指示物、Outlaws、衍生物、快攻、神器
- 完整牌面：Flying, lifelink
Whenever one or more outlaws you control deal combat damage to a player, create a Treasure token. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks are outlaws.)
{3}, Sacrifice two Treasures: Put two +1/+1 counters on each creature you control. Activate only as a sorcery.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Vihaan, Goldwaker（{R}{W}{B}｜Legendary Creature — Dwarf Warlock） — Other outlaws you control have vigilance and haste. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks are outlaws.) At the beginning of combat on your turn, you may 
  2. Mari, the Killing Quill（{1}{B}{B}｜Legendary Creature — Vampire Assassin） — Whenever a creature an opponent controls dies, exile it with a hit counter on it. Assassins, Mercenaries, and Rogues you control have deathtouch and "Whenever this creatu
  3. Back in Town（{X}{2}{B}｜Sorcery） — Return X target outlaw creature cards from your graveyard to the battlefield. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks are outlaws.)
  4. Queen Marchesa（{1}{R}{W}{B}｜Legendary Creature — Human Assassin） — Deathtouch, haste When Queen Marchesa enters, you become the monarch. At the beginning of your upkeep, if an opponent is the monarch, create a 1/1 black Assassin creature
  5. Captain Lannery Storm（{2}{R}｜Legendary Creature — Human Pirate） — Haste Whenever Captain Lannery Storm attacks, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.") Whenever you sacrif
  6. Rain of Riches（{3}{R}{R}｜Enchantment） — When this enchantment enters, create two Treasure tokens. The first spell you cast each turn that mana from a Treasure was spent to cast has cascade. (When you cast the s
- **出场率最高的牌**（大多数牌组都会放）
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Nomad Outpost（｜Land） — This land enters tapped. {T}: Add {R}, {W}, or {B}.
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.


## Gwen Stacy // Ghost-Spider ｜ 格温·史黛西
- 颜色 WUR ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Performer Hero // Legendary Creature — Spider Human Hero
- 流行度：EDHREC 全时段第 515 位，约 5761 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.39 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.48
- 社区标签：＋1/＋1 指示物、放逐、法术连发、冲动抽牌、烧血、组合技
- 完整牌面：When Gwen Stacy enters, exile the top card of your library. You may play that card for as long as you control this creature.
{2}{U}{R}{W}: Transform Gwen Stacy. Activate only as a sorcery.
//
Flying, vigilance, haste
Whenever you play a land from exile or cast a spell from exile, put a +1/+1 counter on Ghost-Spider.
Remove two counters from Ghost-Spider: Exile the top card of your library. You may play that card this turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Interdimensional Web Watch（{4}｜Artifact） — When this artifact enters, exile the top two cards of your library. Until the end of your next turn, you may play those cards. {T}: Add two mana in any combination of col
  2. Laelia, the Blade Reforged（{2}{R}｜Legendary Creature — Spirit Warrior） — Haste Whenever Laelia attacks, exile the top card of your library. You may play that card this turn. Whenever one or more cards are put into exile from your library and/o
  3. Vega, the Watcher（{1}{W}{U}｜Legendary Creature — Bird Spirit） — Flying Whenever you cast a spell from anywhere other than your hand, draw a card.
  4. Araña, Heart of the Spider（{1}{R}{W}｜Legendary Creature — Spider Human Hero） — Whenever you attack, put a +1/+1 counter on target attacking creature. Whenever a modified creature you control deals combat damage to a player, exile the top card of you
  5. Spider-Man 2099（{U}{R}｜Legendary Creature — Spider Human Hero） — From the Future — You can't cast Spider-Man 2099 during your first, second, or third turns of the game. Double strike, vigilance At the beginning of your end step, if you
  6. Party Thrasher（{1}{R}｜Creature — Lizard Wizard） — Noncreature spells you cast from exile have convoke. (Each creature you tap while casting a noncreature spell from exile pays for {1} or one mana of that creature's color
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Expressive Iteration（{U}{R}｜Sorcery） — Look at the top three cards of your library. Put one of them into your hand, put one of them on the bottom of your library, and ex
  - Talisman of Creativity（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {R}. This artifact deals 1 damage to you.
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.


## Alesha, Who Smiles at Death ｜ 蔑死者阿列莎
- 颜色 WBR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Warrior
- 流行度：EDHREC 全时段第 516 位，约 5760 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.35 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.23
- 社区标签：坟场复活、牺牲流、快攻、组合技、坟场、牺牲
- 完整牌面：First strike
Whenever Alesha attacks, you may pay {W/B}{W/B}. If you do, return target creature card with power 2 or less from your graveyard to the battlefield tapped and attacking.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Karmic Guide（{3}{W}{W}｜Creature — Angel Spirit） — Flying, protection from black Echo {3}{W}{W} (At the beginning of your upkeep, if this came under your control since the beginning of your last upkeep, sacrifice it unles
  2. Faithless Looting（{R}｜Sorcery） — Draw two cards, then discard two cards. Flashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then exile it.)
  3. Ravenous Chupacabra（{2}{B}{B}｜Creature — Beast Horror） — When this creature enters, destroy target creature an opponent controls.
  4. Buried Alive（{2}{B}｜Sorcery） — Search your library for up to three creature cards, put them into your graveyard, then shuffle.
  5. Solemn Simulacrum（{4}｜Artifact Creature — Golem） — When this creature enters, you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle. When this creature dies, you may dr
  6. Mentor of the Meek（{2}{W}｜Creature — Human Soldier） — Whenever another creature you control with power 2 or less enters, you may pay {1}. If you do, draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Nomad Outpost（｜Land） — This land enters tapped. {T}: Add {R}, {W}, or {B}.
  - Viscera Seer（{B}｜Creature — Vampire Wizard） — Sacrifice a creature: Scry 1. (Look at the top card of your library. You may put that card on the bottom.)
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.


## Aurelia, the Warleader ｜ 战领欧瑞梨
- 颜色 WR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Angel
- 流行度：EDHREC 全时段第 517 位，约 5758 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.67 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.25
- 社区标签：额外战斗、天使、快攻、装备、飞行、组合技
- 完整牌面：Flying, vigilance, haste
Whenever Aurelia attacks for the first time each turn, untap all creatures you control. After this phase, there is an additional combat phase.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Lyra Dawnbringer（{3}{W}{W}｜Legendary Creature — Angel） — Flying First strike (This creature deals combat damage before creatures without first strike.) Lifelink (Damage dealt by this creature also causes you to gain that much l
  2. Giada, Font of Hope（{1}{W}｜Legendary Creature — Angel） — Flying, vigilance Each other Angel you control enters with an additional +1/+1 counter on it for each Angel you already control. {T}: Add {W}. Spend this mana only to cas
  3. Gisela, Blade of Goldnight（{4}{R}{W}{W}｜Legendary Creature — Angel） — Flying, first strike If a source would deal damage to an opponent or a permanent an opponent controls, that source deals double that damage to that player or permanent in
  4. Aurelia, the Law Above（{3}{R}{W}｜Legendary Creature — Angel） — Flying, vigilance, haste Whenever a player attacks with three or more creatures, you draw a card. Whenever a player attacks with five or more creatures, Aurelia deals 3 d
  5. Helm of the Host（{4}｜Legendary Artifact — Equipment） — At the beginning of combat on your turn, create a token that's a copy of equipped creature, except the token isn't legendary. That token gains haste. Equip {5}
  6. Aurelia, Exemplar of Justice（{2}{R}{W}｜Legendary Creature — Angel） — Flying Mentor (Whenever this creature attacks, put a +1/+1 counter on target attacking creature with lesser power.) At the beginning of combat on your turn, choose up to 
- **出场率最高的牌**（大多数牌组都会放）
  - Boros Charm（{R}{W}｜Instant） — Choose one — • Boros Charm deals 4 damage to target player or planeswalker. • Permanents you control gain indestructible until end
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Boros Signet（{2}｜Artifact） — {1}, {T}: Add {R}{W}.


## Eirdu, Carrier of Dawn // Isilu, Carrier of Twilight ｜ 晨光神使埃尔度
- 颜色 WB ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Elemental God // Legendary Creature — Elemental God
- 流行度：EDHREC 全时段第 519 位，约 5699 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.95
- 社区标签：牺牲流、组合技、＋1/＋1 指示物、衍生物、－1/－1 指示物、坟场复活
- 完整牌面：Flying, lifelink
Creature spells you cast have convoke. (Your creatures can help cast those spells. Each creature you tap while casting a creature spell pays for {1} or one mana of that creature's color.)
At the beginning of your first main phase, you may pay {B}. If you do, transform Eirdu.
//
Flying, lifelink
Each other nontoken creature you control has persist. (When it dies, if it had no -1/-1 counters on it, return it to the battlefield under its owner's control with a -1/-1 counter on it.)
At the beginning of your first main phase, you may pay {W}. If you do, transform Isilu.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Vizier of Remedies（{1}{W}｜Creature — Human Cleric） — If one or more -1/-1 counters would be put on a creature you control, that many -1/-1 counters minus one are put on it instead.
  2. Viscera Seer（{B}｜Creature — Vampire Wizard） — Sacrifice a creature: Scry 1. (Look at the top card of your library. You may put that card on the bottom.)
  3. Umbral Collar Zealot（{1}{B}｜Creature — Human Cleric） — Sacrifice another creature or artifact: Surveil 1. (Look at the top card of your library. You may put it into your graveyard.)
  4. Mikaeus, the Unhallowed（{3}{B}{B}{B}｜Legendary Creature — Zombie Cleric） — Intimidate (This creature can't be blocked except by artifact creatures and/or creatures that share a color with it.) Whenever a Human deals damage to you, destroy it. Ot
  5. Cathars' Crusade（{3}{W}{W}｜Enchantment） — Whenever a creature you control enters, put a +1/+1 counter on each creature you control.
  6. Luminous Broodmoth（{2}{W}{W}｜Creature — Insect） — Flying Whenever a creature you control without flying dies, return it to the battlefield under its owner's control with a flying counter on it.
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Elas il-Kor, Sadistic Pilgrim（{W}{B}｜Legendary Creature — Phyrexian Kor Cleric） — Deathtouch Whenever another creature you control enters, you gain 1 life. Whenever another creature you control dies, each opponen
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.


## Toph, Hardheaded Teacher ｜ 固执师父拓芙
- 颜色 RG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Warrior Ally
- 流行度：EDHREC 全时段第 523 位，约 5661 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.94
- 社区标签：地牌核心、＋1/＋1 指示物、运土、地落、加速、牺牲流
- 完整牌面：When Toph enters, you may discard a card. If you do, return target instant or sorcery card from your graveyard to your hand.
Whenever you cast a spell, earthbend 1. If that spell is a Lesson, put an additional +1/+1 counter on that land. (Target land you control becomes a 0/0 creature with haste that's still a land. Put a +1/+1 counter on it. When it dies or is exiled, return it to the battlefield tapped.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Cycle of Renewal（{2}{G}｜Instant — Lesson） — Sacrifice a land. Search your library for up to two basic land cards, put them onto the battlefield tapped, then shuffle.
  2. Tannuk, Memorial Ensign（{1}{R}{G}｜Legendary Creature — Kavu Pilot） — Landfall — Whenever a land you control enters, Tannuk deals 1 damage to each opponent. If this is the second time this ability has resolved this turn, draw a card.
  3. Shared Roots（{1}{G}｜Sorcery — Lesson） — Search your library for a basic land card, put it onto the battlefield tapped, then shuffle.
  4. Ba Sing Se（｜Land） — This land enters tapped unless you control a basic land. {T}: Add {G}. {2}{G}, {T}: Earthbend 2. Activate only as a sorcery. (Target land you control becomes a 0/0 creatu
  5. Origin of Metalbending（{1}{G}｜Instant — Lesson） — Choose one — • Destroy target artifact or enchantment. • Put a +1/+1 counter on target creature you control. It gains indestructible until end of turn. (Damage and effect
  6. Spelunking（{2}{G}｜Enchantment） — When this enchantment enters, draw a card, then you may put a land card from your hand onto the battlefield. If you put a Cave onto the battlefield this way, you gain 4 l
- **出场率最高的牌**（大多数牌组都会放）
  - Earthbender Ascension（{2}{G}｜Enchantment） — When this enchantment enters, earthbend 2. Then search your library for a basic land card, put it onto the battlefield tapped, the
  - Harrow（{2}{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for up to two basic land cards, put them onto the 
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Gonti, Night Minister ｜ 晚市司贡提
- 颜色 B ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Aetherborn Rogue
- 流行度：EDHREC 全时段第 525 位，约 5642 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.48 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.94
- 社区标签：偷取、群体恩惠、宝物、群体折磨、混乱、不可阻挡
- 完整牌面：Whenever a player casts a spell they don't own, that player creates a Treasure token.
Whenever a creature deals combat damage to one of your opponents, its controller looks at the top card of that opponent's library and exiles it face down. They may play that card for as long as it remains exiled. Mana of any type can be spent to cast a spell this way.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Changeling Outcast（{B}｜Creature — Shapeshifter） — Changeling (This card is every creature type.) This creature can't block and can't be blocked.
  2. Tormented Soul（{B}｜Creature — Spirit） — This creature can't block and can't be blocked.
  3. Thieving Varmint（{1}{B}｜Creature — Varmint） — Deathtouch, lifelink {T}, Pay 1 life: Add two mana of any one color. Spend this mana only to cast spells you don't own.
  4. Cunning Rhetoric（{2}{B}｜Enchantment） — Whenever an opponent attacks you and/or one or more planeswalkers you control, exile the top card of that player's library. You may play that card for as long as it remai
  5. Gix, Yawgmoth Praetor（{1}{B}{B}｜Legendary Creature — Phyrexian Praetor） — Whenever a creature deals combat damage to one of your opponents, its controller may pay 1 life. If they do, they draw a card. {4}{B}{B}{B}, Discard X cards: Exile the to
  6. Gonti, Lord of Luxury（{2}{B}{B}｜Legendary Creature — Aetherborn Rogue） — Deathtouch When Gonti enters, look at the top four cards of target opponent's library, exile one of them face down, then put the rest on the bottom of that library in a r
- **出场率最高的牌**（大多数牌组都会放）
  - Dauthi Voidwalker（{B}{B}｜Creature — Dauthi Rogue） — Shadow (This creature can block or be blocked by only creatures with shadow.) If a card would be put into an opponent's graveyard 
  - Feed the Swarm（{1}{B}｜Sorcery） — Destroy target creature or enchantment an opponent controls. You lose life equal to that permanent's mana value.
  - Brainstealer Dragon（{5}{B}{B}｜Creature — Dragon Horror） — Flying At the beginning of your end step, exile the top card of each opponent's library. You may play those cards for as long as t
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.


## Altaïr Ibn-La'Ahad ｜ 阿泰尔·伊本·拉阿哈德
- 颜色 WBR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Assassin
- 流行度：EDHREC 全时段第 528 位，约 5635 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.78 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.37
- 社区标签：刺客、衍生物、快攻、坟场复活、史迹、额外战斗
- 完整牌面：First strike
Whenever Altaïr attacks, exile up to one target Assassin creature card from your graveyard with a memory counter on it. Then for each creature card you own in exile with a memory counter on it, create a tapped and attacking token that's a copy of it. Exile those tokens at end of combat.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Desmond Miles（{1}{B}｜Legendary Creature — Human Assassin） — Menace Desmond Miles gets +1/+0 for each other Assassin you control and each Assassin card in your graveyard. Whenever Desmond Miles deals combat damage to a player, surv
  2. Arno Dorian（{2}{B}{R}｜Legendary Creature — Human Assassin） — Deathtouch Other Assassins you control get +2/+0. Disguise {B}{R} (You may cast this card face down for {3} as a 2/2 creature with ward {2}. Turn it face up any time for 
  3. Bayek of Siwa（{3}{R}{W}｜Legendary Creature — Human Assassin） — Double strike During your turn, other historic creatures you control have double strike. Disguise {1}{R}{W} (You may cast this card face down for {3} as a 2/2 creature wi
  4. Aya of Alexandria（{2}{R}{W}｜Legendary Creature — Human Assassin） — Menace, lifelink Whenever a historic creature you control deals combat damage to a player, create a 1/1 black Assassin creature token with menace. (Artifacts, legendaries
  5. The Animus（{2}｜Legendary Artifact） — At the beginning of your end step, exile up to one target legendary creature card from a graveyard with a memory counter on it. {T}: Until your next turn, target legendar
  6. Olivia, Opulent Outlaw（{1}{R}{W}{B}｜Legendary Creature — Vampire Assassin） — Flying, lifelink Whenever one or more outlaws you control deal combat damage to a player, create a Treasure token. (Assassins, Mercenaries, Pirates, Rogues, and Warlocks 
- **出场率最高的牌**（大多数牌组都会放）
  - Queen Marchesa（{1}{R}{W}{B}｜Legendary Creature — Human Assassin） — Deathtouch, haste When Queen Marchesa enters, you become the monarch. At the beginning of your upkeep, if an opponent is the monar
  - Ruthless Lawbringer（{1}{W}{B}｜Creature — Vampire Assassin） — When this creature enters, you may sacrifice another creature. When you do, destroy target nonland permanent.
  - Mari, the Killing Quill（{1}{B}{B}｜Legendary Creature — Vampire Assassin） — Whenever a creature an opponent controls dies, exile it with a hit counter on it. Assassins, Mercenaries, and Rogues you control h
  - Faithless Looting（{R}｜Sorcery） — Draw two cards, then discard two cards. Flashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then 


## Quandrix, the Proof ｜ 启证巨龙量析
- 颜色 UG ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Elder Dragon
- 流行度：EDHREC 全时段第 530 位，约 5620 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.29
- 社区标签：倾曳、法术连发、加速、衍生物、地牌核心、额外回合
- 完整牌面：Flying, trample
Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. Put the exiled cards on the bottom in a random order.)
Instant and sorcery spells you cast from your hand have cascade.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Archmage Emeritus（{2}{U}{U}｜Creature — Human Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, draw a card.
  2. Dig Through Time（{6}{U}{U}｜Instant） — Delve (Each card you exile from your graveyard while casting this spell pays for {1}.) Look at the top seven cards of your library. Put two of them into your hand and the
  3. Treasure Cruise（{7}{U}｜Sorcery） — Delve (Each card you exile from your graveyard while casting this spell pays for {1}.) Draw three cards.
  4. Archmage of Runes（{3}{U}{U}｜Creature — Giant Wizard） — Instant and sorcery spells you cast cost {1} less to cast. Whenever you cast an instant or sorcery spell, draw a card.
  5. Imoti, Celebrant of Bounty（{3}{G}{U}｜Legendary Creature — Snake Druid） — Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. 
  6. Ancestral Vision（｜Sorcery） — Suspend 4—{U} (Rather than cast this card from your hand, pay {U} and exile it with four time counters on it. At the beginning of your upkeep, remove a time counter. When
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Dreamroot Cascade（｜Land） — This land enters tapped unless you control two or more other lands. {T}: Add {G} or {U}.
  - Growth Spiral（{G}{U}｜Instant） — Draw a card. You may put a land card from your hand onto the battlefield.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Sami, Wildcat Captain ｜ 私掠队长萨米
- 颜色 WR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Human Artificer Rogue
- 流行度：EDHREC 全时段第 531 位，约 5619 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.58 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.11
- 社区标签：神器、神器共鸣、组合技、风暴、衍生物、装备
- 完整牌面：Double strike, vigilance
Spells you cast have affinity for artifacts. (They cost {1} less to cast for each artifact you control.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Great Furnace（｜Artifact Land） — {T}: Add {R}.
  2. Ancient Den（｜Artifact Land） — {T}: Add {W}.
  3. Darksteel Citadel（｜Artifact Land） — Indestructible {T}: Add {C}.
  4. Mystic Forge（{4}｜Artifact） — You may look at the top card of your library any time. You may cast artifact spells and colorless spells from the top of your library. {T}, Pay 1 life: Exile the top card
  5. The Endstone（{7}｜Legendary Artifact） — Whenever you play a land or cast a spell, draw a card. At the beginning of your end step, your life total becomes half your starting life total, rounded up.
  6. Rustvale Bridge（｜Artifact Land） — This land enters tapped. Indestructible {T}: Add {R} or {W}.
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Conviction（{2}｜Artifact） — {T}: Add {C}. {T}: Add {R} or {W}. This artifact deals 1 damage to you.
  - Sacred Foundry（｜Land — Mountain Plains） — ({T}: Add {R} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Boros Signet（{2}｜Artifact） — {1}, {T}: Add {R}{W}.
  - Battlefield Forge（｜Land） — {T}: Add {C}. {T}: Add {R} or {W}. This land deals 1 damage to you.


## Raphael, Fiendish Savior ｜ 炼狱救星拉斐尔
- 颜色 BR ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Devil Noble
- 流行度：EDHREC 全时段第 535 位，约 5555 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.28 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.55
- 社区标签：恶魔、牺牲流、Devils、生命增益、烧血、衍生物
- 完整牌面：Flying
Other Demons, Devils, Imps, and Tieflings you control get +1/+1 and have lifelink.
At the beginning of each end step, if a creature card was put into your graveyard from anywhere this turn, create a 1/1 red Devil creature token with "When this token dies, it deals 1 damage to any target."
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Zurzoth, Chaos Rider（{2}{R}｜Legendary Creature — Devil） — Whenever an opponent draws their first card each turn, if it's not their turn, you create a 1/1 red Devil creature token with "When this token dies, it deals 1 damage to 
  2. Mahadi, Emporium Master（{1}{B}{R}｜Legendary Creature — Devil） — At the beginning of your end step, create a Treasure token for each creature that died this turn. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any c
  3. Rakdos, the Showstopper（{4}{B}{R}｜Legendary Creature — Demon） — Flying, trample When Rakdos enters, flip a coin for each creature that isn't a Demon, Devil, or Imp. Destroy each creature whose coin comes up tails.
  4. Witty Roastmaster（{2}{R}｜Creature — Devil Citizen） — Alliance — Whenever another creature you control enters, this creature deals 1 damage to each opponent.
  5. Zariel, Archduke of Avernus（{2}{R}{R}｜Legendary Planeswalker — Zariel） — +1: Creatures you control get +1/+0 and gain haste until end of turn. 0: Create a 1/1 red Devil creature token with "When this token dies, it deals 1 damage to any target
  6. Burn Down the House（{3}{R}{R}｜Sorcery） — Choose one — • Burn Down the House deals 5 damage to each creature and each planeswalker. • Create three 1/1 red Devil creature tokens with "When this token dies, it deal
- **出场率最高的牌**（大多数牌组都会放）
  - Mayhem Devil（{1}{B}{R}｜Creature — Devil） — Whenever a player sacrifices a permanent, this creature deals 1 damage to any target.
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.
  - Kardur, Doomscourge（{2}{B}{R}｜Legendary Creature — Demon Berserker） — When Kardur enters, until your next turn, creatures your opponents control attack each combat if able and attack a player other th
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.


## Miles Morales // Ultimate Spider-Man ｜ 迈尔斯·莫拉莱斯
- 颜色 WRG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Citizen Hero // Legendary Creature — Spider Human Hero
- 流行度：EDHREC 全时段第 536 位，约 5555 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.88 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.18
- 社区标签：＋1/＋1 指示物、传奇、蜘蛛、快攻、史迹、英雄
- 完整牌面：When Miles Morales enters, put a +1/+1 counter on each of up to two target creatures.
{3}{R}{G}{W}: Transform Miles Morales. Activate only as a sorcery.
//
First strike, haste
Camouflage — {2}: Put a +1/+1 counter on Ultimate Spider-Man. He gains hexproof and becomes colorless until end of turn.
Whenever you attack, double the number of each kind of counter on each Spider and legendary creature you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Spider-Punk（{1}{R}｜Legendary Creature — Spider Human Hero） — Riot (This creature enters with your choice of a +1/+1 counter or haste.) Other Spiders you control have riot. Spells and abilities can't be countered. Damage can't be pr
  2. Spider-Man India（{3}{G}{W}｜Legendary Creature — Spider Human Hero） — Web-slinging {1}{G}{W} (You may cast this spell for {1}{G}{W} if you also return a tapped creature you control to its owner's hand.) Pavitr's Sevā — Whenever you cast a c
  3. Araña, Heart of the Spider（{1}{R}{W}｜Legendary Creature — Spider Human Hero） — Whenever you attack, put a +1/+1 counter on target attacking creature. Whenever a modified creature you control deals combat damage to a player, exile the top card of you
  4. Scarlet Spider, Ben Reilly（{1}{R}{G}｜Legendary Creature — Spider Human Hero） — Web-slinging {R}{G} (You may cast this spell for {R}{G} if you also return a tapped creature you control to its owner's hand.) Trample Sensational Save — If Scarlet Spide
  5. Radioactive Spider（{G}｜Creature — Spider） — Reach, deathtouch Fateful Bite — {2}, Sacrifice this creature: Search your library for a Spider Hero card, reveal it, put it into your hand, then shuffle. Activate only a
  6. Spectacular Spider-Man（{1}{W}｜Legendary Creature — Spider Human Hero） — Flash {1}: Spectacular Spider-Man gains flying until end of turn. {1}, Sacrifice Spectacular Spider-Man: Creatures you control gain hexproof and indestructible until end 
- **出场率最高的牌**（大多数牌组都会放）
  - Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  - Spider-Man, Miles Morales（{4}{G}{G}｜Legendary Creature — Spider Human Hero） — Vigilance, trample (Attacking doesn't cause this creature to tap. He can deal excess combat damage to the player he's attacking.) 
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Aunt May（{W}｜Legendary Creature — Human Citizen） — Whenever another creature you control enters, you gain 1 life. If it's a Spider, put a +1/+1 counter on it.


## Yuna, Hope of Spira ｜ 史匹拉之望尤娜
- 颜色 WG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Cleric
- 流行度：EDHREC 全时段第 537 位，约 5548 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.51 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.74
- 社区标签：结界流、坟场复活、传纪、生命增益、＋1/＋1 指示物、中速
- 完整牌面：During your turn, Yuna and enchantment creatures you control have trample, lifelink, and ward {2}.
At the beginning of your end step, return up to one target enchantment card from your graveyard to the battlefield with a finality counter on it. (If a permanent with a finality counter on it would be put into a graveyard from the battlefield, exile it instead.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sythis, Harvest's Hand（{G}{W}｜Legendary Enchantment Creature — Nymph） — Whenever you cast an enchantment spell, you gain 1 life and draw a card.
  2. Summon: Titan（{3}{G}{G}｜Enchantment Creature — Saga Giant） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Mill five cards. II — Return all land cards from your graveyard to the battle
  3. Summon: Fenrir（{2}{G}｜Enchantment Creature — Saga Wolf） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Crescent Fang — Search your library for a basic land card, put it onto the ba
  4. Summon: Bahamut（{9}｜Enchantment Creature — Saga Dragon） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after IV.) I, II — Destroy up to one target nonland permanent. III — Draw two cards. IV — Meg
  5. Summon: Yojimbo（{3}{W}｜Enchantment Creature — Saga Samurai） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after IV.) I — Exile target artifact, enchantment, or tapped creature an opponent controls. I
  6. Summon: Knights of Round（{6}{W}{W}｜Enchantment Creature — Saga Knight） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after V.) I, II, III, IV — Create three 2/2 white Knight creature tokens. V — Ultimate End — 
- **出场率最高的牌**（大多数牌组都会放）
  - Sanctum Weaver（{1}{G}｜Enchantment Creature — Dryad） — {T}: Add X mana of any one color, where X is the number of enchantments you control.
  - Eidolon of Blossoms（{2}{G}{G}｜Enchantment Creature — Spirit） — Constellation — Whenever this creature or another enchantment you control enters, draw a card.
  - Jukai Naturalist（{G}{W}｜Enchantment Creature — Human Monk） — Lifelink Enchantment spells you cast cost {1} less to cast.
  - Enchantress's Presence（{2}{G}｜Enchantment） — Whenever you cast an enchantment spell, draw a card.


## Goreclaw, Terror of Qal Sisma ｜ 黑山之威血爪
- 颜色 G ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Bear
- 流行度：EDHREC 全时段第 538 位，约 5542 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.28 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.20
- 社区标签：加速、快攻、大生物、＋1/＋1 指示物、爆费、优质单卡堆
- 完整牌面：Creature spells you cast with power 4 or greater cost {2} less to cast.
Whenever Goreclaw attacks, each creature you control with power 4 or greater gets +1/+1 and gains trample until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Garruk's Packleader（{4}{G}｜Creature — Beast） — Whenever another creature you control with power 3 or greater enters, you may draw a card.
  2. Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess combat damage to the player or planeswalker
  3. Outcaster Trailblazer（{2}{G}｜Creature — Human Druid） — When this creature enters, add one mana of any color. Whenever another creature you control with power 4 or greater enters, draw a card. Plot {2}{G} (You may pay {2}{G} a
  4. Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. (Each of those creatures can deal excess
  5. Ilysian Caryatid（{1}{G}｜Creature — Plant） — {T}: Add one mana of any color. If you control a creature with power 4 or greater, add two mana of any one color instead.
  6. Soul of the Harvest（{4}{G}{G}｜Creature — Elemental） — Trample Whenever another nontoken creature you control enters, you may draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Emerald Medallion（{2}｜Artifact） — Green spells you cast cost {1} less to cast.
  - Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Mosswort Bridge（｜Land） — Hideaway 4 (When this land enters, look at the top four cards of your library, exile one face down, then put the rest on the botto


## Jan Jansen, Chaos Crafter ｜ 混沌械匠姚恩姚森
- 颜色 WBR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Gnome Artificer
- 流行度：EDHREC 全时段第 539 位，约 5528 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.22 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.49
- 社区标签：神器、宝物、衍生物、牺牲流、组合技、牺牲
- 完整牌面：Haste
{T}, Sacrifice an artifact creature: Create two Treasure tokens.
{T}, Sacrifice a noncreature artifact: Create two 1/1 colorless Construct artifact creature tokens.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Academy Manufactor（{3}｜Artifact Creature — Assembly-Worker） — If you would create a Clue, Food, or Treasure token, instead create one of each.
  2. Ichor Wellspring（{2}｜Artifact） — When this artifact enters or is put into a graveyard from the battlefield, draw a card.
  3. Reckless Fireweaver（{1}{R}｜Creature — Human Artificer） — Whenever an artifact you control enters, this creature deals 1 damage to each opponent.
  4. Liquimetal Torque（{2}｜Artifact） — {T}: Add {C}. {T}: Target nonland permanent becomes an artifact in addition to its other types until end of turn.
  5. Clock of Omens（{4}｜Artifact） — Tap two untapped artifacts you control: Untap target artifact.
  6. Marionette Apprentice（{1}{B}｜Creature — Human Artificer） — Fabricate 1 (When this creature enters, put a +1/+1 counter on it or create a 1/1 colorless Servo artifact creature token.) Whenever another creature or artifact you cont
- **出场率最高的牌**（大多数牌组都会放）
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  - Mirkwood Bats（{3}{B}｜Creature — Bat） — Flying Whenever you create or sacrifice a token, each opponent loses 1 life.
  - Mayhem Devil（{1}{B}{R}｜Creature — Devil） — Whenever a player sacrifices a permanent, this creature deals 1 damage to any target.
  - Deadly Dispute（{1}{B}｜Instant） — As an additional cost to cast this spell, sacrifice an artifact or creature. Draw two cards and create a Treasure token. (It's an 


## Kyler, Sigardian Emissary ｜ 席嘉妲密使凯勒尔
- 颜色 WG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Cleric
- 流行度：EDHREC 全时段第 541 位，约 5503 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.35 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.65
- 社区标签：＋1/＋1 指示物、人类、衍生物、快攻、中速、群体加成
- 完整牌面：Whenever another Human you control enters, put a +1/+1 counter on Kyler.
Other Humans you control get +1/+1 for each counter on Kyler.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Heronblade Elite（{2}{G}｜Creature — Human Warrior） — Vigilance Whenever another Human you control enters, put a +1/+1 counter on this creature. {T}: Add X mana of any one color, where X is this creature's power.
  2. Katilda, Dawnhart Prime（{G}{W}｜Legendary Creature — Human Warlock） — Protection from Werewolves Human creatures you control have "{T}: Add one mana of any of this creature's colors." {4}{G}{W}, {T}: Put a +1/+1 counter on each creature you
  3. Torens, Fist of the Angels（{1}{G}{W}｜Legendary Creature — Human Cleric） — Training (Whenever this creature attacks with another creature with greater power, put a +1/+1 counter on this creature.) Whenever you cast a creature spell, create a 1/1
  4. Champion of Lambholt（{1}{G}{G}｜Creature — Human Warrior） — Creatures with power less than this creature's power can't block creatures you control. Whenever another creature you control enters, put a +1/+1 counter on this creature
  5. Horn of Gondor（{3}｜Legendary Artifact） — When Horn of Gondor enters, create a 1/1 white Human Soldier creature token. {3}, {T}: Create X 1/1 white Human Soldier creature tokens, where X is the number of Humans y
  6. Adeline, Resplendent Cathar（{1}{W}{W}｜Legendary Creature — Human Knight） — Vigilance Adeline's power is equal to the number of creatures you control. Whenever you attack, for each opponent, create a 1/1 white Human creature token that's tapped a
- **出场率最高的牌**（大多数牌组都会放）
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Avacyn's Pilgrim（{G}｜Creature — Human Monk） — {T}: Add {W}.
  - Fortified Village（｜Land） — As this land enters, you may reveal a Forest or Plains card from your hand. If you don't, this land enters tapped. {T}: Add {G} or
  - Bastion Protector（{2}{W}｜Creature — Human Soldier） — Commander creatures you control get +2/+2 and have indestructible.


## Faldorn, Dread Wolf Herald ｜ 惧栗狼使法多
- 颜色 RG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Druid
- 流行度：EDHREC 全时段第 542 位，约 5496 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.29 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：放逐、衍生物、倾曳、狼、冲动抽牌、快攻
- 完整牌面：Whenever you cast a spell from exile or a land you control enters from exile, create a 2/2 green Wolf creature token.
{1}, {T}, Discard a card: Exile the top card of your library. You may play it this turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Laelia, the Blade Reforged（{2}{R}｜Legendary Creature — Spirit Warrior） — Haste Whenever Laelia attacks, exile the top card of your library. You may play that card this turn. Whenever one or more cards are put into exile from your library and/o
  2. Escape to the Wilds（{3}{R}{G}｜Sorcery） — Exile the top five cards of your library. You may play cards exiled this way until the end of your next turn. You may play an additional land this turn.
  3. Delayed Blast Fireball（{1}{R}{R}｜Instant） — Delayed Blast Fireball deals 2 damage to each opponent and each creature they control. If this spell was cast from exile, it deals 5 damage to each opponent and each crea
  4. Wild-Magic Sorcerer（{3}{R}｜Creature — Orc Shaman Sorcerer） — The first spell you cast from exile each turn has cascade. (When you cast your first spell from exile, exile cards from the top of your library until you exile a nonland 
  5. Light Up the Stage（{2}{R}｜Sorcery） — Spectacle {R} (You may cast this spell for its spectacle cost rather than its mana cost if an opponent lost life this turn.) Exile the top two cards of your library. Unti
  6. Ignite the Future（{3}{R}｜Sorcery） — Exile the top three cards of your library. Until the end of your next turn, you may play those cards. If this spell was cast from a graveyard, you may play cards this way
- **出场率最高的牌**（大多数牌组都会放）
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Mosswort Bridge（｜Land） — Hideaway 4 (When this land enters, look at the top four cards of your library, exile one face down, then put the rest on the botto
  - Jeska's Will（{2}{R}｜Sorcery） — Choose one. If you control a commander as you cast this spell, you may choose both instead. • Add {R} for each card in target oppo
  - Passionate Archaeologist（{1}{R}｜Legendary Enchantment — Background） — Commander creatures you own have "Whenever you cast a spell from exile, this creature deals damage equal to that spell's mana valu


## Xantcha, Sleeper Agent ｜ 潜藏密探珊迦
- 颜色 BR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Phyrexian Minion
- 流行度：EDHREC 全时段第 543 位，约 5493 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.41 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.89
- 社区标签：强制战斗、群体折磨、混乱、烧血、控制、群体恩惠
- 完整牌面：Xantcha enters under the control of an opponent of your choice.
Xantcha attacks each combat if able and can't attack its owner or planeswalkers its owner controls.
{3}: Xantcha's controller loses 2 life and you draw a card. Any player may activate this ability.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Shiny Impetus（{2}{R}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +2/+2 and is goaded. (It attacks each combat if able and attacks a player other than you if able.) Whenever enchanted creature at
  2. Curse of Opulence（{R}｜Enchantment — Aura Curse） — Enchant player Whenever enchanted player is attacked, create a Gold token. Each opponent attacking that player does the same. (A Gold token is an artifact with "Sacrifice
  3. Bloodthirsty Blade（{2}｜Artifact — Equipment） — Equipped creature gets +2/+0 and is goaded. (It attacks each combat if able and attacks a player other than you if able.) {1}: Attach this Equipment to target creature an
  4. Disrupt Decorum（{2}{R}{R}｜Sorcery） — Goad all creatures you don't control. (Until your next turn, those creatures attack each combat if able and attack a player other than you if able.)
  5. Alexios, Deimos of Kosmos（{3}{R}｜Legendary Creature — Human Berserker） — Trample Alexios attacks each combat if able, can't be sacrificed, and can't attack its owner. At the beginning of each player's upkeep, that player gains control of Alexi
  6. Heartstone（{3}｜Artifact） — Activated abilities of creatures cost {1} less to activate. This effect can't reduce the mana in that cost to less than one mana.
- **出场率最高的牌**（大多数牌组都会放）
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.
  - Kardur, Doomscourge（{2}{B}{R}｜Legendary Creature — Demon Berserker） — When Kardur enters, until your next turn, creatures your opponents control attack each combat if able and attack a player other th
  - Rakdos Signet（{2}｜Artifact） — {1}, {T}: Add {B}{R}.


## Zask, Skittering Swarmlord ｜ 掠行群长札嘶克
- 颜色 BG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Insect
- 流行度：EDHREC 全时段第 544 位，约 5487 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.6 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $26.03
- 社区标签：昆虫、坟场复活、衍生物、坟场、自磨、磨牌
- 完整牌面：You may play lands and cast Insect spells from your graveyard.
Whenever another Insect you control dies, put it on the bottom of its owner's library, then mill two cards. (Put the top two cards of your library into your graveyard.)
{1}{B/G}: Target Insect gets +1/+0 and gains deathtouch until end of turn. ({B/G} can be paid with either {B} or {G}.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Grist, the Hunger Tide（{1}{B}{G}｜Legendary Planeswalker — Grist） — As long as Grist isn't on the battlefield, it's a 1/1 Insect creature in addition to its other types. +1: Create a 1/1 black and green Insect creature token, then mill a 
  2. Caustic Caterpillar（{G}｜Creature — Insect） — {1}{G}, Sacrifice this creature: Destroy target artifact or enchantment.
  3. Grist, Voracious Larva（｜） — 
  4. Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create a token that's a copy of this creature i
  5. Aatchik, Emerald Radian（{3}{B}{B}{G}｜Legendary Creature — Insect Druid） — When Aatchik enters, create a 1/1 green Insect creature token for each artifact and/or creature card in your graveyard. Whenever another Insect you control dies, put a +1
  6. Amzu, Swarm's Hunger（{3}{B}{G}｜Legendary Creature — Insect Shaman） — Flying, menace Other Insects you control have menace. Whenever one or more cards leave your graveyard, you may create a 1/1 black and green Insect creature token, then pu
- **出场率最高的牌**（大多数牌组都会放）
  - Haywire Mite（{1}｜Artifact Creature — Insect） — When this creature dies, you gain 2 life. {G}, Sacrifice this creature: Exile target noncreature artifact or noncreature enchantme
  - Hornet Queen（{4}{G}{G}{G}｜Creature — Insect） — Flying, deathtouch When this creature enters, create four 1/1 green Insect creature tokens with flying and deathtouch.
  - Crawling Sensation（{2}{G}｜Enchantment） — At the beginning of your upkeep, you may mill two cards. (You may put the top two cards of your library into your graveyard.) When
  - Swarmyard（｜Land） — {T}: Add {C}. {T}: Regenerate target Insect, Rat, Spider, or Squirrel. (The next time it would be destroyed this turn, instead tap


## Tamiyo, Inquisitive Student // Tamiyo, Seasoned Scholar ｜ 好问学徒多美代
- 颜色 UG ｜ 法术力值 1.0 ｜ 类型 Legendary Creature — Moonfolk Wizard // Legendary Planeswalker — Tamiyo
- 流行度：EDHREC 全时段第 545 位，约 5478 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.3 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $18.63
- 社区标签：组合技、换手牌、抽牌、小牌抽、控制、Clues
- 完整牌面：Flying
Whenever Tamiyo attacks, investigate. (Create a Clue token. It's an artifact with "{2}, Sacrifice this token: Draw a card.")
When you draw your third card in a turn, exile Tamiyo, then return her to the battlefield transformed under her owner's control.
//
+2: Until your next turn, whenever a creature attacks you or a planeswalker you control, it gets -1/-0 until end of turn.
−3: Return target instant or sorcery card from your graveyard to your hand. If it's a green card, add one mana of any color.
−7: Draw cards equal to half the number of cards in your library, rounded up. You get an emblem with "You have no maximum hand size."
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  2. Flux Channeler（{2}{U}｜Creature — Human Wizard） — Whenever you cast a noncreature spell, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
  3. Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.
  4. Dreamtide Whale（{2}{U}｜Creature — Whale） — Vanishing 2 (This creature enters with two time counters on it. At the beginning of your upkeep, remove a time counter from it. When the last is removed, sacrifice it.) W
  5. Chart a Course（{1}{U}｜Sorcery） — Draw two cards. Then discard a card unless you attacked this turn.
  6. Psychosis Crawler（{5}｜Artifact Creature — Phyrexian Horror） — Psychosis Crawler's power and toughness are each equal to the number of cards in your hand. Whenever you draw a card, each opponent loses 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Yavimaya Coast（｜Land） — {T}: Add {C}. {T}: Add {G} or {U}. This land deals 1 damage to you.
  - Rejuvenating Springs（｜Land） — This land enters tapped unless you have two or more opponents. {T}: Add {G} or {U}.


## Taii Wakeen, Perfect Shot ｜ 精准射手泰依瓦肯
- 颜色 WR ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Mercenary
- 流行度：EDHREC 全时段第 548 位，约 5464 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.44 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.24
- 社区标签：烧血、法术连发、控制、点伤、组合技、衍生物
- 完整牌面：Whenever a source you control deals noncombat damage to a creature equal to that creature's toughness, draw a card.
{X}, {T}: If a source you control would deal noncombat damage to a permanent or player this turn, it deals that much damage plus X instead.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. End the Festivities（{R}｜Sorcery） — End the Festivities deals 1 damage to each opponent and each creature and planeswalker they control.
  2. Tectonic Hazard（{R}｜Sorcery） — Tectonic Hazard deals 1 damage to each opponent and each creature they control.
  3. Blazing Volley（{R}｜Sorcery） — Blazing Volley deals 1 damage to each creature your opponents control.
  4. Electrickery（{R}｜Instant） — Electrickery deals 1 damage to target creature you don't control. Overload {1}{R} (You may cast this spell for its overload cost. If you do, change "target" in its text t
  5. Lightning Bolt（{R}｜Instant） — Lightning Bolt deals 3 damage to any target.
  6. Grapeshot（{1}{R}｜Sorcery） — Grapeshot deals 1 damage to any target. Storm (When you cast this spell, copy it for each spell cast before it this turn. You may choose new targets for the copies.)
- **出场率最高的牌**（大多数牌组都会放）
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Battlefield Forge（｜Land） — {T}: Add {C}. {T}: Add {R} or {W}. This land deals 1 damage to you.
  - Heartflame Duelist（｜） — 
  - Fiery Confluence（{2}{R}{R}｜Sorcery） — Choose three. You may choose the same mode more than once. • Fiery Confluence deals 1 damage to each creature. • Fiery Confluence 


## Minthara, Merciless Soul ｜ 冷酷无情的明萨拉
- 颜色 WB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Elf Cleric
- 流行度：EDHREC 全时段第 549 位，约 5446 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.33 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.22
- 社区标签：衍生物、牺牲流、牺牲、闪现回场、经验指示物、增殖
- 完整牌面：Minthara has ward {X}, where X is the number of experience counters you have.
At the beginning of your end step, if a permanent you controlled left the battlefield this turn, you get an experience counter.
Creatures you control get +1/+0 for each experience counter you have.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Metastatic Evangel（{1}{W}｜Creature — Phyrexian Human Cleric） — Whenever another nontoken creature you control enters, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already t
  2. Grateful Apparition（{1}{W}｜Creature — Spirit） — Flying Whenever this creature deals combat damage to a player or planeswalker, proliferate. (Choose any number of permanents and/or players, then give each another counte
  3. Lae'zel, Vlaakith's Champion（{2}{W}｜Legendary Creature — Gith Warrior） — If you would put one or more counters on a creature or planeswalker you control or on yourself, put that many plus one of each of those kinds of counters on that permanen
  4. Shadowheart, Dark Justiciar（{3}{B}｜Legendary Creature — Human Elf Cleric） — {1}{B}, {T}, Sacrifice another creature: Draw X cards, where X is that creature's power. Choose a Background (You can have a Background as a second commander.)
  5. Nested Shambler（{B}｜Creature — Zombie） — When this creature dies, create X tapped 1/1 green Squirrel creature tokens, where X is this creature's power.
  6. Hidden Stockpile（{W}{B}｜Enchantment） — Revolt — At the beginning of your end step, if a permanent left the battlefield under your control this turn, create a 1/1 colorless Servo artifact creature token. {1}, S
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Deadly Dispute（{1}{B}｜Instant） — As an additional cost to cast this spell, sacrifice an artifact or creature. Draw two cards and create a Treasure token. (It's an 
  - Orzhov Basilica（｜Land） — This land enters tapped. When this land enters, return a land you control to its owner's hand. {T}: Add {W}{B}.
  - Karn's Bastion（｜Land） — {T}: Add {C}. {4}, {T}: Proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind 


## Liliana, Heretical Healer // Liliana, Defiant Necromancer ｜ 异端治疗师莉莲娜
- 颜色 B ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Cleric // Legendary Planeswalker — Liliana
- 流行度：EDHREC 全时段第 550 位，约 5428 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.45 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.06
- 社区标签：僵尸、坟场复活、弃牌、鹏洛客、坟场、牺牲流
- 完整牌面：Lifelink
Whenever another nontoken creature you control dies, exile Liliana, Heretical Healer, then return her to the battlefield transformed under her owner's control. If you do, create a 2/2 black Zombie creature token.
//
+2: Each player discards a card.
−X: Return target nonlegendary creature card with mana value X from your graveyard to the battlefield.
−8: You get an emblem with "Whenever a creature dies, return it to the battlefield under your control at the beginning of the next end step."
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Liliana, Death's Majesty（{3}{B}{B}｜Legendary Planeswalker — Liliana） — +1: Create a 2/2 black Zombie creature token. Mill two cards. −3: Return target creature card from your graveyard to the battlefield. That creature is a black Zombie in a
  2. Liliana, Dreadhorde General（{4}{B}{B}｜Legendary Planeswalker — Liliana） — Whenever a creature you control dies, draw a card. +1: Create a 2/2 black Zombie creature token. −4: Each player sacrifices two creatures of their choice. −9: Each oppone
  3. Liliana's Triumph（{1}{B}｜Instant） — Each opponent sacrifices a creature of their choice. If you control a Liliana planeswalker, each opponent also discards a card.
  4. Liliana, the Last Hope（{1}{B}{B}｜Legendary Planeswalker — Liliana） — +1: Up to one target creature gets -2/-1 until your next turn. −2: Mill two cards, then you may return a creature card from your graveyard to your hand. −7: You get an em
  5. Liliana Vess（{3}{B}{B}｜Legendary Planeswalker — Liliana） — +1: Target player discards a card. −2: Search your library for a card, then shuffle and put that card on top. −8: Put all creature cards from all graveyards onto the batt
  6. Liliana, Waker of the Dead（{2}{B}{B}｜Legendary Planeswalker — Liliana） — +1: Each player discards a card. Each opponent who can't loses 3 life. −3: Target creature gets -X/-X until end of turn, where X is the number of cards in your graveyard.
- **出场率最高的牌**（大多数牌组都会放）
  - Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost thi
  - Liliana of the Dark Realms（{2}{B}{B}｜Legendary Planeswalker — Liliana） — +1: Search your library for a Swamp card, reveal it, put it into your hand, then shuffle. −3: Target creature gets +X/+X or -X/-X 
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.


## Ghoulcaller Gisa ｜ 尸鬼牧者基沙
- 颜色 B ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Wizard
- 流行度：EDHREC 全时段第 555 位，约 5389 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.19 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $4.24
- 社区标签：僵尸、衍生物、坟场复活、牺牲流、牺牲、坟场
- 完整牌面：{B}, {T}, Sacrifice another creature: Create X 2/2 black Zombie creature tokens, where X is the sacrificed creature's power.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Lord of the Accursed（{2}{B}｜Creature — Zombie） — Other Zombies you control get +1/+1. {1}{B}, {T}: All Zombies gain menace until end of turn.
  2. Death Baron（{1}{B}{B}｜Creature — Zombie Wizard） — Skeletons you control and other Zombies you control get +1/+1 and have deathtouch. (Any amount of damage they deal to a creature is enough to destroy it.)
  3. Champion of the Perished（{B}｜Creature — Zombie） — Whenever another Zombie you control enters, put a +1/+1 counter on this creature.
  4. Cemetery Reaper（{1}{B}{B}｜Creature — Zombie） — Other Zombie creatures you control get +1/+1. {2}{B}, {T}: Exile target creature card from a graveyard. Create a 2/2 black Zombie creature token.
  5. Undead Augur（{B}{B}｜Creature — Zombie Wizard） — Whenever this creature or another Zombie you control dies, you draw a card and lose 1 life.
  6. Endless Ranks of the Dead（{2}{B}{B}｜Enchantment） — At the beginning of your upkeep, create X 2/2 black Zombie creature tokens, where X is half the number of Zombies you control, rounded down.
- **出场率最高的牌**（大多数牌组都会放）
  - Gravecrawler（{B}｜Creature — Zombie） — This creature can't block. You may cast this card from your graveyard as long as you control a Zombie.
  - Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost thi
  - Undead Warchief（{2}{B}{B}｜Creature — Zombie） — Zombie spells you cast cost {1} less to cast. Zombie creatures you control get +2/+1.
  - Diregraf Colossus（{2}{B}｜Creature — Zombie Giant） — This creature enters with a +1/+1 counter on it for each Zombie card in your graveyard. Whenever you cast a Zombie spell, create a


## Neera, Wild Mage ｜ 狂野法师妮拉
- 颜色 UR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Human Elf Shaman
- 流行度：EDHREC 全时段第 555 位，约 5387 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.47 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.30
- 社区标签：混乱、法术连发、牌库顶、爆费、风暴、组合技
- 完整牌面：Whenever you cast a spell, you may put it on the bottom of its owner's library. If you do, reveal cards from the top of your library until you reveal a nonland card. You may cast that card without paying its mana cost. Then put all revealed cards not cast this way on the bottom of your library in a random order. This ability triggers only once each turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. One with the Multiverse（{6}{U}{U}｜Enchantment） — You may look at the top card of your library any time. You may play lands and cast spells from the top of your library. Once during each of your turns, you may cast a spe
  2. Etali, Primal Storm（{4}{R}{R}｜Legendary Creature — Elder Dinosaur） — Whenever Etali attacks, exile the top card of each player's library, then you may cast any number of spells from among those cards without paying their mana costs.
  3. Otherworldly Gaze（{U}｜Instant） — Surveil 3. (Look at the top three cards of your library, then put any number of them into your graveyard and the rest on top of your library in any order.) Flashback {1}{
  4. Omniscience（{7}{U}{U}{U}｜Enchantment） — You may cast spells from your hand without paying their mana costs.
  5. Jori En, Ruin Diver（{1}{U}{R}｜Legendary Creature — Merfolk Wizard） — Whenever you cast your second spell each turn, draw a card.
  6. Ovika, Enigma Goliath（{5}{U}{R}｜Legendary Creature — Phyrexian Nightmare） — Flying Ward—{3}, Pay 3 life. Whenever you cast a noncreature spell, create X 1/1 red Phyrexian Goblin creature tokens, where X is the mana value of that spell. They gain 
- **出场率最高的牌**（大多数牌组都会放）
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  - Opt（{U}｜Instant） — Scry 1. (Look at the top card of your library. You may put that card on the bottom.) Draw a card.
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Izzet Signet（{2}｜Artifact） — {1}, {T}: Add {U}{R}.


## Solphim, Mayhem Dominus ｜ 破坏圣主索非穆
- 颜色 R ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Phyrexian Horror
- 流行度：EDHREC 全时段第 556 位，约 5371 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.69 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $28.86
- 社区标签：烧血、群体折磨、法术连发、龙之途径、快攻、组合技
- 完整牌面：If a source you control would deal noncombat damage to an opponent or a permanent an opponent controls, it deals double that damage to that player or permanent instead.
{1}{R/P}{R/P}, Discard two cards: Put an indestructible counter on Solphim. ({R/P} can be paid with either {R} or 2 life.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Heartless Hidetsugu（{3}{R}{R}｜Legendary Creature — Ogre Shaman） — {T}: Heartless Hidetsugu deals damage to each player equal to half that player's life total, rounded down.
  2. Sulfuric Vortex（{1}{R}{R}｜Enchantment） — At the beginning of each player's upkeep, this enchantment deals 2 damage to that player. If a player would gain life, that player gains no life instead.
  3. Fiery Confluence（{2}{R}{R}｜Sorcery） — Choose three. You may choose the same mode more than once. • Fiery Confluence deals 1 damage to each creature. • Fiery Confluence deals 2 damage to each opponent. • Destr
  4. Flame Rift（{1}{R}｜Sorcery） — Flame Rift deals 4 damage to each player.
  5. Guttersnipe（{2}{R}｜Creature — Goblin Shaman） — Whenever you cast an instant or sorcery spell, this creature deals 2 damage to each opponent.
  6. Price of Progress（{1}{R}｜Instant） — Price of Progress deals damage to each player equal to twice the number of nonbasic lands that player controls.
- **出场率最高的牌**（大多数牌组都会放）
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.
  - Ruby Medallion（{2}｜Artifact） — Red spells you cast cost {1} less to cast.
  - Lightning Bolt（{R}｜Instant） — Lightning Bolt deals 3 damage to any target.
  - Torbran, Thane of Red Fell（{1}{R}{R}{R}｜Legendary Creature — Dwarf Noble） — If a red source you control would deal damage to an opponent or a permanent an opponent controls, it deals that much damage plus 2
