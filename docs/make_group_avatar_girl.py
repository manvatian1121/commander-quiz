#!/usr/bin/env python3
"""群头像：二次元美少女 + EDH 指挥官元素。

构图约束（这是关键）：
  群头像在聊天列表里只有 40~64px。
  **全身像 / 半身像在那个尺寸下会糊成一团** —— 脸必须占画面大部分。
  所以统一按「头像式构图」出：胸像以上、正面、居中、背景干净。

EDH 指挥官元素靠这几样传达：手里的卡牌、头顶的皇冠、身后的法阵、
环绕的卡牌框（像光环一样）。
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

NEG = (
    "full body, wide shot, distant, small face, busy background, detailed background, "
    "many objects, text, letters, watermark, signature, username, logo, frame, border, "
    "low contrast, blurry, worst quality, low quality, bad anatomy, bad hands, "
    "extra fingers, jpeg artifacts, multiple views, collage, cropped head"
)

QUALITY = "masterpiece, best quality, score_7, safe, 1girl, solo, "
ICON = ("anime portrait icon, upper body, facing viewer, perfectly centered composition, "
        "deep dark background, strong rim lighting, cel shading, clean, high contrast, "
        "sharp focus on face")

PROMPTS = {
    # ① 手持卡牌的主将
    "m1_card": QUALITY + (
        "cute confident smile, long dark blue hair, violet eyes, "
        "wearing a dark blue hooded mage coat with gold trim, "
        "holding up one glowing golden trading card in front of her chest, "
        "magical sparkles, " + ICON
    ),
    # ② 戴上主将皇冠
    "m2_crown": QUALITY + (
        "confident smirk, short silver hair, red eyes, "
        "wearing a small golden crown, dark regal cloak with gold embroidery, "
        "one glowing card floating beside her face, "
        "dramatic golden rim light, " + ICON
    ),
    # ③ 身后法阵 + 环绕卡牌
    "m3_circle": QUALITY + (
        "calm gentle smile, long purple hair, green eyes, "
        "dark mage outfit with silver trim, "
        "a large glowing golden magic circle behind her, "
        "three glowing trading cards floating around her, "
        "magical particles, " + ICON
    ),
    # ④ 卡牌光环（最图形化，40px 下最吃得开）
    "m4_halo": QUALITY + (
        "big expressive amber eyes, short black hair with blue highlights, "
        "mysterious small smile, dark high collar coat, "
        "four glowing card frames arranged around her head like a halo, "
        "flat graphic composition, bold shapes, " + ICON
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
        "--seed", "777",
        "--prefix", name, "-o", str(OUT), "--timeout", "900",
    ]
    r = subprocess.run(cmd, cwd=str(GEN.parent), capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    tail = [ln for ln in (r.stdout or "").split("\n") if ln.strip()]
    print("   " + (tail[-1] if tail else "(无输出)"))

print("\n完成。")
