# -*- coding: utf-8 -*-
"""附加自检（超出用户 6 项之外的两项加固）：
 A 全局中文牌名扫描：任何「别的主将清单里的中文牌名」出现在某条目正文中，
   若该牌不属于该主将自己的清单 → 越界；若属于本主将但后面没跟（ → 未并列。
 B 编码：UTF-8 无 BOM、无 CRLF 混用；并统计引用牌数分布。
"""
import json
import pathlib
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
SRC = DATA / "writing_batch_new_4.md"
OUT = DATA / "descriptions_12.json"

commanders, per_commander = [], {}
cur = None
for line in SRC.read_text(encoding="utf-8").splitlines():
    m = re.match(r"^## (.+?) ｜ (.+?)\s*$", line)
    if m:
        cur = m.group(1).strip()
        commanders.append(cur)
        per_commander[cur] = {cur}
        continue
    if cur is None:
        continue
    m = re.match(r"^(?:\d+\.|[-*])\s+(.+?)\uff08", line.strip())
    if m:
        n = m.group(1).strip()
        if n and not n.startswith("**"):
            per_commander[cur].add(n)

card_zh = json.loads((DATA / "card_zh.json").read_text(encoding="utf-8"))
cmd_zh = json.loads((DATA / "commander_zh.json").read_text(encoding="utf-8"))
data = json.loads(OUT.read_text(encoding="utf-8"))


def zl(n):
    return card_zh.get(n) or cmd_zh.get(n)


# 全局 中文名 -> 该中文名所属牌名集合
zh_to_names = {}
for c in commanders:
    for n in per_commander[c]:
        z = zl(n)
        if z:
            zh_to_names.setdefault(z, set()).add(n)

# 每个主将清单的完整中文名集合（含无中文名的跳过）
own_zh = {c: {zl(n) for n in per_commander[c] if zl(n)} for c in commanders}

print("【A】全局中文牌名扫描")
hits = []
for c in commanders:
    for f in ("tagline", "intro", "build"):
        v = data[c][f]
        for z, names in zh_to_names.items():
            for m in re.finditer(re.escape(z), v):
                after = v[m.end():m.end() + 1]
                in_own = z in own_zh[c]
                if not in_own:
                    hits.append((c, f, z, "该牌不在本人清单"))
                elif after != "（":
                    hits.append((c, f, z, "未并列英文"))
print(f"    越界/未并列命中：{len(hits)}")
for h in hits:
    print("     ✗", h)
if not hits:
    print("    ✓ 无（正文只出现本主将清单内的中文牌名，且全部中英并列）")

# 反向：所有 （English） 的中文前缀都已由主检查器覆盖，这里只做数量统计
paren = re.compile(r"（([A-Za-z][^（）]*?)）")
tot = sum(len(paren.findall(data[c][f])) for c in commanders
          for f in ("tagline", "intro", "build"))
print(f"\n【B】中英并列牌名引用总数：{tot} 处；"
      f"平均每条目 {tot / len(commanders):.1f} 处")
refs = {c: sum(len(paren.findall(data[c][f])) for f in ("tagline", "intro", "build"))
        for c in commanders}
print("    引用 0 处的条目：", [c for c, n in refs.items() if n == 0] or "无")
print("    引用 ≤1 处的条目：", [(c, n) for c, n in refs.items() if n <= 1] or "无")

raw = OUT.read_bytes()
print(f"\n【C】编码：UTF-8 可解析={bool(json.loads(raw.decode('utf-8')))}"
      f" / BOM={raw[:3] == b'\xef\xbb\xbf'}"
      f" / CRLF数={raw.count(bytes([13, 10]))} / LF数={raw.count(bytes([10]))}")
