#!/usr/bin/env python3
"""线上 EDH 约战群的头像底图。

和视频封面完全不同的要求：
  ① 群头像在聊天列表里只有 40~60px —— 必须极简，一个主体、大色块、高对比
  ② 方形构图、主体居中（微信/QQ 会做圆角裁切，边上不能放东西）
  ③ 不用生成文字 —— 模型渲染文字很差，文字后面用 PIL 加

四个方向：具象（围桌）/ 象征（四牌环绕）/ 人物（主将剪影）/ 符号（骰子）
"""
from __future__ import annotations

import pathlib
import subprocess
import sys


# --- 路径相对本文件解析，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

OUT = ROOT / "docs/group-avatar"
OUT.mkdir(parents=True, exist_ok=True)
GEN = pathlib.Path(r"D:\test01\sdxl_gen.py")
CKPT = "NoobAI-XL-v1.1.safetensors"

# 群头像要的是「图标」不是「插画」，所以负向里重点压细节和背景
NEG = (
    "cluttered, busy, detailed background, many objects, text, letters, watermark, "
    "signature, username, logo, frame, border, low contrast, blurry, "
    "worst quality, low quality, jpeg artifacts, cropped, out of frame, "
    "multiple views, collage"
)

PROMPTS = {
    # ① 抽象象征：四张卡牌围成一圈，中心发光
    "a_ring": (
        "masterpiece, best quality, anime icon, simple flat illustration, "
        "four glowing trading cards arranged in a circle facing inward, "
        "bright golden light in the center, deep dark blue background, "
        "perfectly centered composition, bold flat shapes, strong glow, "
        "high contrast, cel shading, clean vector icon, minimal detail"
    ),
    # ② 人物：兜帽主将剪影居中，四色光点环绕
    "b_silh": (
        "masterpiece, best quality, anime icon, simple flat illustration, "
        "hooded mage silhouette centered, glowing staff, "
        "four small colored light orbs floating around the figure, "
        "deep dark blue background, strong rim light, "
        "perfectly centered composition, bold shapes, high contrast, "
        "cel shading, clean vector icon, minimal detail"
    ),
    # ③ 具象：俯视四个人围桌（EDH 是四人赛制）
    "c_table": (
        "masterpiece, best quality, anime icon, simple flat illustration, "
        "top down view of a round table with four hands holding cards, "
        "four players, four glowing cards, warm light from above, "
        "deep dark background, perfectly centered composition, "
        "bold flat shapes, high contrast, cel shading, vector icon, minimal detail"
    ),
    # ④ 符号：一颗发光的骰子 + 两张卡牌（约战 = 随手开一局）
    "d_dice": (
        "masterpiece, best quality, anime icon, simple flat illustration, "
        "a single large glowing golden twenty sided die centered, "
        "two trading cards crossing behind it, "
        "deep dark blue background, strong rim light, "
        "perfectly centered composition, bold flat shapes, high contrast, "
        "cel shading, clean vector icon, minimal detail"
    ),
}

for name, prompt in PROMPTS.items():
    print(f"--- {name} ---", flush=True)
    cmd = [
        sys.executable, str(GEN),
        "--ckpt", CKPT, "--unet", "none",
        "--prompt", prompt, "--negative", NEG,
        "--width", "1024", "--height", "1024",
        "--steps", "28", "--cfg", "5.0",
        "--sampler", "dpmpp_2m", "--scheduler", "karras",
        "--seed", "2024",
        "--prefix", name, "-o", str(OUT), "--timeout", "900",
    ]
    r = subprocess.run(cmd, cwd=str(GEN.parent), capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    tail = [ln for ln in (r.stdout or "").split("\n") if ln.strip()]
    print("   " + (tail[-1] if tail else "(无输出)"))

print("\n完成。")
