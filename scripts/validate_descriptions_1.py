# -*- coding: utf-8 -*-
"""descriptions_1.json 自检：字段/字数/白名单。

白名单算法：
1. 抽出素材里所有牌名（主将名 + 每张卡的「协同度高/出场率高」清单）→ 白名单。
2. 扫描正文里成对的「中文（English）」结构，取括号内英文，必须精确命中白名单。
3. 扫描正文里所有「连续英文单词串」（长度>=3 且首字母大写开头），逐个判断：
   若它是某条白名单牌名的完整形式、或整条牌名去掉标点后的子串，视为合法；
   若整条牌名是它的父串（说明只是把牌名截断写了），也视为合法（不引入新牌名）。
   其余一律报出。
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
SRC = DATA / "writing_batch_1.md"
OUT = DATA / "descriptions_1.json"

text = SRC.read_text(encoding="utf-8")
commanders = re.findall(r"^## (.+?) ｜", text, re.M)
whitelist = set(commanders)
for line in text.splitlines():
    s = line.strip()
    m = re.match(r"^(?:\d+\.|[-*])\s+(.+?)\uff08", s)
    if not m:
        continue
    name = m.group(1).strip()
    if name.startswith("**") or name.startswith("（"):
        continue
    whitelist.add(name)
whitelist = {w for w in whitelist if w and not w.startswith("**")}


def norm(s: str) -> str:
    """去掉空格和标点，仅留字母数字，用于宽松比较。"""
    return re.sub(r"[^A-Za-z0-9]", "", s).lower()


# 允许的额外条目：素材标题「## X ｜ Y」只写了正面，而官方牌名是「X // Z」的双面牌。
# 这些名字同样经过 mtgch API 精确匹配（见 card_zh_batch1.json），不是凭记忆补的。
DUAL_FACE = {"The Prismatic Bridge"}
for extra_name in DUAL_FACE:
    if norm(extra_name) not in {norm(w) for w in whitelist}:
        whitelist.add(extra_name)


WL_NORM = {w: norm(w) for w in whitelist}
WL_NAMES = sorted(whitelist, key=len, reverse=True)


def count(s: str) -> int:
    return sum(1 for ch in s.replace("\n", "") if not ch.isspace())


def is_ok(frag: str) -> bool:
    """frag 是否属于白名单（完整名 / 截断写法）。"""
    fn = norm(frag)
    if not fn:
        return True
    if fn in WL_NORM.values():
        return True
    # 允许「牌名的一部分」：该片段必须完全落在某条牌名内部
    for w in whitelist:
        if fn and fn in WL_NORM[w]:
            return True
    return False


def main() -> int:
    data = json.loads(OUT.read_text(encoding="utf-8"))
    keys = list(data.keys())
    print("【1】JSON 解析：成功")
    print(f"【2】条目数 {len(data)} / 期望 {len(commanders)}；"
          f"key 集合一致：{set(keys) == set(commanders)}；顺序一致：{keys == commanders}")
    missing = [c for c in commanders if c not in data]
    extra = [k for k in keys if k not in commanders]
    if missing:
        print("    缺失：", missing)
    if extra:
        print("    多余：", extra)

    bad_fields = []
    bad_len = []
    for c in commanders:
        e = data.get(c, {})
        for f in ("tagline", "intro", "build"):
            if not (e.get(f) or "").strip():
                bad_fields.append(f"{c}/{f}")
    print(f"【3】三字段均非空：{'通过' if not bad_fields else '失败 ' + str(bad_fields)}")

    over_t, over_i, over_b = [], [], []
    for c in commanders:
        e = data[c]
        t, i, b = count(e["tagline"]), count(e["intro"]), count(e["build"])
        if t > 20:
            over_t.append((c, t))
        if not (70 <= i <= 120):
            over_i.append((c, i))
        if not (110 <= b <= 170):
            over_b.append((c, b))
    print(f"【4】tagline<=20：{'通过' if not over_t else over_t}")
    print(f"【5】intro 70-120：{'通过' if not over_i else over_i}")
    print(f"     build 110-170：{'通过' if not over_b else over_b}")
    n = len(commanders)
    print(f"     字数区间：tagline {min(count(data[c]['tagline']) for c in commanders)}"
          f"-{max(count(data[c]['tagline']) for c in commanders)} / "
          f"intro {min(count(data[c]['intro']) for c in commanders)}"
          f"-{max(count(data[c]['intro']) for c in commanders)} / "
          f"build {min(count(data[c]['build']) for c in commanders)}"
          f"-{max(count(data[c]['build']) for c in commanders)}  （共 {n} 位）")

    # 白名单：括号内英文
    paren = re.compile(r"（([A-Za-z][^（）]*?)）")
    bad_paren = []
    en_mentions = set()
    for c in commanders:
        for f in ("tagline", "intro", "build"):
            for m in paren.finditer(data[c][f]):
                frag = m.group(1).strip()
                en_mentions.add(frag)
                if not is_ok(frag):
                    bad_paren.append((c, f, frag))
    print(f"【6a】括号内英文牌名 {len(en_mentions)} 个，全部命中白名单：{not bad_paren}")
    if bad_paren:
        for c, f, frag in bad_paren:
            print(f"     ✗ {c}/{f}: {frag}")

    # 白名单：括号外英文串
    eng = re.compile(r"[A-Za-z][A-Za-z'’\-]*(?:\s+[A-Za-z][A-Za-z'’\-]*)*")
    bad_bare = []
    for c in commanders:
        for f in ("tagline", "intro", "build"):
            v = data[c][f]
            # 先把括号内的部分挖掉
            stripped = re.sub(r"（[^（）]*）", "", v)
            for m in eng.finditer(stripped):
                frag = m.group(0).strip()
                if len(frag) < 3:
                    continue
                if is_ok(frag):
                    continue
                bad_bare.append((c, f, frag))
    print(f"【6b】括号外英文串：{'无清单外牌名' if not bad_bare else bad_bare}")

    ok = not (missing or extra or bad_fields or over_t or over_i or over_b
              or bad_paren or bad_bare)
    print(f"\n总判定：{'全部通过' if ok else '存在问题，见上'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
