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

# 素材：36 位主将


## Zaxara, the Exemplary ｜ 斑斓模范札煞拉
- 颜色 UBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Nightmare Hydra
- 流行度：EDHREC 全时段第 75 位，约 20266 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.41 ｜ 上手难度 2/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $1.98
- 社区标签：X 咒语、＋1/＋1 指示物、多头龙、衍生物、加速、组合技
- 完整牌面：Deathtouch
{T}: Add two mana of any one color.
Whenever you cast a spell with {X} in its mana cost, create a 0/0 green Hydra creature token, then put X +1/+1 counters on it.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Hydroid Krasis（{X}{G}{U}｜Creature — Jellyfish Hydra Beast） — When you cast this spell, you gain half X life and draw half X cards. Round down each time. Flying, trample This creature enters with X +1/+1 counters on it.
  2. Unbound Flourishing（{2}{G}｜Enchantment） — Whenever you cast a permanent spell with a mana cost that contains {X}, double the value of X. Whenever you cast an instant or sorcery spell or activate an ability, if th
  3. Primordial Hydra（{X}{G}{G}｜Creature — Hydra） — This creature enters with X +1/+1 counters on it. At the beginning of your upkeep, double the number of +1/+1 counters on this creature. This creature has trample as long
  4. Hungering Hydra（{X}{G}｜Creature — Hydra） — This creature enters with X +1/+1 counters on it. This creature can't be blocked by more than one creature. Whenever this creature is dealt damage, put that many +1/+1 co
  5. Voracious Hydra（{X}{G}{G}｜Creature — Hydra） — Trample This creature enters with X +1/+1 counters on it. When this creature enters, choose one — • Double the number of +1/+1 counters on this creature. • This creature 
  6. Steelbane Hydra（{X}{G}{G}｜Creature — Turtle Hydra） — This creature enters with X +1/+1 counters on it. {2}{G}, Remove a +1/+1 counter from this creature: Destroy target artifact or enchantment.
- **出场率最高的牌**（大多数牌组都会放）
  - Villainous Wealth（{X}{B}{G}{U}｜Sorcery） — Target opponent exiles the top X cards of their library. You may cast any number of spells with mana value X or less from among th
  - Exsanguinate（{X}{B}{B}｜Sorcery） — Each opponent loses X life. You gain life equal to the life lost this way.
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Goldvein Hydra（{X}{G}｜Creature — Hydra） — Vigilance, trample, haste This creature enters with X +1/+1 counters on it. When this creature dies, create a number of tapped Tre


## Terra, Herald of Hope ｜ 希望传令使蒂娜
- 颜色 WBR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Wizard Warrior
- 流行度：EDHREC 全时段第 76 位，约 20253 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.47 ｜ 上手难度 5/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $1.12
- 社区标签：坟场复活、坟场、自磨、快攻、磨牌、牺牲流
- 完整牌面：Trance — At the beginning of combat on your turn, mill two cards. Terra gains flying until end of turn.
Whenever Terra deals combat damage to a player, you may pay {2}. When you do, return target creature card with power 3 or less from your graveyard to the battlefield tapped.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Celes, Rune Knight（{1}{R}{W}{B}｜Legendary Creature — Human Wizard Knight） — When Celes enters, discard any number of cards, then draw that many cards plus one. Whenever one or more other creatures you control enter, if one or more of them entered
  2. Stitcher's Supplier（{B}｜Creature — Zombie） — When this creature enters or dies, mill three cards. (Put the top three cards of your library into your graveyard.)
  3. Reanimate（{B}｜Sorcery） — Put target creature card from a graveyard onto the battlefield under your control. You lose life equal to that card's mana value.
  4. Priest of Fell Rites（{W}{B}｜Creature — Human Warlock） — {T}, Pay 3 life, Sacrifice this creature: Return target creature card from your graveyard to the battlefield. Activate only as a sorcery. Unearth {3}{W}{B} ({3}{W}{B}: Re
  5. Anger（{3}{R}｜Creature — Incarnation） — Haste As long as this card is in your graveyard and you control a Mountain, creatures you control have haste.
  6. Stitch Together（{B}{B}｜Sorcery） — Return target creature card from your graveyard to your hand. Threshold — Return that card from your graveyard to the battlefield instead if there are seven or more cards
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Battlefield Forge（｜Land） — {T}: Add {C}. {T}: Add {R} or {W}. This land deals 1 damage to you.


## Kotis, the Fangkeeper ｜ 龙牙卫柯提斯
- 颜色 UBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Zombie Warrior
- 流行度：EDHREC 全时段第 77 位，约 20078 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.84 ｜ 上手难度 2/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.40
- 社区标签：主将单挑、偷取、装备、灵气、＋1/＋1 指示物、突变
- 完整牌面：Indestructible
Whenever Kotis deals combat damage to a player, exile the top X cards of their library, where X is the amount of damage dealt. You may cast any number of spells with mana value X or less from among them without paying their mana costs.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Rancor（{G}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +2/+0 and has trample. When this Aura is put into a graveyard from the battlefield, return it to its owner's hand.
  2. Aqueous Form（{U}｜Enchantment — Aura） — Enchant creature Enchanted creature can't be blocked. Whenever enchanted creature attacks, scry 1. (Look at the top card of your library. You may put that card on the bot
  3. Dragonfire Blade（{1}｜Artifact — Equipment） — Equipped creature gets +2/+2 and has hexproof from monocolored. Equip {4}. This ability costs {1} less to activate for each color of the creature it targets.
  4. Favor of the Overbeing（{1}{G/U}｜Enchantment — Aura） — Enchant creature As long as enchanted creature is green, it gets +1/+1 and has vigilance. As long as enchanted creature is blue, it gets +1/+1 and has flying.
  5. Felix Five-Boots（{2}{B}{G}{U}｜Legendary Creature — Ooze Rogue） — Menace, ward {2} If a creature you control dealing combat damage to a player causes a triggered ability of a permanent you control to trigger, that ability triggers an ad
  6. Snakeskin Veil（{G}｜Instant） — Put a +1/+1 counter on target creature you control. It gains hexproof until end of turn. (It can't be the target of spells or abilities your opponents control.)
- **出场率最高的牌**（大多数牌组都会放）
  - Opulent Palace（｜Land） — This land enters tapped. {T}: Add {B}, {G}, or {U}.
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Blackblade Reforged（{2}｜Legendary Artifact — Equipment） — Equipped creature gets +1/+1 for each land you control. Equip legendary creature {3} Equip {7}
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.


## Betor, Ancestor's Voice ｜ 先祖之声贝托
- 颜色 WBG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Spirit Dragon
- 流行度：EDHREC 全时段第 78 位，约 20028 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.38 ｜ 上手难度 3/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $3.20
- 社区标签：生命增益、＋1/＋1 指示物、坟场复活、自伤、坟场、吸取生命
- 完整牌面：Flying, lifelink
At the beginning of your end step, put a number of +1/+1 counters on up to one other target creature you control equal to the amount of life you gained this turn. Return up to one target creature card with mana value less than or equal to the amount of life you lost this turn from your graveyard to the battlefield.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Lathiel, the Bounteous Dawn（{2}{G}{W}｜Legendary Creature — Unicorn） — Lifelink At the beginning of each end step, if you gained life this turn, distribute up to that many +1/+1 counters among any number of other target creatures.
  2. Doom Whisperer（{3}{B}{B}｜Creature — Nightmare Demon） — Flying, trample Pay 2 life: Surveil 2. (Look at the top two cards of your library, then put any number of them into your graveyard and the rest on top of your library in 
  3. Children of Korlis（{W}｜Creature — Human Rebel Cleric） — Sacrifice this creature: You gain life equal to the life you've lost this turn. (Damage causes loss of life.)
  4. Rhox Faithmender（{3}{W}｜Creature — Rhino Monk） — Lifelink (Damage dealt by this creature also causes you to gain that much life.) If you would gain life, you gain twice that much life instead.
  5. Beledros Witherbloom（{5}{B}{G}｜Legendary Creature — Elder Dragon） — Flying At the beginning of each upkeep, create a 1/1 black and green Pest creature token with "When this token dies, you gain 1 life." Pay 10 life: Untap all lands you co
  6. Black Market Connections（{2}{B}｜Enchantment） — At the beginning of your first main phase, choose one or more — • Sell Contraband — Create a Treasure token. You lose 1 life. • Buy Information — Draw a card. You lose 2 
- **出场率最高的牌**（大多数牌组都会放）
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Llanowar Wastes（｜Land） — {T}: Add {C}. {T}: Add {B} or {G}. This land deals 1 damage to you.
  - Brushland（｜Land） — {T}: Add {C}. {T}: Add {G} or {W}. This land deals 1 damage to you.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Auntie Ool, Cursewretch ｜ 劣咒婆巫儿大婶
- 颜色 BRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Goblin Warlock
- 流行度：EDHREC 全时段第 79 位，约 19886 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 2/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.38
- 社区标签：－1/－1 指示物、组合技、控制、牺牲流、增殖、衍生物
- 完整牌面：Ward—Blight 2. (To blight 2, a player puts two -1/-1 counters on a creature they control.)
Whenever one or more -1/-1 counters are put on a creature, draw a card if you control that creature. If you don't control it, its controller loses 1 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Blowfly Infestation（{2}{B}｜Enchantment） — Whenever a creature dies, if it had a -1/-1 counter on it, put a -1/-1 counter on target creature.
  2. Hapatra, Vizier of Poisons（{B}{G}｜Legendary Creature — Human Cleric） — Whenever Hapatra deals combat damage to a player, you may put a -1/-1 counter on target creature. Whenever you put one or more -1/-1 counters on a creature, create a 1/1 
  3. Black Sun's Zenith（{X}{B}{B}｜Sorcery） — Put X -1/-1 counters on each creature. Shuffle Black Sun's Zenith into its owner's library.
  4. Necroskitter（{1}{B}{B}｜Creature — Elemental） — Wither (This deals damage to creatures in the form of -1/-1 counters.) Whenever a creature an opponent controls with a -1/-1 counter on it dies, you may return that card 
  5. The Scorpion God（{3}{B}{R}｜Legendary Creature — God） — Whenever a creature with a -1/-1 counter on it dies, draw a card. {1}{B}{R}: Put a -1/-1 counter on another target creature. When The Scorpion God dies, return it to its 
  6. Massacre Girl, Known Killer（{2}{B}{B}｜Legendary Creature — Human Assassin） — Menace Creatures you control have wither. (They deal damage to creatures in the form of -1/-1 counters.) Whenever a creature an opponent controls dies, if its toughness w
- **出场率最高的牌**（大多数牌组都会放）
  - Ignoble Hierarch（{G}｜Creature — Goblin Shaman） — Exalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.) {T}: Add {B}, {R}, or {G}.
  - The Reaper, King No More（{2/B}{2/R}{2/G}｜Legendary Artifact Creature — Scarecrow） — When The Reaper enters, put a -1/-1 counter on each of up to two target creatures. Whenever a creature an opponent controls with a
  - Devoted Druid（{1}{G}｜Creature — Elf Druid） — {T}: Add {G}. Put a -1/-1 counter on this creature: Untap this creature.
  - Kulrath Knight（{3}{B/R}{B/R}｜Creature — Elemental Knight） — Flying Wither (This deals damage to creatures in the form of -1/-1 counters.) Creatures your opponents control with counters on th


## Terra, Magical Adept ｜ 魔导战士蒂娜
- 颜色 WUBRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Wizard Warrior // Legendary Enchantment Creature — Saga Wizard
- 流行度：EDHREC 全时段第 80 位，约 19874 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.55 ｜ 上手难度 5/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $2.35
- 社区标签：结界流、传纪、组合技、坟场复活、中速、优质单卡堆
- 完整牌面：When Terra enters, mill five cards. Put up to one enchantment card milled this way into your hand.
Trance — {4}{R}{G}, {T}: Exile Terra, then return it to the battlefield transformed under its owner's control. Activate only as a sorcery.
//
(As this Saga enters and after your draw step, add a lore counter.)
I, II, III — Create a token that's a copy of target nonlegendary enchantment you control. It gains haste. If it's a Saga, put up to three lore counters on it. Sacrifice it at the beginning of your next end step.
IV — Add {W}{W}, {U}{U}, {B}{B}, {R}{R}, and {G}{G}. Exile Esper Terra, then return it to the battlefield (front face up).
Flying
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Summon: Titan（{3}{G}{G}｜Enchantment Creature — Saga Giant） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Mill five cards. II — Return all land cards from your graveyard to the battle
  2. Summon: Fenrir（{2}{G}｜Enchantment Creature — Saga Wolf） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Crescent Fang — Search your library for a basic land card, put it onto the ba
  3. Summon: Primal Odin（{4}{B}{B}｜Enchantment Creature — Saga Knight） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Gungnir — Destroy target creature an opponent controls. II — Zantetsuken — Th
  4. Summon: Bahamut（{9}｜Enchantment Creature — Saga Dragon） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after IV.) I, II — Destroy up to one target nonland permanent. III — Draw two cards. IV — Meg
  5. Summon: Yojimbo（{3}{W}｜Enchantment Creature — Saga Samurai） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after IV.) I — Exile target artifact, enchantment, or tapped creature an opponent controls. I
  6. Yuna, Hope of Spira（{3}{G}{W}｜Legendary Creature — Human Cleric） — During your turn, Yuna and enchantment creatures you control have trample, lifelink, and ward {2}. At the beginning of your end step, return up to one target enchantment 
