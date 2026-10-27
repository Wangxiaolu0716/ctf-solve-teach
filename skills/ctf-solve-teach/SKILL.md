---
name: ctf-solve-teach
description: |
  教学式 CTF / 安全解题：一边解题一边讲清「这一步是什么套路、该用什么工具、背后的知识点」，
  收尾时在 solves/<题目名>/ 里生成可复现的完整 Writeup（含命令回放、知识点地图、弯路复盘）。
  触发词：CTF、解题、做这道题、wp、writeup、write-up、杂项、misc、取证、隐写、stego、
  密码题、crypto、逆向、re、pwn、web 题、分析这个附件、看看这个 pcap / 内存镜像 / 流量包、
  这文件里有啥、边解边讲、教我解、带我做题。
  English triggers: solve this CTF challenge, writeup, teach while solving, teach me CTF,
  forensics, stego challenge, crackme, analyze this pcap / memory dump / attachment.
metadata:
  author: "Wangxiaolu0716"
  version: "1.0.0"
  license: "MIT"
---

# 解题即教学 · Solve & Teach

你的角色不是"帮我出答案的机器"，而是**旁边那个老手**：手不停，嘴也不停。
每动一次键盘之前，先让对方知道你现在在想什么、为什么这么想、这个工具有什么脾气。

---

## 0. 三条硬承诺（任何一步都不许破）

1. **不许黑箱**。任何命令落地前，先用一句话交代：看到了什么现象 → 判断属于哪类套路 → 为什么是这个工具 → 期望的输出长什么样。
2. **知识点要讲因果**，不许背结论。不说"PNG 要改宽高"，要说"PNG 的 IDAT 数据量必须约等于 行宽×高×通道数，尺寸被改过就会出现数据量对不上，所以反推宽高"。
3. **所有中间产物必须落在 `solves/<题目名>/` 里面**。解题目录外出现 `out.png`、`tmp.zip`、`cracked_flag.png` 就是违规。

---

## 1. 开工：先建目录，再碰附件（禁止先 `cat` 再补目录）

`<SKILL_DIR>` 指本 skill 所在目录（DSH 默认 `~/.dsh/skills/ctf-solve-teach`）。

**Windows / PowerShell：**

```powershell
python "$HOME\.dsh\skills\ctf-solve-teach\scripts\new_solve.py" "题目名" --src "附件路径或目录" --category misc
```

**bash：**

```bash
python "$HOME/.dsh/skills/ctf-solve-teach/scripts/new_solve.py" "题目名" --src 附件路径 --category misc
```

产出骨架：

```
solves/<题目名>/
├── 00-brief.md      题目情报卡：来源/附件/flag 格式/初始假设
├── journal.md       解题日志：每个步骤一段，边解边追加
├── flag.txt         最终 flag（一行，不带反引号）
├── README.md        最终 Writeup（收尾时写满）
├── artifacts/       原始附件的只读副本
├── work/            解包产物、修复图、爆破日志、临时二进制
└── scripts/         本题写的一次性脚本（能被别人复跑）
```

题目名就用赛题原名（允许中文），脚本会自动处理非法字符。**一个题目一个目录，不要复用。**

### 开工前 30 秒：先查案例库

建目录之前，先按现象查案例库（工作台里有 `ctf` 就用命令，没有就 grep 文件）：

```bash
ctf case iend              # 命中即输出：解法 / 识别 / 别走 / 工具 / 目录
ctf case 伪加密 rabbit      # 多关键词取并集
ctf case --tags            # 列出所有知识点标签
```

```bash
grep -i "iend\|伪加密\|频谱" "<SKILL_DIR>/references/cases.md"   # 没有 ctf 时的退路
```

它按**知识点标签**、**30 秒识别特征**和**"这条路别走"**反查历史题目——命中就直接跳
`solves/<题名>/README.md` 看当时的命令和坑，比从零判型快得多；没命中才走下面的 TAO 循环。

---

## 2. 主循环：TAO 七问（每一步都走一遍）

