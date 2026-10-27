# 案例库（自动生成，勿手改）

> 由 `scripts/harvest.py` 从 `solves/*/README.md` 抽取，做完新题跑一次即更新。
> **开工前先按现象搜一遍**：同类题直接跳对应目录看 README，比从零判型快。

共 17 个案例，覆盖 2 类。

## 反查表（按知识点标签）

| 标签 | 出现过的题 |
|---|---|
| `ARC-05` | misc2-rar |
| `ARC-06` | welcome2 |
| `ARC-07` | photo-rar |
| `ATT-05` | rsa-small-d |
| `BOOT-01` | file-floppy |
| `BOOT-02` | file-floppy |
| `COD-11` | 07 |
| `COD-12` | 07, 08 |
| `COD-13` | 08 |
| `COD-20` | misc2-rar |
| `CODE-03` | photo-rar |
| `CRY-01` | crypto06 |
| `CRY-02` | crypto06 |
| `CRY-03` | crypto06 |
| `CRY-04` | crypto06 |
| `CRY-05` | crypto06 |
| `CRY-06` | crypto06 |
| `CRY-09` | misc2-rar |
| `CTX-01` | cangbaoge |
| `DOC-03` | photo-rar |
| `ENC-07` | misc2-rar |
| `ENC-08` | welcome2 |
| `ENC-09` | welcome2 |
| `ENC-11` | crypto2 |
| `ENC-12` | crypto3 |
| `ENC-13` | crypto3 |
| `ENC-14` | crypto3 |
| `ESL-01` | welcome2 |
| `ESL-02` | welcome2 |
| `FLP-01` | file-floppy |
| `FLP-02` | file-floppy |
| `FMT-01` | 07, 08, cangbaoge, vm-106-disk |
| `FMT-02` | cangbaoge |
| `FMT-03` | cangbaoge, gz-bf87ed29, rar附件1 |
| `FMT-04` | cangbaoge |
| `FMT-05` | cangbaoge |
| `FS-01` | vm-106-disk |
| `FS-02` | vm-106-disk |
| `FS-03` | vm-106-disk |
| `FS-04` | vm-106-disk |
| `FS-05` | vm-106-disk |
| `FS-06` | vm-106-disk |
| `FS-07` | vm-106-disk |
| `FS-08` | vm-106-disk |
| `GFX-01` | file-floppy |
| `GFX-02` | file-floppy |
| `IMG-01` | png-25-pieces |
| `IMG-02` | png-25-pieces |
| `IMG-03` | png-25-pieces |
| `IMG-04` | png-25-pieces |
| `IMG-05` | png-25-pieces |
| `IMG-07` | photo-rar |
| `JS-04` | crypto2 |
| `NUM-06` | rsa-small-d |
| `NUM-07` | rsa-small-d |
| `OBS-03` | crypto2 |
| `OCR-01` | cangbaoge |
| `PNG-04` | misc2-rar |
| `PNG-05` | welcome2 |
| `PNG-06` | welcome2 |
| `RSA-01` | rsa-small-d |
| `RSA-02` | rsa-small-d |
| `SAFE-01` | crypto2 |
| `SAFE-02` | crypto3 |
| `SIG-02` | crypto2 |
| `SIG-04` | crypto3 |
| `STEG-01` | png-25-pieces, vm-106-disk |
| `STEG-02` | png-25-pieces |
| `STG-01` | cangbaoge, flag-jpg |
| `STG-02` | cangbaoge, flag-jpg |
| `STG-03` | cangbaoge, flag-jpg |
| `STG-04` | flag-jpg |
| `STG-05` | file-floppy |
| `SUD-01` | png-25-pieces |
| `SUD-02` | png-25-pieces |
| `VER-03` | 07, 08 |
| `VIRT-01` | vm-106-disk |
| `VIRT-02` | vm-106-disk |
| `ZIP-01` | download |
| `ZIP-02` | download |
| `ZIP-03` | download |
| `ZIP-04` | download |
| `ZIP-05` | download |
| `ZIP-06` | misc2-rar |

