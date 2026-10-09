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

# 素材：23 位主将


## Vincent Valentine // Galian Beast ｜ 文森特·瓦伦丁
- 颜色 B ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Assassin // Legendary Creature — Werewolf Beast
- 流行度：EDHREC 全时段第 561 位，约 5343 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.35 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.67
- 社区标签：＋1/＋1 指示物、主将单挑、牺牲、控制、牺牲流、快攻
- 完整牌面：Whenever a creature an opponent controls dies, put a number of +1/+1 counters on Vincent Valentine equal to that creature's power.
Whenever Vincent Valentine attacks, you may transform it.
//
Trample, lifelink
When Galian Beast dies, return it to the battlefield tapped (front face up).
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sheoldred's Edict（{1}{B}｜Instant） — Choose one — • Each opponent sacrifices a nontoken creature of their choice. • Each opponent sacrifices a creature token of their choice. • Each opponent sacrifices a pla
  2. Fleshbag Marauder（{2}{B}｜Creature — Zombie Warrior） — When this creature enters, each player sacrifices a creature of their choice.
  3. Accursed Marauder（{1}{B}｜Creature — Zombie Warrior） — When this creature enters, each player sacrifices a nontoken creature of their choice.
  4. Soul Shatter（{2}{B}｜Instant） — Each opponent sacrifices a creature or planeswalker with the greatest mana value among creatures and planeswalkers they control.
  5. Plaguecrafter（{2}{B}｜Creature — Human Shaman） — When this creature enters, each player sacrifices a creature or planeswalker of their choice. Each player who can't discards a card.
  6. The Masamune（{3}｜Legendary Artifact — Equipment） — As long as equipped creature is attacking, it has first strike and must be blocked if able. Equipped creature has "If a creature dying causes a triggered ability of this 
- **出场率最高的牌**（大多数牌组都会放）
  - Morbid Opportunist（{2}{B}｜Creature — Human Rogue） — Whenever one or more other creatures die, draw a card. This ability triggers only once each turn.
  - Feed the Swarm（{1}{B}｜Sorcery） — Destroy target creature or enchantment an opponent controls. You lose life equal to that permanent's mana value.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.


