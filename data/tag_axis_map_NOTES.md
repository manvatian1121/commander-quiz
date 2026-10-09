# tag_axis_map.json 交付说明

## 产物
- `data/tag_axis_map.json` — 映射表（`mapped` 376 / `ignored` 28）
- `scripts/gen_axis_map.py` — 生成器 + 双向 diff 自检（`--write` 才落盘）
- `scripts/verify_axis_map.py` — 独立校验（重新解析词表与 JSON，不复用生成器逻辑）
- `scripts/smoke_axis_map.py` — 用 151 位主将真实票数跑向量，肉眼核对

## 自检结果
```
词表: 404 个标签
总计 404 / mapped 376 / ignored 28 / 和 404 -> 自检通过
20 轴全部被引用；每标签最多 3 个轴；权重仅 0.5/1.0/1.5/2.0
```
独立校验（`verify_axis_map.py`）：404 全覆盖、无重复、无词表外标签、权重合法。
未映射标签在 151 位主将数据中出现的全部 28 种**恰好等于** `ignored` 名单（无静默漏映射）。

## 轴覆盖（标签数 / 权重和）
tribal 155 | aggro 52 | counters 44 | spells 36 | artifacts 34 | wide 31 |
stompy 30 | grave 30 | combo 30 | ramp 28 | control 22 | drain 21 | chaos 20 |
stax 18 | removal 18 | voltron 15 | politics 12 | blink 11 | clonesteal 10 | enchant 9

## 抽样验证（真实票数 × 权重，取最高轴）
| 主将 | 结果 |
|---|---|
| Atraxa, Praetors' Voice | counters 55% |
| Krenko, Mob Boss | wide 37% / tribal 31% / aggro 19% |
| Muldrotha | grave 61% |
| Meren of Clan Nel Toth | grave 57% / drain 22% |
| Sram, Senior Edificer | voltron 47% / artifacts 26% |
| Brago, King Eternal | blink 52% |
| Tergrid, God of Fright | stax 41% / grave 22% |
| Talrand, Sky Summoner | spells 44% / wide 22% |
| Phenax, God of Deception | grave 45% / stax 26% |
| Light-Paws | enchant 44% / voltron 43% |
| Yarok | ramp 39% / blink 23% |
| Grand Arbiter Augustin IV | stax 58% |
| Xenagos, God of Revels | aggro 47% / stompy 15% |
| Niv-Mizzet, Parun | spells 47% |

## 新机制判定依据（查过规则书 / 官方发布）
| 标签 | 实际效果 | 映射 |
|---|---|---|
| Airbending | 放逐永久物/咒语，其拥有者可付{2}施放（CR 701.65） | removal 1.0, blink 0.5 |
| Earthbending | 地变 0/0 haste 生物 + 等量 +1/+1，死后回场（CR 701.66） | ramp 1.0, counters 1.0, aggro 0.5 |
| Waterbending | 支付费用时每点通用法术力可改为横置神器/生物（CR 701.67） | artifacts 1.0, ramp 0.5 |
| Firebending | 攻击时加等量红法术力，仅限本次战斗（CR 702.189） | spells 1.0, aggro 0.5 |
| Summons | FF 的「召唤」是 Saga 型生物（如 Summon: Bahamut {9}） | ramp 1.0, stompy 0.5 |
| Paradigm | 每回合主阶段前免费复制该咒语并施放（CR 702.192） | spells 1.0, combo 0.5 |
| Increment | 施放费用大于其攻防的咒语时 +1/+1（CR 702.191） | counters 1.0 |
| Storied | 3 个神器/传纪/传奇永久物即获「传诵」（CR 702.195） | enchant 0.5 |
| Blight | 给自己生物放 -1/-1（CR 701.68） | counters 1.0, drain 0.5 |
| Stun | 眩晕指示物：阻止重置（CR 122.1d） | stax 1.0 |
| Opus / Repartee / Paradox | CR 207.2c 能力词，无独立规则义 | 前两个 ignored；Paradox 给 chaos 0.5 |

## 最难的取舍
1. **Mill 没有对应轴** → `grave 1.5 + stax 1.0`。自磨是坟场资源，对对手磨牌是剥夺资源。
2. **Flying / Haste / Deathtouch 等纯关键词** → 除 Deathtouch 给 `removal 0.5`（规则上确属
   互动）外全部 ignored。按题面「关键词不构成原型」处理，避免 aggro 被关键词噪声抬高。
3. **Lifegain 不是 drain**（drain 轴定义是吸取对手生命）→ `drain 1.0 + counters 0.5`，
   理由是回血是 drain 玩法的燃料，且大量回血主将走 +1/+1 成长。
4. **Combo 给 1.5 而非忽略** —— 151/151 都有但票数有区分度，按题目要求映射。
5. **Cid** 不在官方 205.3m 生物类别表里，是主将人物名标签 → ignored。
