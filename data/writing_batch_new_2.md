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

# 素材：3 位主将


## Ardenn, Intrepid Archaeologist // Rograkh, Son of Rohgahh ｜ 无畏考古家亚德恩 // 罗噶之子罗噶克
- 颜色 WR ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Kor Scout // Legendary Creature — Kobold Warrior
- 流行度：EDHREC 全时段第 312 位，约 8555 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.29 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $5.27
- 社区标签：装备、主将单挑、快攻、神器、灵气、已改造生物
- 完整牌面：At the beginning of combat on your turn, you may attach any number of Auras and Equipment you control to target permanent or player.
Partner (You can have two commanders if both have partner.)
//
First strike, menace, trample
Partner (You can have two commanders if both have partner.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Colossus Hammer（{1}｜Artifact — Equipment） — Equipped creature gets +10/+10 and loses flying. Equip {8} ({8}: Attach to target creature you control. Equip only as a sorcery.)
  2. Puresteel Paladin（{W}{W}｜Creature — Human Knight） — Whenever an Equipment you control enters, you may draw a card. Metalcraft — Equipment you control have equip {0} as long as you control three or more artifacts.
  3. Sram, Senior Edificer（{1}{W}｜Legendary Creature — Dwarf Advisor） — Whenever you cast an Aura, Equipment, or Vehicle spell, draw a card.
  4. Open the Armory（{1}{W}｜Sorcery） — Search your library for an Aura or Equipment card, reveal it, put it into your hand, then shuffle.
  5. Masterwork of Ingenuity（{1}｜Artifact — Equipment） — You may have this Equipment enter as a copy of any Equipment on the battlefield.
  6. Steelshaper's Gift（{W}｜Sorcery） — Search your library for an Equipment card, reveal that card, put it into your hand, then shuffle.
- **出场率最高的牌**（大多数牌组都会放）
  - Blackblade Reforged（{2}｜Legendary Artifact — Equipment） — Equipped creature gets +1/+1 for each land you control. Equip legendary creature {3} Equip {7}
  - Akiri, Fearless Voyager（{1}{R}{W}｜Legendary Creature — Kor Warrior） — Whenever you attack a player with one or more equipped creatures, draw a card. {W}: You may unattach an Equipment from a creature 
  - Clifftop Retreat（｜Land） — This land enters tapped unless you control a Mountain or a Plains. {T}: Add {R} or {W}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t


## Krark, the Thumbless // Sakashima of a Thousand Faces ｜ 没有拇指的喀勒克 // 千面客逆岛
- 颜色 UR ｜ 法术力值 6.0 ｜ 类型 Legendary Creature — Goblin Wizard // Legendary Creature — Human Rogue
- 流行度：EDHREC 全时段第 520 位，约 5696 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.71 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $34.1
- 社区标签：法术连发、风暴、复制、组合技、掷硬币、混乱
- 完整牌面：Whenever you cast an instant or sorcery spell, flip a coin. If you lose the flip, return that spell to its owner's hand. If you win the flip, copy that spell, and you may choose new targets for the copy.
Partner (You can have two commanders if both have partner.)
//
You may have Sakashima enter as a copy of another creature you control, except it has Sakashima's other abilities.
The "legend rule" doesn't apply to permanents you control.
Partner (You can have two commanders if both have partner.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Tavern Scoundrel（{1}{R}｜Creature — Human Rogue） — Whenever you win a coin flip, create two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: Add one mana of any color.") {1}, {T}, Sacrifice another per
  2. Krark's Thumb（{2}｜Legendary Artifact） — If you would flip a coin, instead flip two coins and ignore one.
  3. Harmonic Prodigy（{1}{R}｜Creature — Human Wizard） — Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.) If a triggered ability of a Shaman or another Wizard you control triggers, th
  4. Veyran, Voice of Duality（{1}{U}{R}｜Legendary Creature — Efreet Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, Veyran gets +1/+1 until end of turn. If you casting or copying an instant or sorcery spell causes a tri
  5. Strike It Rich（{R}｜Sorcery） — Create a Treasure token. (It's an artifact with "{T}, Sacrifice this token: Add one mana of any color.") Flashback {2}{R} (You may cast this card from your graveyard for 
  6. Twinflame（{1}{R}｜Sorcery） — Strive — This spell costs {2}{R} more to cast for each target beyond the first. Choose any number of target creatures you control. For each of them, create a token that's
- **出场率最高的牌**（大多数牌组都会放）
  - Storm-Kiln Artist（{3}{R}｜Creature — Dwarf Shaman） — This creature gets +1/+0 for each artifact you control. Magecraft — Whenever you cast or copy an instant or sorcery spell, create 
  - Lightning Bolt（{R}｜Instant） — Lightning Bolt deals 3 damage to any target.
  - Archmage Emeritus（{2}{U}{U}｜Creature — Human Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, draw a card.
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.


## Owen Grady, Raptor Trainer // Blue, Loyal Raptor ｜ 迅猛龙驯师欧文·格雷迪 // 忠诚迅猛龙布鲁
- 颜色 URG ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Human Soldier Scientist // Legendary Creature — Dinosaur
- 流行度：EDHREC 全时段第 527 位，约 5640 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.4 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $13.09
- 社区标签：恐龙、＋1/＋1 指示物、快攻、指示物、Keruga Companion、加速
- 完整牌面：Partner with Blue, Loyal Raptor
{T}: Put your choice of a reach, menace, trample, or haste counter on target Dinosaur. Activate only as a sorcery.
//
Partner with Owen Grady, Raptor Trainer (When this creature enters, target player may put Owen into their hand from their library, then shuffle.)
For each kind of counter on Blue, Loyal Raptor, each other Dinosaur you control enters with a counter of that kind on it.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Cresting Mosasaurus（{6}{U}{U}｜Creature — Dinosaur） — Emerge {6}{U} (You may cast this spell by sacrificing a creature and paying the emerge cost reduced by that creature's mana value.) When this creature enters, if you cast
  2. Ghalta, Primal Hunger（{10}{G}{G}｜Legendary Creature — Elder Dinosaur） — This spell costs {X} less to cast, where X is the total power of creatures you control. Trample (This creature can deal excess combat damage to the player or planeswalker
  3. Earthshaker Dreadmaw（{4}{G}{G}｜Creature — Dinosaur） — Trample When this creature enters, draw a card for each other Dinosaur you control.
  4. Hulking Raptor（{2}{G}{G}｜Creature — Dinosaur） — Ward {2} At the beginning of your first main phase, add {G}{G}.
  5. Etali, Primal Storm（{4}{R}{R}｜Legendary Creature — Elder Dinosaur） — Whenever Etali attacks, exile the top card of each player's library, then you may cast any number of spells from among those cards without paying their mana costs.
  6. Quartzwood Crasher（{2}{R}{R}{G}｜Creature — Dinosaur Beast） — Trample Whenever one or more creatures you control with trample deal combat damage to a player, create an X/X green Dinosaur Beast creature token with trample, where X is
- **出场率最高的牌**（大多数牌组都会放）
  - Curious Altisaur（{3}{G}｜Creature — Dinosaur） — Reach, vigilance Whenever a Dinosaur you control deals combat damage to a player, draw a card.
  - Garruk's Uprising（{2}{G}｜Enchantment） — When this enchantment enters, if you control a creature with power 4 or greater, draw a card. Creatures you control have trample. 
  - Regisaur Alpha（{3}{R}{G}｜Creature — Dinosaur） — Other Dinosaurs you control have haste. When this creature enters, create a 3/3 green Dinosaur creature token with trample.
  - Hunting Velociraptor（{2}{R}｜Creature — Dinosaur） — First strike Dinosaur spells you cast have prowl {2}{R}. (You may cast a spell for its prowl cost if you dealt combat damage to a 
