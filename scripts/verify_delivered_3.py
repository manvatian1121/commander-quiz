"""独立复检：只读 descriptions_3.json 交付物 + 素材 + 官方中文名表，不依赖前面的内存数据。"""
import json
import pathlib
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")
OUT = DATA / "descriptions_3.json"

raw = OUT.read_bytes()
print(f"文件：{OUT}  大小 {len(raw)} 字节  UTF-8 可解码：", end="")
try:
    text = raw.decode("utf-8")
    print("是")
except UnicodeDecodeError as exc:
    print("否！", exc)
    sys.exit(1)

data = json.loads(text)
INDEX = json.loads((DATA / "_material_3_index.json").read_text(encoding="utf-8"))
ZH = json.loads((DATA / "_card_zh_3.json").read_text(encoding="utf-8"))
ORDER = [c["en"] for c in INDEX]
CJK = re.compile(r"[\u4e00-\u9fff]")
LATIN = re.compile(r"[A-Za-z][A-Za-z0-9'’,\-:!. ]*[A-Za-z]|[A-Za-z]")
PAREN_SPAN = re.compile(r"（[^（）]*）")
CARD_PAREN = re.compile(r"（([A-Za-z][A-Za-z0-9'’,\-:!. ]*)）")

ok = True

# 1 JSON 解析
print(f"【1】JSON 解析：OK，{len(data)} 个条目")

# 2 key 完全一致
print(f"【2】key 与素材一致：{list(data) == ORDER}（缺 {[k for k in ORDER if k not in data]}，"
      f"多 {[k for k in data if k not in ORDER]}）")
ok &= list(data) == ORDER

# 3 字段非空
empties = [f"{k}.{f}" for k, v in data.items() for f in ("tagline", "intro", "build")
           if not str(v.get(f, "")).strip() or set(v) != {"tagline", "intro", "build"}]
print(f"【3】三字段非空且字段名正确：{not empties} {empties}")
ok &= not empties

# 4/5 长度
bad_len = []
for k, v in data.items():
    for f, lo, hi in (("tagline", 1, 20), ("intro", 70, 120), ("build", 110, 170)):
        s = v[f]
        tot = len(re.sub(r"\s", "", s))
        cjk = len(CJK.findall(s))
        if not (lo <= tot <= hi and lo <= cjk <= hi):
            bad_len.append(f"{k}.{f}: 总长{tot} 汉字{cjk}")
print(f"【4/5】长度全部达标（tagline≤20｜intro 70~120｜build 110~170，双口径）：{not bad_len} {bad_len}")
ok &= not bad_len

# 6 白名单 + 英文串必须出现在（）内 + 中英对照精确
by_cmdr = {c["en"]: c for c in INDEX}
outside_paren = []
not_in_list = []
bad_pair = []
used_pairs = set()
for k, v in data.items():
    own = {n.lower(): n for n in by_cmdr[k]["whitelist"]}
    for f in ("tagline", "intro", "build"):
        s = v[f]
        spans = [(m.start(), m.end()) for m in PAREN_SPAN.finditer(s)]
        inside = set()
        for a, b in spans:
            inside.update(range(a, b))
        for m in LATIN.finditer(s):
            run = m.group(0).strip(" ,:!.'’-")
            if not run or run == "X":
                continue
            if not all(i in inside for i in range(m.start(), m.end())):
                outside_paren.append(f"{k}.{f}: 「{run}」不在（）内")
            if run.lower() not in own:
                not_in_list.append(f"{k}.{f}: 「{run}」不在本主将清单内")
        for m in CARD_PAREN.finditer(s):
            inner = m.group(1).strip()
            zh_part = s[:m.start()]
            tail = re.search(r"[\u4e00-\u9fff]{2,14}$", zh_part)
            zh = tail.group(0) if tail else ""
            if inner in ZH:
                expect = ZH[inner]["zh"].split(" //")[0]
                if not zh.endswith(expect):
                    bad_pair.append(f"{k}.{f}: 「{zh}（{inner}）」≠ 官方「{expect}」")
                used_pairs.add((inner, expect))
            else:
                bad_pair.append(f"{k}.{f}: 「{inner}」无官方中文名记录")

print(f"【6】（）外出现英文：{len(outside_paren)} {outside_paren}")
print(f"【6】清单外牌名：{len(not_in_list)} {not_in_list}")
print(f"【A】中英对照全部精确：{not bad_pair} {bad_pair}")
print(f"     共引用 {len(used_pairs)} 张不同牌，全部为素材清单内、官方译名核对通过")
ok &= not (outside_paren or not_in_list or bad_pair)

# 违禁词
BANNED = ["voltron", "stax", "ramp", "引擎", "曲线", "EDHREC", "Bracket", "咸度", "最强", "上分"]
hits = [(k, b) for k, v in data.items() for b in BANNED if b.lower() in json.dumps(v, ensure_ascii=False).lower()]
print(f"【B】违禁词/吹强度用语：{len(hits)} {hits}")
ok &= not hits

print("\n--- 抽查 4 条全文 ---")
for k in ["Kotis, the Fangkeeper", "High Perfect Morcant", 'Henzie "Toolbox" Torre', "Captain N'ghathrod"]:
    v = data[k]
    print(f"\n▶ {k}")
    print(f"  tagline: {v['tagline']}")
    print(f"  intro  : {v['intro']}")
    print(f"  build  : {v['build']}")

print("\n--- 引用的牌（英文 | 中文）---")
for en, zh in sorted(used_pairs):
    print(f"   {en:32s} | {zh}")

print(f"\n{'✅ 交付物复检全部通过' if ok else '❌ 复检仍有问题'}")
