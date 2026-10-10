# -*- coding: utf-8 -*-
"""descriptions_7.json 自检：结构 / 字段 / 字数 / 牌名白名单。

用法:
    python validate_descriptions_7.py            # 只报问题
    python validate_descriptions_7.py -v         # 附每位主将的字数明细（调长度用）

白名单来源 = 素材 writing_batch_new_4.md 里的 29 位主将名 + 每张卡的「协同度高/出场率高」清单。
字数口径 = 去掉空白后的可见字符数（全角标点、括号、英文字母都算 1 个）。
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
OUT = DATA / "descriptions_7.json"

T_MIN, T_MAX = 0, 20
I_MIN, I_MAX = 70, 120
B_MIN, B_MAX = 110, 170

text = SRC.read_text(encoding="utf-8")
commanders = re.findall(r"^## (.+?) ｜", text, re.M)

# ---- 白名单：主将名 + 清单牌名 ----
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
    return re.sub(r"[^A-Za-z0-9]", "", s).lower()


WL_NORM = {w: norm(w) for w in whitelist}


def count(s: str) -> int:
    return sum(1 for ch in s.replace("\n", "") if not ch.isspace())


def match_of(frag: str):
    """frag 命中哪条白名单牌名；没命中返回 None。"""
    fn = norm(frag)
    if not fn:
        return ""
    if fn in WL_NORM.values():
        return next(w for w, n in WL_NORM.items() if n == fn)
    for w, n in WL_NORM.items():
        if fn in n:
            return w
    return None


def main() -> int:
    verbose = "-v" in sys.argv
    data = json.loads(OUT.read_text(encoding="utf-8"))
    keys = list(data.keys())
    problems = 0

    print("【1】JSON 解析：成功")
    print(f"     白名单：主将 {len(commanders)} + 清单牌名 = 共 {len(whitelist)} 个名字")

    same_set = set(keys) == set(commanders)
    same_order = keys == commanders
    missing = [c for c in commanders if c not in data]
    extra = [k for k in keys if k not in commanders]
    print(f"【2】条目数 {len(data)} / 期望 {len(commanders)}；key 一致：{same_set}"
          f"；顺序一致：{same_order}")
    if missing:
        problems += 1
        print("     ✗ 缺失：", missing)
    if extra:
        problems += 1
        print("     ✗ 多余：", extra)

    bad_fields = [(c, f) for c in commanders for f in ("tagline", "intro", "build")
                  if not (data.get(c, {}).get(f) or "").strip()]
    print(f"【3】三字段均非空：{'通过' if not bad_fields else '失败 ' + str(bad_fields)}")
    problems += bool(bad_fields)

    over_t, bad_i, bad_b = [], [], []
    for c in commanders:
        e = data[c]
        t, i, b = count(e["tagline"]), count(e["intro"]), count(e["build"])
        if not (T_MIN <= t <= T_MAX):
            over_t.append((c, t))
        if not (I_MIN <= i <= I_MAX):
            bad_i.append((c, i))
        if not (B_MIN <= b <= B_MAX):
            bad_b.append((c, b))
    print(f"【4a】tagline ≤ {T_MAX}：{'通过' if not over_t else over_t}")
    print(f"【4b】intro {I_MIN}~{I_MAX}：{'通过' if not bad_i else bad_i}")
    print(f"【4c】build {B_MIN}~{B_MAX}：{'通过' if not bad_b else bad_b}")
    problems += bool(over_t) + bool(bad_i) + bool(bad_b)

    # ---- 牌名白名单 ----
    paren = re.compile(r"（([A-Za-z][^（）]*?)）")
    eng = re.compile(r"[A-Za-z][A-Za-z'’\-]*(?:\s+[A-Za-z][A-Za-z'’\-]*)*")

    bad_paren, bad_bare = [], []
    en_mentions = {}
    for c in commanders:
        for f in ("tagline", "intro", "build"):
            v = data[c][f]
            for m in paren.finditer(v):
                frag = m.group(1).strip()
                hit = match_of(frag)
                if hit is None:
                    bad_paren.append((c, f, frag))
                else:
                    en_mentions.setdefault(hit, 0)
                    en_mentions[hit] += 1
            stripped = re.sub(r"（[^（）]*）", "", v)
            for m in eng.finditer(stripped):
                frag = m.group(0).strip()
                if len(frag) < 3:
                    continue
                if match_of(frag) is None:
                    bad_bare.append((c, f, frag))
                else:
                    en_mentions.setdefault(match_of(frag), 0)
                    en_mentions[match_of(frag)] += 1

    print(f"【5a】括号内英文牌名：出现 {len(en_mentions)} 种，"
          f"未命中白名单 {len(bad_paren)} 处")
    for c, f, frag in bad_paren:
        print(f"     ✗ {c} / {f}：{frag}")
    print(f"【5b】括号外英文串：未命中白名单 {len(bad_bare)} 处")
    for c, f, frag in bad_bare:
        print(f"     ✗ {c} / {f}：{frag}")
    problems += bool(bad_paren) + bool(bad_bare)

    print("【5c】被引用的清单牌名（应为素材内牌名）：")
    for w, n in sorted(en_mentions.items()):
        print(f"     {w} ×{n}")

    if verbose:
        print("\n【明细】非空白字符数（T/I/B；括号内为与区间的差距，负=偏短 正=偏长）")
        for c in commanders:
            e = data[c]
            t, i, b = count(e["tagline"]), count(e["intro"]), count(e["build"])
            di = 0 if I_MIN <= i <= I_MAX else (I_MIN - i if i < I_MIN else I_MAX - i)
            db = 0 if B_MIN <= b <= B_MAX else (B_MIN - b if b < B_MIN else B_MAX - b)
            flag = "" if (t <= T_MAX and di == 0 and db == 0) else "   <<<"
            print(f"     {c[:34]:<34} T{t:>3} I{i:>4}({-di:+d}) B{b:>4}({-db:+d}){flag}")

    print(f"\n总判定：{'全部通过' if not problems else '存在问题，见上'}")
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
