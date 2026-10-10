#!/usr/bin/env python3
"""为 commander-quiz 的 151 位主将批量取 mtgch.com 官方中文名（最终版）。

严格「匹配不上就留空」，绝不猜。匹配分三档，逐档收紧到**可判定**的形态：

  T1 原名精确   : 候选项 name == 查询名（归一化后）。
  T2 截断查询   : 查询名含逗号时，用逗号前的主体再查一次；
                  仅接受 name == 主体 或 name 以「主体,」开头的项。
                  （用途：API 对含逗号的整串查询会返回空，
                    如 "Y'shtola, Night's Blessed" → 0 条，
                    但 "Y'shtola" → 命中该牌。这是纯查询怪癖。）
  T3 正面键面   : name 形如「<查询名> // <背面名>」，即查询名是该牌面的正面。
                  取中文名的「 // 」前一段。
                  （用途：DFC / MDFC 连体牌在 API 里以整张牌面名收录，
                    如 Esika, God of the Tree -> "Esika, God of the Tree // The Prismatic Bridge"，
                    中文 "世界树神埃西卡 // 虹彩桥" → 取 "世界树神埃西卡"。）

T2 / T3 都是**决定性**判定（查询名必须是命中牌名本身或它的正面/主体），
不是模糊相似匹配 —— 不满足条件时一律写 ""。
"""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

BASE = "https://mtgch.com/api/v1"
SRC = ROOT / "data" / "curation_table.json"
OUT = ROOT / "data" / "commander_zh.json"
REPORT = ROOT / "data" / "commander_zh_report.json"
PREV = ROOT / "data" / "_commander_zh_pass1.json"

SLEEP_BETWEEN = 0.3
RETRIES = 3
CN_FIELDS = ("display_name", "translated_name")
FACE_SEP = " // "


def norm(s: str) -> str:
    s = (s or "").replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return " ".join(s.split()).casefold()


def fetch_auto(q: str) -> list[dict]:
    url = BASE + "/autocomplete/?" + urllib.parse.urlencode({"q": q})
    last_err = None
    for attempt in range(1, RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "dsh-mtg-agent/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8", "replace"))
            items = data.get("items")
            return items if isinstance(items, list) else []
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code} {e.reason}"
            if e.code in (429, 500, 502, 503, 504) and attempt < RETRIES:
                time.sleep(attempt)
                continue
            break
        except Exception as e:  # noqa: BLE001
            last_err = f"{type(e).__name__}: {e}"
            if attempt < RETRIES:
                time.sleep(attempt)
                continue
            break
    raise RuntimeError(last_err or "unknown error")


def cn_raw(item: dict) -> str:
    for f in CN_FIELDS:
        v = item.get(f)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return ""


# 记录每个命中项的原始中文字段，用于事后审计（是否残留 ' // ' 等）
RAW_LOG: dict[str, dict] = {}


def front_only(cn: str) -> str:
    """只取正面中文名：一律切掉 ' // ' 之后的部分（搭档牌/连体牌）。

    必须**无条件**切 —— 曾出现 entry 的连体中文名分隔符间距与预期不同，
    条件式切分会漏切，导致输出里残留 ' // '。
    """
    return cn.split(FACE_SEP)[0].strip()


def match_in(items: list[dict], name_wanted: str) -> tuple[str, dict | None, str]:
    """在候选中按 T1/T3 找 name_wanted 对应的中文名。返回 (中文, 命中项, 档位)。"""
    target = norm(name_wanted)

    # T1: 整名精确
    for it in items:
        if norm(it.get("name", "")) == target:
            cn = cn_raw(it)
            if cn:
                return front_only(cn), it, "exact"

    # T3: 查询名是该牌面正面（name = "<查询名> // 背面"）
    for it in items:
        full = it.get("name", "") or ""
        if FACE_SEP not in full:
            continue
        front_en = norm(full.split(FACE_SEP)[0])
        if front_en == target:
            cn = cn_raw(it)
            if cn:
                return front_only(cn), it, "front_face"
    return "", None, ""


def match_truncated(items: list[dict], base: str) -> tuple[str, dict | None, str]:
    """T2: 用逗号前的主体匹配 name == 主体 或 name 以「主体,」开头。"""
    tb = norm(base)
    for it in items:
        full = it.get("name", "") or ""
        nf = norm(full)
        if nf == tb or nf.startswith(tb + ",") or nf.startswith(tb + FACE_SEP):
            cn = cn_raw(it)
            if cn:
                return front_only(cn), it, "truncated"
    return "", None, ""


