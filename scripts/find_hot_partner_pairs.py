#!/usr/bin/env python3
"""找出最热门的拍档 / 身世组合。

全枚举 4302 组太慢，而热门组合一定由热门单卡组成。
所以先查每张单卡的独立流行度，只把最热的那批两两配对，再探 EDHREC。
"""
from __future__ import annotations

import itertools
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request


# --- 路径相对本文件解析，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = ROOT / "data"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

DIACRITICS = str.maketrans({"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
                            "ñ": "n", "û": "u", "ü": "u", "à": "a", "â": "a"})
TOP_N = 22          # 只取最热的 N 张单卡两两配对
MIN_DECKS = 800     # 组合的套牌数门槛


def slugify(name: str) -> str:
    base = name.translate(DIACRITICS).replace("'", "").replace("\u2019", "")
    base = base.replace(",", "").replace(" // ", "-").replace(" ", "-").lower()
    base = re.sub(r"[^a-z0-9\-]", "", base)
    return re.sub(r"-+", "-", base).strip("-")


def fetch(slug: str):
    url = f"https://json.edhrec.com/pages/commanders/{slug}.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            payload = json.loads(r.read().decode("utf-8", "replace"))
    except Exception:  # noqa: BLE001
        return None
    card = (payload.get("container") or {}).get("json_dict", {}).get("card") or {}
    if not card.get("num_decks"):
        return None
    return {"name": card.get("name"), "num_decks": card.get("num_decks"),
            "rank": card.get("rank"), "color_identity": card.get("color_identity")}


def main() -> int:
    pools = json.loads((DATA / "partner_pool.json").read_text(encoding="utf-8"))
    singles = {
        "泛用拍档": pools["generic_partner"],
        "身世指挥官": pools["choose_background"],
        "身世牌": pools["backgrounds"],
        "指定拍档": pools["partner_with"],
    }

    # ① 查每张单卡的独立流行度
    scored: dict[str, list[dict]] = {}
    for label, names in singles.items():
        rows = []
        for n in names:
            p = fetch(slugify(n))
            if p:
                rows.append(p)
            time.sleep(0.28)
        rows.sort(key=lambda r: -(r["num_decks"] or 0))
        scored[label] = rows
        print(f"\n【{label}】有档案 {len(rows)}/{len(names)}，最热 6 张：")
        for r in rows[:6]:
            print(f"    {r['num_decks']:>7,}  #{str(r['rank']):>5}  {r['name']}")

    # ② 生成组合并探测
    def pairs(names_a, names_b=None, both_orders=True):
        if names_b is None:
            combos = list(itertools.combinations(names_a, 2))
        else:
            combos = list(itertools.product(names_a, names_b))
        return combos

    jobs: list[tuple[str, str]] = []
    hot_generic = [r["name"] for r in scored["泛用拍档"][:TOP_N]]
    hot_bgcmd = [r["name"] for r in scored["身世指挥官"][:TOP_N]]
    hot_bg = [r["name"] for r in scored["身世牌"][:20]]
    hot_with = [r["name"] for r in scored["指定拍档"][:TOP_N]]

    for a, b in pairs(hot_generic):
        jobs += [(f"{a} // {b}", "拍档"), (f"{b} // {a}", "拍档")]
    for a, b in pairs(hot_bgcmd, hot_bg):
        jobs += [(f"{a} // {b}", "身世"), (f"{b} // {a}", "身世")]
    for a, b in pairs(hot_with):
        jobs += [(f"{a} // {b}", "指定拍档"), (f"{b} // {a}", "指定拍档")]

    print(f"\n待探组合（含两种顺序）：{len(jobs)} 个")
    print("预计耗时 {:.0f} 分钟\n".format(len(jobs) * 0.3 / 60))

    found: dict[str, dict] = {}
    for i, (name, kind) in enumerate(jobs, 1):
        slug = slugify(name)
        if slug in found:
            continue
        p = fetch(slug)
        if p and p["num_decks"] >= MIN_DECKS:
            p["kind"] = kind
            p["slug"] = slug
            found[p["name"]] = p
            print(f"  ✓ {p['num_decks']:>7,}  #{str(p['rank']):>5}  {p['name']}")
        if i % 200 == 0:
            print(f"    …{i}/{len(jobs)}　已找到 {len(found)}", flush=True)
        time.sleep(0.26)

    rows = sorted(found.values(), key=lambda r: -(r["num_decks"] or 0))
    (DATA / "partner_candidates.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n=== 套牌数 ≥{MIN_DECKS} 的组合：{len(rows)} 个 ===")
    for r in rows:
        print(f"  {r['num_decks']:>7,}  #{str(r['rank']):>5}  {r['kind']:<5}  {r['name']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
