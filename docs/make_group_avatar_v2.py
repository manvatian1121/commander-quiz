#!/usr/bin/env python3
"""群头像第二版：按实际显示尺寸重做。

第一版在 1024px 下看着挺好，缩到 64px/40px 一看：
  「EDH」读得清 ✓
  「约战群」完全糊成一团 ✗

结论：群头像只装得下一个信息。删掉副标题，让 EDH 当主角，
剪影退成背景。
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
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"
S = 1024


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=0)


def build(src: str, tag: str, title: str = "EDH",
          dim_bg: float = 0.55, brighten: float = 1.3) -> None:
    im = Image.open(AV / src).convert("RGB")
    im = ImageEnhance.Brightness(im).enhance(brighten)
    im = ImageEnhance.Contrast(im).enhance(1.15)
    # 剪影退成背景：整体压暗，让前景的字跳出来
    im = ImageEnhance.Brightness(im).enhance(dim_bg).convert("RGBA")

    # 中央压暗一圈，给字让位
    vig = Image.new("L", (S, S), 0)
    vp = vig.load()
    cx0, cy0, r = S / 2, S / 2, S * 0.42
    for y in range(S):
        dy = (y - cy0) / r
        for x in range(S):
            dx = (x - cx0) / r
            d = (dx * dx + dy * dy) ** 0.5
            vp[x, y] = int(120 * max(0.0, min(1.0, 1.15 - d)))
    im = Image.composite(Image.new("RGB", (S, S), (5, 8, 18)).convert("RGBA"),
                         im, vig)

    # 字尽量大：占满宽度 78%
    f = font(FONT_BOLD, 420)
    while f.getlength(title) > S * 0.78 and f.size > 120:
        f = font(FONT_BOLD, f.size - 8)

    d = ImageDraw.Draw(im)
    bbox = d.textbbox((0, 0), title, font=f)
    ty = int(S / 2 - (bbox[3] - bbox[1]) / 2 - bbox[1])
    sw = max(8, f.size // 20)

    gl = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(gl).text((S // 2, ty), title, font=f,
                            fill=(120, 190, 255, 180), anchor="ma")
    im = Image.alpha_composite(im, gl.filter(ImageFilter.GaussianBlur(16)))

    d = ImageDraw.Draw(im)
    d.text((S // 2, ty), title, font=f, fill=(255, 255, 255), anchor="ma",
           stroke_width=sw, stroke_fill=(6, 10, 22))

    out = im.convert("RGB")
    out.save(AV / f"avatar_{tag}.png")
    for px in (96, 64, 40):
        out.resize((px, px), Image.LANCZOS).resize(
            (px * 5, px * 5), Image.NEAREST).save(AV / f"_preview{px}_{tag}.png")
    print(f"  ✓ avatar_{tag}.png  「{title}」{f.size}px")
    # 拼尺寸对比
    parts = [(out.resize((380, 380), Image.LANCZOS), 380)]
    for px in (96, 64, 40):
        parts.append((Image.open(AV / f"_preview{px}_{tag}.png")
                      .resize((int(px * 5 * 380 / (96 * 5)), int(px * 5 * 380 / (96 * 5)))),
                      int(px * 5 * 380 / (96 * 5))))
    W = 380 + sum(p[1] for p in parts[1:]) + 30 * len(parts)
    canvas = Image.new("RGB", (W, 420), (22, 26, 34))
    x = 0
    for img, w in parts:
        canvas.paste(img, (x, (420 - img.size[1]) // 2))
        x += w + 30
    canvas.save(AV / f"_compare_{tag}.png")


build("b_silh_00001_.png", "silh")
build("c_table_00001_.png", "ring", brighten=1.25)
print("完成。")
