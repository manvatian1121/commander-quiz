#!/usr/bin/env python3
"""第二轮封面文案——围绕「10 分钟 + 零门槛」。

用户提的版本：「10分钟，完全不懂万智牌也能尝试的」
问题：语法是半句（…的）、太长、用词偏书面。

这一轮试几种改法，并处理一个取舍：
「10 分钟」和「不懂也能测」都是降低门槛，但**两个卖点放一行会互相稀释**。
所以有几种分配方式，都出出来对比。
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
SRC = OUT / "noobai_i2i_wide_clean.png"
FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_REG = r"C:\Windows\Fonts\msyh.ttc"
W, H = 1536, 864

# name: (第一行, 第二行, 第三行小字)
VARIANTS = {
    "e1_noname":   ("506 位主将", "10 分钟，不懂万智牌也能测", "EDH 指挥官性格测试"),
    "e2_zero":     ("506 位主将", "10 分钟，零基础也能测",     "EDH 指挥官性格测试"),
    "e3_split":    ("506 位主将", "10 分钟，挑出适合你的",     "不懂万智牌也能测"),
    "e4_barrier":  ("506 位主将", "不懂万智牌也能测",          "10 分钟出结果 · EDH 指挥官"),
    "e5_punch":    ("506 位主将，挑哪个？", "10 分钟，零基础也能测", "EDH 指挥官性格测试"),
}


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=0)


def main() -> int:
    base = Image.open(SRC).convert("RGB")
    for name, (l1, l2, l3) in VARIANTS.items():
        img = base.copy().convert("RGBA")

        big = font(FONT_BOLD, 124)
        while big.getlength(l1) > W - 190 and big.size > 76:
            big = font(FONT_BOLD, big.size - 4)
        mid = font(FONT_BOLD, 58)
        while mid.getlength(l2) > W - 200 and mid.size > 36:
            mid = font(FONT_BOLD, mid.size - 3)

        L1 = (455, 262)
        L2 = (458, 432)
        L3 = (458, 524)
        foot = (455, 782)

        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.text(L1, l1, font=big, fill=(120, 190, 255, 165), anchor="la")
        gd.text(L2, l2, font=mid, fill=(255, 200, 90, 135), anchor="la")
        img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(10)))

        d = ImageDraw.Draw(img)
        d.text(L1, l1, font=big, fill=(255, 255, 255), anchor="la",
               stroke_width=9, stroke_fill=(8, 14, 26))
        d.text(L2, l2, font=mid, fill=(255, 214, 110), anchor="la",
               stroke_width=7, stroke_fill=(8, 14, 26))
        d.text(L3, l3, font=font(FONT_REG, 30), fill=(200, 216, 240), anchor="la",
               stroke_width=4, stroke_fill=(8, 14, 26))
        d.text(foot, "manvatian1121.github.io/commander-quiz",
               font=font(FONT_REG, 26), fill=(158, 178, 204), anchor="la",
               stroke_width=3, stroke_fill=(8, 14, 26))

        out = img.convert("RGB")
        out.save(OUT / f"copy_{name}.png", quality=95)
        cw = int(H * 1146 / 717)
        left = (W - cw) // 2
        out.crop((left, 0, left + cw, H)).save(OUT / f"copy_{name}_bili.png", quality=95)
        print(f"  ✓ {name:<12} 「{l1}」/「{l2}」/「{l3}」  第二行 {mid.size}px"
              f"（{mid.getlength(l2):.0f}px 宽）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
