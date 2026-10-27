#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prune.py - 收尾清理：删掉能重建的中间产物，只留核心件。

默认只报告（dry-run），加 --apply 才真的删。

用法:
    python prune.py solves/*                 # 看一眼会删什么
    python prune.py solves/某题 --apply      # 真删
    python prune.py solves --apply --max-work-mb 32

保留（永不删）：
    README.md / journal.md / 00-brief.md / flag*.txt / scripts/ 下的自写脚本

删除：
    1. 缓存：__pycache__、*.pyc、.DS_Store、Thumbs.db、*.tmp、*.part
    2. work/ 里的 node_modules（npm 可重装）
    3. artifacts/ 内的完全重复文件（同 sha256 留一个，优先干净文件名）
    4. work/ 里与 artifacts/ 完全相同的副本
    5. work/ 里超过 --max-work-mb 的单个文件（中间产物，可由原件重建）
    6. 空文件与空目录

不删 artifacts/ 里的原件——那是唯一来源。
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

NOISE_DIRS = {"__pycache__", ".ipynb_checkpoints", ".pytest_cache"}
NOISE_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}
NOISE_SUFFIX = {".pyc", ".pyo", ".tmp", ".part", ".swp", ".bak"}
KEEP_NAMES = {"README.md", "journal.md", "00-brief.md", "flag.txt"}


def is_core(p: Path) -> bool:
    if p.name in KEEP_NAMES:
        return True
    return p.name.lower().startswith("flag")


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def clean_name(s: str) -> tuple:
    """优先保留不带 _1 / (1) / copy 这类后缀的名字。"""
    noisy = any(t in s for t in ("_1", "(1)", " copy", "_copy", "-副本"))
    return (noisy, len(s), s)


def plan(solve: Path, max_work_mb: int):
    deletes = []   # (path, reason, size)
    if not solve.is_dir():
        return deletes

    # 1/2. 噪声 + node_modules
    for p in solve.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(solve)
        if any(part in NOISE_DIRS or part == "node_modules" for part in rel.parts):
            if not is_core(p):
                deletes.append((p, "缓存/可重装", p.stat().st_size))
            continue
        if p.name in NOISE_FILES or p.suffix in NOISE_SUFFIX:
            if not is_core(p):
                deletes.append((p, "系统/临时文件", p.stat().st_size))

    deleted = {str(p) for p, _, _ in deletes}

    # 3. artifacts 去重
    art = solve / "artifacts"
    if art.is_dir():
        by_hash = {}
        for p in sorted(art.rglob("*")):
            if not p.is_file() or str(p) in deleted:
                continue
            by_hash.setdefault(sha256(p), []).append(p)
        for h, files in by_hash.items():
            if len(files) < 2:
                continue
            files.sort(key=lambda x: clean_name(x.name))
            for dup in files[1:]:
                deletes.append((dup, "与 %s 重复" % files[0].name, dup.stat().st_size))
                deleted.add(str(dup))

    # 4/5. work 里可重建的大件与副本
    work = solve / "work"
    art_hashes = {}
    if art.is_dir():
        for p in art.rglob("*"):
            if p.is_file() and str(p) not in deleted:
                art_hashes.setdefault(sha256(p), p.name)
    if work.is_dir():
        for p in sorted(work.rglob("*")):
            if not p.is_file() or str(p) in deleted or is_core(p):
                continue
            size = p.stat().st_size
            if size == 0:
                deletes.append((p, "空文件", 0))
                continue
            if max_work_mb > 0 and size >= max_work_mb * 1024 * 1024:
                deletes.append((p, "中间产物 >%dMB，可由原件重建" % max_work_mb, size))
                continue
            if size < 200 * 1024 * 1024 and sha256(p) in art_hashes:
                deletes.append((p, "与 artifacts/%s 相同" % art_hashes[sha256(p)], size))

    # 6. 空目录
    for d in sorted(solve.rglob("*"), key=lambda x: -len(x.parts)):
        if d.is_dir() and d.name not in ("artifacts", "work", "scripts") and not any(d.iterdir()):
            deletes.append((d, "空目录", 0))
    return deletes


def main():
    ap = argparse.ArgumentParser(description="收尾清理：只留核心件")
    ap.add_argument("paths", nargs="+", help="题目录或 solves 目录")
    ap.add_argument("--apply", action="store_true", help="真的删除（默认只报告）")
    ap.add_argument("--max-work-mb", type=int, default=64, help="work/ 单文件上限，0 关闭")
    args = ap.parse_args()

    targets = []
    for raw in args.paths:
        p = Path(raw)
        if p.is_dir() and (p / "artifacts").is_dir():
            targets.append(p)
        elif p.is_dir():
            targets.extend([d for d in sorted(p.iterdir())
                            if d.is_dir() and (d / "artifacts").is_dir()])
        else:
            print("跳过（不是题目录）: %s" % p, file=sys.stderr)

    total = 0
    rows = []
    for solve in targets:
        items = plan(solve, args.max_work_mb)
        if not items:
            continue
        freed = sum(s for _, _, s in items)
        total += freed
        rows.append((solve, items, freed))

    if not rows:
        print("没有可清理的内容。")
        return 0

    for solve, items, freed in rows:
        print("\n[%s] 删 %d 项，释放 %.1f MB" % (solve, len(items), freed / 1048576))
        for p, reason, size in sorted(items, key=lambda x: -x[2])[:8]:
            print("  - %-52s %7.1f MB  %s" % (str(p.relative_to(solve))[:52], size / 1048576, reason))
        if len(items) > 8:
            print("  ... 另有 %d 项" % (len(items) - 8))

    print("\n合计：%d 个题目录，%d 项，释放 %.1f MB" % (len(rows), sum(len(r[1]) for r in rows), total / 1048576))

    if not args.apply:
        print("\n[dry-run] 没有删除。确认后加 --apply 执行。")
        return 0

    removed = 0
    for _, items, _ in rows:
        for p, _, _ in items:
            try:
                if p.is_dir():
                    p.rmdir()
                else:
                    p.unlink()
                removed += 1
            except OSError as e:
                print("  删除失败 %s: %s" % (p, e), file=sys.stderr)
    print("\n已删除 %d 项，释放 %.1f MB" % (removed, total / 1048576))
    return 0


if __name__ == "__main__":
    sys.exit(main())