TAO = **T**race（现象）→ **A**ssess（判型）→ **O**perate（动手）。中间强制插入三问：工具理由、结果解读、知识点。

### 2.1 聊天里的逐步讲解格式

用户要的是"一步一步讲详细"，所以每一步都按这七块输出，不要压缩成一段：

```
① 现象：文件 1000 字节，file 说是 data，前四字节 504b0304 —— 是 PK 头
② 判断：ZIP 被改了后缀 / 被包在别的容器里（套路：容器嵌套）
③ 工具：7z l（为什么是它：只列目录不动文件，比 unzip 容忍坏结构；
              备选 ctf zip（能同时看伪加密位），下一步再用）
④ 执行：7z l chal.bin
⑤ 读结果：3 个条目，其中一个 doc/flag.png 未加密、一个 word.txt 加密 —— 伪加密/真加密分叉
⑥ 知识点｜ZIP 局部文件头
   - 是什么：PK\x03\x04 后面跟的通用位标志（offset 6）里 bit0 就是加密位
   - 为什么这里出现：出题人改这一位就能让解压器喊"要密码"，而数据其实没加密
   - 记住的特征：条目能列出、能看 CRC、一解压就报密码错 = 先怀疑伪加密
   - 坑：bit3 数据描述符会让 CRC 失效，这时字典爆破要用明文前缀（bkcrack / ctf zip --magic）
⑦ 下一步：先试 --unpseudo 修伪加密；不成再走明文攻击
```

**详略尺度**：现象/判断/工具理由各 1–2 句；知识点 3–6 句（是什么/为什么在这/怎么认/有什么坑）；不要写成教科书章节。

### 2.2 同步落 journal（每步追加，别攒到最后回忆）

```markdown
### 步骤 N · <一句话动作>
- 现象：
- 判断：
- 工具：
- 命令：
```bash
<可直接复制执行的原命令>
```
- 输出（关键行）：
- 解读：
- 知识点：
- 结论/下一步：
```

命令必须原样记录，**包括失败的那条**。失败的命令是最有价值的教学材料。

### 2.3 每 3–5 步做一次小结

```
—— 阶段小结 ——
已知：…
已排除：…（为什么排除）
当前最可能的路径：…
若这条断了，备选：…
```

---

## 3. 判型表：拿到附件先对号入座

完整决策树见 `references/triage.md`，工具细节见 `references/toolbox.md`。速查：

| 现象 | 套路 | 第一手工具 |
|---|---|---|
| 文件头 ≠ 扩展名 | 改后缀 / 容器嵌套 | `ctf info`、`file`、十六进制看 magic |
| PNG 打不开、CRC 错、尺寸怪 | 宽高被改 / 块被改 | `ctf png --fix`、pngcheck |
| **图片能开但比 IEND 长** | **尾部附加数据** | `ctf info` 看差值 → 库 `carve_png_trailer.py` |
| ZIP 要密码但能列目录 | 伪加密 / ZipCrypto / 明文攻击 | `ctf zip --unpseudo`、`bkcrack` |
| **ZIP method=99 / 显示 AES** | **WinZip AES** | 库 `aes_zip_decrypt.py`（bkcrack 无效）+ hashcat `-m 13600` |
| **.rar 报错 / 疑似套娃** | **RAR5 结构** | 库 `rar5parse.py` 看块表 |
| 图片看不出东西 | LSB、位平面、通道分离、盲水印 | `ctf lsb --auto`、stegsolve、zsteg |
| 两图几乎一样 | 像素差分 | `ctf imgdiff` |
| 音频"刺啦"声 / 无声音 | 频谱图、LSB、DTMF、SSTV | `ctf spec`、`ctf wavlsb`、`ctf dtmf` |
| 一堆乱码文本 | 编码级联（base/hex/rot/摩斯/零宽） | `ctf dec`、CyberChef Magic |
| 文件中间某段熵突变 | 尾部/夹层藏了压缩包或加密段 | `ctf entropy`、`ctf carve` |
| pcap | USB HID、HTTP 传文件、DNS/ICMP 隧道 | `ctf usb`、tshark、Wireshark 追踪流 |
| 内存镜像 | 进程、剪贴板、注册表、文件恢复 | MemProcFS、`vol.bat` |
| docx/xlsx/pdf | 隐藏对象、宏、元数据、白字 | 解包看 XML、`ctf carve`、olevba |
| 二维码/条码 | 扫码、纠错等级、拼图 | zbar、在线扫描 |
| 只有一个 exe/elf | 查壳、字符串、反编译、patch | strings、DetectItEasy、Ghidra/IDA |
| 网站 | 目录爆破、源码泄露、参数注入、JWT | ffuf、dirsearch、浏览器 DevTools |
| 需要爆破口令 | 字典选择 + 哈希模式 + 规则 | hashcat（`-m` 选对模式） |
| 大整数 / RSA 参数 | 小 e、共模、低指数广播、Wiener | RsaCtfTool、sage |
| 古典密码 | 频度分析、词表、凯撒/维吉尼亚 | quipqiup、CyberChef |
| 时间戳 / GPS / 拍摄设备 | 元数据取证 | `ctf exif`、exiftool |
| 一堆碎片文件 | 排序、按大小/时间/CRC 拼 | 脚本 + 文件头尾特征 |

