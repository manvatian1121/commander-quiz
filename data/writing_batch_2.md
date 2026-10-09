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


## Rin and Seri, Inseparable ｜ 林恩与瑟黎永不离
- 颜色 WRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Dog Cat
- 流行度：EDHREC 全时段第 38 位，约 25093 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.5 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $32.53
- 社区标签：猫、衍生物、狗、＋1/＋1 指示物、生命增益、快攻
- 完整牌面：Whenever you cast a Dog spell, create a 1/1 green Cat creature token.
Whenever you cast a Cat spell, create a 1/1 white Dog creature token.
{R}{G}{W}, {T}: Rin and Seri deals damage to any target equal to the number of Dogs you control. You gain life equal to the number of Cats you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Regal Caracal（{3}{W}{W}｜Creature — Cat） — Other Cats you control get +1/+1 and have lifelink. (Damage dealt by those creatures also causes you to gain that much life.) When this creature enters, create two 1/1 wh
  2. Feline Sovereign（{2}{G}｜Creature — Cat） — Other Cats you control get +1/+1 and have protection from Dogs. Whenever one or more Cats you control deal combat damage to a player, destroy up to one target artifact or
  3. Pack Leader（{1}{W}｜Creature — Dog） — Other Dogs you control get +1/+1. Whenever this creature attacks, prevent all combat damage that would be dealt this turn to Dogs you control.
  4. Arahbo, the First Fang（{2}{W}｜Legendary Creature — Cat Avatar） — Other Cats you control get +1/+1. Whenever Arahbo or another nontoken Cat you control enters, create a 1/1 white Cat creature token.
  5. Jinnie Fay, Jetmir's Second（{R/G}{G}{G/W}｜Legendary Creature — Elf Druid） — If you would create one or more tokens, you may instead create that many 2/2 green Cat creature tokens with haste or that many 3/1 green Dog creature tokens with vigilanc
  6. King of the Pride（{2}{W}｜Creature — Cat） — Other Cats you control get +2/+1.
- **出场率最高的牌**（大多数牌组都会放）
  - Jetmir, Nexus of Revels（{1}{R}{G}{W}｜Legendary Creature — Cat Demon） — Creatures you control get +1/+0 and have vigilance as long as you control three or more creatures. Creatures you control also get 
  - Kutzil, Malamet Exemplar（{1}{G}{W}｜Legendary Creature — Cat Warrior） — Your opponents can't cast spells during your turn. Whenever one or more creatures you control each with power greater than its bas
  - Felidar Retreat（{3}{W}｜Enchantment） — Landfall — Whenever a land you control enters, choose one — • Create a 2/2 white Cat Beast creature token. • Put a +1/+1 counter o
  - Spirited Companion（{1}{W}｜Enchantment Creature — Dog） — When this creature enters, draw a card.


## Glarb, Calamity's Augur ｜ 灾祸卜算师格拉布
- 颜色 UBG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Frog Wizard Noble
- 流行度：EDHREC 全时段第 39 位，约 24476 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.36 ｜ 上手难度 2/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $4.16
- 社区标签：地牌核心、坟场复活、组合技、蛙、中速、加速
- 完整牌面：Deathtouch
You may look at the top card of your library any time.
You may play lands and cast spells with mana value 4 or greater from the top of your library.
{T}: Surveil 2.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Exploration（{G}｜Enchantment） — You may play an additional land on each of your turns.
  2. Culling Ritual（{2}{B}{G}｜Sorcery） — Destroy each nonland permanent with mana value 2 or less. Add {B} or {G} for each permanent destroyed this way.
  3. Valley Floodcaller（{2}{U}｜Creature — Otter Wizard） — Flash You may cast noncreature spells as though they had flash. Whenever you cast a noncreature spell, Birds, Frogs, Otters, and Rats you control get +1/+1 until end of t
  4. Enhanced Surveillance（{1}{U}｜Enchantment） — You may look at an additional two cards each time you surveil. Exile this enchantment: Shuffle your graveyard into your library.
  5. Sensei's Divining Top（{1}｜Artifact） — {1}: Look at the top three cards of your library, then put them back in any order. {T}: Draw a card, then put this artifact on top of its owner's library.
  6. The Gitrog Monster（{3}{B}{G}｜Legendary Creature — Frog Horror） — Deathtouch At the beginning of your upkeep, sacrifice The Gitrog Monster unless you sacrifice a land. You may play an additional land on each of your turns. Whenever one 
- **出场率最高的牌**（大多数牌组都会放）
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Polluted Delta（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for an Island or Swamp card, put it onto the battlefield, then shuffle.


## Animar, Soul of Elements ｜ 元素之魂阿尼玛
- 颜色 URG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Elemental
- 流行度：EDHREC 全时段第 40 位，约 23642 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.05 ｜ 上手难度 1/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $31.05
- 社区标签：＋1/＋1 指示物、组合技、加速、奥札奇、诞生荚、X 咒语
- 完整牌面：Protection from white and from black
Whenever you cast a creature spell, put a +1/+1 counter on Animar.
Creature spells you cast cost {1} less to cast for each +1/+1 counter on Animar.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Beast Whisperer（{2}{G}{G}｜Creature — Elf Druid） — Whenever you cast a creature spell, draw a card.
  2. Ancestral Statue（{4}｜Artifact Creature — Golem） — When this creature enters, return a nonland permanent you control to its owner's hand.
  3. Forgotten Ancient（{3}{G}｜Creature — Elemental） — Whenever a player casts a spell, you may put a +1/+1 counter on this creature. At the beginning of your upkeep, you may move any number of +1/+1 counters from this creatu
  4. Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  5. Soul of the Harvest（{4}{G}{G}｜Creature — Elemental） — Trample Whenever another nontoken creature you control enters, you may draw a card.
  6. Peregrine Drake（{4}{U}｜Creature — Drake） — Flying When this creature enters, untap up to five lands.