- **出场率最高的牌**（大多数牌组都会放）
  - Summon: Knights of Round（{6}{W}{W}｜Enchantment Creature — Saga Knight） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after V.) I, II, III, IV — Create three 2/2 white Kni
  - Sanctum Weaver（{1}{G}｜Enchantment Creature — Dryad） — {T}: Add X mana of any one color, where X is the number of enchantments you control.
  - Sythis, Harvest's Hand（{G}{W}｜Legendary Enchantment Creature — Nymph） — Whenever you cast an enchantment spell, you gain 1 life and draw a card.
  - Rydia, Summoner of Mist（{R}{G}｜Legendary Creature — Human Shaman） — Landfall — Whenever a land you control enters, you may discard a card. If you do, draw a card. Summon — {X}, {T}: Return target Sa


## Ghyrson Starn, Kelermorph ｜ 三枪侠吉尔森·史塔恩
- 颜色 UR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Tyranid Human
- 流行度：EDHREC 全时段第 81 位，约 19822 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.11 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $33.36
- 社区标签：烧血、法术连发、点伤、风暴、组合技、快攻
- 完整牌面：Ward {2} (Whenever this creature becomes the target of a spell or ability an opponent controls, counter it unless that player pays {2}.)
Three Autostubs — Whenever another source you control deals exactly 1 damage to a permanent or player, Ghyrson Starn deals 2 damage to that permanent or player.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. End the Festivities（{R}｜Sorcery） — End the Festivities deals 1 damage to each opponent and each creature and planeswalker they control.
  2. Thermo-Alchemist（{1}{R}｜Creature — Human Shaman） — Defender {T}: This creature deals 1 damage to each opponent. Whenever you cast an instant or sorcery spell, untap this creature.
  3. Tectonic Hazard（{R}｜Sorcery） — Tectonic Hazard deals 1 damage to each opponent and each creature they control.
  4. Firebrand Archer（{1}{R}｜Creature — Human Archer） — Whenever you cast a noncreature spell, this creature deals 1 damage to each opponent.
  5. Electrickery（{R}｜Instant） — Electrickery deals 1 damage to target creature you don't control. Overload {1}{R} (You may cast this spell for its overload cost. If you do, change "target" in its text t
  6. Basilisk Collar（{1}｜Artifact — Equipment） — Equipped creature has deathtouch and lifelink. (Any amount of damage it deals to a creature is enough to destroy it. Damage dealt by this creature also causes you to gain
- **出场率最高的牌**（大多数牌组都会放）
  - Curiosity（{U}｜Enchantment — Aura） — Enchant creature Whenever enchanted creature deals damage to an opponent, you may draw a card.
  - Kessig Flamebreather（{1}{R}｜Creature — Human Shaman） — Whenever you cast a noncreature spell, this creature deals 1 damage to each opponent.
  - Grapeshot（{1}{R}｜Sorcery） — Grapeshot deals 1 damage to any target. Storm (When you cast this spell, copy it for each spell cast before it this turn. You may 
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.


## The First Sliver ｜ 原初裂片妖
- 颜色 WUBRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Sliver
- 流行度：EDHREC 全时段第 82 位，约 19819 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 1.66 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $38.15
- 社区标签：裂片妖、倾曳、快攻、组合技、中速、加速
- 完整牌面：Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. Put the exiled cards on the bottom in a random order.)
Sliver spells you cast have cascade.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Cloudshredder Sliver（{R}{W}｜Creature — Sliver） — Sliver creatures you control have flying and haste.
  2. Sliver Hivelord（{W}{U}{B}{R}{G}｜Legendary Creature — Sliver） — Sliver creatures you control have indestructible. (Damage and effects that say "destroy" don't destroy them.)
  3. Gemhide Sliver（{1}{G}｜Creature — Sliver） — All Slivers have "{T}: Add one mana of any color."
  4. Manaweft Sliver（{1}{G}｜Creature — Sliver） — Sliver creatures you control have "{T}: Add one mana of any color."
  5. Harmonic Sliver（{1}{G}{W}｜Creature — Sliver） — All Slivers have "When this permanent enters, destroy target artifact or enchantment."
  6. Crystalline Sliver（{W}{U}｜Creature — Sliver） — All Slivers have shroud. (They can't be the targets of spells or abilities.)
- **出场率最高的牌**（大多数牌组都会放）
  - Bonescythe Sliver（{3}{W}｜Creature — Sliver） — Sliver creatures you control have double strike. (They deal both first-strike and regular combat damage.)
  - Sentinel Sliver（{1}{W}｜Creature — Sliver） — Sliver creatures you control have vigilance. (Attacking doesn't cause them to tap.)
  - Galerider Sliver（{U}｜Creature — Sliver） — Sliver creatures you control have flying.
  - Syphon Sliver（{2}{B}｜Creature — Sliver） — Sliver creatures you control have lifelink. (Damage dealt by a Sliver creature you control also causes you to gain that much life.


## Xyris, the Writhing Storm ｜ 纠拧风暴塞利兹
- 颜色 URG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Snake Leviathan
- 流行度：EDHREC 全时段第 83 位，约 19783 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.5 ｜ 上手难度 3/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $2.12
- 社区标签：换手牌、衍生物、群体恩惠、抽牌、蛇、烧血
- 完整牌面：Flying
Whenever an opponent draws a card except the first one they draw in each of their draw steps, create a 1/1 green Snake creature token.
Whenever Xyris deals combat damage to a player, you and that player each draw that many cards.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  2. Windfall（{2}{U}｜Sorcery） — Each player discards their hand, then draws cards equal to the greatest number of cards a player discarded this way.
  3. Goblin Bombardment（{1}{R}｜Enchantment） — Sacrifice a creature: This enchantment deals 1 damage to any target.
  4. Howling Mine（{2}｜Artifact） — At the beginning of each player's draw step, if this artifact is untapped, that player draws an additional card.
  5. Magus of the Wheel（{2}{R}｜Creature — Human Wizard） — {1}{R}, {T}, Sacrifice this creature: Each player discards their hand, then draws seven cards.
  6. Scrawling Crawler（{3}｜Artifact Creature — Phyrexian Construct） — At the beginning of your upkeep, each player draws a card. Whenever an opponent draws a card, that player loses 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Frontier Bivouac（｜Land） — This land enters tapped. {T}: Add {G}, {U}, or {R}.
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Kilo, Apogee Mind ｜ 至高思维奇洛
- 颜色 WUR ｜ 法术力值 3.0 ｜ 类型 Legendary Artifact Creature — Robot Artificer
- 流行度：EDHREC 全时段第 84 位，约 19530 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.39 ｜ 上手难度 1/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $2.05
- 社区标签：神器、＋1/＋1 指示物、增殖、组合技、毒侵、充能指示物
- 完整牌面：Haste
Whenever Kilo becomes tapped, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Tekuthal, Inquiry Dominus（{2}{U}{U}｜Legendary Creature — Phyrexian Horror） — Flying If you would proliferate, proliferate twice instead. {1}{U/P}{U/P}, Remove three counters from among other artifacts, creatures, and planeswalkers you control: Put
  2. Inspirit, Flagship Vessel（{U}{R}{W}｜Legendary Artifact — Spacecraft） — Station (Tap another creature you control: Put charge counters equal to its power on this Spacecraft. Station only as a sorcery. It's an artifact creature at 8+.) 1+ | At
  3. Everflowing Chalice（{0}｜Artifact） — Multikicker {2} (You may pay an additional {2} any number of times as you cast this spell.) This artifact enters with a charge counter on it for each time it was kicked. 
  4. Insight Engine（{2}{U}｜Artifact） — {2}, {T}: Put a charge counter on this artifact, then draw a card for each charge counter on it.
  5. Surge Conductor（{3}｜Artifact Creature — Robot） — Whenever another nontoken artifact you control enters, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already t
  6. Seat of the Synod（｜Artifact Land） — {T}: Add {U}.
- **出场率最高的牌**（大多数牌组都会放）
  - Ancient Den（｜Artifact Land） — {T}: Add {W}.
  - Great Furnace（｜Artifact Land） — {T}: Add {R}.
  - Patrolling Peacemaker（{2}{W}｜Artifact Creature — Robot Soldier） — This creature enters with two +1/+1 counters on it. Whenever an opponent commits a crime, proliferate. (They commit a crime if the
  - Ripples of Potential（{1}{U}｜Instant） — Proliferate, then choose any number of permanents you control that had a counter put on them this way. Those permanents phase out.


## Sisay, Weatherlight Captain ｜ 晴空号船长西赛
- 颜色 WUBRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Soldier
- 流行度：EDHREC 全时段第 85 位，约 19382 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.98 ｜ 上手难度 2/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $2.62
- 社区标签：传奇、组合技、史迹、工具箱、鹏洛客、中速
- 完整牌面：Sisay gets +1/+1 for each color among other legendary permanents you control.
{W}{U}{B}{R}{G}: Search your library for a legendary permanent card with mana value less than Sisay's power, put that card onto the battlefield, then shuffle.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Relic of Legends（{3}｜Artifact） — {T}: Add one mana of any color. Tap an untapped legendary creature you control: Add one mana of any color.
  2. Derevi, Empyrial Tactician（{G}{W}{U}｜Legendary Creature — Bird Wizard） — Flying When Derevi enters and whenever a creature you control deals combat damage to a player, you may tap or untap target permanent. {1}{G}{W}{U}: Put Derevi onto the ba
  3. Selvala, Heart of the Wilds（{1}{G}{G}｜Legendary Creature — Elf Scout） — Whenever another creature enters, its controller may draw a card if its power is greater than each other creature's power. {G}, {T}: Add X mana in any combination of colo
  4. Teferi, Time Raveler（{1}{W}{U}｜Legendary Planeswalker — Teferi） — Each opponent can cast spells only any time they could cast a sorcery. +1: Until your next turn, you may cast sorcery spells as though they had flash. −3: Return up to on
  5. Kinnan, Bonder Prodigy（{G}{U}｜Legendary Creature — Human Druid） — Whenever you tap a nonland permanent for mana, add one mana of any type that permanent produced. {5}{G}{U}: Look at the top five cards of your library. You may put a non-
  6. Lotho, Corrupt Shirriff（{W}{B}｜Legendary Creature — Halfling Rogue） — Whenever a player casts their second spell each turn, you lose 1 life and create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any 
- **出场率最高的牌**（大多数牌组都会放）
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Bloom Tender（{1}{G}｜Creature — Elf Druid） — Vivid — {T}: For each color among permanents you control, add one mana of that color.
  - Windswept Heath（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Plains card, put it onto the battlefield, then shuffle.
  - Flooded Strand（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Plains or Island card, put it onto the battlefield, then shuffle.


## Eriette of the Charmed Apple ｜ 毒苹果艾纶缇
- 颜色 WB ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Warlock
- 流行度：EDHREC 全时段第 86 位，约 19099 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.49 ｜ 上手难度 2/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.36
- 社区标签：灵气、结界流、生命增益、控制、吸取生命、铁壁防守
- 完整牌面：Each creature that's enchanted by an Aura you control can't attack you or planeswalkers you control.
At the beginning of your end step, each opponent loses X life and you gain X life, where X is the number of Auras you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mesa Enchantress（{1}{W}{W}｜Creature — Human Druid） — Whenever you cast an enchantment spell, you may draw a card.
  2. Sram, Senior Edificer（{1}{W}｜Legendary Creature — Dwarf Advisor） — Whenever you cast an Aura, Equipment, or Vehicle spell, draw a card.
  3. Kor Spiritdancer（{1}{W}｜Creature — Kor Wizard） — This creature gets +2/+2 for each Aura attached to it. Whenever you cast an Aura spell, you may draw a card.
  4. Killian, Ink Duelist（{W}{B}｜Legendary Creature — Human Warlock） — Lifelink Menace (This creature can't be blocked except by two or more creatures.) Spells you cast that target a creature cost {2} less to cast.
  5. All That Glitters（{1}{W}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 for each artifact and/or enchantment you control.
  6. Ethereal Armor（{W}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 for each enchantment you control and has first strike.
- **出场率最高的牌**（大多数牌组都会放）
  - Darksteel Mutation（{1}{W}｜Enchantment — Aura） — Enchant creature Enchanted creature is an Insect artifact creature with base power and toughness 0/1 and has indestructible, and i
  - Sage's Reverie（{3}{W}｜Enchantment — Aura） — Enchant creature When this Aura enters, draw a card for each Aura you control that's attached to a creature. Enchanted creature ge
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Parasitic Impetus（{2}{B}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +2/+2 and is goaded. (It attacks each combat if able and attacks a player other than you 


## Ragost, Deft Gastronaut ｜ 灵巧美食家拉戈斯
- 颜色 WR ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Lobster Citizen
- 流行度：EDHREC 全时段第 87 位，约 19082 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.35 ｜ 上手难度 4/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.36
- 社区标签：神器、烧血、生命增益、衍生物、食品、组合技
- 完整牌面：Artifacts you control are Foods in addition to their other types and have "{2}, {T}, Sacrifice this artifact: You gain 3 life."
{1}, {T}, Sacrifice a Food: Ragost deals 3 damage to each opponent.
At the beginning of each end step, if you gained life this turn, untap Ragost.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Weapons Manufacturing（{1}{R}｜Enchantment） — Whenever a nontoken artifact you control enters, create a colorless artifact token named Munitions with "When this token leaves the battlefield, it deals 2 damage to any 
  2. Nuka-Cola Vending Machine（{3}｜Artifact） — {1}, {T}: Create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.") Whenever you sacrifice a Food, create a tapped Treasure token. (
  3. Academy Manufactor（{3}｜Artifact Creature — Assembly-Worker） — If you would create a Clue, Food, or Treasure token, instead create one of each.
  4. Ichor Wellspring（{2}｜Artifact） — When this artifact enters or is put into a graveyard from the battlefield, draw a card.
  5. Prized Statue（{2}｜Artifact） — When this artifact enters or is put into a graveyard from the battlefield, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any
  6. Basilisk Collar（{1}｜Artifact — Equipment） — Equipped creature has deathtouch and lifelink. (Any amount of damage it deals to a creature is enough to destroy it. Damage dealt by this creature also causes you to gain
- **出场率最高的牌**（大多数牌组都会放）
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Ancient Den（｜Artifact Land） — {T}: Add {W}.
  - Great Furnace（｜Artifact Land） — {T}: Add {R}.
  - Haliya, Guided by Light（{2}{W}｜Legendary Creature — Human Soldier） — Whenever Haliya or another creature or artifact you control enters, you gain 1 life. At the beginning of your end step, draw a car


## Norman Osborn ｜ 诺曼·奥斯本
- 颜色 UBR ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Scientist Villain // Legendary Creature — Goblin Human Villain
- 流行度：EDHREC 全时段第 88 位，约 18953 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.74 ｜ 上手难度 5/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $14.78
- 社区标签：弃牌、换手牌、组合技、坟场复活、坟场、刺探
- 完整牌面：Norman Osborn can't be blocked.
Whenever Norman Osborn deals combat damage to a player, he connives. (Draw a card, then discard a card. If you discarded a nonland card, put a +1/+1 counter on this creature.)
{1}{U}{B}{R}: Transform Norman Osborn. Activate only as a sorcery.
//
Flying, menace
Spells you cast from your graveyard cost {2} less to cast.
Goblin Formula — Each nonland card in your graveyard has mayhem. The mayhem cost is equal to its mana cost. (You may cast a card from your graveyard for its mayhem cost if you discarded it this turn. Timing rules still apply.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Shadow of the Goblin（{1}{R}｜Enchantment） — Unreliable Visions — At the beginning of your first main phase, discard a card. If you do, draw a card. Undying Vengeance — Whenever you play a land or cast a spell from 
  2. Ultimate Green Goblin（{1}{B/R}{B/R}｜Legendary Creature — Goblin Villain） — At the beginning of your upkeep, discard a card, then create a Treasure token. Mayhem {2}{B/R} (You may cast this card from your graveyard for {2}{B/R} if you discarded i
  3. Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.
  4. Faithless Looting（{R}｜Sorcery） — Draw two cards, then discard two cards. Flashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then exile it.)
  5. Psychic Frog（{U}{B}｜Creature — Frog） — Whenever this creature deals combat damage to a player or planeswalker, draw a card. Discard a card: Put a +1/+1 counter on this creature. Exile three cards from your gra
  6. Ghostly Pilferer（{1}{U}｜Creature — Spirit Rogue） — Whenever this creature becomes untapped, you may pay {2}. If you do, draw a card. Whenever an opponent casts a spell from anywhere other than their hand, draw a card. Dis
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.
  - Oscorp Industries（｜Land） — This land enters tapped. When this land enters from a graveyard, you lose 2 life. {T}: Add {U}, {B}, or {R}. Mayhem (You may play 
  - Talisman of Indulgence（{2}｜Artifact） — {T}: Add {C}. {T}: Add {B} or {R}. This artifact deals 1 damage to you.
  - Windfall（{2}{U}｜Sorcery） — Each player discards their hand, then draws cards equal to the greatest number of cards a player discarded this way.


## Henzie "Toolbox" Torre ｜ 万金油亨齐托雷
- 颜色 BRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Devil Rogue
- 流行度：EDHREC 全时段第 89 位，约 18871 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.69 ｜ 上手难度 5/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.97
- 社区标签：坟场复活、快攻、牺牲流、诞生荚、工具箱、牺牲
- 完整牌面：Each creature spell you cast with mana value 4 or greater has blitz. The blitz cost is equal to its mana cost. (You may choose to cast that spell for its blitz cost. If you do, it gains haste and "When this creature dies, draw a card." Sacrifice it at the beginning of the next end step.)
Blitz costs you pay cost {1} less for each time you've cast your commander from the command zone this game.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Junji, the Midnight Sky（{3}{B}{B}｜Legendary Creature — Dragon Spirit） — Flying, menace When Junji dies, choose one — • Each opponent discards two cards and loses 2 life. • Put target non-Dragon creature card from a graveyard onto the battlefi
  2. Solemn Simulacrum（{4}｜Artifact Creature — Golem） — When this creature enters, you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle. When this creature dies, you may dr
  3. Seedguide Ash（{4}{G}｜Creature — Treefolk Druid） — When this creature dies, you may search your library for up to three Forest cards, put them onto the battlefield tapped, then shuffle.
  4. Etali, Primal Storm（{4}{R}{R}｜Legendary Creature — Elder Dinosaur） — Whenever Etali attacks, exile the top card of each player's library, then you may cast any number of spells from among those cards without paying their mana costs.
  5. Primeval Herald（{3}{G}｜Creature — Elf Scout） — Trample (This creature can deal excess combat damage to the player or planeswalker it's attacking.) Whenever this creature enters or attacks, you may search your library 
  6. Industrial Advancement（{3}{R}｜Enchantment） — At the beginning of your end step, you may sacrifice a creature. If you do, look at the top X cards of your library, where X is that creature's mana value. You may put a 
- **出场率最高的牌**（大多数牌组都会放）
  - Ignoble Hierarch（{G}｜Creature — Goblin Shaman） — Exalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.) {T}: Add {B}, {R}, or {G}.
  - Victimize（{2}{B}｜Sorcery） — Choose two target creature cards in your graveyard. Sacrifice a creature. If you do, return the chosen cards to the battlefield ta
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Ojer Kaslem, Deepest Growth（｜） — 


## Urtet, Remnant of Memnarch ｜ 蒙纳珂孑遗尔铁
- 颜色 WUBRG ｜ 法术力值 3.0 ｜ 类型 Legendary Artifact Creature — Myr
- 流行度：EDHREC 全时段第 90 位，约 18647 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.47 ｜ 上手难度 4/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $6.65
- 社区标签：神器、秘耳、＋1/＋1 指示物、衍生物、组合技、神器共鸣
- 完整牌面：Whenever you cast a Myr spell, create a 1/1 colorless Myr artifact creature token.
At the beginning of combat on your turn, untap each Myr you control.
{W}{U}{B}{R}{G}, {T}: Put three +1/+1 counters on each Myr you control. Activate only during your turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Gold Myr（{2}｜Artifact Creature — Myr） — {T}: Add {W}.
  2. Silver Myr（{2}｜Artifact Creature — Myr） — {T}: Add {U}.
  3. Copper Myr（{2}｜Artifact Creature — Myr） — {T}: Add {G}.
  4. Iron Myr（{2}｜Artifact Creature — Myr） — {T}: Add {R}.
  5. Leaden Myr（{2}｜Artifact Creature — Myr） — {T}: Add {B}.
  6. Myr Galvanizer（{3}｜Artifact Creature — Myr） — Other Myr creatures you control get +1/+1. {1}, {T}: Untap each other Myr you control.
- **出场率最高的牌**（大多数牌组都会放）
  - Palladium Myr（{3}｜Artifact Creature — Myr） — {T}: Add {C}{C}.
  - Myr Battlesphere（{7}｜Artifact Creature — Myr Construct） — When this creature enters, create four 1/1 colorless Myr artifact creature tokens. Whenever this creature attacks, you may tap X u
  - Alloy Myr（{3}｜Artifact Creature — Myr） — {T}: Add one mana of any color.
  - Shimmer Myr（{3}｜Artifact Creature — Myr） — Flash You may cast artifact spells as though they had flash.


## Captain N'ghathrod ｜ 纳噶斯罗船长
- 颜色 UB ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Horror Pirate
- 流行度：EDHREC 全时段第 91 位，约 18608 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.6 ｜ 上手难度 5/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $None
- 社区标签：磨牌、惊惧兽、偷取、坟场复活、坟场、控制
- 完整牌面：Horrors you control have menace.
Whenever a Horror you control deals combat damage to a player, that player mills that many cards.
At the beginning of your end step, choose target artifact or creature card in an opponent's graveyard that was put there from their library this turn. Put it onto the battlefield under your control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Consuming Aberration（{3}{U}{B}｜Creature — Horror） — Consuming Aberration's power and toughness are each equal to the number of cards in your opponents' graveyards. Whenever you cast a spell, each opponent reveals cards fro
  2. Nemesis of Reason（{3}{U}{B}｜Creature — Leviathan Horror） — Whenever this creature attacks, defending player mills ten cards.
  3. Zellix, Sanity Flayer（{2}{U}｜Legendary Creature — Horror） — Hive Mind — Whenever a player mills one or more creature cards, you create a 1/1 black Horror creature token. {1}, {T}: Target player mills three cards. Choose a Backgrou
  4. Mindcrank（{2}｜Artifact） — Whenever an opponent loses life, that player mills that many cards. (Damage causes loss of life.)
  5. Grazilaxx, Illithid Scholar（{1}{U}{U}｜Legendary Creature — Horror） — Whenever a creature you control becomes blocked, you may return it to its owner's hand. Whenever one or more creatures you control deal combat damage to a player, draw a 
  6. Guiltfeeder（{3}{B}{B}｜Creature — Horror） — Fear (This creature can't be blocked except by artifact creatures and/or black creatures.) Whenever this creature attacks and isn't blocked, defending player loses 1 life
- **出场率最高的牌**（大多数牌组都会放）
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Fractured Sanity（{U}{U}{U}｜Sorcery） — Each opponent mills fourteen cards. Cycling {1}{U} ({1}{U}, Discard this card: Draw a card.) When you cycle this card, each oppone
  - Drown in the Loch（{U}{B}｜Instant） — Choose one — • Counter target spell with mana value less than or equal to the number of cards in its controller's graveyard. • Des
  - Uchuulon（{3}{B}｜Creature — Crab Ooze Horror） — Uchuulon's power is equal to the number of Crabs, Oozes, and/or Horrors you control. Horrific Symbiosis — At the beginning of your


## Omnath, Locus of Creation ｜ 生机核欧那斯
- 颜色 WURG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Elemental
- 流行度：EDHREC 全时段第 92 位，约 18605 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.02 ｜ 上手难度 4/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $4.99
- 社区标签：地牌核心、地落、加速、衍生物、组合技、元素
- 完整牌面：When Omnath enters, draw a card.
Landfall — Whenever a land you control enters, you gain 4 life if this is the first time this ability has resolved this turn. If it's the second time, add {R}{G}{W}{U}. If it's the third time, Omnath deals 4 damage to each opponent and each planeswalker you don't control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  2. Omnath, Locus of Rage（{3}{R}{R}{G}{G}｜Legendary Creature — Elemental） — Landfall — Whenever a land you control enters, create a 5/5 red and green Elemental creature token. Whenever Omnath or another Elemental you control dies, Omnath deals 3 
  3. Tatyova, Benthic Druid（{3}{G}{U}｜Legendary Creature — Merfolk Druid） — Landfall — Whenever a land you control enters, you gain 1 life and draw a card.
  4. Azusa, Lost but Seeking（{2}{G}｜Legendary Creature — Human Monk） — You may play two additional lands on each of your turns.
  5. Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create a token that's a copy of this creature i
  6. Ancient Greenwarden（{4}{G}{G}｜Creature — Elemental） — Reach (This creature can block creatures with flying.) You may play lands from your graveyard. If a land entering causes a triggered ability of a permanent you control to
- **出场率最高的牌**（大多数牌组都会放）
  - Dryad of the Ilysian Grove（{2}{G}｜Enchantment Creature — Nymph Dryad） — You may play an additional land on each of your turns. Lands you control are every basic land type in addition to their other type
  - Aesi, Tyrant of Gyre Strait（{4}{G}{U}｜Legendary Creature — Serpent） — You may play an additional land on each of your turns. Landfall — Whenever a land you control enters, you may draw a card.
  - Avenger of Zendikar（{5}{G}{G}｜Creature — Elemental） — When this creature enters, create a 0/1 green Plant creature token for each land you control. Landfall — Whenever a land you contr
  - Felidar Retreat（{3}{W}｜Enchantment） — Landfall — Whenever a land you control enters, choose one — • Create a 2/2 white Cat Beast creature token. • Put a +1/+1 counter o


## Hope Estheim ｜ 霍普·埃斯特海姆
- 颜色 WU ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Wizard
- 流行度：EDHREC 全时段第 93 位，约 18598 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.76 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.37
- 社区标签：磨牌、生命增益、控制、组合技、＋1/＋1 指示物、铁壁防守
- 完整牌面：Lifelink
At the beginning of your end step, each opponent mills X cards, where X is the amount of life you gained this turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. The Wind Crystal（{2}{W}{W}｜Legendary Artifact） — White spells you cast cost {1} less to cast. If you would gain life, you gain twice that much life instead. {4}{W}{W}, {T}: Creatures you control gain flying and lifelink
  2. Rhox Faithmender（{3}{W}｜Creature — Rhino Monk） — Lifelink (Damage dealt by this creature also causes you to gain that much life.) If you would gain life, you gain twice that much life instead.
  3. The Water Crystal（{2}{U}{U}｜Legendary Artifact） — Blue spells you cast cost {1} less to cast. If an opponent would mill one or more cards, they mill that many cards plus four instead. {4}{U}{U}, {T}: Each opponent mills 
  4. Soul Warden（{W}｜Creature — Human Cleric） — Whenever another creature enters, you gain 1 life.
  5. Space-Time Anomaly（{2}{W}{U}｜Sorcery） — Target player mills cards equal to your life total.
  6. Will, Scion of Peace（{1}{W}{U}｜Legendary Creature — Human Wizard） — Vigilance {T}: Spells you cast this turn that are white and/or blue cost {X} less to cast, where X is the amount of life you gained this turn. Activate only as a sorcery.
- **出场率最高的牌**（大多数牌组都会放）
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Prairie Stream（｜Land — Plains Island） — ({T}: Add {W} or {U}.) This land enters tapped unless you control two or more basic lands.
  - Soul's Attendant（{W}｜Creature — Human Cleric） — Whenever another creature enters, you may gain 1 life.
  - Authority of the Consuls（{W}｜Enchantment） — Creatures your opponents control enter tapped. Whenever a creature an opponent controls enters, you gain 1 life.


## Voja, Jaws of the Conclave ｜ 盟会尖颚沃亚
- 颜色 WRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Wolf
- 流行度：EDHREC 全时段第 94 位，约 18443 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 1.68 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $None
- 社区标签：妖精、＋1/＋1 指示物、快攻、狼、加速、衍生物
- 完整牌面：Vigilance, trample, ward {3}
Whenever Voja attacks, put X +1/+1 counters on each creature you control, where X is the number of Elves you control. Draw a card for each Wolf you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Priest of Titania（{1}{G}｜Creature — Elf Druid） — {T}: Add {G} for each Elf on the battlefield.
  2. Elvish Archdruid（{1}{G}{G}｜Creature — Elf Druid） — Other Elf creatures you control get +1/+1. {T}: Add {G} for each Elf you control.
  3. Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  4. Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  5. Shalai and Hallar（{1}{R}{G}{W}｜Legendary Creature — Angel Elf） — Flying, vigilance Whenever one or more +1/+1 counters are put on a creature you control, Shalai and Hallar deals that much damage to target opponent.
  6. Marwyn, the Nurturer（{2}{G}｜Legendary Creature — Elf Druid） — Whenever another Elf you control enters, put a +1/+1 counter on Marwyn. {T}: Add an amount of {G} equal to Marwyn's power.
- **出场率最高的牌**（大多数牌组都会放）
  - Maskwood Nexus（{4}｜Artifact） — Creatures you control are every creature type. The same is true for creature spells you control and creature cards you own that ar
  - Rhythm of the Wild（{1}{R}{G}｜Enchantment） — Creature spells you control can't be countered. Nontoken creatures you control have riot. (They enter with your choice of a +1/+1 
  - Beast Whisperer（{2}{G}{G}｜Creature — Elf Druid） — Whenever you cast a creature spell, draw a card.
  - Fyndhorn Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.


## High Perfect Morcant ｜ 最高至美茉坎特
- 颜色 BG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Elf Noble
- 流行度：EDHREC 全时段第 95 位，约 18046 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 3/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $1.28
- 社区标签：－1/－1 指示物、妖精、衍生物、＋1/＋1 指示物、毒侵、增殖
- 完整牌面：Whenever High Perfect Morcant or another Elf you control enters, each opponent blights 1. (They each put a -1/-1 counter on a creature they control.)
Tap three untapped Elves you control: Proliferate. Activate only as a sorcery. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Lathril, Blade of the Elves（{2}{B}{G}｜Legendary Creature — Elf Noble） — Menace (This creature can't be blocked except by two or more creatures.) Whenever Lathril deals combat damage to a player, create that many 1/1 green Elf Warrior creature
  2. Flourishing Defenses（{4}{G}｜Enchantment） — Whenever a -1/-1 counter is put on a creature, you may create a 1/1 green Elf Warrior creature token.
  3. Elvish Archdruid（{1}{G}{G}｜Creature — Elf Druid） — Other Elf creatures you control get +1/+1. {T}: Add {G} for each Elf you control.
  4. Priest of Titania（{1}{G}｜Creature — Elf Druid） — {T}: Add {G} for each Elf on the battlefield.
  5. Imperious Perfect（{2}{G}｜Creature — Elf Warrior） — Other Elves you control get +1/+1. {G}, {T}: Create a 1/1 green Elf Warrior creature token.
  6. Lys Alana Huntmaster（{2}{G}{G}｜Creature — Elf Warrior） — Whenever you cast an Elf spell, you may create a 1/1 green Elf Warrior creature token.
- **出场率最高的牌**（大多数牌组都会放）
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Marwyn, the Nurturer（{2}{G}｜Legendary Creature — Elf Druid） — Whenever another Elf you control enters, put a +1/+1 counter on Marwyn. {T}: Add an amount of {G} equal to Marwyn's power.
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.


## Alela, Cunning Conqueror ｜ 黠智霸主阿莉莱
- 颜色 UB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Faerie Warlock
- 流行度：EDHREC 全时段第 96 位，约 17983 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.8 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $13.02
- 社区标签：仙灵、控制、飞行、衍生物、强制战斗、闪现
- 完整牌面：Flying
Whenever you cast your first spell during each opponent's turn, create a 1/1 black Faerie Rogue creature token with flying.
Whenever one or more Faeries you control deal combat damage to a player, goad target creature that player controls.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Obyra, Dreaming Duelist（{U}{B}｜Legendary Creature — Faerie Warrior） — Flash Flying Whenever another Faerie you control enters, each opponent loses 1 life.
  2. Scion of Oona（{2}{U}｜Creature — Faerie Soldier） — Flash Flying Other Faerie creatures you control get +1/+1. Other Faeries you control have shroud. (They can't be the targets of spells or abilities.)
  3. Tegwyll, Duke of Splendor（{1}{U}{B}｜Legendary Creature — Faerie Noble） — Flying, deathtouch Other Faeries you control get +1/+1. Whenever another Faerie you control dies, you draw a card and you lose 1 life.
  4. Spellstutter Sprite（{1}{U}｜Creature — Faerie Wizard） — Flash Flying When this creature enters, counter target spell with mana value X or less, where X is the number of Faeries you control.
  5. Spell Stutter（{1}{U}｜Instant） — Counter target spell unless its controller pays {2} plus an additional {1} for each Faerie you control.
  6. Brazen Borrower（｜） — 
- **出场率最高的牌**（大多数牌组都会放）
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.
  - Nymris, Oona's Trickster（{3}{U}{B}｜Legendary Creature — Faerie Knight） — Flash Flying Whenever you cast your first spell during each opponent's turn, look at the top two cards of your library. Put one of
  - Secluded Glen（｜Land） — As this land enters, you may reveal a Faerie card from your hand. If you don't, this land enters tapped. {T}: Add {U} or {B}.


## Magda, Brazen Outlaw ｜ 莽勇狂徒玛格妲
- 颜色 R ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Dwarf Berserker
- 流行度：EDHREC 全时段第 97 位，约 17975 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.82 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $8.20
- 社区标签：宝物、矮人、神器、组合技、龙、锁场
- 完整牌面：Other Dwarves you control get +1/+0.
Whenever a Dwarf you control becomes tapped, create a Treasure token.
Sacrifice five Treasures: Search your library for an artifact or Dragon card, put that card onto the battlefield, then shuffle.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Axgard Cavalry（{1}{R}｜Creature — Dwarf Berserker） — {T}: Target creature gains haste until end of turn. (It can attack and {T} this turn.)
  2. Dwarven Grunt（{R}｜Creature — Dwarf） — Mountainwalk (This creature can't be blocked as long as defending player controls a Mountain.)
  3. Universal Automaton（{1}｜Artifact Creature — Shapeshifter） — Changeling (This card is every creature type.)
  4. Springleaf Drum（{1}｜Artifact） — {T}, Tap an untapped creature you control: Add one mana of any color.
  5. Xorn（{2}{R}｜Creature — Elemental） — If you would create one or more Treasure tokens, instead create those tokens plus an additional Treasure token.
  6. Magda, the Hoardmaster（{1}{R}｜Legendary Creature — Dwarf Berserker） — Whenever you commit a crime, create a tapped Treasure token. This ability triggers only once each turn. (Targeting opponents, anything they control, and/or cards in their
- **出场率最高的牌**（大多数牌组都会放）
  - Maskwood Nexus（{4}｜Artifact） — Creatures you control are every creature type. The same is true for creature spells you control and creature cards you own that ar
  - Plundering Barbarian（{2}{R}｜Creature — Dwarf Barbarian） — When this creature enters, choose one — • Smash the Chest — Destroy target artifact. • Pry It Open — Create a Treasure token. (It'
  - Bloodfire Dwarf（{R}｜Creature — Dwarf） — {R}, Sacrifice this creature: It deals 1 damage to each creature without flying.
  - Clock of Omens（{4}｜Artifact） — Tap two untapped artifacts you control: Untap target artifact.


## Obeka, Splitter of Seconds ｜ 裂时术师欧蓓卡
- 颜色 UBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Ogre Warlock
- 流行度：EDHREC 全时段第 98 位，约 17856 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.61 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.28
- 社区标签：额外维持、君主、主将单挑、地城、装备、结界流
- 完整牌面：Menace
Whenever Obeka deals combat damage to a player, you get that many additional upkeep steps after this phase.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. As Foretold（{2}{U}｜Enchantment） — At the beginning of your upkeep, put a time counter on this enchantment. Once each turn, you may pay {0} rather than pay the mana cost for a spell you cast with mana valu
  2. Dragonmaster Outcast（{R}｜Creature — Human Shaman） — At the beginning of your upkeep, if you control six or more lands, create a 5/5 red Dragon creature token with flying.
  3. Court of Ire（{3}{R}{R}｜Enchantment） — When this enchantment enters, you become the monarch. At the beginning of your upkeep, this enchantment deals 2 damage to any target. If you're the monarch, it deals 7 da
  4. Twilight Prophet（{2}{B}{B}｜Creature — Vampire Cleric） — Flying Ascend (If you control ten or more permanents, you get the city's blessing for the rest of the game.) At the beginning of your upkeep, if you have the city's bless
  5. Replicating Ring（{3}｜Snow Artifact） — {T}: Add one mana of any color. At the beginning of your upkeep, put a night counter on this artifact. Then if it has eight or more night counters on it, remove all of th
  6. Ring of Valkas（{2}｜Artifact — Equipment） — Equipped creature has haste. (It can attack and {T} no matter when it came under your control.) At the beginning of your upkeep, put a +1/+1 counter on equipped creature 
- **出场率最高的牌**（大多数牌组都会放）
  - Court of Ambition（{2}{B}{B}｜Enchantment） — When this enchantment enters, you become the monarch. At the beginning of your upkeep, each opponent loses 3 life unless they disc
  - Court of Embereth（{2}{R}{R}｜Enchantment） — When this enchantment enters, you become the monarch. At the beginning of your upkeep, create a 3/1 red Knight creature token. The
  - Court of Vantress（{2}{U}{U}｜Enchantment） — When this enchantment enters, you become the monarch. At the beginning of your upkeep, choose up to one other target enchantment o
  - Creeping Bloodsucker（{1}{B}｜Creature — Vampire） — At the beginning of your upkeep, this creature deals 1 damage to each opponent. You gain life equal to the damage dealt this way.


## Sidar Jabari of Zhalfir ｜ 赛费尔的西达将军贾巴力
- 颜色 WUB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Knight
- 流行度：EDHREC 全时段第 99 位，约 17789 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.63 ｜ 上手难度 4/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.51
- 社区标签：骑士、坟场复活、快攻、中速、弃牌、＋1/＋1 指示物
- 完整牌面：Eminence — Whenever you attack with one or more Knights, if Sidar Jabari is in the command zone or on the battlefield, draw a card, then discard a card.
Flying, first strike
Whenever Sidar Jabari deals combat damage to a player, return target Knight creature card from your graveyard to the battlefield.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Knight Exemplar（{1}{W}{W}｜Creature — Human Knight） — First strike (This creature deals combat damage before creatures without first strike.) Other Knight creatures you control get +1/+1 and have indestructible. (Damage and 
  2. Herald of Hoofbeats（{3}{U}｜Creature — Human Knight） — Horsemanship (This creature can't be blocked except by creatures with horsemanship.) Other Knights you control have horsemanship.
  3. Vodalian Wave-Knight（{2}{W}{U}｜Creature — Merfolk Knight） — Whenever you draw a card, put a +1/+1 counter on each other Merfolk and/or Knight you control.
  4. Knights' Charge（{1}{W}{B}｜Enchantment） — Whenever a Knight you control attacks, each opponent loses 1 life and you gain 1 life. {6}{W}{B}, Sacrifice this enchantment: Return all Knight creature cards from your g
  5. Haakon, Stromgald Scourge（{1}{B}{B}｜Legendary Creature — Zombie Knight） — You may cast this card from your graveyard, but not from anywhere else. As long as Haakon is on the battlefield, you may cast Knight spells from your graveyard. When Haak
  6. Exsanguinator Cavalry（{2}{B}｜Creature — Vampire Knight） — Menace, lifelink Whenever a Knight you control deals combat damage to a player, put a +1/+1 counter on that creature and create a Blood token. (It's an artifact with "{1}
- **出场率最高的牌**（大多数牌组都会放）
  - Knight of the White Orchid（{W}{W}｜Creature — Human Knight） — First strike When this creature enters, if an opponent controls more lands than you, you may search your library for a Plains card
  - Marshal of Zhalfir（{W}{U}｜Creature — Human Knight） — Other Knights you control get +1/+1. {W}{U}, {T}: Tap another target creature.
  - Valiant Knight（{3}{W}｜Creature — Human Knight） — Other Knights you control get +1/+1. {3}{W}{W}: Knights you control gain double strike until end of turn.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t


## Zinnia, Valley's Voice ｜ 苍茂谷之声琴尼亚
- 颜色 WUR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Bird Bard
- 流行度：EDHREC 全时段第 100 位，约 17776 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.73 ｜ 上手难度 2/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.45
- 社区标签：衍生物、子嗣、复制、烧血、增殖衍生物、进场触发
- 完整牌面：Flying
Zinnia gets +X/+0, where X is the number of other creatures you control with base power 1.
Creature spells you cast gain offspring {2} as you cast them. (You may pay an additional {2} as you cast a creature spell. If you do, when that creature enters, create a 1/1 token copy of it.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Agate Instigator（{1}{R}｜Creature — Lizard Rogue） — Offspring {1}{R} (You may pay an additional {1}{R} as you cast this spell. If you do, when this creature enters, create a 1/1 token copy of it.) Whenever another creature
  2. Selfless Spirit（{1}{W}｜Creature — Spirit Cleric） — Flying Sacrifice this creature: Creatures you control gain indestructible until end of turn.
  3. Curiosity Crafter（{3}{U}｜Creature — Bird Wizard） — Flying You have no maximum hand size. Whenever a creature token you control deals combat damage to a player, draw a card.
  4. Ornithopter of Paradise（{2}｜Artifact Creature — Thopter） — Flying {T}: Add one mana of any color.
  5. Rapid Augmenter（{1}{U}{R}｜Creature — Otter Artificer） — Haste Whenever another creature you control with base power 1 enters, it gains haste until end of turn. Whenever another creature you control enters, if it wasn't cast, p
  6. Aether Channeler（{2}{U}｜Creature — Human Wizard） — When this creature enters, choose one — • Create a 1/1 white Bird creature token with flying. • Return another target nonland permanent to its owner's hand. • Draw a card
- **出场率最高的牌**（大多数牌组都会放）
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.


## Niv-Mizzet, Parun ｜ 元祖尼米捷
- 颜色 UR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Dragon Wizard
- 流行度：EDHREC 全时段第 123 位，约 15658 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.27 ｜ 上手难度 2/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $5.09
- 社区标签：法术连发、组合技、换手牌、烧血、抽牌、控制
- 完整牌面：This spell can't be countered.
Flying
Whenever you draw a card, Niv-Mizzet deals 1 damage to any target.
Whenever a player casts an instant or sorcery spell, you draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Curiosity（{U}｜Enchantment — Aura） — Enchant creature Whenever enchanted creature deals damage to an opponent, you may draw a card.
  2. Niv-Mizzet, the Firemind（{2}{U}{U}{R}{R}｜Legendary Creature — Dragon Wizard） — Flying Whenever you draw a card, Niv-Mizzet deals 1 damage to any target. {T}: Draw a card.
  3. Ophidian Eye（{2}{U}｜Enchantment — Aura） — Flash (You may cast this spell any time you could cast an instant.) Enchant creature Whenever enchanted creature deals damage to an opponent, you may draw a card.
  4. Tandem Lookout（{2}{U}｜Creature — Human Scout） — Soulbond (You may pair this creature with another unpaired creature when either enters. They remain paired for as long as you control both of them.) As long as Tandem Loo
  5. Guttersnipe（{2}{R}｜Creature — Goblin Shaman） — Whenever you cast an instant or sorcery spell, this creature deals 2 damage to each opponent.
  6. Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
- **出场率最高的牌**（大多数牌组都会放）
  - Izzet Signet（{2}｜Artifact） — {1}, {T}: Add {U}{R}.
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Opt（{U}｜Instant） — Scry 1. (Look at the top card of your library. You may put that card on the bottom.) Draw a card.
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.


## Brago, King Eternal ｜ 不朽国王布莱戈
- 颜色 WU ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Spirit Noble
- 流行度：EDHREC 全时段第 126 位，约 15275 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.98 ｜ 上手难度 1/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $3.34
- 社区标签：闪现回场、控制、组合技、进场触发、衍生物、锁场
- 完整牌面：Flying
Whenever Brago deals combat damage to a player, exile any number of target nonland permanents you control, then return those cards to the battlefield under their owner's control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Peregrine Drake（{4}{U}｜Creature — Drake） — Flying When this creature enters, untap up to five lands.
  2. Aether Channeler（{2}{U}｜Creature — Human Wizard） — When this creature enters, choose one — • Create a 1/1 white Bird creature token with flying. • Return another target nonland permanent to its owner's hand. • Draw a card
  3. Soulherder（{1}{W}{U}｜Creature — Spirit） — Whenever a creature is exiled from the battlefield, put a +1/+1 counter on this creature. At the beginning of your end step, you may exile another target creature you con
  4. Panharmonicon（{4}｜Artifact） — If an artifact or creature entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
  5. Reflector Mage（{1}{W}{U}｜Creature — Human Wizard） — When this creature enters, return target creature an opponent controls to its owner's hand. That creature's owner can't cast spells with the same name as that creature un
  6. Wall of Omens（{1}{W}｜Creature — Wall） — Defender When this creature enters, draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Prairie Stream（｜Land — Plains Island） — ({T}: Add {W} or {U}.) This land enters tapped unless you control two or more basic lands.
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Azorius Signet（{2}｜Artifact） — {1}, {T}: Add {W}{U}.
  - Ephemerate（{W}｜Instant） — Exile target creature you control, then return it to the battlefield under its owner's control. Rebound (If you cast this spell fr


## Grand Arbiter Augustin IV ｜ 大仲裁者奥古斯汀四世
- 颜色 WU ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Advisor
- 流行度：EDHREC 全时段第 149 位，约 14128 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 2.58 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $20.11
- 社区标签：锁场、控制、锁场小兵、铁壁防守、组合技、反击咒语
- 完整牌面：White spells you cast cost {1} less to cast.
Blue spells you cast cost {1} less to cast.
Spells your opponents cast cost {1} more to cast.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Aura of Silence（{1}{W}{W}｜Enchantment） — Artifact and enchantment spells your opponents cast cost {2} more to cast. Sacrifice this enchantment: Destroy target artifact or enchantment.
  2. Lavinia, Azorius Renegade（{W}{U}｜Legendary Creature — Human Soldier） — Each opponent can't cast noncreature spells with mana value greater than the number of lands that player controls. Whenever an opponent casts a spell, if no mana was spen
  3. Propaganda（{2}{U}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  4. Ghostly Prison（{2}{W}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  5. God-Pharaoh's Statue（{6}｜Legendary Artifact） — Spells your opponents cast cost {2} more to cast. At the beginning of your end step, each opponent loses 1 life.
  6. Grand Abolisher（{W}{W}｜Creature — Human Cleric） — During your turn, your opponents can't cast spells or activate abilities of artifacts, creatures, or enchantments.
- **出场率最高的牌**（大多数牌组都会放）
  - Rhystic Study（{2}{U}｜Enchantment） — Whenever an opponent casts a spell, you may draw a card unless that player pays {1}.
  - Smothering Tithe（{3}{W}｜Enchantment） — Whenever an opponent draws a card, that player may pay {2}. If the player doesn't, you create a Treasure token. (It's an artifact 
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t


## Anikthea, Hand of Erebos ｜ 厄睿柏斯之手阿尼克霞
- 颜色 WBG ｜ 法术力值 5.0 ｜ 类型 Legendary Enchantment Creature — Demigod
- 流行度：EDHREC 全时段第 160 位，约 13362 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.39 ｜ 上手难度 2/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $None
- 社区标签：结界流、坟场复活、衍生物、坟场、磨牌、自磨
- 完整牌面：Menace
Other enchantment creatures you control have menace.
Whenever Anikthea enters or attacks, exile up to one target non-Aura enchantment card from your graveyard. Create a token that's a copy of that card, except it's a 3/3 black Zombie creature in addition to its other types.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sanctum Weaver（{1}{G}｜Enchantment Creature — Dryad） — {T}: Add X mana of any one color, where X is the number of enchantments you control.
  2. Eidolon of Blossoms（{2}{G}{G}｜Enchantment Creature — Spirit） — Constellation — Whenever this creature or another enchantment you control enters, draw a card.
  3. Sythis, Harvest's Hand（{G}{W}｜Legendary Enchantment Creature — Nymph） — Whenever you cast an enchantment spell, you gain 1 life and draw a card.
  4. Setessan Champion（{2}{G}｜Creature — Human Warrior） — Constellation — Whenever an enchantment you control enters, put a +1/+1 counter on this creature and draw a card.
  5. Doomwake Giant（{4}{B}｜Enchantment Creature — Giant） — Constellation — Whenever this creature or another enchantment you control enters, creatures your opponents control get -1/-1 until end of turn.
  6. Enchantress's Presence（{2}{G}｜Enchantment） — Whenever you cast an enchantment spell, draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Jukai Naturalist（{G}{W}｜Enchantment Creature — Human Monk） — Lifelink Enchantment spells you cast cost {1} less to cast.
  - Mirari's Wake（{3}{G}{W}｜Enchantment） — Creatures you control get +1/+1. Whenever you tap a land for mana, add one mana of any type that land produced.
  - Extinguish All Hope（{4}{B}{B}｜Sorcery） — Destroy all nonenchantment creatures.
  - Grasp of Fate（{1}{W}{W}｜Enchantment） — When this enchantment enters, for each opponent, exile up to one target nonland permanent that player controls until this enchantm


## Yarok, the Desecrated ｜ 秽灵雅若克
- 颜色 UBG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Elemental Horror
- 流行度：EDHREC 全时段第 163 位，约 13289 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.72 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.40
- 社区标签：地牌核心、地落、闪现回场、进场触发、加速、组合技
- 完整牌面：Deathtouch, lifelink
If a permanent entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Coiling Oracle（{G}{U}｜Creature — Snake Elf Druid） — When this creature enters, reveal the top card of your library. If it's a land card, put it onto the battlefield. Otherwise, put that card into your hand.
  2. Panharmonicon（{4}｜Artifact） — If an artifact or creature entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
  3. Mulldrifter（{4}{U}｜Creature — Elemental） — Flying When this creature enters, draw two cards. Evoke {2}{U} (You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters.)
  4. Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  5. Tatyova, Benthic Druid（{3}{G}{U}｜Legendary Creature — Merfolk Druid） — Landfall — Whenever a land you control enters, you gain 1 life and draw a card.
  6. Risen Reef（{1}{G}{U}｜Creature — Elemental） — Whenever this creature or another Elemental you control enters, look at the top card of your library. If it's a land card, you may put it onto the battlefield tapped. If 
- **出场率最高的牌**（大多数牌组都会放）
  - Eternal Witness（{1}{G}{G}｜Creature — Human Shaman） — When this creature enters, you may return target card from your graveyard to your hand.
  - Tireless Provisioner（{2}{G}｜Creature — Elf Scout） — Landfall — Whenever a land you control enters, create a Food token or a Treasure token. (Food is an artifact with "{2}, {T}, Sacri
  - Baleful Strix（{U}{B}｜Artifact Creature — Bird） — Flying, deathtouch When this creature enters, draw a card.
  - Avenger of Zendikar（{5}{G}{G}｜Creature — Elemental） — When this creature enters, create a 0/1 green Plant creature token for each land you control. Landfall — Whenever a land you contr


## Tergrid, God of Fright ｜ 惊惶神特格莉德
- 颜色 B ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — God // Legendary Artifact
- 流行度：EDHREC 全时段第 175 位，约 12822 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 2.8 ｜ 上手难度 5/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $19.49
- 社区标签：弃牌、牺牲、偷取、群体折磨、控制、锁场
- 完整牌面：Menace
Whenever an opponent sacrifices a nontoken permanent or discards a permanent card, you may put that card from a graveyard onto the battlefield under your control.
//
{T}: Target player loses 3 life unless they sacrifice a nonland permanent of their choice or discard a card.
{3}{B}: Untap Tergrid's Lantern.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Smallpox（{B}{B}｜Sorcery） — Each player loses 1 life, discards a card, sacrifices a creature of their choice, then sacrifices a land of their choice.
  2. Waste Not（{1}{B}｜Enchantment） — Whenever an opponent discards a creature card, create a 2/2 black Zombie creature token. Whenever an opponent discards a land card, add {B}{B}. Whenever an opponent disca
  3. Dark Deal（{2}{B}｜Sorcery） — Each player discards all the cards in their hand, then draws that many cards minus one.
  4. Rankle, Master of Pranks（{2}{B}{B}｜Legendary Creature — Faerie Rogue） — Flying, haste Whenever Rankle deals combat damage to a player, choose any number — • Each player discards a card. • Each player loses 1 life and draws a card. • Each play
  5. Oppression（{1}{B}{B}｜Enchantment） — Whenever a player casts a spell, that player discards a card.
  6. Plaguecrafter（{2}{B}｜Creature — Human Shaman） — When this creature enters, each player sacrifices a creature or planeswalker of their choice. Each player who can't discards a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Cabal Coffers（｜Land） — {2}, {T}: Add {B} for each Swamp you control.
  - Sheoldred's Edict（{1}{B}｜Instant） — Choose one — • Each opponent sacrifices a nontoken creature of their choice. • Each opponent sacrifices a creature token of their 


## Light-Paws, Emperor's Voice ｜ 帝皇玉音轻脚
- 颜色 W ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Fox Advisor
- 流行度：EDHREC 全时段第 183 位，约 12435 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.17 ｜ 上手难度 3/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $1.52
- 社区标签：灵气、主将单挑、结界流、快攻、锁场、工具箱
- 完整牌面：Whenever an Aura you control enters, if you cast it, you may search your library for an Aura card with mana value less than or equal to that Aura and with a different name than each Aura you control, put that card onto the battlefield attached to Light-Paws, then shuffle.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ethereal Armor（{W}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 for each enchantment you control and has first strike.
  2. All That Glitters（{1}{W}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 for each artifact and/or enchantment you control.
  3. Sage's Reverie（{3}{W}｜Enchantment — Aura） — Enchant creature When this Aura enters, draw a card for each Aura you control that's attached to a creature. Enchanted creature gets +1/+1 for each Aura you control that'
  4. Hyena Umbra（{W}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 and has first strike. Umbra armor (If enchanted creature would be destroyed, instead remove all damage from it and destroy 
  5. Daybreak Coronet（{W}{W}｜Enchantment — Aura） — Enchant creature with another Aura attached to it Enchanted creature gets +3/+3 and has first strike, vigilance, and lifelink. (Damage dealt by the creature also causes i
  6. Kor Spiritdancer（{1}{W}｜Creature — Kor Wizard） — This creature gets +2/+2 for each Aura attached to it. Whenever you cast an Aura spell, you may draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Sram, Senior Edificer（{1}{W}｜Legendary Creature — Dwarf Advisor） — Whenever you cast an Aura, Equipment, or Vehicle spell, draw a card.
  - Mantle of the Ancients（{3}{W}{W}｜Enchantment — Aura） — Enchant creature you control When this Aura enters, return any number of target Aura and/or Equipment cards from your graveyard to
  - Spirit Mantle（{1}{W}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 and has protection from creatures.
  - Timely Ward（{2}{W}｜Enchantment — Aura） — You may cast this spell as though it had flash if it targets a commander. Enchant creature Enchanted creature has indestructible.


## Xenagos, God of Revels ｜ 贪欢神谢纳戈斯
- 颜色 RG ｜ 法术力值 5.0 ｜ 类型 Legendary Enchantment Creature — God
- 流行度：EDHREC 全时段第 308 位，约 8685 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.65 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $10.96
- 社区标签：额外战斗、快攻、加速、大生物、中速、＋1/＋1 指示物
- 完整牌面：Indestructible
As long as your devotion to red and green is less than seven, Xenagos isn't a creature.
At the beginning of combat on your turn, another target creature you control gains haste and gets +X/+X until end of turn, where X is that creature's power.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Goreclaw, Terror of Qal Sisma（{3}{G}｜Legendary Creature — Bear） — Creature spells you cast with power 4 or greater cost {2} less to cast. Whenever Goreclaw attacks, each creature you control with power 4 or greater gets +1/+1 and gains 
  2. Anzrag, the Quake-Mole（{2}{R}{G}｜Legendary Creature — Mole God） — Whenever Anzrag becomes blocked, untap each creature you control. After this phase, there is an additional combat phase. {3}{R}{R}{G}{G}: Anzrag must be blocked each comb
  3. Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess combat damage to the player or planeswalker
  4. Quartzwood Crasher（{2}{R}{R}{G}｜Creature — Dinosaur Beast） — Trample Whenever one or more creatures you control with trample deal combat damage to a player, create an X/X green Dinosaur Beast creature token with trample, where X is
  5. Ilharg, the Raze-Boar（{3}{R}{R}｜Legendary Creature — Boar God） — Trample Whenever Ilharg attacks, you may put a creature card from your hand onto the battlefield tapped and attacking. Return that creature to your hand at the beginning 
  6. Ojer Kaslem, Deepest Growth（｜） — 
- **出场率最高的牌**（大多数牌组都会放）
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Rootbound Crag（｜Land） — This land enters tapped unless you control a Mountain or a Forest. {T}: Add {R} or {G}.
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Talrand, Sky Summoner ｜ 空召师陶岚
- 颜色 U ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Merfolk Wizard
- 流行度：EDHREC 全时段第 403 位，约 7028 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.38 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $1.80
- 社区标签：法术连发、衍生物、控制、小牌抽、飞行、反击咒语
- 完整牌面：Whenever you cast an instant or sorcery spell, create a 2/2 blue Drake creature token with flying.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Opt（{U}｜Instant） — Scry 1. (Look at the top card of your library. You may put that card on the bottom.) Draw a card.
  2. Favorable Winds（{1}{U}｜Enchantment） — Creatures you control with flying get +1/+1.
  3. Murmuring Mystic（{3}{U}｜Creature — Human Wizard） — Whenever you cast an instant or sorcery spell, create a 1/1 blue Bird Illusion creature token with flying.
  4. Preordain（{U}｜Sorcery） — Scry 2, then draw a card. (To scry 2, look at the top two cards of your library, then put any number of them on the bottom and the rest on top in any order.)
  5. Impulse（{1}{U}｜Instant） — Look at the top four cards of your library. Put one of them into your hand and the rest on the bottom of your library in any order.
  6. Winged Words（{2}{U}｜Sorcery） — This spell costs {1} less to cast if you control a creature with flying. Draw two cards.
- **出场率最高的牌**（大多数牌组都会放）
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  - Ponder（{U}｜Sorcery） — Look at the top three cards of your library, then put them back in any order. You may shuffle. Draw a card.
  - Mystic Sanctuary（｜Land — Island） — ({T}: Add {U}.) This land enters tapped unless you control three or more other Islands. When this land enters untapped, you may pu
  - Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.


## Wyleth, Soul of Steel ｜ 钢铁之魂威烈斯
- 颜色 WR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Warrior
- 流行度：EDHREC 全时段第 939 位，约 2696 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.18 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $None
- 社区标签：装备、主将单挑、灵气、快攻、神器、额外战斗
- 完整牌面：Trample
Whenever Wyleth attacks, draw a card for each Aura and Equipment attached to it.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sigarda's Aid（{W}｜Enchantment） — You may cast Aura and Equipment spells as though they had flash. Whenever an Equipment you control enters, you may attach it to target creature you control.
  2. Sram, Senior Edificer（{1}{W}｜Legendary Creature — Dwarf Advisor） — Whenever you cast an Aura, Equipment, or Vehicle spell, draw a card.
  3. Blackblade Reforged（{2}｜Legendary Artifact — Equipment） — Equipped creature gets +1/+1 for each land you control. Equip legendary creature {3} Equip {7}
  4. Spirit Mantle（{1}{W}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 and has protection from creatures.
  5. Danitha Capashen, Paragon（{2}{W}｜Legendary Creature — Human Knight） — First strike, vigilance, lifelink Aura and Equipment spells you cast cost {1} less to cast.
  6. Timely Ward（{2}{W}｜Enchantment — Aura） — You may cast this spell as though it had flash if it targets a commander. Enchant creature Enchanted creature has indestructible.
- **出场率最高的牌**（大多数牌组都会放）
  - Boros Charm（{R}{W}｜Instant） — Choose one — • Boros Charm deals 4 damage to target player or planeswalker. • Permanents you control gain indestructible until end
  - Puresteel Paladin（{W}{W}｜Creature — Human Knight） — Whenever an Equipment you control enters, you may draw a card. Metalcraft — Equipment you control have equip {0} as long as you co
  - Slayers' Stronghold（｜Land） — {T}: Add {C}. {R}{W}, {T}: Target creature gets +2/+0 and gains vigilance and haste until end of turn.
  - Boros Signet（{2}｜Artifact） — {1}, {T}: Add {R}{W}.
