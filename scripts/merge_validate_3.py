"""合并 4 份分片 → descriptions_3.json，并跑 6 项自检 + 2 项加强检查。

自检项：
 1. JSON 可解析
 2. 条目数 = 36，key 与素材主将名完全一致
 3. 三个字段都非空
 4. tagline <= 20 字
 5. intro 70~120 字 / build 110~170 字（同时按「总长（去空白）」和「纯汉字数」两种口径算）
 6. 牌名白名单校验（素材内所有牌名做成白名单）
加强检查：
 A. 中英对照一致性：正文里每个「中文（English）」的中文必须等于 API 查到的官方中文名
 B. 违禁词：写作规范禁用的行话与后台指标名
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
INDEX = json.loads((DATA / "_material_3_index.json").read_text(encoding="utf-8"))
ZH = json.loads((DATA / "_card_zh_3.json").read_text(encoding="utf-8"))

parts = []
for i in (1, 2, 3, 4):
    parts.append(json.loads((DATA / f"_part{i}_3.json").read_text(encoding="utf-8")))

merged: dict[str, dict] = {}
for p in parts:
    overlap = set(merged) & set(p)
    if overlap:
        print("!! 分片 key 重复：", overlap)
    merged.update(p)

ORDER = [c["en"] for c in INDEX]
out = {k: merged[k] for k in ORDER if k in merged}

CJK = re.compile(r"[\u4e00-\u9fff]")
LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z0-9'’,\- ]*[A-Za-z]|[A-Za-z]")
PAIR = re.compile(r"([\u4e00-\u9fff]{2,14})（([A-Za-z][A-Za-z0-9'’,\-:! ]*)）")
ALLOWED_SYMBOL = {"X"}

BANNED = ["voltron", "stax", "ramp", "引擎", "曲线", "EDHREC", "Bracket", "bracket", "咸度"]

problems: list[str] = []
warn: list[str] = []
cross_list: list[str] = []
pair_bad: list[str] = []
unknown_latin: list[str] = []
banned_hits: list[str] = []


def counts(s: str) -> tuple[int, int]:
    return len(re.sub(r"\s", "", s)), len(CJK.findall(s))


# --- 2. key 一致性 ---
missing = [k for k in ORDER if k not in merged]
extra = [k for k in merged if k not in ORDER]
if missing:
    problems.append(f"[2] 缺少主将：{missing}")
if extra:
    problems.append(f"[2] 多余 key：{extra}")
print(f"【2】条目数 = {len(merged)}（素材 {len(ORDER)}）；缺 {len(missing)}，多 {len(extra)}")

GLOBAL_NAMES = {n.lower() for c in INDEX for n in c["whitelist"]}

for c in INDEX:
    en = c["en"]
    if en not in merged:
        continue
    own = {n.lower() for n in c["whitelist"]}
    entry = merged[en]
    for field in ("tagline", "intro", "build"):
        text = entry.get(field, "")
        if not str(text).strip():
            problems.append(f"[3] {en}.{field} 为空")

    tag = entry.get("tagline", "")
    intro = entry.get("intro", "")
    build = entry.get("build", "")

    # --- 4 / 5 长度 ---
    t_tot, t_cjk = counts(tag)
    if t_tot > 20 or t_cjk > 20:
        problems.append(f"[4] {en} tagline 超长：总长 {t_tot} / 汉字 {t_cjk}")
    i_tot, i_cjk = counts(intro)
    if not (70 <= i_tot <= 120 and 70 <= i_cjk <= 120):
        problems.append(f"[5] {en} intro 越界：总长 {i_tot} / 汉字 {i_cjk}")
    b_tot, b_cjk = counts(build)
    if not (110 <= b_tot <= 170 and 110 <= b_cjk <= 170):
        problems.append(f"[5] {en} build 越界：总长 {b_tot} / 汉字 {b_cjk}")

    # --- 6 白名单 + A 中英对照 + B 违禁词 ---
    for field in ("tagline", "intro", "build"):
        text = entry.get(field, "")
        for run in LATIN_RUN.findall(text):
            r = run.strip(" ,'-’")
            if not r:
                continue
            if r in ALLOWED_SYMBOL:
                continue
            low = r.lower()
            if low in GLOBAL_NAMES:
                if low not in own:
                    cross_list.append(f"{en}.{field}: {r}（在本主将清单之外）")
            elif not any(low in n for n in own):
                unknown_latin.append(f"{en}.{field}: {r}")
        for m in PAIR.finditer(text):
            zh_name, en_name = m.group(1), m.group(2).strip()
            expect = ZH.get(en_name, {}).get("zh", "")
            base = expect.split(" //")[0]
            if not expect:
                pair_bad.append(f"{en}.{field}: {en_name} 无官方中文名记录，却写了「{zh_name}」")
            elif not zh_name.endswith(base):
                pair_bad.append(f"{en}.{field}: 「{zh_name}（{en_name}）」结尾应为「{base}」")
        for b in BANNED:
            if b.lower() in text.lower():
                idx = text.lower().find(b.lower())
                banned_hits.append(f"{en}.{field}: 「{text[max(0, idx-6):idx+len(b)+6]}」（命中 {b}）")

print(f"【3】空字段：{sum(1 for p in problems if p.startswith('[3]'))}")
print(f"【4】tagline 超长：{sum(1 for p in problems if p.startswith('[4]'))}")
print(f"【5】intro/build 越界：{sum(1 for p in problems if p.startswith('[5]'))}")
print(f"【6】白名单外的英文串：{len(unknown_latin)}   跨主将清单引用：{len(cross_list)}")
print(f"【A】中英对照不一致：{len(pair_bad)}")
print(f"【B】违禁词命中：{len(banned_hits)}")

for name, lst in (("问题", problems), ("白名单外英文串", unknown_latin), ("跨清单", cross_list),
                  ("中英对照", pair_bad), ("违禁词", banned_hits)):
    if lst:
        print(f"\n--- {name} ---")
        for x in lst:
            print("   ", x)

# 长度明细
print("\n--- 长度明细（tagline总长 / intro总长·汉字 / build总长·汉字）---")
for c in INDEX:
    e = merged.get(c["en"])
    if not e:
        continue
    tt, _ = counts(e["tagline"])
    it, ic = counts(e["intro"])
    bt, bc = counts(e["build"])
    flag = ""
    if not (70 <= it <= 120 and 70 <= ic <= 120):
        flag += " <intro!"
    if not (110 <= bt <= 170 and 110 <= bc <= 170):
        flag += " <build!"
    if tt > 20:
        flag += " <tag!"
    print(f"   {c['en'][:34]:36s} {tt:3d} | {it:4d}·{ic:4d} | {bt:4d}·{bc:4d}{flag}")

if not problems and not unknown_latin and not cross_list and not pair_bad and not banned_hits:
    (DATA / "descriptions_3.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n✅ 全部通过，已写出 descriptions_3.json")
else:
    print("\n❌ 存在问题，未写出 descriptions_3.json")
