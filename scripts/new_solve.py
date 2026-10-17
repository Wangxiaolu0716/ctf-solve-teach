#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""new_solve.py - 为一道 CTF 题目创建标准工作目录骨架。

用法:
    python new_solve.py "题目名" [--src 附件 或 目录 ...] [--root solves] [--category misc]

产出:
    <root>/<题目名>/
      |-- 00-brief.md   题目情报卡
      |-- journal.md    解题日志骨架
      |-- flag.txt      flag 占位
      |-- README.md     Writeup 骨架(收尾时写满)
      |-- artifacts/    原始附件副本(只读)
      |-- work/         临时产物
      `-- scripts/      本题脚本

幂等：目录已存在时只补缺失文件，不覆盖已有内容。
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import shutil
import sys
import unicodedata
from pathlib import Path

BAD_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "references" / "writeup-template.md"

FALLBACK_README = """# {{TITLE}}

> 一句话结论：待填 —— flag{...}

## 1. 题目情报

- 分类：
- 附件：
- flag 格式：

## 2. 一句话结论

## 3. 解题路径

## 4. 关键步骤复盘

## 5. 工具与用法清单

## 6. 知识点地图

## 7. 卡壳与弯路

## 8. 可复用脚本

## 9. 同类题迁移
"""


def slugify(name: str) -> str:
    s = unicodedata.normalize("NFC", name.strip())
    s = BAD_CHARS.sub("", s)
    s = re.sub(r"\s+", "_", s).strip(" ._")
    return s[:60] or "challenge"


def write_if_absent(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def copy_sources(sources, dest: Path) -> list[str]:
    copied = []
    for src in sources:
        src = Path(src).expanduser()
        if not src.exists():
            print(f"  ! 跳过不存在的路径: {src}")
            continue
        if src.is_file():
            target = dest / src.name
            if target.exists():
                stem, suffix = target.stem, target.suffix
                i = 2
                while target.exists():
                    target = dest / f"{stem}_{i}{suffix}"
                    i += 1
            shutil.copy2(src, target)
            copied.append(target.name)
        else:
            for p in sorted(src.rglob("*")):
                if not p.is_file():
                    continue
                rel = p.relative_to(src)
                target = dest / rel
                if target.exists():
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, target)
                copied.append(str(rel))
    return copied


def main() -> int:
    ap = argparse.ArgumentParser(description="创建 CTF 题目工作目录骨架")
    ap.add_argument("title", help="题目名（允许中文）")
    ap.add_argument("--src", nargs="*", default=[], help="附件文件或目录，可多个")
    ap.add_argument("--root", default="solves", help="工作根目录，默认 solves")
    ap.add_argument("--category", default="misc", help="misc/crypto/re/web/pwn/forensics/...")
    args = ap.parse_args()

    slug = slugify(args.title)
    root = Path(args.root).expanduser()
    base = root / slug
    created = []

    for sub in ("artifacts", "work", "scripts"):
        d = base / sub
        if not d.exists():
            d.mkdir(parents=True, exist_ok=True)
            created.append(f"{slug}/{sub}/")

    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")

    brief = f"""# 题目情报 · {args.title}

| 项 | 内容 |
|---|---|
| 题目名 | {args.title} |
| 分类 | {args.category} |
| 来源 | （比赛/平台/题号） |
| 开工时间 | {now} |
| 附件 | artifacts/ |
| flag 格式 | flag{{...}} |
| 初始假设 | |

## 题面原文

（原样粘贴，不要转述、不要删提示）

## 已知信息 / 提示

-
"""

    journal = f"""# 解题日志 · {args.title}

> 规则：每个步骤一段，边解边写，攒到最后回忆会失真。
> 字段：现象 → 判断 → 工具 → 命令 → 输出 → 解读 → 知识点 → 下一步。
> 失败的命令必须留，那是最贵的教材。

## 阶段 0 · 初筛

### 步骤 1 · 文件指纹与初步判型
- 现象：
- 判断：
- 工具：
- 命令：
```bash
ctf info artifacts/REPLACE_ME
```
- 输出（关键行）：
- 解读：
- 知识点：
- 结论/下一步：
"""

    flag = "# 找到后删掉这一行，只留 flag 本身\nTODO\n"

    if not TEMPLATE.exists():
        readme = FALLBACK_README.replace("{{TITLE}}", args.title)
    else:
        readme = TEMPLATE.read_text(encoding="utf-8")
        readme = (readme.replace("{{TITLE}}", args.title)
                        .replace("{{CATEGORY}}", args.category)
                        .replace("{{DATE}}", now)
                        .replace("{{SLUG}}", slug))

    for name, content in (("00-brief.md", brief), ("journal.md", journal),
                          ("flag.txt", flag), ("README.md", readme)):
        if write_if_absent(base / name, content):
            created.append(f"{slug}/{name}")

    copied = copy_sources(args.src, base / "artifacts") if args.src else []

    print(f"题目录: {base.resolve()}")
    for c in created:
        print(f"  + {c}")
    for c in copied:
        print(f"  附件 -> artifacts/{c}")
    if not created and not copied:
        print("  (目录已完整，未改动)")
    print()
    print("下一步: 先写 00-brief.md 的题面与假设，再从 journal.md 的步骤 1 开始。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
