# -*- coding: utf-8 -*-
"""把 _draft_8.py 的 {English Name} 占位替换成「中文名（English Name）」并落盘 descriptions_8.json。

用法：
    python build_descriptions_8.py            # 干跑：只报字数
    python build_descriptions_8.py --write    # 写出 descriptions_8.json
中文名来源：data/card_zh.json（单卡）；主将本人若不在其中，用素材标题里的官方中文名。
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))

from _draft_8 import CONTENT  # noqa: E402

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

DATA = pathlib.Path(ROOT / "data")
IDX = json.loads(pathlib.Path(
    SCRIPT_DIR / "_material_index_8.json").read_text(encoding="utf-8"))
card_zh = json.loads((DATA / "card_zh.json").read_text(encoding="utf-8"))

T_MIN, T_MAX = 0, 20
I_MIN, I_MAX = 70, 120
B_MIN, B_MAX = 110, 170

PLACEHOLDER = re.compile(r"\{([^{}]+)\}")


def count(s: str) -> int:
    return sum(1 for ch in s if not ch.isspace())


def zh_of(name: str, commander: str) -> str | None:
    if name == commander:
        return IDX[commander]["zh"] or IDX[commander]["zh_material"]
    return card_zh.get(name)


def main() -> int:
    write = "--write" in sys.argv
    problems = []
    out = {}
    rows = []

    for commander, entry in IDX.items():
        if commander not in CONTENT:
            problems.append(f"草稿缺失：{commander}")
            continue
        own = set(entry["cards"]) | {commander}
        built = {}
        for field in ("tagline", "intro", "build"):
            raw = CONTENT[commander][field]

            def sub(m):
                name = m.group(1)
                if name not in own:
                    problems.append(f"{commander} / {field}：占位符不在本人清单内 → {name}")
                    return name
                zh = zh_of(name, commander)
                return f"{zh}（{name}）" if zh else f"{name}"

            built[field] = PLACEHOLDER.sub(sub, raw)
            if "{" in built[field] or "}" in built[field]:
                problems.append(f"{commander} / {field}：有未替换的括号")
        out[commander] = built

        t, i, b = (count(built[f]) for f in ("tagline", "intro", "build"))
        flags = []
        if t > T_MAX:
            flags.append(f"T超{t - T_MAX}")
        if not (I_MIN <= i <= I_MAX):
            flags.append(f"I{i - (I_MAX if i > I_MAX else I_MIN):+d}")
        if not (B_MIN <= b <= B_MAX):
            flags.append(f"B{b - (B_MAX if b > B_MAX else B_MIN):+d}")
        rows.append((commander, t, i, b, ",".join(flags)))

    print(f"{'主将':<36}{'T':>4}{'I':>5}{'B':>5}  问题")
    for c, t, i, b, f in rows:
        print(f"{c:<36}{t:>4}{i:>5}{b:>5}  {f}")

    extra = [k for k in CONTENT if k not in IDX]
    if extra:
        problems.append(f"草稿里有多余主将：{extra}")

    print(f"\n条目 {len(out)}")
    print("结构问题：", problems if problems else "无")

    if write:
        if problems:
            print("✗ 有问题，未写出")
            return 1
        (DATA / "descriptions_8.json").write_text(
            json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✓ 已写出 {DATA / 'descriptions_8.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
