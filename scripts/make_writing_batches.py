#!/usr/bin/env python3
"""生成写作素材包：每位主将一份资料卡，含真实牌面 + EDHREC 实测搭配牌。"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
BATCHES = 8

STYLE = """# 写作规范（务必先读）

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
"""


def main() -> None:
    payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    scry = json.loads((DATA / "commanders_scryfall.json").read_text(encoding="utf-8"))
    verified = json.loads((DATA / "card_verified.json").read_text(encoding="utf-8"))
    display = json.loads((DATA / "card_display.json").read_text(encoding="utf-8"))
    tag_zh = json.loads((DATA / "tag_zh.json").read_text(encoding="utf-8"))

    lookup = {}
    for name, card in scry.items():
        lookup[name] = card
        lookup.setdefault(name.split(" // ")[0], card)

    # 增量模式：只给还没有介绍文的主将出素材（用于扩池后补写）
    existing: set[str] = set()
    for index in range(1, 17):
        path = DATA / f"descriptions_{index}.json"
        if path.exists():
            existing |= set(json.loads(path.read_text(encoding="utf-8")))
    if existing:
        print(f"已有介绍文 {len(existing)} 篇，本次只处理缺的那些")

    commanders = [c for c in sorted(payload["commanders"],
                                    key=lambda c: c["all_time_rank"] or 9999)
                  if c["en"] not in existing]
    if not commanders:
        print("✓ 没有缺介绍文的主将")
        return
    print(f"待写 {len(commanders)} 位，分 {BATCHES} 批")
    per_batch = -(-len(commanders) // BATCHES)

    for batch in range(BATCHES):
        chunk = commanders[batch * per_batch:(batch + 1) * per_batch]
        if not chunk:
            continue
        lines = [STYLE, "\n---\n", f"# 素材：{len(chunk)} 位主将\n"]
        for card in chunk:
            name = card["en"]
            source = lookup.get(name) or lookup.get(name.split(" // ")[0]) or {}
            entry = display.get(name) or {"synergy": [], "popular": []}
            lines.append(f"\n## {name} ｜ {card['zh']}")
            lines.append(f"- 颜色 {card['colors']} ｜ 法术力值 {card['cmc']} ｜ 类型 {card['type']}")
            lines.append(f"- 流行度：EDHREC 全时段第 {card['all_time_rank']} 位，"
                         f"约 {card['num_decks']} 副套牌")
            lines.append(f"- 常见强度档 Bracket {card['bracket']} ｜ 咸度 {card['salt']} ｜ "
                         f"上手难度 {card['complexity']}/5 ｜ 造价档位 {card['budget']}/5 ｜ "
                         f"单卡参考价 ${card['usd']}")
            lines.append(f"- 社区标签：{'、'.join(tag_zh.get(t, t) for t in card['top_tags'])}")
            lines.append(f"- 完整牌面：{(source.get('oracle_text') or '').strip()}")

            lines.append("- **协同度最高的牌**（EDHREC 实测：专门为它而来的人最多）")
            for index, cname in enumerate(entry["synergy"], 1):
                info = verified.get(cname) or {}
                text = " ".join((info.get("oracle_text") or "").split())[:170]
                lines.append(f"  {index}. {cname}"
                             f"（{info.get('mana_cost', '')}｜{info.get('type_line', '')}）"
                             f" — {text}")
            if entry["popular"]:
                lines.append("- **出场率最高的牌**（大多数牌组都会放）")
                for cname in entry["popular"]:
                    info = verified.get(cname) or {}
                    text = " ".join((info.get("oracle_text") or "").split())[:130]
                    lines.append(f"  - {cname}"
                                 f"（{info.get('mana_cost', '')}｜{info.get('type_line', '')}）"
                                 f" — {text}")
            lines.append("")

        path = DATA / f"writing_batch_new_{batch + 1}.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"✓ {path.name}：{len(chunk)} 位主将，{len('\\n'.join(lines)) / 1024:.0f} KB")

    print("\n主将总数", len(commanders))


if __name__ == "__main__":
    main()
