"""按「最小化轴覆盖损失」重做 bank2 的 6 处替换（从备份重建，保证干净）。"""
import shutil
import sys
from pathlib import Path

# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding="utf-8")

DATA = Path(ROOT / "data")
CUR, BAK = DATA / "bank2.json", DATA / "_backup_bank2.json"

REPL = [
    ("h2a3", '        {"t": "隔三差五复盘一次，看看还能怎么优化", "s": {"counters": 2.5, "artifacts": 1.5}},',
     '        {"t": "不会，拖着拖着这事就翻过去了，懒得再回头折腾", "s": {"drain": 2.0, "chaos": 1.5}},'),
    ("s27", '        {"t": "周末自己摸，每个按钮点一遍，界面也调成自己顺眼的", "s": {"artifacts": 2.5, "enchant": 1.5, "combo": 1.0}},',
     '        {"t": "不太当回事，反正不会用的又不止我一个，用两天自然就顺了", "s": {"politics": 2.0, "drain": 1.5, "enchant": 1.0}},'),
    ("s29", '        {"t": "先做个粗糙版本，再一轮轮改", "s": {"blink": 2.5, "enchant": 1.0, "counters": 1.0}},',
     '        {"t": "不着急，先放着吧，隔几天翻出来弄两下，慢慢就磨完了", "s": {"drain": 2.0, "blink": 1.0, "enchant": 1.0}},'),
    ("s30", '        {"t": "先重新定一遍三件事的截止时间，按我的表来", "s": {"stax": 2.5, "politics": 1.5}},',
     '        {"t": "不往心里去，被催两句又不会少块肉，照旧一天天慢慢来", "s": {"stompy": 2.0, "drain": 1.5, "counters": 1.0}},'),
    ("h2c2", '        {"t": "先翻出当初的记录，看看是谁的建议", "s": {"grave": 2.0, "politics": 1.5}},',
     '        {"t": "无所谓，随他说，我犯不上为这个跟人掰扯", "s": {"chaos": 2.0, "stompy": 1.5}},'),
    ("s31", '        {"t": "跟他讲清楚：我只干我擅长的那块，别的别找我", "s": {"stax": 2.5, "voltron": 1.5}}',
     '        {"t": "算了，钱和朋友掺一起迟早要出事，这种局我不掺和", "s": {"control": 2.0, "stax": 1.5}}'),
]


def main():
    shutil.copyfile(BAK, CUR)
    text = CUR.read_text(encoding="utf-8")
    for qid, old, new in REPL:
        if text.count(old) != 1:
            print(f"[FAIL] {qid}: 命中 {text.count(old)} 次")
            return 1
        text = text.replace(old, new)
        print(f"[OK] {qid}")
    CUR.write_text(text, encoding="utf-8", newline="")
    print("bank2.json 已按最小损失方案重建")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
