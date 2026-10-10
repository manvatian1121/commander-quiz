# -*- coding: utf-8 -*-
"""校对辅助扫描：对 bank4 / bank5 / bankC / bankE 做文本层与向量层的体检。

只读，不写文件。输出供人工阅读用。
"""
import sys, json, re, math
from pathlib import Path
from itertools import combinations



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

DATA = Path(ROOT / "data")
FILES = ["bank4.json", "bank5.json", "bankC.json", "bankE.json"]


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def vec(opt):
    v = dict(opt.get("s") or {})
    for k in ("col", "cval"):
        for kk, vv in (opt.get(k) or {}).items():
            v[f"{k}:{kk}"] = vv
    if "exp" in opt:
        v["exp"] = opt["exp"]
    return v


def cos(a, b):
    keys = set(a) | set(b)
    num = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
    da = math.sqrt(sum(a.get(k, 0) ** 2 for k in keys))
    db = math.sqrt(sum(b.get(k, 0) ** 2 for k in keys))
    if da == 0 or db == 0:
        return 0.0
    return num / (da * db)


DUP_CHAR_WHITELIST = {"慢慢", "一点点", "轻轻", "常常", "刚刚", "渐渐", "悄悄",
                      "静静", "多多", "紧紧", "死死", "好好", "连连", "处处",
                      "人人", "天天", "年年", "一一", "两两", "各自", "明明"}

SUSPECT_PAIRS = ["在再", "做作", "必需", "必须", "其它", "其他", "帐", "账",
                 "既", "即", "需", "须", "份", "分"]

ASCII_PUNCT = re.compile(r"[,.;:!?()]")

report = []
ALL = {}

for name in FILES:
    data = load(name)
    qs = data["questions"]
    ALL[name] = data
    report.append("=" * 78)
    report.append(f"### {name}  batch={data.get('batch')!r}  题数={len(qs)}")
    report.append("=" * 78)
    for q in qs:
        opts = q["opts"]
        report.append(f"\n-- {q['id']}  [{q.get('sec')}]  kind={q.get('kind')} multi={q.get('multi')} "
                      f"next={q.get('next')!r}  选项数={len(opts)}")
        report.append(f"   Q: {q['q']}")
        # 题干层
        for m in re.finditer(r"(.)\1", q["q"]):
            if m.group(0) not in DUP_CHAR_WHITELIST:
                report.append(f"   [题干叠字] {m.group(0)!r} @{m.start()}")
        if q["q"].rstrip().endswith(("你会？", "你会选？")):
            report.append("   [题干截断] 以「你会？/你会选？」结尾")
        for m in ASCII_PUNCT.finditer(q["q"]):
            report.append(f"   [题干半角标点] {m.group(0)!r}")
        # 选项层
        texts = [o["t"] for o in opts]
        for i, t in enumerate(texts):
            tag = f"      {chr(65+i)}: {t}"
            report.append(tag)
            for m in re.finditer(r"(.)\1", t):
                if m.group(0) not in DUP_CHAR_WHITELIST:
                    report.append(f"         [叠字] {m.group(0)!r} @{m.start()}")
            for m in ASCII_PUNCT.finditer(t):
                report.append(f"         [半角标点] {m.group(0)!r}")
            if t != t.strip():
                report.append("         [首尾空格]")
            if re.search(r"[\u4e00-\u9fff][0-9]|[0-9][\u4e00-\u9fff]", t):
                report.append("         [中西文数字混排] 复核")
            if re.search(r"[得地]", t):
                report.append(f"         [得/地] 复核: {re.findall(r'.{0,4}[得地].{0,4}', t)}")
            if opt_has := [p for p in SUSPECT_PAIRS if p in t]:
                report.append(f"         [易错字] {opt_has}")
        # 选项文本重复
        seen = {}
        for i, t in enumerate(texts):
            key = t.strip()
            if key in seen:
                report.append(f"   [选项重复] {chr(65+seen[key])} 与 {chr(65+i)} 文本相同")
            seen[key] = i
        # 向量
        vs = [vec(o) for o in opts]
        for i, j in combinations(range(len(opts)), 2):
            c = cos(vs[i], vs[j])
            if c >= 0.85:
                report.append(f"   [余弦≥0.85] {chr(65+i)}-{chr(65+j)} = {c:.3f}")
            if vs[i] == vs[j]:
                report.append(f"   [向量完全相同] {chr(65+i)}-{chr(65+j)}")
            if set(vs[i]) == set(vs[j]) and vs[i] != vs[j]:
                report.append(f"   [键集合相同] {chr(65+i)}-{chr(65+j)}")
            if not vs[i] or not vs[j]:
                report.append(f"   [空向量] {chr(65+i) if not vs[i] else chr(65+j)}")

# 汇总
report.append("\n" + "=" * 78)
report.append("### 汇总")
report.append("=" * 78)
b4 = ALL["bank4.json"]["questions"]
col_count = {}
for q in b4:
    for o in q["opts"]:
        for k in (o.get("col") or {}):
            col_count[k] = col_count.get(k, 0) + 1
report.append(f"bank4 col 计数: {col_count}  合计={sum(col_count.values())}")
report.append("bank4 带 col 的题: " + ", ".join(q["id"] for q in b4 if any(o.get("col") for o in q["opts"])))
b5 = ALL["bank5.json"]["questions"]
report.append("bank5 multi: " + ", ".join(f"{q['id']}={q.get('multi')}" for q in b5 if "multi" in q))
for name in FILES:
    ids = [q["id"] for q in ALL[name]["questions"]]
    report.append(f"{name} ids({len(ids)}): {ids}")

out = DATA / "proof_scan_45CE.txt"
out.write_text("\n".join(report), encoding="utf-8")
print("\n".join(report))
print(f"\n[saved] {out}")
