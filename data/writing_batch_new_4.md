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


## Pir, Imaginative Rascal // Toothy, Imaginary Friend ｜ 奇想顽童皮儿 // 奇妙伙伴大牙
- 颜色 UG ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Human // Legendary Creature — Illusion
- 流行度：EDHREC 全时段第 862 位，约 3088 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.36 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $15.86
- 社区标签：＋1/＋1 指示物、抽牌、闪现回场、鹏洛客、主将单挑、小牌抽
- 完整牌面：Partner with Toothy, Imaginary Friend (When this creature enters, target player may put Toothy into their hand from their library, then shuffle.)
If one or more counters would be put on a permanent your team controls, that many plus one of each of those kinds of counters are put on that permanent instead.
//
Partner with Pir, Imaginative Rascal (When this creature enters, target player may put Pir into their hand from their library, then shuffle.)
Whenever you draw a card, put a +1/+1 counter on Toothy.
When Toothy leaves the battlefield, draw a card for each +1/+1 counter on it.
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Hardened Scales（{G}｜Enchantment） — If one or more +1/+1 counters would be put on a creature you control, that many plus one +1/+1 counters are put on it instead.
  2. Forgotten Ancient（{3}{G}｜Creature — Elemental） — Whenever a player casts a spell, you may put a +1/+1 counter on this creature. At the beginning of your upkeep, you may move any number of +1/+1 counters from this creatu
  3. Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.
  4. Simic Ascendancy（{G}{U}｜Enchantment） — {1}{G}{U}: Put a +1/+1 counter on target creature you control. Whenever one or more +1/+1 counters are put on a creature you control, put that many growth counters on thi
  5. Essence Flux（{U}｜Instant） — Exile target creature you control, then return that card to the battlefield under its owner's control. If it's a Spirit, put a +1/+1 counter on it.
  6. Laboratory Maniac（{2}{U}｜Creature — Human Wizard） — If you would draw a card while your library has no cards in it, you win the game instead.
- **出场率最高的牌**（大多数牌组都会放）
  - Hinterland Harbor（｜Land） — This land enters tapped unless you control a Forest or an Island. {T}: Add {G} or {U}.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Yavimaya Coast（｜Land） — {T}: Add {C}. {T}: Add {G} or {U}. This land deals 1 damage to you.
  - Rejuvenating Springs（｜Land） — This land enters tapped unless you have two or more opponents. {T}: Add {G} or {U}.


## Gale, Waterdeep Prodigy // Scion of Halaster ｜ 深水城逸才盖尔 // 海拉斯特的后裔
- 颜色 UB ｜ 法术力值 5.0 ｜ 类型 Legendary Creature — Human Wizard // Legendary Enchantment — Background
- 流行度：EDHREC 全时段第 898 位，约 2915 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.21 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.7
- 社区标签：法术连发、控制、磨牌、组合技、坟场复活、坟场
- 完整牌面：Whenever you cast an instant or sorcery spell from your hand, you may cast up to one target card of the other type from your graveyard. If a spell cast from your graveyard this way would be put into your graveyard, exile it instead.
Choose a Background (You can have a Background as a second commander.)
//
Commander creatures you own have "The first time you would draw a card each turn, instead look at the top two cards of your library. Put one of them into your graveyard and the other back on top of your library. Then draw a card."
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Consider（{U}｜Instant） — Surveil 1. (Look at the top card of your library. You may put it into your graveyard.) Draw a card.
  2. Thought Scour（{U}｜Instant） — Target player mills two cards. Draw a card.
  3. Frantic Search（{2}{U}｜Instant） — Draw two cards, then discard two cards. Untap up to three lands.
  4. See the Truth（{1}{U}｜Sorcery） — Look at the top three cards of your library. Put one of those cards into your hand and the rest on the bottom of your library in any order. If this spell was cast from an
  5. Archmage Emeritus（{2}{U}{U}｜Creature — Human Wizard） — Magecraft — Whenever you cast or copy an instant or sorcery spell, draw a card.
  6. Baral, Chief of Compliance（{1}{U}｜Legendary Creature — Human Wizard） — Instant and sorcery spells you cast cost {1} less to cast. Whenever a spell or ability you control counters a spell, you may draw a card. If you do, discard a card.
- **出场率最高的牌**（大多数牌组都会放）
  - Sunken Hollow（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) This land enters tapped unless you control two or more basic lands.
  - Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  - Ponder（{U}｜Sorcery） — Look at the top three cards of your library, then put them back in any order. You may shuffle. Draw a card.
  - Brainstorm（{U}｜Instant） — Draw three cards, then put two cards from your hand on top of your library in any order.


## Sakashima of a Thousand Faces // Vial Smasher the Fierce ｜ 千面客逆岛 // 砸瓶女汉子
- 颜色 UBR ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Human Rogue // Legendary Creature — Goblin Berserker
- 流行度：EDHREC 全时段第 983 位，约 2524 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.9 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $35.73
- 社区标签：复制、烧血、混乱、法术连发、群体折磨、控制
- 完整牌面：You may have Sakashima enter as a copy of another creature you control, except it has Sakashima's other abilities.
The "legend rule" doesn't apply to permanents you control.
Partner (You can have two commanders if both have partner.)
//
Whenever you cast your first spell each turn, choose an opponent at random. Vial Smasher deals damage equal to that spell's mana value to that player or a planeswalker that player controls.
Partner (You can have two commanders if both have partner.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Phyrexian Metamorph（{3}{U/P}｜Artifact Creature — Phyrexian Shapeshifter） — ({U/P} can be paid with either {U} or 2 life.) You may have this creature enter as a copy of any artifact or creature on the battlefield, except it's an artifact in addit
  2. Dig Through Time（{6}{U}{U}｜Instant） — Delve (Each card you exile from your graveyard while casting this spell pays for {1}.) Look at the top seven cards of your library. Put two of them into your hand and the
  3. Clever Impersonator（{2}{U}{U}｜Creature — Shapeshifter） — You may have this creature enter as a copy of any nonland permanent on the battlefield.
  4. Spark Double（{3}{U}｜Creature — Illusion） — You may have this creature enter as a copy of a creature or planeswalker you control, except it enters with an additional +1/+1 counter on it if it's a creature, it enter
  5. Treasure Cruise（{7}{U}｜Sorcery） — Delve (Each card you exile from your graveyard while casting this spell pays for {1}.) Draw three cards.
  6. Glasspool Mimic（｜） — 
- **出场率最高的牌**（大多数牌组都会放）
  - Blasphemous Act（{8}{R}｜Sorcery） — This spell costs {1} less to cast for each creature on the battlefield. Blasphemous Act deals 13 damage to each creature.
  - Steam Vents（｜Land — Island Mountain） — ({T}: Add {U} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Blood Crypt（｜Land — Swamp Mountain） — ({T}: Add {B} or {R}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
