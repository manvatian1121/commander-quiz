# -*- coding: utf-8 -*-
"""bank3 / bank4 修正后状态审计（供复核）。

1) 修正一普查：题干是「别人造成的不利处境」的题，现在是否都有「不在意」口径选项
2) 修正二普查：倾向性问句的会/不会两组比例是否已 ≤ 3:2
3) 新增选项落盘确认

Run:  python audit_fix_34.py
"""
import json
import sys
from pathlib import Path



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

DATA = Path(ROOT / "data")

# 修正一：题干含「别人/外部造成的不利处境」信号的题 -> 处境描述 + 现在的不在意口径
ADVERSE = {
    "s35": ("商家咬死不给减价（外部造成的处境）", "本次新增第 5 项"),
    "s36": ("室友堆碗占水池（别人造成的处境）", "本次新增第 3 项"),
    "s37": ("同事把你的方案署自己的名（别人造成的处境）", "原有第 3 项「算了，反正项目能推进就行」"),
    "s41": ("朋友半夜来电、声音不对（别人出了状况）", "原有第 3 项「有的人我马上去，有的人我拖着」"),
    "s42": ("合买对方用得多（别人造成的处境）", "本次新增第 3 项"),
    "s43": ("群里有人 @ 你说你办得不对（别人造成的处境）", "原有第 3 项「回一句收到，然后该干嘛干嘛」"),
    "s44": ("对方回你越来越慢（别人造成的处境）", "本次新增第 4 项"),
    "s45": ("有人当众开你玩笑（别人造成的处境）", "原有第 2 项「笑一笑接过去，把话岔开」"),
    "s46": ("有人一杯接一杯劝酒（别人造成的压力）", "原有第 4 项「偷偷换成茶，能糊弄就糊弄」"),
    "s47": ("朋友开口借一笔不小的钱（别人提出的请求）", "本次新增第 5 项"),    "h3a2": ("涨房租/换工位/让朋友还钱（别人造成的处境）", "本次新增第 5 项"),
    "h3b1": ("排队被插队（别人造成的处境）", "本次新增第 5 项"),
    "h3b2": ("群里被公开说难听话（别人造成的处境）", "本次新增第 5 项"),
    "h3b3": ("跟人闹僵之后（双方造成的处境）", "原有第 2 项「算了吧。人情账在心里记着」"),
}

# 修正二：倾向性问句 + 修正后的会/不会分组
POLAR = [
    ("bank4", "s56", "3:2",
     "会 3 项：纠结材质 / 摆收藏 / 淘旧柜自己刷漆；不会 2 项：先空着不急着弄（本次新增）"),
]

NEW_TEXTS = [
    ("bank3", "那就算了，这个价我就不买了"),
    ("bank3", "不在意，堆就堆着吧，我不着急用"),
    ("bank3", "懒得算谁用多谁用少，反正买回来就是给大家用的"),
    ("bank3", "回得慢就慢吧，我不往心里去，也不缺这一个朋友"),
    ("bank3", "借了就借了，什么时候还我不惦记，真还不上也不去催"),
    ("bank3", "笑一笑就过去了，几分钟的事，不往心里去"),
    ("bank3", "看到那句话就翻过去了，该干嘛干嘛，不往心里去"),
    ("bank4", "先空着，不急着弄，什么时候有兴致了再说"),
]

banks = {}
for b in ("bank3", "bank4"):
    banks[b] = json.loads((DATA / f"{b}.json").read_text(encoding="utf-8"))

print("=" * 78)
print("修正后状态审计")
print("=" * 78)

print("\n[修正一] 别人造成的不利处境 -> 不在意口径选项（bank3 / social）")
for q in banks["bank3"]["questions"]:
    qid = q["id"]
    if qid not in ADVERSE:
        continue
    situ, how = ADVERSE[qid]
    has = "OK" if ("本次新增" in how or "原有第" in how) else "--"
    print(f"  [{has}] {qid:<6} {len(q['opts'])} 项  {situ}")
    print(f"         不在意口径: {how}")

print("\n[修正二] 倾向性问句的会/不会配平")
for bank, qid, ratio, detail in POLAR:
    q = next(x for x in banks[bank]["questions"] if x["id"] == qid)
    print(f"  {bank} {qid}: {ratio}  题干「{q['q']}」")
    print(f"         {detail}")

print("\n[新增选项落盘确认]")
for bank, t in NEW_TEXTS:
    hit = any(o["t"] == t for q in banks[bank]["questions"] for o in q["opts"])
    print(f"  {'OK  ' if hit else 'MISS'} {bank}  {t}")

print("\n[选项长度分布]（新选项不应显著偏离原库）")
for bank in ("bank3", "bank4"):
    ln = sorted(len(o["t"]) for q in banks[bank]["questions"] for o in q["opts"])
    print(f"  {bank}: {len(ln)} 项，最短 {ln[0]}，中位 {ln[len(ln)//2]}，最长 {ln[-1]}")

print("\n[颜色题 col 完整性]（bank4 的 4 道颜色题）")
for q in banks["bank4"]["questions"]:
    cols = [o["col"] for o in q["opts"] if "col" in o]
    if cols:
        print(f"  {q['id']}: {len(q['opts'])} 选项，col {[list(c)[0] for c in cols]}")
