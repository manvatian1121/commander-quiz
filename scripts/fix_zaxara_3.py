"""修正 Zaxara 条目：去掉裸露的拉丁字母 X（项目的 validate_descriptions.py 会判为白名单外英文）。"""
import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
P = pathlib.Path(ROOT / "data" / "_part1_3.json")
data = json.loads(P.read_text(encoding="utf-8"))

data["Zaxara, the Exemplary"]["intro"] = (
    "她是一头会致命触碰的多头龙，本身还能横置产出两点任意颜色的法术力。"
    "她的本事是给「花多少由你决定的咒语」加码：你每放一个这种咒语，"
    "就额外得到一头同样大小的多头龙。喜欢一次花一大笔、看场面瞬间变大的玩家会很对味。"
)
data["Zaxara, the Exemplary"]["build"] = (
    "一半以上放地，其余大多是加速，先把法术力堆厚。"
    "主力是放干鲜血（Exsanguinate）这类投入越多越狠的咒语，"
    "水螅融合体（Hydroid Krasis）则能一次给你一头生物、几张牌和几点生命。"
    "新人要注意：就算把那笔投入定成零，主将也会触发，"
    "但那头 0/0 的多头龙一进场就会立刻死掉，等于白花一张牌；"
    "她自己也是能打的生物，上场挡一下并不亏。"
)

P.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Zaxara 已改写")
print("intro:", data["Zaxara, the Exemplary"]["intro"])
print("build:", data["Zaxara, the Exemplary"]["build"])
