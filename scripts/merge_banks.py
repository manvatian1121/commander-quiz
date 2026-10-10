#!/usr/bin/env python3
"""把 5 个题库存并成 questions.json，并计算快速版题序。"""
from __future__ import annotations

import json
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

SECTIONS = [
    {"id": "exp", "name": "先了解一下你", "intro": "这题只用来决定后面给你出什么题、按什么标准挑主将。"},
    {"id": "life", "name": "日常节奏", "intro": "先从你每天怎么过说起。"},
    {"id": "decide", "name": "决策与风险", "intro": "你是怎么做决定的。"},
    {"id": "social", "name": "与人相处", "intro": "牌桌之外，你也是个社会人。"},
    {"id": "taste", "name": "审美与兴趣", "intro": "喜欢什么，往往比擅长什么更重要。"},
    {"id": "mind", "name": "输赢与心态", "intro": "赢了输了，你都是什么反应。"},
    {"id": "money", "name": "金钱与投入", "intro": "爱好是要花钱的，你怎么看。"},
    {"id": "pick", "name": "最后几个多选题", "intro": "这组可以多选，凭直觉挑。"},
]

QUICK_STEP = 6      # 快速版每隔几道主线题抽一道
HUB_KINDS = {"hub", "gate"}


def main() -> int:
    questions: list[dict] = []
    seen: dict[str, str] = {}
    problems: list[str] = []

    for index in range(1, 6):
        path = DATA / f"bank{index}.json"
        if not path.exists():
            problems.append(f"缺少 {path.name}")
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        batch = payload.get("questions") or []
        for q in batch:
            qid = q.get("id")
            if not qid:
                problems.append(f"bank{index} 有一道题缺 id")
                continue
            if qid in seen:
                problems.append(f"id 重复：{qid}（bank{index} 与 {seen[qid]}）")
                continue
            seen[qid] = f"bank{index}"
            questions.append(q)
        print(f"  bank{index}: {len(batch)} 题")

    # 约束题（主 agent 补写），插在多选题之前
    cpath = DATA / "bankC.json"
    if cpath.exists():
        cq = json.loads(cpath.read_text(encoding="utf-8"))["questions"]
        questions.extend(cq)
        print(f"  bankC: {len(cq)} 题（约束题）")

    # 经验门槛题（主 agent 补写），是全测试的入口
    epath = DATA / "bankE.json"
    if epath.exists():
        eq = json.loads(epath.read_text(encoding="utf-8"))["questions"]
        for q in eq:
            if q["id"] in seen:
                problems.append(f"id 重复：{q['id']}（bankE 与 {seen[q['id']]}）")
                continue
            seen[q["id"]] = "bankE"
            questions.append(q)
        print(f"  bankE: {len(eq)} 题（经验门槛 + 分支）")

    if problems:
        print("\n✗ 合并前发现问题：")
        for item in problems:
            print(f"  - {item}")
        return 1

    by_id = {q["id"]: q for q in questions}
    start = "e0"
    if start not in by_id:
        print(f"✗ 找不到起始题 {start}")
        return 1

    # 把约束题链接进主线：s74 → c01 → ... → c06 → s75
    if "c01" in by_id and "s74" in by_id and "s75" in by_id:
        by_id["s74"]["next"] = "c01"
        print("  ✓ 约束题已插入 s74 与 s75 之间")
    else:
        print("  ⚠ 未能插入约束题（缺 s74 / s75 / c01 之一）")

    # 主线顺序：从起点沿 next 走（忽略 goto）
    spine: list[str] = []
    cursor = start
    guard = 0
    while cursor and guard < 600:
        spine.append(cursor)
        node = by_id.get(cursor)
        if not node:
            break
        cursor = node.get("next")
        guard += 1

    # 输出顺序：主线顺序，分支题紧跟在其枢纽之后（便于阅读与文档生成）
    ordered: list[dict] = []
    emitted: set[str] = set()

    def emit(qid: str) -> None:
        if qid in emitted or qid not in by_id:
            return
        node = by_id[qid]
        ordered.append(node)
        emitted.add(qid)
        if node.get("kind") in HUB_KINDS:
            for opt in node["opts"]:
                branch = opt.get("goto")
                walk = branch
                g2 = 0
                while walk and g2 < 20:
                    emit(walk)
                    walk = by_id[walk].get("next")
                    g2 += 1
                    if walk and walk in spine:
                        break

    for sid in spine:
        emit(sid)
    # 兜底：把任何还没输出的题补上
    for q in questions:
        emit(q["id"])

    # 快速版：每隔 QUICK_STEP 抽一道主线题，加上全部枢纽与全部多选题
    hubs = [q["id"] for q in ordered if q.get("kind") in HUB_KINDS]
    multis = [q["id"] for q in ordered if q.get("multi")]
    quick = sorted(
        {spine[i] for i in range(0, len(spine), QUICK_STEP)} | set(hubs) | set(multis),
        key=lambda qid: (spine.index(qid) if qid in spine else 9999))

    payload = {
        "meta": {
            "title": "你是哪种指挥官？— EDH 新人主将挑选测试",
            "version": "2.0",
            "note": "生活化性格题 + 分支衍生题。s=玩法轴得分，cval=约束档位，col=颜色倾向。",
            "bank_size": len(ordered),
            "spine_size": len(spine),
            "hub_count": len(hubs),
            "multi_count": len(multis),
        },
        "start": start,
        "spine": spine,
        "quick": quick,
        "sections": SECTIONS,
        "questions": ordered,
    }
    (DATA / "questions.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✓ 合并 {len(ordered)} 题（主线 {len(spine)}，枢纽 {len(hubs)}，多选 {len(multis)}）")
    print(f"  快速版 {len(quick)} 道主线题")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
