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

# 素材：37 位主将


## Y'shtola, Night's Blessed ｜ 夜之民雅·修特拉
- 颜色 WUB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Cat Warlock
- 流行度：EDHREC 全时段第 1 位，约 56157 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.92 ｜ 上手难度 3/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $5.36
- 社区标签：控制、法术连发、生命增益、烧血、吸取生命、组合技
- 完整牌面：Vigilance
At the beginning of each end step, if a player lost 4 or more life this turn, you draw a card.
Whenever you cast a noncreature spell with mana value 3 or greater, Y'shtola deals 2 damage to each opponent and you gain 2 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Snuff Out（{3}{B}｜Instant） — If you control a Swamp, you may pay 4 life rather than pay this spell's mana cost. Destroy target nonblack creature. It can't be regenerated.
  2. Curiosity（{U}｜Enchantment — Aura） — Enchant creature Whenever enchanted creature deals damage to an opponent, you may draw a card.
  3. Papalymo Totolymo（{W}{B}｜Legendary Creature — Dwarf Wizard） — Whenever you cast a noncreature spell, Papalymo Totolymo deals 1 damage to each opponent and you gain 1 life. {4}, {T}, Sacrifice Papalymo Totolymo: Each opponent who los
  4. Propaganda（{2}{U}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  5. Emet-Selch of the Third Seat（{2}{U}{B}｜Legendary Creature — Elder Wizard） — Spells you cast from your graveyard cost {2} less to cast. Whenever one or more opponents lose life, you may cast target instant or sorcery card from your graveyard. If t
  6. Lyse Hext（{1}{W}{U}｜Legendary Creature — Human Rebel Monk） — Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.) Noncreature spells you cast cost {1} less to cast. As long as you've cast two
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.
  - Void Rend（{W}{U}{B}｜Instant） — This spell can't be countered. Destroy target nonland permanent.
  - Talisman of Progress（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {U}. This artifact deals 1 damage to you.
  - Talisman of Hierarchy（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {B}. This artifact deals 1 damage to you.


## Edgar Markov ｜ 艾德嘉马可夫
- 颜色 WBR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Vampire Knight
- 流行度：EDHREC 全时段第 2 位，约 51527 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 2.05 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $44.22
- 社区标签：吸血鬼、生命增益、衍生物、快攻、牺牲流、＋1/＋1 指示物
- 完整牌面：Eminence — Whenever you cast another Vampire spell, if Edgar is in the command zone or on the battlefield, create a 1/1 black Vampire creature token.
First strike, haste
Whenever Edgar attacks, put a +1/+1 counter on each Vampire you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Captivating Vampire（{1}{B}{B}｜Creature — Vampire） — Other Vampire creatures you control get +1/+1. Tap five untapped Vampires you control: Gain control of target creature. It becomes a Vampire in addition to its other type
  2. Cordial Vampire（{B}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, put a +1/+1 counter on each Vampire you control.
  3. Stromkirk Captain（{1}{B}{R}｜Creature — Vampire Soldier） — First strike Other Vampire creatures you control get +1/+1 and have first strike.
  4. Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  5. Indulgent Aristocrat（{B}｜Creature — Vampire Noble） — Lifelink {2}, Sacrifice a creature: Put a +1/+1 counter on each Vampire you control.
  6. Legion Lieutenant（{W}{B}｜Creature — Vampire Knight） — Other Vampires you control get +1/+1.
- **出场率最高的牌**（大多数牌组都会放）
  - Welcoming Vampire（{2}{W}｜Creature — Vampire） — Flying Whenever one or more other creatures you control with power 2 or less enter, draw a card. This ability triggers only once e
  - Bloodline Keeper（｜） — 
  - Sanctum Seeker（{2}{B}{B}｜Creature — Vampire Knight） — Whenever a Vampire you control attacks, each opponent loses 1 life and you gain 1 life.
  - Vito, Thorn of the Dusk Rose（{2}{B}｜Legendary Creature — Vampire Cleric） — Whenever you gain life, target opponent loses that much life. {3}{B}{B}: Creatures you control gain lifelink until end of turn.


## The Ur-Dragon ｜ 太初龙
- 颜色 WUBRG ｜ 法术力值 9.0 ｜ 类型 Legendary Creature — Dragon Avatar
- 流行度：EDHREC 全时段第 3 位，约 51281 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.97 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $36.25
- 社区标签：龙、飞行、快攻、加速、变形兽、组合技
- 完整牌面：Eminence — As long as The Ur-Dragon is in the command zone or on the battlefield, other Dragon spells you cast cost {1} less to cast.
Flying
Whenever one or more Dragons you control attack, draw that many cards, then you may put a permanent card from your hand onto the battlefield.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Miirym, Sentinel Wyrm（{3}{G}{U}{R}｜Legendary Creature — Dragon Spirit） — Flying, ward {2} Whenever another nontoken Dragon you control enters, create a token that's a copy of it, except the token isn't legendary.
  2. Dragon Tempest（{1}{R}｜Enchantment） — Whenever a creature you control with flying enters, it gains haste until end of turn. Whenever a Dragon you control enters, it deals X damage to any target, where X is th
  3. Crux of Fate（{3}{B}{B}｜Sorcery） — Choose one — • Destroy all Dragon creatures. • Destroy all non-Dragon creatures.
  4. Tiamat（{2}{W}{U}{B}{R}{G}｜Legendary Creature — Dragon God） — Flying When Tiamat enters, if you cast it, search your library for up to five Dragon cards not named Tiamat that each have different names, reveal them, put them into you
  5. Haven of the Spirit Dragon（｜Land） — {T}: Add {C}. {T}: Add one mana of any color. Spend this mana only to cast a Dragon creature spell. {2}, {T}, Sacrifice this land: Return target Dragon creature card or U
  6. Atarka, World Render（{5}{R}{G}｜Legendary Creature — Dragon） — Flying, trample Whenever a Dragon you control attacks, it gains double strike until end of turn.
- **出场率最高的牌**（大多数牌组都会放）
  - Lathliss, Dragon Queen（{4}{R}{R}｜Legendary Creature — Dragon） — Flying Whenever another nontoken Dragon you control enters, create a 5/5 red Dragon creature token with flying. {1}{R}: Dragons yo
  - Dragonlord Dromoka（{4}{G}{W}｜Legendary Creature — Elder Dragon） — This spell can't be countered. Flying, lifelink Your opponents can't cast spells during your turn.
  - Terror of the Peaks（{3}{R}{R}｜Creature — Dragon） — Flying Spells your opponents cast that target this creature cost an additional 3 life to cast. Whenever another creature you contr
  - Temur Ascendancy（{G}{U}{R}｜Enchantment） — Creatures you control have haste. Whenever a creature you control with power 4 or greater enters, you may draw a card.


## Atraxa, Praetors' Voice ｜ 魔判官之声亚崔夏
- 颜色 WUBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Phyrexian Angel Horror
- 流行度：EDHREC 全时段第 4 位，约 45365 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.72 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $27.85
- 社区标签：毒侵、＋1/＋1 指示物、鹏洛客、增殖、非瑞人、－1/－1 指示物
- 完整牌面：Flying, vigilance, deathtouch, lifelink
At the beginning of your end step, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Tekuthal, Inquiry Dominus（{2}{U}{U}｜Legendary Creature — Phyrexian Horror） — Flying If you would proliferate, proliferate twice instead. {1}{U/P}{U/P}, Remove three counters from among other artifacts, creatures, and planeswalkers you control: Put
  2. Evolution Sage（{2}{G}｜Creature — Elf Druid） — Landfall — Whenever a land you control enters, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
  3. Karn's Bastion（｜Land） — {T}: Add {C}. {4}, {T}: Proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
  4. Ezuri, Stalker of Spheres（{2}{G}{U}｜Legendary Creature — Phyrexian Elf Warrior） — When Ezuri enters, you may pay {3}. If you do, proliferate twice. Whenever you proliferate, draw a card.
  5. Inexorable Tide（{3}{U}{U}｜Enchantment） — Whenever you cast a spell, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
  6. Vraska, Betrayal's Sting（{4}{B}{B/P}｜Legendary Planeswalker — Vraska） — Compleated ({B/P} can be paid with {B} or 2 life. If life was paid, this planeswalker enters with two fewer loyalty counters.) 0: You draw a card and lose 1 life. Prolife
