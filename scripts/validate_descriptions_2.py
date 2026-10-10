#!/usr/bin/env python3
"""descriptions_2.json 自检：6 项。"""
from __future__ import annotations

import json
import pathlib
import re
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

DATA = pathlib.Path(ROOT / "data")
MD = DATA / "writing_batch_2.md"
JSON = DATA / "descriptions_2.json"

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
# 英文单词序列：拉丁字母 + 数字 + 名称里可能出现的标点
EN = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9'’.,\- ]{2,}")
CARD_LINE = re.compile(r"^\s+(?:\d+\.|[-*])\s+(.+?)（")
HEAD_LINE = re.compile(r"^## (.+?) ｜ ")


def norm(text: str) -> str:
    text = text.replace("’", "'").lower()
    text = re.sub(r"[.,]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_material() -> tuple[dict[str, list[str]], dict[str, str]]:
    """返回 {主将: [本卡清单牌名]} 与 {主将: 中文名}。"""
    lists: dict[str, list[str]] = {}
    zh: dict[str, str] = {}
    current: str | None = None
    for line in MD.read_text(encoding="utf-8").splitlines():
        head = HEAD_LINE.match(line)
        if head:
            current = head.group(1).strip()
            lists[current] = []
            zh[current] = line.split("｜", 1)[1].strip()
            continue
        if current is None:
            continue
        m = CARD_LINE.match(line)
        if m:
            lists[current].append(m.group(1).strip())
    return lists, zh


def main() -> int:
    problems: list[str] = []
    notes: list[str] = []

    lists, zh_names = parse_material()
    raw = JSON.read_text(encoding="utf-8")
    data = json.loads(raw)

    # 1 JSON 可解析（上面已解析成功）
    print("[1] JSON 解析：OK")

    # 2 条目数与 key
    print(f"[2] 条目数：{len(data)}（素材 {len(lists)}）")
    if len(data) != 37:
        problems.append(f"条目数 {len(data)} != 37")
    if set(data) != set(lists):
        problems.append(f"key 不一致：多 {sorted(set(data) - set(lists))} 缺 {sorted(set(lists) - set(data))}")
    else:
        print("    key 与素材完全一致")

    # 3 三字段非空
    for key, entry in data.items():
        for field in ("tagline", "intro", "build"):
            if not str(entry.get(field, "")).strip():
                problems.append(f"{key}.{field} 为空")
    print("[3] 三字段非空：检查完成")

    # 4/5 长度
    print("[4/5] 长度（tagline ≤20 字；intro 70~120；build 110~170，均为中文字符数）")
    for key, entry in data.items():
        tag = entry["tagline"]
        tag_len = len(tag)
        if tag_len > 20:
            problems.append(f"tagline 超长 {tag_len}：{key}「{tag}」")
        for field, lo, hi in (("intro", 70, 120), ("build", 110, 170)):
            text = entry[field]
            cjk = len(CJK.findall(text))
            total = len(text)
            mark = ""
            if cjk < lo:
                mark = "  ← 偏短"
                problems.append(f"{field} 偏短 {cjk}（{lo}~{hi}）：{key}")
            elif cjk > hi:
                mark = "  ← 偏长"
                problems.append(f"{field} 偏长 {cjk}（{lo}~{hi}）：{key}")
            print(f"    {key:<32} {field:<8} 中文 {cjk:>4} 总长 {total:>4}{mark}")

    # 6 牌名白名单
    print("[6] 牌名白名单")
    global_ok = {norm(n) for names in lists.values() for n in names}
    global_ok |= {norm(n) for n in lists}
    for key, entry in data.items():
        allowed = {norm(n) for n in lists[key]} | {norm(key)}
        text = " ".join(entry.values())
        for match in EN.finditer(text):
            seq = match.group(0).strip(" .,-")
            if sum(c.isalpha() for c in seq) < 2:
                continue
            if norm(seq) in allowed:
                continue
            tag = "全局白名单内有、但不在本位主将清单" if norm(seq) in global_ok else "完全不在白名单"
            problems.append(f"清单外牌名：{key} → 「{seq}」（{tag}）")
    if not any(p.startswith("清单外牌名") for p in problems):
        print("    未发现清单外英文牌名")

    # 额外：牌名出现次数统计
    print("\n附：每位主将 build 里提到的牌")
    for key, entry in data.items():
        found = [m.group(0).strip(" .,-") for m in EN.finditer(entry["build"])]
        print(f"    {key:<32} {'、'.join(found)}")

    print("\n=== 结论 ===")
    if problems:
        for p in problems:
            print(f"  ✗ {p}")
    else:
        print("  6 项全部通过")
    for n in notes:
        print(f"  · {n}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