## Kumena, Tyrant of Orazca ｜ 欧拉兹卡暴君库莫那
- 颜色 UG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Merfolk Shaman
- 流行度：EDHREC 全时段第 562 位，约 5290 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.37 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.33
- 社区标签：人鱼、＋1/＋1 指示物、组合技、横置／重置、衍生物、快攻
- 完整牌面：Tap another untapped Merfolk you control: Kumena can't be blocked this turn.
Tap three untapped Merfolk you control: Draw a card.
Tap five untapped Merfolk you control: Put a +1/+1 counter on each Merfolk you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Merrow Reejerey（{2}{U}｜Creature — Merfolk Soldier） — Other Merfolk creatures you control get +1/+1. Whenever you cast a Merfolk spell, you may tap or untap target permanent.
  2. Deeproot Waters（{2}{U}｜Enchantment） — Whenever you cast a Merfolk spell, create a 1/1 blue Merfolk creature token with hexproof. (A creature with hexproof can't be the target of spells or abilities your oppon
  3. Master of the Pearl Trident（{U}{U}｜Creature — Merfolk） — Other Merfolk creatures you control get +1/+1 and have islandwalk. (They can't be blocked as long as defending player controls an Island.)
  4. Svyelun of Sea and Sky（{1}{U}{U}｜Legendary Creature — Merfolk God） — Svyelun has indestructible as long as you control at least two other Merfolk. Whenever Svyelun attacks, draw a card. Other Merfolk you control have ward {1}. (Whenever an
  5. Stonybrook Banneret（{1}{U}｜Creature — Merfolk Wizard） — Islandwalk (This creature can't be blocked as long as defending player controls an Island.) Merfolk spells and Wizard spells you cast cost {1} less to cast.
  6. Deeproot Pilgrimage（{1}{U}｜Enchantment） — Whenever one or more nontoken Merfolk you control become tapped, create a 1/1 blue Merfolk creature token with hexproof.
- **出场率最高的牌**（大多数牌组都会放）
  - Emperor Mihail II（{1}{U}{U}｜Legendary Creature — Merfolk Noble） — You may look at the top card of your library any time. You may cast Merfolk spells from the top of your library. Whenever you cast
  - Kopala, Warden of Waves（{1}{U}{U}｜Legendary Creature — Merfolk Wizard） — Spells your opponents cast that target a Merfolk you control cost {2} more to cast. Abilities your opponents activate that target 
  - Deeproot Elite（{1}{G}｜Creature — Merfolk Warrior） — Whenever another Merfolk you control enters, put a +1/+1 counter on target Merfolk you control.
  - Merfolk Sovereign（{1}{U}{U}｜Creature — Merfolk Noble） — Other Merfolk creatures you control get +1/+1. {T}: Target Merfolk creature can't be blocked this turn.


## Rakdos, the Muscle ｜ 帮凶魔头拉铎司
- 颜色 BR ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Demon Mercenary
- 流行度：EDHREC 全时段第 565 位，约 5269 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.35 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.23
- 社区标签：牺牲、牺牲流、组合技、偷取、风暴、坟场复活
- 完整牌面：Flying, trample
Whenever you sacrifice another creature, exile cards equal to its mana value from the top of target player's library. Until your next end step, you may play those cards, and mana of any type can be spent to cast those spells.
Sacrifice another creature: Rakdos gains indestructible until end of turn. Tap it. Activate only once each turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Shriekmaw（{4}{B}｜Creature — Elemental） — Fear (This creature can't be blocked except by artifact creatures and/or black creatures.) When this creature enters, destroy target nonartifact, nonblack creature. Evoke
  2. Ingot Chewer（{4}{R}｜Creature — Elemental） — When this creature enters, destroy target artifact. Evoke {R} (You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters.)
  3. Forsaken Miner（{B}｜Creature — Skeleton Rogue） — This creature can't block. Whenever you commit a crime, you may pay {B}. If you do, return this card from your graveyard to the battlefield. (Targeting opponents, anythin
  4. Poxwalkers（{2}{B}｜Creature — Zombie） — Deathtouch Curse of the Walking Pox — Whenever you cast a spell from anywhere other than your hand, return this card from your graveyard to the battlefield tapped.
  5. Ashnod's Altar（{3}｜Artifact） — Sacrifice a creature: Add {C}{C}.
  6. Burnt Offering（{B}｜Instant） — As an additional cost to cast this spell, sacrifice a creature. Add X mana in any combination of {B} and/or {R}, where X is the sacrificed creature's mana value.
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Indulgence（{2}｜Artifact） — {T}: Add {C}. {T}: Add {B} or {R}. This artifact deals 1 damage to you.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Blood Crypt（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Sulfurous Springs（｜Land） — {T}: Add {C}. {T}: Add {B} or {R}. This land deals 1 damage to you.


## Syr Vondam, Sunstar Exemplar ｜ 辉星模范冯棠爵士
- 颜色 WB ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Knight
- 流行度：EDHREC 全时段第 566 位，约 5269 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.19 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.39
- 社区标签：闪现回场、牺牲流、衍生物、＋1/＋1 指示物、生命增益、牺牲
- 完整牌面：Vigilance, menace
Whenever another creature you control dies or is put into exile, put a +1/+1 counter on Syr Vondam and you gain 1 life.
When Syr Vondam dies or is put into exile while its power is 4 or greater, destroy up to one target nonland permanent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ephemerate（{W}｜Instant） — Exile target creature you control, then return it to the battlefield under its owner's control. Rebound (If you cast this spell from your hand, exile it as it resolves. A
  2. Cloudshift（{W}｜Instant） — Exile target creature you control, then return that card to the battlefield under your control.
  3. Elegy Acolyte（{2}{B}{B}｜Creature — Human Cleric） — Lifelink Whenever one or more creatures you control deal combat damage to a player, you draw a card and lose 1 life. Void — At the beginning of your end step, if a nonlan
  4. Flowering of the White Tree（{W}{W}｜Legendary Enchantment） — Legendary creatures you control get +2/+1 and have ward {1}. Nonlegendary creatures you control get +1/+1.
  5. Haliya, Guided by Light（{2}{W}｜Legendary Creature — Human Soldier） — Whenever Haliya or another creature or artifact you control enters, you gain 1 life. At the beginning of your end step, draw a card if you've gained 3 or more life this t
  6. Parting Gust（{W}{W}｜Instant） — Gift a tapped Fish (You may promise an opponent a gift as you cast this spell. If you do, they create a tapped 1/1 blue Fish creature token before its other effects.) Exi
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Caves of Koilos（｜Land） — {T}: Add {C}. {T}: Add {W} or {B}. This land deals 1 damage to you.
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Elas il-Kor, Sadistic Pilgrim（{W}{B}｜Legendary Creature — Phyrexian Kor Cleric） — Deathtouch Whenever another creature you control enters, you gain 1 life. Whenever another creature you control dies, each opponen


## Heliod, Sun-Crowned ｜ 日冠赫利欧德
- 颜色 W ｜ 法术力值 3.0 ｜ 类型 Legendary Enchantment Creature — God
- 流行度：EDHREC 全时段第 567 位，约 5268 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.9 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $22.16
- 社区标签：生命增益、＋1/＋1 指示物、组合技、锁场、衍生物、虔诚
- 完整牌面：Indestructible
As long as your devotion to white is less than five, Heliod isn't a creature.
Whenever you gain life, put a +1/+1 counter on target creature or enchantment you control.
{1}{W}: Another target creature gains lifelink until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Daxos, Blessed by the Sun（{W}{W}｜Legendary Enchantment Creature — Demigod） — Daxos's toughness is equal to your devotion to white. (Each {W} in the mana costs of permanents you control counts toward your devotion to white.) Whenever another creatu
  2. Soul Warden（{W}｜Creature — Human Cleric） — Whenever another creature enters, you gain 1 life.
  3. Soul's Attendant（{W}｜Creature — Human Cleric） — Whenever another creature enters, you may gain 1 life.
  4. Walking Ballista（{X}{X}｜Artifact Creature — Construct） — This creature enters with X +1/+1 counters on it. {4}: Put a +1/+1 counter on this creature. Remove a +1/+1 counter from this creature: It deals 1 damage to any target.
  5. Voice of the Blessed（{W}{W}｜Creature — Spirit Cleric） — Whenever you gain life, put a +1/+1 counter on this creature. As long as this creature has four or more +1/+1 counters on it, it has flying and vigilance. As long as this
  6. Authority of the Consuls（{W}｜Enchantment） — Creatures your opponents control enter tapped. Whenever a creature an opponent controls enters, you gain 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Pearl Medallion（{2}｜Artifact） — White spells you cast cost {1} less to cast.
  - Esper Sentinel（{W}｜Artifact Creature — Human Soldier） — Whenever an opponent casts their first noncreature spell each turn, draw a card unless that player pays {X}, where X is this creat
  - Serra Ascendant（{W}｜Creature — Human Monk） — Lifelink (Damage dealt by this creature also causes you to gain that much life.) As long as you have 30 or more life, this creatur


## Rat King, Verminister ｜ 疫病根源鼠王
- 颜色 B ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Rat Avatar
- 流行度：EDHREC 全时段第 568 位，约 5242 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.69
- 社区标签：老鼠、坟场复活、衍生物、鼠群、牺牲流、Relentless Rats
- 完整牌面：Disappear — At the beginning of your end step, if a permanent left the battlefield under your control this turn, create a 1/1 black Rat creature token and put a +1/+1 counter on Rat King.
{T}, Sacrifice three Rats: Return target creature card and all other cards with the same name as that card from your graveyard to the battlefield tapped.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Marrow-Gnawer（{3}{B}{B}｜Legendary Creature — Rat Rogue） — All Rats have fear. {T}, Sacrifice a Rat: Create X 1/1 black Rat creature tokens, where X is the number of Rats you control.
  2. Rat Colony（{1}{B}｜Creature — Rat） — This creature gets +1/+0 for each other Rat you control. A deck can have any number of cards named Rat Colony.
  3. Thrumming Stone（{5}｜Legendary Artifact） — Spells you cast have ripple 4. (Whenever you cast a spell, you may reveal the top four cards of your library. You may cast spells with the same name as that spell from am
  4. Piper of the Swarm（{1}{B}｜Creature — Human Warlock） — Rats you control have menace. {1}{B}, {T}: Create a 1/1 black Rat creature token. {2}{B}{B}, {T}, Sacrifice three Rats: Gain control of target creature.
  5. Karumonix, the Rat King（{1}{B}{B}｜Legendary Creature — Phyrexian Rat） — Toxic 1 (Players dealt combat damage by this creature also get a poison counter.) Other Rats you control have toxic 1. When Karumonix enters, look at the top five cards o
  6. Ogre Slumlord（{3}{B}{B}｜Creature — Ogre Rogue） — Whenever another nontoken creature dies, you may create a 1/1 black Rat creature token. Rats you control have deathtouch.
- **出场率最高的牌**（大多数牌组都会放）
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Swarmyard（｜Land） — {T}: Add {C}. {T}: Regenerate target Insect, Rat, Spider, or Squirrel. (The next time it would be destroyed this turn, instead tap
  - Ashcoat of the Shadow Swarm（{3}{B}｜Legendary Creature — Rat Warlock） — Whenever Ashcoat attacks or blocks, other Rats you control get +X/+X until end of turn, where X is the number of Rats you control.
  - Cabal Coffers（｜Land） — {2}, {T}: Add {B} for each Swamp you control.


## Slicer, Hired Muscle // Slicer, High-Speed Antagonist ｜ 受雇狂徒切片
- 颜色 R ｜ 法术力值 5.0 ｜ 类型 Legendary Artifact Creature — Robot // Legendary Artifact — Vehicle
- 流行度：EDHREC 全时段第 569 位，约 5238 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 0.96 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $7.23
- 社区标签：装备、主将单挑、快攻、神器、强制战斗、锁场
- 完整牌面：More Than Meets the Eye {2}{R} (You may cast this card converted for {2}{R}.)
Double strike, haste
At the beginning of each opponent's upkeep, you may have that player gain control of Slicer until end of turn. If you do, untap Slicer, goad it, and it can't be sacrificed this turn. If you don't, convert it.
//
Living metal (During your turn, this Vehicle is also a creature.)
First strike, haste
Whenever Slicer deals combat damage to a player, convert it at end of combat.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mask of Memory（{2}｜Artifact — Equipment） — Whenever equipped creature deals combat damage to a player, you may draw two cards. If you do, discard a card. Equip {1} ({1}: Attach to target creature you control. Equi
  2. Beamtown Beatstick（{R}｜Artifact — Equipment） — Equipped creature gets +1/+0 and has menace. (It can't be blocked except by two or more creatures.) Whenever equipped creature deals combat damage to a player or battle, 
  3. Goldvein Pick（{2}｜Artifact — Equipment） — Equipped creature gets +1/+1. Whenever equipped creature deals combat damage to a player, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add 
  4. O-Naginata（{1}｜Artifact — Equipment） — This Equipment can be attached only to a creature with power 3 or greater. Equipped creature gets +3/+0 and has trample. Equip {2} ({2}: Attach to target creature you con
  5. Welding Jar（{0}｜Artifact） — Sacrifice this artifact: Regenerate target artifact.
  6. Jeska, Thrice Reborn（{2}{R}｜Legendary Planeswalker — Jeska） — Jeska enters with a loyalty counter on her for each time you've cast a commander from the command zone this game. 0: Choose target creature. Until your next turn, if that
- **出场率最高的牌**（大多数牌组都会放）
  - Simian Spirit Guide（{2}{R}｜Creature — Ape Spirit） — Exile this card from your hand: Add {R}.
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.
  - Desperate Ritual（{1}{R}｜Instant — Arcane） — Add {R}{R}{R}. Splice onto Arcane {1}{R} (As you cast an Arcane spell, you may reveal this card from your hand and pay its splice 
  - Abrade（{1}{R}｜Instant） — Choose one — • Abrade deals 3 damage to target creature. • Destroy target artifact.


## Kozilek, the Great Distortion ｜ 无际曲相寇基雷
- 颜色 C ｜ 法术力值 10.0 ｜ 类型 Legendary Creature — Eldrazi
- 流行度：EDHREC 全时段第 570 位，约 5176 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.36 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.25
- 社区标签：奥札奇、神器、加速、爆费、组合技、控制
- 完整牌面：When you cast this spell, if you have fewer than seven cards in hand, draw cards equal to the difference.
Menace
Discard a card with mana value X: Counter target spell with mana value X.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Eldrazi Temple（｜Land） — {T}: Add {C}. {T}: Add {C}{C}. Spend this mana only to cast colorless Eldrazi spells or activate abilities of colorless Eldrazi.
  2. Geode Golem（{5}｜Artifact Creature — Golem） — Trample Whenever this creature deals combat damage to a player, you may cast your commander from the command zone without paying its mana cost. (You still pay any additio
  3. Conduit of Ruin（{6}｜Creature — Eldrazi） — When you cast this spell, you may search your library for a colorless creature card with mana value 7 or greater, reveal it, then shuffle and put that card on top. The fi
  4. Sanctum of Ugin（｜Land） — {T}: Add {C}. Whenever you cast a colorless spell with mana value 7 or greater, you may sacrifice this land. If you do, search your library for a colorless creature card,
  5. Eye of Ugin（｜Legendary Land） — Colorless Eldrazi spells you cast cost {2} less to cast. {7}, {T}: Search your library for a colorless creature card, reveal it, put it into your hand, then shuffle.
  6. Ulamog, the Ceaseless Hunger（{10}｜Legendary Creature — Eldrazi） — When you cast this spell, exile two target permanents. Indestructible Whenever Ulamog attacks, defending player exiles the top twenty cards of their library.
- **出场率最高的牌**（大多数牌组都会放）
  - All Is Dust（{7}｜Kindred Sorcery — Eldrazi） — Each player sacrifices all permanents they control that are one or more colors.
  - Forsaken Monument（{5}｜Legendary Artifact） — Colorless creatures you control get +2/+2. Whenever you tap a permanent for {C}, add an additional {C}. Whenever you cast a colorl
  - Thran Dynamo（{4}｜Artifact） — {T}: Add {C}{C}{C}.
  - Hedron Archive（{4}｜Artifact） — {T}: Add {C}{C}. {2}, {T}, Sacrifice this artifact: Draw two cards.


## Savra, Queen of the Golgari ｜ 葛加理女王撒芙儿
- 颜色 BG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Elf Shaman
- 流行度：EDHREC 全时段第 573 位，约 5138 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.31 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $7.84
- 社区标签：牺牲流、牺牲、衍生物、生命增益、坟场复活、控制
- 完整牌面：Whenever you sacrifice a black creature, you may pay 2 life. If you do, each other player sacrifices a creature of their choice.
Whenever you sacrifice a green creature, you may gain 2 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Creakwood Liege（{1}{B/G}{B/G}{B/G}｜Creature — Horror） — Other black creatures you control get +1/+1. Other green creatures you control get +1/+1. At the beginning of your upkeep, you may create a 1/1 black and green Worm creat
  2. Dina, Soul Steeper（{B}{G}｜Legendary Creature — Dryad Druid） — Whenever you gain life, each opponent loses 1 life. {1}, Sacrifice another creature: Dina gets +X/+0 until end of turn, where X is the sacrificed creature's power.
  3. Viscera Seer（{B}｜Creature — Vampire Wizard） — Sacrifice a creature: Scry 1. (Look at the top card of your library. You may put that card on the bottom.)
  4. Reassembling Skeleton（{1}{B}｜Creature — Skeleton Warrior） — {1}{B}: Return this card from your graveyard to the battlefield tapped.
  5. Beledros Witherbloom（{5}{B}{G}｜Legendary Creature — Elder Dragon） — Flying At the beginning of each upkeep, create a 1/1 black and green Pest creature token with "When this token dies, you gain 1 life." Pay 10 life: Untap all lands you co
  6. Blight Mound（{2}{B}｜Enchantment） — Attacking Pests you control get +1/+0 and have menace. Whenever a nontoken creature you control dies, create a 1/1 black and green Pest creature token with "When this tok
- **出场率最高的牌**（大多数牌组都会放）
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Sakura-Tribe Elder（{1}{G}｜Creature — Snake Shaman） — Sacrifice this creature: Search your library for a basic land card, put that card onto the battlefield tapped, then shuffle.
  - Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
  - Zulaport Cutthroat（{1}{B}｜Creature — Human Rogue Ally） — Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life.


## Ultron, Artificial Malevolence ｜ 人工恶意奥创
- 颜色 C ｜ 法术力值 3.0 ｜ 类型 Legendary Artifact Creature — Robot Villain
- 流行度：EDHREC 全时段第 574 位，约 5138 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $7.08
- 社区标签：神器、衍生物、复制、组合技、神器共鸣、加速
- 完整牌面：Whenever another nontoken artifact you control enters, you may pay {2}. If you do, create a token that's a copy of it. If the token isn't a creature, it becomes a 2/2 Robot Villain creature in addition to its other types.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Idol of Oblivion（{2}｜Artifact） — {T}: Draw a card. Activate only if you created a token this turn. {8}, {T}, Sacrifice this artifact: Create a 10/10 colorless Eldrazi creature token.
  2. Krang, Utrom Warlord（{9}｜Legendary Artifact Creature — Utrom Robot） — Flying, trample, indestructible, haste Other artifact creatures you control have flying, trample, indestructible, and haste.
  3. Cybermen Squadron（{7}｜Artifact Creature — Cyberman） — Nonlegendary artifact creatures you control have myriad. (Whenever a creature with myriad attacks, for each opponent other than defending player, you may create a token c
  4. Cloud Key（{3}｜Artifact） — As this artifact enters, choose artifact, creature, enchantment, instant, or sorcery. Spells you cast of the chosen type cost {1} less to cast.
  5. Cyberman Patrol（{2}｜Artifact Creature — Cyberman） — Artifact creatures you control have afflict 3. (Whenever a creature with afflict 3 becomes blocked, defending player loses 3 life.)
  6. Iron Spider, Stark Upgrade（{3}｜Legendary Artifact Creature — Spider Hero） — Vigilance {T}: Put a +1/+1 counter on each artifact creature and/or Vehicle you control. {2}, Remove two +1/+1 counters from among artifacts you control: Draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Foundry Inspector（{3}｜Artifact Creature — Construct） — Artifact spells you cast cost {1} less to cast.
  - Forsaken Monument（{5}｜Legendary Artifact） — Colorless creatures you control get +2/+2. Whenever you tap a permanent for {C}, add an additional {C}. Whenever you cast a colorl
  - Thran Dynamo（{4}｜Artifact） — {T}: Add {C}{C}{C}.
  - Urza's Power Plant（｜Land — Urza's Power-Plant） — {T}: Add {C}. If you control an Urza's Mine and an Urza's Tower, add {C}{C} instead.


## Liberty Prime, Recharged ｜ 满电自由至尊
- 颜色 WUR ｜ 法术力值 5.0 ｜ 类型 Legendary Artifact Creature — Robot
- 流行度：EDHREC 全时段第 575 位，约 5118 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.22 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：能量、神器、主将单挑、装备、衍生物、快攻
- 完整牌面：Vigilance, trample, haste
Whenever Liberty Prime attacks or blocks, sacrifice it unless you pay {E}{E} (two energy counters).
{2}, {T}, Sacrifice an artifact: You get {E}{E} and draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Dr. Madison Li（{U}{R}{W}｜Legendary Creature — Human Scientist） — Whenever you cast an artifact spell, you get {E} (an energy counter). {T}, Pay {E}: Target creature gets +1/+0 and gains trample and haste until end of turn. {T}, Pay {E}
  2. Electrosiphon（{U}{U}{R}｜Instant） — Counter target spell. You get an amount of {E} (energy counters) equal to its mana value.
  3. Plasma Caster（{1}{R}｜Artifact — Equipment） — Equipped creature gets +1/+1. Whenever equipped creature attacks, you get {E}{E} (two energy counters). Pay {E}{E}: Choose target creature that's blocking equipped creatu
  4. HELIOS One（｜Land） — {T}: Add {C}. {1}, {T}: You get {E} (an energy counter). {3}, {T}, Pay X {E}, Sacrifice this land: Destroy target nonland permanent with mana value X. Activate only as a 
  5. Assaultron Dominator（{1}{R}｜Artifact Creature — Robot） — When this creature enters, you get {E}{E} (two energy counters). Whenever an artifact creature you control attacks, you may pay {E}. If you do, put your choice of a +1/+1
  6. Automated Assembly Line（{1}{W}｜Artifact） — Whenever one or more artifact creatures you control deal combat damage to a player, you get {E} (an energy counter). Pay {E}{E}{E}: Create a tapped 3/3 colorless Robot ar
- **出场率最高的牌**（大多数牌组都会放）
  - Mystic Monastery（｜Land） — This land enters tapped. {T}: Add {U}, {R}, or {W}.
  - Dispatch（{W}｜Instant） — Tap target creature. Metalcraft — If you control three or more artifacts, exile that creature.
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Brotherhood Scribe（{1}{W}｜Creature — Human Artificer） — Metalcraft — {T}: You get {E} (an energy counter). Activate only if you control three or more artifacts. Whenever you get one or m


## Grub, Storied Matriarch // Grub, Notorious Auntie ｜ 盛誉族母寻宝
- 颜色 BR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Goblin Warlock // Legendary Creature — Goblin Warrior
- 流行度：EDHREC 全时段第 576 位，约 5115 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.37
- 社区标签：鬼怪、衍生物、牺牲流、快攻、坟场复活、－1/－1 指示物
- 完整牌面：Menace
Whenever this creature enters or transforms into Grub, Storied Matriarch, return up to one target Goblin card from your graveyard to your hand.
At the beginning of your first main phase, you may pay {R}. If you do, transform Grub.
//
Menace
Whenever Grub attacks, you may blight 1. If you do, create a tapped and attacking token that's a copy of the blighted creature, except it has "At the beginning of the end step, sacrifice this token."
At the beginning of your first main phase, you may pay {B}. If you do, transform Grub.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Boggart Cursecrafter（{B}{R}｜Creature — Goblin Warlock） — Deathtouch Whenever another Goblin you control dies, this creature deals 1 damage to each opponent.
  2. Boggart Mischief（{2}{B}｜Kindred Enchantment — Goblin） — When this enchantment enters, you may blight 1. If you do, create two 1/1 black and red Goblin creature tokens. (To blight 1, put a -1/-1 counter on a creature you contro
  3. Krenko, Mob Boss（{2}{R}{R}｜Legendary Creature — Goblin Warrior） — {T}: Create X 1/1 red Goblin creature tokens, where X is the number of Goblins you control.
  4. Eclipsed Boggart（{B/R}{B/R}{B/R}｜Creature — Goblin Scout） — When this creature enters, look at the top four cards of your library. You may reveal a Goblin, Swamp, or Mountain card from among them and put it into your hand. Put the
  5. Goblin Matron（{2}{R}｜Creature — Goblin） — When this creature enters, you may search your library for a Goblin card, reveal that card, put it into your hand, then shuffle.
  6. Skirk Prospector（{R}｜Creature — Goblin） — Sacrifice a Goblin: Add {R}.
- **出场率最高的牌**（大多数牌组都会放）
  - Goblin Warchief（{1}{R}{R}｜Creature — Goblin Warrior） — Goblin spells you cast cost {1} less to cast. Goblins you control have haste.
  - Grub's Command（{3}{B}{R}｜Kindred Sorcery — Goblin） — Choose two — • Create a token that's a copy of target Goblin you control. • Creatures target player controls get +1/+1 and gain ha
  - Sling-Gang Lieutenant（{3}{B}｜Creature — Goblin） — When this creature enters, create two 1/1 red Goblin creature tokens. Sacrifice a Goblin: Target player loses 1 life and you gain 
  - Siege-Gang Commander（{3}{R}{R}｜Creature — Goblin） — When this creature enters, create three 1/1 red Goblin creature tokens. {1}{R}, Sacrifice a Goblin: This creature deals 2 damage t


## The Council of Four ｜ 四人议会
- 颜色 WU ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Noble
- 流行度：EDHREC 全时段第 577 位，约 5104 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.49 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $4.39
- 社区标签：换手牌、衍生物、群体恩惠、控制、抽牌、骑士
- 完整牌面：Whenever a player draws their second card during their turn, you draw a card.
Whenever a player casts their second spell during their turn, you create a 2/2 white Knight creature token.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Howling Mine（{2}｜Artifact） — At the beginning of each player's draw step, if this artifact is untapped, that player draws an additional card.
  2. Dictate of Kruphix（{1}{U}{U}｜Enchantment） — Flash (You may cast this spell any time you could cast an instant.) At the beginning of each player's draw step, that player draws an additional card.
  3. Kami of the Crescent Moon（{U}{U}｜Legendary Creature — Spirit） — At the beginning of each player's draw step, that player draws an additional card.
  4. Vodalian Wave-Knight（{2}{W}{U}｜Creature — Merfolk Knight） — Whenever you draw a card, put a +1/+1 counter on each other Merfolk and/or Knight you control.
  5. Mangara, the Diplomat（{3}{W}｜Legendary Creature — Human Cleric） — Lifelink Whenever an opponent attacks with creatures, if two or more of those creatures are attacking you and/or planeswalkers you control, draw a card. Whenever an oppon
  6. Prince Imrahil the Fair（{W}{U}｜Legendary Creature — Human Noble） — Whenever you draw your second card each turn, create a 1/1 white Human Soldier creature token.
- **出场率最高的牌**（大多数牌组都会放）
  - Prairie Stream（｜Land — Plains Island） — ({T}: Add {W} or {U}.) This land enters tapped unless you control two or more basic lands.
  - Glacial Fortress（｜Land） — This land enters tapped unless you control a Plains or an Island. {T}: Add {W} or {U}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Azorius Signet（{2}｜Artifact） — {1}, {T}: Add {W}{U}.


## Alesha, Who Laughs at Fate ｜ 嘲命者阿列莎
- 颜色 BR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Warrior
- 流行度：EDHREC 全时段第 578 位，约 5097 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.3 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.42
- 社区标签：坟场复活、牺牲流、快攻、牺牲、宝物、＋1/＋1 指示物
- 完整牌面：First strike
Whenever Alesha attacks, put a +1/+1 counter on it.
Raid — At the beginning of your end step, if you attacked this turn, return target creature card with mana value less than or equal to Alesha's power from your graveyard to the battlefield.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Accursed Marauder（{1}{B}｜Creature — Zombie Warrior） — When this creature enters, each player sacrifices a nontoken creature of their choice.
  2. Perforating Artist（{1}{B}{R}｜Creature — Devil） — Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.) Raid — At the beginning of your end step, if you attacked this turn, each opponent los
  3. Inti, Seneschal of the Sun（{1}{R}｜Legendary Creature — Human Knight） — Whenever you attack, you may discard a card. When you do, put a +1/+1 counter on target attacking creature. It gains trample until end of turn. Whenever you discard one o
  4. Buried Alive（{2}{B}｜Sorcery） — Search your library for up to three creature cards, put them into your graveyard, then shuffle.
  5. Plaguecrafter（{2}{B}｜Creature — Human Shaman） — When this creature enters, each player sacrifices a creature or planeswalker of their choice. Each player who can't discards a card.
  6. Stitcher's Supplier（{B}｜Creature — Zombie） — When this creature enters or dies, mill three cards. (Put the top three cards of your library into your graveyard.)
- **出场率最高的牌**（大多数牌组都会放）
  - Smoldering Marsh（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) This land enters tapped unless you control two or more basic lands.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Faithless Looting（{R}｜Sorcery） — Draw two cards, then discard two cards. Flashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then 
  - Victimize（{2}{B}｜Sorcery） — Choose two target creature cards in your graveyard. Sacrifice a creature. If you do, return the chosen cards to the battlefield ta


## Lonis, Cryptozoologist ｜ 隐匿动物学家罗尼斯
- 颜色 UG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Snake Elf Scout
- 流行度：EDHREC 全时段第 580 位，约 5087 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.25 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.33
- 社区标签：Clues、衍生物、神器、组合技、闪现回场、控制
- 完整牌面：Whenever another nontoken creature you control enters, investigate.
{T}, Sacrifice X Clues: Target opponent reveals the top X cards of their library. You may put a nonland permanent card with mana value X or less from among them onto the battlefield under your control. That player puts the rest on the bottom of their library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Academy Manufactor（{3}｜Artifact Creature — Assembly-Worker） — If you would create a Clue, Food, or Treasure token, instead create one of each.
  2. Shrieking Drake（{U}｜Creature — Drake） — Flying When this creature enters, return a creature you control to its owner's hand.
  3. Erdwal Illuminator（{1}{U}｜Creature — Spirit） — Flying Whenever you investigate for the first time each turn, investigate an additional time.
  4. Tireless Tracker（{2}{G}｜Creature — Human Scout） — Landfall — Whenever a land you control enters, investigate. (Create a Clue token. It's an artifact with "{2}, Sacrifice this token: Draw a card.") Whenever you sacrifice 
  5. Jaheira, Friend of the Forest（{2}{G}｜Legendary Creature — Human Elf Druid） — Tokens you control have "{T}: Add {G}." Choose a Background (You can have a Background as a second commander.)
  6. Inspiring Statuary（{3}｜Artifact） — Nonartifact spells you cast have improvise. (Your artifacts can help cast those spells. Each artifact you tap after you're done activating mana abilities pays for {1}.)
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Eternal Witness（{1}{G}{G}｜Creature — Human Shaman） — When this creature enters, you may return target card from your graveyard to your hand.
  - Yavimaya Coast（｜Land） — {T}: Add {C}. {T}: Add {G} or {U}. This land deals 1 damage to you.
  - Coiling Oracle（{G}{U}｜Creature — Snake Elf Druid） — When this creature enters, reveal the top card of your library. If it's a land card, put it onto the battlefield. Otherwise, put t


## Vishgraz, the Doomhive ｜ 末日繁生威袭瑰
- 颜色 WBG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Phyrexian Insect
- 流行度：EDHREC 全时段第 582 位，约 5069 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.72 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.43
- 社区标签：毒侵、非瑞人、衍生物、闪现回场、增殖、＋1/＋1 指示物
- 完整牌面：Menace, toxic 1 (Players dealt combat damage by this creature also get a poison counter.)
When Vishgraz enters, create three 1/1 colorless Phyrexian Mite artifact creature tokens with toxic 1 and "This token can't block."
Vishgraz gets +1/+1 for each poison counter your opponents have.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Infectious Inquiry（{2}{B}｜Sorcery） — You draw two cards and you lose 2 life. Each opponent gets a poison counter.
  2. Necrogen Rotpriest（{2}{B}{G}｜Creature — Phyrexian Zombie Cleric） — Toxic 2 (Players dealt combat damage by this creature also get two poison counters.) Whenever a creature you control with toxic deals combat damage to a player, that play
  3. Vraska's Fall（{2}{B}｜Instant） — Each opponent sacrifices a creature or planeswalker of their choice and gets a poison counter.
  4. Skrelv's Hive（{1}{W}｜Enchantment） — At the beginning of your upkeep, you lose 1 life and create a 1/1 colorless Phyrexian Mite artifact creature token with toxic 1 and "This token can't block." Corrupted — 
  5. Skrelv, Defector Mite（{W}｜Legendary Artifact Creature — Phyrexian Mite） — Toxic 1 (Players dealt combat damage by this creature also get a poison counter.) Skrelv can't block. {W/P}, {T}: Choose a color. Another target creature you control gain
  6. Venerated Rotpriest（{G}｜Creature — Phyrexian Druid） — Toxic 1 (Players dealt combat damage by this creature also get a poison counter.) Whenever a creature you control becomes the target of a spell, target opponent gets a po
- **出场率最高的牌**（大多数牌组都会放）
  - Phyresis Outbreak（{2}{B}｜Sorcery） — Each opponent gets a poison counter. Then each creature your opponents control gets -1/-1 until end of turn for each poison counte
  - Contaminant Grafter（{4}{G}｜Creature — Phyrexian Druid） — Trample, toxic 1 Whenever one or more creatures you control deal combat damage to one or more players, proliferate. Corrupted — At
  - White Sun's Twilight（{X}{W}{W}｜Sorcery） — You gain X life. Create X 1/1 colorless Phyrexian Mite artifact creature tokens with toxic 1 and "This token can't block." If X is
  - Bloated Contaminator（{2}{G}｜Creature — Phyrexian Beast） — Trample Toxic 1 (Players dealt combat damage by this creature also get a poison counter.) Whenever this creature deals combat dama


## Plagon, Lord of the Beach ｜ 滩涂之主普拉贡
- 颜色 WU ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Starfish Wizard
- 流行度：EDHREC 全时段第 583 位，约 5059 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.27 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：防御力核心、闪现回场、组合技、控制、抽牌、风暴
- 完整牌面：When Plagon enters, draw a card for each creature you control with toughness greater than its power.
{W/U}: Target creature you control assigns combat damage equal to its toughness rather than its power this turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ephemerate（{W}｜Instant） — Exile target creature you control, then return it to the battlefield under its owner's control. Rebound (If you cast this spell from your hand, exile it as it resolves. A
  2. Cloudshift（{W}｜Instant） — Exile target creature you control, then return that card to the battlefield under your control.
  3. Essence Flux（{U}｜Instant） — Exile target creature you control, then return that card to the battlefield under its owner's control. If it's a Spirit, put a +1/+1 counter on it.
  4. Ornithopter（{0}｜Artifact Creature — Thopter） — Flying
  5. Momentary Blink（{1}{W}｜Instant） — Exile target creature you control, then return it to the battlefield under its owner's control. Flashback {3}{U} (You may cast this card from your graveyard for its flash
  6. Dour Port-Mage（{1}{U}｜Creature — Frog Wizard） — Whenever one or more other creatures you control leave the battlefield without dying, draw a card. {1}{U}, {T}: Return another target creature you control to its owner's 
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Progress（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {U}. This artifact deals 1 damage to you.
  - Adarkar Wastes（｜Land） — {T}: Add {C}. {T}: Add {W} or {U}. This land deals 1 damage to you.
  - Ornithopter of Paradise（{2}｜Artifact Creature — Thopter） — Flying {T}: Add one mana of any color.
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Herigast, Erupting Nullkite ｜ 喷焰虚虐体赫厉轧
- 颜色 R ｜ 法术力值 9.0 ｜ 类型 Legendary Creature — Eldrazi Dragon
- 流行度：EDHREC 全时段第 584 位，约 5040 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.22 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.52
- 社区标签：奥札奇、神器、牺牲、偷取、爆费、快攻
- 完整牌面：Emerge {6}{R}{R} (You may cast this spell by sacrificing a creature and paying the emerge cost reduced by that creature's mana value.)
When you cast this spell, you may exile your hand. If you do, draw three cards.
Flying
Each creature spell you cast has emerge. The emerge cost is equal to its mana cost.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Artisan of Kozilek（{9}｜Creature — Eldrazi） — When you cast this spell, you may return target creature card from your graveyard to the battlefield. Annihilator 2 (Whenever this creature attacks, defending player sacr
  2. Hideous Taskmaster（{6}{R}｜Creature — Eldrazi） — Devoid (This card has no color.) When you cast this spell, for each opponent, gain control of up to one target creature that player controls until end of turn. Untap thos
  3. Solemn Simulacrum（{4}｜Artifact Creature — Golem） — When this creature enters, you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle. When this creature dies, you may dr
  4. Anticausal Vestige（{6}｜Creature — Eldrazi） — When this creature leaves the battlefield, draw a card, then you may put a permanent card with mana value less than or equal to the number of lands you control from your 
  5. Palladium Myr（{3}｜Artifact Creature — Myr） — {T}: Add {C}{C}.
  6. Skitterbeam Battalion（{9}｜Artifact Creature — Construct） — Prototype {3}{R}{R} — 2/2 (You may cast this spell with different mana cost, color, and size. It keeps its abilities and types.) Trample, haste When this creature enters,
- **出场率最高的牌**（大多数牌组都会放）
  - Anger（{3}{R}｜Creature — Incarnation） — Haste As long as this card is in your graveyard and you control a Mountain, creatures you control have haste.
  - Atsushi, the Blazing Sky（{2}{R}{R}｜Legendary Creature — Dragon Spirit） — Flying, trample When Atsushi dies, choose one — • Exile the top two cards of your library. Until the end of your next turn, you ma
  - Feldon of the Third Path（{1}{R}{R}｜Legendary Creature — Human Artificer） — {2}{R}, {T}: Create a token that's a copy of target creature card in your graveyard, except it's an artifact in addition to its ot
  - Combustible Gearhulk（{4}{R}{R}｜Artifact Creature — Construct） — First strike When this creature enters, target opponent may have you draw three cards. If the player doesn't, you mill three cards


## Odric, Lunarch Marshal ｜ 月主会元帅欧吉克
- 颜色 W ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Soldier
- 流行度：EDHREC 全时段第 585 位，约 5038 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.35 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.97
- 社区标签：Keywords、快攻、生命增益、装备、衍生物、飞行
- 完整牌面：At the beginning of each combat, creatures you control gain first strike until end of turn if a creature you control has first strike. The same is true for flying, deathtouch, double strike, haste, hexproof, indestructible, lifelink, menace, reach, skulk, trample, and vigilance.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Aerial Responder（{1}{W}{W}｜Creature — Dwarf Soldier） — Flying, vigilance, lifelink
  2. Shrike Force（{2}{W}｜Creature — Bird Knight） — Flying, double strike, vigilance
  3. Zetalpa, Primal Dawn（{6}{W}{W}｜Legendary Creature — Elder Dinosaur） — Flying, double strike, vigilance, trample, indestructible
  4. Oketra the True（{3}{W}｜Legendary Creature — God） — Double strike, indestructible Oketra can't attack or block unless you control at least three other creatures. {3}{W}: Create a 1/1 white Warrior creature token with vigil
  5. Healer's Hawk（{W}｜Creature — Bird） — Flying Lifelink (Damage dealt by this creature also causes you to gain that much life.)
  6. Akroma, Vision of Ixidor（{5}{W}{W}｜Legendary Creature — Angel） — Flying, first strike, vigilance, trample At the beginning of each combat, until end of turn, each other creature you control gets +1/+1 if it has flying, +1/+1 if it has 
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Danitha Capashen, Paragon（{2}{W}｜Legendary Creature — Human Knight） — First strike, vigilance, lifelink Aura and Equipment spells you cast cost {1} less to cast.
  - Pearl Medallion（{2}｜Artifact） — White spells you cast cost {1} less to cast.
  - Oketra's Monument（{3}｜Legendary Artifact） — White creature spells you cast cost {1} less to cast. Whenever you cast a creature spell, create a 1/1 white Warrior creature toke


## Black Waltz No. 3 ｜ 黑色华尔兹3号
- 颜色 BR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Wizard
- 流行度：EDHREC 全时段第 588 位，约 5019 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.35 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.37
- 社区标签：烧血、法术连发、群体折磨、毒侵、法师、组合技
- 完整牌面：Flying, deathtouch
Whenever you cast a noncreature spell, Black Waltz No. 3 deals 2 damage to each opponent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Black Mage's Rod（{1}{B}｜Artifact — Equipment） — Job select (When this Equipment enters, create a 1/1 colorless Hero creature token, then attach this to it.) Equipped creature gets +1/+0, has "Whenever you cast a noncre
  2. Cornered by Black Mages（{1}{B}{B}｜Sorcery） — Target opponent sacrifices a creature of their choice. Create a 0/1 black Wizard creature token with "Whenever you cast a noncreature spell, this token deals 1 damage to 
  3. Kuja, Genome Sorcerer（｜） — 
  4. Guttersnipe（{2}{R}｜Creature — Goblin Shaman） — Whenever you cast an instant or sorcery spell, this creature deals 2 damage to each opponent.
  5. Circle of Power（{3}{B}｜Sorcery） — You draw two cards and you lose 2 life. Create a 0/1 black Wizard creature token with "Whenever you cast a noncreature spell, this token deals 1 damage to each opponent."
  6. Coruscation Mage（{1}{R}｜Creature — Otter Wizard） — Offspring {2} (You may pay an additional {2} as you cast this spell. If you do, when this creature enters, create a 1/1 token copy of it.) Whenever you cast a noncreature
- **出场率最高的牌**（大多数牌组都会放）
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Lightning Bolt（{R}｜Instant） — Lightning Bolt deals 3 damage to any target.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.
  - Faithless Looting（{R}｜Sorcery） — Draw two cards, then discard two cards. Flashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then 


## Tinybones, Trinket Thief ｜ 琐物窃贼细骨
- 颜色 B ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Skeleton Rogue
- 流行度：EDHREC 全时段第 589 位，约 5018 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.1 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $16.01
- 社区标签：弃牌、控制、锁场、组合技、坟场复活、群体折磨
- 完整牌面：At the beginning of each end step, if an opponent discarded a card this turn, you draw a card and you lose 1 life.
{4}{B}{B}: Each opponent with no cards in hand loses 10 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Waste Not（{1}{B}｜Enchantment） — Whenever an opponent discards a creature card, create a 2/2 black Zombie creature token. Whenever an opponent discards a land card, add {B}{B}. Whenever an opponent disca
  2. Bottomless Pit（{1}{B}{B}｜Enchantment） — At the beginning of each player's upkeep, that player discards a card at random.
  3. Geth's Grimoire（{4}｜Artifact — Book） — Whenever an opponent discards a card, you may draw a card.
  4. Necrogen Mists（{2}{B}｜Enchantment） — At the beginning of each player's upkeep, that player discards a card.
  5. Oppression（{1}{B}{B}｜Enchantment） — Whenever a player casts a spell, that player discards a card.
  6. Liliana's Caress（{1}{B}｜Enchantment） — Whenever an opponent discards a card, that player loses 2 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Syphon Mind（{3}{B}｜Sorcery） — Each other player discards a card. You draw a card for each card discarded this way.
  - Painful Quandary（{3}{B}{B}｜Enchantment） — Whenever an opponent casts a spell, that player loses 5 life unless they discard a card.
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.


## Toph, Earthbending Master ｜ 运土宗师拓芙
- 颜色 G ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Warrior Ally
- 流行度：EDHREC 全时段第 590 位，约 5013 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $38.13
- 社区标签：地牌核心、＋1/＋1 指示物、地落、运土、加速、Land Animation
- 完整牌面：Landfall — Whenever a land you control enters, you get an experience counter.
Whenever you attack, earthbend X, where X is the number of experience counters you have. (Target land you control becomes a 0/0 creature with haste that's still a land. Put X +1/+1 counters on it. When it dies or is exiled, return it to the battlefield tapped.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Earthbender Ascension（{2}{G}｜Enchantment） — When this enchantment enters, earthbend 2. Then search your library for a basic land card, put it onto the battlefield tapped, then shuffle. Landfall — Whenever a land yo
  2. Ba Sing Se（｜Land） — This land enters tapped unless you control a basic land. {T}: Add {G}. {2}{G}, {T}: Earthbend 2. Activate only as a sorcery. (Target land you control becomes a 0/0 creatu
  3. Avatar Kyoshi, Earthbender（{5}{G}{G}{G}｜Legendary Creature — Human Avatar） — During your turn, Avatar Kyoshi has hexproof. At the beginning of combat on your turn, earthbend 8, then untap that land. (Target land you control becomes a 0/0 creature 
  4. Badgermole（{4}{G}｜Creature — Badger Mole） — When this creature enters, earthbend 2. (Target land you control becomes a 0/0 creature with haste that's still a land. Put two +1/+1 counters on it. When it dies or is e
  5. Toph, the Blind Bandit（{2}{G}｜Legendary Creature — Human Warrior Ally） — When Toph enters, earthbend 2. (Target land you control becomes a 0/0 creature with haste that's still a land. Put two +1/+1 counters on it. When it dies or is exiled, re
  6. The Legend of Kyoshi（｜） — 
- **出场率最高的牌**（大多数牌组都会放）
  - Evolution Sage（{2}{G}｜Creature — Elf Druid） — Landfall — Whenever a land you control enters, proliferate. (Choose any number of permanents and/or players, then give each anothe
  - Terrasymbiosis（{2}{G}｜Enchantment） — Whenever you put one or more +1/+1 counters on a creature you control, you may draw that many cards. Do this only once each turn.
  - Secret Tunnel（｜Land — Cave） — This land can't be blocked. {T}: Add {C}. {4}, {T}: Two target creatures you control that share a creature type can't be blocked t
  - Badgermole Cub（{1}{G}｜Creature — Badger Mole） — When this creature enters, earthbend 1. (Target land you control becomes a 0/0 creature with haste that's still a land. Put a +1/+


## Otharri, Suns' Glory ｜ 五阳荣光欧萨利
- 颜色 WR ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Phoenix
- 流行度：EDHREC 全时段第 591 位，约 5004 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.2 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $None
- 社区标签：衍生物、额外战斗、快攻、装备、经验指示物、烧血
- 完整牌面：Flying, lifelink, haste
Whenever Otharri attacks, you get an experience counter. Then create a 2/2 red Rebel creature token that's tapped and attacking for each experience counter you have.
{2}{R}{W}, Tap an untapped Rebel you control: Return this card from your graveyard to the battlefield tapped.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Neyali, Suns' Vanguard（{2}{R}{W}｜Legendary Creature — Human Rebel） — Attacking tokens you control have double strike. Whenever one or more tokens you control attack a player, exile the top card of your library. During any turn you attacked
  2. Goldnight Commander（{3}{W}｜Creature — Human Cleric Soldier） — Whenever another creature you control enters, creatures you control get +1/+1 until end of turn.
  3. Karn's Bastion（｜Land） — {T}: Add {C}. {4}, {T}: Proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)
  4. Idol of Oblivion（{2}｜Artifact） — {T}: Draw a card. Activate only if you created a token this turn. {8}, {T}, Sacrifice this artifact: Create a 10/10 colorless Eldrazi creature token.
  5. Warleader's Call（{1}{R}{W}｜Enchantment） — Creatures you control get +1/+1. Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  6. Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
- **出场率最高的牌**（大多数牌组都会放）
  - Talisman of Conviction（{2}｜Artifact） — {T}: Add {C}. {T}: Add {R} or {W}. This artifact deals 1 damage to you.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Boros Signet（{2}｜Artifact） — {1}, {T}: Add {R}{W}.
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