- **出场率最高的牌**（大多数牌组都会放）
  - Thrummingbird（{1}{U}｜Creature — Phyrexian Bird Horror） — Flying Whenever this creature deals combat damage to a player, proliferate. (Choose any number of permanents and/or players, then 
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Tezzeret's Gambit（{3}{U/P}｜Sorcery） — ({U/P} can be paid with either {U} or 2 life.) Draw two cards, then proliferate. (Choose any number of permanents and/or players, 
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Krenko, Mob Boss ｜ 暴民头目克仑可
- 颜色 R ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Goblin Warrior
- 流行度：EDHREC 全时段第 5 位，约 44388 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 1.17 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $2.76
- 社区标签：鬼怪、衍生物、快攻、组合技、烧血、＋1/＋1 指示物
- 完整牌面：{T}: Create X 1/1 red Goblin creature tokens, where X is the number of Goblins you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Goblin Warchief（{1}{R}{R}｜Creature — Goblin Warrior） — Goblin spells you cast cost {1} less to cast. Goblins you control have haste.
  2. Skirk Prospector（{R}｜Creature — Goblin） — Sacrifice a Goblin: Add {R}.
  3. Goblin Matron（{2}{R}｜Creature — Goblin） — When this creature enters, you may search your library for a Goblin card, reveal that card, put it into your hand, then shuffle.
  4. Goblin Chieftain（{1}{R}{R}｜Creature — Goblin） — Haste (This creature can attack and {T} as soon as it comes under your control.) Other Goblin creatures you control get +1/+1 and have haste.
  5. Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  6. Goblin Bombardment（{1}{R}｜Enchantment） — Sacrifice a creature: This enchantment deals 1 damage to any target.
- **出场率最高的牌**（大多数牌组都会放）
  - Brightstone Ritual（{R}｜Instant） — Add {R} for each Goblin on the battlefield.
  - Pashalik Mons（{2}{R}｜Legendary Creature — Goblin Warrior） — Whenever Pashalik Mons or another Goblin you control dies, Pashalik Mons deals 1 damage to any target. {3}{R}, Sacrifice a Goblin:
  - Siege-Gang Commander（{3}{R}{R}｜Creature — Goblin） — When this creature enters, create three 1/1 red Goblin creature tokens. {1}{R}, Sacrifice a Goblin: This creature deals 2 damage t
  - Goblin King（{1}{R}{R}｜Creature — Goblin） — Other Goblins get +1/+1 and have mountainwalk.


## Vivi Ornitier ｜ 比比·奥尼提尔
- 颜色 UR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Wizard
- 流行度：EDHREC 全时段第 6 位，约 41814 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 2.81 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $32.30
- 社区标签：法术连发、风暴、烧血、组合技、＋1/＋1 指示物、控制
- 完整牌面：{0}: Add X mana in any combination of {U} and/or {R}, where X is Vivi Ornitier's power. Activate only during your turn and only once each turn.
Whenever you cast a noncreature spell, put a +1/+1 counter on Vivi Ornitier and it deals 1 damage to each opponent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Curiosity（{U}｜Enchantment — Aura） — Enchant creature Whenever enchanted creature deals damage to an opponent, you may draw a card.
  2. Ophidian Eye（{2}{U}｜Enchantment — Aura） — Flash (You may cast this spell any time you could cast an instant.) Enchant creature Whenever enchanted creature deals damage to an opponent, you may draw a card.
  3. Harmonic Prodigy（{1}{R}｜Creature — Human Wizard） — Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.) If a triggered ability of a Shaman or another Wizard you control triggers, th
  4. Tandem Lookout（{2}{U}｜Creature — Human Scout） — Soulbond (You may pair this creature with another unpaired creature when either enters. They remain paired for as long as you control both of them.) As long as Tandem Loo
  5. Wizard's Staff（{1}{U}｜Artifact — Equipment） — Equipped creature has prowess. (Whenever its controller casts a noncreature spell, that creature gets +1/+1 until end of turn.) If a triggered ability of equipped creatur
  6. Gitaxian Probe（{U/P}｜Sorcery） — ({U/P} can be paid with either {U} or 2 life.) Look at target player's hand. Draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  - Steam Vents（｜Land — Island Mountain） — ({T}: Add {U} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Ponder（{U}｜Sorcery） — Look at the top three cards of your library, then put them back in any order. You may shuffle. Draw a card.
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.


## Sauron, the Dark Lord ｜ 黑暗魔君索隆
- 颜色 UBR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Avatar Horror
- 流行度：EDHREC 全时段第 7 位，约 40433 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.15 ｜ 上手难度 5/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $19.85
- 社区标签：坟场复活、僵尸、聚兵、＋1/＋1 指示物、衍生物、幽灵
- 完整牌面：Ward—Sacrifice a legendary artifact or legendary creature.
Whenever an opponent casts a spell, amass Orcs 1.
Whenever an Army you control deals combat damage to a player, the Ring tempts you.
Whenever the Ring tempts you, you may discard your hand. If you do, draw four cards.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Call of the Ring（{1}{B}｜Enchantment） — At the beginning of your upkeep, the Ring tempts you. Whenever you choose a creature as your Ring-bearer, you may pay 2 life. If you do, draw a card.
  2. Saruman, the White Hand（{1}{U}{B}{R}｜Legendary Creature — Avatar Wizard） — Whenever you cast a noncreature spell, amass Orcs X, where X is that spell's mana value. (Put X +1/+1 counters on an Army you control. It's also an Orc. If you don't cont
  3. Barad-dûr（｜Legendary Land） — Barad-dûr enters tapped unless you control a legendary creature. {T}: Add {B}. {X}{X}{B}, {T}: Amass Orcs X. Activate only if a creature died this turn.
  4. Relic of Sauron（{4}｜Artifact） — {T}: Add two mana in any combination of {U}, {B}, and/or {R}. {3}, {T}: Draw two cards, then discard a card.
  5. The Black Gate（｜Legendary Land — Gate） — As The Black Gate enters, you may pay 3 life. If you don't, it enters tapped. {T}: Add {B}. {1}{B}, {T}: Choose a player with the most life or tied for most life. Target 
  6. Witch-king of Angmar（{3}{B}{B}｜Legendary Creature — Wraith Noble） — Flying Whenever one or more creatures deal combat damage to you, each opponent sacrifices a creature of their choice that dealt combat damage to you this turn. The Ring t
- **出场率最高的牌**（大多数牌组都会放）
  - Reanimate（{B}｜Sorcery） — Put target creature card from a graveyard onto the battlefield under your control. You lose life equal to that card's mana value.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Crumbling Necropolis（｜Land） — This land enters tapped. {T}: Add {U}, {B}, or {R}.
  - Drowned Catacomb（｜Land） — This land enters tapped unless you control an Island or a Swamp. {T}: Add {U} or {B}.


## Kaalia of the Vast ｜ 穹境的卡莉雅
- 颜色 WBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Cleric
- 流行度：EDHREC 全时段第 8 位，约 40129 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.19 ｜ 上手难度 2/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $4.70
- 社区标签：飞行、天使、快攻、恶魔、龙、额外战斗
- 完整牌面：Flying
Whenever Kaalia attacks an opponent, you may put an Angel, Demon, or Dragon creature card from your hand onto the battlefield tapped and attacking that opponent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Gisela, Blade of Goldnight（{4}{R}{W}{W}｜Legendary Creature — Angel） — Flying, first strike If a source would deal damage to an opponent or a permanent an opponent controls, that source deals double that damage to that player or permanent in
  2. Rune-Scarred Demon（{5}{B}{B}｜Creature — Demon） — Flying When this creature enters, search your library for a card, put it into your hand, then shuffle.
  3. Avacyn, Angel of Hope（{5}{W}{W}{W}｜Legendary Creature — Angel） — Flying, vigilance, indestructible Other permanents you control have indestructible.
  4. Aurelia, the Warleader（{2}{R}{R}{W}{W}｜Legendary Creature — Angel） — Flying, vigilance, haste Whenever Aurelia attacks for the first time each turn, untap all creatures you control. After this phase, there is an additional combat phase.
  5. Sephara, Sky's Blade（{4}{W}{W}{W}｜Legendary Creature — Angel） — You may pay {W} and tap four untapped creatures you control with flying rather than pay this spell's mana cost. Flying, lifelink Other creatures you control with flying h
  6. Liesa, Forgotten Archangel（{2}{W}{W}{B}｜Legendary Creature — Angel） — Flying, lifelink Whenever another nontoken creature you control dies, return that card to its owner's hand at the beginning of the next end step. If a creature an opponen
- **出场率最高的牌**（大多数牌组都会放）
  - Master of Cruelties（{3}{B}{R}｜Creature — Demon） — First strike, deathtouch This creature can only attack alone. Whenever this creature attacks a player and isn't blocked, that play
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Balefire Dragon（{5}{R}{R}｜Creature — Dragon） — Flying Whenever this creature deals combat damage to a player, it deals that much damage to each creature that player controls.


