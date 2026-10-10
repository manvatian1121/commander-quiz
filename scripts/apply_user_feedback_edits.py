#!/usr/bin/env python3
"""按 data/USER_FEEDBACK_SPEC.md 的 9 条实测反馈修改题库（只改这 9 道题）。

- 改动前备份全部 bank*.json 到 _scratch/data/_feedback_bak/
- id / next / goto / kind / cval 一律不碰
- 写入用 json.dumps(ensure_ascii=False, indent=2)，已实测与现有文件字节级一致，
  因此未被改动的题目在磁盘上保持原样。

用法： python scripts/apply_user_feedback_edits.py          # 真正写入
       python scripts/apply_user_feedback_edits.py --dry    # 只报告
"""
from __future__ import annotations

import json
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
BAK = ROOT / "_scratch" / "data" / "_feedback_bak"

# 题干改动（s50 需要覆盖「看片 / 刷视频」两种）
SET_Q = {
    ("bank4.json", "s50"): "周末晚上窝在沙发上，你会点开哪一类？（长片、短视频都算）",
}

# 改写已有选项：expect_* 先校验旧值，避免误改
SET_OPTS = {
    ("bank2.json", "s19", 1): {
        "expect_t": "干脆两台都买回来用一周，留顺手的那台",
        "expect_s": {"wide": 1.9, "aggro": 0.73, "artifacts": 0.8},
        "t": "先划一条硬底线：有一条指标绝不能让步，剩下的全凭顺眼",
        "s": {"stax": 1.05, "enchant": 1.4},
    },
    # s24 是枢纽题：只改措辞，轴与 goto 全部保持原样
    ("bank2.json", "s24", 1): {
        "expect_t": "最坏能坏到哪，我兜不兜得住",
        "t": "真砸了，我手上的钱和精力扛不扛得住",
    },
    ("bank2.json", "s24", 2): {
        "expect_t": "万一走错了，我还能不能回来",
        "t": "万一走错了，还能不能原样退回来",
    },
    # c05 是约束题：只改文本，cval 与轴都不动
    ("bankC.json", "c05", 1): {
        "expect_t": "看人下菜。跟熟人就随便玩，跟不熟的就用",
        "t": "看跟谁玩。熟人局就随便打打，不熟的人我可不会留手",
    },
}

# 新增选项（追加到该题末尾，保持 key 顺序 t, s）
ADD_OPTS = {
    ("bank1.json", "s04"): [
        {"t": "在家躺着打游戏，一天不出门，饭都懒得做",
         "s": {"drain": 1.57, "control": 0.5}},
    ],
    ("bank1.json", "h1c3"): [
        {"t": "不换。我就接着玩这个，新的再好也提不起兴趣",
         "s": {"grave": 1.3, "drain": 0.94}},
    ],
    ("bank3.json", "s36"): [
        {"t": "直接跟他说，「你的碗，你自己洗」",
         "s": {"aggro": 1.21, "removal": 0.79}},
    ],
    ("bank3.json", "s45"): [
        {"t": "笑着把话扎回去，让他当着人下不来台",
         "s": {"politics": 1.28, "chaos": 0.76}},
    ],
    ("bank4.json", "s50"): [
        {"t": "动画、番剧这类，认准的那几部一直追下去",
         "s": {"tribal": 1.62, "enchant": 1.4}},
    ],
    ("bank4.json", "s51"): [
        {"t": "有声书、播客这类，听的是内容不是音乐",
         "s": {"ramp": 1.69, "counters": 0.79}},
    ],
}

TARGET_FILES = ["bank1.json", "bank2.json", "bank3.json", "bank4.json", "bank5.json",
                "bankC.json", "bankE.json"]


def dump(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def main() -> int:
    dry = "--dry" in sys.argv

    # 1) 备份（只在备份不存在时写，保住最初的 before 快照）
    BAK.mkdir(parents=True, exist_ok=True)
    for name in TARGET_FILES:
        src = DATA / name
        dst = BAK / name
        if not dst.exists():
            shutil.copy2(src, dst)
            print(f"  备份 {name} -> {dst.relative_to(ROOT)}")
        else:
            print(f"  备份已存在，跳过 {name}")

    # 2) 应用改动（按文件聚合）
    by_file: dict[str, dict] = {}
    for (fname, qid), text in SET_Q.items():
        by_file.setdefault(fname, {}).setdefault(qid, {})["q"] = text
    for (fname, qid, idx), patch in SET_OPTS.items():
        by_file.setdefault(fname, {}).setdefault(qid, {}).setdefault("opts", {})[idx] = patch
    for (fname, qid), opts in ADD_OPTS.items():
        by_file.setdefault(fname, {}).setdefault(qid, {}).setdefault("add", []).extend(opts)

    changed_questions: list[str] = []
    for fname in sorted(by_file):
        path = DATA / fname
        obj = json.loads(path.read_text(encoding="utf-8"))
        index = {q["id"]: q for q in obj["questions"]}
        for qid, patch in by_file[fname].items():
            q = index[qid]
            notes = []

            if "q" in patch:
                if q["q"] != patch["q"]:
                    notes.append(f"题干：{q['q']}  ->  {patch['q']}")
                    if not dry:
                        q["q"] = patch["q"]
                else:
                    notes.append("题干已是新值")

            for idx, p in sorted(patch.get("opts", {}).items()):
                opt = q["opts"][idx]
                if opt["t"] != p["expect_t"]:
                    if opt["t"] == p["t"]:
                        notes.append(f"选项{idx}已是新值")
                        continue
                    print(f"✗ {fname} {qid} 选项{idx} 旧文本与预期不符：\n   实际 {opt['t']!r}\n   预期 {p['expect_t']!r}")
                    return 1
                if "expect_s" in p and opt["s"] != p["expect_s"]:
                    print(f"✗ {fname} {qid} 选项{idx} 旧轴与预期不符：{opt['s']} != {p['expect_s']}")
                    return 1
                notes.append(f"选项{idx} [{opt['t']}] -> [{p['t']}]"
                             + (f"  轴 {opt['s']} -> {p['s']}" if "s" in p else "  轴不变"))
                if not dry:
                    opt["t"] = p["t"]
                    if "s" in p:
                        # 重建 dict 以保持 t, s 的 key 顺序
                        rebuilt = {"t": opt["t"], "s": p["s"]}
                        for k, v in opt.items():
                            if k not in rebuilt:
                                rebuilt[k] = v
                        q["opts"][idx] = rebuilt

            for new_opt in patch.get("add", []):
                texts = [o["t"] for o in q["opts"]]
                if new_opt["t"] in texts:
                    notes.append(f"新增选项已存在：{new_opt['t']}")
                    continue
                notes.append(f"新增选项 [{new_opt['t']}]  轴 {new_opt['s']}  （{len(q['opts'])} -> {len(q['opts']) + 1}）")
                if not dry:
                    q["opts"].append({"t": new_opt["t"], "s": dict(new_opt["s"])})

            changed_questions.append(qid)
            print(f"\n● {fname} · {qid}")
            for n in notes:
                print(f"    {n}")

        if not dry:
            path.write_text(dump(obj), encoding="utf-8")

    print(f"\n{'（dry-run，未写入）' if dry else '✓ 已写入'}：{len(changed_questions)} 道题 -> "
          f"{', '.join(changed_questions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
