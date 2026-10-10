# -*- coding: utf-8 -*-
"""descriptions_6.json 自检：
1) JSON 可解析、条目数 = 30、key 与素材完全一致
2) 三个字段非空；tagline ≤ 20 字
3) intro 70~120、build 110~170（非空格可见字符数）
4) 牌名白名单：正文里的英文片段必须属于该主将自己的清单（协同 / 出场 / 主将名），
   且必须是精确牌名（不允许只靠单词拼凑）
5) 附加：禁用术语/吹强度词、括号外不得出现英文
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
TARGET = DATA / "descriptions_6.json"
INDEX = json.loads((DATA / "_material_new3_index.json").read_text(encoding="utf-8"))

LEN_RULES = {"tagline": (1, 20), "intro": (70, 120), "build": (110, 170)}
EN_PHRASE = re.compile(r"[A-Z][A-Za-z'\u2019\-]*(?:\s+(?:of|the|and|as|to|in|a)\s+)?"
                       r"(?:\s+[A-Z][A-Za-z'\u2019\-]*)*")
PAREN = re.compile(r"[（(]([^）)]*[A-Za-z][^）)]*)[）)]")
ALLOW_EXTRA = {"edh", "mtg", "mv", "w", "u", "b", "r", "g", "c"}
BANNED = ["最强", "上分神器", "无敌", "碾压一切", "必赢", "无敌", "bracket", "edhrec",
          "voltron", "stax", "ramp", "引擎", "曲线", "咸度"]


def visible_len(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def name_words(name: str) -> set[str]:
    return {w.lower() for w in re.findall(r"[A-Za-z'\u2019\-]+", name)}


def main() -> int:
    data = json.loads(TARGET.read_text(encoding="utf-8"))
    print(f"① JSON 可解析 ✓  条目数 = {len(data)}")

    expected = [c["en"] for c in INDEX]
    missing = [n for n in expected if n not in data]
    extra = [n for n in data if n not in expected]
    print(f"   key 与素材完全一致：{'✓' if not missing and not extra else '✗'}"
          f"（缺 {len(missing)}，多 {len(extra)}；顺序一致：{list(data) == expected}）")

    empty, long_tagline, bad_len, banned_hits = [], [], [], []
    outside_paren, inexact = [], []
    lens = {k: [] for k in LEN_RULES}

    for c in INDEX:
        en = c["en"]
        entry = data.get(en)
        if entry is None:
            continue
        own = set(c["whitelist"])
        own_words = {w for n in own for w in name_words(n)} | ALLOW_EXTRA

        for field, (low, high) in LEN_RULES.items():
            text = (entry.get(field) or "").strip()
            if not text:
                empty.append(f"{en}.{field}")
                continue
            n = visible_len(text)
            lens[field].append(n)
            if field == "tagline":
                if n > 20:
                    long_tagline.append(f"{en} = {n}")
            elif not (low <= n <= high):
                bad_len.append(f"{en}.{field} = {n}（要求 {low}~{high}）")

        blob = " ".join(str(entry.get(f) or "") for f in ("tagline", "intro", "build"))
        low_blob = blob.lower()
        for word in BANNED:
            if word.lower() in low_blob:
                banned_hits.append(f"{en} → {word}")

        # 括号内的英文必须是本主将清单里的精确牌名
        for group in PAREN.findall(blob):
            t = group.strip()
            if t not in own:
                inexact.append(f"{en} → 「{t}」")

        # 任何英文片段都必须在括号里（即：每张牌名都配了中文名）
        spans = [(m.start(), m.end()) for m in PAREN.finditer(blob)]
        for m in EN_PHRASE.finditer(blob):
            p = m.group(0).strip()
            if not p:
                continue
            inside = any(s <= m.start() and m.end() <= e for s, e in spans)
            if not inside:
                outside_paren.append(f"{en} → 「{p}」")

    print(f"\n② 空字段：{len(empty)} 处 {empty if empty else '✓'}")
    print(f"   tagline > 20 字：{len(long_tagline)} 处 {long_tagline if long_tagline else '✓'}")

    print(f"\n③ 长度（非空格可见字符）：")
    for field, values in lens.items():
        low, high = LEN_RULES[field]
        print(f"   {field:<8} {min(values)}~{max(values)}（要求 {low}~{high}）"
              f" 中位 {sorted(values)[len(values) // 2]}")
    print(f"   {'✓ 全部落在区间内' if not bad_len else '✗ 超区间 ' + str(bad_len)}")

    print(f"\n④ 白名单校验")
    print(f"   括号内非本主将清单牌名：{len(inexact)} 处")
    for x in inexact:
        print("      -", x)
    print(f"   括号外的裸露英文片段：{len(outside_paren)} 处")
    for x in outside_paren:
        print("      -", x)

    print(f"\n⑤ 禁用术语/吹强度词：{len(banned_hits)} 处")
    for x in banned_hits:
        print("      -", x)

    ok = not (missing or extra or empty or long_tagline or bad_len
              or inexact or outside_paren or banned_hits)
    print("\n" + ("✓ 自检全部通过" if ok else "✗ 自检未通过，见上"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
