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


## Omnath, Locus of Rage ｜ 怒火核欧那斯
- 颜色 RG ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Elemental
- 流行度：EDHREC 全时段第 298 位，约 8902 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.57 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.33
- 社区标签：地牌核心、地落、加速、衍生物、元素、烧血
- 完整牌面：Landfall — Whenever a land you control enters, create a 5/5 red and green Elemental creature token.
Whenever Omnath or another Elemental you control dies, Omnath deals 3 damage to any target.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ancient Greenwarden（{4}{G}{G}｜Creature — Elemental） — Reach (This creature can block creatures with flying.) You may play lands from your graveyard. If a land entering causes a triggered ability of a permanent you control to
  2. Harrow（{2}{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for up to two basic land cards, put them onto the battlefield, then shuffle.
  3. Mina and Denn, Wildborn（{2}{R}{G}｜Legendary Creature — Elf Ally） — You may play an additional land on each of your turns. {R}{G}, Return a land you control to its owner's hand: Target creature gains trample until end of turn.
  4. Azusa, Lost but Seeking（{2}{G}｜Legendary Creature — Human Monk） — You may play two additional lands on each of your turns.
  5. Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  6. Ramunap Excavator（{2}{G}｜Creature — Snake Cleric） — You may play lands from your graveyard.
- **出场率最高的牌**（大多数牌组都会放）
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.
  - Gruul Turf（｜Land） — This land enters tapped. When this land enters, return a land you control to its owner's hand. {T}: Add {R}{G}.
  - Warstorm Surge（{5}{R}｜Enchantment） — Whenever a creature you control enters, it deals damage equal to its power to any target.


## Elas il-Kor, Sadistic Pilgrim ｜ 虐之华寇族黜人依拉丝
- 颜色 WB ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Phyrexian Kor Cleric
- 流行度：EDHREC 全时段第 304 位，约 8788 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.43 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.81
- 社区标签：牺牲流、生命增益、衍生物、吸取生命、组合技、牺牲
- 完整牌面：Deathtouch
Whenever another creature you control enters, you gain 1 life.
Whenever another creature you control dies, each opponent loses 1 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Zulaport Cutthroat（{1}{B}｜Creature — Human Rogue Ally） — Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life.
  2. Corpse Knight（{W}{B}｜Creature — Zombie Knight） — Whenever another creature you control enters, each opponent loses 1 life.
  3. Cruel Celebrant（{W}{B}｜Creature — Vampire） — Whenever this creature or another creature or planeswalker you control dies, each opponent loses 1 life and you gain 1 life.
  4. Marauding Blight-Priest（{2}{B}｜Creature — Vampire Cleric） — Whenever you gain life, each opponent loses 1 life.
  5. Viscera Seer（{B}｜Creature — Vampire Wizard） — Sacrifice a creature: Scry 1. (Look at the top card of your library. You may put that card on the bottom.)
  6. Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  - Bastion of Remembrance（{2}{B}｜Enchantment） — When this enchantment enters, create a 1/1 white Human Soldier creature token. Whenever a creature you control dies, each opponent


## Obeka, Brute Chronologist ｜ 蛮野时代学者欧蓓卡
- 颜色 UBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Ogre Wizard
- 流行度：EDHREC 全时段第 305 位，约 8773 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.46 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.31
- 社区标签：复制、额外回合、坟场复活、衍生物、组合技、偷取
- 完整牌面：{T}: The player whose turn it is may end the turn. (Exile all spells and abilities from the stack. The player whose turn it is discards down to their maximum hand size. Damage wears off, and "this turn" and "until end of turn" effects end.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sundial of the Infinite（{2}｜Artifact） — {1}, {T}: End the turn. Activate only during your turn. (Exile all spells and abilities from the stack. Discard down to your maximum hand size. Damage wears off, and "thi
  2. Ideas Unbound（{U}{U}｜Sorcery — Arcane） — Draw three cards. Discard three cards at the beginning of the next end step.
  3. Sneak Attack（{3}{R}｜Enchantment） — {R}: You may put a creature card from your hand onto the battlefield. That creature gains haste. Sacrifice the creature at the beginning of the next end step.
  4. Feldon of the Third Path（{1}{R}{R}｜Legendary Creature — Human Artificer） — {2}{R}, {T}: Create a token that's a copy of target creature card in your graveyard, except it's an artifact in addition to its other types. It gains haste. Sacrifice it 
  5. Last Chance（{R}{R}｜Sorcery） — Take an extra turn after this one. At the beginning of that turn's end step, you lose the game.
  6. Glorious End（{2}{R}｜Instant） — End the turn. (Exile all spells and abilities from the stack, including this card. The player whose turn it is discards down to their maximum hand size. Damage wears off,
- **出场率最高的牌**（大多数牌组都会放）
  - Saheeli, the Sun's Brilliance（{U}{R}｜Legendary Creature — Human Artificer） — {U}{R}, {T}: Create a token that's a copy of another target creature or artifact you control, except it's an artifact in addition 
  - Final Fortune（{R}{R}｜Instant） — Take an extra turn after this one. At the beginning of that turn's end step, you lose the game.
  - Nightscape Familiar（{1}{B}｜Creature — Zombie） — Blue spells and red spells you cast cost {1} less to cast. {1}{B}: Regenerate this creature.
  - Flameshadow Conjuring（{3}{R}｜Enchantment） — Whenever a nontoken creature you control enters, you may pay {R}. If you do, create a token that's a copy of that creature. That t


## Adrix and Nev, Twincasters ｜ 双咒法师艾季与涅夫
- 颜色 UG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Merfolk Wizard
- 流行度：EDHREC 全时段第 306 位，约 8768 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.63 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $8.61
- 社区标签：衍生物、复制、＋1/＋1 指示物、加速、组合技、增殖衍生物
- 完整牌面：Ward {2} (Whenever this creature becomes the target of a spell or ability an opponent controls, counter it unless that player pays {2}.)
If one or more tokens would be created under your control, twice that many of those tokens are created instead.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Rite of Replication（{2}{U}{U}｜Sorcery） — Kicker {5} (You may pay an additional {5} as you cast this spell.) Create a token that's a copy of target creature. If this spell was kicked, create five of those tokens 
  2. Esix, Fractal Bloom（{4}{G}{U}｜Legendary Creature — Fractal） — Flying The first time you would create one or more tokens during each of your turns, you may instead choose a creature other than Esix and create that many tokens that ar
  3. Curiosity Crafter（{3}{U}｜Creature — Bird Wizard） — Flying You have no maximum hand size. Whenever a creature token you control deals combat damage to a player, draw a card.
  4. Second Harvest（{2}{G}{G}｜Instant） — For each token you control, create a token that's a copy of that permanent.
  5. Idol of Oblivion（{2}｜Artifact） — {T}: Draw a card. Activate only if you created a token this turn. {8}, {T}, Sacrifice this artifact: Create a 10/10 colorless Eldrazi creature token.
  6. Reef Worm（{3}{U}｜Creature — Worm） — When this creature dies, create a 3/3 blue Fish creature token with "When this token dies, create a 6/6 blue Whale creature token with 'When this token dies, create a 9/9
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Yavimaya Coast（｜Land） — {T}: Add {C}. {T}: Add {G} or {U}. This land deals 1 damage to you.
  - Simic Growth Chamber（｜Land） — This land enters tapped. When this land enters, return a land you control to its owner's hand. {T}: Add {G}{U}.
  - Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create 


## Brimaz, Blight of Oreskos ｜ 俄瑞恣荒王布黎玛
- 颜色 WB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Phyrexian Cat
- 流行度：EDHREC 全时段第 309 位，约 8686 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.47 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.47
- 社区标签：非瑞人、衍生物、毒侵、＋1/＋1 指示物、神器、增殖
- 完整牌面：Whenever you cast a Phyrexian creature or artifact creature spell, incubate X, where X is that spell's mana value. (Create an Incubator token with X +1/+1 counters on it and "{2}: Transform this token." It transforms into a 0/0 Phyrexian artifact creature.)
At the beginning of each end step, if a Phyrexian died under your control this turn, proliferate.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Progenitor Exarch（{X}{X}{W}｜Creature — Phyrexian Cat Cleric） — When this creature enters, incubate 3 X times. (To incubate 3, create an Incubator token with three +1/+1 counters on it and "{2}: Transform this token." It transforms in
  2. Filigree Vector（{3}{W}｜Artifact Creature — Phyrexian Construct） — When this creature enters, put a +1/+1 counter on each of any number of target creatures and a charge counter on each of any number of target artifacts. {1}, {T}, Sacrifi
  3. Karn's Bastion（｜Land） — {T}: Add {C}. {4}, {T}: Proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
  4. Essence of Orthodoxy（{3}{W}{W}｜Creature — Phyrexian） — Flying Whenever this creature or another Phyrexian you control enters, incubate 2. (Create an Incubator token with two +1/+1 counters on it and "{2}: Transform this token
  5. Grafted Butcher（{1}{B}｜Creature — Phyrexian Samurai） — When this creature enters, Phyrexians you control gain menace until end of turn. Other Phyrexians you control get +1/+1. {3}{B}, Sacrifice an artifact or creature: Return
  6. Norn's Inquisitor（{1}{W}｜Creature — Phyrexian Knight） — When this creature enters, incubate 2. (Create an Incubator token with two +1/+1 counters on it and "{2}: Transform this token." It transforms into a 0/0 Phyrexian artifa
- **出场率最高的牌**（大多数牌组都会放）
  - Elesh Norn（｜） — 
  - Phyrexian Censor（{2}{W}｜Creature — Phyrexian Wizard） — Each player can't cast more than one non-Phyrexian spell each turn. Non-Phyrexian creatures enter tapped.
  - Tainted Field（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. Activate only if you control a Swamp.
  - Metastatic Evangel（{1}{W}｜Creature — Phyrexian Human Cleric） — Whenever another nontoken creature you control enters, proliferate. (Choose any number of permanents and/or players, then give eac


## Braids, Arisen Nightmare ｜ 觉醒梦魇布蕾德
- 颜色 B ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Nightmare
- 流行度：EDHREC 全时段第 315 位，约 8448 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.05 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $4.14
- 社区标签：牺牲流、牺牲、坟场复活、控制、组合技、弃牌
- 完整牌面：At the beginning of your end step, you may sacrifice an artifact, creature, enchantment, land, or planeswalker. If you do, each opponent may sacrifice a permanent of their choice that shares a card type with it. For each opponent who doesn't, that player loses 2 life and you draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ichor Wellspring（{2}｜Artifact） — When this artifact enters or is put into a graveyard from the battlefield, draw a card.
  2. Jadar, Ghoulcaller of Nephalia（{1}{B}｜Legendary Creature — Human Wizard） — At the beginning of your end step, if you control no creatures with decayed, create a 2/2 black Zombie creature token with decayed. (It can't block. When it attacks, sacr
  3. Ophiomancer（{2}{B}｜Creature — Human Shaman） — At the beginning of each upkeep, if you control no Snakes, create a 1/1 black Snake creature token with deathtouch.
  4. Reassembling Skeleton（{1}{B}｜Creature — Skeleton Warrior） — {1}{B}: Return this card from your graveyard to the battlefield tapped.
  5. Bloodghast（{B}{B}｜Creature — Vampire Spirit） — This creature can't block. This creature has haste as long as an opponent has 10 or less life. Landfall — Whenever a land you control enters, you may return this card fro
  6. Prized Statue（{2}｜Artifact） — When this artifact enters or is put into a graveyard from the battlefield, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any
- **出场率最高的牌**（大多数牌组都会放）
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost thi
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.


## Strefan, Maurer Progenitor ｜ 茂威原祖史崔凡
- 颜色 BR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Vampire Noble
- 流行度：EDHREC 全时段第 318 位，约 8397 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.06 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.70
- 社区标签：吸血鬼、Blood、衍生物、快攻、神器、生命增益
- 完整牌面：Flying
At the beginning of your end step, create a Blood token for each player who lost life this turn.
Whenever Strefan attacks, you may sacrifice two Blood tokens. If you do, you may put a Vampire card from your hand onto the battlefield tapped and attacking. It gains indestructible until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Crossway Troublemakers（{5}{B}｜Creature — Vampire） — Attacking Vampires you control have deathtouch and lifelink. (Any amount of damage they deal to a creature is enough to destroy it. Damage dealt by those creatures also c
  2. Glass-Cast Heart（{2}{B}｜Artifact） — Whenever one or more Vampires you control attack, create a Blood token. (It's an artifact with "{1}, {T}, Discard a card, Sacrifice this token: Draw a card.") {B}, {T}, P
  3. Markov Enforcer（{4}{R}{R}｜Creature — Vampire Soldier） — Whenever this creature or another Vampire you control enters, this creature fights up to one target creature an opponent controls. Whenever a creature dealt damage by thi
  4. Anje, Maid of Dishonor（{2}{B}{R}｜Legendary Creature — Vampire） — Whenever Anje and/or one or more other Vampires you control enter, create a Blood token. This ability triggers only once each turn. (It's an artifact with "{1}, {T}, Disc
  5. Patron of the Vein（{4}{B}{B}｜Creature — Vampire Shaman） — Flying When this creature enters, destroy target creature an opponent controls. Whenever a creature an opponent controls dies, exile it and put a +1/+1 counter on each Va
  6. Bloodtithe Harvester（{B}{R}｜Creature — Vampire） — When this creature enters, create a Blood token. (It's an artifact with "{1}, {T}, Discard a card, Sacrifice this token: Draw a card.") {T}, Sacrifice this creature: Targ
- **出场率最高的牌**（大多数牌组都会放）
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.
  - Voldaren Estate（｜Land） — {T}: Add {C}. {T}, Pay 1 life: Add one mana of any color. Spend this mana only to cast a Vampire spell. {5}, {T}: Create a Blood t
  - Olivia's Attendants（{4}{R}{R}｜Creature — Vampire） — Menace Whenever this creature deals damage, create that many Blood tokens. (They're artifacts with "{1}, {T}, Discard a card, Sacr
  - Sanctum Seeker（{2}{B}{B}｜Creature — Vampire Knight） — Whenever a Vampire you control attacks, each opponent loses 1 life and you gain 1 life.


## Marwyn, the Nurturer ｜ 培育人玛雯
- 颜色 G ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elf Druid
- 流行度：EDHREC 全时段第 323 位，约 8234 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 0.55 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.76
- 社区标签：妖精、＋1/＋1 指示物、组合技、加速、快攻、衍生物
- 完整牌面：Whenever another Elf you control enters, put a +1/+1 counter on Marwyn.
{T}: Add an amount of {G} equal to Marwyn's power.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Elvish Archdruid（{1}{G}{G}｜Creature — Elf Druid） — Other Elf creatures you control get +1/+1. {T}: Add {G} for each Elf you control.
  2. Priest of Titania（{1}{G}｜Creature — Elf Druid） — {T}: Add {G} for each Elf on the battlefield.
  3. Leaf-Crowned Visionary（{G}{G}｜Creature — Elf Druid） — Other Elves you control get +1/+1. Whenever you cast an Elf spell, you may pay {G}. If you do, draw a card.
  4. Imperious Perfect（{2}{G}｜Creature — Elf Warrior） — Other Elves you control get +1/+1. {G}, {T}: Create a 1/1 green Elf Warrior creature token.
  5. Ezuri, Renegade Leader（{1}{G}{G}｜Legendary Creature — Elf Warrior） — {G}: Regenerate another target Elf. {2}{G}{G}{G}: Elf creatures you control get +3/+3 and gain trample until end of turn.
  6. Elvish Visionary（{1}{G}｜Creature — Elf Shaman） — When this creature enters, draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Beast Whisperer（{2}{G}{G}｜Creature — Elf Druid） — Whenever you cast a creature spell, draw a card.
  - Fyndhorn Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.


## Maelstrom Wanderer ｜ 涡心漫游怪
- 颜色 URG ｜ 法术力值 8.0 ｜ 类型 Legendary Creature — Elemental
- 流行度：EDHREC 全时段第 327 位，约 8133 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.65 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.33
- 社区标签：倾曳、加速、混乱、爆费、组合技、快攻
- 完整牌面：Creatures you control have haste.
Cascade, cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. Put the exiled cards on the bottom in a random order. Then do it again.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Imoti, Celebrant of Bounty（{3}{G}{U}｜Legendary Creature — Snake Druid） — Cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. 
  2. Goreclaw, Terror of Qal Sisma（{3}{G}｜Legendary Creature — Bear） — Creature spells you cast with power 4 or greater cost {2} less to cast. Whenever Goreclaw attacks, each creature you control with power 4 or greater gets +1/+1 and gains 
  3. Etali, Primal Storm（{4}{R}{R}｜Legendary Creature — Elder Dinosaur） — Whenever Etali attacks, exile the top card of each player's library, then you may cast any number of spells from among those cards without paying their mana costs.
  4. Apex Devastator（{8}{G}{G}｜Creature — Chimera Hydra） — Cascade, cascade, cascade, cascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it wit
  5. Genesis Ultimatum（{G}{G}{U}{U}{U}{R}{R}｜Sorcery） — Look at the top five cards of your library. Put any number of permanent cards from among them onto the battlefield and the rest into your hand. Exile Genesis Ultimatum.
  6. Averna, the Chaos Bloom（{G}{U}{R}｜Legendary Creature — Elemental Shaman） — As you cascade, you may put a land card from among the exiled cards onto the battlefield tapped. (Do this after the last card is exiled but before deciding whether to cas
- **出场率最高的牌**（大多数牌组都会放）
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Steam Vents（｜Land — Island Mountain） — ({T}: Add {U} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Skyshroud Claim（{3}{G}｜Sorcery） — Search your library for up to two Forest cards, put them onto the battlefield, then shuffle.


## Imotekh the Stormlord ｜ 风暴领主伊摩特克
- 颜色 B ｜ 法术力值 4.0 ｜ 类型 Legendary Artifact Creature — Necron
- 流行度：EDHREC 全时段第 329 位，约 8107 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.28 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：神器、坟场复活、坟场、衍生物、Necrons、组合技
- 完整牌面：Phaeron — Whenever one or more artifact cards leave your graveyard, create two 2/2 black Necron Warrior artifact creature tokens.
Grand Strategist — At the beginning of combat on your turn, another target artifact creature you control gets +2/+2 and gains menace until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Their Name Is Death（{3}{B}{B}{B}｜Sorcery） — Destroy all nonartifact creatures.
  2. Cryptothrall（{4}｜Artifact Creature — Construct） — Protector — Other artifact creatures you control have hexproof.
  3. Skorpekh Lord（{2}{B}｜Artifact Creature — Necron Noble） — Menace Command Protocols — Other artifact creatures you control get +1/+0 and have menace. Unearth {2}{B} ({2}{B}: Return this card from your graveyard to the battlefield
  4. Vault of Whispers（｜Artifact Land） — {T}: Add {B}.
  5. Scrap Trawler（{3}｜Artifact Creature — Construct） — Whenever this creature dies or another artifact you control is put into a graveyard from the battlefield, return to your hand target artifact card in your graveyard with 
  6. Anrakyr the Traveller（{4}{B}｜Legendary Artifact Creature — Necron） — Lord of the Pyrrhian Legions — Whenever Anrakyr the Traveller attacks, you may cast an artifact spell from your hand or graveyard by paying life equal to its mana value r
- **出场率最高的牌**（大多数牌组都会放）
  - Mystic Forge（{4}｜Artifact） — You may look at the top card of your library any time. You may cast artifact spells and colorless spells from the top of your libr
  - Chronomancer（{1}{B}｜Artifact Creature — Necron Wizard） — Flying Atomic Transmutation — {1}, {T}, Sacrifice another artifact: Draw a card. Unearth {2}{B} ({2}{B}: Return this card from you
  - Necron Deathmark（{3}{B}{B}｜Artifact Creature — Necron） — Flash Synaptic Disintegrator — When this creature enters, destroy up to one target creature and target player mills three cards.
  - Foundry Inspector（{3}｜Artifact Creature — Construct） — Artifact spells you cast cost {1} less to cast.


## Elesh Norn, Mother of Machines ｜ 机械之母艾蕾侬
- 颜色 W ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Phyrexian Praetor
- 流行度：EDHREC 全时段第 331 位，约 8097 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.76 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $25.64
- 社区标签：闪现回场、衍生物、进场触发、锁场、控制、生命增益
- 完整牌面：Vigilance
If a permanent entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
Permanents entering don't cause abilities of permanents your opponents control to trigger.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Panharmonicon（{4}｜Artifact） — If an artifact or creature entering causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
  2. Ephemerate（{W}｜Instant） — Exile target creature you control, then return it to the battlefield under its owner's control. Rebound (If you cast this spell from your hand, exile it as it resolves. A
  3. Teleportation Circle（{3}{W}｜Enchantment） — At the beginning of your end step, exile up to one target artifact or creature you control, then return that card to the battlefield under its owner's control.
  4. Restoration Angel（{3}{W}｜Creature — Angel） — Flash Flying When this creature enters, you may exile target non-Angel creature you control, then return that card to the battlefield under your control.
  5. Spirited Companion（{1}{W}｜Enchantment Creature — Dog） — When this creature enters, draw a card.
  6. Charming Prince（{1}{W}｜Creature — Human Noble） — When this creature enters, choose one — • Scry 2. • You gain 3 life. • Exile another target creature you own. Return it to the battlefield under your control at the begin
- **出场率最高的牌**（大多数牌组都会放）
  - Pearl Medallion（{2}｜Artifact） — White spells you cast cost {1} less to cast.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Solemn Simulacrum（{4}｜Artifact Creature — Golem） — When this creature enters, you may search your library for a basic land card, put that card onto the battlefield tapped, then shuf
  - Suture Priest（{1}{W}｜Creature — Phyrexian Cleric） — Whenever another creature you control enters, you may gain 1 life. Whenever a creature an opponent controls enters, you may have t


## Kellan, the Kid ｜ 凯澜小子
- 颜色 WUG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Faerie Rogue
- 流行度：EDHREC 全时段第 332 位，约 8083 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.69 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.82
- 社区标签：Foretell、放逐、倾曳、Adventures、Plot、加速
- 完整牌面：Flying, lifelink
Whenever you cast a spell from anywhere other than your hand, you may cast a permanent spell with equal or lesser mana value from your hand without paying its mana cost. If you don't, you may put a land card from your hand onto the battlefield.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Vega, the Watcher（{1}{W}{U}｜Legendary Creature — Bird Spirit） — Flying Whenever you cast a spell from anywhere other than your hand, draw a card.
  2. Doc Aurlock, Grizzled Genius（{G}{U}｜Legendary Creature — Bear Druid） — Spells you cast from your graveyard or from exile cost {2} less to cast. Plotting cards from your hand costs {2} less.
  3. Fblthp, Lost on the Range（{1}{U}{U}｜Legendary Creature — Homunculus） — Ward {2} You may look at the top card of your library any time. The top card of your library has plot. The plot cost is equal to its mana cost. You may plot nonland cards
  4. The Key to the Vault（{1}{U}｜Legendary Artifact — Equipment） — Whenever equipped creature deals combat damage to a player, look at that many cards from the top of your library. You may exile a nonland card from among them. Put the re
  5. Saw It Coming（{1}{U}{U}｜Instant） — Counter target spell. Foretell {1}{U} (During your turn, you may pay {2} and exile this card from your hand face down. Cast it on a later turn for its foretell cost.)
  6. Sage of the Beyond（{5}{U}{U}｜Creature — Spirit Giant） — Flying Spells you cast from anywhere other than your hand cost {2} less to cast. Foretell {4}{U} (During your turn, you may pay {2} and exile this card from your hand fac
- **出场率最高的牌**（大多数牌组都会放）
  - Rashmi, Eternities Crafter（{2}{G}{U}｜Legendary Creature — Elf Druid） — Whenever you cast your first spell each turn, reveal the top card of your library. You may cast it without paying its mana cost if
  - The Reality Chip（{1}{U}｜Legendary Artifact Creature — Equipment Jellyfish） — You may look at the top card of your library any time. As long as The Reality Chip is attached to a creature, you may play lands a
  - Behold the Multiverse（{3}{U}｜Instant） — Scry 2, then draw two cards. Foretell {1}{U} (During your turn, you may pay {2} and exile this card from your hand face down. Cast
  - Make Your Own Luck（{3}{G}{U}｜Sorcery） — Look at the top three cards of your library. You may exile a nonland card from among them. If you do, it becomes plotted. Put the 


## Grist, the Hunger Tide ｜ 饥潮格蕊斯
- 颜色 BG ｜ 法术力值 3.0 ｜ 类型 Legendary Planeswalker — Grist
- 流行度：EDHREC 全时段第 333 位，约 8063 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.38 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.52
- 社区标签：昆虫、自磨、坟场复活、磨牌、衍生物、坟场
- 完整牌面：As long as Grist isn't on the battlefield, it's a 1/1 Insect creature in addition to its other types.
+1: Create a 1/1 black and green Insect creature token, then mill a card. If an Insect card was milled this way, put a loyalty counter on Grist and repeat this process.
−2: You may sacrifice a creature. When you do, destroy target creature or planeswalker.
−5: Each opponent loses life equal to the number of creature cards in your graveyard.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Caustic Caterpillar（{G}｜Creature — Insect） — {1}{G}, Sacrifice this creature: Destroy target artifact or enchantment.
  2. Aatchik, Emerald Radian（{3}{B}{B}{G}｜Legendary Creature — Insect Druid） — When Aatchik enters, create a 1/1 green Insect creature token for each artifact and/or creature card in your graveyard. Whenever another Insect you control dies, put a +1
  3. Zask, Skittering Swarmlord（{3}{G}{G}｜Legendary Creature — Insect） — You may play lands and cast Insect spells from your graveyard. Whenever another Insect you control dies, put it on the bottom of its owner's library, then mill two cards.
  4. Grist, Voracious Larva（｜） — 
  5. Hornet Queen（{4}{G}{G}{G}｜Creature — Insect） — Flying, deathtouch When this creature enters, create four 1/1 green Insect creature tokens with flying and deathtouch.
  6. Hornet Nest（{2}{G}｜Creature — Insect） — Defender (This creature can't attack.) Whenever this creature is dealt damage, create that many 1/1 green Insect creature tokens with flying and deathtouch. (Any amount o
- **出场率最高的牌**（大多数牌组都会放）
  - Haywire Mite（{1}｜Artifact Creature — Insect） — When this creature dies, you gain 2 life. {G}, Sacrifice this creature: Exile target noncreature artifact or noncreature enchantme
  - Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create 
  - Giant Adephage（{5}{G}{G}｜Creature — Insect） — Trample Whenever this creature deals combat damage to a player, create a token that's a copy of this creature.
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.


## Bristly Bill, Spine Sower ｜ 锐刺播种师尖棘比利
- 颜色 G ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Plant Druid
- 流行度：EDHREC 全时段第 334 位，约 8047 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.96 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $34.08
- 社区标签：＋1/＋1 指示物、地牌核心、地落、加速、快攻、衍生物
- 完整牌面：Landfall — Whenever a land you control enters, put a +1/+1 counter on target creature.
{3}{G}{G}: Double the number of +1/+1 counters on each creature you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  2. Branching Evolution（{2}{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, twice that many +1/+1 counters are put on that creature instead.
  3. Mossborn Hydra（{2}{G}｜Creature — Elemental Hydra） — Trample (This creature can deal excess combat damage to the player or planeswalker it's attacking.) This creature enters with a +1/+1 counter on it. Landfall — Whenever a
  4. Kami of Whispered Hopes（{2}{G}｜Creature — Spirit） — If one or more +1/+1 counters would be put on a permanent you control, that many plus one +1/+1 counters are put on that permanent instead. {T}: Add X mana of any one col
  5. Evolution Sage（{2}{G}｜Creature — Elf Druid） — Landfall — Whenever a land you control enters, proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
  6. Kodama of the West Tree（{2}{G}｜Legendary Creature — Spirit） — Reach Modified creatures you control have trample. (Equipment, Auras you control, and counters are modifications.) Whenever a modified creature you control deals combat d
- **出场率最高的牌**（大多数牌组都会放）
  - Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create 
  - Inspiring Call（{2}{G}｜Instant） — Draw a card for each creature you control with a +1/+1 counter on it. Those creatures gain indestructible until end of turn. (Dama
  - Azusa, Lost but Seeking（{2}{G}｜Legendary Creature — Human Monk） — You may play two additional lands on each of your turns.
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 


## Tuvasa the Sunlit ｜ 阳辉吐瓦萨
- 颜色 WUG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Merfolk Shaman
- 流行度：EDHREC 全时段第 336 位，约 8040 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.09 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：结界流、灵气、主将单挑、铁壁防守、控制、组合技
- 完整牌面：Tuvasa gets +1/+1 for each enchantment you control.
Whenever you cast your first enchantment spell each turn, draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sythis, Harvest's Hand（{G}{W}｜Legendary Enchantment Creature — Nymph） — Whenever you cast an enchantment spell, you gain 1 life and draw a card.
  2. Enchantress's Presence（{2}{G}｜Enchantment） — Whenever you cast an enchantment spell, draw a card.
  3. Sanctum Weaver（{1}{G}｜Enchantment Creature — Dryad） — {T}: Add X mana of any one color, where X is the number of enchantments you control.
  4. Eidolon of Blossoms（{2}{G}{G}｜Enchantment Creature — Spirit） — Constellation — Whenever this creature or another enchantment you control enters, draw a card.
  5. Sterling Grove（{G}{W}｜Enchantment） — Other enchantments you control have shroud. (They can't be the targets of spells or abilities.) {1}, Sacrifice this enchantment: Search your library for an enchantment ca
  6. Setessan Champion（{2}{G}｜Creature — Human Warrior） — Constellation — Whenever an enchantment you control enters, put a +1/+1 counter on this creature and draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Wild Growth（{G}｜Enchantment — Aura） — Enchant land Whenever enchanted land is tapped for mana, its controller adds an additional {G}.
  - Jukai Naturalist（{G}{W}｜Enchantment Creature — Human Monk） — Lifelink Enchantment spells you cast cost {1} less to cast.
  - Fertile Ground（{1}{G}｜Enchantment — Aura） — Enchant land Whenever enchanted land is tapped for mana, its controller adds an additional one mana of any color.
  - Mesa Enchantress（{1}{W}{W}｜Creature — Human Druid） — Whenever you cast an enchantment spell, you may draw a card.


## Talion, the Kindly Lord ｜ 仁慈仙王塔莱恩
- 颜色 UB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Faerie Noble
- 流行度：EDHREC 全时段第 340 位，约 7978 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.72 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $9.00
- 社区标签：控制、仙灵、复制、组合技、中速、飞行
- 完整牌面：Flying
As Talion enters, choose a number between 1 and 10.
Whenever an opponent casts a spell with mana value, power, or toughness equal to the chosen number, that player loses 2 life and you draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Faerie Mastermind（{1}{U}｜Creature — Faerie Rogue） — Flash Flying Whenever an opponent draws their second card each turn, you draw a card. {3}{U}: Each player draws a card.
  2. Bloodchief Ascension（{B}｜Enchantment） — At the beginning of each end step, if an opponent lost 2 or more life this turn, you may put a quest counter on this enchantment. (Damage causes loss of life.) Whenever a
  3. Sheoldred, the Apocalypse（{2}{B}{B}｜Legendary Creature — Phyrexian Praetor） — Deathtouch Whenever you draw a card, you gain 2 life. Whenever an opponent draws a card, they lose 2 life.
  4. Mystic Remora（{U}｜Enchantment） — Cumulative upkeep {1} (At the beginning of your upkeep, put an age counter on this permanent, then sacrifice it unless you pay its upkeep cost for each age counter on it.
  5. Orcish Bowmasters（{1}{B}｜Creature — Orc Archer） — Flash When this creature enters and whenever an opponent draws a card except the first one they draw in each of their draw steps, this creature deals 1 damage to any targ
  6. Swan Song（{U}｜Instant） — Counter target enchantment, instant, or sorcery spell. Its controller creates a 2/2 blue Bird creature token with flying.
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Dominance（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {B}. This artifact deals 1 damage to you.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - An Offer You Can't Refuse（{U}｜Instant） — Counter target noncreature spell. Its controller creates two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: 


## Gisa and Geralf ｜ 基沙与基拉夫
- 颜色 UB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Wizard
- 流行度：EDHREC 全时段第 345 位，约 7906 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.26 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.37
- 社区标签：僵尸、坟场复活、坟场、衍生物、磨牌、自磨
- 完整牌面：When Gisa and Geralf enters, mill four cards.
Once during each of your turns, you may cast a Zombie creature spell from your graveyard.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Diregraf Captain（{1}{U}{B}｜Creature — Zombie Soldier） — Deathtouch Other Zombie creatures you control get +1/+1. Whenever another Zombie you control dies, target opponent loses 1 life.
  2. Lord of the Accursed（{2}{B}｜Creature — Zombie） — Other Zombies you control get +1/+1. {1}{B}, {T}: All Zombies gain menace until end of turn.
  3. Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost this way. (Each {B} in the mana costs of pe
  4. Champion of the Perished（{B}｜Creature — Zombie） — Whenever another Zombie you control enters, put a +1/+1 counter on this creature.
  5. Rooftop Storm（{5}{U}｜Enchantment） — You may pay {0} rather than pay the mana cost for Zombie creature spells you cast.
  6. Zombie Apocalypse（{3}{B}{B}{B}｜Sorcery） — Return all Zombie creature cards from your graveyard to the battlefield tapped, then destroy all Humans.
- **出场率最高的牌**（大多数牌组都会放）
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Choked Estuary（｜Land） — As this land enters, you may reveal an Island or Swamp card from your hand. If you don't, this land enters tapped. {T}: Add {U} or
  - Cemetery Reaper（{1}{B}{B}｜Creature — Zombie） — Other Zombie creatures you control get +1/+1. {2}{B}, {T}: Exile target creature card from a graveyard. Create a 2/2 black Zombie 
  - Undead Augur（{B}{B}｜Creature — Zombie Wizard） — Whenever this creature or another Zombie you control dies, you draw a card and lose 1 life.


## Gluntch, the Bestower ｜ 遣施怪古朗奇
- 颜色 WG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Jellyfish
- 流行度：EDHREC 全时段第 347 位，约 7889 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.25 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.51
- 社区标签：群体恩惠、＋1/＋1 指示物、衍生物、铁壁防守、生命增益、加速
- 完整牌面：Flying
At the beginning of your end step, choose a player. They put two +1/+1 counters on a creature they control. Choose a second player to draw a card. Then choose a third player to create two Treasure tokens.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Flumph（{1}{W}｜Creature — Jellyfish） — Defender, flying Whenever this creature is dealt damage, you and target opponent each draw a card.
  2. Selvala, Explorer Returned（{1}{G}{W}｜Legendary Creature — Elf Scout） — Parley — {T}: Each player reveals the top card of their library. For each nonland card revealed this way, add {G} and you gain 1 life. Then each player draws a card. (Act
  3. Rites of Flourishing（{2}{G}｜Enchantment） — At the beginning of each player's draw step, that player draws an additional card. Each player may play an additional land on each of their turns.
  4. Cut a Deal（{2}{W}｜Sorcery） — Each opponent draws a card, then you draw a card for each opponent who drew a card this way.
  5. Orzhov Advokist（{2}{W}｜Creature — Human Advisor） — At the beginning of your upkeep, each player may put two +1/+1 counters on a creature they control. If a player does, creatures that player controls can't attack you or p
  6. Nils, Discipline Enforcer（{2}{W}｜Legendary Creature — Human Cleric） — At the beginning of your end step, for each player, put a +1/+1 counter on up to one target creature that player controls. Each creature with one or more counters on it c
- **出场率最高的牌**（大多数牌组都会放）
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Sunpetal Grove（｜Land） — This land enters tapped unless you control a Forest or a Plains. {T}: Add {G} or {W}.
  - Secret Rendezvous（{1}{W}{W}｜Sorcery） — You and target opponent each draw three cards.


## Breena, the Demagogue ｜ 煽动师布莉娜
- 颜色 WB ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Bird Warlock
- 流行度：EDHREC 全时段第 348 位，约 7868 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.45 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.91
- 社区标签：＋1/＋1 指示物、铁壁防守、政治、群体恩惠、快攻、飞行
- 完整牌面：Flying
Whenever a player attacks one of your opponents, if that opponent has more life than another of your opponents, that attacking player draws a card and you put two +1/+1 counters on a creature you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Duelist's Heritage（{2}{W}｜Enchantment） — Whenever one or more creatures attack, you may have target attacking creature gain double strike until end of turn.
  2. Felisa, Fang of Silverquill（{2}{W}{B}｜Legendary Creature — Vampire Wizard） — Flying Mentor (Whenever this creature attacks, put a +1/+1 counter on target attacking creature with lesser power.) Whenever a nontoken creature you control dies, if it h
  3. Dusk Legion Duelist（{1}{W}｜Creature — Vampire Soldier） — Vigilance Whenever one or more +1/+1 counters are put on this creature, draw a card. This ability triggers only once each turn.
  4. Orzhov Advokist（{2}{W}｜Creature — Human Advisor） — At the beginning of your upkeep, each player may put two +1/+1 counters on a creature they control. If a player does, creatures that player controls can't attack you or p
  5. Shadrix Silverquill（{3}{W}{B}｜Legendary Creature — Elder Dragon） — Flying, double strike At the beginning of combat on your turn, you may choose two. Each mode must target a different player. • Target player creates a 2/1 white and black
  6. Promise of Loyalty（{4}{W}｜Sorcery） — Each player puts a vow counter on a creature they control and sacrifices the rest. Each of those creatures can't attack you or planeswalkers you control for as long as it
- **出场率最高的牌**（大多数牌组都会放）
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Inkshield（{3}{W}{B}｜Instant） — Prevent all combat damage that would be dealt to you this turn. For each 1 damage prevented this way, create a 2/1 white and black
  - Tainted Field（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. Activate only if you control a Swamp.


## Koma, Cosmos Serpent ｜ 寰宇盘蛇寇玛
- 颜色 UG ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Serpent
- 流行度：EDHREC 全时段第 349 位，约 7863 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.52 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.29
- 社区标签：衍生物、复制、控制、加速、海洋生物、地牌核心
- 完整牌面：This spell can't be countered.
At the beginning of each upkeep, create a 3/3 blue Serpent creature token named Koma's Coil.
Sacrifice another Serpent: Choose one —
• Tap target permanent. Its activated abilities can't be activated this turn.
• Koma gains indestructible until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Adrix and Nev, Twincasters（{2}{G}{U}｜Legendary Creature — Merfolk Wizard） — Ward {2} (Whenever this creature becomes the target of a spell or ability an opponent controls, counter it unless that player pays {2}.) If one or more tokens would be cr
  2. Elemental Bond（{2}{G}｜Enchantment） — Whenever a creature you control with power 3 or greater enters, draw a card.
  3. Whelming Wave（{2}{U}{U}｜Sorcery） — Return all creatures to their owners' hands except for Krakens, Leviathans, Octopuses, and Serpents.
  4. Koma, World-Eater（{3}{G}{G}{U}{U}｜Legendary Creature — Serpent） — This spell can't be countered. Trample, ward {4} Whenever Koma deals combat damage to a player, create four 3/3 blue Serpent creature tokens named Koma's Coil.
  5. Spark Double（{3}{U}｜Creature — Illusion） — You may have this creature enter as a copy of a creature or planeswalker you control, except it enters with an additional +1/+1 counter on it if it's a creature, it enter
  6. Junk Winder（{5}{U}{U}｜Creature — Serpent） — Affinity for tokens (This spell costs {1} less to cast for each token you control.) Whenever a token you control enters, tap target nonland permanent an opponent controls
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Parallel Lives（{3}{G}｜Enchantment） — If an effect would create one or more tokens under your control, it creates twice that many of those tokens instead.
  - Growth Spiral（{G}{U}｜Instant） — Draw a card. You may put a land card from your hand onto the battlefield.


## Lathiel, the Bounteous Dawn ｜ 丰饶曙光拉狄雷
- 颜色 WG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Unicorn
- 流行度：EDHREC 全时段第 350 位，约 7861 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.25 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.85
- 社区标签：生命增益、＋1/＋1 指示物、Unicorns、衍生物、组合技、快攻
- 完整牌面：Lifelink
At the beginning of each end step, if you gained life this turn, distribute up to that many +1/+1 counters among any number of other target creatures.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Soul Warden（{W}｜Creature — Human Cleric） — Whenever another creature enters, you gain 1 life.
  2. Essence Warden（{G}｜Creature — Elf Shaman） — Whenever another creature enters, you gain 1 life.
  3. Soul's Attendant（{W}｜Creature — Human Cleric） — Whenever another creature enters, you may gain 1 life.
  4. Rhox Faithmender（{3}{W}｜Creature — Rhino Monk） — Lifelink (Damage dealt by this creature also causes you to gain that much life.) If you would gain life, you gain twice that much life instead.
  5. Cleric Class（{W}｜Enchantment — Class） — (Gain the next level as a sorcery to add its ability.) If you would gain life, you gain that much life plus 1 instead. {3}{W}: Level 2 Whenever you gain life, put a +1/+1
  6. Conclave Mentor（{G}{W}｜Creature — Centaur Cleric） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on that creature instead. When this creature dies, you gai
- **出场率最高的牌**（大多数牌组都会放）
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Blossoming Sands（｜Land） — This land enters tapped. When this land enters, you gain 1 life. {T}: Add {G} or {W}.
  - Inspiring Call（{2}{G}｜Instant） — Draw a card for each creature you control with a +1/+1 counter on it. Those creatures gain indestructible until end of turn. (Dama
  - Sunpetal Grove（｜Land） — This land enters tapped unless you control a Forest or a Plains. {T}: Add {G} or {W}.


## Sidisi, Brood Tyrant ｜ 族群暴君谢迪西
- 颜色 UBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Snake Shaman
- 流行度：EDHREC 全时段第 351 位，约 7836 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.37 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.34
- 社区标签：磨牌、坟场复活、自磨、挖掘、坟场、衍生物
- 完整牌面：Whenever Sidisi enters or attacks, mill three cards.
Whenever one or more creature cards are put into your graveyard from your library, create a 2/2 black Zombie creature token.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Dread Return（{2}{B}{B}｜Sorcery） — Return target creature card from your graveyard to the battlefield. Flashback—Sacrifice three creatures. (You may cast this card from your graveyard for its flashback cos
  2. Wonder（{3}{U}｜Creature — Incarnation） — Flying As long as this card is in your graveyard and you control an Island, creatures you control have flying.
  3. Snarling Gorehound（{B}｜Creature — Dog） — Menace Whenever another creature you control with power 2 or less enters, surveil 1. (Look at the top card of your library. You may put it into your graveyard.)
  4. Skull Prophet（{B}{G}｜Creature — Human Druid） — {T}: Add {B} or {G}. {T}: Mill two cards. (Put the top two cards of your library into your graveyard.)
  5. Wight of the Reliquary（{B}{G}｜Creature — Zombie Knight） — Vigilance This creature gets +1/+1 for each creature card in your graveyard. {T}, Sacrifice another creature: Search your library for a land card, put it onto the battlef
  6. Syr Konrad, the Grim（{3}{B}{B}｜Legendary Creature — Human Knight） — Whenever another creature dies, or a creature card is put into a graveyard from anywhere other than the battlefield, or a creature card leaves your graveyard, Syr Konrad 
- **出场率最高的牌**（大多数牌组都会放）
  - Stitcher's Supplier（{B}｜Creature — Zombie） — When this creature enters or dies, mill three cards. (Put the top three cards of your library into your graveyard.)
  - Eternal Witness（{1}{G}{G}｜Creature — Human Shaman） — When this creature enters, you may return target card from your graveyard to your hand.
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Opulent Palace（｜Land） — This land enters tapped. {T}: Add {B}, {G}, or {U}.


## Admiral Brass, Unsinkable ｜ 不沉传奇霸司总帅
- 颜色 UBR ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Pirate
- 流行度：EDHREC 全时段第 354 位，约 7802 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.38 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.26
- 社区标签：海盗、宝物、坟场复活、快攻、偷取、坟场
- 完整牌面：When Admiral Brass enters, mill four cards.
At the beginning of combat on your turn, you may return target Pirate creature card from your graveyard to the battlefield with a finality counter on it. It has base power and toughness 4/4. It gains haste until end of turn. (If a creature with a finality counter on it would die, exile it instead.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Malcolm, Keen-Eyed Navigator（{2}{U}｜Legendary Creature — Siren Pirate） — Flying Whenever one or more Pirates you control deal damage to your opponents, you create a Treasure token for each opponent dealt damage. (It's an artifact with "{T}, Sa
  2. Skeleton Crew（{3}{B}｜Creature — Skeleton Pirate） — Each other creature you control that's a Skeleton or Pirate gets +1/+1. Whenever one or more creature cards leave your graveyard, create a 2/2 black Skeleton Pirate creat
  3. Port Razer（{3}{R}{R}｜Creature — Orc Pirate） — Whenever this creature deals combat damage to a player, untap each creature you control. After this phase, there is an additional combat phase. This creature can't attack
  4. Coercive Recruiter（{4}{R}｜Creature — Orc Pirate） — Whenever this creature or another Pirate you control enters, gain control of target creature until end of turn. Untap that creature. Until end of turn, it gains haste and
  5. Corsair Captain（{2}{U}｜Creature — Human Pirate） — When this creature enters, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.") Other Pirates you control get +1/+1.
  6. Admiral Beckett Brass（{1}{U}{B}{R}｜Legendary Creature — Human Pirate） — Other Pirates you control get +1/+1. At the beginning of your end step, gain control of target nonland permanent controlled by a player who was dealt combat damage by thr
- **出场率最高的牌**（大多数牌组都会放）
  - Hostage Taker（{2}{U}{B}｜Creature — Human Pirate） — When this creature enters, exile another target creature or artifact until this creature leaves the battlefield. You may cast that
  - Siren Stormtamer（{U}｜Creature — Siren Pirate Wizard） — Flying {U}, Sacrifice this creature: Counter target spell or ability that targets you or a creature you control.
  - Gemcutter Buccaneer（{3}{R}｜Creature — Orc Pirate Artificer） — Whenever this creature or another Pirate you control enters, create a tapped Treasure token. Treasures you control are Equipment i
  - Captain Lannery Storm（{2}{R}｜Legendary Creature — Human Pirate） — Haste Whenever Captain Lannery Storm attacks, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one 


## Ellivere of the Wild Court ｜ 幻野廷的莉薇尔
- 颜色 WG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Knight
- 流行度：EDHREC 全时段第 355 位，约 7794 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.36 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.43
- 社区标签：灵气、结界流、锁场小兵、锁场、快攻、主将单挑
- 完整牌面：Whenever Ellivere enters or attacks, create a Virtuous Role token attached to another target creature you control. (If you control another Role on it, put that one into the graveyard. Enchanted creature gets +1/+1 for each enchantment you control.)
Whenever an enchanted creature you control deals combat damage to a player, draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sanctum Weaver（{1}{G}｜Enchantment Creature — Dryad） — {T}: Add X mana of any one color, where X is the number of enchantments you control.
  2. Setessan Champion（{2}{G}｜Creature — Human Warrior） — Constellation — Whenever an enchantment you control enters, put a +1/+1 counter on this creature and draw a card.
  3. Winds of Rath（{3}{W}{W}｜Sorcery） — Destroy all creatures that aren't enchanted. They can't be regenerated.
  4. Utopia Sprawl（{G}｜Enchantment — Aura） — Enchant Forest As this Aura enters, choose a color. Whenever enchanted Forest is tapped for mana, its controller adds an additional one mana of the chosen color.
  5. Umbra Mystic（{2}{W}｜Creature — Human Wizard） — Auras attached to permanents you control have umbra armor. (If an enchanted permanent you control would be destroyed, instead remove all damage from it and destroy an Aur
  6. Destiny Spinner（{1}{G}｜Enchantment Creature — Human） — Creature and enchantment spells you control can't be countered. {3}{G}: Target land you control becomes an X/X Elemental creature with trample and haste until end of turn
- **出场率最高的牌**（大多数牌组都会放）
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Eidolon of Blossoms（{2}{G}{G}｜Enchantment Creature — Spirit） — Constellation — Whenever this creature or another enchantment you control enters, draw a card.
  - Ethereal Armor（{W}｜Enchantment — Aura） — Enchant creature Enchanted creature gets +1/+1 for each enchantment you control and has first strike.
  - Kenrith's Transformation（{1}{G}｜Enchantment — Aura） — Enchant creature When this Aura enters, draw a card. Enchanted creature loses all abilities and is a green Elk creature with base 


## Sméagol, Helpful Guide ｜ 有用向导斯密戈
- 颜色 BG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Halfling Horror
- 流行度：EDHREC 全时段第 357 位，约 7764 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.86 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.36
- 社区标签：地牌核心、磨牌、地落、牺牲、牺牲流、The Ring
- 完整牌面：At the beginning of your end step, if a creature died under your control this turn, the Ring tempts you.
Whenever the Ring tempts you, target opponent reveals cards from the top of their library until they reveal a land card. Put that card onto the battlefield tapped under your control and the rest into their graveyard.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Call of the Ring（{1}{B}｜Enchantment） — At the beginning of your upkeep, the Ring tempts you. Whenever you choose a creature as your Ring-bearer, you may pay 2 life. If you do, draw a card.
  2. Gollum, Patient Plotter（{1}{B}｜Legendary Creature — Halfling Horror） — When Gollum leaves the battlefield, the Ring tempts you. {B}, Sacrifice a creature: Return this card from your graveyard to your hand. Activate only as a sorcery.
  3. Sam's Desperate Rescue（{B}｜Sorcery） — Return target creature card from your graveyard to your hand. The Ring tempts you.
  4. Claim the Precious（{1}{B}{B}｜Sorcery） — Destroy target creature. The Ring tempts you.
  5. Bombadil's Song（{1}{G}｜Instant） — Target creature you control gets +1/+1 and gains hexproof until end of turn. The Ring tempts you. (A creature with hexproof can't be the target of spells or abilities you
  6. Dúnedain Rangers（{3}{G}｜Creature — Human Ranger） — Landfall — Whenever a land you control enters, if you don't control a Ring-bearer, the Ring tempts you.
- **出场率最高的牌**（大多数牌组都会放）
  - Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create 
  - Nazgûl（{2}{B}｜Creature — Wraith Knight） — Deathtouch When this creature enters, the Ring tempts you. Whenever the Ring tempts you, put a +1/+1 counter on each Wraith you co
  - Bloodghast（{B}{B}｜Creature — Vampire Spirit） — This creature can't block. This creature has haste as long as an opponent has 10 or less life. Landfall — Whenever a land you cont
  - Sakura-Tribe Elder（{1}{G}｜Creature — Snake Shaman） — Sacrifice this creature: Search your library for a basic land card, put that card onto the battlefield tapped, then shuffle.


## Commodore Guff ｜ 古夫准将
- 颜色 WUR ｜ 法术力值 4.0 ｜ 类型 Legendary Planeswalker — Guff
- 流行度：EDHREC 全时段第 358 位，约 7710 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.6 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：鹏洛客、控制、增殖、烧血、铁壁防守、额外回合
- 完整牌面：At the beginning of your end step, put a loyalty counter on another target planeswalker you control.
+1: Create a 1/1 red Wizard creature token with "{T}: Add {R}. Spend this mana only to cast a planeswalker spell."
−3: You draw X cards and Commodore Guff deals X damage to each opponent, where X is the number of planeswalkers you control.
Commodore Guff can be your commander.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Oath of Teferi（{3}{W}{U}｜Legendary Enchantment） — When Oath of Teferi enters, exile another target permanent you control. Return it to the battlefield under its owner's control at the beginning of the next end step. You 
  2. Chandra, Legacy of Fire（{4}{R}｜Legendary Planeswalker — Chandra） — At the beginning of your end step, Chandra deals X damage to each opponent, where X is the number of planeswalkers you control. +1: Add {R} for each planeswalker you cont
  3. Interplanar Beacon（｜Land） — Whenever you cast a planeswalker spell, you gain 1 life. {T}: Add {C}. {1}, {T}: Add two mana of different colors. Spend this mana only to cast planeswalker spells.
  4. Chandra, Torch of Defiance（{2}{R}{R}｜Legendary Planeswalker — Chandra） — +1: Exile the top card of your library. You may cast that card. If you don't, Chandra deals 2 damage to each opponent. +1: Add {R}{R}. −3: Chandra deals 4 damage to targe
  5. The Chain Veil（{4}｜Legendary Artifact） — At the beginning of your end step, if you didn't activate a loyalty ability of a planeswalker this turn, you lose 2 life. {4}, {T}: For each planeswalker you control, you
  6. Vronos, Masked Inquisitor（{3}{U}{U}｜Legendary Planeswalker — Vronos） — +1: Up to two other target planeswalkers you control phase out at the beginning of the next end step. (Treat them and anything attached to them as though they don't exist
- **出场率最高的牌**（大多数牌组都会放）
  - Elspeth, Sun's Champion（{4}{W}{W}｜Legendary Planeswalker — Elspeth） — +1: Create three 1/1 white Soldier creature tokens. −3: Destroy all creatures with power 4 or greater. −7: You get an emblem with 
  - Deepglow Skate（{4}{U}｜Creature — Fish） — When this creature enters, double the number of each kind of counter on any number of target permanents.
  - Karn's Bastion（｜Land） — {T}: Add {C}. {4}, {T}: Proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind 
  - Flux Channeler（{2}{U}｜Creature — Human Wizard） — Whenever you cast a noncreature spell, proliferate. (Choose any number of permanents and/or players, then give each another counte


## The Gitrog, Ravenous Ride ｜ 血口坐骑噬人蛙怪
- 颜色 BG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Frog Horror Mount
- 流行度：EDHREC 全时段第 359 位，约 7706 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.52 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.80
- 社区标签：大生物、地牌核心、加速、地落、快攻、牺牲
- 完整牌面：Trample, haste
Whenever The Gitrog deals combat damage to a player, you may sacrifice a creature that saddled it this turn. If you do, draw X cards, then put up to X land cards from your hand onto the battlefield tapped, where X is the sacrificed creature's power.
Saddle 1
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Daemogoth Titan（{B/G}{B/G}{B/G}{B/G}｜Creature — Demon） — Whenever this creature attacks or blocks, sacrifice a creature.
  2. Yargle and Multani（{3}{B}{B}{G}｜Legendary Creature — Frog Spirit Elemental） — 
  3. Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess combat damage to the player or planeswalker
  4. Spelunking（{2}{G}｜Enchantment） — When this enchantment enters, draw a card, then you may put a land card from your hand onto the battlefield. If you put a Cave onto the battlefield this way, you gain 4 l
  5. Rampaging Baloths（{4}{G}{G}｜Creature — Beast） — Trample Landfall — Whenever a land you control enters, create a 4/4 green Beast creature token.
  6. Pugnacious Hammerskull（{2}{G}｜Creature — Dinosaur） — Whenever this creature attacks while you don't control another Dinosaur, put a stun counter on it. (If a permanent with a stun counter would become untapped, remove one f
- **出场率最高的牌**（大多数牌组都会放）
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Tireless Provisioner（{2}{G}｜Creature — Elf Scout） — Landfall — Whenever a land you control enters, create a Food token or a Treasure token. (Food is an artifact with "{2}, {T}, Sacri
  - Assassin's Trophy（{B}{G}｜Instant） — Destroy target permanent an opponent controls. Its controller may search their library for a basic land card, put it onto the batt
  - The Skullspore Nexus（{6}{G}{G}｜Legendary Artifact） — This spell costs {X} less to cast, where X is the greatest power among creatures you control. Whenever one or more nontoken creatu


## Kardur, Doomscourge ｜ 末日灾祸卡尔杜
- 颜色 BR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Demon Berserker
- 流行度：EDHREC 全时段第 360 位，约 7693 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.57 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.56
- 社区标签：强制战斗、群体折磨、混乱、牺牲流、烧血、快攻
- 完整牌面：When Kardur enters, until your next turn, creatures your opponents control attack each combat if able and attack a player other than you if able.
Whenever an attacking creature dies, each opponent loses 1 life and you gain 1 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Conjurer's Closet（{5}｜Artifact） — At the beginning of your end step, you may exile target creature you control, then return that card to the battlefield under your control.
  2. Geode Rager（{4}{R}{R}｜Creature — Elemental） — First strike Landfall — Whenever a land you control enters, goad each creature target player controls. (Until your next turn, those creatures attack each combat if able a
  3. Disrupt Decorum（{2}{R}{R}｜Sorcery） — Goad all creatures you don't control. (Until your next turn, those creatures attack each combat if able and attack a player other than you if able.)
  4. Kazuul, Tyrant of the Cliffs（{3}{R}{R}｜Legendary Creature — Ogre Warrior） — Whenever a creature an opponent controls attacks, if you're the defending player, create a 3/3 red Ogre creature token unless that creature's controller pays {3}.
  5. Vengeful Ancestor（{2}{R}{R}｜Creature — Spirit Dragon） — Flying Whenever this creature enters or attacks, goad target creature. (Until your next turn, that creature attacks each combat if able and attacks a player other than yo
  6. Morbid Opportunist（{2}{B}｜Creature — Human Rogue） — Whenever one or more other creatures die, draw a card. This ability triggers only once each turn.
- **出场率最高的牌**（大多数牌组都会放）
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.
  - Rakdos Signet（{2}｜Artifact） — {1}, {T}: Add {B}{R}.
  - Rakdos Charm（{B}{R}｜Instant） — Choose one — • Exile target player's graveyard. • Destroy target artifact. • Each creature deals 1 damage to its controller.
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.


## Nethroi, Apex of Death ｜ 夺命霸狮涅司罗
- 颜色 WBG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Cat Nightmare Beast
- 流行度：EDHREC 全时段第 361 位，约 7690 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.5 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.36
- 社区标签：坟场复活、突变、磨牌、坟场、自磨、牺牲流
- 完整牌面：Mutate {4}{G/W}{B}{B} (If you cast this spell for its mutate cost, put it over or under target non-Human creature you own. They mutate into the creature on top plus all abilities from under it.)
Deathtouch, lifelink
Whenever this creature mutates, return any number of target creature cards with total power 10 or less from your graveyard to the battlefield.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Gemrazer（{3}{G}｜Creature — Beast） — Mutate {1}{G}{G} (If you cast this spell for its mutate cost, put it over or under target non-Human creature you own. They mutate into the creature on top plus all abilit
  2. Necropanther（{1}{W}{B}｜Creature — Cat Nightmare） — Mutate {2}{W/B}{W/B} (If you cast this spell for its mutate cost, put it over or under target non-Human creature you own. They mutate into the creature on top plus all ab
  3. Boneyard Lurker（{2}{B}{G}｜Creature — Nightmare Beast） — Mutate {2}{B/G}{B/G} (If you cast this spell for its mutate cost, put it over or under target non-Human creature you own. They mutate into the creature on top plus all ab
  4. Migratory Greathorn（{3}{G}｜Creature — Beast） — Mutate {2}{G} (If you cast this spell for its mutate cost, put it over or under target non-Human creature you own. They mutate into the creature on top plus all abilities
  5. Buried Alive（{2}{B}｜Sorcery） — Search your library for up to three creature cards, put them into your graveyard, then shuffle.
  6. Stitcher's Supplier（{B}｜Creature — Zombie） — When this creature enters or dies, mill three cards. (Put the top three cards of your library into your graveyard.)
- **出场率最高的牌**（大多数牌组都会放）
  - Sandsteppe Citadel（｜Land） — This land enters tapped. {T}: Add {W}, {B}, or {G}.
  - Indatha Triome（｜Land — Plains Swamp Forest） — ({T}: Add {W}, {B}, or {G}.) This land enters tapped. Cycling {3} ({3}, Discard this card: Draw a card.)
  - Eerie Ultimatum（{W}{W}{B}{B}{B}{G}{G}｜Sorcery） — Return any number of permanent cards with different names from your graveyard to the battlefield.
  - Sakura-Tribe Elder（{1}{G}｜Creature — Snake Shaman） — Sacrifice this creature: Search your library for a basic land card, put that card onto the battlefield tapped, then shuffle.


## Sigarda, Font of Blessings ｜ 祝福圣源席嘉妲
- 颜色 WG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Angel
- 流行度：EDHREC 全时段第 366 位，约 7621 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.56 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.02
- 社区标签：天使、＋1/＋1 指示物、人类、生命增益、飞行、衍生物
- 完整牌面：Flying
Other permanents you control have hexproof.
You may look at the top card of your library any time.
You may cast Angel spells and Human spells from the top of your library.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Giada, Font of Hope（{1}{W}｜Legendary Creature — Angel） — Flying, vigilance Each other Angel you control enters with an additional +1/+1 counter on it for each Angel you already control. {T}: Add {W}. Spend this mana only to cas
  2. Lyra Dawnbringer（{3}{W}{W}｜Legendary Creature — Angel） — Flying First strike (This creature deals combat damage before creatures without first strike.) Lifelink (Damage dealt by this creature also causes you to gain that much l
  3. Herald of War（{3}{W}{W}｜Creature — Angel） — Flying Whenever this creature attacks, put a +1/+1 counter on it. Angel spells and Human spells you cast cost {1} less to cast for each +1/+1 counter on this creature.
  4. Avacyn, Angel of Hope（{5}{W}{W}{W}｜Legendary Creature — Angel） — Flying, vigilance, indestructible Other permanents you control have indestructible.
  5. Starnheim Aspirant（{2}{W}｜Creature — Human Cleric） — Angel spells you cast cost {2} less to cast.
  6. Righteous Valkyrie（{2}{W}｜Creature — Angel Cleric） — Flying Whenever another Angel or Cleric you control enters, you gain life equal to that creature's toughness. As long as you have at least 7 life more than your starting 
- **出场率最高的牌**（大多数牌组都会放）
  - Shalai, Voice of Plenty（{3}{W}｜Legendary Creature — Angel） — Flying You, planeswalkers you control, and other creatures you control have hexproof. {4}{G}{G}: Put a +1/+1 counter on each creat
  - Canopy Vista（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) This land enters tapped unless you control two or more basic lands.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Avacyn's Pilgrim（{G}｜Creature — Human Monk） — {T}: Add {W}.
