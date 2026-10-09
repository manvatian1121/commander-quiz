# -*- coding: utf-8 -*-
"""附加审计：
 A. 中英并列配对检查 —— 正文里「中文（English）」结构，括号前的中文是否与 API 中文名对得上。
 B. 只写中文、没写英文的牌名（rule「中英并列」的漏项）—— 用 API 中文名反查。
 C. 历史上已交付的 descriptions_3.json 做同样统计，用于比对house style。
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

zh4 = json.loads((DATA / "zh_cards.json").read_text(encoding="utf-8"))          # 本批 299 个名字
_zh3raw = json.loads((DATA / "_card_zh_3.json").read_text(encoding="utf-8"))    # 上一批
zh3 = {k: (v.get("zh") if isinstance(v, dict) else v) for k, v in _zh3raw.items()}


def front(v):
    return (v or "").split(" // ")[0].strip()


def audit(path, zhmap, label):
    data = json.loads(path.read_text(encoding="utf-8"))
    rev = {}
    for en, cn in zhmap.items():
        cn = front(cn)
        if len(cn) >= 3:
            rev.setdefault(cn, en)
    names = sorted(rev, key=len, reverse=True)
    print(f"\n=== {label}（{len(data)} 条，中文名表 {len(rev)} 个）===")
    pair_bad, cn_only_total = [], 0
    for k, e in data.items():
        for f in ("tagline", "intro", "build"):
            v = e[f]
            # A: 中文（English） 配对
            for m in re.finditer(r"([\u4e00-\u9fff·]+)（([A-Za-z][^（）]*?)）", v):
                cn_frag, en_frag = m.group(1), m.group(2)
                want = front(zhmap.get(en_frag, ""))
                if not want:
                    continue
                if not cn_frag.endswith(want):
                    pair_bad.append((k, f, cn_frag, en_frag, want))
            # B: 纯中文牌名（该条里没有配对的英文）
            body = v
            for cn, en in rev.items():
                if cn in body and en.lower() not in body.lower():
                    cn_only_total += 1
                    print(f"  [纯中文] {k} / {f}：{cn}（{en}）")
    print(f"  A 配对不符：{len(pair_bad)}")
    for r in pair_bad:
        print("    ✗", r)
    print(f"  B 纯中文牌名出现次数：{cn_only_total}")
    return len(pair_bad), cn_only_total


if __name__ == "__main__":
    audit(DATA / "descriptions_7.json", zh4, "本批 descriptions_7（素材4）")
    try:
        audit(DATA / "descriptions_3.json", zh3, "上批 descriptions_3（对照）")
    except Exception as ex:
        print("对照批读取失败：", ex)