## 按分类

### crypto

| 题目 | 一句话解法 | 关键工具 |
|---|---|---|
| crypto06 | `Salted__` 头 + 非块整数倍长度 → 流密码；密钥提示"加密方式名" → 试 `Rabbit`；真正命中靠 **`RabbitLegacy`** 变体。 | `7z x` / `xxd` / `Python 取模` / `openssl enc -ciphers` / `scripts/cryptojs_rabbit.py` / `crypto-js RabbitLegacy` |
| crypto2 | JSFuck 编码的自执行表达式，`Function("return eval")()` 掏出 eval 后打印 flag；用 `vm` 注入 `console` 跑一次即得。 | `7z l / 7z x` / `tr+fold+sort -u` / `node + vm` / `Proxy Hook` / `Python 计数脚本` |
| crypto3 | 颜文字版 JS 混淆（AAEncode），本质是可执行代码；受控执行即得 flag，无需手写解码器。 | `scripts/kali.py pull` / `7z l` / `ctf info` / `tail -c + Python 计数` / `node + vm` / `Proxy Hook` |
| rsa-small-d | 由 `ed ≡ 1 (mod φ(n))` 直接求模逆，`d = 594420748649`。 | `pow(e,-1,phi)` / `scripts/rsa_small_d.py` / `内联 Python` / `手写 egcd` |

### misc

| 题目 | 一句话解法 | 关键工具 |
|---|---|---|
| 07 | Ook! → Brainfuck → 解释执行，38 字节输出就是 flag。 | `7z` / `xxd` / `scripts/ook.py` |
| 08 | `08.txt` 就是 Brainfuck 程序，跑一遍即得 flag。 | `7z` / `xxd` / `scripts/bf.py` |
| cangbaoge | 用 16 进制定位 `IEND` 结束偏移（745648）与文件实际大小（827432）的 81784 字节差值， | `ctf info` / `ctf png` / `xxd` / `Python zipfile` / `PIL crop/resize` / `numpy` |
| download | 中央目录伪造了加密位，清除后免密解压得到 flag。 | `xxd` / `7z l` / `python zipfile` / `scripts/dump_headers.py` / `ctf zip --unpseudo` |
| file-floppy | 启动软盘镜像看屏幕，或静态解码内核绘制的字形指针，得到 `flag{ctfshow}`。 | `7z` / `file` / `Python + struct` / `capstone` / `decode_message.py` / `render_font.py` |
| flag-jpg | `Jphswin.exe`（JPHS 0.5）空口令 Seek `flag.jpg`，隐藏文件 38 字节： | `stegdetect` / `stegbreak` / `jpseek 0.3` / `Jphswin.exe（JPHS 0.5）` / `wine32 + Xvfb` / `xdotool` |
| gz-bf87ed29 | （30 字以内说清"用什么方法拿到了什么"） | - |
| misc2-rar | 逐层口令：`2020`（doc）→ `welcome_to_payhelp`（RAR hint）→ `hello 2020!`（RAR flag）。 | `7z` / `rar5parse.py` / `python zipfile` / `fix_png_height.py` / `decode_hint.py` / `crypto-js + rabbit_legacy.js` |
| photo-rar | EXIF `XPComment=little stars` → doc 口令；doc 白色文字 `Hello friend!` → flag.png 口令；QR 内容即 flag。 | `file` / `7z` / `ctf exif` / `Pillow getexif` / `olefile + doc_text.py` / `pyzbar + qr_decode.py` |
| png-25-pieces | - | `zipfile` / `Pillow` / `自写 ASCII 降采样` / `行/列覆盖率剖面` / `scripts/grid_glyphs.py` / `scripts/digits.py` |
| rar附件1 | （30 字以内说清"用什么方法拿到了什么"） | - |
| vm-106-disk | - | `python zipfile` / `scripts/qcow2raw.py` / `mmap 魔数扫描` / `7z l` / `scripts/ext4dump.py` / `zlib.decompressobj(31)` |
| welcome2 | `welcome.png` 的 IEND 后附 ZIP，PNG 注释给 7z 口令，`thienc.txt` 是双层 hex，`secenc.txt` 是 Base64/32 循环，最后是 Ook! 标点 + 两段 BF | `ctf info` / `xxd` / `dd` / `7z` / `parse_thienc.py` / `decode_secenc.py` |

