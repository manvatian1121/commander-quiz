#!/usr/bin/env python3
"""封面文案变体——把「145 道题」换掉。

问题：145 是题库总量，不是用户要答的题数（实际 88~106），
既不准确也吓人。而且「题数」比「时间」听着重得多。

所以新文案统一改成：第一行给价值（506 位主将），第二行给成本（用时间或「挑一个」）。
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
    "a_minutes": ("506 位主将", "10 分钟，挑出适合你的"),
    "b_quick":   ("506 位主将", "最短 3 分钟就出结果"),
    "c_nocount": ("506 位主将", "挑一个真正适合你的"),
    "d_norules": ("506 位主将", "不懂规则也能测"),
}


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=0)


def main() -> int:
    base = Image.open(SRC).convert("RGB")
    for name, (l1, l2) in VARIANTS.items():
        img = base.copy().convert("RGBA")
        big = font(FONT_BOLD, 124)
        mid = font(FONT_BOLD, 58)

        # 文案变长时缩字号，保证不出画
        while mid.getlength(l2) > W - 200 and mid.size > 38:
            mid = font(FONT_BOLD, mid.size - 3)

        L1 = (455, 268)
        L2 = (458, 438)
        L3 = (458, 528)
        foot = (455, 782)

        # 柔光垫底
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
        d.text(L3, "EDH 指挥官性格测试", font=font(FONT_REG, 30),
               fill=(200, 216, 240), anchor="la",
               stroke_width=4, stroke_fill=(8, 14, 26))
        d.text(foot, "manvatian1121.github.io/commander-quiz",
               font=font(FONT_REG, 26), fill=(158, 178, 204), anchor="la",
               stroke_width=3, stroke_fill=(8, 14, 26))

        out = img.convert("RGB")
        out.save(OUT / f"copy_{name}.png", quality=95)
        crop_w = int(H * 1146 / 717)
        left = (W - crop_w) // 2
        out.crop((left, 0, left + crop_w, H)).save(
            OUT / f"copy_{name}_bili.png", quality=95)
        print(f"  ✓ copy_{name}.png   「{l2}」")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
