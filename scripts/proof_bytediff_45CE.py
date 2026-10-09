# -*- coding: utf-8 -*-
"""字节级复核：改后文件 vs _proof_bak 快照，确认只有预期行变化、编码/EOL 未变。"""
import sys, hashlib
from pathlib import Path

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")
DATA = Path(ROOT / "data")
BAK = DATA / "_proof_bak"
for name in ["bank4.json", "bank5.json", "bankC.json", "bankE.json"]:
    a = (BAK / name).read_bytes()
    b = (DATA / name).read_bytes()
    print(f"\n### {name}")
    print(f"  BOM: 改前={a[:3] == b'\xef\xbb\xbf'} 改后={b[:3] == b'\xef\xbb\xbf'}"
          f"   CRLF数: 改前={a.count(b'\r\n')} 改后={b.count(b'\r\n')}"
          f"   行数: {len(a.splitlines())} -> {len(b.splitlines())}")
    la, lb = a.decode("utf-8").splitlines(), b.decode("utf-8").splitlines()
    assert len(la) == len(lb), f"{name} 行数不一致"
    n = 0
    for i, (x, y) in enumerate(zip(la, lb), 1):
        if x != y:
            n += 1
            print(f"  L{i}")
            print(f"    - {x.strip()}")
            print(f"    + {y.strip()}")
    print(f"  变化行数: {n}")