## 案例卡

### 07

- 分类：misc
- 解法：Ook! → Brainfuck → 解释执行，38 字节输出就是 flag。
- flag：`flag{b615c4b79a1aede83b9ae67104ff4eb5}`
- 知识点：`FMT-01`、`COD-11`、`COD-12`、`VER-03`
- 工具：`7z` / `xxd` / `scripts/ook.py`
- 30 秒识别：
  - 文本只由 2–3 个固定单词反复组合 → 先想 esolang（Ook!/Cow/Whitespace）。
  - 文本只有空格、制表符、换行 → Whitespace。
  - 大量 `+-><.,[]` 字符 → 直接是 Brainfuck，上解释器即可。
  - 如果换成 Cow 语言 → 同一套思路，换映射表（`moo` 系列关键字）。
- 坑：一上来想用 ctf dec 自动解码；映射表选择

### 08

- 分类：misc
- 解法：`08.txt` 就是 Brainfuck 程序，跑一遍即得 flag。
- flag：`flag{99754106633f94d350db34d548d6091a}`
- 知识点：`FMT-01`、`COD-12`、`COD-13`、`VER-03`
- 工具：`7z` / `xxd` / `scripts/bf.py`
- 30 秒识别：
  - 文本只有 `+-<>.,[]`（可能夹空格）→ Brainfuck，直接跑。
  - 只有 `Ook.`/`Ook?`/`Ook!` 成对出现 → Ook!，先翻译成 BF（见 07 题）。
  - 只有空格/制表/换行三种可见空白 → Whitespace，需可视化后再解析。
  - 如果 BF 里带 `,` 输入 → 先看题面是否给了输入串，否则按 0/EOF 试跑。
- 坑：一开始没意识到空格是注释

### cangbaoge

- 分类：misc
- 解法：用 16 进制定位 `IEND` 结束偏移（745648）与文件实际大小（827432）的 81784 字节差值，
- flag：`flag{haobachang-17231678231427890}`
- 知识点：`FMT-01`、`FMT-02`、`FMT-03`、`FMT-04`、`FMT-05`、`STG-01`、`STG-02`、`STG-03`、`OCR-01`、`CTX-01`
- 工具：`ctf info` / `ctf png` / `xxd` / `Python zipfile` / `PIL crop/resize` / `numpy`
- 30 秒识别：
  - **如果尾部不是 ZIP 而是另一张图**（`\x89PNG` / `\xFF\xD8\xFF`）→ 按偏移 `dd` 切出，
  - **如果 ZIP 带密码但能列目录** → 先看 `flag_bits` 判伪加密（`ctf zip --unpseudo`）；
  - **如果尾部数据被截断、`zipfile` 报 BadZipFile** → 用 `7z x` 或按局部头
  - **如果 IEND 前后都干净、CRC 还全对** → 转攻像素域：`ctf lsb --auto`、
- 坑：内部图 83KB 偏大；一度想直接跑 binwalk；担心数字串看错

### crypto06

