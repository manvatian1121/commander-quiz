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


## Tevesh Szat, Doom of Fools // Thrasios, Triton Hero ｜ 愚者末日泰维司刹特 // 屈东英雄萨拉希洛斯
- 颜色 UBG ｜ 法术力值 7.0 ｜ 类型 Legendary Planeswalker — Szat // Legendary Creature — Merfolk Wizard
- 流行度：EDHREC 全时段第 991 位，约 2508 副套牌
- 常见强度档 Bracket 5 ｜ 咸度 0.57 ｜ 上手难度 4/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $6.7
- 社区标签：组合技、中速、诞生荚、控制、加速、优质单卡堆
- 完整牌面：+2: Create two 0/1 black Thrull creature tokens.
+1: You may sacrifice another creature or planeswalker. If you do, draw two cards, then draw another card if the sacrificed permanent was a commander.
−10: Gain control of all commanders. Put all commanders from the command zone onto the battlefield under your control.
Tevesh Szat, Doom of Fools can be your commander.
Partner
//
{4}: Scry 1, then reveal the top card of your library. If it's a land card, put it onto the battlefield tapped. Otherwise, draw a card.
Partner (You can have two commanders if both have partner.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Chrome Mox（{0}｜Artifact） — Imprint — When this artifact enters, you may exile a nonartifact, nonland card from your hand. {T}: Add one mana of any of the exiled card's colors.
  2. Mana Vault（{1}｜Artifact） — This artifact doesn't untap during your untap step. At the beginning of your upkeep, you may pay {4}. If you do, untap this artifact. At the beginning of your draw step, 
  3. Dark Ritual（{B}｜Instant） — Add {B}{B}{B}.
  4. Force of Will（{3}{U}{U}｜Instant） — You may pay 1 life and exile a blue card from your hand rather than pay this spell's mana cost. Counter target spell.
  5. Lotus Petal（{0}｜Artifact） — {T}, Sacrifice this artifact: Add one mana of any color.
  6. Flusterstorm（{U}｜Instant） — Counter target instant or sorcery spell unless its controller pays {1}. Storm (When you cast this spell, copy it for each spell cast before it this turn. You may choose n
- **出场率最高的牌**（大多数牌组都会放）
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Polluted Delta（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for an Island or Swamp card, put it onto the battlefield, then shuffle.
  - Misty Rainforest（｜Land） — {T}, Pay 1 life, Sacrifice this land: Search your library for a Forest or Island card, put it onto the battlefield, then shuffle.


## Cecily, Haunted Mage // Othelm, Sigardian Outcast ｜ 遭祟法师塞西莉 // 席嘉妲黜人奥塞姆
- 颜色 WUBRG ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Human Wizard // Legendary Creature — Human
- 流行度：EDHREC 全时段第 1002 位，约 2487 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.73 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $0.81
- 社区标签：线索、组合技、衍生物、神器、坟场复活、传奇
- 完整牌面：Your maximum hand size is eleven.
Whenever Cecily, Haunted Mage attacks, you draw a card and you lose 1 life. Then if you have eleven or more cards in your hand, you may cast an instant or sorcery spell from your hand without paying its mana cost.
Partner—Friends forever (You can have two commanders if both have this ability.)
//
{2}, {T}: Choose target creature card in your graveyard that was put there from the battlefield this turn. Return it to the battlefield tapped.
Partner—Friends forever (You can have two commanders if both have this ability.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Elmar, Ulvenwald Informant（{1}{R}{G}｜Legendary Creature — Human） — Haste Whenever you cast your second spell each turn, untap target creature, then investigate. (Create a colorless Clue artifact token with "{2}, Sacrifice this artifact: 
  2. Wernog, Rider's Chaplain（{W}{B}｜Legendary Creature — Human） — When Wernog, Rider's Chaplain enters or leaves the battlefield, each opponent may investigate. Each opponent who doesn't loses 1 life. You investigate X times, where X is
  3. Sophina, Spearsage Deserter（{2}{R}{W}｜Legendary Creature — Human Soldier） — Menace Whenever Sophina, Spearsage Deserter attacks, investigate once for each nontoken attacking creature. (To investigate, create a Clue token. It's an artifact with "{
  4. Hargilde, Kindly Runechanter（{2}{W}{U}｜Legendary Creature — Human） — {T}: Add {C}{C}. Spend this mana only to cast artifact spells or activate abilities of artifacts. Partner—Friends forever (You can have two commanders if both have this a
  5. Bjorna, Nightfall Alchemist（{U}{R}｜Legendary Creature — Human） — {T}, Sacrifice an artifact: Bjorna, Nightfall Alchemist deals 1 damage to target creature. Goad that creature. (Until your next turn, that creature attacks each combat if
  6. Ruinous Ultimatum（{R}{R}{W}{W}{W}{B}{B}｜Sorcery） — Destroy all nonland permanents your opponents control.
- **出场率最高的牌**（大多数牌组都会放）
  - Breeding Pool（｜Land — Forest Island） — ({T}: Add {G} or {U}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Birds of Paradise（{G}｜Creature — Bird） — Flying {T}: Add one mana of any color.
  - Temple Garden（｜Land — Forest Plains） — ({T}: Add {G} or {W}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.
  - Watery Grave（｜Land — Island Swamp） — ({T}: Add {U} or {B}.) As this land enters, you may pay 2 life. If you don't, it enters tapped.


## Rograkh, Son of Rohgahh // Yoshimaru, Ever Faithful ｜ 罗噶之子罗噶克 // 忠犬义丸
- 颜色 WR ｜ 法术力值 1.0 ｜ 类型 Legendary Creature — Kobold Warrior // Legendary Creature — Dog
- 流行度：EDHREC 全时段第 1003 位，约 2481 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.66 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $10.76
- 社区标签：传奇、史迹、快攻、装备、主将单挑、＋1/＋1 指示物
- 完整牌面：First strike, menace, trample
Partner (You can have two commanders if both have partner.)
//
Whenever another legendary permanent you control enters, put a +1/+1 counter on Yoshimaru.
Partner (You can have two commanders if both have partner.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Norin the Wary（{R}｜Legendary Creature — Human Warrior） — When a player casts a spell or a creature attacks, exile Norin. Return it to the battlefield under its owner's control at the beginning of the next end step.
  2. Mines of Moria（｜Legendary Land） — Mines of Moria enters tapped unless you control a legendary creature. {T}: Add {R}. {3}{R}, {T}, Exile three cards from your graveyard: Create two Treasure tokens.
  3. Flowering of the White Tree（{W}{W}｜Legendary Enchantment） — Legendary creatures you control get +2/+1 and have ward {1}. Nonlegendary creatures you control get +1/+1.
  4. Keleth, Sunmane Familiar（{1}{W}｜Legendary Creature — Horse） — Whenever a commander you control attacks, put a +1/+1 counter on it. Partner (You can have two commanders if both have partner.)
  5. Kediss, Emberclaw Familiar（{1}{R}｜Legendary Creature — Elemental Lizard） — Whenever a commander you control deals combat damage to an opponent, it deals that much damage to each other opponent. Partner (You can have two commanders if both have p
  6. Minas Tirith（｜Legendary Land） — Minas Tirith enters tapped unless you control a legendary creature. {T}: Add {W}. {1}{W}, {T}: Draw a card. Activate only if you attacked with two or more creatures this 
- **出场率最高的牌**（大多数牌组都会放）
  - Eiganjo, Seat of the Empire（｜Legendary Land） — {T}: Add {W}. Channel — {2}{W}, Discard this card: It deals 4 damage to target attacking or blocking creature. This ability costs 
  - Path to Exile（{W}｜Instant） — Exile target creature. Its controller may search their library for a basic land card, put that card onto the battlefield tapped, t
  - Sokenzan, Crucible of Defiance（｜Legendary Land） — {T}: Add {R}. Channel — {3}{R}, Discard this card: Create two 1/1 colorless Spirit creature tokens. They gain haste until end of t
  - Urza's Ruinous Blast（{4}{W}｜Legendary Sorcery） — (You may cast a legendary sorcery only if you control a legendary creature or planeswalker.) Exile all nonland permanents that are
