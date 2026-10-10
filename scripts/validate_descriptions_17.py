# -*- coding: utf-8 -*-
"""descriptions_17.json 交付自检（用户指定的 6 项）。

 1 JSON 可解析、条目数 = 17、key 与素材完全一致
 2 三字段非空；tagline ≤ 20
 3 intro 70~120、build 110~170（去掉空白后的可见字符数）
 4 逐主将白名单：正文里的英文牌名必须属于该主将自己的协同/出场清单
   （组合主将的两半名字本身出现在正文里是允许的）
 5 中英并列：牌名一律「中文（English）」，中文名与 card_zh.json / 素材标题逐字一致；
   查不到中文名就只写英文
 6 术语：haste=敏捷（非加速）、menace=威慑（非威吓）、intimidate 才是威吓

用法：python validate_descriptions_17.py [-v]
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SRC_FILES = [DATA / f"writing_batch_new_{i}.md" for i in (1, 2, 3, 4, 5, 6)]
OUT = DATA / "descriptions_17.json"

T_MAX = 20
I_MIN, I_MAX = 70, 120
B_MIN, B_MAX = 110, 170

# ---------- 素材解析：主将顺序 + 逐主将清单 + 素材自带中文名 ----------
commanders, per_commander, zh_material = [], {}, {}
for src in SRC_FILES:
    cur = None
    for line in src.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## (.+?) ｜ (.+?)\s*$", line)
        if m:
            cur = m.group(1).strip()
            if cur in per_commander:      # 素材内重复
                continue
            commanders.append(cur)
            # 白名单 = 组合全名（允许出现在正文）+ 两半各自的名字 + 清单里的牌
            own = {cur}
            own.update(p.strip() for p in cur.split(" // "))
            per_commander[cur] = own
            zh_material[cur] = m.group(2).strip()
            continue
        if cur is None:
            continue
        m = re.match(r"^(?:\d+\.|[-*])\s+(.+?)\uff08", line.strip())
        if m:
            n = m.group(1).strip()
            if n and not n.startswith("**"):
                per_commander[cur].add(n)

card_zh = json.loads((DATA / "card_zh.json").read_text(encoding="utf-8"))
commander_zh = json.loads((DATA / "commander_zh.json").read_text(encoding="utf-8"))

# 两半中文名：优先 commander_zh.json（组合全名 -> "中文甲 // 中文乙"），
# 其次素材标题里的中文（同样是权威来源）
half_zh = {}
for full, zh in zh_material.items():
    en_parts = [p.strip() for p in full.split(" // ")]
    zh_parts = [p.strip() for p in zh.split(" // ")]
    if len(en_parts) == len(zh_parts):
        for a, b in zip(en_parts, zh_parts):
            half_zh.setdefault(a, b)
for full, zh in commander_zh.items():
    if " // " not in full:
        continue
    en_parts = [p.strip() for p in full.split(" // ")]
    zh_parts = [p.strip() for p in zh.split(" // ")]
    if len(en_parts) == len(zh_parts):
        for a, b in zip(en_parts, zh_parts):
            half_zh.setdefault(a, b)


def zh_lookup(name: str):
    """单卡中文名优先 card_zh.json；组合主将全名回退 commander_zh.json。"""
    return card_zh.get(name) or commander_zh.get(name)


def count(s: str) -> int:
    return sum(1 for ch in s if not ch.isspace())


def main() -> int:
    verbose = "-v" in sys.argv
    problems = []
    data = json.loads(OUT.read_text(encoding="utf-8"))
    keys = list(data)

    # ---------- 1 ----------
    print("【1】JSON 解析：成功")
    same_set = set(keys) == set(commanders)
    print(f"     条目数 {len(keys)} / 素材 {len(commanders)} 位；key 集合一致：{same_set}"
          f"；顺序一致：{keys == commanders}")
    if not same_set:
        problems.append("key 与素材不一致")
        print("     × 缺：", [c for c in commanders if c not in data])
        print("     × 多：", [k for k in keys if k not in commanders])

    # ---------- 2 ----------
    empty = [(c, f) for c in commanders for f in ("tagline", "intro", "build")
             if not (data.get(c, {}).get(f) or "").strip()]
    if empty:
        problems.append(f"字段为空：{empty}")
    print(f"【2a】三字段非空：{'通过' if not empty else '失败 ' + str(empty)}")
    over_t = [(c, count(data[c]["tagline"])) for c in commanders
              if count(data[c]["tagline"]) > T_MAX]
    print(f"【2b】tagline ≤ {T_MAX}：{'通过' if not over_t else over_t}"
          f"（最长 {max(count(data[c]['tagline']) for c in commanders)}）")
    if over_t:
        problems.append(f"tagline 超标：{over_t}")

    # ---------- 3 ----------
    bad_i = [(c, count(data[c]["intro"])) for c in commanders
             if not (I_MIN <= count(data[c]["intro"]) <= I_MAX)]
    bad_b = [(c, count(data[c]["build"])) for c in commanders
             if not (B_MIN <= count(data[c]["build"]) <= B_MAX)]
    print(f"【3a】intro {I_MIN}~{I_MAX}：{'通过' if not bad_i else bad_i}")
    print(f"【3b】build {B_MIN}~{B_MAX}：{'通过' if not bad_b else bad_b}")
    if bad_i:
        problems.append(f"intro 超标：{bad_i}")
    if bad_b:
        problems.append(f"build 超标：{bad_b}")

    # ---------- 4 / 5 ----------
    paren = re.compile(r"（([A-Za-z][^（）]*?)）")
    eng_bare = re.compile(r"[A-Za-z][A-Za-z'’\-]*(?:\s+[A-Za-z][A-Za-z'’\-]*)*")
    zh_any = re.compile(r"[\u4e00-\u9fff]{2,}")

    bad_own, bad_exact, bare_eng, bare_zh, no_zh = [], [], [], [], []
    per_cmd_count, per_cmd_cards = {}, {}
    for c in commanders:
        own = per_commander[c]
        cards = set()
        for f in ("tagline", "intro", "build"):
            v = data[c][f]
            for m in paren.finditer(v):
                frag = m.group(1).strip()
                if frag not in own:
                    bad_own.append((c, f, frag))
                want = zh_lookup(frag) or half_zh.get(frag)
                prev = v[max(0, m.start() - 12):m.start()]
                if want and not prev.endswith(want):
                    bad_exact.append((c, f, frag, prev[-6:], want))
                if not want:
                    no_zh.append((c, f, frag, "无中文名，只写英文（合规）"))
                    if re.search(r"[\u4e00-\u9fff]$", prev):
                        bare_zh.append((c, f, frag, "该牌无官方中文名，却写了中文"))
                if frag not in own - {c} - set(c.split(" // ")):
                    cards.add(frag)
            stripped = re.sub(r"（[^（）]*）", "", v)
            for m in eng_bare.finditer(stripped):
                frag = m.group(0).strip()
                if len(frag) >= 3:
                    bare_eng.append((c, f, frag))
            for card in own:
                z = zh_lookup(card) or half_zh.get(card)
                if not z:
                    continue
                for m in re.finditer(re.escape(z), v):
                    if v[m.end():m.end() + 1] != "（":
                        bare_zh.append((c, f, card, f"中文名「{z}」未并列英文"))
        per_cmd_count[c] = len(cards)
        per_cmd_cards[c] = sorted(cards)

    print(f"【4】逐主将白名单（英文牌名必须属于本人清单）："
          f"{'通过' if not bad_own else '失败'}")
    for b in bad_own:
        print("     ×", b)
    if bad_own:
        problems.append(f"白名单越界：{bad_own}")
    print(f"【5a】括号外裸英文串：{'无' if not bare_eng else bare_eng}")
    print(f"【5b】中文名未与官方英文并列表述：{'无' if not bare_zh else ''}")
    for b in bare_zh:
        print("     ×", b)
    print(f"【5c】「中文（English）」与官方中文名逐字一致："
          f"{'通过' if not bad_exact else '失败'}")
    for b in bad_exact:
        print("     ×", b)
    if not no_zh:
        print("【5d】无中文名、只写英文的牌：无")
    else:
        print(f"【5d】无中文名、只写英文的牌：{len(no_zh)} 处（合规，列出备查）")
        for b in no_zh:
            print("     ·", b[0][:26], b[1], b[2])
    if bad_exact or bare_zh:
        problems.append("中英并列问题")

    # ---------- 6 ----------
    BAD_TERMS = {
        "威吓": "intimidate 才是威吓，menace 应写「威慑」",
        "获得加速": "haste 应写「敏捷」",
        "有加速": "haste 应写「敏捷」",
        "得到加速": "haste 应写「敏捷」",
        "给全体加速": "haste 应写「敏捷」",
        "加速指示物": "haste 应写「敏捷」",
        "敏捷指示物": "haste 词条本身可以，但要看上下文是否指敏捷（备查）",
    }
    JARGON = ["曲线", "ramp", "stax", "voltron", "Bracket", "EDHREC", "咸度",
              "最强", "上分", "引擎", "提速"]
    term_hits, jargon_hits = [], []
    for c in commanders:
        for f in ("tagline", "intro", "build"):
            v = data[c][f]
            for w, why in BAD_TERMS.items():
                if w in v:
                    term_hits.append((c, f, w, why))
            for w in JARGON:
                if w in v:
                    jargon_hits.append((c, f, w))
    hard_term = [t for t in term_hits if t[2] not in ("敏捷指示物",)]
    print(f"【6a】禁用术语（威吓当 menace / 加速当 haste 用）："
          f"{'无' if not hard_term else hard_term}")
    if term_hits:
        print("     · 备查（含「敏捷指示物」等正常用法）：", term_hits)
    print(f"【6b】行话词：{'无' if not jargon_hits else jargon_hits}")
    print("【6c】术语用词分布：", {
        w: sum(data[c][f].count(w) for c in commanders
               for f in ("tagline", "intro", "build"))
        for w in ("敏捷", "威慑", "威吓", "加速", "先攻", "践踏", "系命")})
    if hard_term:
        problems.append(f"术语错误：{hard_term}")
    if jargon_hits:
        problems.append(f"行话词：{jargon_hits}")

    if verbose:
        print("\n【明细】字数（T/I/B）+ 引用牌数")
        for c in commanders:
            t = count(data[c]["tagline"])
            i = count(data[c]["intro"])
            b = count(data[c]["build"])
            print(f"     {c:<58} T{t:>3} I{i:>4} B{b:>4}  引用 {per_cmd_count[c]:>2} 张"
                  f"/清单 {len(per_commander[c]) - 1 - (len(c.split(' // ')) - 1)} 张")

    print(f"\n总判定：{'全部通过' if not problems else '存在问题：' + str(problems)}")
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
