#!/usr/bin/env python3
"""确认校对修正都进了成品 HTML，且旧文案已消失。"""
from __future__ import annotations

import json
import pathlib
import re
import sys

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(ROOT)
html = (ROOT / "commander_quiz.html").read_text(encoding="utf-8")
md = (ROOT / "commander_quiz.md").read_text(encoding="utf-8")

MUST_APPEAR = [
    ("s18 搬家时间表", "先把整套流程排成时间表"),
    ("s58 量词", "要买一件每天都要用的东西"),
    ("s58 量词", "直接上贵的那个"),
    ("h5a1 热身", "先热热身"),
    ("s66 今天", "认了，今天就是不站我这边"),
    ("h5a2 成了就收手", "成了就收手"),
    ("s75 删没看", "把攒着的旧东西翻出来重看一遍"),
    ("h4b2 太贵", "太贵就是没缘分"),
    ("c06 哪个角色", "最想当哪个角色"),
    ("e0 指挥官", "只是想换个指挥官玩玩"),
    ("s25 一样点一份", "干脆一样点一份摆一桌"),
    ("s42 办法", "琢磨个办法把两边的量都记下来"),
    ("h3b1 他们", "找工作人员，让他们去管"),
    ("h1a2 说早半小时", "下次约他我把时间说早半小时"),
    ("s29 最后一天", "拖到最后一天再一口气弄完"),
]

MUST_NOT_APPEAR = [
    ("旧 s18", "把全家的时间表排出来"),
    ("旧 s58", "要买一把每天都要用的东西"),
    ("旧 s58", "直接上贵的那把"),
    ("旧 h5a1", "先把状态练热"),
    ("旧 s66", "认了，这天就是不站我这边"),
    ("旧 h5a2", "成就收手"),
    ("旧 s75", "攒着没看的旧东西翻出来重看"),
    ("旧 h4b2", "买不到就是没缘分"),
    ("旧 c06", "最想当那个什么角色"),
    ("旧 e0", "只想换个主将玩玩"),
    ("旧 s25", "干脆一人点一份摆一桌"),
    ("旧 s42", "琢磨个用法把两边的量都记下来"),
    ("旧 h3b1", "让工作人员去管"),
    ("旧 h1a2", "下次约他我提前半小时说"),
    ("旧 s29", "隔几天翻出来弄两下"),
]

fail = 0
print("=== 应出现 ===")
for label, text in MUST_APPEAR:
    ok_html, ok_md = text in html, text in md
    flag = "✓" if (ok_html and ok_md) else "✗"
    if flag == "✗":
        fail += 1
    print(f"  {flag} {label:<16} HTML={ok_html} MD={ok_md}")

print("\n=== 应已消失 ===")
for label, text in MUST_NOT_APPEAR:
    gone_html, gone_md = text not in html, text not in md
    flag = "✓" if (gone_html and gone_md) else "✗"
    if flag == "✗":
        fail += 1
    print(f"  {flag} {label:<16} HTML={gone_html} MD={gone_md}")

print("\n" + "=" * 60)
print("✓ 全部校对修正已进入成品" if not fail else f"✗ {fail} 项不符")
sys.exit(1 if fail else 0)
