# 🧩 ctf-solve-teach · 解题即教学

> 一个给 AI 用的 Skill：**解 CTF 题的时候不许闷头算答案，必须边解边讲——这一步是什么套路、为什么用这个工具、背后的知识点是什么。**
> 收尾自动在 `solves/<题目名>/` 里产出可复现的完整 Writeup。

[![awesome · DSH plugin](https://awesome-dsh-plugin.com/badge.svg)](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![DSH Plugin](https://img.shields.io/badge/DSH-Plugin-5b8def)
![Agent Skill](https://img.shields.io/badge/Agent-Skill-blue)
![npm](https://img.shields.io/npm/v/dsh-ctf-solve-teach)
![GitHub stars](https://img.shields.io/github/stars/Wangxiaolu0716/ctf-solve-teach?style=flat)

**两种用法**：作为 DSH 插件安装（装完技能自动出现在技能目录），或者把 `skills/ctf-solve-teach/` 整个复制进任意 agent 的 skill 目录。

```bash
dsh plugin add dsh-ctf-solve-teach          # npm 包
dsh plugin add github:Wangxiaolu0716/ctf-solve-teach   # 或直接从仓库装
```

---

## 解决什么问题

用 AI 做 CTF，最常见的两种失败：

1. **一口价答案**。AI 三秒给出 flag，你抄完什么也没学到——下次换个皮还是不会。
2. **流水账 WP**。过程很详细，但没有"为什么用这个工具"，也没有"这个机制为什么存在"，看完只会做这一道题。

这个 Skill 把解题过程强制拆成**七问循环**，每一步都要交代因果；同时用目录契约和质量门，
保证每次都能留下来一份"三个月后自己还看得懂、别人能照着重做"的文档。

---

## 三条硬承诺（Skill 内置约束）

| # | 约束 | 具体表现 |
|---|---|---|
| 1 | 不许黑箱 | 任何命令落地前先说：现象 → 判断属于哪类套路 → 为什么是这个工具 → 期望输出 |
| 2 | 知识点讲因果 | 不说"PNG 改宽高"，要说"IDAT 解压字节数 = (1+宽×通道)×高，所以能反推" |
| 3 | 产物不外溢 | 所有中间文件都落在 `solves/<题目名>/` 里，工作区根目录不许出现 `out.png` |

---

## 每一步长这样

```
① 现象：文件 1000 字节，file 说 data，前四字节 504b0304 —— PK 头
② 判断：ZIP 被改后缀（套路：容器嵌套）
③ 工具：7z l —— 只列目录不动文件，比 unzip 容忍坏结构；备选 ctf zip 能同时看伪加密位，下一步用
④ 执行：7z l chal.bin
⑤ 读结果：3 个条目，doc/flag.png 未加密、word.txt 加密 —— 伪加密/真加密分叉
⑥ 知识点｜ZIP 通用位标志
   - 是什么：PK\x03\x04 后 offset 6 的 bit0 就是加密位
   - 为什么在这：出题人改这一位就能让解压器喊"要密码"，而数据没加密
   - 怎么认：能列条能看 CRC，一解压就报密码错
   - 坑：bit3 数据描述符会让 CRC 失效，爆破要改用明文前缀
⑦ 下一步：先 --unpseudo 修伪加密；不成走明文攻击
```

---

## 产出物长这样

```
solves/真的假的/
├── README.md          ← 最终 Writeup（9 个必备章节）
├── 00-brief.md        ← 题目情报卡：题面原文 / 附件 / flag 格式 / 初始假设
├── journal.md         ← 解题日志：每步七字段，含失败命令
├── flag.txt           ← 一行 flag
├── artifacts/         ← 原始附件只读副本
├── work/              ← 解包产物、修复图、爆破日志
└── scripts/           ← 这次写的一次性脚本（别人能复跑）
```

> `solves/` 已写进 `.gitignore`：解题产物（flag、附件、他人题目内容）不会误提交。

`README.md` 的九个章节是**质量门强制项**（`check_doc.py` 会逐条查）：

1. 题目情报 2. 一句话结论 3. 解题路径 4. 关键步骤复盘
5. 工具与用法清单 6. 知识点地图 7. 卡壳与弯路 8. 可复用脚本 9. 同类题迁移

其中 **第 7 章"卡壳与弯路"** 和 **第 9 章"同类题迁移"** 是最少见的章节，
也是把"会做这道题"变成"会做这一类题"的关键。

---

## 越做越快：经验复用

每道题做完，收尾第 5 步会跑一次 `scripts/harvest.py`。它扫 `solves/*/README.md` 与
`journal.md`，把每道题压成一张卡：

- **反查表**：知识点标签 → 哪些题出现过
- **反模式清单**：这条路别走（来自 journal 里记下的失败分支）
- **案例卡**：解法 / 30 秒识别特征 / 别走 / 工具 / 坑

下次遇到同类题，开工前先查：

```bash
ctf case iend           # 命中即输出：解法、识别特征、别走、工具、题目录
ctf case 伪加密 rabbit    # 多关键词取并集
ctf case --tags         # 列出所有知识点标签
```

`ctf` 是配套 Windows 工作台的 CLI；换环境就 `grep` 同一个 `references/cases.md`。

---

## 安装

本仓库同时是 **DSH 插件**（npm 包 `dsh-ctf-solve-teach`）和 **独立 skill**，按需选一种。

### 方式一：DSH 插件（推荐）

```bash
dsh plugin add dsh-ctf-solve-teach
```

或在插件市场里搜索任一关键词：

```text
ctf    教学式 CTF    writeup    网络安全    取证
```

装完重启 DSH，技能目录里直接出现 `ctf-solve-teach`，不用再手动放文件。

插件的工作方式：`cordis.patch.yml` 把插件插进 profile，插件启动时读包内的
`skills/ctf-solve-teach/SKILL.md`，调用 `ctx.skills.register()` 注册成 runtime skill，
并把 `references/` 与 `scripts/` 作为 `resourceBase` 一起交出去——所以模型读到的是完整技能，
相对路径也能正确解析到示例与脚本。

### 方式二：纯 skill（不装插件，任何 agent 通用）

```bash
git clone https://github.com/Wangxiaolu0716/ctf-solve-teach.git /tmp/cst
cp -r /tmp/cst/skills/ctf-solve-teach ~/.dsh/skills/
```

Claude Code 把目标换成 `~/.claude/skills/`；其他 agent 同理，只要它的 skill 目录认 `SKILL.md`。

### 方式三：本地开发

```bash
git clone https://github.com/Wangxiaolu0716/ctf-solve-teach.git
cd ctf-solve-teach
node --test          # 插件冒烟测试，4 条
npm pack --dry-run   # 看会发布哪些文件
```

---

## 用法

装好之后不用记命令，直接用自然语言触发：

```text
帮我解一下这道杂项题，附件在 D:\ctf\chall.zip
这道流量分析题我的思路卡住了，边解边讲
给我写个 wp，按教学向的那种
```

Agent 会自动：建目录 → 建情报卡 → 逐步解题并讲解 → 收尾写 README → 跑质量门。

### 也可以手动调脚本

```bash
# 建目录骨架（可带附件，会复制进 artifacts/）
python skills/ctf-solve-teach/scripts/new_solve.py "题目名" --src 附件或目录 --category misc

# 交付前自检
python skills/ctf-solve-teach/scripts/check_doc.py "solves/题目名"
```

```bash
# 收尾：把这道题收进案例库（成功/失败都跑）
python skills/ctf-solve-teach/scripts/harvest.py --solves solves

# 收尾：清掉能重建的中间产物（默认只报告，--apply 才删）
python skills/ctf-solve-teach/scripts/prune.py "solves/题目名" --apply
```

`new_solve.py` 是幂等的：目录已存在时只补缺失文件，不会覆盖你写了一半的 README。
`prune.py` 只删 `work/` 里的重货（>64MB）、`node_modules`、重复文件与缓存，
`artifacts/` 原件和 README/journal/flag 一律不动。

---

## 目录结构

```
ctf-solve-teach/                    # npm 包 dsh-ctf-solve-teach
├── package.json                    # 包元数据，dsh.bundle.patch 指向下面的补丁
├── cordis.patch.yml                # 把插件插进 DSH profile 的 4 行补丁
├── plugin/
│   └── index.js                    # 零依赖：读 SKILL.md → ctx.skills.register()
├── test/
│   └── smoke.test.mjs              # 冒烟测试：解析/注册/卸载/frontmatter
└── skills/ctf-solve-teach/         # ← 技能本体，可单独复制进任何 agent
    ├── SKILL.md                    # 三条承诺 + 七问循环 + 判型表 + 纪律
    ├── references/
    │   ├── triage.md               # 60 秒判型决策树（按附件类型分流）
    │   ├── toolbox.md              # 工具库：用途/命令/备选/何时别用
    │   ├── knowledge-index.md      # 知识点索引（ID 化，含深水区展开）
    │   └── writeup-template.md     # README 模板
    ├── scripts/
    │   ├── new_solve.py            # 建目录骨架
    │   ├── check_doc.py            # 交付质量门（九章）
    │   ├── harvest.py              # 收割案例库 cases.md
    │   └── prune.py                # 收尾清理中间产物
    └── examples/                   # 真实跑通、已过质量门的示例
```

### 插件是怎么工作的（60 行代码）

`package.json` 里的 `dsh.bundle.patch` 指向 `cordis.patch.yml`，DSH 安装时读这段补丁把插件挂进 profile：

```yaml
- insert:
    - id: ctf-solve-teach
      name: 'dsh-ctf-solve-teach'
      config: {}
```

插件启动后只做三件事：读 `SKILL.md`、剥掉 frontmatter、调 `ctx.skills.register()`。
同一份内容在插件里注册一次，文件系统 provider 那边就不用再放一份——runtime skill 优先级高于 user 层。

---

## 设计原则

- **教学优先**：宁可多花 30 秒解释工具选型，也不要快进到答案。
- **可复现**：命令原样保留，路径相对化，脚本进 `scripts/`。
- **诚实**：做不出来就写 `PARTIAL: ...`，并在"卡壳与弯路"里说清卡在哪。
- **不绑平台**：判型表和工具箱按"能力"组织，本地工具（`ctf` CLI）只是示例，换环境照用。

---

## English

A teaching-first CTF skill for AI agents. Instead of dumping the flag, the agent
narrates every step — what pattern this is, why this tool, what the underlying
mechanism is — and finally writes a reproducible writeup into
`solves/<challenge-name>/` with a 9-section checklist enforced by `check_doc.py`.

Two install paths:

1. **DSH plugin** — npm package `dsh-ctf-solve-teach`. It ships `cordis.patch.yml` and
   registers the skill on `ctx.skills` at load time; nothing to copy by hand.
2. **Plain skill** — copy `skills/ctf-solve-teach/` into your agent's skill folder
   (`~/.dsh/skills/`, `~/.claude/skills/`, …).

Trigger with "solve this CTF challenge" or "teach me while solving".

---

## License

MIT © Wangxiaolu0716
