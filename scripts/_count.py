# -*- coding: utf-8 -*-
"""测量：对给定文本按 validate 口径报告字数并判定是否达标。"""
import sys

sys.stdout.reconfigure(encoding="utf-8")


def count(s: str) -> int:
    return sum(1 for ch in s.replace("\n", "") if not ch.isspace())


LIMITS = {"tagline": 20, "intro": 120, "build": 170}
MINS = {"intro": 70, "build": 110}

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        field, _, value = arg.partition("=")
        n = count(value)
        lo, hi = MINS.get(field, 1), LIMITS.get(field, 9999)
        ok = "✓" if lo <= n <= hi else "✗"
        print(f"{ok} {field} {n} (目标 {lo}-{hi})")
