#!/usr/bin/env python3
"""用 NoobAI 出封面底图——按封面要求来，不是按「好看的插画」来。

封面要求（和普通插画的区别）：
  ① 16:9 横构图，主体在左、右侧留白放字
  ② 大色块、强对比 —— 缩到信息流里还要看得清
  ③ 焦点明确、背景别抢戏 —— 上一版就败在「细节太密，缩图糊成一片」
  ④ 不要文字/水印

NoobAI 的负向提示词是真生效的，所以「压细节」这件事正好靠它来做。
"""
from __future__ import annotations

import pathlib
import subprocess
import sys


# --- 路径相对本文件解析，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

OUT = ROOT / "docs/thumbnails"
GEN = pathlib.Path(r"D:\test01\sdxl_gen.py")
CKPT = "NoobAI-XL-v1.1.safetensors"

# 负向：压细节、压亮度、压水印。NoobAI 下这些真的起作用。
NEG = (
    "cluttered, busy background, too many details, small details, intricate patterns, "
    "stained glass, ornate architecture, crowd, multiple views, text, watermark, "
    "signature, username, artist name, logo, low contrast, washed out, blurry, "
    "jpeg artifacts, worst quality, low quality, bad anatomy, bad hands, "
    "extra fingers, cropped, out of frame"
)

PROMPTS = {
    "v1_wall": (
        "masterpiece, best quality, anime key visual, official art, 1girl, solo, "
        "female mage in dark blue hooded cloak, back view, standing on the left side "
        "of the frame, facing a large wall of big glowing cards, "
        "simple clean composition, big color blocks, strong silhouette, "
        "dramatic rim lighting, deep blue and gold color scheme, "
        "wide empty dark space on the right side, cinematic wide shot, "
        "shallow depth of field, minimal background detail, poster composition, "
        "high contrast, cel shading"
    ),
    "v2_card": (
        "masterpiece, best quality, anime key visual, poster art, 1girl, solo, "
        "hooded mage silhouette seen from behind, standing on the left side of the frame, "
        "one giant glowing card floating in front of her, huge card filling the right side, "
        "simple graphic composition, bold flat shapes, deep dark blue background, "
        "golden rim light, negative space, cel shading, high contrast, "
        "minimal detail, vector art feel"
    ),
    "v3_orbs": (
        "masterpiece, best quality, anime key visual, poster art, 1girl, solo, "
        "hooded mage seen from behind on the left side of the frame, "
        "five large glowing orbs floating in an arc on the right, "
        "white blue black red green orbs, simple clean composition, bold shapes, "
        "deep dark background, negative space, cel shading, high contrast, "
        "poster art, minimal background detail, particle glow"
    ),
    "v4_dof": (
        "masterpiece, best quality, anime key visual, 1girl, solo, "
        "hooded mage back view occupying the left third of the frame, "
        "a softly glowing wall of cards far in the background, heavily blurred background, "
        "strong bokeh, shallow depth of field, simple composition, dark blue tones, "
        "golden glow, large negative space on the right, high contrast, cel shading, "
        "clean flat shading, poster"
    ),
}

for name, prompt in PROMPTS.items():
    print(f"--- {name} ---", flush=True)
    cmd = [
        sys.executable, str(GEN),
        "--ckpt", CKPT, "--unet", "none",
        "--prompt", prompt, "--negative", NEG,
        "--width", "1536", "--height", "864",
        "--steps", "28", "--cfg", "5.0",
        "--sampler", "dpmpp_2m", "--scheduler", "karras",
        "--seed", "777",
        "--prefix", name, "-o", str(OUT), "--timeout", "900",
    ]
    r = subprocess.run(cmd, cwd=str(GEN.parent), capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    tail = [ln for ln in (r.stdout or "").split("\n") if ln.strip()]
    print("   " + (tail[-1] if tail else "(无输出)"))
    if r.returncode != 0:
        err = [ln for ln in (r.stderr or "").split("\n") if "Error" in ln or "error" in ln]
        for ln in err[:2]:
            print("   ! " + ln.strip())

print("\n完成。")
