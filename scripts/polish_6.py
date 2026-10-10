# -*- coding: utf-8 -*-
"""最后三处措辞微调（保持字数区间）。"""
import pathlib
import sys



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
P = pathlib.Path(SCRIPT_DIR / "draft_descriptions_6.py")
text = P.read_text(encoding="utf-8")

PAIRS = [
    ("谁有几个生物这回合没攻击，他就掉几点血。", "谁有几个生物这回合没攻击，谁就掉几点血。"),
    ("手牌永远比对手厚", "手牌就比别人厚"),
    ("这回合只要有人掉过血，你之后进场的每个生物", "这回合只要有对手掉过血，你之后进场的每个生物"),
]
for old, new in PAIRS:
    if text.count(old) != 1:
        print("✗ 匹配异常：", old[:24])
        raise SystemExit(1)
    text = text.replace(old, new)
P.write_text(text, encoding="utf-8")
print("✓ 措辞微调完成")