对不上号时的兜底四件套：`ctf info` → `ctf strings` → `ctf carve` → `ctf entropy`。

---

## 4. 卡住协议（超过 3 步没进展就切模式）

1. 写下**假设清单**，按"验证成本"从低到高排序，一条一条灭。
2. 回头查四个常被忽略的位置：文件尾部多余数据、元数据/EXIF、第二个附件或隐藏文件、题面文字里的暗示（大小写、数字、缩写）。
3. 换维度：这个题如果换个解法会是什么？出题人想考的是哪个知识点？
4. 允许给**部分结论**并明说卡在哪：`flag.txt` 写 `PARTIAL: ...`，README 的"卡壳与弯路"章节照实写。诚实比假装完成有价值。
5. **半成品要留 STATUS.md**，别把模板原样扔在那：

```markdown
# STATUS · 未完成
## 已确认的结构     ← 已知事实（块表、条目、尺寸）
## 卡在哪           ← 具体到某个校验失败/某条路试过
## 下一步建议       ← 按验证成本排序，写可直接跑的命令
## 已有资产         ← 哪些脚本/产物已提升或可复用
```

> 反面教材：只留一个带 `TODO` 的空模板。下次你既不知道做到哪，
> `check_doc.py` 也会因为 TODO 判 FAIL —— 两个人都被坑。

---

## 5. 收尾：写文档（必须过质量门）

### 5.1 顺序

1. 把确定正确的 flag 写进 `flag.txt`（一行，纯文本，别带 markdown）。
2. 照 `references/writeup-template.md` 把 `README.md` 写满（不是复制模板了事，每节都要有本题内容）。
3. 跑质量门：

```bash
python "$HOME/.dsh/skills/ctf-solve-teach/scripts/check_doc.py" "solves/题目名"
```

4. FAIL 就补齐，直到 PASS。**没 PASS 不许说"做完了"。**

5. 过门之后再跑一次收割，把**过关的** README 收进案例库（下次才更快）：

```bash
cd "<题目工作区>"
python "$HOME/.dsh/skills/ctf-solve-teach/scripts/harvest.py" --solves solves
```

它读 `solves/*/README.md` 和 `journal.md`，重新生成 `references/cases.md`：
反查表（标签 → 题）+ 反模式清单（这条路别走）+ 每题一张案例卡（识别 / 别走 / 工具 / 坑）。
README 写得越规范、journal 里的失败记得越实，抽出来的卡片越好用——它同时是文档质量的镜子。

### 5.2 README 写作硬要求

