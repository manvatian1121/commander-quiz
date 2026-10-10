# -*- coding: utf-8 -*-
"""descriptions_8.json 交付自检（用户指定的 6 项）。

 1 JSON 可解析、条目数 = 27、key 与素材完全一致
 2 三字段非空；tagline ≤ 20
 3 intro 70~120、build 110~170（去掉空白后的可见字符数）
 4 逐主将白名单：正文里的英文牌名必须属于该主将自己的协同/出场清单（或主将本人）
 5 中英并列：牌名一律「中文（English）」；中文名与 card_zh.json 完全一致，
   若该牌不在 card_zh.json（主将本人回退 commander_zh.json）则只写英文名
 6 术语：haste=敏捷（非加速）、menace=威慑（非威吓）、intimidate=威吓

用法：python validate_descriptions_8.py [-v]
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
SRC_FILES = [DATA / f"writing_batch_new_{i}.md" for i in (1, 2, 3, 4)]
OUT = DATA / "descriptions_8.json"

T_MAX = 20
I_MIN, I_MAX = 70, 120
B_MIN, B_MAX = 110, 170

# ---- 素材解析：主将顺序 + 逐主将清单 ----
commanders, per_commander, zh_material = [], {}, {}
for src in SRC_FILES:
    cur = None
    for line in src.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## (.+?) ｜ (.+?)\s*$", line)
        if m:
            cur = m.group(1).strip()
            commanders.append(cur)
            per_commander[cur] = {cur}
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


def zh_lookup(name: str):
    """单卡中文名优先查 card_zh.json；主将本人回退 commander_zh.json。"""
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
        print("     ✗ 缺：", [c for c in commanders if c not in data])
        print("     ✗ 多：", [k for k in keys if k not in commanders])
    if keys != commanders:
        print("     ! 顺序与素材不同（不影响解析，仅提示）")

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

    bad_own, bad_zh, bad_exact, bare_eng, bare_zh = [], [], [], [], []
    per_cmd_count = {}
    for c in commanders:
        own = per_commander[c]
        n_ref = 0
        for f in ("tagline", "intro", "build"):
            v = data[c][f]
            # 括号内的英文牌名
            for m in paren.finditer(v):
                frag = m.group(1).strip()
                if frag not in own:
                    bad_own.append((c, f, frag))
                want = zh_lookup(frag)
                prev = v[max(0, m.start() - 12):m.start()]
                if want and not prev.endswith(want):
                    bad_exact.append((c, f, frag, prev[-6:], want))
                if not want:
                    prev2 = v[max(0, m.start() - 12):m.start()]
                    if re.search(r"[\u4e00-\u9fff]$", prev2):
                        bare_zh.append((c, f, frag, "该牌无官方中文名，却写了中文"))
                n_ref += 1
            # 括号外的裸英文
            stripped = re.sub(r"（[^（）]*）", "", v)
            for m in eng_bare.finditer(stripped):
                frag = m.group(0).strip()
                if len(frag) >= 3:
                    bare_eng.append((c, f, frag))
            # 裸中文牌名（清单里的中文名出现却没跟英文）
            for card in own:
                z = zh_lookup(card)
                if not z:
                    continue
                for m in re.finditer(re.escape(z), v):
                    if not v[m.end():m.end() + 1] == "（":
                        bare_zh.append((c, f, card, f"中文名「{z}」未并列英文"))
        per_cmd_count[c] = n_ref

    print(f"【4】逐主将白名单（英文牌名必须在本人清单内）："
          f"{'通过' if not bad_own else '失败'}")
    for b in bad_own:
        print("     ✗", b)
    if bad_own:
        problems.append(f"白名单越界：{bad_own}")

    print(f"【5a】括号外裸英文串：{'无' if not bare_eng else bare_eng}")
    print(f"【5b】中文名未与官方名并列表述：{'无' if not bare_zh else ''}")
    for b in bare_zh:
        print("     ✗", b)
    print(f"【5c】「中文（English）」与官方中文名逐字一致："
          f"{'通过' if not bad_exact else '失败'}")
    for b in bad_exact:
        print("     ✗", b)
    if bad_zh or bare_zh or bad_exact:
        problems.append("中英并列问题")

    # ---------- 6 ----------
    BAD_TERMS = {
        "威吓": "intimidate 才是威吓，menace 应写「威慑」",
        "获得加速": "haste 应写「敏捷」",
        "有加速": "haste 应写「敏捷」",
        "得到加速": "haste 应写「敏捷」",
        "给全体加速": "haste 应写「敏捷」",
    }
    JARGON = ["曲线", "ramp", "stax", "voltron", "Bracket", "EDHREC", "咸度", "最强"]
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
    print(f"【6a】禁用术语（威吓/加速当 haste 用）：{'无' if not term_hits else term_hits}")
    print(f"【6b】行话词：{'无' if not jargon_hits else jargon_hits}")
    print("【6c】术语用词分布：", {w: sum(data[c][f].count(w)
          for c in commanders for f in ("tagline", "intro", "build"))
          for w in ("敏捷", "威慑", "威吓", "加速", "连击", "死触", "系命", "践踏")})
    if term_hits:
        problems.append(f"术语错误：{term_hits}")

    if verbose:
        print("\n【明细】字数（T/I/B）+ 引用牌数")
        for c in commanders:
            t = count(data[c]["tagline"])
            i = count(data[c]["intro"])
            b = count(data[c]["build"])
            print(f"     {c:<34} T{t:>3} I{i:>4} B{b:>4}  引用 {per_cmd_count[c]:>2} 张"
                  f"/清单 {len(per_commander[c]) - 1} 张")

    print(f"\n总判定：{'全部通过' if not problems else '存在问题：' + str(problems)}")
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
