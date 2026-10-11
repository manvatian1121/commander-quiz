#!/usr/bin/env python3
"""第三轮：把「测」换成「尝试」系。

用户判断：「尝试」比「测」更吸引人——「测」像考试，「尝试」像随便玩玩。
这个判断对，因为整个项目的定位就是「没有正确答案」，用「测」是自相矛盾的。

语法上只需去掉那个多余的「的」即可（headline 以动词结尾在中文里很常见）。
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

VARIANTS = {
    "f1_trychinese": ("506 位主将", "10 分钟，不懂万智牌也能尝试", "EDH 指挥官性格测试"),
    "f2_shi":        ("506 位主将", "10 分钟，不懂万智牌也能试",   "EDH 指挥官性格测试"),
    "f3_front":      ("506 位主将", "不懂万智牌也能尝试",          "10 分钟出结果 · EDH 指挥官"),
    "f4_noexp":      ("506 位主将", "10 分钟，没玩过也能尝试",     "EDH 指挥官性格测试"),
}


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=0)


def main() -> int:
    base = Image.open(SRC).convert("RGB")
    for name, (l1, l2, l3) in VARIANTS.items():
        img = base.copy().convert("RGBA")
        big = font(FONT_BOLD, 124)
        mid = font(FONT_BOLD, 58)
        while mid.getlength(l2) > W - 200 and mid.size > 36:
            mid = font(FONT_BOLD, mid.size - 3)

        L1, L2, L3 = (455, 262), (458, 432), (458, 524)
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
        print(f"  ✓ {name:<14} 「{l2}」  {mid.size}px / 宽 {mid.getlength(l2):.0f}px")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
