# -*- coding: utf-8 -*-
"""descriptions_14.json 自检（独立读盘，不依赖构建脚本）。

6 项：
  [1] JSON 可解析 / 条目数 30 / key 与素材一致
  [2] 三字段非空；tagline ≤20（去空格可见字符数）
  [3] intro 70~120；build 110~170
  [4] 逐主将白名单：正文英文牌名必须属于该主将自己的清单
  [5] 中英并列：中文名必须等于 card_zh.json 的官方值；缺映射只能写英文
  [6] 术语：haste=敏捷（不写"加速"）、menace=威慑（不写"威吓"）、intimidate 才是威吓
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

BASE = pathlib.Path(ROOT)
DATA = BASE / "data"
MD = DATA / "writing_batch_new_6.md"
JSONP = DATA / "descriptions_14.json"
CARD_ZH = DATA / "card_zh.json"

HEAD_LINE = re.compile(r"^## (.+?) ｜ (.+?)\s*$")
CARD_LINE = re.compile(r"^\s+(?:\d+\.|[-*])\s+(.+?)（")
LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z0-9'’.,!\-\s]*[A-Za-z0-9'’!]|[A-Za-z]")
PAREN_PAIR = re.compile(r"([\u4e00-\u9fff·]*)[（(]([A-Za-z][^（）()]*?)[）)]")
CJK = re.compile(r"[\u4e00-\u9fff]")

FORBIDDEN_TERMS = ["加速", "威吓", "威摄", "voltron", "stax", "ramp",
                   "引擎", "曲线", "最强", "上分", "Bracket", "EDHREC", "咸度", "咸味"]
LATIN_BOUNDED = re.compile(r"\b(?:voltron|stax|ramp)\b", re.I)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.replace("’", "'").lower())


def count(s: str) -> int:
    return sum(1 for ch in s if not ch.isspace())


def parse_material() -> dict[str, list[str]]:
    lists: dict[str, list[str]] = {}
    cur: str | None = None
    for line in MD.read_text(encoding="utf-8").splitlines():
        h = HEAD_LINE.match(line)
        if h:
            cur = h.group(1).strip()
            lists[cur] = []
            continue
        if cur is None:
            continue
        m = CARD_LINE.match(line)
        if m:
            n = m.group(1).strip()
            if n not in lists[cur]:
                lists[cur].append(n)
    return lists


def main() -> int:
    problems: list[str] = []
    notes: list[str] = []

    material = parse_material()
    raw = JSONP.read_text(encoding="utf-8")
    data = json.loads(raw)  # [1] 解析
    print("[1] JSON 可解析：OK")
    print(f"    条目数：{len(data)}（素材 {len(material)}）")
    if len(data) != 30:
        problems.append(f"条目数 {len(data)} != 30")
    if set(data) != set(material):
        problems.append(f"key 不一致：缺 {sorted(set(material) - set(data))}，多 {sorted(set(data) - set(material))}")
    else:
        print("    key 与素材逐字一致 ✓")
    if list(data) != list(material):
        notes.append("key 顺序与素材不同（无影响）")

    zh_map: dict[str, str] = json.loads(CARD_ZH.read_text(encoding="utf-8"))
    # 主将自己的官方中文名：card_zh.json 常缺，素材标题与 commander_zh.json 一致（已核对 30/30）
    cmd_zh: dict[str, str] = json.loads((DATA / "commander_zh.json").read_text(encoding="utf-8"))
    head_zh: dict[str, str] = {}
    for line in MD.read_text(encoding="utf-8").splitlines():
        h = HEAD_LINE.match(line)
        if h:
            head_zh[h.group(1).strip()] = h.group(2).strip()
    zh_map.update(cmd_zh)
    mismatch_head = [k for k in material if zh_map.get(k) and zh_map[k] != head_zh.get(k)]
    print(f"[1b] 主将中文名：素材标题 vs commander_zh.json 不一致 {len(mismatch_head)} 处"
          f"{'（' + str(mismatch_head) + '）' if mismatch_head else ' ✓'}")
    zh_map.update({k: v for k, v in head_zh.items() if k not in zh_map})
    # 双面主将：正面名视为同一条目（素材标题 / commander_zh 给的是正面中文名）
    for k, v in list(zh_map.items()):
        if " // " in k:
            for face in k.split(" // "):
                zh_map.setdefault(face.strip(), v)

    # [2][3] 字段与长度
    empty, over_t, over_i, over_b = [], [], [], []
    for k, e in data.items():
        for f in ("tagline", "intro", "build"):
            if not str(e.get(f, "")).strip():
                empty.append(f"{k}.{f}")
        t, i, b = count(e["tagline"]), count(e["intro"]), count(e["build"])
        if t > 20:
            over_t.append((k, t))
        if not (70 <= i <= 120):
            over_i.append((k, i))
        if not (110 <= b <= 170):
            over_b.append((k, b))
    print(f"[2] 三字段非空：{'通过' if not empty else empty}")
    print(f"    tagline ≤20：{'通过' if not over_t else over_t}"
          f"（实测 {min(count(e['tagline']) for e in data.values())}~{max(count(e['tagline']) for e in data.values())}）")
    print(f"[3] intro 70~120：{'通过' if not over_i else over_i}"
          f"（实测 {min(count(e['intro']) for e in data.values())}~{max(count(e['intro']) for e in data.values())}）")
    print(f"    build 110~170：{'通过' if not over_b else over_b}"
          f"（实测 {min(count(e['build']) for e in data.values())}~{max(count(e['build']) for e in data.values())}）")
    problems += [f"空字段 {x}" for x in empty] + [f"tagline 超长 {x}" for x in over_t] \
        + [f"intro 越界 {x}" for x in over_i] + [f"build 越界 {x}" for x in over_b]

    # [4] 白名单（英文牌名必须属于本主将清单）
    outside: list[tuple[str, str, str]] = []
    truncated: list[tuple[str, str, str]] = []
    used: dict[str, set[str]] = {}
    for k, e in data.items():
        allowed = list(material[k]) + [k]
        norm_allowed = {n: norm(n) for n in allowed}
        used[k] = set()
        for f in ("tagline", "intro", "build"):
            for m in LATIN_RUN.finditer(e[f]):
                run = m.group(0).strip(" .,-!")
                if sum(c.isalpha() for c in run) < 2:
                    continue
                nr = norm(run)
                exact = [n for n, nn in norm_allowed.items() if nn == nr]
                if exact:
                    used[k].update(exact)
                    continue
                if any(nr in nn for nn in norm_allowed.values()):
                    truncated.append((k, f, run))
                    continue
                # 贪心拼接：整段是否由若干清单牌名拼成
                rest = nr
                for n in sorted(norm_allowed.values(), key=len, reverse=True):
                    while n and n in rest:
                        rest = rest.replace(n, "")
                if rest == "":
                    continue
                outside.append((k, f, run))
    print(f"[4] 白名单：{'通过' if not outside else '发现问题'}")
    if outside:
        for k, f, run in outside:
            print(f"    ✗ {k} / {f}：「{run}」不在本主将清单内")
    if truncated:
        print("    · 属于清单牌名的截断写法（非新增牌名）：")
        for k, f, run in truncated:
            print(f"      {k} / {f}：「{run}」")
    problems += [f"清单外牌名 {k}/{f}：{run}" for k, f, run in outside]
    cited = sum(len(v) for v in used.values())
    print(f"    命中清单牌名 {cited} 处（含主将自指），覆盖 {len([k for k in used if used[k]])}/{len(data)} 位主将")

    # [5] 中英并列 / 官方中文名
    bad_zh, bad_bare = [], []
    bare_ok, paren_total = 0, 0
    for k, e in data.items():
        allowed = list(material[k]) + [k]
        norm_allowed = [norm(n) for n in allowed]
        for f in ("tagline", "intro", "build"):
            v = e[f]
            for m in PAREN_PAIR.finditer(v):
                pre, en = m.group(1), m.group(2).strip()
                paren_total += 1
                nr = norm(en)
                if not any(nr in nn for nn in norm_allowed):
                    bad_zh.append((k, f, en, "括号内英文不在清单"))
                    continue
                official = zh_map.get(en)
                if official is None:
                    # 无官方映射 -> 不该有中文前缀
                    if pre:
                        bad_zh.append((k, f, en, f"无官方中文名却写了前缀「{pre}」"))
                elif not pre.endswith(official):
                    bad_zh.append((k, f, en, f"中文「{pre}」≠ 官方「{official}」"))
            # 括号外的裸英文牌名：必须是没有官方中文名的那类
            outside_parens = re.sub(r"[（(][^（）()]*[）)]", "", v)
            for m in LATIN_RUN.finditer(outside_parens):
                run = m.group(0).strip(" .,-!")
                if sum(c.isalpha() for c in run) < 2:
                    continue
                nr = norm(run)
                if not any(nr in nn for nn in norm_allowed):
                    continue  # 已由 [4] 报出
                if nr in {norm(n) for n in allowed}:
                    hit = [n for n in allowed if norm(n) == nr][0]
                    if hit in zh_map:
                        bad_bare.append((k, f, hit))
                    else:
                        bare_ok += 1
    print(f"[5] 中英并列：括号对 {paren_total} 处；{'全部合规' if not bad_zh else '发现问题'}")
    if bad_zh:
        for k, f, en, why in bad_zh:
            print(f"    ✗ {k} / {f}：「{en}」{why}")
    print(f"    无官方中文名、按规则只写英文：{bare_ok} 处（均为括号外裸英文）")
    if bad_bare:
        print("    ✗ 有官方中文名却只写了英文：")
        for k, f, hit in bad_bare:
            print(f"      {k} / {f}：{hit}")
    problems += [f"中英并列问题 {k}/{f}：{en} {why}" for k, f, en, why in bad_zh]
    problems += [f"该并列却只写英文 {k}/{f}：{hit}" for k, f, hit in bad_bare]

    # [6] 术语
    hits: list[tuple[str, str, str]] = []
    for k, e in data.items():
        for f in ("tagline", "intro", "build"):
            for term in FORBIDDEN_TERMS:
                if term in e[f]:
                    hits.append((k, f, term))
            for m in LATIN_BOUNDED.finditer(e[f]):
                hits.append((k, f, m.group(0)))
    print(f"[6] 术语：{'通过' if not hits else '发现问题'}")
    for k, f, term in hits:
        print(f"    ✗ {k} / {f}：出现「{term}」")
    problems += [f"术语 {k}/{f}：{term}" for k, f, term in hits]
    corpus = "".join(f for e in data.values() for f in e.values())
    print(f"    正向使用：敏捷 {corpus.count('敏捷')} 次、威慑 {corpus.count('威慑')} 次、"
          f"威吓 {corpus.count('威吓')} 次、加速 {corpus.count('加速')} 次")

    print("\n=== 结论 ===")
    if problems:
        for p in problems:
            print(f"  ✗ {p}")
        print(f"  共 {len(problems)} 项问题")
        return 1
    print("  6 项自检全部通过")
    for n in notes:
        print(f"  · {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
