#!/usr/bin/env python3
"""去左下角水印（第二版）。

第一版失败的教训：
  ① 检测区域开太大，把斗篷的亮边也算成水印 → 补丁里带了斗篷边缘 → 块状伪影
  ② 羽化半径过大 → 补丁半透明 → 水印仍然透出来

这一版：
  · 检测区域严格限制在 x<84（斗篷左缘在 x≈85 之外）
  · 克隆源取正上方同宽的一条，只做 2px 极窄羽化
  · 用「背景基准色」而不是简单克隆来做二次清理——水印笔画细，
    直接抹成局部背景更干净
"""
from __future__ import annotations

import pathlib
import sys

import numpy as np
from PIL import Image, ImageFilter


# --- 路径相对本文件解析，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
THUMBS = ROOT / "docs/thumbnails"
SRC = THUMBS / "noobai_i2i_wide_00001_.png"
DST = THUMBS / "noobai_i2i_wide_clean.png"

# 严格避开斗篷：只处理 x < 84 的竖条
SAFE_X1 = 84


def main() -> int:
    im = Image.open(SRC).convert("RGB")
    W, H = im.size
    arr = np.array(im).astype(float)
    print(f"源图 {W}×{H}")

    # ① 在安全竖条里找亮笔画。水印在图的极下方，从 y=815 往下找。
    y0, y1 = 815, H
    sub = arr[y0:y1, 0:SAFE_X1]
    lum = sub.mean(axis=2)
    bg = float(np.median(lum))
    mask = lum > bg + 22
    ys, xs = np.where(mask)
    if len(ys) == 0:
        print("安全竖条里没找到亮笔画")
        return 1
    bx0, bx1 = int(xs.min()), int(xs.max()) + 1
    by0, by1 = y0 + int(ys.min()), y0 + int(ys.max()) + 1
    print(f"  水印 bbox = ({bx0}, {by0}, {bx1}, {by1})  "
          f"宽{bx1-bx0} 高{by1-by0}  背景亮度基准 {bg:.1f}")

    # ② 取正上方同宽的一条当克隆源（再往上让开一点，避免压到笔画）
    pad_y = 6
    h = by1 - by0
    sy1 = max(0, by0 - pad_y)
    sy0 = max(0, sy1 - h)
    patch = im.crop((0, sy0, SAFE_X1, sy1))
    if patch.size[1] != h:                       # 上方空间不够就拉伸
        patch = patch.resize((SAFE_X1, h), Image.LANCZOS)
    patch = patch.transpose(Image.FLIP_TOP_BOTTOM)

    # ③ 极窄羽化（2px），只在上下边blend，左右不羽化
    m = np.full((h, SAFE_X1), 255.0)
    for i in range(2):
        v = 255.0 * (i + 1) / 3.0
        m[i, :] = np.minimum(m[i, :], v)
        m[h - 1 - i, :] = np.minimum(m[h - 1 - i, :], v)
    mask_img = Image.fromarray(m.astype(np.uint8), "L")

    out = im.copy()
    out.paste(patch, (0, by0), mask_img)

    # ④ 二次清理：克隆后仍有残留（背景不是绝对纯色），把这块的
    #    异常亮点直接压到局部背景色
    a = np.array(out).astype(float)
    region = a[by0:by1, 0:SAFE_X1]
    rl = region.mean(axis=2)
    base = np.median(rl)
    bad = rl > base + 14
    if bad.sum():
        # 逐列取该列的中位数当背景，把亮像素替换掉
        for x in range(SAFE_X1):
            col = region[:, x, :]
            col_l = col.mean(axis=1)
            col_base = np.median(col_l)
            idx = np.where(col_l > col_base + 14)[0]
            for yy in idx:
                col[yy] = [col_base, col_base, col_base] if False else \
                    np.median(region[:, x, :], axis=0)
        a[by0:by1, 0:SAFE_X1] = region
        out = Image.fromarray(a.astype(np.uint8), "RGB")
        print(f"  二次清理：{int(bad.sum())} 个残留亮点被抹平")

    out.save(DST, quality=95)
    print(f"写出 {DST.name}")

    z = (0, by0 - 45, SAFE_X1 + 90, H)
    out.crop(z).resize(((z[2] - z[0]) * 4, (z[3] - z[1]) * 4),
                       Image.NEAREST).save(THUMBS / "_wm_fixed_zoom.png")
    print("导出复核图 _wm_fixed_zoom.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