def main() -> int:
    with open(SRC, encoding="utf-8") as f:
        rows = json.load(f)
    names = [r["name"] for r in rows]
    print(f"共 {len(names)} 位主将，开始查询…\n")

    result: dict[str, str] = {}
    report: list[dict] = []
    stats: dict[str, int] = {}

    for idx, name in enumerate(names, 1):
        best_cn, hit, via = "", None, ""
        tries: list[dict] = []
        notes: list[str] = []

        # 依次尝试的查询串：原名 → 正面/截断主体
        queries = [name]
        if FACE_SEP in name:
            # 搭档牌「A // B」：单独查前半张（正面），前面也必须是精确/正面命中
            front = name.split(FACE_SEP)[0].strip()
            if front and norm(front) != norm(name):
                queries.append(front)
        elif "," in name:
            # 含逗号的整串查询会被 API 判空，退回逗号前主体
            base = name.split(",")[0].strip()
            if base and norm(base) != norm(name):
                queries.append(base)

        for qi, q in enumerate(queries):
            try:
                items = fetch_auto(q)
            except Exception as e:  # noqa: BLE001
                notes.append(f"q={q!r} 请求失败: {e}")
                time.sleep(SLEEP_BETWEEN)
                continue

            tries.append({"q": q, "names": [it.get("name") for it in items[:10]]})

            if qi == 0:
                cn, it, v = match_in(items, name)
            else:
                cn, it, v = match_truncated(items, q)
                if not cn:                      # 截断查询也可能命中正面键面
                    cn, it, v = match_in(items, name)

            if cn:
                best_cn, hit, via = cn, it, v
                RAW_LOG[name] = {
                    "en": (it or {}).get("name"),
                    "raw_zh": cn_raw(it),
                    "used_field": next((f for f in CN_FIELDS
                                        if isinstance((it or {}).get(f), str)
                                        and (it or {}).get(f).strip()), None),
                }
                break
            time.sleep(SLEEP_BETWEEN)
        else:
            time.sleep(0)

        if best_cn:
            stats[via] = stats.get(via, 0) + 1
            tag = {"exact": "OK ", "truncated": "TRC", "front_face": "DFC",
                   "front_face_nosplit": "DFC"}.get(via, "OK ")
            print(f"[{idx:3d}/{len(names)}] {tag} {name}  ->  {best_cn}")
        else:
            stats["blank"] = stats.get("blank", 0) + 1
            print(f"[{idx:3d}/{len(names)}] --- {name}  ->  (留空)")

        result[name] = best_cn
        report.append({
            "name": name, "zh": best_cn, "matched_via": via,
            "matched_set": (hit or {}).get("set") if hit else None,
            "candidates": tries, "api_notes": notes,
        })

        if idx < len(names):
            time.sleep(SLEEP_BETWEEN)

    # ---- 回归对照：确认上一轮已命中的条目没有被改坏 ----
    regressions = []
    try:
        with open(PREV, encoding="utf-8") as f:
            prev = json.load(f)
        for k, v in prev.items():
            if v and result.get(k) != v:
                regressions.append({"name": k, "pass1": v, "final": result.get(k)})
    except FileNotFoundError:
        prev = {}

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(REPORT, "w", encoding="utf-8") as f:
        json.dump({"stats": stats, "regressions": regressions,
                   "raw_log": RAW_LOG, "entries": report},
                  f, ensure_ascii=False, indent=2)
        f.write("\n")

    # ---- 最终自检：值里不得残留 ' // '；raw_log 里带分隔符的必须已被切开 ----
    leftover = {k: v for k, v in result.items() if "//" in v}
    multi_face = {k: r["raw_zh"] for k, r in RAW_LOG.items() if FACE_SEP in (r["raw_zh"] or "")}

    print("\n" + "=" * 64)
    print("档位统计:", stats)
    print("键数:", len(result), "| 非空:", sum(1 for v in result.values() if v),
          "| 空:", sum(1 for v in result.values() if not v))
    print("回归差异（应仅为本轮新填的条目）:", len(regressions))
    for r in regressions:
        print("   ", r)
    print("自检 — 输出残留 '//' 的条目:", leftover or "无（通过）")
    print("自检 — 原始中文名含 ' // ' 的条目（应已被切开）:")
    for k, v in multi_face.items():
        print(f"    {k}\n      raw={v!r}\n      out={result.get(k)!r}")
    empties = [k for k, v in result.items() if not v]
    print("留空清单:")
    for e in empties:
        print("  -", e)
    print(f"\n已写出: {OUT}\n已写出: {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