- 分类：crypto
- 解法：`Salted__` 头 + 非块整数倍长度 → 流密码；密钥提示"加密方式名" → 试 `Rabbit`；真正命中靠 **`RabbitLegacy`** 变体。
- flag：`flag{a8db1d82db78ed452ba0882fb9554fc9}`
- 知识点：`CRY-01`、`CRY-02`、`CRY-03`、`CRY-04`、`CRY-05`、`CRY-06`
- 工具：`7z x` / `xxd` / `Python 取模` / `openssl enc -ciphers` / `scripts/cryptojs_rabbit.py` / `crypto-js RabbitLegacy`
- 30 秒识别：
  - **换成 AES 加密** → 长度必是 16 倍数；用 `openssl enc -d -aes-256-cbc -a -k <pw>` 一行搞定。
  - **换成 crypto-js AES** → 注意它默认 CBC + Pkcs7 + EvpKDF(md5)，与 openssl 默认一致，可互通。
  - **换成无 salt 的密文** → `Salted__` 不存在，KDF 直接 `MD5(pass)` 或 `MD5(pass+salt)`。
  - **换成 3DES** → 长度必是 8 倍数；crypto-js 里叫 `TripleDES`。
- 坑：判型；步骤 3；步骤 4

### crypto2

- 分类：crypto
- 解法：JSFuck 编码的自执行表达式，`Function("return eval")()` 掏出 eval 后打印 flag；用 `vm` 注入 `console` 跑一次即得。
- flag：`flag{3e858ccd79287cfe8509f15a71b4c45d}`
- 知识点：`ENC-11`、`SIG-02`、`JS-04`、`SAFE-01`、`OBS-03`
- 工具：`7z l / 7z x` / `tr+fold+sort -u` / `node + vm` / `Proxy Hook` / `Python 计数脚本`
- 30 秒识别：
  - **换成 `aaa` 风格（AAEncode）** → 同样是"可执行文本"，但混入日文假名/颜文字，`vm` 跑之前要先剥掉外层 `(ﾟ∀ﾟ)` 调用；hook 手段不变。
  - **换成 JJEncode** → 形如 `$=~[]`，本质仍是 JS，node 直跑；如果报 `$ is not defined` 就用 `vm.runInThisContext` 而非新 context。
  - **加了字符串混淆 / 反调试** → 保留 `hook_jsfuck.js` 的 Proxy 思路，把 `eval`、`Function`、`setTimeout`、`atob` 一起挂 Proxy，一次性把"动态生成的代码"全打出来。
  - **附件变成 pcap / 内存镜像** → 先找浏览器 `console` 输出或剪贴板；这类题的 flag 常常就躺在 `console.log` 的抓包里。
- 坑：步骤 3 拿到 undefined；判型第一反应

### crypto3

- 分类：crypto
- 解法：颜文字版 JS 混淆（AAEncode），本质是可执行代码；受控执行即得 flag，无需手写解码器。
- flag：`flag{js_da_fa_hao}`
- 知识点：`ENC-12`、`ENC-13`、`ENC-14`、`SIG-04`、`SAFE-02`
- 工具：`scripts/kali.py pull` / `7z l` / `ctf info` / `tail -c + Python 计数` / `node + vm` / `Proxy Hook`
- 30 秒识别：
  - **换成 JJEncode** → 打法不变，但 `vm` 新 context 下 `$` 未定义会报错；改用 `vm.runInThisContext` 或在 context 里预置 `$`。
  - **换成多层嵌套（AA 套 AA / AA 套 base64）** → 不手动解；写个循环：跑一次 → 看 `FUNC-APPLY` 拿到的源码 → 若还是混淆就再跑一次，直到出现可读代码。
  - **加反调试（`debugger` 死循环 / `console` 重定义）** → 在 `vm` 里把 `console` 换成自己的收集器（本脚本已这么做），`debugger` 对 `vm` 无效。
  - **换成 Python 的马（Opcode / pickle 混淆）** → 思路一致：先看它"想执行什么"，用 AST 或 `dis` 而非直接 `exec`。
- 坑：建目录时 $HOME 展开；RESULT: undefined；内层 \143\157...

### download

