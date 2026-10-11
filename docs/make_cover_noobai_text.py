#!/usr/bin/env python3
"""给 NoobAI 出的居中构图封面底图配字。

和 Anima 那张不同：这几张主体在正中，右侧没有大片留白，
所以排版改成「底部压一条暗带 + 左下角大字」。

底图暗部本来就在下方，压一条渐变只加深一点点，
不会像上次那样把整张图压平。
"""
from __future__ import annotations

import pathlib
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont


# --- 路径相对本文件解析，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

OUT = ROOT / "docs/thumbnails"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"
W, H = 1536, 864


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=0)


def bottom_band(img: Image.Image, strength: int = 190,
                start: float = 0.52) -> Image.Image:
    """底部向上渐隐的暗带，只压暗下方约一半，给文字一个稳定的底。"""
    mask = Image.new("L", (W, H), 0)
    px = mask.load()
    y0 = int(H * start)
    for y in range(y0, H):
        t = (y - y0) / max(1, H - y0)
        v = int(strength * (t ** 0.8))
        for x in range(W):
            px[x, y] = v
    dark = Image.new("RGB", (W, H), (4, 7, 14))
    return Image.composite(dark, img, mask)


def compose(src_name: str, line1: str, line2: str) -> None:
    src = OUT / src_name
    img = bottom_band(Image.open(src).convert("RGB")).convert("RGBA")

    big = font(FONT_BOLD, 118)
    mid = font(FONT_BOLD, 54)
    small = font(FONT_REG, 28)

    L1 = (86, 492)
    L2 = (90, 636)
    foot = (88, 800)

    def paint(d: ImageDraw.ImageDraw, l1c, l2c) -> None:
        d.text(L1, line1, font=big, fill=l1c, anchor="la")
        d.text(L2, line2, font=mid, fill=l2c, anchor="la")

    # 柔光垫底
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    paint(ImageDraw.Draw(glow), (130, 200, 255, 160), (255, 200, 90, 130))
    img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(10)))

    d = ImageDraw.Draw(img)
    paint(d, (255, 255, 255), (255, 214, 110))
    d.text(L1, line1, font=big, fill=None)          # 占位，保持层序清晰
    d.text(foot, "manvatian1121.github.io/commander-quiz",
           font=small, fill=(158, 178, 204), anchor="la",
           stroke_width=3, stroke_fill=(4, 7, 14))
    d.text((92, 726), "EDH 指挥官性格测试", font=font(FONT_REG, 30),
           fill=(200, 216, 240), anchor="la", stroke_width=4, stroke_fill=(4, 7, 14))

    # 重画一遍主体字，压在发光层之上并加粗描边
    paint(d, (255, 255, 255), (255, 214, 110))
    for xy, txt, f, col, sw in (
        (L1, line1, big, (255, 255, 255), 9),
        (L2, line2, mid, (255, 214, 110), 7),
    ):
        d.text(xy, txt, font=f, fill=col, anchor="la",
               stroke_width=sw, stroke_fill=(6, 10, 20))

    out = img.convert("RGB")
    tag = src_name.split("_")[0]
    p1 = OUT / f"final_{tag}.png"
    out.save(p1, quality=95)
    crop_w = int(H * 1146 / 717)
    left = (W - crop_w) // 2
    out.crop((left, 0, left + crop_w, H)).save(
        OUT / f"final_{tag}_bili1146x717.png", quality=95)
    print(f"  ✓ {p1.name}")


compose("v4_dof_00001_.png", "506 位主将", "145 道题，测出你该玩哪个")
compose("v1_wall_00001_.png", "506 位主将", "145 道题，测出你该玩哪个")
print("完成。")
