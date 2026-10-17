# examples · 可直接复跑的示例

## 示例_B64双重编码

一道最小的"编码级联"题，用来演示这个 skill 的完整产出形态。

```bash
# 1) 生成题目附件（等价于出题人给你的 chall.txt）
cd 示例_B64双重编码
python scripts/make_chall.py        # 生成 artifacts/_build_chall.txt

# 2) 复现解题
ctf dec "$(cat artifacts/_build_chall.txt)"

# 3) 看产出文档
cat README.md        # 教学向 Writeup
cat journal.md       # 逐步日志（含弯路）
cat flag.txt
```

关注点：

- `00-brief.md` 里"初始假设"写了什么，以及后面怎么被纠正；
- `journal.md` 每步都带"工具"和"知识点"，失败的命令也留着；
- `README.md` 的第 7 章（卡壳与弯路）和第 9 章（同类题迁移）长什么样。

这个示例已经通过 `check_doc.py` 质量门，可以直接拿来对照格式。
