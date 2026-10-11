#!/usr/bin/env python3
"""给群头像底图配字，并导出「实际显示尺寸」预览。

群头像在聊天列表里大概 40~64px。**必须按那个尺寸验一次**——
不然做完在 1024px 下看着挺好，进群里就是一团糊。

所以除了 1024 成图，还导出 64px 与 40px 的预览（用 NEAREST 放大回来便于观察）。
"""
from __future__ import annotations

import pathlib
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont


# --- 路径相对本文件解析，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

AV = ROOT / "docs/group-avatar"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"
S = 1024
FIT = 0.78          # 微信/QQ 群头像会有圆角甚至圆形裁切，重要内容收进中心


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=0)


def compose(src: str, title: str, sub: str, tag: str,
            brighten: float = 1.0) -> Image.Image:
    im = Image.open(AV / src).convert("RGB")
    if brighten != 1.0:
        from PIL import ImageEnhance
        im = ImageEnhance.Brightness(im).enhance(brighten)
        im = ImageEnhance.Contrast(im).enhance(1.12)
    im = im.convert("RGBA")

    d = ImageDraw.Draw(im)
    # 主字：EDH。放画面下半，字号按宽度自适应
    f_big = font(FONT_BOLD, 210)
    while f_big.getlength(title) > S * 0.66 and f_big.size > 90:
        f_big = font(FONT_BOLD, f_big.size - 6)
    f_small = font(FONT_REG, 54)

    cx = S // 2
    y1 = int(S * 0.58)
    # 用实际字高来排下一行，别用估算的比例——否则「约战群」会压在 EDH 上
    bbox = d.textbbox((0, 0), title, font=f_big)
    y2 = y1 + (bbox[3] - bbox[1]) + 26

    # 底部压一条淡渐变，保证字清楚
    grad = Image.new("L", (S, S), 0)
    gp = grad.load()
    for y in range(int(S * 0.55), S):
        # 钳到 [0,1]：循环第一个像素的 t 会是极小的负数，
        # 而 Python 里负数的 1.5 次方返回复数
        t = max(0.0, (y - S * 0.55) / (S - S * 0.55))
        v = int(150 * (t ** 1.5))
        for x in range(S):
            gp[x, y] = v
    im = Image.composite(Image.new("RGB", (S, S), (6, 10, 22)).convert("RGBA"),
                         im, grad)

    d = ImageDraw.Draw(im)
    # 柔光
    gl = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    gd = ImageDraw.Draw(gl)
    gd.text((cx, y1), title, font=f_big, fill=(120, 190, 255, 170), anchor="ma")
    gd.text((cx, y2), sub, font=f_small, fill=(255, 200, 90, 140), anchor="ma")
    im = Image.alpha_composite(im, gl.filter(ImageFilter.GaussianBlur(12)))

    d = ImageDraw.Draw(im)
    d.text((cx, y1), title, font=f_big, fill=(255, 255, 255), anchor="ma",
           stroke_width=max(6, f_big.size // 22), stroke_fill=(6, 10, 22))
    d.text((cx, y2), sub, font=f_small, fill=(255, 216, 120), anchor="ma",
           stroke_width=5, stroke_fill=(6, 10, 22))

    out = im.convert("RGB")
    out.save(AV / f"avatar_{tag}.png")
    # 实际尺寸预览
    for px in (64, 40):
        small = out.resize((px, px), Image.LANCZOS)
        small.resize((px * 6, px * 6), Image.NEAREST).save(
            AV / f"_preview{px}_{tag}.png")
    print(f"  ✓ avatar_{tag}.png   （预览 64px / 40px 已导出）")
    return out


compose("b_silh_00001_.png", "EDH", "约 战 群", "silh", brighten=1.35)
compose("c_table_00001_.png", "EDH", "约 战 群", "ring", brighten=1.15)
print("\n完成。")
