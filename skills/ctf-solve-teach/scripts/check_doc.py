#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_doc.py - 交付前质量门：检查解题目录是否够格叫"完整 Writeup"。

用法:
    python check_doc.py solves/题目名 [--strict]

检查项:
  1. 目录结构（artifacts/ work/ scripts/ flag.txt journal.md README.md）
  2. README 必备章节（9 个语义章节，允许同义词）
  3. README 残留模板占位符 / TODO
  4. README 代码块数量（命令可复制）
  5. journal 步骤数 + 每步是否含"工具/知识点"
  6. flag.txt 是否有真实内容

退出码: 0 = PASS, 1 = 有待修项
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    ("题目情报", ("情报", "题目信息", "题面")),
    ("一句话结论", ("结论", "一句话", "答案")),
    ("解题路径", ("路径", "流程", "思路", "总览")),
    ("关键步骤复盘", ("复盘", "关键步骤", "详细步骤")),
    ("工具与用法", ("工具",)),
    ("知识点地图", ("知识点", "知识")),
    ("卡壳与弯路", ("卡壳", "弯路", "踩坑", "失败")),
    ("可复用脚本", ("脚本", "复用")),
    ("同类题迁移", ("迁移", "变体", "同类", "举一反三")),
]

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z_]+\}\}")
STEP_RE = re.compile(r"^###\s*步骤", re.MULTILINE)


class Report:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []
        self.fail = 0

    def ok(self, item: str, detail: str = "") -> None:
        self.rows.append(("PASS", item, detail))

    def bad(self, item: str, detail: str = "") -> None:
        self.rows.append(("FAIL", item, detail))
        self.fail += 1

    def warn(self, item: str, detail: str = "") -> None:
        self.rows.append(("WARN", item, detail))

    def render(self) -> str:
        width = max((len(r[1]) for r in self.rows), default=10) + 2
        out = []
        for status, item, detail in self.rows:
            mark = {"PASS": "[ok]  ", "FAIL": "[FAIL]", "WARN": "[warn]"}[status]
            out.append(f"{mark} {item.ljust(width)} {detail}".rstrip())
        return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", help="题目目录，如 solves/我的题")
    ap.add_argument("--strict", action="store_true", help="WARN 也算失败")
    args = ap.parse_args()

    base = Path(args.dir).expanduser()
    rep = Report()

    if not base.is_dir():
        print(f"[FAIL] 目录不存在: {base}")
        return 1

    for sub in ("artifacts", "work", "scripts"):
        d = base / sub
        rep.ok("目录 " + sub + "/") if d.is_dir() else rep.bad("目录 " + sub + "/", "缺失")

    for name in ("00-brief.md", "journal.md", "flag.txt", "README.md"):
        p = base / name
        rep.ok(name) if p.is_file() else rep.bad(name, "缺失")

    readme_path = base / "README.md"
    readme = readme_path.read_text(encoding="utf-8", errors="replace") if readme_path.is_file() else ""

    h2 = [ln.strip("# ").strip() for ln in readme.splitlines() if ln.startswith("## ")]
    for label, keys in REQUIRED_SECTIONS:
        hit = any(any(k in h for k in keys) for h in h2)
        rep.ok(f"章节 {label}") if hit else rep.bad(f"章节 {label}", "README 里没有对应 ## 标题")

    ph = PLACEHOLDER_RE.findall(readme)
    rep.bad("无模板占位符", f"残留 {', '.join(sorted(set(ph)))}") if ph else rep.ok("无模板占位符")

    todo = readme.count("TODO")
    rep.warn("无 TODO 标记", f"{todo} 处") if todo else rep.ok("无 TODO 标记")

    blocks = readme.count("```") // 2
    if blocks >= 4:
        rep.ok("命令代码块", f"{blocks} 个")
    elif blocks >= 1:
        rep.warn("命令代码块", f"只有 {blocks} 个，建议关键步骤都贴原命令")
    else:
        rep.bad("命令代码块", "一个都没有，命令要可复制")

    journal_path = base / "journal.md"
    journal = journal_path.read_text(encoding="utf-8", errors="replace") if journal_path.is_file() else ""
    steps = STEP_RE.findall(journal)
    if len(steps) >= 3:
        rep.ok("journal 步骤数", f"{len(steps)} 步")
    elif steps:
        rep.warn("journal 步骤数", f"只有 {len(steps)} 步，过程记录偏少")
    else:
        rep.bad("journal 步骤数", "没有 '### 步骤' 记录")

    chunks = re.split(r"^###\s*步骤", journal, flags=re.MULTILINE)[1:]
    complete = sum(1 for c in chunks if "工具" in c and "知识点" in c)
    if chunks and complete >= max(2, len(chunks) // 2):
        rep.ok("步骤含工具/知识点", f"{complete}/{len(chunks)} 步完整")
    elif chunks:
        rep.warn("步骤含工具/知识点", f"{complete}/{len(chunks)} 步完整，教学字段要补齐")
    else:
        rep.bad("步骤含工具/知识点", "无法检查")

    flag_path = base / "flag.txt"
    flag = ""
    if flag_path.is_file():
        for ln in flag_path.read_text(encoding="utf-8", errors="replace").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and ln != "TODO":
                flag = ln
                break
    if flag:
        rep.ok("flag.txt", flag[:80])
    else:
        rep.bad("flag.txt", "没有真实 flag（部分结论请写 PARTIAL: ...）")

    print(rep.render())
    print()
    if rep.fail == 0:
        if args.strict and any(r[0] == "WARN" for r in rep.rows):
            print("结论: FAIL（strict 模式，WARN 也拦）")
            return 1
        print("结论: PASS —— 可以交付")
        return 0
    print(f"结论: FAIL —— {rep.fail} 项待修（按上面的 FAIL 逐条补）")
    return 1


if __name__ == "__main__":
    sys.exit(main())
