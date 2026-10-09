#!/usr/bin/env python3
"""术语一致性检查与修正。

起因：批次 6 的写作者发现别的批次把 menace 写成了「威吓」——威吓对应的是
intimidate（CR 702.13），menace 的正确译名是「威慑」（CR 702.111）。
这里做全库扫描，并把确认错误的写法统一掉。
"""
from __future__ import annotations

import json
import pathlib
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

# 错误写法 → 正确写法（附依据）
FIXES = {
    "威吓": ("威慑", "威吓是 intimidate（CR 702.13）；menace 是威慑（CR 702.111）"),
    "终结指示物": ("终命指示物", "finality counter 的官方译名（CR 122.1h）"),
    "鲜血衍生物": ("血滴衍生物", "Blood token 的官方译名（CR 111.10g）"),
    "双重打击": ("连击", "double strike 的官方译名"),
    "鲜血token": ("血滴衍生物", "同上"),
    # haste 的官方译名是「敏捷」；「给全体/全队加速」说的是给生物敏捷，不是法术力加速
    "给全体加速": ("给全体敏捷", "haste 的官方译名是敏捷，此处指给生物敏捷"),
    "给全队加速": ("给全队敏捷", "同上"),
    "给全队加敏捷": ("给全队敏捷", "同上"),
    "致命触碰": ("死触", "deathtouch 的官方译名是死触"),
    "宝物衍生物": ("珍宝衍生物", "Treasure token 的官方译名是珍宝"),
    "宝物的": ("珍宝的", "同上"),
    # 英文机制名要译成中文：Plot = 谋划
    "Plot": ("谋划", "plot 的官方中文是谋划"),
}

# 只做报告、不自动改的：可能是正常用词、官方牌名，或本身就有歧义
# 「剧毒」是 poisonous 的官方译名、「先制」是先制机制（initiative）的官方译名，
# 只有在实际指 toxic / first strike 时才是错的，必须看上下文，不能批量替换。
WATCH = ["发现", "倾探", "加速", "曲线", "引擎", "最强", "碾压",
         "剧毒", "先制", "涌现", "教唆", "双重打击"]


def main() -> int:
    files = [DATA / f"descriptions_{i}.json" for i in range(1, 17)]
    total_fix = 0

    for path in files:
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = 0
        for entry in data.values():
            for field in ("intro", "build"):
                text = entry.get(field)
                if not text:
                    continue
                for wrong, (right, _reason) in FIXES.items():
                    if wrong not in text:
                        continue
                    # 纯英文词必须按词边界替换：
                    # 否则 Gollum, Patient Plotter → 「Patient 谋划ter」、
                    # Sky Rampart → 「Sky 法术力加速art」。这个坑踩过两次。
                    if wrong.isascii():
                        pattern = r"\b" + re.escape(wrong) + r"\b"
                        changed += len(re.findall(pattern, text))
                        text = re.sub(pattern, right, text)
                    else:
                        changed += text.count(wrong)
                        text = text.replace(wrong, right)
                entry[field] = text
        if changed:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        total_fix += changed
        print(f"  {path.name}: 修正 {changed} 处")

    print(f"\n✓ 共修正 {total_fix} 处术语")

    print("\n=== 全库术语复查 ===")
    for path in files:
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        hits: dict[str, int] = {}
        for entry in data.values():
            blob = (entry.get("intro") or "") + (entry.get("build") or "")
            for wrong in FIXES:
                if wrong in blob:
                    hits[wrong] = hits.get(wrong, 0) + blob.count(wrong)
        status = "干净" if not hits else str(hits)
        print(f"  {path.name}: {status}")

    print("\n=== 观察词（只报告）===")
    for path in files:
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        hits: dict[str, int] = {}
        for entry in data.values():
            blob = (entry.get("intro") or "") + (entry.get("build") or "")
            for word in WATCH:
                if word in blob:
                    hits[word] = hits.get(word, 0) + blob.count(word)
        if hits:
            print(f"  {path.name}: {hits}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
