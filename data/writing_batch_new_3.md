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


## Thrasios, Triton Hero // Vial Smasher the Fierce ｜ 屈东英雄萨拉希洛斯 // 砸瓶女汉子
- 颜色 UBRG ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Merfolk Wizard // Legendary Creature — Goblin Berserker
- 流行度：EDHREC 全时段第 645 位，约 4538 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 1.34 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $3.21
- 社区标签：组合技、中速、诞生荚、控制、加速、优质单卡堆
- 完整牌面：{4}: Scry 1, then reveal the top card of your library. If it's a land card, put it onto the battlefield tapped. Otherwise, draw a card.
Partner (You can have two commanders if both have partner.)
//
Whenever you cast your first spell each turn, choose an opponent at random. Vial Smasher deals damage equal to that spell's mana value to that player or a planeswalker that player controls.
Partner (You can have two commanders if both have partner.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Seedborn Muse（{3}{G}{G}｜Creature — Spirit） — Untap all permanents you control during each other player's untap step.
  2. Force of Will（{3}{U}{U}｜Instant） — You may pay 1 life and exile a blue card from your hand rather than pay this spell's mana cost. Counter target spell.
  3. Training Grounds（{U}｜Enchantment） — Activated abilities of creatures you control cost {2} less to activate. This effect can't reduce the mana in that cost to less than one mana.
  4. Mystic Remora（{U}｜Enchantment） — Cumulative upkeep {1} (At the beginning of your upkeep, put an age counter on this permanent, then sacrifice it unless you pay its upkeep cost for each age counter on it.
  5. Fierce Guardianship（{2}{U}｜Instant） — If you control a commander, you may cast this spell without paying its mana cost. Counter target noncreature spell.
  6. Swan Song（{U}｜Instant） — Counter target enchantment, instant, or sorcery spell. Its controller creates a 2/2 blue Bird creature token with flying.
- **出场率最高的牌**（大多数牌组都会放）
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Polluted Delta（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for an Island or Swamp card, put it onto the battlefield, then shuffle.
  - Misty Rainforest（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Island card, put it onto the battlefield, then shuffle.
  - Wooded Foothills（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Mountain or Forest card, put it onto the battlefield, then shuffle


## Thrasios, Triton Hero // Yoshimaru, Ever Faithful ｜ 屈东英雄萨拉希洛斯 // 忠犬义丸
- 颜色 WUG ｜ 法术力值 3.0 ｜ 类型 Legendary Creature — Merfolk Wizard // Legendary Creature — Dog
- 流行度：EDHREC 全时段第 655 位，约 4490 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 1.34 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $8.64
- 社区标签：组合技、中速、诞生荚、传奇、地牌核心、＋1/＋1 指示物
- 完整牌面：{4}: Scry 1, then reveal the top card of your library. If it's a land card, put it onto the battlefield tapped. Otherwise, draw a card.
Partner (You can have two commanders if both have partner.)
//
Whenever another legendary permanent you control enters, put a +1/+1 counter on Yoshimaru.
Partner (You can have two commanders if both have partner.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Mox Amber（{0}｜Legendary Artifact） — {T}: Add one mana of any color among legendary creatures and planeswalkers you control.
  2. Training Grounds（{U}｜Enchantment） — Activated abilities of creatures you control cost {2} less to activate. This effect can't reduce the mana in that cost to less than one mana.
  3. Finale of Devastation（{X}{G}{G}｜Sorcery） — Search your library and/or graveyard for a creature card with mana value X or less and put it onto the battlefield. If you search your library this way, shuffle. If X is 
  4. Silence（{W}｜Instant） — Your opponents can't cast spells this turn.
  5. Gaea's Cradle（｜Legendary Land） — {T}: Add {G} for each creature you control.
  6. Crop Rotation（{G}｜Instant） — As an additional cost to cast this spell, sacrifice a land. Search your library for a land card, put that card onto the battlefield, then shuffle.
- **出场率最高的牌**（大多数牌组都会放）
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Windswept Heath（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Plains card, put it onto the battlefield, then shuffle.
  - Misty Rainforest（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Island card, put it onto the battlefield, then shuffle.


## Brallin, Skyshark Rider // Shabraz, the Skyshark ｜ 空鲨骑手布雷林 // 空鲨沙布拉兹
- 颜色 WUR ｜ 法术力值 9.0 ｜ 类型 Legendary Creature — Human Shaman // Legendary Creature — Shark Bird
- 流行度：EDHREC 全时段第 722 位，约 3936 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.31 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $14.15
- 社区标签：换手牌、弃牌、循环、＋1/＋1 指示物、抽牌、组合技
- 完整牌面：Partner with Shabraz, the Skyshark (When this creature enters, target player may put Shabraz into their hand from their library, then shuffle.)
Whenever you discard a card, put a +1/+1 counter on Brallin and it deals 1 damage to each opponent.
{R}: Target Shark gains trample until end of turn.
//
Partner with Brallin, Skyshark Rider
Flying
Whenever you draw a card, put a +1/+1 counter on Shabraz and you gain 1 life.
{W/U}: Target Human gains flying until end of turn.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Windfall（{2}{U}｜Sorcery） — Each player discards their hand, then draws cards equal to the greatest number of cards a player discarded this way.
  2. Faithless Looting（{R}｜Sorcery） — Draw two cards, then discard two cards. Flashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then exile it.)
  3. Glint-Horn Buccaneer（{1}{R}{R}｜Creature — Minotaur Pirate） — Haste Whenever you discard a card, this creature deals 1 damage to each opponent. {1}{R}, Discard a card: Draw a card. Activate only if this creature is attacking.
  4. Tolarian Winds（{1}{U}｜Instant） — Discard all the cards in your hand, then draw that many cards.
  5. Curiosity（{U}｜Enchantment — Aura） — Enchant creature Whenever enchanted creature deals damage to an opponent, you may draw a card.
  6. Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.
- **出场率最高的牌**（大多数牌组都会放）
  - Mystic Monastery（｜Land） — This land enters tapped. {T}: Add {U}, {R}, or {W}.
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Rielle, the Everwise（{1}{U}{R}｜Legendary Creature — Human Wizard） — Rielle gets +1/+0 for each instant and sorcery card in your graveyard. Whenever you discard one or more cards for the first time e
  - Talisman of Creativity（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {R}. This artifact deals 1 damage to you.