- 分类：misc
- 解法：中央目录伪造了加密位，清除后免密解压得到 flag。
- flag：`flag{79ddfa61bda03defa7bfd8d702a656e4}`
- 知识点：`ZIP-01`、`ZIP-02`、`ZIP-03`、`ZIP-04`、`ZIP-05`
- 工具：`xxd` / `7z l` / `python zipfile` / `scripts/dump_headers.py` / `ctf zip --unpseudo`
- 30 秒识别：
  - 能列目录、能看到原始大小，一解压就报"要密码" → 伪加密，先看 flag 位。
  - 压缩后大小 ≈ 原始大小甚至略大，且 method=8 → 不像 AES（AES 会明显膨胀并有 method=99）。
  - 目录名/文件名在暗示"密码""忘记" → 基本可以确定不用爆破。
  - 如果真 ZipCrypto（清位后 CRC 错）→ `bkcrack` 已知明文攻击，或 `ctf zip --crack rockyou.txt --jobs 16`。
- 坑：7z l 显示 38→40；文件名乱码

### file-floppy

- 分类：misc
- 解法：启动软盘镜像看屏幕，或静态解码内核绘制的字形指针，得到 `flag{ctfshow}`。
- flag：`flag{ctfshow}`
- 知识点：`FLP-01`、`FLP-02`、`BOOT-01`、`BOOT-02`、`GFX-01`、`GFX-02`、`STG-05`
- 工具：`7z` / `file` / `Python + struct` / `capstone` / `decode_message.py` / `render_font.py`
- 30 秒识别：
  - 附件解压后是 1,474,560 B（或 720KB/2.88MB）→ 软盘镜像，先看 0x00 是否 `EB xx 90` + `FAT12`。
  - 文件系统里没有可疑文件、卷标/文件名像提示（`flagnothere`）→ 想"启动后会发生什么"。
  - 内核/引导里有大量 `push 0x0031xxxx` → 字库指针，直接换算字符。
  - 如果画的是像素图而不是文字 → 用 Unicorn/QEMU 跑内核，dump `0xA0000` 显存，或直接解析绘图数据。
- 坑：先入为主找隐藏文件；反汇编偏移错位；一度把 flag{ctfshow} 当 decoy

### flag-jpg

- 分类：misc
- 解法：`Jphswin.exe`（JPHS 0.5）空口令 Seek `flag.jpg`，隐藏文件 38 字节：
- flag：`flag{3c87fb959e5910b40a04e0491bf230fb}`
- 知识点：`STG-01`、`STG-02`、`STG-03`、`STG-04`
- 工具：`stegdetect` / `stegbreak` / `jpseek 0.3` / `Jphswin.exe（JPHS 0.5）` / `wine32 + Xvfb` / `xdotool`
- 30 秒识别：
  - `stegdetect -t p` 报 `jphide(***)` → 先找 Windows JPHS，不要只试 Linux `jpseek`。
  - `stegbreak -c` 能解析出 `bits`/`iv` → 图里确实有 JPHide 数据。
  - `jpseek` 只说 `Nothing done` 而不是 `Pass phrase wrong` → 大概率是空口令被 CLI 拒绝。
  - 如果换成 v3 图 → Linux `jpseek` 可用，但仍要避开空口令。
- 坑：jpseek 输出随机 31 KB；自写 v5 提取器；猜口令

### gz-bf87ed29

- 分类：misc
- 解法：（30 字以内说清"用什么方法拿到了什么"）
- 知识点：`FMT-03`
- 30 秒识别：
  - 如果换成 …… 编码 → 我会先 ……
  - 如果加了壳 → 我会先 ……
  - 如果附件变成流量包 → 我会先 ……

### misc2-rar

