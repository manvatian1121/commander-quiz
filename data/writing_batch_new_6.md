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

# 素材：2 位主将


## Karlach, Fury of Avernus // Sword Coast Sailor ｜ 禽绝地狱之怒卡莱琪 // 剑湾水手
- 颜色 UR ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Tiefling Barbarian // Legendary Enchantment — Background
- 流行度：EDHREC 全时段第 1427 位，约 1363 副套牌
- 常见强度档 Bracket 3 ｜ 咸度 0.61 ｜ 上手难度 2/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $20.42
- 社区标签：额外战斗、主将单挑、快攻、装备、宝物、额外回合
- 完整牌面：Whenever you attack, if it's the first combat phase of the turn, untap all attacking creatures. They gain first strike until end of turn. After this phase, there is an additional combat phase.
Choose a Background (You can have a Background as a second commander.)
//
Commander creatures you own have "Whenever this creature attacks a player, if no opponent has more life than that player, this creature can't be blocked this turn."
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Kediss, Emberclaw Familiar（{1}{R}｜Legendary Creature — Elemental Lizard） — Whenever a commander you control deals combat damage to an opponent, it deals that much damage to each other opponent. Partner (You can have two commanders if both have p
  2. Two-Handed Axe（｜） — 
  3. Combat Celebrant（{2}{R}｜Creature — Human Warrior） — If this creature hasn't been exerted this turn, you may exert it as it attacks. When you do, untap all other creatures you control and after this phase, there is an addit
  4. Combat Research（{U}｜Enchantment — Aura） — Enchant creature Enchanted creature has "Whenever this creature deals combat damage to a player, draw a card." As long as enchanted creature is legendary, it gets +1/+1 a
  5. Professional Face-Breaker（{2}{R}｜Creature — Human Warrior） — Menace Whenever one or more creatures you control deal combat damage to a player, create a Treasure token. Sacrifice a Treasure: Exile the top card of your library. You m
  6. Lizard Blades（{1}{R}｜Artifact Creature — Equipment Lizard） — Double strike Equipped creature has double strike. Reconfigure {2} ({2}: Attach to target creature you control; or unattach from a creature. Reconfigure only as a sorcery
- **出场率最高的牌**（大多数牌组都会放）
  - Sulfur Falls（｜Land） — This land enters tapped unless you control an Island or a Mountain. {T}: Add {U} or {R}.
  - Shivan Reef（｜Land） — {T}: Add {C}. {T}: Add {U} or {R}. This land deals 1 damage to you.
  - Izzet Signet（{2}｜Artifact） — {1}, {T}: Add {U}{R}.
  - Talisman of Creativity（{2}｜Artifact） — {T}: Add {C}. {T}: Add {U} or {R}. This artifact deals 1 damage to you.


## Shadowheart, Dark Justiciar // Haunted One ｜ 暗夜法官影心 // 溺往苦主
- 颜色 B ｜ 法术力值 7.0 ｜ 类型 Legendary Creature — Human Elf Cleric // Legendary Enchantment — Background
- 流行度：EDHREC 全时段第 1578 位，约 1139 副套牌
- 常见强度档 Bracket 2 ｜ 咸度 0.18 ｜ 上手难度 3/5 ｜ 造价档位 5/5 ｜ 单卡参考价 $1.39
- 社区标签：牺牲流、坟场复活、僧侣、牺牲、人类、影裔使徒
- 完整牌面：{1}{B}, {T}, Sacrifice another creature: Draw X cards, where X is that creature's power.
Choose a Background (You can have a Background as a second commander.)
//
Commander creatures you own have "Whenever this creature becomes tapped, it and other creatures you control that share a creature type with it each get +2/+0 and gain undying until end of turn." (When a creature with undying dies, if it had no +1/+1 counters on it, return it to the battlefield under its owner's control with a +1/+1 counter on it.)
- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）
  1. Taborax, Hope's Demise（{2}{B}｜Legendary Creature — Demon Cleric） — Flying Taborax has lifelink as long as it has five or more +1/+1 counters on it. Whenever another nontoken creature you control dies, put a +1/+1 counter on Taborax. If t
  2. Shadow-Rite Priest（{1}{B}｜Creature — Human Cleric） — Other Clerics you control get +1/+1. {3}{B}{B}, {T}, Sacrifice another Cleric: Search your library for a black creature card, put it onto the battlefield, then shuffle.
  3. Priest of Forgotten Gods（{1}{B}｜Creature — Human Cleric） — {T}, Sacrifice two other creatures: Any number of target players each lose 2 life and sacrifice a creature of their choice. You add {B}{B} and draw a card. (Activate only
  4. Doomed Necromancer（{2}{B}｜Creature — Human Cleric Mercenary） — {B}, {T}, Sacrifice this creature: Return target creature card from your graveyard to the battlefield.
  5. Twilight Diviner（{2}{B}｜Creature — Elf Cleric） — When this creature enters, surveil 2. (Look at the top two cards of your library, then put any number of them into your graveyard and the rest on top of your library in a
  6. Priest of Gix（{2}{B}｜Creature — Phyrexian Human Cleric Minion） — When this creature enters, add {B}{B}{B}.
- **出场率最高的牌**（大多数牌组都会放）
  - Victimize（{2}{B}｜Sorcery） — Choose two target creature cards in your graveyard. Sacrifice a creature. If you do, return the chosen cards to the battlefield ta
  - Ayara, First of Locthwain（{B}{B}{B}｜Legendary Creature — Elf Noble） — Whenever Ayara or another black creature you control enters, each opponent loses 1 life and you gain 1 life. {T}, Sacrifice anothe
  - Zulaport Cutthroat（{1}{B}｜Creature — Human Rogue Ally） — Whenever this creature or another creature you control dies, each opponent loses 1 life and you gain 1 life.
  - Black Market（{3}{B}{B}｜Enchantment） — Whenever a creature dies, put a charge counter on this enchantment. At the beginning of your first main phase, add {B} for each ch
