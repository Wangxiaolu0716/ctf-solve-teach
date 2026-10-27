#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""harvest.py - 把 solves/ 里做完的题收成可复用的案例库。

用法:
    python harvest.py [--solves solves] [--out references/cases.md] [--check]

从每道题的 README.md 抽取：分类、一句话解法、知识点标签、工具链、
30 秒识别特征、坑，输出按分类分组、可按标签反查的 cases.md。

目标：下次遇到同类题，先 grep 现象直接跳到当时的解法，不用从头再走一遍。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

H2 = re.compile(r"^##\s+(.+)$", re.M)


def section(text, keyword):
    """取某个 ## 标题下的正文（到下一个 ## 为止）。"""
    marks = list(H2.finditer(text))
    for i, m in enumerate(marks):
        if keyword in m.group(1):
            start = m.end()
            end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
            return text[start:end].strip()
    return ""


def table_cols(block, col=0):
    """从 markdown 表格取指定列（跳过表头与分隔行）。"""
    out = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip().replace(chr(96), "") for c in line.strip("|").split("|")]
        if len(cells) <= col:
            continue
        if set(cells[0]) <= set("-: "):
            continue
        if cells[0] in ("ID", "工具", "卡在哪", "项", "#"):
            continue
        if not cells[col]:
            continue
        out.append(cells[col])
    return out


def field(block, key):
    for line in block.splitlines():
        cells = [c.strip().replace(chr(96), "") for c in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0] == key:
            return cells[1]
    return ""


def bullets(block):
    out = []
    for line in block.splitlines():
        s = line.strip()
        if s.startswith(("- ", "* ")):
            out.append(s[2:].strip())
    return out


def first_para(block):
    for line in block.splitlines():
        s = line.strip()
        if s and not s.startswith(("#", "|", ">", "-", "*", "\x60\x60\x60")):
            return s
    return ""


BAD_HEAD = re.compile(r"弯路|失败|死路|反例|踩坑|放弃")
BT3 = chr(96) * 3


def extract_avoid(text):
    """只从 journal 的「弯路/失败」章节抽结论，避免把正文里的“别”当弯路。"""
    out = []
    blocks = re.split(r"^#{2,3}\s+", text, flags=re.M)[1:]
    for b in blocks:
        lines = b.splitlines()
        if not lines:
            continue
        head, body = lines[0], lines[1:]
        if not BAD_HEAD.search(head):
            continue
        for line in body:
            s = line.strip()
            if not s or s.startswith((">", "|", BT3, "### ")):
                continue
            s = re.sub(r"^[-*]\s*", "", s)
            s = re.sub(r"^(现象|判断|解读|结论|教训|原因|结果)[：:]\s*", "", s)
            s = s.replace("**", "").strip()
            if len(s) < 10:
                continue
            if s not in out:
                out.append(s[:80])
            if len(out) >= 2:
                return out
    return out


def load_case(d):
    readme = d / "README.md"
    if not readme.is_file():
        return None
    t = readme.read_text(encoding="utf-8", errors="replace")
    if len(H2.findall(t)) < 5:
        return None

    info = section(t, "题目情报")
    case = {
        "name": d.name,
        "category": re.split(r"[/\s（(]", field(info, "分类") or "misc")[0] or "misc",
        "summary": first_para(section(t, "结论")) or "-",
        "points": table_cols(section(t, "知识点"), 0),
        "tools": [x for x in table_cols(section(t, "工具"), 0) if x][:6],
        "signs": bullets(section(t, "同类题迁移"))[:4],
        "traps": table_cols(section(t, "卡壳"), 0)[:3],
    }
    flag_file = d / "flag.txt"
    if flag_file.is_file():
        for ln in flag_file.read_text(encoding="utf-8", errors="replace").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and ln != "TODO":
                case["flag"] = ln
                break
    jr = d / "journal.md"
    if jr.is_file():
        case["avoid"] = extract_avoid(jr.read_text(encoding="utf-8", errors="replace"))
    if not case["points"]:
        case["points"] = re.findall(r"^###\s+(?:步骤\s*\d+\s*·\s*)?知识点｜(.+)$", t, re.M)[:4]
    return case


