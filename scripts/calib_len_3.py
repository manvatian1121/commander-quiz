"""校准：确认计数口径（总长 vs 纯汉字数）下，样本文案是否落在区间内。"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

CJK = re.compile(r"[\u4e00-\u9fff]")


def stats(s: str):
    total = len(re.sub(r"\s", "", s))
    cjk = len(CJK.findall(s))
    return total, cjk


samples = {
    "intro-1": "她是一头会致命触碰的多头龙，本身还能横置产出两点任意颜色的法术力。她的本事是给「要花 X 点的咒语」加码：每放一个这种咒语，就额外送你一头同样大小的多头龙。喜欢一次花大钱、场面瞬间变大的玩家会很对味。",
    "build-1": "一半以上放地，其余大多是加速，先把法术力堆厚；主力是放干鲜血（Exsanguinate）这种「X 越大越狠」的咒语，水螅融合体（Hydroid Krasis）能一次给你生物、手牌和生命。新人要注意：X 定成 0 也会触发主将，但那只 0/0 的多头龙进场就会死，白白浪费一张牌。",
    "tagline-1": "花多少费，就白送多大的多头龙",
    "intro-2": "她每次战斗开始前先让你把牌库顶两张牌放进坟场，然后飞起来。她打中对手时，只要再付两点法术力，就能把坟场里一个力量 3 以下的小生物拉回场上。喜欢坟场、愿意用小生物反复换命的玩家会喜欢她。",
    "build-2": "思路是主动往坟场里送牌：拼接师备尸（Stitcher's Supplier）这类进场或死亡就磨牌的生物很合适，再用活尸法（Reanimate）把大生物抢回场上。新人注意两点：坟场里得先有货，主将的复活效果才用得上；另外记得每回合留出额外两点法术力。",
}
for k, v in samples.items():
    t, c = stats(v)
    print(f"{k:10s} 总长={t:4d}  纯汉字={c:4d}")
