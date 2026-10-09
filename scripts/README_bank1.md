# commander-quiz / scripts — bank1 相关脚本说明

## 验收（随时可跑，只读）

```powershell
cd D:\万智\commander-quiz
python scripts\check_bank1.py          # 九项自检，退出码 0 = 全通过
python scripts\dump_bank1.py           # 人读版题目清单
python scripts\audit_fuzzy_bank1.py 0.58   # 相似度较高的选项对，供人工复核
```

`check_bank1.py` 的九项对应 `data/QUESTION_SPEC.md` 第六节与任务书第四步：

| 项 | 内容 |
|---|---|
| 1 | JSON 合法、id 唯一、题集完整（s01~s16 + h1a/b/c 各 3 题）、sec 全为 `life`、枢纽题只有 s08 |
| 2 | 每题都有 `next`（`next=null` 只允许出现在 s16） |
| 3 | 所有 `goto` 命中存在的 id，且只出现在枢纽题选项上 |
| 4 | 从 s01 按 next/goto 走通：主线 s01→s16、三条分支各 3 题、三条分支都回归 s09 |
| 5 | 每题选项 3~5 个、文本非空、题内两两不同 |
| 6 | 每选项 1~3 个轴、权重只用 1.0/1.5/2.0/2.5/3.0、轴名合法 |
| 7 | 同题内任意两个选项轴向量余弦相似度 < 0.85 |
| 8 | 20 个轴各被 ≥12 个选项引用 |
| 9 | 题干与选项不出现万智牌术语（54 个关键词） |

## 改题脚本：**一次性**，不要单独重跑

这几个脚本当初是按顺序对 `data/bank1.json` 做增量修改的，多数不是幂等的
（例如 `balance_bank1_pass4.py` 会往 s15 追加一个选项，只做了「文本去重」级别的保护）。
**当前 `bank1.json` 已是终态，改题请直接改 JSON，不要再跑这些脚本。**

若确需从头复现，严格按下列顺序跑：

```powershell
python scripts\balance_bank1.py
python scripts\balance_bank1_pass2.py
python scripts\balance_bank1_pass4.py
python scripts\fix_bank1_semantics.py   # 修轴与语义不符的选项
python scripts\fix_bank1_last.py        # 补 spells/drain，并把 s16.next 复位为 null（必须最后）
python scripts\check_bank1.py
```

注意 `fix_bank1_last.py` 必须排在最后：前面的脚本会整份重写 JSON，
把 `s16.next` 写回 `"s17"`，而 s17 属于 batch2 的 `bank2.json`，本文件里必须写 `null`。