BT = chr(96)


def render(cases):
    by_cat = {}
    for c in cases:
        by_cat.setdefault(c["category"], []).append(c)

    out = [
        "# 案例库（自动生成，勿手改）",
        "",
        "> 由 " + BT + "scripts/harvest.py" + BT + " 从 " + BT + "solves/*/README.md" + BT + " 抽取，做完新题跑一次即更新。",
        "> **开工前先按现象搜一遍**：同类题直接跳对应目录看 README，比从零判型快。",
        "",
        "共 " + str(len(cases)) + " 个案例，覆盖 " + str(len(by_cat)) + " 类。",
        "",
        "## 反查表（按知识点标签）",
        "",
        "| 标签 | 出现过的题 |",
        "|---|---|",
    ]

    tag_map = {}
    for c in cases:
        for tag in c["points"]:
            tag_map.setdefault(tag, []).append(c["name"])
    for tag in sorted(tag_map):
        out.append("| " + BT + tag + BT + " | " + ", ".join(sorted(set(tag_map[tag]))) + " |")

    if any(c.get("avoid") for c in cases):
        out += ["", "## 反模式清单（这条路别走）", ""]
        for c in sorted(cases, key=lambda x: x["name"]):
            for a in c.get("avoid", [])[:2]:
                out.append("- **" + c["name"] + "**：" + a)

    out += ["", "## 按分类", ""]
    for cat in sorted(by_cat):
        out += ["### " + cat, "", "| 题目 | 一句话解法 | 关键工具 |", "|---|---|---|"]
        for c in sorted(by_cat[cat], key=lambda x: x["name"]):
            tools = " / ".join(BT + x + BT for x in c["tools"]) or "-"
            summary = c["summary"].replace("|", chr(92) + "|")[:110]
            out.append("| " + c["name"] + " | " + summary + " | " + tools + " |")
        out.append("")

    out += ["## 案例卡", ""]
    for c in sorted(cases, key=lambda x: x["name"]):
        out.append("### " + c["name"])
        out.append("")
        out.append("- 分类：" + c["category"])
        out.append("- 解法：" + c["summary"])
        if c.get("flag"):
            out.append("- flag：" + BT + c["flag"] + BT)
        if c["points"]:
            out.append("- 知识点：" + "、".join(BT + p + BT for p in c["points"]))
        if c["tools"]:
            out.append("- 工具：" + " / ".join(BT + x + BT for x in c["tools"]))
        if c["signs"]:
            out.append("- 30 秒识别：")
            for s in c["signs"]:
                out.append("  - " + s)
        if c["traps"]:
            out.append("- 坑：" + "；".join(c["traps"]))
        if c.get("avoid"):
            out.append("- 别走：" + "；".join(c["avoid"][:2]))
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description="把 solves/ 收成案例库")
    ap.add_argument("--solves", default="solves", help="解题目录，默认 ./solves")
    ap.add_argument("--out", default=str(here.parent / "references" / "cases.md"))
    ap.add_argument("--check", action="store_true", help="只比对不写；不一致返回 1")
    args = ap.parse_args()

    root = Path(args.solves)
    if not root.is_dir():
        print("目录不存在: " + str(root), file=sys.stderr)
        return 2

    cases = []
    for d in sorted(root.iterdir()):
        if not d.is_dir() or d.name.startswith(("_", ".")):
            continue
        c = load_case(d)
        if c:
            cases.append(c)

    text = render(cases)
    out = Path(args.out)
    if args.check:
        old = out.read_text(encoding="utf-8") if out.is_file() else ""
        if old != text:
            print("案例库不是最新：" + str(out), file=sys.stderr)
            return 1
        print("案例库已是最新：" + str(len(cases)) + " 个案例")
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print("已更新 " + str(out) + "：" + str(len(cases)) + " 个案例")
    return 0


if __name__ == "__main__":
    sys.exit(main())
