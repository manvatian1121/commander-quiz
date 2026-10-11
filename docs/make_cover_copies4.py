#!/usr/bin/env python3
"""第三行小字的改法。

用户想用「基于MBTI测试的个人指挥官主将推荐」。这个不能做——本项目与 MBTI
没有任何关系（4 个维度 vs 20 个轴、16 型 vs 主将排序、类型学 vs 余弦相似度），
而且 MBTI 是注册商标。

但用户的需求是对的：需要一个大众熟悉的锚点，让人一秒明白「这是个性格测试」。
下面这些说法既准确、又能达到同样的效果。
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
    "g1_plain":  "性格测试 · 指挥官主将推荐",
    "g2_dims":   "20 维性格测试 · EDH 主将推荐",
    "g3_life":   "生活化性格题，挑出你的主将",
    "g4_honest": "不问牌技，只问性格",
    "g5_old":    "EDH 指挥官性格测试",          # 对照：原来的
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
        print(f"  ✓ {name:<11} 「{l3}」  {small.size}px")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