- 分类：misc
- 解法：逐层口令：`2020`（doc）→ `welcome_to_payhelp`（RAR hint）→ `hello 2020!`（RAR flag）。
- flag：`flag{g00d_f0r_y0u}`
- 知识点：`ARC-05`、`ZIP-06`、`PNG-04`、`COD-20`、`CRY-09`、`ENC-07`
- 工具：`7z` / `rar5parse.py` / `python zipfile` / `fix_png_height.py` / `decode_hint.py` / `crypto-js + rabbit_legacy.js`
- 30 秒识别：
  - RAR/ZIP 里同时有 `hint.txt`、`flag.txt`、另一个压缩包 → 多阶段口令链，先找未加密的那层。
  - PNG 能列出块但解码器报错/尺寸异常 → 先算 `len(zlib)/stride`，怀疑高度被改。
  - 文档里出现 ♭‖♯♬♩♫ → 音乐符号密码；`U2FsdGVkX1` + 非块长度 → 流密码（Rabbit/RC4）。
  - 注释同时出现年份和 `rat?or?` → 试 Rabbit 的两个变体。
- 坑：先用 2020 解 RAR；PIL 打不开 PNG；看到 IEND 后的 flag{flag_1s_n0t_h3r3}

### photo-rar

- 分类：misc
- 解法：EXIF `XPComment=little stars` → doc 口令；doc 白色文字 `Hello friend!` → flag.png 口令；QR 内容即 flag。
- flag：`flag{welcome_to_ctfshow}`
- 知识点：`ARC-07`、`IMG-07`、`DOC-03`、`CODE-03`
- 工具：`file` / `7z` / `ctf exif` / `Pillow getexif` / `olefile + doc_text.py` / `pyzbar + qr_decode.py`
- 30 秒识别：
  - 无后缀附件 + `file` 报 RAR/ZIP → 先 `7z l`，看哪些条目免密。
  - 图片免密、文档/压缩包加密 → 图片的 EXIF/注释里通常有第一个口令。
  - Word 里"空白" → 改字体颜色/直接读 `WordDocument` 流。
  - 拿到纯黑白方图 → 先 `pyzbar`，再考虑隐写。
- 坑：直接 7z x 全包；doc 解出 0 字节；只 strings 看 doc

### png-25-pieces

- 分类：misc
- 解法：-
- flag：`flag{392756418418392576657841293586139742129478635734265981273584169945613827861927354}`
- 知识点：`IMG-01`、`IMG-02`、`IMG-03`、`IMG-04`、`IMG-05`、`SUD-01`、`SUD-02`、`STEG-01`、`STEG-02`
- 工具：`zipfile` / `Pillow` / `自写 ASCII 降采样` / `行/列覆盖率剖面` / `scripts/grid_glyphs.py` / `scripts/digits.py`
- 30 秒识别：
  - 换成**棋盘/格子更小**（如 5×5）→ 同样的“覆盖率剖面 + bbox 归一化聚类”直接可用，卷积/OCR 都不必要。
  - 换成**彩色网格**（每格涂不同颜色）→ 把聚类键从“点阵”换成“颜色值”，其余流程不变。
  - 换成**帧数不够覆盖**（比如只给 5 帧，总有格子从未显示）→ 这时必须动用数独约束求解（把未知格留 0 交给求解器），而不是并集。
  - 换成**掩码真的承载消息**（作者故意编码）→ 位流可打印率会显著高于 0.4，或出现互补对；这时按帧序/行列序扫一遍就能出文本。
- 坑：无视觉模型看不了图；第一次聚类出 57 种字形；模板指纹全落空（全 ?）

### rar附件1

- 分类：misc
- 解法：（30 字以内说清"用什么方法拿到了什么"）
- 知识点：`FMT-03`
- 30 秒识别：
  - 如果换成 …… 编码 → 我会先 ……
  - 如果加了壳 → 我会先 ……
  - 如果附件变成流量包 → 我会先 ……

### rsa-small-d

