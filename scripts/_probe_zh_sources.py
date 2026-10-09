# -*- coding: utf-8 -*-
"""探查哪些 zh 映射文件含有这 27 位主将的中文名。"""
import io
import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

targets = ["Zur the Enchanter", "Urza, Chief Artificer", "Alela, Artful Provocateur",
           "Morophon, the Boundless", "Zada, Hedron Grinder", "Magus Lucea Kane",
           "Satoru Umezawa", "Inalla, Archmage Ritualist", "Omnath, Locus of All",
           "Kykar, Wind's Fury", "Winota, Joiner of Forces", "Marchesa, the Black Rose",
           "Najeela, the Blade-Blossom", "Shelob, Child of Ungoliant", "Rocco, Street Chef",
           "Liesa, Shroud of Dusk", "Ramos, Dragon Engine", "Sefris of the Hidden Ways",
           "Varina, Lich Queen", "Judith, Carnage Connoisseur", "Stella Lee, Wild Card",
           "Sheoldred, the Apocalypse"]

for f in ["commander_zh.json", "card_display.json", "zh_cards.json", "_card_zh_new3.json",
          "card_zh_b2.json", "card_zh_batch1.json", "new_candidates.json",
          "commanders.json", "commander_cards.json"]:
    p = DATA / f
    if not p.exists():
        print(f"{f}: 不存在")
        continue
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"{f}: 读取失败 {e}")
        continue
    if isinstance(d, dict):
        hits = {t: d[t] for t in targets if t in d}
        print(f"{f}: dict[{len(d)}] 命中主将 key {len(hits)}")
        if hits:
            print("   ", json.dumps(hits, ensure_ascii=False)[:1200])
    elif isinstance(d, list):
        hits = [x for x in d if isinstance(x, dict) and x.get("en") in targets]
        print(f"{f}: list[{len(d)}] 命中 {len(hits)}")
        if hits:
            print("   ", json.dumps(hits[:2], ensure_ascii=False)[:1200])
    else:
        print(f"{f}: {type(d)}")