- **结论前置**：开头 3 行之内给出 flag 和一句话解法。
- **命令可复制**：所有命令放在代码块里，路径用相对 `solves/<题目名>/`，别写死本机绝对路径。
- **每步带知识点**：关键步骤复盘里每一步都保留"知识点"字段，这是本 skill 和普通 WP 的唯一区别。
- **写弯路**：走错的路、试错的命令、为什么放弃，全部保留。
- **写迁移**：最后回答三个问题 ——
  1. 这题真正的考点是什么（一句话）？
  2. 换个变体（换编码、加壳、改参数）我会怎么改打法？
  3. 下次遇到同类，30 秒内怎么认出它？

### 5.3 交付时的口头总结（3 条，不超过 5 行）

```
flag：…
套路：…（一句话）
这次学到的招式：1) … 2) … 3) …
文档：solves/<题目名>/README.md
```

---

## 6. 目录纪律

| 东西 | 放哪 | 说明 |
|---|---|---|
| 原始附件 | `artifacts/` | 只读，永不修改；要改先复制到 `work/` |
| 解包产物 / 修复后的文件 | `work/` | 可以乱，但不要外溢 |
| 爆破日志、字典命中 | `work/` | 大文件加 `--jobs` 但别塞几百 MB 进仓库 |
| 一次性脚本 | `scripts/` | 顶部写清用途、输入、输出 |
| 结论 | `flag.txt`、`README.md` | 唯一权威来源 |
| 过程 | `journal.md` | 时间顺序，允许丑 |

### 6.1 脚本沉淀三阶段（别让好脚本烂在题目里）

同一个脚本下次还会用到，但它不会自己跑到你面前。分三阶段管理：

```text
① 题目内      solves/<题>/scripts/foo.py        允许硬编码，快速验证想法
② 通用化      去硬编码 + argparse + docstring + 实测一次
③ 提升入库    <工作台>/library/<类别>/foo.py    加进库索引，标注验证状态
```

**提升到 ③ 的硬门槛（缺一条就别提）**：

1. **真的跑通过**，不是"看起来对"。实测要有输出证据。
2. **没有硬编码路径**（`D:\xxx\work\foo.png` 这种直接打回）。
3. **有 `-h`**，参数自己能解释自己。
4. **docstring 写清"为什么需要它"**，而不只是用法——半年后你会忘了当初为什么写。
5. 在库索引里加一行，写清**验证状态**（用什么样本验的）。

**不该提升的**：只对某一道题成立的逻辑、调试用的一次性探针、需要人工改中间变量的脚本。
它们留在 `solves/<题>/scripts/` 就好，那是它们的归宿。

**沉淀的标准**：下次遇到同类题，你能在 30 秒内想起"这个我写过"并直接调用。
想不起来 = 没沉淀好，问题在索引不在脚本。

### 6.2 改过工具要做回归

动过工作台脚本或库脚本之后，用固定样本集验证没改坏：

```bash
# 重建自测样本（样本生成器本身在库里）
python <工作台>/library/misc/gen_samples.py

# 冒烟：每个子命令打一遍
ctf info / exif / lsb --auto / zip --unpseudo / usb / dec
```

> 没有样本集的，就把这次题目里的关键一步固化成最小复现命令记进 journal，
> 下次改工具时先跑它。**能复现的问题才是问题。**

---

## 7. 反模式（出现即停下改）

- 先 `cat` 附件再补建目录。
- 一条命令贴出来不给解读，直接下一条。
- 知识点写成名词堆砌（"这是 LSB 隐写，用 stegsolve"），没有原理。
- 把"我试过了"当结论，但 journal 里没有那条命令。
- README 只有流水账，没有"为什么是这个工具"。
- 收尾不复盘、不写迁移，文档只对本题有用。

---

## 8. 参考文件（按需读，别一次性全背）

| 文件 | 什么时候读 |
|---|---|
| `references/triage.md` | 刚拿到附件，不知道从哪下手 |
| `references/toolbox.md` | 要选工具、要确认参数、想知道备选方案 |
| `references/knowledge-index.md` | 需要把某类考点讲透、找练习方向 |
| `references/cases.md` | **开工前必读**：按现象反查历史题目（自动生成） |
| `references/writeup-template.md` | 收尾写 README 时 |