- **出场率最高的牌**（大多数牌组都会放）
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Steam Vents（｜Land — Island Mountain） — ({T}: Add {U} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Aragorn, the Uniter ｜ 重联君王阿拉贡
- 颜色 WURG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Noble
- 流行度：EDHREC 全时段第 41 位，约 23299 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.75 ｜ 上手难度 5/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $5.87
- 社区标签：传奇、人类、衍生物、多色核心、法术连发、史迹
- 完整牌面：Whenever you cast a white spell, create a 1/1 white Human Soldier creature token.
Whenever you cast a blue spell, scry 2.
Whenever you cast a red spell, Aragorn deals 3 damage to target opponent.
Whenever you cast a green spell, target creature gets +4/+4 until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Éowyn, Shieldmaiden（{2}{U}{R}{W}｜Legendary Creature — Human Knight） — First strike At the beginning of combat on your turn, if another Human entered the battlefield under your control this turn, create two 2/2 red Human Knight creature toke
  2. Aragorn, King of Gondor（{1}{U}{R}{W}｜Legendary Creature — Human Noble） — Vigilance, lifelink When Aragorn enters, you become the monarch. Whenever Aragorn attacks, up to one target creature can't block this turn. If you're the monarch, creatur
  3. Théoden, King of Rohan（{1}{R}{W}｜Legendary Creature — Human Noble） — Whenever Théoden or another Human you control enters, target creature gains double strike until end of turn.
  4. Pippin, Guard of the Citadel（{W}{U}｜Legendary Creature — Halfling Soldier） — Vigilance, ward {1} {T}: Another target creature you control gains protection from the card type of your choice until end of turn. (It can't be blocked, targeted, dealt d
  5. General Ferrous Rokiric（{1}{R}{W}｜Legendary Creature — Human Soldier） — Hexproof from monocolored Whenever you cast a multicolored spell, create a 4/4 red and white Golem artifact creature token.
  6. Boromir, Warden of the Tower（{2}{W}｜Legendary Creature — Human Soldier） — Vigilance Whenever an opponent casts a spell, if no mana was spent to cast it, counter that spell. Sacrifice Boromir: Creatures you control gain indestructible until end 
- **出场率最高的牌**（大多数牌组都会放）
  - Annie Joins Up（{1}{R}{G}{W}｜Legendary Enchantment） — When Annie Joins Up enters, it deals 5 damage to target creature or planeswalker an opponent controls. If a triggered ability of a
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Boros Charm（{R}{W}｜Instant） — Choose one — • Boros Charm deals 4 damage to target player or planeswalker. • Permanents you control gain indestructible until end
  - Growth Spiral（{G}{U}｜Instant） — Draw a card. You may put a land card from your hand onto the battlefield.


## Arcades, the Strategist ｜ 智龙阿卡迪
- 颜色 WUG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Elder Dragon
- 流行度：EDHREC 全时段第 42 位，约 23277 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.82 ｜ 上手难度 2/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $3.87
- 社区标签：防御力核心、守军、快攻、抽牌、铁壁防守、中速
- 完整牌面：Flying, vigilance
Whenever a creature you control with defender enters, draw a card.
Each creature you control with defender assigns combat damage equal to its toughness rather than its power and can attack as though it didn't have defender.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Overgrown Battlement（{1}{G}｜Creature — Wall） — Defender {T}: Add {G} for each creature you control with defender.
  2. Wall of Denial（{1}{W}{U}｜Creature — Wall） — Defender, flying Shroud (This creature can't be the target of spells or abilities.)
  3. Axebane Guardian（{2}{G}｜Creature — Human Druid） — Defender {T}: Add X mana in any combination of colors, where X is the number of creatures you control with defender.
  4. Tetsuko Umezawa, Fugitive（{1}{U}｜Legendary Creature — Human Rogue） — Creatures you control with power or toughness 1 or less can't be blocked.
  5. Wall of Blossoms（{1}{G}｜Creature — Plant Wall） — Defender When this creature enters, draw a card.
  6. High Alert（{1}{W}{U}｜Enchantment） — Each creature you control assigns combat damage equal to its toughness rather than its power. Creatures you control can attack as though they didn't have defender. {2}{W}
- **出场率最高的牌**（大多数牌组都会放）
  - Wall of Omens（{1}{W}｜Creature — Wall） — Defender When this creature enters, draw a card.
  - Stalwart Shield-Bearers（{1}{W}｜Creature — Human Soldier） — Defender Other creatures you control with defender get +0/+2.
  - The Pride of Hull Clade（{10}{G}｜Legendary Creature — Crocodile Elk Turtle） — This spell costs {X} less to cast, where X is the total toughness of creatures you control. Defender {2}{U}{U}: Until end of turn,
  - Sunscape Familiar（{1}{W}｜Creature — Wall） — Defender (This creature can't attack.) Green spells and blue spells you cast cost {1} less to cast.


## Ygra, Eater of All ｜ 万生噬兽依格拉
- 颜色 BG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Elemental Cat
- 流行度：EDHREC 全时段第 43 位，约 23028 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.93 ｜ 上手难度 3/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $12.31
- 社区标签：牺牲、衍生物、牺牲流、＋1/＋1 指示物、食品、神器
- 完整牌面：Ward—Sacrifice a Food.
Other creatures are Food artifacts in addition to their other types and have "{2}, {T}, Sacrifice this permanent: You gain 3 life."
Whenever a Food is put into a graveyard from the battlefield, put two +1/+1 counters on Ygra.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Camellia, the Seedmiser（{1}{B}{G}｜Legendary Creature — Squirrel Warlock） — Menace Other Squirrels you control have menace. Whenever you sacrifice one or more Foods, create a 1/1 green Squirrel creature token. {2}, Forage: Put a +1/+1 counter on 
  2. Experimental Confectioner（{2}{B}｜Creature — Human Peasant） — When this creature enters, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.") Whenever you sacrifice a Food, create a 1/1 bla
  3. Cauldron Familiar（{B}｜Creature — Cat） — When this creature enters, each opponent loses 1 life and you gain 1 life. Sacrifice a Food: Return this card from your graveyard to the battlefield.
  4. Peregrin Took（{2}{G}｜Legendary Creature — Halfling Citizen） — If one or more tokens would be created under your control, those tokens plus an additional Food token are created instead. (It's an artifact with "{2}, {T}, Sacrifice thi
  5. Savvy Hunter（{1}{B}{G}｜Creature — Human Warrior） — Whenever this creature attacks or blocks, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.") Sacrifice two Foods: Draw a card
  6. Gilded Goose（{G}｜Creature — Bird） — Flying When this creature enters, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.") {1}{G}, {T}: Create a Food token. {T}, S
- **出场率最高的牌**（大多数牌组都会放）
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Chatterfang, Squirrel General（{2}{G}｜Legendary Creature — Squirrel Warrior） — Forestwalk (This creature can't be blocked as long as defending player controls a Forest.) If one or more tokens would be created 
  - Night of the Sweets' Revenge（{3}{G}｜Enchantment） — When this enchantment enters, create a Food token. (It's an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life.") Food
  - Academy Manufactor（{3}｜Artifact Creature — Assembly-Worker） — If you would create a Clue, Food, or Treasure token, instead create one of each.


## Maralen, Fae Ascendant ｜ 化身仙儿的马拉兰
- 颜色 UBG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Elf Faerie Noble
- 流行度：EDHREC 全时段第 44 位，约 22999 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 4/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.30
- 社区标签：妖精、仙灵、偷取、衍生物、组合技、飞行
- 完整牌面：Flying
Whenever Maralen or another Elf or Faerie you control enters, exile the top two cards of target opponent's library.
Once each turn, you may cast a spell with mana value less than or equal to the number of Elves and Faeries you control from among cards exiled with Maralen this turn without paying its mana cost.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. High Fae Trickster（{3}{U}｜Creature — Faerie Wizard） — Flash (You may cast this spell any time you could cast an instant.) Flying You may cast spells as though they had flash.
  2. Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  3. Bitterbloom Bearer（{B}{B}｜Creature — Faerie Rogue） — Flash Flying At the beginning of your upkeep, you lose 1 life and create a 1/1 blue and black Faerie creature token with flying.
  4. Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  5. Bitterblossom（{1}{B}｜Kindred Enchantment — Faerie） — At the beginning of your upkeep, you lose 1 life and create a 1/1 black Faerie Rogue creature token with flying.
  6. Obyra, Dreaming Duelist（{U}{B}｜Legendary Creature — Faerie Warrior） — Flash Flying Whenever another Faerie you control enters, each opponent loses 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Bloom Tender（{1}{G}｜Creature — Elf Druid） — Vivid — {T}: For each color among permanents you control, add one mana of that color.
  - Priest of Titania（{1}{G}｜Creature — Elf Druid） — {T}: Add {G} for each Elf on the battlefield.


## Mr. House, President and CEO ｜ 总裁兼执行官豪斯先生
- 颜色 WBR ｜ 法术力值 3.0 ｜ 类型 Legendary Artifact Creature — Human
- 流行度：EDHREC 全时段第 45 位，约 22962 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.88 ｜ 上手难度 3/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $None
- 社区标签：宝物、衍生物、神器、掷骰、游乐设施、混乱
- 完整牌面：Whenever you roll a 4 or higher, create a 3/3 colorless Robot artifact creature token. If you rolled 6 or higher, instead create that token and a Treasure token.
{4}, {T}: Roll a six-sided die plus an additional six-sided die for each mana from Treasures spent to activate this ability.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Barbarian Class（{R}｜Enchantment — Class） — (Gain the next level as a sorcery to add its ability.) If you would roll one or more dice, instead roll that many dice plus one and ignore the lowest roll. {1}{R}: Level 
  2. Wyll, Blade of Frontiers（{1}{R}｜Legendary Creature — Human Warlock） — If you would roll one or more dice, instead roll that many dice plus one and ignore the lowest roll. Whenever you roll one or more dice, put a +1/+1 counter on Wyll. Choo
  3. Vexing Puzzlebox（{3}｜Artifact） — Whenever you roll one or more dice, put a number of charge counters on this artifact equal to the result. {T}: Add one mana of any color. Roll a d20. {T}, Remove 100 char
  4. Contraband Livestock（{1}{W}｜Instant） — Exile target creature, then roll a d20. 1—9 | Its controller creates a 4/4 green Ox creature token. 10—19 | Its controller creates a 2/2 green Boar creature token. 20 | I
  5. Hoarding Ogre（{3}{R}｜Creature — Ogre） — Whenever this creature attacks, roll a d20. 1—9 | Create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.") 10—19 | Create 
  6. Wyll's Reversal（{2}{R}｜Instant） — Choose target spell or ability with one or more targets. Roll a d20 and add the greatest power among creatures you control. 1—14 | You may choose new targets for that spe
- **出场率最高的牌**（大多数牌组都会放）
  - Delina, Wild Mage（{3}{R}｜Legendary Creature — Elf Shaman） — Whenever Delina attacks, choose target creature you control, then roll a d20. 1—14 | Create a tapped and attacking token that's a 
  - Wand of Wonder（{3}{R}｜Artifact） — {4}, {T}: Roll a d20. Each opponent exiles cards from the top of their library until they exile an instant or sorcery card, then s
  - Component Pouch（{3}｜Artifact） — {T}, Remove a component counter from this artifact: Add two mana of different colors. {T}: Roll a d20. 1—9 | Put a component count
  - Myrkul's Edict（{1}{B}｜Sorcery） — Roll a d20. 1—9 | Choose an opponent. That player sacrifices a creature of their choice. 10—19 | Each opponent sacrifices a creatu


## Caesar, Legion's Emperor ｜ 军团皇帝凯撒
- 颜色 WBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Soldier
- 流行度：EDHREC 全时段第 46 位，约 22867 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.48 ｜ 上手难度 5/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $None
- 社区标签：衍生物、牺牲流、快攻、人类、士兵、烧血
- 完整牌面：Whenever you attack, you may sacrifice another creature. When you do, choose two —
• Create two 1/1 red and white Soldier creature tokens with haste that are tapped and attacking.
• You draw a card and you lose 1 life.
• Caesar deals damage equal to the number of creature tokens you control to target opponent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Bastion of Remembrance（{2}{B}｜Enchantment） — When this enchantment enters, create a 1/1 white Human Soldier creature token. Whenever a creature you control dies, each opponent loses 1 life and you gain 1 life.
  2. Secure the Wastes（{X}{W}｜Instant） — Create X 1/1 white Warrior creature tokens.
  3. Pitiless Plunderer（{3}{B}｜Creature — Human Pirate） — Whenever another creature you control dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")
  4. General's Enforcer（{W}{B}｜Creature — Human Soldier） — Legendary Humans you control have indestructible. {2}{W}{B}: Exile target card from a graveyard. If it was a creature card, create a 1/1 white Human Soldier creature toke
  5. Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  6. Martial Coup（{X}{W}{W}｜Sorcery） — Create X 1/1 white Soldier creature tokens. If X is 5 or more, destroy all other creatures.
- **出场率最高的牌**（大多数牌组都会放）
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Nomad Outpost（｜Land） — This land enters tapped. {T}: Add {R}, {W}, or {B}.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.


## The Necrobloom ｜ 死冥盛花
- 颜色 WBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Plant
- 流行度：EDHREC 全时段第 47 位，约 22861 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.65 ｜ 上手难度 4/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.32
- 社区标签：地牌核心、衍生物、挖掘、地落、坟场复活、加速
- 完整牌面：Landfall — Whenever a land you control enters, create a 0/1 green Plant creature token. If you control seven or more lands with different names, create a 2/2 black Zombie creature token instead.
Land cards in your graveyard have dredge 2. (You may return a land card from your graveyard to your hand and mill two cards instead of drawing a card.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. The Gitrog Monster（{3}{B}{G}｜Legendary Creature — Frog Horror） — Deathtouch At the beginning of your upkeep, sacrifice The Gitrog Monster unless you sacrifice a land. You may play an additional land on each of your turns. Whenever one 
  2. Wight of the Reliquary（{B}{G}｜Creature — Zombie Knight） — Vigilance This creature gets +1/+1 for each creature card in your graveyard. {T}, Sacrifice another creature: Search your library for a land card, put it onto the battlef
  3. Scute Swarm（{2}{G}｜Creature — Insect） — Landfall — Whenever a land you control enters, create a 1/1 green Insect creature token. If you control six or more lands, create a token that's a copy of this creature i
  4. Six（{2}{G}｜Legendary Creature — Treefolk） — Reach Whenever Six attacks, mill three cards. You may put a land card from among them into your hand. During your turn, nonland permanent cards in your graveyard have ret
  5. Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  6. Thalia and The Gitrog Monster（{1}{W}{B}{G}｜Legendary Creature — Human Frog Horror） — First strike, deathtouch You may play an additional land on each of your turns. Creatures and nonbasic lands your opponents control enter tapped. Whenever Thalia and The 
- **出场率最高的牌**（大多数牌组都会放）
  - Aftermath Analyst（{1}{G}｜Creature — Elf Detective） — When this creature enters, mill three cards. (Put the top three cards of your library into your graveyard.) {3}{G}, Sacrifice this
  - Crop Rotation（{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for a land card, put that card onto the battlefiel
  - Windswept Heath（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Plains card, put it onto the battlefield, then shuffle.
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Flubs, the Fool ｜ 愚者法布斯
- 颜色 URG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Frog Scout
- 流行度：EDHREC 全时段第 48 位，约 22857 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.56 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $2.88
- 社区标签：地牌核心、地落、风暴、组合技、弃牌、零费神器流
- 完整牌面：You may play an additional land on each of your turns.
Whenever you play a land or cast a spell, draw a card if you have no cards in hand. Otherwise, discard a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Song of Creation（{1}{G}{U}{R}｜Enchantment） — You may play an additional land on each of your turns. Whenever you cast a spell, draw two cards. At the beginning of your end step, discard your hand.
  2. Eruth, Tormented Prophet（{1}{U}{R}｜Legendary Creature — Human Wizard） — If you would draw a card, exile the top two cards of your library instead. You may play those cards this turn.
  3. Azusa, Lost but Seeking（{2}{G}｜Legendary Creature — Human Monk） — You may play two additional lands on each of your turns.
  4. Lotus Cobra（{1}{G}｜Creature — Snake） — Landfall — Whenever a land you control enters, add one mana of any color.
  5. Containment Construct（{2}｜Artifact Creature — Construct） — Whenever you discard a card, you may exile that card from your graveyard. If you do, you may play that card this turn.
  6. Dryad of the Ilysian Grove（{2}{G}｜Enchantment Creature — Nymph Dryad） — You may play an additional land on each of your turns. Lands you control are every basic land type in addition to their other types.
- **出场率最高的牌**（大多数牌组都会放）
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Exploration（{G}｜Enchantment） — You may play an additional land on each of your turns.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Steam Vents（｜Land — Island Mountain） — ({T}: Add {U} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Kuja, Genome Sorcerer ｜ 基因组术士库加
- 颜色 BR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Mutant Wizard // Legendary Creature — Avatar Wizard
- 流行度：EDHREC 全时段第 49 位，约 22665 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.68 ｜ 上手难度 5/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $1.66
- 社区标签：烧血、法术连发、法师、群体折磨、衍生物、风暴
- 完整牌面：At the beginning of your end step, create a tapped 0/1 black Wizard creature token with "Whenever you cast a noncreature spell, this token deals 1 damage to each opponent." Then if you control four or more Wizards, transform Kuja.
//
Flare Star — If a Wizard you control would deal damage to a permanent or player, it deals double that damage instead.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Black Waltz No. 3（{2}{B}{R}｜Legendary Creature — Wizard） — Flying, deathtouch Whenever you cast a noncreature spell, Black Waltz No. 3 deals 2 damage to each opponent.
  2. Circle of Power（{3}{B}｜Sorcery） — You draw two cards and you lose 2 life. Create a 0/1 black Wizard creature token with "Whenever you cast a noncreature spell, this token deals 1 damage to each opponent."
  3. Black Mage's Rod（{1}{B}｜Artifact — Equipment） — Job select (When this Equipment enters, create a 1/1 colorless Hero creature token, then attach this to it.) Equipped creature gets +1/+0, has "Whenever you cast a noncre
  4. Cornered by Black Mages（{1}{B}{B}｜Sorcery） — Target opponent sacrifices a creature of their choice. Create a 0/1 black Wizard creature token with "Whenever you cast a noncreature spell, this token deals 1 damage to 
  5. Coruscation Mage（{1}{R}｜Creature — Otter Wizard） — Offspring {2} (You may pay an additional {2} as you cast this spell. If you do, when this creature enters, create a 1/1 token copy of it.) Whenever you cast a noncreature
  6. Transpose（{2}{B}｜Instant） — Draw a card, then discard a card. You lose 1 life. If this spell was cast from your hand, create a 0/1 black Wizard creature token with "Whenever you cast a noncreature s
- **出场率最高的牌**（大多数牌组都会放）
  - Harmonic Prodigy（{1}{R}｜Creature — Human Wizard） — Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.) If a triggered ability of a Shaman or
  - Lindblum, Industrial Regency（｜） — 
  - Queen Brahne（{2}{R}｜Legendary Creature — Human Noble） — Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.) Whenever Queen Brahne attacks, create
  - Mysidian Elder（{2}{R}｜Creature — Human Wizard） — When this creature enters, create a 0/1 black Wizard creature token with "Whenever you cast a noncreature spell, this token deals 


## Wilhelt, the Rotcleaver ｜ 断腐尸威海特
- 颜色 UB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Zombie Warrior
- 流行度：EDHREC 全时段第 50 位，约 22627 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.52 ｜ 上手难度 5/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $9.53
- 社区标签：僵尸、衍生物、牺牲流、坟场复活、组合技、坟场
- 完整牌面：Whenever another Zombie you control dies, if it didn't have decayed, create a 2/2 black Zombie creature token with decayed. (It can't block. When it attacks, sacrifice it at end of combat.)
At the beginning of your end step, you may sacrifice a Zombie. If you do, draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Diregraf Captain（{1}{U}{B}｜Creature — Zombie Soldier） — Deathtouch Other Zombie creatures you control get +1/+1. Whenever another Zombie you control dies, target opponent loses 1 life.
  2. Rooftop Storm（{5}{U}｜Enchantment） — You may pay {0} rather than pay the mana cost for Zombie creature spells you cast.
  3. Diregraf Colossus（{2}{B}｜Creature — Zombie Giant） — This creature enters with a +1/+1 counter on it for each Zombie card in your graveyard. Whenever you cast a Zombie spell, create a tapped 2/2 black Zombie creature token.
  4. Gravecrawler（{B}｜Creature — Zombie） — This creature can't block. You may cast this card from your graveyard as long as you control a Zombie.
  5. Undead Augur（{B}{B}｜Creature — Zombie Wizard） — Whenever this creature or another Zombie you control dies, you draw a card and lose 1 life.
  6. Death Baron（{1}{B}{B}｜Creature — Zombie Wizard） — Skeletons you control and other Zombies you control get +1/+1 and have deathtouch. (Any amount of damage they deal to a creature is enough to destroy it.)
- **出场率最高的牌**（大多数牌组都会放）
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost thi
  - Necroduality（{3}{U}｜Enchantment） — Whenever a nontoken Zombie you control enters, create a token that's a copy of that creature.
  - Headless Rider（{2}{B}｜Creature — Zombie） — Whenever this creature or another nontoken Zombie you control dies, create a 2/2 black Zombie creature token.


## Oloro, Ageless Ascetic ｜ 永生苦修士欧罗若
- 颜色 WUB ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Giant Soldier
- 流行度：EDHREC 全时段第 51 位，约 22604 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 1.14 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $18.51
- 社区标签：生命增益、控制、组合技、铁壁防守、吸取生命、锁场
- 完整牌面：At the beginning of your upkeep, you gain 2 life.
Whenever you gain life, you may pay {1}. If you do, draw a card and each opponent loses 1 life.
At the beginning of your upkeep, if Oloro is in the command zone, you gain 2 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sanguine Bond（{3}{B}{B}｜Enchantment） — Whenever you gain life, target opponent loses that much life.
  2. Aetherflux Reservoir（{4}｜Artifact） — Whenever you cast a spell, you gain 1 life for each spell you've cast this turn. Pay 50 life: This artifact deals 50 damage to any target.
  3. Soul Warden（{W}｜Creature — Human Cleric） — Whenever another creature enters, you gain 1 life.
  4. Vito, Thorn of the Dusk Rose（{2}{B}｜Legendary Creature — Vampire Cleric） — Whenever you gain life, target opponent loses that much life. {3}{B}{B}: Creatures you control gain lifelink until end of turn.
  5. Authority of the Consuls（{W}｜Enchantment） — Creatures your opponents control enter tapped. Whenever a creature an opponent controls enters, you gain 1 life.
  6. Kambal, Consul of Allocation（{1}{W}{B}｜Legendary Creature — Human Advisor） — Whenever an opponent casts a noncreature spell, that player loses 2 life and you gain 2 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Godless Shrine（｜Land — Plains Swamp） — ({T}: Add {W} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Hallowed Fountain（｜Land — Plains Island） — ({T}: Add {W} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Ghostly Prison（{2}{W}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.


## Breya, Etherium Shaper ｜ 乙金塑师布莱娅
- 颜色 WUBR ｜ 法术力值 4.0 ｜ 类型 Legendary Artifact Creature — Human
- 流行度：EDHREC 全时段第 52 位，约 22567 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.24 ｜ 上手难度 3/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.35
- 社区标签：神器、衍生物、组合技、闪现回场、振翼机、神器共鸣
- 完整牌面：When Breya enters, create two 1/1 blue Thopter artifact creature tokens with flying.
{2}, Sacrifice two artifacts: Choose one —
• Breya deals 3 damage to target player or planeswalker.
• Target creature gets -4/-4 until end of turn.
• You gain 5 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sai, Master Thopterist（{2}{U}｜Legendary Creature — Human Artificer） — Whenever you cast an artifact spell, create a 1/1 colorless Thopter artifact creature token with flying. {1}{U}, Sacrifice two artifacts: Draw a card.
  2. Seat of the Synod（｜Artifact Land） — {T}: Add {U}.
  3. Etherium Sculptor（{1}{U}｜Artifact Creature — Vedalken Artificer） — Artifact spells you cast cost {1} less to cast.
  4. Great Furnace（｜Artifact Land） — {T}: Add {R}.
  5. Ancient Den（｜Artifact Land） — {T}: Add {W}.
  6. Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
- **出场率最高的牌**（大多数牌组都会放）
  - Vault of Whispers（｜Artifact Land） — {T}: Add {B}.
  - Emry, Lurker of the Loch（{2}{U}｜Legendary Creature — Merfolk Wizard） — Affinity for artifacts (This spell costs {1} less to cast for each artifact you control.) When Emry enters, mill four cards. {T}: 
  - Thopter Spy Network（{2}{U}{U}｜Enchantment） — At the beginning of your upkeep, if you control an artifact, create a 1/1 colorless Thopter artifact creature token with flying. W
  - Spire of Industry（｜Land） — {T}: Add {C}. {T}, Pay 1 life: Add one mana of any color. Activate only if you control an artifact.


## Ureni of the Unwritten ｜ 未详之威乌列尼
- 颜色 URG ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Spirit Dragon
- 流行度：EDHREC 全时段第 53 位，约 22437 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.85 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $21.48
- 社区标签：龙、飞行、加速、快攻、中速、额外战斗
- 完整牌面：Flying, trample
Whenever Ureni enters or attacks, look at the top eight cards of your library. You may put a Dragon creature card from among them onto the battlefield. Put the rest on the bottom of your library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Dragon Tempest（{1}{R}｜Enchantment） — Whenever a creature you control with flying enters, it gains haste until end of turn. Whenever a Dragon you control enters, it deals X damage to any target, where X is th
  2. Hellkite Courser（{4}{R}{R}｜Creature — Dragon） — Flying When this creature enters, you may put a commander you own from the command zone onto the battlefield. It gains haste. Return it to the command zone at the beginni
  3. Lathliss, Dragon Queen（{4}{R}{R}｜Legendary Creature — Dragon） — Flying Whenever another nontoken Dragon you control enters, create a 5/5 red Dragon creature token with flying. {1}{R}: Dragons you control get +1/+0 until end of turn.
  4. Sarkhan, Soul Aflame（{1}{U}{R}｜Legendary Creature — Human Shaman） — Dragon spells you cast cost {1} less to cast. Whenever a Dragon you control enters, you may have Sarkhan become a copy of it until end of turn, except its name is Sarkhan
  5. Haven of the Spirit Dragon（｜Land） — {T}: Add {C}. {T}: Add one mana of any color. Spend this mana only to cast a Dragon creature spell. {2}, {T}, Sacrifice this land: Return target Dragon creature card or U
  6. Atarka, World Render（{5}{R}{G}｜Legendary Creature — Dragon） — Flying, trample Whenever a Dragon you control attacks, it gains double strike until end of turn.
- **出场率最高的牌**（大多数牌组都会放）
  - Temur Ascendancy（{G}{U}{R}｜Enchantment） — Creatures you control have haste. Whenever a creature you control with power 4 or greater enters, you may draw a card.
  - Broodcaller Scourge（{5}{G}{G}｜Creature — Dragon） — Flying Whenever one or more Dragons you control deal combat damage to a player, you may put a permanent card with mana value less 
  - Miirym, Sentinel Wyrm（{3}{G}{U}{R}｜Legendary Creature — Dragon Spirit） — Flying, ward {2} Whenever another nontoken Dragon you control enters, create a token that's a copy of it, except the token isn't l
  - Rootbound Crag（｜Land） — This land enters tapped unless you control a Mountain or a Forest. {T}: Add {R} or {G}.


## Meren of Clan Nel Toth ｜ 奈拓族的莫伦
- 颜色 BG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Shaman
- 流行度：EDHREC 全时段第 54 位，约 22364 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.74 ｜ 上手难度 4/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $2.28
- 社区标签：牺牲流、坟场复活、坟场、牺牲、诞生荚、组合技
- 完整牌面：Whenever another creature you control dies, you get an experience counter.
At the beginning of your end step, choose target creature card in your graveyard. If that card's mana value is less than or equal to the number of experience counters you have, return it to the battlefield. Otherwise, put it into your hand.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Spore Frog（{G}｜Creature — Frog） — Sacrifice this creature: Prevent all combat damage that would be dealt this turn.
  2. Plaguecrafter（{2}{B}｜Creature — Human Shaman） — When this creature enters, each player sacrifices a creature or planeswalker of their choice. Each player who can't discards a card.
  3. Sakura-Tribe Elder（{1}{G}｜Creature — Snake Shaman） — Sacrifice this creature: Search your library for a basic land card, put that card onto the battlefield tapped, then shuffle.
  4. Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost this way. (Each {B} in the mana costs of pe
  5. Eternal Witness（{1}{G}{G}｜Creature — Human Shaman） — When this creature enters, you may return target card from your graveyard to your hand.
  6. Buried Alive（{2}{B}｜Sorcery） — Search your library for up to three creature cards, put them into your graveyard, then shuffle.
- **出场率最高的牌**（大多数牌组都会放）
  - Woodland Cemetery（｜Land） — This land enters tapped unless you control a Swamp or a Forest. {T}: Add {B} or {G}.
  - Victimize（{2}{B}｜Sorcery） — Choose two target creature cards in your graveyard. Sacrifice a creature. If you do, return the chosen cards to the battlefield ta
  - Viscera Seer（{B}｜Creature — Vampire Wizard） — Sacrifice a creature: Scry 1. (Look at the top card of your library. You may put that card on the bottom.)
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}


## Arabella, Abandoned Doll ｜ 遭弃娃娃阿拉贝拉
- 颜色 WR ｜ 法术力值 2.0 ｜ 类型 Legendary Artifact Creature — Toy
- 流行度：EDHREC 全时段第 55 位，约 21974 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.55 ｜ 上手难度 1/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.86
- 社区标签：衍生物、快攻、烧血、生命增益、群体折磨、小生物
- 完整牌面：Whenever Arabella attacks, it deals X damage to each opponent and you gain X life, where X is the number of creatures you control with power 2 or less.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Dusk // Dawn（{2}{W}{W} // {3}{W}{W}｜Sorcery // Sorcery） — 
  2. Welcoming Vampire（{2}{W}｜Creature — Vampire） — Flying Whenever one or more other creatures you control with power 2 or less enter, draw a card. This ability triggers only once each turn.
  3. Enduring Innocence（{1}{W}{W}｜Enchantment Creature — Sheep Glimmer） — Lifelink Whenever one or more other creatures you control with power 2 or less enter, draw a card. This ability triggers only once each turn. When Enduring Innocence dies
  4. Impact Tremors（{1}{R}｜Enchantment） — Whenever a creature you control enters, this enchantment deals 1 damage to each opponent.
  5. Delney, Streetwise Lookout（{2}{W}｜Legendary Creature — Human Scout） — Creatures you control with power 2 or less can't be blocked by creatures with power 3 or greater. If a triggered ability of a creature you control with power 2 or less tr
  6. Mentor of the Meek（{2}{W}｜Creature — Human Soldier） — Whenever another creature you control with power 2 or less enters, you may pay {1}. If you do, draw a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Anim Pakal, Thousandth Moon（{1}{R}{W}｜Legendary Creature — Human Soldier） — Whenever you attack with one or more non-Gnome creatures, put a +1/+1 counter on Anim Pakal, then create X 1/1 colorless Gnome art
  - Loyal Apprentice（{1}{R}｜Creature — Human Artificer） — Haste Lieutenant — At the beginning of combat on your turn, if you control your commander, create a 1/1 colorless Thopter artifact


## Kinnan, Bonder Prodigy ｜ 持绊逸才季宁
- 颜色 UG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Druid
- 流行度：EDHREC 全时段第 56 位，约 21888 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 2.15 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $16.71
- 社区标签：组合技、加速、中速、神器、控制、爆费
- 完整牌面：Whenever you tap a nonland permanent for mana, add one mana of any type that permanent produced.
{5}{G}{U}: Look at the top five cards of your library. You may put a non-Human creature card from among them onto the battlefield. Put the rest on the bottom of your library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Basalt Monolith（{3}｜Artifact） — This artifact doesn't untap during your untap step. {T}: Add {C}{C}{C}. {3}: Untap this artifact.
  2. Thrasios, Triton Hero（{G}{U}｜Legendary Creature — Merfolk Wizard） — {4}: Scry 1, then reveal the top card of your library. If it's a land card, put it onto the battlefield tapped. Otherwise, draw a card. Partner (You can have two commande
  3. Fyndhorn Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  4. Elvish Mystic（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  5. Springleaf Drum（{1}｜Artifact） — {T}, Tap an untapped creature you control: Add one mana of any color.
  6. Hullbreaker Horror（{5}{U}{U}｜Creature — Kraken Horror） — Flash This spell can't be countered. Whenever you cast a spell, choose up to one — • Return target spell you don't control to its owner's hand. • Return target nonland pe
- **出场率最高的牌**（大多数牌组都会放）
  - Llanowar Elves（{G}｜Creature — Elf Druid） — {T}: Add {G}.
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Talisman of Curiosity（{2}｜Artifact） — {T}: Add {C}. {T}: Add {G} or {U}. This artifact deals 1 damage to you.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Tidus, Yuna's Guardian ｜ 尤娜护卫提达
- 颜色 WUG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Human Warrior
- 流行度：EDHREC 全时段第 57 位，约 21745 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.45 ｜ 上手难度 5/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $2.75
- 社区标签：＋1/＋1 指示物、增殖、指示物、快攻、中速、组合技
- 完整牌面：At the beginning of combat on your turn, you may move a counter from target creature you control onto a second target creature you control.
Cheer — Whenever one or more creatures you control with counters on them deal combat damage to a player, you may draw a card and proliferate. Do this only once each turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Yuna, Grand Summoner（{1}{G}{W}{U}｜Legendary Creature — Human Cleric） — Grand Summon — {T}: Add one mana of any color. When you next cast a creature spell this turn, that creature enters with two additional +1/+1 counters on it. Whenever anot
  2. Sphere Grid（{1}{G}｜Enchantment） — Whenever a creature you control deals combat damage to a player, put a +1/+1 counter on that creature. Unlock Ability — Creatures you control with +1/+1 counters on them 
  3. Damning Verdict（{3}{W}{W}｜Sorcery） — Destroy all creatures with no counters on them.
  4. Rikku, Resourceful Guardian（{2}{U}｜Legendary Creature — Human Artificer） — Whenever you put one or more counters on a creature, until end of turn, that creature can't be blocked by creatures your opponents control. Steal — {1}, {T}: Move a count
  5. Wakka, Devoted Guardian（{2}{G}{W}｜Legendary Creature — Human Warrior） — Reach, trample Whenever Wakka deals combat damage to a player, destroy up to one target artifact that player controls and put a +1/+1 counter on Wakka. Blitzball Captain 
  6. Gyre Sage（{1}{G}｜Creature — Elf Druid） — Evolve (Whenever a creature you control enters, if that creature has greater power or toughness than this creature, put a +1/+1 counter on this creature.) {T}: Add {G} fo
- **出场率最高的牌**（大多数牌组都会放）
  - Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Incubation Druid（{1}{G}｜Creature — Elf Druid） — {T}: Add one mana of any type that a land you control could produce. If this creature has a +1/+1 counter on it, add three mana of


## Teysa Karlov ｜ 泰莎卡洛夫
- 颜色 WB ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Advisor
- 流行度：EDHREC 全时段第 58 位，约 21693 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.53 ｜ 上手难度 1/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $2.60
- 社区标签：牺牲流、衍生物、牺牲、生命增益、组合技、吸取生命
- 完整牌面：If a creature dying causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.
Creature tokens you control have vigilance and lifelink.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Zulaport Cutthroat（{1}{B}｜Creature — Human Rogue Ally） — Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life.
  2. Pitiless Plunderer（{3}{B}｜Creature — Human Pirate） — Whenever another creature you control dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")
  3. Cruel Celebrant（{W}{B}｜Creature — Vampire） — Whenever this creature or another creature or planeswalker you control dies, each opponent loses 1 life and you gain 1 life.
  4. Bastion of Remembrance（{2}{B}｜Enchantment） — When this enchantment enters, create a 1/1 white Human Soldier creature token. Whenever a creature you control dies, each opponent loses 1 life and you gain 1 life.
  5. Teysa, Orzhov Scion（{1}{W}{B}｜Legendary Creature — Human Advisor） — Sacrifice three white creatures: Exile target creature. Whenever another black creature you control dies, create a 1/1 white Spirit creature token with flying.
  6. Blood Artist（{1}{B}｜Creature — Vampire） — Whenever this creature or another creature dies, target player loses 1 life and you gain 1 life.
- **出场率最高的牌**（大多数牌组都会放）
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  - Elas il-Kor, Sadistic Pilgrim（{W}{B}｜Legendary Creature — Phyrexian Kor Cleric） — Deathtouch Whenever another creature you control enters, you gain 1 life. Whenever another creature you control dies, each opponen
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Viscera Seer（{B}｜Creature — Vampire Wizard） — Sacrifice a creature: Scry 1. (Look at the top card of your library. You may put that card on the bottom.)


## Zhulodok, Void Gorger ｜ 虚空饕体祖禄铎
- 颜色 C ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Eldrazi
- 流行度：EDHREC 全时段第 59 位，约 21418 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.37 ｜ 上手难度 4/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $None
- 社区标签：奥札奇、倾曳、爆费、神器、加速、歼灭
- 完整牌面：Colorless spells you cast from your hand with mana value 7 or greater have "Cascade, cascade." (When you cast one, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. Put the exiled cards on the bottom in a random order. Then do it again.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Kozilek, the Great Distortion（{8}{C}{C}｜Legendary Creature — Eldrazi） — When you cast this spell, if you have fewer than seven cards in hand, draw cards equal to the difference. Menace Discard a card with mana value X: Counter target spell wi
  2. Eldrazi Temple（｜Land） — {T}: Add {C}. {T}: Add {C}{C}. Spend this mana only to cast colorless Eldrazi spells or activate abilities of colorless Eldrazi.
  3. Flayer of Loyalties（{8}{C}{C}｜Creature — Eldrazi） — When you cast this spell, gain control of target creature until end of turn. Untap that creature. Until end of turn, it has base power and toughness 10/10 and gains tramp
  4. It That Betrays（{12}｜Creature — Eldrazi） — Annihilator 2 (Whenever this creature attacks, defending player sacrifices two permanents of their choice.) Whenever an opponent sacrifices a nontoken permanent, put that
  5. Darksteel Monolith（{8}｜Artifact） — Indestructible Once each turn, you may pay {0} rather than pay the mana cost for a colorless spell you cast from your hand.
  6. Ulamog, the Ceaseless Hunger（{10}｜Legendary Creature — Eldrazi） — When you cast this spell, exile two target permanents. Indestructible Whenever Ulamog attacks, defending player exiles the top twenty cards of their library.
- **出场率最高的牌**（大多数牌组都会放）
  - All Is Dust（{7}｜Kindred Sorcery — Eldrazi） — Each player sacrifices all permanents they control that are one or more colors.
  - Forsaken Monument（{5}｜Legendary Artifact） — Colorless creatures you control get +2/+2. Whenever you tap a permanent for {C}, add an additional {C}. Whenever you cast a colorl
  - Thran Dynamo（{4}｜Artifact） — {T}: Add {C}{C}{C}.
  - Urza's Mine（｜Land — Urza's Mine） — {T}: Add {C}. If you control an Urza's Power-Plant and an Urza's Tower, add {C}{C} instead.


## Gishath, Sun's Avatar ｜ 烈阳化身基撒斯
- 颜色 WRG ｜ 法术力值 8.0 ｜ 类型 Legendary Creature — Dinosaur Avatar
- 流行度：EDHREC 全时段第 60 位，约 21373 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.93 ｜ 上手难度 2/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $4.90
- 社区标签：恐龙、加速、快攻、大生物、中速、发现
- 完整牌面：Vigilance, trample, haste
Whenever Gishath deals combat damage to a player, reveal that many cards from the top of your library. Put any number of Dinosaur creature cards from among them onto the battlefield and the rest on the bottom of your library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Zacama, Primal Calamity（{6}{R}{G}{W}｜Legendary Creature — Elder Dinosaur） — Reach, vigilance, trample When Zacama enters, if you cast it, untap all lands you control. {2}{R}: Zacama deals 3 damage to target creature. {2}{G}: Destroy target artifa
  2. Pantlaza, Sun-Favored（{2}{R}{G}{W}｜Legendary Creature — Dinosaur） — Whenever Pantlaza or another Dinosaur you control enters, you may discover X, where X is that creature's toughness. Do this only once each turn. (Exile cards from the top
  3. Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess combat damage to the player or planeswalker
  4. Etali, Primal Storm（{4}{R}{R}｜Legendary Creature — Elder Dinosaur） — Whenever Etali attacks, exile the top card of each player's library, then you may cast any number of spells from among those cards without paying their mana costs.
  5. Regisaur Alpha（{3}{R}{G}｜Creature — Dinosaur） — Other Dinosaurs you control have haste. When this creature enters, create a 3/3 green Dinosaur creature token with trample.
  6. Zetalpa, Primal Dawn（{6}{W}{W}｜Legendary Creature — Elder Dinosaur） — Flying, double strike, vigilance, trample, indestructible
- **出场率最高的牌**（大多数牌组都会放）
  - Temple Altisaur（{4}{W}｜Creature — Dinosaur） — If a source would deal damage to another Dinosaur you control, prevent all but 1 of that damage.
  - Earthshaker Dreadmaw（{4}{G}{G}｜Creature — Dinosaur） — Trample When this creature enters, draw a card for each other Dinosaur you control.
  - Wakening Sun's Avatar（{5}{W}{W}{W}｜Creature — Dinosaur Avatar） — When this creature enters, if you cast it from your hand, destroy all non-Dinosaur creatures.
  - Quartzwood Crasher（{2}{R}{R}{G}｜Creature — Dinosaur Beast） — Trample Whenever one or more creatures you control with trample deal combat damage to a player, create an X/X green Dinosaur Beast


## Tom Bombadil ｜ 汤姆·邦巴迪尔
- 颜色 WUBRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — God Bard
- 流行度：EDHREC 全时段第 61 位，约 21338 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.43 ｜ 上手难度 4/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $3.32
- 社区标签：传纪、结界流、史迹、衍生物、控制、中速
- 完整牌面：As long as there are four or more lore counters among Sagas you control, Tom Bombadil has hexproof and indestructible.
Whenever the final chapter ability of a Saga you control resolves, reveal cards from the top of your library until you reveal a Saga card. Put that card onto the battlefield and the rest on the bottom of your library in a random order. This ability triggers only once each turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Binding the Old Gods（{2}{B}{G}｜Enchantment — Saga） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Destroy target nonland permanent an opponent controls. II — Search your libra
  2. There and Back Again（{3}{R}{R}｜Enchantment — Saga） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Up to one target creature can't block for as long as you control this Saga. T
  3. Satsuki, the Living Lore（{G}{W}｜Legendary Creature — Human Druid） — {T}: Put a lore counter on each Saga you control. Activate only as a sorcery. When Satsuki dies, choose up to one — • Return target Saga or enchantment creature you contr
  4. The Eldest Reborn（{4}{B}｜Enchantment — Saga） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I — Each opponent sacrifices a creature or planeswalker of their choice. II — Eac
  5. Narci, Fable Singer（{1}{W}{B}{G}｜Legendary Creature — Human Bard） — Lifelink Whenever you sacrifice an enchantment, draw a card. Whenever the final chapter ability of a Saga you control resolves, each opponent loses X life and you gain X 
  6. The Kami War（｜） — 
- **出场率最高的牌**（大多数牌组都会放）
  - Sythis, Harvest's Hand（{G}{W}｜Legendary Enchantment Creature — Nymph） — Whenever you cast an enchantment spell, you gain 1 life and draw a card.
  - Sanctum Weaver（{1}{G}｜Enchantment Creature — Dryad） — {T}: Add X mana of any one color, where X is the number of enchantments you control.
  - Goldberry, River-Daughter（{1}{U}｜Legendary Creature — Nymph） — {T}: Move a counter of each kind not on Goldberry from another target permanent you control onto Goldberry. {U}, {T}: Move one or 
  - The Bath Song（{3}{U}｜Enchantment — Saga） — (As this Saga enters and after your draw step, add a lore counter. Sacrifice after III.) I, II — Draw two cards, then discard a ca


## Atla Palani, Nest Tender ｜ 护巢人娥拉帕拉尼
- 颜色 WRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Shaman
- 流行度：EDHREC 全时段第 62 位，约 21332 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.55 ｜ 上手难度 3/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $1.90
- 社区标签：蛋、恐龙、衍生物、快攻、组合技、牺牲
- 完整牌面：{2}, {T}: Create a 0/1 green Egg creature token with defender.
Whenever an Egg you control dies, reveal cards from the top of your library until you reveal a creature card. Put that card onto the battlefield and the rest on the bottom of your library in a random order.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ashnod's Altar（{3}｜Artifact） — Sacrifice a creature: Add {C}{C}.
  2. Palani's Hatcher（{3}{R}{G}｜Creature — Dinosaur） — Other Dinosaurs you control have haste. When this creature enters, create two 0/1 green Dinosaur Egg creature tokens. At the beginning of combat on your turn, if you cont
  3. Goblin Bombardment（{1}{R}｜Enchantment） — Sacrifice a creature: This enchantment deals 1 damage to any target.
  4. High Market（｜Land） — {T}: Add {C}. {T}, Sacrifice a creature: You gain 1 life.
  5. Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  6. Nesting Dragon（{3}{R}{R}｜Creature — Dragon） — Flying Landfall — Whenever a land you control enters, create a 0/2 red Dragon Egg creature token with defender and "When this token dies, create a 2/2 red Dragon creature
- **出场率最高的牌**（大多数牌组都会放）
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Jungle Shrine（｜Land） — This land enters tapped. {T}: Add {R}, {G}, or {W}.
  - Etali, Primal Storm（{4}{R}{R}｜Legendary Creature — Elder Dinosaur） — Whenever Etali attacks, exile the top card of each player's library, then you may cast any number of spells from among those cards
  - Cinder Glade（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) This land enters tapped unless you control two or more basic lands.


## Korvold, Fae-Cursed King ｜ 受诅国王寇沃
- 颜色 BRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Dragon Noble
- 流行度：EDHREC 全时段第 63 位，约 21191 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 1.65 ｜ 上手难度 2/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.41
- 社区标签：牺牲、宝物、牺牲流、衍生物、组合技、＋1/＋1 指示物
- 完整牌面：Flying
Whenever Korvold enters or attacks, sacrifice another permanent.
Whenever you sacrifice a permanent, put a +1/+1 counter on Korvold and draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mayhem Devil（{1}{B}{R}｜Creature — Devil） — Whenever a player sacrifices a permanent, this creature deals 1 damage to any target.
  2. Tireless Provisioner（{2}{G}｜Creature — Elf Scout） — Landfall — Whenever a land you control enters, create a Food token or a Treasure token. (Food is an artifact with "{2}, {T}, Sacrifice this token: You gain 3 life." Treas
  3. Pitiless Plunderer（{3}{B}｜Creature — Human Pirate） — Whenever another creature you control dies, create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")
  4. Chatterfang, Squirrel General（{2}{G}｜Legendary Creature — Squirrel Warrior） — Forestwalk (This creature can't be blocked as long as defending player controls a Forest.) If one or more tokens would be created under your control, those tokens plus th
  5. Warren Soultrader（{2}{B}｜Creature — Zombie Goblin Wizard） — Pay 1 life, Sacrifice another creature: Create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.")
  6. Academy Manufactor（{3}｜Artifact Creature — Assembly-Worker） — If you would create a Clue, Food, or Treasure token, instead create one of each.
- **出场率最高的牌**（大多数牌组都会放）
  - Ignoble Hierarch（{G}｜Creature — Goblin Shaman） — Exalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.) {T}: Add {B}, {R}, or {G}.
  - Stomping Ground（｜Land — Mountain Forest） — ({T}: Add {R} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Overgrown Tomb（｜Land — Swamp Forest） — ({T}: Add {B} or {G}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Blood Crypt（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Zurgo Stormrender ｜ 镇霆可汗珠高
- 颜色 WBR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Orc Warrior
- 流行度：EDHREC 全时段第 64 位，约 21175 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.28 ｜ 上手难度 4/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $4.58
- 社区标签：衍生物、牺牲流、快攻、烧血、攻击触发、牺牲
- 完整牌面：Mobilize 1 (Whenever this creature attacks, create a tapped and attacking 1/1 red Warrior creature token. Sacrifice it at the beginning of the next end step.)
Whenever a creature token you control leaves the battlefield, draw a card if it was attacking. Otherwise, each opponent loses 1 life.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Ainok Strike Leader（{1}{W}｜Creature — Dog Warrior） — Whenever you attack with this creature and/or your commander, for each opponent, create a 1/1 red Goblin creature token that's tapped and attacking that player. Sacrifice
  2. Will of the Mardu（{2}{W}｜Instant） — Choose one. If you control a commander as you cast this spell, you may choose both instead. • Create a number of 1/1 red Warrior creature tokens equal to the number of cr
  3. Adeline, Resplendent Cathar（{1}{W}{W}｜Legendary Creature — Human Knight） — Vigilance Adeline's power is equal to the number of creatures you control. Whenever you attack, for each opponent, create a 1/1 white Human creature token that's tapped a
  4. Redoubled Stormsinger（{2}{R}｜Creature — Orc Wizard） — First strike Whenever this creature attacks, for each creature token you control that entered this turn, create a tapped and attacking token that's a copy of that token. 
  5. Grand Crescendo（{X}{W}{W}｜Instant） — Create X 1/1 green and white Citizen creature tokens. Creatures you control gain indestructible until end of turn.
  6. Infantry Shield（{2}{R}｜Artifact — Equipment） — Equipped creature has menace and mobilize X, where X is its power. (Whenever it attacks, create X tapped and attacking 1/1 red Warrior creature tokens. Sacrifice them at 
- **出场率最高的牌**（大多数牌组都会放）
  - Skullclamp（{1}｜Artifact — Equipment） — Equipped creature gets +1/-1. Whenever equipped creature dies, draw two cards. Equip {1}
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Isolated Chapel（｜Land） — This land enters tapped unless you control a Plains or a Swamp. {T}: Add {W} or {B}.
  - Dragonskull Summit（｜Land） — This land enters tapped unless you control a Swamp or a Mountain. {T}: Add {B} or {R}.


## Shorikai, Genesis Engine ｜ 创机胜利械
- 颜色 WU ｜ 法术力值 4.0 ｜ 类型 Legendary Artifact — Vehicle
- 流行度：EDHREC 全时段第 65 位，约 21020 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.57 ｜ 上手难度 3/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $2.92
- 社区标签：载具、神器、控制、组合技、衍生物、抽牌
- 完整牌面：{1}, {T}: Draw two cards, then discard a card. Create a 1/1 colorless Pilot creature token with "This token crews Vehicles as though its power were 2 greater."
Crew 8 (Tap any number of creatures you control with total power 8 or more: This Vehicle becomes an artifact creature until end of turn.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Unwinding Clock（{4}｜Artifact） — Untap all artifacts you control during each other player's untap step.
  2. Imposter Mech（{1}{U}｜Artifact — Vehicle） — You may have this Vehicle enter as a copy of a creature an opponent controls, except it's a Vehicle artifact with crew 3 and it loses all other card types. Crew 3
  3. Kotori, Pilot Prodigy（{1}{W}{U}｜Legendary Creature — Moonfolk Pilot） — Vehicles you control have crew 2. At the beginning of combat on your turn, target artifact creature you control gains lifelink and vigilance until end of turn.
  4. Mobilizer Mech（{1}{U}｜Artifact — Vehicle） — Flying Whenever this Vehicle becomes crewed, up to one other target Vehicle you control becomes an artifact creature until end of turn. Crew 3 (Tap any number of creature
  5. Manifold Key（{1}｜Artifact） — {1}, {T}: Untap another target artifact. {3}, {T}: Target creature can't be blocked this turn.
  6. Etherium Sculptor（{1}{U}｜Artifact Creature — Vedalken Artificer） — Artifact spells you cast cost {1} less to cast.
- **出场率最高的牌**（大多数牌组都会放）
  - Prairie Stream（｜Land — Plains Island） — ({T}: Add {W} or {U}.) This land enters tapped unless you control two or more basic lands.
  - Azorius Signet（{2}｜Artifact） — {1}, {T}: Add {W}{U}.
  - Dispatch（{W}｜Instant） — Tap target creature. Metalcraft — If you control three or more artifacts, exile that creature.
  - Foundry Inspector（{3}｜Artifact Creature — Construct） — Artifact spells you cast cost {1} less to cast.


## Felothar the Steadfast ｜ 坚毅可汗芾洛塔
- 颜色 WBG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Warrior
- 流行度：EDHREC 全时段第 66 位，约 20936 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.33 ｜ 上手难度 3/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $2.97
- 社区标签：守军、防御力核心、中速、生命增益、快攻、坟场复活
- 完整牌面：Each creature you control assigns combat damage equal to its toughness rather than its power.
Creatures you control can attack as though they didn't have defender.
{3}, {T}, Sacrifice another creature: Draw cards equal to the sacrificed creature's toughness, then discard cards equal to its power.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Overgrown Battlement（{1}{G}｜Creature — Wall） — Defender {T}: Add {G} for each creature you control with defender.
  2. Axebane Guardian（{2}{G}｜Creature — Human Druid） — Defender {T}: Add X mana in any combination of colors, where X is the number of creatures you control with defender.
  3. Crashing Drawbridge（{2}｜Artifact Creature — Wall） — Defender {T}: Creatures you control gain haste until end of turn.
  4. Wall of Omens（{1}{W}｜Creature — Wall） — Defender When this creature enters, draw a card.
  5. Wall of Blossoms（{1}{G}｜Creature — Plant Wall） — Defender When this creature enters, draw a card.
  6. Tree of Redemption（{3}{G}｜Creature — Plant） — Defender {T}: Exchange your life total with this creature's toughness.
- **出场率最高的牌**（大多数牌组都会放）
  - Sylvan Caryatid（{1}{G}｜Creature — Plant） — Defender, hexproof {T}: Add one mana of any color.
  - Arbor Adherent（{3}{G}｜Creature — Dog Druid） — {T}: Add one mana of any color. {T}: Add X mana of any one color, where X is the greatest toughness among other creatures you cont
  - Jaws of Defeat（{3}{B}｜Enchantment） — Whenever a creature you control enters, target opponent loses life equal to the difference between that creature's power and its t
  - Behind the Scenes（{2}{B}｜Enchantment） — Creatures you control have skulk. (They can't be blocked by creatures with greater power.) {4}{W}: Creatures you control get +1/+1


## The Wandering Minstrel ｜ 异国的诗人
- 颜色 WUBRG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Human Bard
- 流行度：EDHREC 全时段第 67 位，约 20887 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.55 ｜ 上手难度 4/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.29
- 社区标签：地牌核心、加速、组合技、地落、衍生物、城镇
- 完整牌面：Lands you control enter untapped.
The Minstrel's Ballad — At the beginning of combat on your turn, if you control five or more Towns, create a 2/2 Elemental creature token that's all colors.
{3}{W}{U}{B}{R}{G}: Other creatures you control get +X/+X until end of turn, where X is the number of Towns you control.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Guadosalam, Farplane Gateway（｜Land — Town） — This land enters tapped. {T}: Add {G} or {U}.
  2. Gongaga, Reactor Town（｜Land — Town） — This land enters tapped. {T}: Add {R} or {G}.
  3. Gohn, Town of Ruin（｜Land — Town） — This land enters tapped. {T}: Add {B} or {G}.
  4. Windurst, Federation Center（｜Land — Town） — This land enters tapped. {T}: Add {G} or {W}.
  5. Sharlayan, Nation of Scholars（｜Land — Town） — This land enters tapped. {T}: Add {W} or {U}.
  6. Baron, Airship Kingdom（｜Land — Town） — This land enters tapped. {T}: Add {U} or {R}.
- **出场率最高的牌**（大多数牌组都会放）
  - Treno, Dark City（｜Land — Town） — This land enters tapped. {T}: Add {U} or {B}.
  - Starting Town（｜Land — Town） — This land enters tapped unless it's your first, second, or third turn of the game. {T}: Add {C}. {T}, Pay 1 life: Add one mana of 
  - Rabanastre, Royal City（｜Land — Town） — This land enters tapped. {T}: Add {R} or {W}.
  - Insomnia, Crown City（｜Land — Town） — This land enters tapped. {T}: Add {W} or {B}.


## Queen Marchesa ｜ 玛切莎女王
- 颜色 WBR ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Assassin
- 流行度：EDHREC 全时段第 68 位，约 20767 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.37 ｜ 上手难度 2/5 ｜ 造价档位 3/5 ｜ 单卡参考价 $2.18
- 社区标签：君主、借力打力、强制战斗、铁壁防守、控制、政治
- 完整牌面：Deathtouch, haste
When Queen Marchesa enters, you become the monarch.
At the beginning of your upkeep, if an opponent is the monarch, create a 1/1 black Assassin creature token with deathtouch and haste.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Deflecting Palm（{R}{W}｜Instant） — The next time a source of your choice would deal damage to you this turn, prevent that damage. If damage is prevented this way, Deflecting Palm deals that much damage to 
  2. Ghostly Prison（{2}{W}｜Enchantment） — Creatures can't attack you unless their controller pays {2} for each creature they control that's attacking you.
  3. Court of Grace（{2}{W}{W}｜Enchantment） — When this enchantment enters, you become the monarch. At the beginning of your upkeep, create a 1/1 white Spirit creature token with flying. If you're the monarch, create
  4. Mangara, the Diplomat（{3}{W}｜Legendary Creature — Human Cleric） — Lifelink Whenever an opponent attacks with creatures, if two or more of those creatures are attacking you and/or planeswalkers you control, draw a card. Whenever an oppon
  5. Kardur, Doomscourge（{2}{B}{R}｜Legendary Creature — Demon Berserker） — When Kardur enters, until your next turn, creatures your opponents control attack each combat if able and attack a player other than you if able. Whenever an attacking cr
  6. Breena, the Demagogue（{1}{W}{B}｜Legendary Creature — Bird Warlock） — Flying Whenever a player attacks one of your opponents, if that opponent has more life than another of your opponents, that attacking player draws a card and you put two 
- **出场率最高的牌**（大多数牌组都会放）
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Nomad Outpost（｜Land） — This land enters tapped. {T}: Add {R}, {W}, or {B}.
  - Talisman of Conviction（{2}｜Artifact） — {T}: Add {C}. {T}: Add {R} or {W}. This artifact deals 1 damage to you.
  - Talisman of Hierarchy（{2}｜Artifact） — {T}: Add {C}. {T}: Add {W} or {B}. This artifact deals 1 damage to you.


## Urza, Lord High Artificer ｜ 铸物勋爵克撒
- 颜色 U ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Artificer
- 流行度：EDHREC 全时段第 69 位，约 20657 副套牌
- 常见强度档 Bracket 4 ｜ 咸度 2.31 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $16.18
- 社区标签：神器、组合技、控制、锁场、衍生物、风暴
- 完整牌面：When Urza enters, create a 0/0 colorless Construct artifact creature token with "This token gets +1/+1 for each artifact you control."
Tap an untapped artifact you control: Add {U}.
{5}: Shuffle your library, then exile the top card. Until end of turn, you may play that card without paying its mana cost.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Unwinding Clock（{4}｜Artifact） — Untap all artifacts you control during each other player's untap step.
  2. Dramatic Reversal（{1}{U}｜Instant） — Untap all nonland permanents you control.
  3. Basalt Monolith（{3}｜Artifact） — This artifact doesn't untap during your untap step. {T}: Add {C}{C}{C}. {3}: Untap this artifact.
  4. Seat of the Synod（｜Artifact Land） — {T}: Add {U}.
  5. Fabricate（{2}{U}｜Sorcery） — Search your library for an artifact card, reveal it, put it into your hand, then shuffle.
  6. Isochron Scepter（{2}｜Artifact） — Imprint — When this artifact enters, you may exile an instant card with mana value 2 or less from your hand. {2}, {T}: You may copy the exiled card. If you do, you may ca
- **出场率最高的牌**（大多数牌组都会放）
  - Sapphire Medallion（{2}｜Artifact） — Blue spells you cast cost {1} less to cast.
  - Etherium Sculptor（{1}{U}｜Artifact Creature — Vedalken Artificer） — Artifact spells you cast cost {1} less to cast.
  - Hullbreaker Horror（{5}{U}{U}｜Creature — Kraken Horror） — Flash This spell can't be countered. Whenever you cast a spell, choose up to one — • Return target spell you don't control to its 
  - Everflowing Chalice（{0}｜Artifact） — Multikicker {2} (You may pay an additional {2} any number of times as you cast this spell.) This artifact enters with a charge cou


## Avatar Aang ｜ 降世神通安昂
- 颜色 WUBRG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Human Avatar Ally // Legendary Creature — Avatar Ally
- 流行度：EDHREC 全时段第 70 位，约 20615 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0 ｜ 上手难度 5/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $3.40
- 社区标签：伙伴、御气、运土、御水、御火、＋1/＋1 指示物
- 完整牌面：Flying, firebending 2
Whenever you waterbend, earthbend, firebend, or airbend, draw a card. Then if you've done all four this turn, transform Avatar Aang.
//
Flying
Spells you cast cost {W}{U}{B}{R}{G} less to cast. (This can reduce generic costs.)
At the beginning of each upkeep, you may transform Aang, Master of Elements. If you do, you gain 4 life, draw four cards, put four +1/+1 counters on him, and he deals 4 damage to each opponent.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Katara, the Fearless（{G}{W}{U}｜Legendary Creature — Human Warrior Ally） — If a triggered ability of an Ally you control triggers, that ability triggers an additional time.
  2. Aang, Swift Savior（｜） — 
  3. Haru, Hidden Talent（{1}{G}｜Legendary Creature — Human Peasant Ally） — Whenever another Ally you control enters, earthbend 1. (Target land you control becomes a 0/0 creature with haste that's still a land. Put a +1/+1 counter on it. When it 
  4. Airbending Lesson（{2}{W}｜Instant — Lesson） — Airbend target nonland permanent. (Exile it. While it's exiled, its owner may cast it for {2} rather than its mana cost.) Draw a card.
  5. Great Divide Guide（{1}{G}｜Creature — Human Scout Ally） — Each land and Ally you control has "{T}: Add one mana of any color."
  6. Aang, at the Crossroads（｜） — 
- **出场率最高的牌**（大多数牌组都会放）
  - Katara, Water Tribe's Hope（{2}{W}{U}{U}｜Legendary Creature — Human Warrior Ally） — Vigilance When Katara enters, create a 1/1 white Ally creature token. Waterbend {X}: Creatures you control have base power and tou
  - Avatar's Wrath（{2}{W}{W}｜Sorcery） — Choose up to one target creature, then airbend all other creatures. (Exile them. While each one is exiled, its owner may cast it f
  - Airbender Ascension（{1}{W}｜Enchantment） — When this enchantment enters, airbend up to one target creature. Whenever a creature you control enters, put a quest counter on th
  - Waterbender Ascension（{1}{U}｜Enchantment） — Whenever a creature you control deals combat damage to a player, put a quest counter on this enchantment. Then if it has four or m


## Go-Shintai of Life's Origin ｜ 命源御神体
- 颜色 WUBRG ｜ 法术力值 4.0 ｜ 类型 Legendary Enchantment Creature — Shrine
- 流行度：EDHREC 全时段第 71 位，约 20602 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.55 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $8.38
- 社区标签：结界流、神龛、衍生物、铁壁防守、史迹、传奇
- 完整牌面：{W}{U}{B}{R}{G}, {T}: Return target enchantment card from your graveyard to the battlefield.
Whenever Go-Shintai of Life's Origin or another nontoken Shrine you control enters, create a 1/1 colorless Shrine enchantment creature token.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sanctum of All（{W}{U}{B}{R}{G}｜Legendary Enchantment — Shrine） — At the beginning of your upkeep, you may search your library and/or graveyard for a Shrine card and put it onto the battlefield. If you search your library this way, shuf
  2. Sanctum of Fruitful Harvest（{2}{G}｜Legendary Enchantment — Shrine） — At the beginning of your first main phase, add X mana of any one color, where X is the number of Shrines you control.
  3. Sanctum of Stone Fangs（{1}{B}｜Legendary Enchantment — Shrine） — At the beginning of your first main phase, each opponent loses X life and you gain X life, where X is the number of Shrines you control.
  4. Sanctum of Calm Waters（{3}{U}｜Legendary Enchantment — Shrine） — At the beginning of your first main phase, you may draw X cards, where X is the number of Shrines you control. If you do, discard a card.
  5. Honden of Infinite Rage（{2}{R}｜Legendary Enchantment — Shrine） — At the beginning of your upkeep, Honden of Infinite Rage deals damage to any target equal to the number of Shrines you control.
  6. Go-Shintai of Hidden Cruelty（{3}{B}｜Legendary Enchantment Creature — Shrine） — Deathtouch At the beginning of your end step, you may pay {1}. When you do, destroy target creature with toughness X or less, where X is the number of Shrines you control
- **出场率最高的牌**（大多数牌组都会放）
  - Go-Shintai of Shared Purpose（{3}{W}｜Legendary Enchantment Creature — Shrine） — Vigilance At the beginning of your end step, you may pay {1}. If you do, create a 1/1 colorless Spirit creature token for each Shr
  - Go-Shintai of Ancient Wars（{2}{R}｜Legendary Enchantment Creature — Shrine） — First strike At the beginning of your end step, you may pay {1}. When you do, Go-Shintai of Ancient Wars deals X damage to target 
  - Honden of Cleansing Fire（{3}{W}｜Legendary Enchantment — Shrine） — At the beginning of your upkeep, you gain 2 life for each Shrine you control.
  - Honden of Life's Web（{4}{G}｜Legendary Enchantment — Shrine） — At the beginning of your upkeep, create a 1/1 colorless Spirit creature token for each Shrine you control.


## Helga, Skittish Seer ｜ 难测先知赫尔嘉
- 颜色 WUG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Frog Druid
- 流行度：EDHREC 全时段第 72 位，约 20372 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.28 ｜ 上手难度 4/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $4.16
- 社区标签：＋1/＋1 指示物、加速、爆费、组合技、X 咒语、中速
- 完整牌面：Whenever you cast a creature spell with mana value 4 or greater, you draw a card, gain 1 life, and put a +1/+1 counter on Helga.
{T}: Add X mana of any one color, where X is Helga's power. Spend this mana only to cast creature spells with mana value 4 or greater or creature spells with {X} in their mana costs.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. (Each of those creatures can deal excess
  2. Chulane, Teller of Tales（{2}{G}{W}{U}｜Legendary Creature — Human Druid） — Vigilance Whenever you cast a creature spell, draw a card, then you may put a land card from your hand onto the battlefield. {3}, {T}: Return target creature you control 
  3. Chakram Retriever（{4}{U}｜Creature — Elemental Dog） — Partner with Chakram Slinger (When this creature enters, target player may put Chakram Slinger into their hand from their library, then shuffle.) Whenever you cast a spel
  4. Goreclaw, Terror of Qal Sisma（{3}{G}｜Legendary Creature — Bear） — Creature spells you cast with power 4 or greater cost {2} less to cast. Whenever Goreclaw attacks, each creature you control with power 4 or greater gets +1/+1 and gains 
  5. Kiora, Behemoth Beckoner（{2}{G/U}｜Legendary Planeswalker — Kiora） — Whenever a creature you control with power 4 or greater enters, draw a card. −1: Untap target permanent.
  6. Inga and Esika（{2}{G}{U}｜Legendary Creature — Human God） — Creatures you control have vigilance and "{T}: Add one mana of any color. Spend this mana only to cast a creature spell." Whenever you cast a creature spell, if three or 
- **出场率最高的牌**（大多数牌组都会放）
  - Forgotten Ancient（{3}{G}｜Creature — Elemental） — Whenever a player casts a spell, you may put a +1/+1 counter on this creature. At the beginning of your upkeep, you may move any n
  - Beast Whisperer（{2}{G}{G}｜Creature — Elf Druid） — Whenever you cast a creature spell, draw a card.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.


## K'rrik, Son of Yawgmoth ｜ 约格莫夫之子格锐克
- 颜色 B ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Phyrexian Horror Minion
- 流行度：EDHREC 全时段第 73 位，约 20367 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 1.28 ｜ 上手难度 2/5 ｜ 造价档位 4/5 ｜ 单卡参考价 $1.12
- 社区标签：生命增益、组合技、自伤、坟场复活、风暴、虔诚
- 完整牌面：({B/P} can be paid with either {B} or 2 life.)
Lifelink
For each {B} in a cost, you may pay 2 life rather than pay that mana.
Whenever you cast a black spell, put a +1/+1 counter on K'rrik.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Vilis, Broker of Blood（{5}{B}{B}{B}｜Legendary Creature — Demon） — Flying {B}, Pay 2 life: Target creature gets -1/-1 until end of turn. Whenever you lose life, draw that many cards. (Damage causes loss of life.)
  2. Blood Celebrant（{B}｜Creature — Human Cleric） — {B}, Pay 1 life: Add one mana of any color.
  3. Chainer, Dementia Master（{3}{B}{B}｜Legendary Creature — Human Minion） — All Nightmares get +1/+1. {B}{B}{B}, Pay 3 life: Put target creature card from a graveyard onto the battlefield under your control. That creature is black and is a Nightm
  4. Asmodeus the Archfiend（{4}{B}{B}｜Legendary Creature — Devil God） — Binding Contract — If you would draw a card, exile the top card of your library face down instead. {B}{B}{B}: Draw seven cards. {B}: Return all cards exiled with Asmodeus
  5. Peer into the Abyss（{4}{B}{B}{B}｜Sorcery） — Target player draws cards equal to half the number of cards in their library and loses half their life. Round up each time.
  6. Necrotic Ooze（{2}{B}{B}｜Creature — Ooze） — As long as this creature is on the battlefield, it has all activated abilities of all creature cards in all graveyards.
- **出场率最高的牌**（大多数牌组都会放）
  - Gray Merchant of Asphodel（{3}{B}{B}｜Creature — Zombie） — When this creature enters, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost thi
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Jet Medallion（{2}｜Artifact） — Black spells you cast cost {1} less to cast.
  - Bolas's Citadel（{3}{B}{B}{B}｜Legendary Artifact） — You may look at the top card of your library any time. You may play lands and cast spells from the top of your library. If you cas


## Choco, Seeker of Paradise ｜ 桃源寻旅巧克
- 颜色 WUG ｜ 法术力值 4.0 ｜ 类型 Legendary Creature — Bird
- 流行度：EDHREC 全时段第 74 位，约 20339 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.43 ｜ 上手难度 5/5 ｜ 造价档位 2/5 ｜ 单卡参考价 $0.39
- 社区标签：地牌核心、鸟、飞行、地落、＋1/＋1 指示物、衍生物
- 完整牌面：Whenever one or more Birds you control attack, look at that many cards from the top of your library. You may put one of them into your hand. Then put any number of land cards from among them onto the battlefield tapped and the rest into your graveyard.
Landfall — Whenever a land you control enters, Choco gets +1/+0 until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Sazh's Chocobo（{G}｜Creature — Bird） — Landfall — Whenever a land you control enters, put a +1/+1 counter on this creature.
  2. Kastral, the Windcrested（{3}{W}{U}｜Legendary Creature — Bird Scout） — Flying Whenever one or more Birds you control deal combat damage to a player, choose one — • You may put a Bird creature card from your hand or graveyard onto the battlef
  3. Chocobo Racetrack（{3}{G}{G}｜Artifact） — Landfall — Whenever a land you control enters, create a 2/2 green Bird creature token with "Whenever a land you control enters, this token gets +1/+0 until end of turn."
  4. Bartz and Boko（{3}{G}{G}｜Legendary Creature — Human Bird） — Affinity for Birds (This spell costs {1} less to cast for each Bird you control.) When Bartz and Boko enters, each other Bird you control deals damage equal to its power 
  5. Sidequest: Raise a Chocobo（｜） — 
  6. Traveling Chocobo（{2}{G}｜Creature — Bird） — You may look at the top card of your library any time. You may play lands and cast Bird spells from the top of your library. If a land or Bird you control entering the ba
- **出场率最高的牌**（大多数牌组都会放）
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Emeria Angel（{2}{W}{W}｜Creature — Angel） — Flying Landfall — Whenever a land you control enters, you may create a 1/1 white Bird creature token with flying.
  - Ambrosia Whiteheart（{1}{W}｜Legendary Creature — Bird） — Flash When Ambrosia Whiteheart enters, you may return another permanent you control to its owner's hand. Landfall — Whenever a lan
  - Murmuration（{4}{W}｜Enchantment） — Birds you control get +1/+1 and have vigilance. At the beginning of your end step, for each spell you've cast this turn, create a 
