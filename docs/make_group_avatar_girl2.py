#!/usr/bin/env python3
"""二次元美少女群头像：排版 + 实际尺寸验证。

和美少女构图搭配的两个新问题：
  ① 脸占满画面了，「EDH」往哪放？底部压条会切到下巴，顶部会切到头发
  ② **群名本身就写着 EDH**，头像未必要重复这个信息

所以做两版：带字 / 不带字，都按 40px 验一遍再决定。
"""
from __future__ import annotations

import pathlib
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


# --- 路径相对本文件解析，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

AV = ROOT / "docs/group-avatar"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
S = 1024


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=0)


def build(src: str, tag: str, with_text: bool) -> Image.Image:
    im = Image.open(AV / src).convert("RGB")
    im = ImageEnhance.Contrast(im).enhance(1.08)
    # 稍微提高一点饱和，缩小后颜色才不会发灰
    im = ImageEnhance.Color(im).enhance(1.12).convert("RGBA")

    if with_text:
        # 底部压一条窄渐变，只在最下面留一条放字——不碰脸
        grad = Image.new("L", (S, S), 0)
        gp = grad.load()
        y0 = int(S * 0.76)
        for y in range(y0, S):
            t = max(0.0, (y - y0) / (S - y0))
            v = int(215 * (t ** 1.2))
            for x in range(S):
                gp[x, y] = v
        im = Image.composite(Image.new("RGB", (S, S), (5, 8, 18)).convert("RGBA"),
                             im, grad)

        f = font(FONT_BOLD, 168)
        while f.getlength("EDH") > S * 0.60 and f.size > 80:
            f = font(FONT_BOLD, f.size - 6)
        d0 = ImageDraw.Draw(im)
        bb = d0.textbbox((0, 0), "EDH", font=f)
        ty = S - int(S * 0.09) - (bb[3] - bb[1])

        gl = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        ImageDraw.Draw(gl).text((S // 2, ty), "EDH", font=f,
                                fill=(120, 190, 255, 175), anchor="ma")
        im = Image.alpha_composite(im, gl.filter(ImageFilter.GaussianBlur(14)))

        d = ImageDraw.Draw(im)
        d.text((S // 2, ty), "EDH", font=f, fill=(255, 255, 255), anchor="ma",
               stroke_width=max(6, f.size // 20), stroke_fill=(6, 10, 22))

    out = im.convert("RGB")
    suffix = "" if with_text else "_notext"
    out.save(AV / f"girl_{tag}{suffix}.png")
    for px in (96, 64, 40):
        out.resize((px, px), Image.LANCZOS).resize(
            (px * 5, px * 5), Image.NEAREST).save(
            AV / f"_gpreview{px}_{tag}{suffix}.png")
    print(f"  ✓ girl_{tag}{suffix}.png")
    return out


def compare(tag: str) -> None:
    big = Image.open(AV / f"girl_{tag}.png").resize((400, 400), Image.LANCZOS)
    nt = Image.open(AV / f"girl_{tag}_notext.png").resize((400, 400), Image.LANCZOS)
    items = [big, nt] + [Image.open(AV / f"_gpreview{px}_{tag}.png")
                         .resize((px * 4, px * 4), Image.LANCZOS)
                         for px in (96, 64, 40)]
    labels = ["1024 带字", "1024 无字", "96px", "64px", "40px"]
    W = sum(i.size[0] for i in items) + 24 * (len(items) + 1)
    canvas = Image.new("RGB", (W, 440), (22, 26, 34))
    dc = ImageDraw.Draw(canvas)
    fnt = font(r"C:\Windows\Fonts\msyh.ttc", 18)
    x = 24
    for img, lab in zip(items, labels):
        canvas.paste(img, (x, 20))
        dc.text((x + img.size[0] // 2, 25 + img.size[1]), lab,
                font=fnt, fill=(170, 185, 205), anchor="ma")
        x += img.size[0] + 24
    canvas.save(AV / f"_gcompare_{tag}.png")


for src, tag in (("m1_card_00001_.png", "mage"), ("m2_crown_00001_.png", "crown")):
    build(src, tag, with_text=True)
    build(src, tag, with_text=False)
    compare(tag)
print("完成。")
