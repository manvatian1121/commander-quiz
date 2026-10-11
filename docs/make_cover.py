#!/usr/bin/env python3
"""给封面底图配文字。

底图：兜帽法师 + 一整面发光卡牌墙（1536×864）。
问题：右三分之二都是亮而密的卡牌墙，直接把字压上去会糊。

做法：
  ① 在右侧叠一层水平渐变暗底，压住卡牌墙的亮度（不遮死，还看得见墙）
  ② 大字用微软雅黑 Bold + 粗描边，保证压在光点上也能读
  ③ 再叠一层柔和投影，让字从背景里"浮"起来

尺寸注意：B 站封面是 1146×717（约 1.6:1），本图是 1.78:1，
裁到 1.6:1 会从左右各切掉约 78px，所以文字全部放在 x∈[420,1450] 的安全区里。
"""
from __future__ import annotations

import pathlib
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.stdout.reconfigure(encoding="utf-8")

import os
SRC = pathlib.Path(os.environ.get("COVER_SRC") or (pathlib.Path(__file__).parent / "thumbnails" / "thumb1_00001_.png"))
SUFFIX = os.environ.get("COVER_SUFFIX") or ""
OUT = SRC.parent
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"

W, H = 1536, 864


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=0)


def gradient_panel(base: Image.Image, strength: int = 205,
                   start: float = 0.22) -> Image.Image:
    """从左侧透明到右侧半透明黑的水平渐变，压住卡牌墙的亮度。"""
    panel = Image.new("L", (W, H), 0)
    px = panel.load()
    x0 = int(W * start)
    for x in range(x0, W):
        # 前 40% 快速加深，之后平缓，避免出现一条硬边
        t = (x - x0) / max(1, W - x0)
        v = int(strength * (t ** 0.55))
        for y in range(H):
            px[x, y] = v
    dark = Image.new("RGB", (W, H), (6, 10, 20))
    return Image.composite(dark, base, panel)


def glow_layer(size: tuple[int, int], draw_fn) -> Image.Image:
    """先在一张透明图上画字，模糊后当柔光垫在下面。"""
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(layer))
    return layer.filter(ImageFilter.GaussianBlur(9))


def put(draw: ImageDraw.ImageDraw, xy, text, fnt, fill, stroke=0,
        stroke_fill=None, anchor="la") -> None:
    draw.text(xy, text, font=fnt, fill=fill, anchor=anchor,
              stroke_width=stroke, stroke_fill=stroke_fill)


def build(variant: str) -> Image.Image:
    base = Image.open(SRC).convert("RGB")
    img = gradient_panel(base) if variant != "nopanel" else base.copy()
    img = img.convert("RGBA")

    big = font(FONT_BOLD, 132)
    mid = font(FONT_BOLD, 62)
    small = font(FONT_REG, 30)

    # 文字内容随变体微调
    if variant == "alt":
        line1, line2 = "506 位主将", "哪一位适合你？"
        color2 = (255, 220, 130)
    else:
        line1, line2 = "506 位主将", "145 道题，测出你该玩哪个"
        color2 = (255, 214, 110)

    L1 = (455, 250)
    L2 = (458, 415)
    L3 = (458, 500)
    foot = (455, 782)

    def paint(d: ImageDraw.ImageDraw) -> None:
        put(d, L1, line1, big, (255, 255, 255), 0, None)
        put(d, L2, line2, mid, color2, 0, None)

    # ① 柔光：白色字迹模糊后垫底，让字有"发光"感
    glow = glow_layer((W, H), lambda d: (
        put(d, L1, line1, big, (120, 190, 255, 165)),
        put(d, L2, line2, mid, (255, 200, 90, 130)),
    ))
    img = Image.alpha_composite(img, glow)

    # ② 主体字：粗描边保证压在光点上也能读
    d = ImageDraw.Draw(img)
    put(d, L1, line1, big, (255, 255, 255), 9, (8, 14, 26))
    put(d, L2, line2, mid, color2, 6, (8, 14, 26))

    # ③ 副标题：小字，浅色
    put(d, L3, "EDH 指挥官性格测试", small, (196, 214, 238), 4, (8, 14, 26))

    # ④ 左下角标注（暗处，不抢眼）
    put(d, foot, "manvatian1121.github.io/commander-quiz",
        font(FONT_REG, 26), (150, 172, 200), 3, (8, 14, 26))

    out = img.convert("RGB")
    path = OUT / f"cover_{variant}{SUFFIX}.png"
    out.save(path, quality=95)
    # 同时给一张裁到 B 站封面比例的
    crop_w = int(H * 1146 / 717)
    if crop_w <= W:
        left = (W - crop_w) // 2
        out.crop((left, 0, left + crop_w, H)).save(
            OUT / f"cover_{variant}{SUFFIX}_bili1146x717.png", quality=95)
    print(f"  ✓ {path.name}")
    return out


for v in ("nopanel", "alt"):
    build(v)
print("\n同时导出了裁到 1146×717 的 B 站封面版本。")
