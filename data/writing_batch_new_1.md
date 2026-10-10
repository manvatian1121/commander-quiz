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


## Thrasios, Triton Hero // Tymna the Weaver ｜ 屈东英雄萨拉希洛斯 // 织命使堤谟娜
- 颜色 WUBG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Merfolk Wizard // Legendary Creature — Human Cleric
- 流行度：EDHREC 全时段第 209 位，约 11442 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 1.34 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.0
- 社区标签：诞生荚、组合技、中速、优质单卡堆、控制、苦痛抽牌
- 完整牌面：{4}: Scry 1, then reveal the top card of your library. If it's a land card, put it onto the battlefield tapped. Otherwise, draw a card.
Partner (You can have two commanders if both have partner.)
//
Lifelink
At the beginning of each of your postcombat main phases, you may pay X life, where X is the number of opponents that were dealt combat damage this turn. If you do, draw X cards.
Partner (You can have two commanders if both have partner.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Silence（{W}｜Instant） — Your opponents can't cast spells this turn.
  2. Thassa's Oracle（{U}{U}｜Creature — Merfolk Wizard） — When this creature enters, look at the top X cards of your library, where X is your devotion to blue. Put up to one of them on top of your library and the rest on the bot
  3. Devoted Druid（{1}{G}｜Creature — Elf Druid） — {T}: Add {G}. Put a -1/-1 counter on this creature: Untap this creature.
  4. Flusterstorm（{U}｜Instant） — Counter target instant or sorcery spell unless its controller pays {1}. Storm (When you cast this spell, copy it for each spell cast before it this turn. You may choose n
  5. Chrome Mox（{0}｜Artifact） — Imprint — When this artifact enters, you may exile a nonartifact, nonland card from your hand. {T}: Add one mana of any of the exiled card's colors.
  6. Lotus Petal（{0}｜Artifact） — {T}, Sacrifice this artifact: Add one mana of any color.
- **出场率最高的牌**（大多数牌组都会放）
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Polluted Delta（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for an Island or Swamp card, put it onto the battlefield, then shuffle.
  - Misty Rainforest（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Island card, put it onto the battlefield, then shuffle.
  - Flooded Strand（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Plains or Island card, put it onto the battlefield, then shuffle.


## Okaun, Eye of Chaos // Zndrsplt, Eye of Wisdom ｜ 混沌之眼欧寇然 // 智慧之眼岑斯莉
- 颜色 UR ｜ 法术力值 10.0 ｜ 类型 Legendary Creature — Cyclops Berserker // Legendary Creature — Homunculus
- 流行度：EDHREC 全时段第 247 位，约 10064 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.07 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.95
- 社区标签：混乱、掷硬币、主将单挑、组合技、抽牌、快攻
- 完整牌面：Partner with Zndrsplt, Eye of Wisdom (When this creature enters, target player may put Zndrsplt into their hand from their library, then shuffle.)
At the beginning of combat on your turn, flip a coin until you lose a flip.
Whenever a player wins a coin flip, double Okaun's power and toughness until end of turn.
//
Partner with Okaun, Eye of Chaos (When this creature enters, target player may put Okaun into their hand from their library, then shuffle.)
At the beginning of combat on your turn, flip a coin until you lose a flip.
Whenever a player wins a coin flip, draw a card.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Krark's Thumb（{2}｜Legendary Artifact） — If you would flip a coin, instead flip two coins and ignore one.
  2. Tavern Scoundrel（{1}{R}｜Creature — Human Rogue） — Whenever you win a coin flip, create two Treasure tokens. (They're artifacts with "{T}, Sacrifice this token: Add one mana of any color.") {1}, {T}, Sacrifice another per
  3. Yusri, Fortune's Flame（{1}{U}{R}｜Legendary Creature — Efreet） — Flying Whenever Yusri attacks, choose a number between 1 and 5. Flip that many coins. For each flip you win, draw a card. For each flip you lose, Yusri deals 2 damage to 
  4. Stitch in Time（{1}{U}{R}｜Sorcery） — Flip a coin. If you win the flip, take an extra turn after this one.
  5. Chance Encounter（{2}{R}{R}｜Enchantment） — Whenever you win a coin flip, put a luck counter on this enchantment. At the beginning of your upkeep, if this enchantment has ten or more luck counters on it, you win th
  6. Fiery Gambit（{2}{R}｜Sorcery） — Flip a coin until you lose a flip or choose to stop flipping. If you lose a flip, Fiery Gambit has no effect. If you win one or more flips, Fiery Gambit deals 3 damage to
- **出场率最高的牌**（大多数牌组都会放）
  - Squee's Revenge（{1}{U}{R}｜Sorcery） — Choose a number. Flip a coin that many times or until you lose a flip, whichever comes first. If you win all the flips, draw two c
  - Krark, the Thumbless（{1}{R}｜Legendary Creature — Goblin Wizard） — Whenever you cast an instant or sorcery spell, flip a coin. If you lose the flip, return that spell to its owner's hand. If you wi
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Planar Chaos（{2}{R}｜Enchantment） — At the beginning of your upkeep, flip a coin. If you lose the flip, sacrifice this enchantment. Whenever a player casts a spell, t


## Rograkh, Son of Rohgahh // Thrasios, Triton Hero ｜ 罗噶之子罗噶克 // 屈东英雄萨拉希洛斯
- 颜色 URG ｜ 法术力值 2.0 ｜ 类型 Legendary Creature — Kobold Warrior // Legendary Creature — Merfolk Wizard
- 流行度：EDHREC 全时段第 275 位，约 9275 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.66 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $2.12
- 社区标签：组合技、诞生荚、中速、加速、地牌核心、风暴
- 完整牌面：First strike, menace, trample
Partner (You can have two commanders if both have partner.)
//
{4}: Scry 1, then reveal the top card of your library. If it's a land card, put it onto the battlefield tapped. Otherwise, draw a card.
Partner (You can have two commanders if both have partner.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mox Amber（{0}｜Legendary Artifact） — {T}: Add one mana of any color among legendary creatures and planeswalkers you control.
  2. Springleaf Drum（{1}｜Artifact） — {T}, Tap an untapped creature you control: Add one mana of any color.
  3. Chrome Mox（{0}｜Artifact） — Imprint — When this artifact enters, you may exile a nonartifact, nonland card from your hand. {T}: Add one mana of any of the exiled card's colors.
  4. Gaea's Cradle（｜Legendary Land） — {T}: Add {G} for each creature you control.
  5. Crop Rotation（{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for a land card, put that card onto the battlefield, then shuffle.
  6. Mox Diamond（{0}｜Artifact） — If this artifact would enter, you may discard a land card instead. If you do, put this artifact onto the battlefield. If you don't, put it into its owner's graveyard. {T}
- **出场率最高的牌**（大多数牌组都会放）
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Misty Rainforest（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Island card, put it onto the battlefield, then shuffle.
  - Scalding Tarn（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for an Island or Mountain card, put it onto the battlefield, then shuffl
  - Wooded Foothills（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Mountain or Forest card, put it onto the battlefield, then shuffle