- 分类：crypto
- 解法：由 `ed ≡ 1 (mod φ(n))` 直接求模逆，`d = 594420748649`。
- flag：`flag{594420748649}`
- 知识点：`RSA-01`、`RSA-02`、`NUM-06`、`NUM-07`、`ATT-05`
- 工具：`pow(e,-1,phi)` / `scripts/rsa_small_d.py` / `内联 Python` / `手写 egcd`
- 30 秒识别：
  - **只给 n 和 e** → 先 factordb 查库；查不到再 yafu/ecm；`n` 若由两个近素数构成用 **Fermat 分解**（本题 p、q 差得远，Fermat 反而慢）。
  - **给 n, e, c，要求明文** → 先算 d（若 p、q 可得），再 `m = pow(c, d, n)`；若只给 n、e，则看是否属于低指数/共模/广播三类。
  - **p 或 q 其实是合数** → `φ=(p-1)(q-1)` 立刻失效，往返验证会失败；此时要用真实 φ，或先分解 p、q。
  - **要求"第二小的 d"** → `d2 = d + φ`；本题场景下即 `594420748649 + 918650247912`。
- 坑：可疑点；q = 2053 比 p 小 5 个数量级；e = 17 很小

### vm-106-disk

- 分类：misc
- 解法：-
- flag：`flag{c28c424b-fd8c-45b9-b406-0a933b1ca7b1}`
- 知识点：`VIRT-01`、`VIRT-02`、`FS-01`、`FS-02`、`FS-03`、`FS-04`、`FS-05`、`FS-06`、`FS-07`、`FS-08`、`STEG-01`、`FMT-01`
- 工具：`python zipfile` / `scripts/qcow2raw.py` / `mmap 魔数扫描` / `7z l` / `scripts/ext4dump.py` / `zlib.decompressobj(31)`
- 30 秒识别：
  - 换成 **VMDK/VHDX**：思路一样，但 VMDK 要处理 descriptor + extent（`qemu-img convert` 最省事），VHDX 有 BAT 表 + 日志；本机无 qemu 时同理自写解析。
  - 换成 **LUKS 加密卷**：签名扫描会命中 `LUKS\xba\xbe`，先做 header 分析（`cryptsetup luksDump`），再谈口令（字典 / `hashcat -m 14600`）。
  - 换成 **Windows 磁盘（NTFS）**：删除恢复看 `$MFT` 记录里的 `$FILE_NAME`、`$DATA` 的 runlist，工具换 `MFTECmd`/`photorec`；"文件名字在但内容没了"的等价物是 MFT 记录被标记为未使用。
  - 换成 **ext4 journal 里翻旧 extent**：若数据块被覆盖，还能回放 `journal`（inode 8，16 MiB）里的旧 `ext4_extent` 事务；本题 journal 全零（挂载后没做过写操作），所以没走这条路。
- 坑：找分区表；看到 4 个 ext 魔数；7z l 只有 Journal

### welcome2

- 分类：misc
- 解法：`welcome.png` 的 IEND 后附 ZIP，PNG 注释给 7z 口令，`thienc.txt` 是双层 hex，`secenc.txt` 是 Base64/32 循环，最后是 Ook! 标点 + 两段 BF。
- flag：`flag{Welc0me_tO_cTf_3how!}`
- 知识点：`PNG-05`、`PNG-06`、`ARC-06`、`ENC-08`、`ENC-09`、`ESL-01`、`ESL-02`
- 工具：`ctf info` / `xxd` / `dd` / `7z` / `parse_thienc.py` / `decode_secenc.py`
- 30 秒识别：
  - 图片 IEND 后还有大量数据 → 先 `dd` 切尾巴，按 `PK`/`Rar!`/`7z` 魔数判断类型。
  - PNG 有 `tEXt Comment`/`zTXt`/`iTXt` → Base64/Base32 试一遍。
  - 文本是 `0x` 开头、长度不是 4 的倍数 → 变长 `0xHH`，按 `0x` split。
  - 文本只含三种标点、长度偶数 → 想 Ook!/BF 变体。
- 坑：thienc.txt 解析；.!? 文本；BF 第一段输出
