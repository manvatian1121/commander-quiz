#!/usr/bin/env python3
"""第四轮第三行文案：用户提的「基于20维性格测试的EDH主将推荐」。

评价：
- 「基于…的」结构语法正确，比「·」分隔更明确 ✓
- 但有一个精度问题：那 20 个维度是「玩法轴」，不是「性格维度」。
  输入是性格题，输出是 20 维玩法偏好向量。所以严格讲
  「20 维性格测试」把输入的性质安到了输出的维度上。
- 格式问题：数字前后要留空格、去掉「的」前的空格

三个版本对比：用户原意 / 最简 / 最精确。
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

L1 = "506 位主将"
L2 = "10 分钟，不懂万智牌也能尝试"

THIRD = {
    "h1_user":  "基于 20 维性格测试的 EDH 主将推荐",   # 用户原意，修了格式
    "h2_dot":   "20 维性格测试 · EDH 主将推荐",        # 最简（上一轮的 g2）
    "h3_exact": "20 个玩法维度 · EDH 主将推荐",        # 最精确
}


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=0)


def main() -> int:
    base = Image.open(SRC).convert("RGB")
    for name, l3 in THIRD.items():
        img = base.copy().convert("RGBA")
        big = font(FONT_BOLD, 124)
        mid = font(FONT_BOLD, 58)
        small = font(FONT_REG, 30)
        while small.getlength(l3) > W - 200 and small.size > 22:
            small = font(FONT_REG, small.size - 2)

        P1, P2, P3 = (455, 262), (458, 432), (458, 524)
        foot = (455, 782)

        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.text(P1, L1, font=big, fill=(120, 190, 255, 165), anchor="la")
        gd.text(P2, L2, font=mid, fill=(255, 200, 90, 135), anchor="la")
        img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(10)))

        d = ImageDraw.Draw(img)
        d.text(P1, L1, font=big, fill=(255, 255, 255), anchor="la",
               stroke_width=9, stroke_fill=(8, 14, 26))
        d.text(P2, L2, font=mid, fill=(255, 214, 110), anchor="la",
               stroke_width=7, stroke_fill=(8, 14, 26))
        d.text(P3, l3, font=small, fill=(200, 216, 240), anchor="la",
               stroke_width=4, stroke_fill=(8, 14, 26))
        d.text(foot, "manvatian1121.github.io/commander-quiz",
               font=font(FONT_REG, 26), fill=(158, 178, 204), anchor="la",
               stroke_width=3, stroke_fill=(8, 14, 26))

        out = img.convert("RGB")
        out.save(OUT / f"copy_{name}.png", quality=95)
        cw = int(H * 1146 / 717)
        left = (W - cw) // 2
        out.crop((left, 0, left + cw, H)).save(OUT / f"copy_{name}_bili.png", quality=95)
        print(f"  ✓ {name:<10} 「{l3}」  {small.size}px / 宽 {small.getlength(l3):.0f}px")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
