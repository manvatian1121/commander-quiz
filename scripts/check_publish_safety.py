#!/usr/bin/env python3
"""发布前安全自检 —— 以后不用再人工问「要不要查」。

上次人工全查的结论仍然有效（900 个对象全遍历、提交身份、仓库设置）。
但每次推送都会新增内容，所以真正需要的是**把它变成每次自动跑的检查**，
而不是每次重新人工过一遍。

这个脚本查五件事：
  ① 已跟踪文件里有没有本机绝对路径 / 用户名
  ② 已跟踪文件里有没有凭据类内容
  ③ 提交者邮箱是不是隐私邮箱
  ④ 暂存区里有没有体积异常的二进制（上次 git add -A 吞进 108MB 的教训）
  ⑤ 工作区里有没有该被忽略却会被 add 进去的大目录
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parent.parent

BIG_FILE_MB = 1.0          # 单文件超过这个体积就警告
BIG_TOTAL_MB = 40.0        # 已跟踪内容总字节上限

SECRETS = {
    "GitHub token":   r"gh[pousr]_[A-Za-z0-9]{20,}",
    "AWS 访问密钥":    r"AKIA[0-9A-Z]{16}",
    "Slack token":    r"xox[abposr]-[A-Za-z0-9-]{10,}",
    "Google API key": r"AIza[0-9A-Za-z_\-]{35}",
    "OpenAI 风格密钥": r"\bsk-[A-Za-z0-9]{32,}",
    "私钥 PEM":        r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "JWT":            r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.",
    "赋值式密钥":      r"(?i)\b(api[_-]?key|secret|passwd|password|access[_-]?token)\b"
                      r"\s*[:=]\s*['\"][^'\"]{8,}['\"]",
}
LOCAL = {
    "本机绝对路径": r"[A-Za-z]:[\\/]{1,2}(万智|Users[\\/]{1,2}[A-Za-z0-9_.\-]+)",
    "本机用户名":   r"\bq0112\b",
}


def git(*a: str) -> str:
    r = subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.stdout or ""


def main() -> int:
    problems: list[str] = []
    files = [f for f in git("ls-files").split("\n") if f.strip()]
    print(f"已跟踪 {len(files)} 个文件")

    # ① + ② 内容扫描
    hits: dict[str, list[str]] = {}
    for f in files:
        p = ROOT / f
        if not p.is_file():
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for name, rx in {**LOCAL, **SECRETS}.items():
            if re.search(rx, text):
                hits.setdefault(name, []).append(f)
    for name in {**LOCAL, **SECRETS}:
        got = hits.get(name, [])
        if got:
            problems.append(f"{name}：{len(got)} 个文件（{', '.join(got[:3])}）")
            print(f"  ✗ {name}：{got[:3]}")
        else:
            print(f"  ✓ {name}")

    # ③ 提交者邮箱
    emails = {e.strip() for e in git("log", "--all", "--format=%ae%n%ce").split("\n")
              if "@" in e}
    bad_mail = [e for e in emails if "noreply" not in e.lower()]
    print(f"  {'✗ 含非隐私邮箱：' + str(bad_mail) if bad_mail else '✓ 提交邮箱全部为隐私邮箱'}")
    if bad_mail:
        problems.append(f"提交邮箱泄露：{bad_mail}")

    # ④ 大体积文件
    big = []
    total = 0
    for f in files:
        p = ROOT / f
        if not p.is_file():
            continue
        total += p.stat().st_size
        if p.stat().st_size > BIG_FILE_MB * 1024 * 1024:
            big.append((f, p.stat().st_size / 1024 / 1024))
    total_mb = total / 1024 / 1024
    print(f"  已跟踪内容合计 {total_mb:.1f} MB"
          f"  {'✗ 超上限' if total_mb > BIG_TOTAL_MB else '✓'}")
    if total_mb > BIG_TOTAL_MB:
        problems.append(f"跟踪体积 {total_mb:.1f} MB 超过 {BIG_TOTAL_MB} MB")
    for f, mb in sorted(big, key=lambda x: -x[1])[:5]:
        print(f"     {mb:5.1f} MB  {f}")

    # ⑤ 未跟踪的大目录（会被 git add -A 吞进去）
    ignored = set((ROOT / ".gitignore").read_text(encoding="utf-8").split("\n"))
    suspects = []
    for d in ("_scratch", "docs/thumbnails", "docs/group-avatar"):
        p = ROOT / d
        if not p.is_dir():
            continue
        size = sum(f.stat().st_size for f in p.rglob("*") if f.is_file())
        covered = any(s.strip().rstrip("/") == d or d.startswith(s.strip().rstrip("/"))
                      for s in ignored if s.strip() and not s.strip().startswith("#"))
        mark = "✓ 已忽略" if covered else "✗ 未忽略"
        print(f"  {mark}  {d:<20} {size / 1024 / 1024:6.1f} MB"
              f"{'' if covered else '  ← git add -A 会吞进去'}")
        if not covered and size > 5 * 1024 * 1024:
            suspects.append(d)
    if suspects:
        problems.append(f"未忽略的大目录：{suspects}（git add -A 有风险）")

    print()
    if problems:
        print(f"✗ 发现 {len(problems)} 个问题：")
        for p in problems:
            print(f"    - {p}")
        return 1
    print("✓ 发布前自检全部通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