## Teval, the Balanced Scale ｜ 公正鳞龙特瓦尔
- 颜色 UBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Spirit Dragon
- 流行度：EDHREC 全时段第 9 位，约 39580 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.6 ｜ 上手难度 3/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $5.48
- 社区标签：坟场复活、地牌核心、磨牌、自磨、坟场、衍生物
- 完整牌面：Flying
Whenever Teval attacks, mill three cards. Then you may return a land card from your graveyard to the battlefield tapped.
Whenever one or more cards leave your graveyard, create a 2/2 black Zombie Druid creature token.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Teval's Judgment（{2}{B}｜Enchantment） — Whenever one or more cards leave your graveyard, choose one that hasn't been chosen this turn — • Draw a card. • Create a Treasure token. • Create a 2/2 black Zombie Drui
  2. Colossal Grave-Reaver（{6}{B}{G}｜Creature — Dragon） — Flying Whenever this creature enters or attacks, mill three cards. Whenever one or more creature cards are put into your graveyard from your library, put one of them onto
  3. Life from the Loam（{1}{G}｜Sorcery） — Return up to three target land cards from your graveyard to your hand. Dredge 3 (If you would draw a card, you may mill three cards instead. If you do, return this card f
  4. Gravecrawler（{B}｜Creature — Zombie） — This creature can't block. You may cast this card from your graveyard as long as you control a Zombie.
  5. Victimize（{2}{B}｜Sorcery） — Choose two target creature cards in your graveyard. Sacrifice a creature. If you do, return the chosen cards to the battlefield tapped.
  6. Hedron Crab（{U}｜Creature — Crab） — Landfall — Whenever a land you control enters, target player mills three cards. (They put the top three cards of their library into their graveyard.)
- **出场率最高的牌**（大多数牌组都会放）
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Wonder（{3}{U}｜Creature — Incarnation） — Flying As long as this card is in your graveyard and you control an Island, creatures you control have flying.
  - Dreamroot Cascade（｜Land） — This land enters tapped unless you control two or more other lands. {T}: Add {G} or {U}.


## Fire Lord Azula ｜ 烈火君阿祖拉
- 颜色 UBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Noble
- 流行度：EDHREC 全时段第 10 位，约 38554 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 4/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $1.07
- 社区标签：法术连发、组合技、咒语复制、快攻、风暴、烧血
- 完整牌面：Firebending 2 (Whenever this creature attacks, add {R}{R}. This mana lasts until end of combat.)
Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell. You may choose new targets for the copy. (A copy of a permanent spell becomes a token.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Storm-Kiln Artist（{3}{R}｜Creature — Dwarf Shaman） — This creature gets +1/+0 for each artifact you control. Magecraft — Whenever you cast or copy an instant or sorcery spell, create a Treasure token. (It's an artifact with
  2. Big Score（{3}{R}｜Instant） — As an additional cost to cast this spell, discard a card. Draw two cards and create two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: Add one mana 
  3. Electrodominance（{X}{R}{R}｜Instant） — Electrodominance deals X damage to any target. You may cast a spell with mana value X or less from your hand without paying its mana cost.
  4. Archmage Emeritus（{2}{U}{U}｜Creature — Human Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, draw a card.
  5. Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.
  6. Lightning Bolt（{R}｜Instant） — Lightning Bolt deals 3 damage to any target.
- **出场率最高的牌**（大多数牌组都会放）
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Snap（{1}{U}｜Instant） — Return target creature to its owner's hand. Untap up to two lands.
  - Unexpected Windfall（{2}{R}{R}｜Instant） — As an additional cost to cast this spell, discard a card. Draw two cards and create two Treasure tokens. (They're artifacts with "
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.


## Ms. Bumbleflower ｜ 野花小姐
- 颜色 WUG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Rabbit Citizen
- 流行度：EDHREC 全时段第 11 位，约 37240 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.81 ｜ 上手难度 2/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $7.47
- 社区标签：＋1/＋1 指示物、群体恩惠、换手牌、抽牌、控制、小牌抽
- 完整牌面：Vigilance
Whenever you cast a spell, target opponent draws a card. Put a +1/+1 counter on target creature. It gains flying until end of turn. If this is the second time this ability has resolved this turn, you draw two cards.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Wizard Class（{U}｜Enchantment — Class） — (Gain the next level as a sorcery to add its ability.) You have no maximum hand size. {2}{U}: Level 2 When this Class becomes level 2, draw two cards. {4}{U}: Level 3 Whe
  2. Loran of the Third Path（{2}{W}｜Legendary Creature — Human Artificer） — Vigilance When Loran enters, destroy up to one target artifact or enchantment. {T}: You and target opponent each draw a card.
  3. Wear Down（{1}{G}｜Sorcery） — Gift a card (You may promise an opponent a gift as you cast this spell. If you do, they draw a card before its other effects.) Destroy target artifact or enchantment. If 
  4. Long River's Pull（{U}{U}｜Instant） — Gift a card (You may promise an opponent a gift as you cast this spell. If you do, they draw a card before its other effects.) Counter target creature spell. If the gift 
  5. Peerless Recycling（{1}{G}｜Instant） — Gift a card (You may promise an opponent a gift as you cast this spell. If you do, they draw a card before its other effects.) Return target permanent card from your grav
  6. Twenty-Toed Toad（{3}{U}｜Creature — Frog Wizard） — Your maximum hand size is twenty. Whenever you attack with two or more creatures, put a +1/+1 counter on this creature and draw a card. Whenever this creature attacks, yo
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Sunpetal Grove（｜Land） — This land enters tapped unless you control a Forest or a Plains. {T}: Add {G} or {W}.
  - An Offer You Can't Refuse（{U}｜Instant） — Counter target noncreature spell. Its controller creates two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: 


## Pantlaza, Sun-Favored ｜ 烈阳眷恩潘塔札
- 颜色 WRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Dinosaur
- 流行度：EDHREC 全时段第 12 位，约 37236 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.84 ｜ 上手难度 4/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $6.03
- 社区标签：恐龙、发现、加速、闪现回场、快攻、大生物
- 完整牌面：Whenever Pantlaza or another Dinosaur you control enters, you may discover X, where X is that creature's toughness. Do this only once each turn. (Exile cards from the top of your library until you exile a nonland card with that mana value or less. Cast it without paying its mana cost or put it into your hand. Put the rest on the bottom in a random order.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Gishath, Sun's Avatar（{5}{R}{G}{W}｜Legendary Creature — Dinosaur Avatar） — Vigilance, trample, haste Whenever Gishath deals combat damage to a player, reveal that many cards from the top of your library. Put any number of Dinosaur creature cards
  2. Zacama, Primal Calamity（{6}{R}{G}{W}｜Legendary Creature — Elder Dinosaur） — Reach, vigilance, trample When Zacama enters, if you cast it, untap all lands you control. {2}{R}: Zacama deals 3 damage to target creature. {2}{G}: Destroy target artifa
  3. Regisaur Alpha（{3}{R}{G}｜Creature — Dinosaur） — Other Dinosaurs you control have haste. When this creature enters, create a 3/3 green Dinosaur creature token with trample.
  4. Wrathful Raptors（{4}{R}｜Creature — Dinosaur） — Trample Whenever a Dinosaur you control is dealt damage, it deals that much damage to any target that isn't a Dinosaur.
  5. Earthshaker Dreadmaw（{4}{G}{G}｜Creature — Dinosaur） — Trample When this creature enters, draw a card for each other Dinosaur you control.
  6. Curious Altisaur（{3}{G}｜Creature — Dinosaur） — Reach, vigilance Whenever a Dinosaur you control deals combat damage to a player, draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Etali, Primal Storm（{4}{R}{R}｜Legendary Creature — Elder Dinosaur） — Whenever Etali attacks, exile the top card of each player's library, then you may cast any number of spells from among those cards
  - Rhythm of the Wild（{1}{R}{G}｜Enchantment） — Creature spells you control can't be countered. Nontoken creatures you control have riot. (They enter with your choice of a +1/+1 
  - Topiary Stomper（{1}{G}{G}｜Creature — Plant Dinosaur） — Vigilance (Attacking doesn't cause this creature to tap.) When this creature enters, search your library for a basic land card, pu
  - Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess com


## Giada, Font of Hope ｜ 希望圣源吉娅妲
- 颜色 W ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Angel
- 流行度：EDHREC 全时段第 13 位，约 36665 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.46 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.72
- 社区标签：天使、生命增益、＋1/＋1 指示物、飞行、衍生物、快攻
- 完整牌面：Flying, vigilance
Each other Angel you control enters with an additional +1/+1 counter on it for each Angel you already control.
{T}: Add {W}. Spend this mana only to cast an Angel spell.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Lyra Dawnbringer（{3}{W}{W}｜Legendary Creature — Angel） — Flying First strike (This creature deals combat damage before creatures without first strike.) Lifelink (Damage dealt by this creature also causes you to gain that much l
  2. Righteous Valkyrie（{2}{W}｜Creature — Angel Cleric） — Flying Whenever another Angel or Cleric you control enters, you gain life equal to that creature's toughness. As long as you have at least 7 life more than your starting 
  3. Youthful Valkyrie（{1}{W}｜Creature — Angel） — Flying Whenever another Angel you control enters, put a +1/+1 counter on this creature.
  4. Herald of War（{3}{W}{W}｜Creature — Angel） — Flying Whenever this creature attacks, put a +1/+1 counter on it. Angel spells and Human spells you cast cost {1} less to cast for each +1/+1 counter on this creature.
  5. Seraph Sanctuary（｜Land） — When this land enters, you gain 1 life. Whenever an Angel you control enters, you gain 1 life. {T}: Add {C}.
  6. Starnheim Aspirant（{2}{W}｜Creature — Human Cleric） — Angel spells you cast cost {2} less to cast.
- **出场率最高的牌**（大多数牌组都会放）
  - Pearl Medallion（{2}｜Artifact） — White spells you cast cost {1} less to cast.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Sephara, Sky's Blade（{4}{W}{W}{W}｜Legendary Creature — Angel） — You may pay {W} and tap four untapped creatures you control with flying rather than pay this spell's mana cost. Flying, lifelink O
  - Resplendent Angel（{1}{W}{W}｜Creature — Angel） — Flying At the beginning of each end step, if you gained 5 or more life this turn, create a 4/4 white Angel creature token with fly


## Lathril, Blade of the Elves ｜ 妖精之刃拉席莉
- 颜色 BG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Elf Noble
- 流行度：EDHREC 全时段第 14 位，约 35951 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.91 ｜ 上手难度 3/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $2.00
- 社区标签：妖精、衍生物、快攻、＋1/＋1 指示物、加速、组合技
- 完整牌面：Menace (This creature can't be blocked except by two or more creatures.)
Whenever Lathril deals combat damage to a player, create that many 1/1 green Elf Warrior creature tokens.
{T}, Tap ten untapped Elves you control: Each opponent loses 10 life and you gain 10 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Elvish Archdruid（{1}{G}{G}｜Creature — Elf Druid） — Other Elf creatures you control get +1/+1. {T}: Add {G} for each Elf you control.
  2. Priest of Titania（{1}{G}｜Creature — Elf Druid） — {T}: Add {G} for each Elf on the battlefield.
  3. Imperious Perfect（{2}{G}｜Creature — Elf Warrior） — Other Elves you control get +1/+1. {G}, {T}: Create a 1/1 green Elf Warrior creature token.
  4. Marwyn, the Nurturer（{2}{G}｜Legendary Creature — Elf Druid） — Whenever another Elf you control enters, put a +1/+1 counter on Marwyn. {T}: Add an amount of {G} equal to Marwyn's power.
  5. Beast Whisperer（{2}{G}{G}｜Creature — Elf Druid） — Whenever you cast a creature spell, draw a card.
  6. Elvish Warmaster（{1}{G}｜Creature — Elf Warrior） — Whenever one or more other Elves you control enter, create a 1/1 green Elf Warrior creature token. This ability triggers only once each turn. {5}{G}{G}: Elves you control
- **出场率最高的牌**（大多数牌组都会放）
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Reclamation Sage（{2}{G}｜Creature — Elf Shaman） — When this creature enters, you may destroy target artifact or enchantment.
  - Dwynen, Gilt-Leaf Daen（{2}{G}{G}｜Legendary Creature — Elf Warrior） — Reach (This creature can block creatures with flying.) Other Elf creatures you control get +1/+1. Whenever Dwynen attacks, you gai


## The Wise Mothman ｜ 天蛾人智者
- 颜色 UBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Insect Mutant
- 流行度：EDHREC 全时段第 15 位，约 33866 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 1.01 ｜ 上手难度 3/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $12.52
- 社区标签：磨牌、＋1/＋1 指示物、突变体、辐射指示物、坟场复活、自磨
- 完整牌面：Flying
Whenever The Wise Mothman enters or attacks, each player gets a rad counter.
Whenever one or more nonland cards are milled, put a +1/+1 counter on each of up to X target creatures, where X is the number of nonland cards milled this way.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Nuclear Fallout（{X}{B}{B}｜Sorcery） — Each creature gets twice -X/-X until end of turn. Each player gets X rad counters.
  2. Glowing One（{2}{G}｜Creature — Zombie Mutant） — Deathtouch Whenever this creature deals combat damage to a player, they get four rad counters. Whenever a player mills a nonland card, you gain 1 life.
  3. Vexing Radgull（{1}{U}｜Creature — Bird Mutant） — Flying Whenever this creature deals combat damage to a player, that player gets two rad counters if they don't have any rad counters. Otherwise, proliferate. (Choose any 
  4. Mutational Advantage（{1}{G}{U}｜Instant） — Permanents you control with counters on them gain hexproof and indestructible until end of turn. Prevent all damage that would be dealt to those permanents this turn. Pro
  5. Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  6. Mirelurk Queen（{4}{U}｜Creature — Crab Mutant） — Vigilance When this creature enters, target player gets two rad counters. Whenever one or more nonland cards are milled, draw a card, then put a +1/+1 counter on this cre
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Screeching Scorchbeast（{4}{B}{B}｜Creature — Bat Mutant） — Flying, menace Whenever this creature attacks, each player gets two rad counters. Whenever one or more nonland cards are milled, y
  - Drowned Catacomb（｜Land） — This land enters tapped unless you control an Island or a Swamp. {T}: Add {U} or {B}.


## Toph, the First Metalbender ｜ 冶金师始祖拓芙
- 颜色 WRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Warrior Ally
- 流行度：EDHREC 全时段第 16 位，约 33675 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 4/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $1.07
- 社区标签：地牌核心、神器、＋1/＋1 指示物、运土、地落、加速
- 完整牌面：Nontoken artifacts you control are lands in addition to their other types. (They don't gain the ability to {T} for mana.)
At the beginning of your end step, earthbend 2. (Target land you control becomes a 0/0 creature with haste that's still a land. Put two +1/+1 counters on it. When it dies or is exiled, return it to the battlefield tapped.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ba Sing Se（｜Land） — This land enters tapped unless you control a basic land. {T}: Add {G}. {2}{G}, {T}: Earthbend 2. Activate only as a sorcery. (Target land you control becomes a 0/0 creatu
  2. Bumi, Unleashed（{3}{R}{G}｜Legendary Creature — Human Noble Ally） — Trample When Bumi enters, earthbend 4. Whenever Bumi deals combat damage to a player, untap all lands you control. After this phase, there is an additional combat phase. 
  3. Toph, Hardheaded Teacher（{2}{R}{G}｜Legendary Creature — Human Warrior Ally） — When Toph enters, you may discard a card. If you do, return target instant or sorcery card from your graveyard to your hand. Whenever you cast a spell, earthbend 1. If th
  4. Earthbender Ascension（{2}{G}｜Enchantment） — When this enchantment enters, earthbend 2. Then search your library for a basic land card, put it onto the battlefield tapped, then shuffle. Landfall — Whenever a land yo
  5. Ichor Wellspring（{2}｜Artifact） — When this artifact enters or is put into a graveyard from the battlefield, draw a card.
  6. Toph, the Blind Bandit（{2}{G}｜Legendary Creature — Human Warrior Ally） — When Toph enters, earthbend 2. (Target land you control becomes a 0/0 creature with haste that's still a land. Put two +1/+1 counters on it. When it dies or is exiled, re
- **出场率最高的牌**（大多数牌组都会放）
  - Tannuk, Memorial Ensign（{1}{R}{G}｜Legendary Creature — Kavu Pilot） — Landfall — Whenever a land you control enters, Tannuk deals 1 damage to each opponent. If this is the second time this ability has
  - Zuran Orb（{0}｜Artifact） — Sacrifice a land: You gain 2 life.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Toph, Earthbending Master（{3}{G}｜Legendary Creature — Human Warrior Ally） — Landfall — Whenever a land you control enters, you get an experience counter. Whenever you attack, earthbend X, where X is the num


## Jodah, the Unifier ｜ 诸界一统裘达
- 颜色 WUBRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Wizard
- 流行度：EDHREC 全时段第 17 位，约 33603 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.94 ｜ 上手难度 4/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $3.24
- 社区标签：传奇、史迹、倾曳、快攻、＋1/＋1 指示物、优质单卡堆
- 完整牌面：Legendary creatures you control get +X/+X, where X is the number of legendary creatures you control.
Whenever you cast a legendary spell from your hand, exile cards from the top of your library until you exile a legendary nonland card with lesser mana value. You may cast that card without paying its mana cost. Put the rest on the bottom of your library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Urza's Ruinous Blast（{4}{W}｜Legendary Sorcery） — (You may cast a legendary sorcery only if you control a legendary creature or planeswalker.) Exile all nonland permanents that aren't legendary.
  2. Sisay, Weatherlight Captain（{2}{W}｜Legendary Creature — Human Soldier） — Sisay gets +1/+1 for each color among other legendary permanents you control. {W}{U}{B}{R}{G}: Search your library for a legendary permanent card with mana value less tha
  3. Relic of Legends（{3}｜Artifact） — {T}: Add one mana of any color. Tap an untapped legendary creature you control: Add one mana of any color.
  4. Primevals' Glorious Rebirth（{5}{W}{B}｜Legendary Sorcery） — (You may cast a legendary sorcery only if you control a legendary creature or planeswalker.) Return all legendary permanent cards from your graveyard to the battlefield.
  5. Annie Joins Up（{1}{R}{G}{W}｜Legendary Enchantment） — When Annie Joins Up enters, it deals 5 damage to target creature or planeswalker an opponent controls. If a triggered ability of a legendary creature you control triggers
  6. Shanid, Sleepers' Scourge（{1}{R}{W}{B}｜Legendary Creature — Human Knight） — Menace Other legendary creatures you control have menace. Whenever you play a legendary land or cast a legendary spell, you draw a card and you lose 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Plaza of Heroes（｜Land） — {T}: Add {C}. {T}: Add one mana of any color. Spend this mana only to cast a legendary spell. {T}: Add one mana of any color among
  - Heroes' Podium（{5}｜Legendary Artifact） — Each legendary creature you control gets +1/+1 for each other legendary creature you control. {X}, {T}: Look at the top X cards of
  - Jhoira, Weatherlight Captain（{2}{U}{R}｜Legendary Creature — Human Artificer） — Whenever you cast a historic spell, draw a card. (Artifacts, legendaries, and Sagas are historic.)
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t


## Nekusar, the Mindrazer ｜ 毁灵师奈库萨
- 颜色 UBR ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Zombie Wizard
- 流行度：EDHREC 全时段第 18 位，约 32428 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.24 ｜ 上手难度 2/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $3.79
- 社区标签：换手牌、群体折磨、烧血、抽牌、弃牌、群体恩惠
- 完整牌面：At the beginning of each player's draw step, that player draws an additional card.
Whenever an opponent draws a card, Nekusar deals 1 damage to that player.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Underworld Dreams（{B}{B}{B}｜Enchantment） — Whenever an opponent draws a card, this enchantment deals 1 damage to that player.
  2. Fate Unraveler（{3}{B}｜Enchantment Creature — Hag） — Whenever an opponent draws a card, this creature deals 1 damage to that player.
  3. Razorkin Needlehead（{R}{R}｜Creature — Human Assassin） — This creature has first strike during your turn. Whenever an opponent draws a card, this creature deals 1 damage to them.
  4. Howling Mine（{2}｜Artifact） — At the beginning of each player's draw step, if this artifact is untapped, that player draws an additional card.
  5. Scrawling Crawler（{3}｜Artifact Creature — Phyrexian Construct） — At the beginning of your upkeep, each player draws a card. Whenever an opponent draws a card, that player loses 1 life.
  6. Windfall（{2}{U}｜Sorcery） — Each player discards their hand, then draws cards equal to the greatest number of cards a player discarded this way.
- **出场率最高的牌**（大多数牌组都会放）
  - Magus of the Wheel（{2}{R}｜Creature — Human Wizard） — {1}{R}, {T}, Sacrifice this creature: Each player discards their hand, then draws seven cards.
  - Jace's Archivist（{1}{U}{U}｜Creature — Vedalken Wizard） — {U}, {T}: Each player discards their hand, then draws cards equal to the greatest number of cards a player discarded this way.
  - Teferi's Puzzle Box（{4}｜Artifact） — At the beginning of each player's draw step, that player puts the cards in their hand on the bottom of their library in any order,
  - Spiteful Visions（{2}{B/R}{B/R}｜Enchantment） — At the beginning of each player's draw step, that player draws an additional card. Whenever a player draws a card, this enchantmen


## Cloud, Ex-SOLDIER ｜ 前神罗战士克劳德
- 颜色 WRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Soldier Mercenary
- 流行度：EDHREC 全时段第 19 位，约 32256 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.7 ｜ 上手难度 3/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $1.45
- 社区标签：装备、主将单挑、神器、已改造生物、快攻、额外战斗
- 完整牌面：Haste
When Cloud enters, attach up to one target Equipment you control to it.
Whenever Cloud attacks, draw a card for each equipped attacking creature you control. Then if Cloud has power 7 or greater, create two Treasure tokens.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Puresteel Paladin（{W}{W}｜Creature — Human Knight） — Whenever an Equipment you control enters, you may draw a card. Metalcraft — Equipment you control have equip {0} as long as you control three or more artifacts.
  2. Colossus Hammer（{1}｜Artifact — Equipment） — Equipped creature gets +10/+10 and loses flying. Equip {8} ({8}: Attach to target creature you control. Equip only as a sorcery.)
  3. Conqueror's Flail（{2}｜Artifact — Equipment） — Equipped creature gets +1/+1 for each color among permanents you control. As long as this Equipment is attached to a creature, your opponents can't cast spells during you
  4. Red XIII, Proud Warrior（{1}{R}{G}｜Legendary Creature — Beast Warrior） — Vigilance, trample Other modified creatures you control have vigilance and trample. (Equipment, Auras you control, and counters are modifications.) Cosmo Memory — When Re
  5. Tifa, Martial Artist（{1}{R}{G}{W}｜Legendary Creature — Human Monk） — Melee (Whenever this creature attacks, it gets +1/+1 until end of turn for each opponent you attacked this combat.) Whenever one or more creatures you control with power 
  6. Sword of the Animist（{2}｜Legendary Artifact — Equipment） — Equipped creature gets +1/+1. Whenever equipped creature attacks, you may search your library for a basic land card, put it onto the battlefield tapped, then shuffle. Equ
- **出场率最高的牌**（大多数牌组都会放）
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Sunpetal Grove（｜Land） — This land enters tapped unless you control a Forest or a Plains. {T}: Add {G} or {W}.
  - Cid, Freeflier Pilot（{1}{W}｜Legendary Creature — Human Warrior Pilot） — Equipment and Vehicle spells you cast cost {1} less to cast. Jump — During your turn, Cid has flying. {2}, {T}: Return target Equi
  - Rootbound Crag（｜Land） — This land enters tapped unless you control a Mountain or a Forest. {T}: Add {R} or {G}.


## Hearthhull, the Worldseed ｜ 播世之种芯炉号
- 颜色 BRG ｜ 法术力值 4.0 ｜ 类型 Legendary Artifact — Spacecraft
- 流行度：EDHREC 全时段第 20 位，约 32159 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.46 ｜ 上手难度 5/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $1.22
- 社区标签：地牌核心、地落、加速、炸地、牺牲、烧血
- 完整牌面：Station (Tap another creature you control: Put charge counters equal to its power on this Spacecraft. Station only as a sorcery. It's an artifact creature at 8+.)
2+ | {1}, {T}, Sacrifice a land: Draw two cards. You may play an additional land this turn.
8+ | Flying, vigilance, haste
Whenever you sacrifice a land, each opponent loses 2 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. The Gitrog Monster（{3}{B}{G}｜Legendary Creature — Frog Horror） — Deathtouch At the beginning of your upkeep, sacrifice The Gitrog Monster unless you sacrifice a land. You may play an additional land on each of your turns. Whenever one 
  2. Splendid Reclamation（{3}{G}｜Sorcery） — Return all land cards from your graveyard to the battlefield tapped.
  3. Aftermath Analyst（{1}{G}｜Creature — Elf Detective） — When this creature enters, mill three cards. (Put the top three cards of your library into your graveyard.) {3}{G}, Sacrifice this creature: Return all land cards from yo
  4. Oracle of Mul Daya（{3}{G}｜Creature — Elf Shaman） — You may play an additional land on each of your turns. Play with the top card of your library revealed. You may play lands from the top of your library.
  5. Horizon Explorer（{2}{G}｜Creature — Insect Scout） — Lands you control enter untapped. Whenever you attack a player, create a Lander token. (It's an artifact with "{2}, {T}, Sacrifice this token: Search your library for a b
  6. Exploration Broodship（{G}｜Artifact — Spacecraft） — Station (Tap another creature you control: Put charge counters equal to its power on this Spacecraft. Station only as a sorcery. It's an artifact creature at 8+.) 3+ | Yo
- **出场率最高的牌**（大多数牌组都会放）
  - Fabled Passage（｜Land） — {T}, Sacrifice this land: Search your library for a basic land card, put it onto the battlefield tapped, then shuffle. Then if you
  - Korvold, Fae-Cursed King（{2}{B}{R}{G}｜Legendary Creature — Dragon Noble） — Flying Whenever Korvold enters or attacks, sacrifice another permanent. Whenever you sacrifice a permanent, put a +1/+1 counter on
  - Harrow（{2}{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for up to two basic land cards, put them onto the 
  - Titania, Protector of Argoth（{3}{G}{G}｜Legendary Creature — Elemental） — When Titania enters, return target land card from your graveyard to the battlefield. Whenever a land you control is put into a gra


## Kefka, Court Mage ｜ 宫廷魔法师凯夫卡
- 颜色 UBR ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Wizard // Legendary Creature — Avatar Wizard
- 流行度：EDHREC 全时段第 21 位，约 31895 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.22 ｜ 上手难度 5/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $6.12
- 社区标签：弃牌、组合技、控制、坟场复活、闪现回场、中速
- 完整牌面：Whenever Kefka enters or attacks, each player discards a card. Then you draw a card for each card type among cards discarded this way.
{8}: Each opponent sacrifices a permanent of their choice. Transform Kefka. Activate only as a sorcery.
//
Flying
Whenever an opponent loses life during your turn, you draw that many cards.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Waste Not（{1}{B}｜Enchantment） — Whenever an opponent discards a creature card, create a 2/2 black Zombie creature token. Whenever an opponent discards a land card, add {B}{B}. Whenever an opponent disca
  2. Harmonic Prodigy（{1}{R}｜Creature — Human Wizard） — Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.) If a triggered ability of a Shaman or another Wizard you control triggers, th
  3. Essence Flux（{U}｜Instant） — Exile target creature you control, then return that card to the battlefield under its owner's control. If it's a Spirit, put a +1/+1 counter on it.
  4. Displacer Kitten（{3}{U}｜Creature — Cat Beast） — Avoidance — Whenever you cast a noncreature spell, exile up to one target nonland permanent you control, then return that card to the battlefield under its owner's contro
  5. Tinybones, Bauble Burglar（{1}{B}｜Legendary Creature — Skeleton Rogue） — Whenever an opponent discards a card, exile it from their graveyard with a stash counter on it. During your turn, you may play cards you don't own with stash counters on 
  6. Reanimate（{B}｜Sorcery） — Put target creature card from a graveyard onto the battlefield under your control. You lose life equal to that card's mana value.
- **出场率最高的牌**（大多数牌组都会放）
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Talisman of Indulgence（{2}｜Artifact） — {T}: Add {C}. {T}: Add {B} or {R}. This artifact deals 1 damage to you.


## Yuriko, the Tiger's Shadow ｜ 虎影百合子
- 颜色 UB ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Ninja
- 流行度：EDHREC 全时段第 22 位，约 31772 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 2.15 ｜ 上手难度 5/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $3.14
- 社区标签：忍术、忍者、节奏、快攻、组合技、烧血
- 完整牌面：Commander ninjutsu {U}{B} ({U}{B}, Return an unblocked attacker you control to hand: Put this card onto the battlefield from your hand or the command zone tapped and attacking.)
Whenever a Ninja you control deals combat damage to a player, reveal the top card of your library and put that card into your hand. Each opponent loses life equal to that card's mana value.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ingenious Infiltrator（{2}{U}{B}｜Creature — Vedalken Ninja） — Ninjutsu {U}{B} ({U}{B}, Return an unblocked attacker you control to hand: Put this card onto the battlefield from your hand tapped and attacking.) Whenever a Ninja you c
  2. Thousand-Faced Shadow（{U}｜Creature — Human Ninja） — Ninjutsu {2}{U}{U} ({2}{U}{U}, Return an unblocked attacker you control to hand: Put this card onto the battlefield from your hand tapped and attacking.) Flying When this
  3. Prosperous Thief（{2}{U}｜Creature — Human Ninja） — Ninjutsu {1}{U} ({1}{U}, Return an unblocked attacker you control to hand: Put this card onto the battlefield from your hand tapped and attacking.) Whenever one or more N
  4. Changeling Outcast（{B}｜Creature — Shapeshifter） — Changeling (This card is every creature type.) This creature can't block and can't be blocked.
  5. Mistblade Shinobi（{2}{U}｜Creature — Human Ninja） — Ninjutsu {U} ({U}, Return an unblocked attacker you control to hand: Put this card onto the battlefield from your hand tapped and attacking.) Whenever this creature deals
  6. Ornithopter（{0}｜Artifact Creature — Thopter） — Flying
- **出场率最高的牌**（大多数牌组都会放）
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  - Silver-Fur Master（{U}{B}｜Creature — Rat Ninja） — Ninjutsu {U}{B} ({U}{B}, Return an unblocked attacker you control to hand: Put this card onto the battlefield from your hand tappe
  - Tetsuko Umezawa, Fugitive（{1}{U}｜Legendary Creature — Human Rogue） — Creatures you control with power or toughness 1 or less can't be blocked.
  - Ninja of the Deep Hours（{3}{U}｜Creature — Human Ninja） — Ninjutsu {1}{U} ({1}{U}, Return an unblocked attacker you control to hand: Put this card onto the battlefield from your hand tappe


## Kenrith, the Returned King ｜ 复归国王肯理斯
- 颜色 WUBRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Noble
- 流行度：EDHREC 全时段第 23 位，约 31707 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.09 ｜ 上手难度 5/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $3.13
- 社区标签：群体恩惠、组合技、坟场复活、政治、＋1/＋1 指示物、传奇
- 完整牌面：{R}: All creatures gain trample and haste until end of turn.
{1}{G}: Put a +1/+1 counter on target creature.
{2}{W}: Target player gains 5 life.
{3}{U}: Target player draws a card.
{4}{B}: Put target creature card from a graveyard onto the battlefield under its owner's control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Training Grounds（{U}｜Enchantment） — Activated abilities of creatures you control cost {2} less to activate. This effect can't reduce the mana in that cost to less than one mana.
  2. Biomancer's Familiar（{G}{U}｜Creature — Mutant） — Activated abilities of creatures you control cost {2} less to activate. This effect can't reduce the mana in that cost to less than one mana. {T}: The next time target cr
  3. Zirda, the Dawnwaker（{1}{R/W}{R/W}｜Legendary Creature — Elemental Fox） — Companion — Each permanent card in your starting deck has an activated ability. (If this card is your chosen companion, you may put it into your hand from outside the gam
  4. Agatha of the Vile Cauldron（{R}{G}｜Legendary Creature — Human Warlock） — Activated abilities of creatures you control cost {X} less to activate, where X is Agatha's power. This effect can't reduce the mana in that cost to less than one mana. {
  5. Seedborn Muse（{3}{G}{G}｜Creature — Spirit） — Untap all permanents you control during each other player's untap step.
  6. Wilderness Reclamation（{3}{G}｜Enchantment） — At the beginning of your end step, untap all lands you control.
- **出场率最高的牌**（大多数牌组都会放）
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Windswept Heath（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Plains card, put it onto the battlefield, then shuffle.
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Flooded Strand（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Plains or Island card, put it onto the battlefield, then shuffle.


## Sephiroth, Fabled SOLDIER ｜ 传奇神罗战士萨菲罗斯
- 颜色 B ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Avatar Soldier // Legendary Creature — Angel Nightmare Avatar
- 流行度：EDHREC 全时段第 24 位，约 31081 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.43 ｜ 上手难度 5/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $28.42
- 社区标签：牺牲流、牺牲、组合技、坟场复活、生命增益、吸取生命
- 完整牌面：Whenever Sephiroth enters or attacks, you may sacrifice another creature. If you do, draw a card.
Whenever another creature dies, target opponent loses 1 life and you gain 1 life. If this is the fourth time this ability has resolved this turn, transform Sephiroth.
//
Flying
Super Nova — As this creature transforms into Sephiroth, One-Winged Angel, you get an emblem with "Whenever a creature dies, target opponent loses 1 life and you gain 1 life."
Whenever Sephiroth attacks, you may sacrifice any number of other creatures. If you do, draw that many cards.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Forsaken Miner（{B}｜Creature — Skeleton Rogue） — This creature can't block. Whenever you commit a crime, you may pay {B}. If you do, return this card from your graveyard to the battlefield. (Targeting opponents, anythin
  2. Ophiomancer（{2}{B}｜Creature — Human Shaman） — At the beginning of each upkeep, if you control no Snakes, create a 1/1 black Snake creature token with deathtouch.
  3. Accursed Marauder（{1}{B}｜Creature — Zombie Warrior） — When this creature enters, each player sacrifices a nontoken creature of their choice.
  4. The Masamune（{3}｜Legendary Artifact — Equipment） — As long as equipped creature is attacking, it has first strike and must be blocked if able. Equipped creature has "If a creature dying causes a triggered ability of this 
  5. Warren Soultrader（{2}{B}｜Creature — Zombie Goblin Wizard） — Pay 1 life, Sacrifice another creature: Create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")
  6. Pitiless Plunderer（{3}{B}｜Creature — Human Pirate） — Whenever another creature you control dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")
- **出场率最高的牌**（大多数牌组都会放）
  - Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Zulaport Cutthroat（{1}{B}｜Creature — Human Rogue Ally） — Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life.


## Isshin, Two Heavens as One ｜ 二天一流一心
- 颜色 WBR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Samurai
- 流行度：EDHREC 全时段第 25 位，约 30831 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.65 ｜ 上手难度 1/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $3.68
- 社区标签：快攻、衍生物、攻击触发、额外战斗、装备、武士
- 完整牌面：If a creature attacking causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Krenko, Tin Street Kingpin（{2}{R}｜Legendary Creature — Goblin） — Whenever Krenko attacks, put a +1/+1 counter on it, then create a number of 1/1 red Goblin creature tokens equal to Krenko's power.
  2. Sword of the Animist（{2}｜Legendary Artifact — Equipment） — Equipped creature gets +1/+1. Whenever equipped creature attacks, you may search your library for a basic land card, put it onto the battlefield tapped, then shuffle. Equ
  3. Etali, Primal Storm（{4}{R}{R}｜Legendary Creature — Elder Dinosaur） — Whenever Etali attacks, exile the top card of each player's library, then you may cast any number of spells from among those cards without paying their mana costs.
  4. Windcrag Siege（{1}{R}{W}｜Enchantment） — As this enchantment enters, choose Mardu or Jeskai. • Mardu — If a creature attacking causes a triggered ability of a permanent you control to trigger, that ability trigg
  5. Adeline, Resplendent Cathar（{1}{W}{W}｜Legendary Creature — Human Knight） — Vigilance Adeline's power is equal to the number of creatures you control. Whenever you attack, for each opponent, create a 1/1 white Human creature token that's tapped a
  6. Fervent Charge（{1}{R}{W}{B}｜Enchantment） — Whenever a creature you control attacks, it gets +2/+2 until end of turn.
- **出场率最高的牌**（大多数牌组都会放）
  - Nomad Outpost（｜Land） — This land enters tapped. {T}: Add {R}, {W}, or {B}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Anim Pakal, Thousandth Moon（{1}{R}{W}｜Legendary Creature — Human Soldier） — Whenever you attack with one or more non-Gnome creatures, put a +1/+1 counter on Anim Pakal, then create X 1/1 colorless Gnome art


## Baylen, the Haymaker ｜ 干草堆匠拜棱
- 颜色 WRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Rabbit Warrior
- 流行度：EDHREC 全时段第 26 位，约 29838 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.92 ｜ 上手难度 1/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $1.11
- 社区标签：衍生物、＋1/＋1 指示物、兔、组合技、快攻、增殖衍生物
- 完整牌面：Tap two untapped tokens you control: Add one mana of any color.
Tap three untapped tokens you control: Draw a card.
Tap four untapped tokens you control: Put three +1/+1 counters on Baylen. It gains trample until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  2. Second Harvest（{2}{G}{G}｜Instant） — For each token you control, create a token that's a copy of that permanent.
  3. Jacked Rabbit（{X}{1}{W}｜Creature — Rabbit Warrior） — Ravenous (This creature enters with X +1/+1 counters on it. If X is 5 or more, draw a card when it enters.) Whenever this creature attacks, create a number of 1/1 white R
  4. Finneas, Ace Archer（{G}{W}｜Legendary Creature — Rabbit Archer） — Reach, vigilance Whenever Finneas attacks, put a +1/+1 counter on each other creature you control that's a token or a Rabbit. Then if creatures you control have total pow
  5. Farmer Cotton（{X}{G}{W}｜Legendary Creature — Halfling Peasant） — When this creature enters, create X 1/1 white Halfling creature tokens and X Food tokens. (They're artifacts with "{2}, {T}, Sacrifice this token: You gain 3 life.")
  6. Halo Fountain（{2}{W}｜Artifact） — {W}, {T}, Untap a tapped creature you control: Create a 1/1 green and white Citizen creature token. {W}{W}, {T}, Untap two tapped creatures you control: Draw a card. {W}{
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Sacred Foundry（｜Land — Mountain Plains） — ({T}: Add {R} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Valgavoth, Harrower of Souls ｜ 搅魂魔瓦伽沃
- 颜色 BR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Elder Demon
- 流行度：EDHREC 全时段第 27 位，约 29831 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.76 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $23.89
- 社区标签：群体折磨、烧血、＋1/＋1 指示物、快攻、吸取生命、点伤
- 完整牌面：Flying
Ward—Pay 2 life.
Whenever an opponent loses life for the first time during each of their turns, put a +1/+1 counter on Valgavoth and draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Kederekt Parasite（{B}｜Creature — Horror） — Whenever an opponent draws a card, if you control a red permanent, you may have this creature deal 1 damage to that player.
  2. Mogis, God of Slaughter（{2}{B}{R}｜Legendary Enchantment Creature — God） — Indestructible As long as your devotion to black and red is less than seven, Mogis isn't a creature. At the beginning of each opponent's upkeep, Mogis deals 2 damage to t
  3. Fate Unraveler（{3}{B}｜Enchantment Creature — Hag） — Whenever an opponent draws a card, this creature deals 1 damage to that player.
  4. Blood Seeker（{1}{B}｜Creature — Vampire Shaman） — Whenever a creature an opponent controls enters, you may have that player lose 1 life.
  5. Razorkin Needlehead（{R}{R}｜Creature — Human Assassin） — This creature has first strike during your turn. Whenever an opponent draws a card, this creature deals 1 damage to them.
  6. Gleeful Arsonist（{2}{R}｜Creature — Human Wizard） — Whenever an opponent casts a noncreature spell, this creature deals damage equal to its power to that player. Undying (When this creature dies, if it had no +1/+1 counter
- **出场率最高的牌**（大多数牌组都会放）
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.
  - Rakdos Charm（{B}{R}｜Instant） — Choose one — • Exile target player's graveyard. • Destroy target artifact. • Each creature deals 1 damage to its controller.
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.


## Miirym, Sentinel Wyrm ｜ 上古龙卫米瑞穆
- 颜色 URG ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Dragon Spirit
- 流行度：EDHREC 全时段第 28 位，约 28681 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.78 ｜ 上手难度 1/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $5.94
- 社区标签：龙、复制、衍生物、飞行、加速、快攻
- 完整牌面：Flying, ward {2}
Whenever another nontoken Dragon you control enters, create a token that's a copy of it, except the token isn't legendary.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ganax, Astral Hunter（{4}{R}｜Legendary Creature — Dragon） — Flying Whenever Ganax or another Dragon you control enters, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.") Choos
  2. Dragon Tempest（{1}{R}｜Enchantment） — Whenever a creature you control with flying enters, it gains haste until end of turn. Whenever a Dragon you control enters, it deals X damage to any target, where X is th
  3. Dragonspeaker Shaman（{1}{R}{R}｜Creature — Human Barbarian Shaman） — Dragon spells you cast cost {2} less to cast.
  4. Lathliss, Dragon Queen（{4}{R}{R}｜Legendary Creature — Dragon） — Flying Whenever another nontoken Dragon you control enters, create a 5/5 red Dragon creature token with flying. {1}{R}: Dragons you control get +1/+0 until end of turn.
  5. Atarka, World Render（{5}{R}{G}｜Legendary Creature — Dragon） — Flying, trample Whenever a Dragon you control attacks, it gains double strike until end of turn.
  6. Scourge of Valkas（{2}{R}{R}{R}｜Creature — Dragon） — Flying Whenever this creature or another Dragon you control enters, it deals X damage to any target, where X is the number of Dragons you control. {R}: This creature gets
- **出场率最高的牌**（大多数牌组都会放）
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Temur Ascendancy（{G}{U}{R}｜Enchantment） — Creatures you control have haste. Whenever a creature you control with power 4 or greater enters, you may draw a card.
  - Haven of the Spirit Dragon（｜Land） — {T}: Add {C}. {T}: Add one mana of any color. Spend this mana only to cast a Dragon creature spell. {2}, {T}, Sacrifice this land:
  - Dragonlord's Servant（{1}{R}｜Creature — Goblin Shaman） — Dragon spells you cast cost {1} less to cast.


## Chatterfang, Squirrel General ｜ 松鼠将军聒牙
- 颜色 BG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Squirrel Warrior
- 流行度：EDHREC 全时段第 29 位，约 27873 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.96 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $10.81
- 社区标签：衍生物、牺牲流、松鼠、组合技、牺牲、宝物
- 完整牌面：Forestwalk (This creature can't be blocked as long as defending player controls a Forest.)
If one or more tokens would be created under your control, those tokens plus that many 1/1 green Squirrel creature tokens are created instead.
{B}, Sacrifice X Squirrels: Target creature gets +X/-X until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Chitterspitter（{2}{G}｜Artifact） — At the beginning of your upkeep, you may sacrifice a token. If you do, put an acorn counter on this artifact. Squirrels you control get +1/+1 for each acorn counter on th
  2. Hazel of the Rootbloom（{2}{B}{G}｜Legendary Creature — Squirrel Druid） — {T}, Pay 2 life, Tap X untapped tokens you control: Add X mana in any combination of colors. At the beginning of your end step, create a token that's a copy of target tok
  3. Toski, Bearer of Secrets（{3}{G}｜Legendary Creature — Squirrel） — This spell can't be countered. Indestructible Toski attacks each combat if able. Whenever a creature you control deals combat damage to a player, draw a card.
  4. Swarmyard（｜Land） — {T}: Add {C}. {T}: Regenerate target Insect, Rat, Spider, or Squirrel. (The next time it would be destroyed this turn, instead tap it, remove it from combat, and heal all
  5. Deep Forest Hermit（{3}{G}{G}｜Creature — Elf Druid） — Vanishing 3 (This creature enters with three time counters on it. At the beginning of your upkeep, remove a time counter from it. When the last is removed, sacrifice it.)
  6. Squirrel Nest（{1}{G}{G}｜Enchantment — Aura） — Enchant land Enchanted land has "{T}: Create a 1/1 green Squirrel creature token."
- **出场率最高的牌**（大多数牌组都会放）
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Zulaport Cutthroat（{1}{B}｜Creature — Human Rogue Ally） — Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life.
  - Pitiless Plunderer（{3}{B}｜Creature — Human Pirate） — Whenever another creature you control dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one ma


## Ulalek, Fused Atrocity ｜ 残暴合体钨拉雷
- 颜色 WUBRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Eldrazi
- 流行度：EDHREC 全时段第 30 位，约 27805 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.32 ｜ 上手难度 4/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.78
- 社区标签：奥札奇、无色、加速、衍生物、歼灭、爆费
- 完整牌面：Devoid (This card has no color.)
Whenever you cast an Eldrazi spell, you may pay {C}{C}. If you do, copy all spells you control, then copy all other activated and triggered abilities you control. You may choose new targets for the copies. (Mana abilities can't be copied.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Eldrazi Temple（｜Land） — {T}: Add {C}. {T}: Add {C}{C}. Spend this mana only to cast colorless Eldrazi spells or activate abilities of colorless Eldrazi.
  2. Glaring Fleshraker（{2}{C}｜Creature — Eldrazi Drone） — Whenever you cast a colorless spell, create a 0/1 colorless Eldrazi Spawn creature token with "Sacrifice this token: Add {C}." Whenever another colorless creature you con
  3. Forsaken Monument（{5}｜Legendary Artifact） — Colorless creatures you control get +2/+2. Whenever you tap a permanent for {C}, add an additional {C}. Whenever you cast a colorless spell, you gain 2 life.
  4. All Is Dust（{7}｜Kindred Sorcery — Eldrazi） — Each player sacrifices all permanents they control that are one or more colors.
  5. Echoes of Eternity（{3}{C}{C}{C}｜Kindred Enchantment — Eldrazi） — If a triggered ability of a colorless spell you control or another colorless permanent you control triggers, that ability triggers an additional time. Whenever you cast a
  6. Shrine of the Forsaken Gods（｜Land） — {T}: Add {C}. {T}: Add {C}{C}. Spend this mana only to cast colorless spells. Activate only if you control seven or more lands.
- **出场率最高的牌**（大多数牌组都会放）
  - Eldritch Immunity（{C}｜Kindred Instant — Eldrazi） — Target creature you control gains protection from each color until end of turn. Overload {4}{C} (You may cast this spell for its o
  - Ugin, the Ineffable（{6}｜Legendary Planeswalker — Ugin） — Colorless spells you cast cost {2} less to cast. +1: Exile the top card of your library face down and look at it. Create a 2/2 col
  - Sire of Stagnation（{4}{U}{B}｜Creature — Eldrazi） — Devoid (This card has no color.) Whenever a land an opponent controls enters, that player exiles the top two cards of their librar
  - Yavimaya Coast（｜Land） — {T}: Add {C}. {T}: Add {G} or {U}. This land deals 1 damage to you.


## Hashaton, Scarab's Fist ｜ 甲虫神之拳哈夏顿
- 颜色 WUB ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Zombie Wizard
- 流行度：EDHREC 全时段第 31 位，约 27372 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.67 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.90
- 社区标签：弃牌、坟场复活、衍生物、僵尸、组合技、换手牌
- 完整牌面：Whenever you discard a creature card, you may pay {2}{U}. If you do, create a tapped token that's a copy of that card, except it's a 4/4 black Zombie.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Tortured Existence（{B}｜Enchantment） — {B}, Discard a creature card: Return target creature card from your graveyard to your hand.
  2. Ghostly Pilferer（{1}{U}｜Creature — Spirit Rogue） — Whenever this creature becomes untapped, you may pay {2}. If you do, draw a card. Whenever an opponent casts a spell from anywhere other than their hand, draw a card. Dis
  3. Psychic Frog（{U}{B}｜Creature — Frog） — Whenever this creature deals combat damage to a player or planeswalker, draw a card. Discard a card: Put a +1/+1 counter on this creature. Exile three cards from your gra
  4. Archfiend of Ifnir（{3}{B}{B}｜Creature — Demon） — Flying Whenever you cycle or discard another card, put a -1/-1 counter on each creature your opponents control. Cycling {2} ({2}, Discard this card: Draw a card.)
  5. Likeness Looter（{U}{B}｜Creature — Faerie Shapeshifter） — Flying {T}: Draw a card, then discard a card. {X}: This creature becomes a copy of target creature card in your graveyard with mana value X, except it has flying and this
  6. Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.
  - Reanimate（{B}｜Sorcery） — Put target creature card from a graveyard onto the battlefield under your control. You lose life equal to that card's mana value.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Frodo, Adventurous Hobbit // Sam, Loyal Attendant ｜ 雄心霍比特人弗罗多
- 颜色 WB ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Halfling Scout
- 流行度：EDHREC 全时段第 32 位，约 27341 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.42 ｜ 上手难度 2/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.33
- 社区标签：生命增益、衍生物、食品、哈比人、组合技、神器
- 完整牌面：Partner with Sam, Loyal Attendant
Vigilance
Whenever Frodo attacks, if you gained 3 or more life this turn, the Ring tempts you. Then if Frodo is your Ring-bearer and the Ring has tempted you two or more times this game, draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Peregrin Took（{2}{G}｜Legendary Creature — Halfling Citizen） — If one or more tokens would be created under your control, those tokens plus an additional Food token are created instead. (It's an artifact with "{2}, {T}, Sacrifice thi
  2. Gilded Goose（{G}｜Creature — Bird） — Flying When this creature enters, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.") {1}{G}, {T}: Create a Food token. {T}, S
  3. Farmer Cotton（{X}{G}{W}｜Legendary Creature — Halfling Peasant） — When this creature enters, create X 1/1 white Halfling creature tokens and X Food tokens. (They're artifacts with "{2}, {T}, Sacrifice this token: You gain 3 life.")
  4. Mirkwood Bats（{3}{B}｜Creature — Bat） — Flying Whenever you create or sacrifice a token, each opponent loses 1 life.
  5. The Gaffer（{2}{W}｜Legendary Creature — Halfling Peasant） — At the beginning of each end step, if you gained 3 or more life this turn, draw a card.
  6. Pippin, Warden of Isengard（{B}{G}｜Legendary Creature — Halfling Advisor） — Partner with Merry, Warden of Isengard (When this creature enters, target player may put Merry into their hand from their library, then shuffle.) {1}, {T}: Create a Food 
- **出场率最高的牌**（大多数牌组都会放）
  - Rosie Cotton of South Lane（{2}{W}｜Legendary Creature — Halfling Peasant） — When Rosie Cotton enters, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.") Whenever
  - Tireless Provisioner（{2}{G}｜Creature — Elf Scout） — Landfall — Whenever a land you control enters, create a Food token or a Treasure token. (Food is an artifact with "{2}, {T}, Sacri
  - Samwise Gamgee（{G}{W}｜Legendary Creature — Halfling Peasant） — Whenever another nontoken creature you control enters, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.


## Ashling, the Limitless ｜ 瀚力无边灰儿
- 颜色 WUBRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elemental Sorcerer
- 流行度：EDHREC 全时段第 33 位，约 26927 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 5/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.39
- 社区标签：元素、衍生物、呼引、进场触发、组合技、中速
- 完整牌面：Elemental permanent spells you cast from your hand gain evoke {4} as you cast them. (If you cast a spell for its evoke cost, it's sacrificed when it enters.)
Whenever you sacrifice a nontoken Elemental, create a token that's a copy of it. The token gains haste until end of turn. At the beginning of your next end step, sacrifice it unless you pay {W}{U}{B}{R}{G}.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Risen Reef（{1}{G}{U}｜Creature — Elemental） — Whenever this creature or another Elemental you control enters, look at the top card of your library. If it's a land card, you may put it onto the battlefield tapped. If 
  2. Mulldrifter（{4}{U}｜Creature — Elemental） — Flying When this creature enters, draw two cards. Evoke {2}{U} (You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters.)
  3. Maelstrom Wanderer（{5}{G}{U}{R}｜Legendary Creature — Elemental） — Creatures you control have haste. Cascade, cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You
  4. Greenwarden of Murasa（{4}{G}{G}｜Creature — Elemental） — When this creature enters, you may return target card from your graveyard to your hand. When this creature dies, you may exile it. If you do, return target card from your
  5. Titan of Industry（{4}{G}{G}{G}｜Creature — Elemental） — Reach, trample When this creature enters, choose two — • Destroy target artifact or enchantment. • Target player gains 5 life. • Create a 4/4 green Rhino Warrior creature
  6. Yarok, the Desecrated（{2}{B}{G}{U}｜Legendary Creature — Elemental Horror） — Deathtouch, lifelink If a permanent entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
- **出场率最高的牌**（大多数牌组都会放）
  - Flamebraider（{1}{R}｜Creature — Elemental Bard） — {T}: Add two mana in any combination of colors. Spend this mana only to cast Elemental spells or activate abilities of Elemental s
  - Smokebraider（{1}{R}｜Creature — Elemental Shaman） — {T}: Add two mana in any combination of colors. Spend this mana only to cast Elemental spells or activate abilities of Elementals.
  - Lamentation（{5}{B}｜Creature — Elemental Incarnation） — When this creature enters, destroy target creature an opponent controls. You gain 3 life. Encore {6}{B}{B} ({6}{B}{B}, Exile this 
  - Omnath, Locus of Rage（{3}{R}{R}{G}{G}｜Legendary Creature — Elemental） — Landfall — Whenever a land you control enters, create a 5/5 red and green Elemental creature token. Whenever Omnath or another Ele


## Bello, Bard of the Brambles ｜ 刺棘诗人贝洛
- 颜色 RG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Raccoon Bard
- 流行度：EDHREC 全时段第 34 位，约 26276 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.6 ｜ 上手难度 2/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $2.58
- 社区标签：结界流、神器、非自然、快攻、载具、加速
- 完整牌面：During your turn, each non-Equipment artifact and non-Aura enchantment you control with mana value 4 or greater is a 4/4 Elemental creature in addition to its other types and has indestructible, haste, and "Whenever this creature deals combat damage to a player, draw a card."
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Berserkers' Onslaught（{3}{R}{R}｜Enchantment） — Attacking creatures you control have double strike.
  2. Gratuitous Violence（{2}{R}{R}{R}｜Enchantment） — If a creature you control would deal damage to a permanent or player, it deals double that damage instead.
  3. Sunbird's Invocation（{5}{R}｜Enchantment） — Whenever you cast a spell from your hand, reveal the top X cards of your library, where X is that spell's mana value. You may cast a spell with mana value X or less from 
  4. Unnatural Growth（{1}{G}{G}{G}{G}｜Enchantment） — At the beginning of each combat, double the power and toughness of each creature you control until end of turn.
  5. Thran Dynamo（{4}｜Artifact） — {T}: Add {C}{C}{C}.
  6. Warstorm Surge（{5}{R}｜Enchantment） — Whenever a creature you control enters, it deals damage equal to its power to any target.
- **出场率最高的牌**（大多数牌组都会放）
  - Rootbound Crag（｜Land） — This land enters tapped unless you control a Mountain or a Forest. {T}: Add {R} or {G}.
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 


## Esika, God of the Tree ｜ 世界树神埃西卡
- 颜色 WUBRG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — God // Legendary Enchantment
- 流行度：EDHREC 全时段第 35 位，约 26243 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.15 ｜ 上手难度 5/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $21.60
- 社区标签：鹏洛客、传奇、神、史迹、虔诚、结界流
- 完整牌面：Vigilance
{T}: Add one mana of any color.
Other legendary creatures you control have vigilance and "{T}: Add one mana of any color."
//
At the beginning of your upkeep, reveal cards from the top of your library until you reveal a creature or planeswalker card. Put that card onto the battlefield and the rest on the bottom of your library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Nicol Bolas, Dragon-God（{U}{B}{B}{B}{R}｜Legendary Planeswalker — Bolas） — Nicol Bolas has all loyalty abilities of all other planeswalkers on the battlefield. +1: You draw a card. Each opponent exiles a card from their hand or a permanent they 
  2. The World Tree（｜Land） — This land enters tapped. {T}: Add {G}. As long as you control six or more lands, lands you control have "{T}: Add one mana of any color." {W}{W}{U}{U}{B}{B}{R}{R}{G}{G}, 
  3. Nicol Bolas, God-Pharaoh（{4}{U}{B}{R}｜Legendary Planeswalker — Bolas） — +2: Target opponent exiles cards from the top of their library until they exile a nonland card. Until end of turn, you may cast that card without paying its mana cost. +1
  4. Oath of Teferi（{3}{W}{U}｜Legendary Enchantment） — When Oath of Teferi enters, exile another target permanent you control. Return it to the battlefield under its owner's control at the beginning of the next end step. You 
  5. Vorinclex, Monstrous Raider（{4}{G}{G}｜Legendary Creature — Phyrexian Praetor） — Trample, haste If you would put one or more counters on a permanent or player, put twice that many of each of those kinds of counters on that permanent or player instead.
  6. Primevals' Glorious Rebirth（{5}{W}{B}｜Legendary Sorcery） — (You may cast a legendary sorcery only if you control a legendary creature or planeswalker.) Return all legendary permanent cards from your graveyard to the battlefield.
- **出场率最高的牌**（大多数牌组都会放）
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Hakbal of the Surging Soul ｜ 翻涌之魂哈巴尔
- 颜色 UG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Merfolk Scout
- 流行度：EDHREC 全时段第 36 位，约 25418 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.74 ｜ 上手难度 5/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.45
- 社区标签：人鱼、＋1/＋1 指示物、探索、快攻、加速、衍生物
- 完整牌面：At the beginning of combat on your turn, each Merfolk creature you control explores. (Reveal the top card of your library. Put that card into your hand if it's a land. Otherwise, put a +1/+1 counter on the exploring creature, then put the card back or put it into your graveyard.)
Whenever Hakbal attacks, you may put a land card from your hand onto the battlefield. If you don't, draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Nicanzil, Current Conductor（{G}{U}｜Legendary Creature — Merfolk Scout） — Whenever a creature you control explores a land card, you may put a land card from your hand onto the battlefield tapped. Whenever a creature you control explores a nonla
  2. Master of the Pearl Trident（{U}{U}｜Creature — Merfolk） — Other Merfolk creatures you control get +1/+1 and have islandwalk. (They can't be blocked as long as defending player controls an Island.)
  3. Svyelun of Sea and Sky（{1}{U}{U}｜Legendary Creature — Merfolk God） — Svyelun has indestructible as long as you control at least two other Merfolk. Whenever Svyelun attacks, draw a card. Other Merfolk you control have ward {1}. (Whenever an
  4. Emperor Mihail II（{1}{U}{U}｜Legendary Creature — Merfolk Noble） — You may look at the top card of your library any time. You may cast Merfolk spells from the top of your library. Whenever you cast a Merfolk spell, you may pay {1}. If yo
  5. Kopala, Warden of Waves（{1}{U}{U}｜Legendary Creature — Merfolk Wizard） — Spells your opponents cast that target a Merfolk you control cost {2} more to cast. Abilities your opponents activate that target a Merfolk you control cost {2} more to a
  6. Stonybrook Banneret（{1}{U}｜Creature — Merfolk Wizard） — Islandwalk (This creature can't be blocked as long as defending player controls an Island.) Merfolk spells and Wizard spells you cast cost {1} less to cast.
- **出场率最高的牌**（大多数牌组都会放）
  - Herald of Secret Streams（{3}{U}｜Creature — Merfolk Warrior） — Creatures you control with +1/+1 counters on them can't be blocked.
  - Merrow Reejerey（{2}{U}｜Creature — Merfolk Soldier） — Other Merfolk creatures you control get +1/+1. Whenever you cast a Merfolk spell, you may tap or untap target permanent.
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Merfolk Sovereign（{1}{U}{U}｜Creature — Merfolk Noble） — Other Merfolk creatures you control get +1/+1. {T}: Target Merfolk creature can't be blocked this turn.


## Muldrotha, the Gravetide ｜ 腐潮穆杜塔
- 颜色 UBG ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Elemental Avatar
- 流行度：EDHREC 全时段第 37 位，约 25364 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.9 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.57
- 社区标签：坟场复活、磨牌、坟场、自磨、牺牲、组合技
- 完整牌面：During each of your turns, you may play a land and cast a permanent spell of each permanent type from your graveyard. (If a card has multiple permanent types, choose one as you play it.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Spore Frog（{G}｜Creature — Frog） — Sacrifice this creature: Prevent all combat damage that would be dealt this turn.
  2. Seal of Primordium（{1}{G}｜Enchantment） — Sacrifice this enchantment: Destroy target artifact or enchantment.
  3. Kaya's Ghostform（{B}｜Enchantment — Aura） — Enchant creature or planeswalker you control When enchanted permanent dies or is put into exile, return that card to the battlefield under your control.
  4. Gravebreaker Lamia（{4}{B}｜Enchantment Creature — Snake Lamia） — Lifelink When this creature enters, search your library for a card, put it into your graveyard, then shuffle. Spells you cast from your graveyard cost {1} less to cast.
  5. Secrets of the Dead（{2}{U}｜Enchantment） — Whenever you cast a spell from your graveyard, draw a card.
  6. Haywire Mite（{1}｜Artifact Creature — Insect） — When this creature dies, you gain 2 life. {G}, Sacrifice this creature: Exile target noncreature artifact or noncreature enchantment.
- **出场率最高的牌**（大多数牌组都会放）
  - Sakura-Tribe Elder（{1}{G}｜Creature — Snake Shaman） — Sacrifice this creature: Search your library for a basic land card, put that card onto the battlefield tapped, then shuffle.
  - Eternal Witness（{1}{G}{G}｜Creature — Human Shaman） — When this creature enters, you may return target card from your graveyard to your hand.
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
