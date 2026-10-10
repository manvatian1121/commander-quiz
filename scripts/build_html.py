#!/usr/bin/env python3
"""把数据注入 HTML 模板，生成单文件可交互测验。"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)
DATA = ROOT / "data"

AXES = {
    "aggro": {"zh": "快攻压制", "desc": "低费生物早早铺开，抢先手把人打死"},
    "voltron": {"zh": "主将单挑", "desc": "把主将本人养成巨威胁，靠主将伤害取胜"},
    "wide": {"zh": "铺场爆兵", "desc": "造一大堆小兵，人多打人少"},
    "ramp": {"zh": "加速爆费", "desc": "疯狂找地加速，早早打出超大咒语"},
    "stompy": {"zh": "大生物压制", "desc": "单只巨兽就够吓人，硬碰硬"},
    "control": {"zh": "控制反击", "desc": "反击咒语、清场，拖到后期靠资源优势赢"},
    "removal": {"zh": "精准互动", "desc": "点杀、拆神器结界，见招拆招"},
    "combo": {"zh": "组合技", "desc": "找齐特定几张牌凑成无限连"},
    "spells": {"zh": "法术连发", "desc": "以瞬间法术为主，一回合连打多张"},
    "artifacts": {"zh": "神器机械", "desc": "神器、装备、载具为核心"},
    "enchant": {"zh": "结界灵气", "desc": "结界、灵气、传纪为核心"},
    "grave": {"zh": "坟场复用", "desc": "把牌送进坟场再反复捞回来用"},
    "tribal": {"zh": "生物部落", "desc": "围绕某个生物类别组牌"},
    "drain": {"zh": "吸血消耗", "desc": "生命差玩法，吸取对手生命慢慢磨死"},
    "stax": {"zh": "锁场剥夺", "desc": "让对手做不了事：弃牌、锁地、加税"},
    "clonesteal": {"zh": "复制偷取", "desc": "复制自己的牌或偷对手的牌来用"},
    "politics": {"zh": "政治博弈", "desc": "谈判、结盟、君主、借刀杀人"},
    "chaos": {"zh": "随机搞事", "desc": "骰子、赌博、混乱效应"},
    "counters": {"zh": "指示物增殖", "desc": "＋1/＋1 指示物、增殖、堆叠成长"},
    "blink": {"zh": "进场触发", "desc": "反复把生物闪现回场，重复触发进场异能"},
}


def load_descriptions() -> dict:
    merged: dict[str, dict] = {}
    for index in range(1, 21):
        path = DATA / f"descriptions_{index}.json"
        if not path.exists():
            continue
        merged.update(json.loads(path.read_text(encoding="utf-8")))
    return merged


def build_card_info() -> dict:
    display = json.loads((DATA / "card_display.json").read_text(encoding="utf-8"))
    zh = json.loads((DATA / "card_zh.json").read_text(encoding="utf-8"))
    verified = json.loads((DATA / "card_verified.json").read_text(encoding="utf-8"))
    info = {}
    for entry in display.values():
        for name in entry["synergy"] + entry["popular"]:
            if name in info:
                continue
            card = verified.get(name) or {}
            info[name] = {
                "zh": zh.get(name, ""),
                "cmc": card.get("cmc"),
                "type": (card.get("type_line") or "")[:40],
            }
    return info


def main() -> int:
    quiz = json.loads((DATA / "questions.json").read_text(encoding="utf-8"))
    payload = json.loads((DATA / "commanders.json").read_text(encoding="utf-8"))
    tag_zh = json.loads((DATA / "tag_zh.json").read_text(encoding="utf-8"))
    template = (ROOT / "templates" / "quiz_template.html").read_text(encoding="utf-8")

    descriptions = load_descriptions()
    card_display = json.loads((DATA / "card_display.json").read_text(encoding="utf-8"))
    card_info = build_card_info()

    blob = {
        "quiz": quiz,
        "commanders": payload["commanders"],
        "axes": AXES,
        "tagZh": tag_zh,
        "descriptions": descriptions,
        "cardDisplay": card_display,
        "cardInfo": card_info,
    }
    encoded = json.dumps(blob, ensure_ascii=False, separators=(",", ":"))
    encoded = encoded.replace("</", "<\\/")   # 防止提前闭合内联脚本
    html = template.replace("/*__DATA__*/", encoded)

    out = ROOT / "commander_quiz.html"
    out.write_text(html, encoding="utf-8")
    print(f"✓ 写出 {out}（{len(html) / 1024:.0f} KB）")
    print(f"  题目 {len(quiz['questions'])} 道 / 主将 {len(payload['commanders'])} 位 / "
          f"介绍文 {len(descriptions)} 篇 / 搭配牌 {len(card_info)} 张")

    missing_desc = [c["en"] for c in payload["commanders"] if c["en"] not in descriptions]
    if missing_desc:
        print(f"  ⚠ 缺介绍文 {len(missing_desc)} 位：{missing_desc[:8]}")
    else:
        print("  ✓ 每位主将都有介绍文")

    missing_cards = sorted(n for n, v in card_info.items() if not v["zh"])
    if missing_cards:
        print(f"  ⚠ 缺中文名 {len(missing_cards)} 张：{missing_cards[:8]}")
    else:
        print("  ✓ 搭配牌全部有中文名")

    missing_tags = sorted({t for c in payload["commanders"] for t in c["top_tags"]} - set(tag_zh))
    print("  ✓ 标签全部有中文" if not missing_tags else f"  ⚠ 未翻译标签 {missing_tags}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
