# 案例库（自动生成，勿手改）

> 由 `scripts/harvest.py` 从 `solves/*/README.md` 抽取，做完新题跑一次即更新。
> **开工前先按现象搜一遍**：同类题直接跳对应目录看 README，比从零判型快。

共 26 个案例，覆盖 3 类。

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
| `CRY-01` | Misc-03, catcatcat, crypto06 |
| `CRY-02` | Misc-03, catcatcat, crypto06 |
| `CRY-03` | crypto06 |
| `CRY-04` | crypto06 |
| `CRY-05` | crypto06 |
| `CRY-06` | crypto06 |
| `CRY-09` | misc2-rar |
| `CTF-01` | 310085c4 |
| `CTX-01` | cangbaoge |
| `DOC-01` | Misc-03 |
| `DOC-03` | photo-rar |
| `ELF-01` | core-dump-memory |
| `ELF-02` | core-dump-memory |
| `ELF-03` | core-dump-memory |
| `ELF-04` | core-dump-memory |
| `ENC-01` | catcatcat |
| `ENC-02` | catcatcat |
| `ENC-03` | catcatcat |
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
| `FMT-01` | 07, 08, cangbaoge, catcatcat, vm-106-disk |
| `FMT-02` | cangbaoge |
| `FMT-03` | cangbaoge, core-dump-memory, rar附件1 |
| `FMT-04` | cangbaoge |
| `FMT-05` | cangbaoge |
| `FMT-12` | 解体 |
| `FOR-01` | Excaliflag, Misc-03 |
| `FOR-02` | Excaliflag |
| `FOR-05` | 解体 |
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
| `MEM-01` | core-dump-memory |
| `META-01` | 倒立屋 |
| `META-02` | 倒立屋 |
| `NET-01` | Misc-03 |
| `NET-02` | Misc-03 |
| `NET-21` | 解体 |
| `NET-22` | 解体 |
| `NUM-06` | rsa-small-d |
| `NUM-07` | rsa-small-d |
| `OBS-03` | crypto2 |
| `OCR-01` | Excaliflag, cangbaoge |
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
| `STG-01` | Excaliflag, cangbaoge, catcatcat, flag-jpg, 倒立屋 |
| `STG-02` | Excaliflag, cangbaoge, flag-jpg |
| `STG-03` | Excaliflag, cangbaoge, flag-jpg |
| `STG-04` | flag-jpg, 倒立屋 |
| `STG-05` | file-floppy, 倒立屋 |
| `STG-11` | core-dump-memory |
| `SUD-01` | png-25-pieces |
| `SUD-02` | png-25-pieces |
| `TOOL-31` | 解体 |
| `VER-01` | core-dump-memory |
| `VER-03` | 07, 08 |
| `VIRT-01` | vm-106-disk |
| `VIRT-02` | vm-106-disk |
| `ZIP-01` | 310085c4, download |
| `ZIP-02` | 310085c4, download |
| `ZIP-03` | 310085c4, download |
| `ZIP-04` | 310085c4, download |
| `ZIP-05` | 310085c4, download |
| `ZIP-06` | 310085c4, misc2-rar |

## 反模式清单（这条路别走）

- **310085c4**：判断：属于「弱口令」套路，先拿小字典打，成本最低。
- **310085c4**：工具：`ctf zip --crack` —— 多进程 + 预筛，比手写 `zipfile.extractall` 循环快两个数量级；备选 `fcrackzip
- **crypto06**：想用最权威的 openssl 直接解
- **crypto06**：openssl enc 支持 AES/DES/RC4 等，但不支持 Rabbit
- **crypto2**：`node scripts/run_jsfuck.js work/x/file.txt` → `TYPE: undefined`
- **crypto2**：上一轮猜"纯表达式返回字符串"是错的；`undefined` 说明尾部那次取值落空
- **f732347c**：一开始认定"9 帧拼图 → 图上有 flag"，于是花大量时间做 ASCII/Braille 渲染、连通域分析、字体模板匹配、OCR（RapidOCR 三次全 
- **f732347c**：图确实只是"画着 ISCC 的装饰画"，密文根本不在像素里。教训是——拼图题拼出图之后，要立刻问一句"图上有没有可读的字符串"，没有就转字节层。
- **flag-jpg**：从 stegdetect 源码改出 `break_jphide_v5`，头部校验通过，`length=38`，但载荷 38 字节是随机值。
- **flag-jpg**：头部正确、空口令正确，但载荷流/头部长度处理与原版 GUI 不一致。
- **gz-bf87ed29**：8192 点谱自相关找谐波间距
- **gz-bf87ed29**：工具：自写 `scripts/burst_pitch.py`
- **vm-106-disk**：第一版用 `'<HHHIIIIIIII'` 解 inode，读出来 `mode=0o40755 size=2869428224 links=524290`，明显
- **vm-106-disk**：字段顺序凭记忆写错了 —— `i_gid` 在 0x18、`i_links_count` 在 0x1A，不在紧接 uid 的位置；`i_size` 只有低 32
- **zip-6686092e**：需要判断这到底是张什么照片
- **zip-6686092e**：亮度图/饱和度图/局部方差图/Sobel 边缘图/高通残差图/2×2 半图/1:1 实体特写，逐个渲染读

## 按分类

### Misc

| 题目 | 一句话解法 | 关键工具 |
|---|---|---|
| Excaliflag | ELA（重压 JPEG 求差）→ 差值图出现 −30° 斜向亮带 → 转正 OCR → `3DS{Gr4b_Only_th1s_B1ts}`。 | `ctf info` / `numpy / PIL` / `cv2` / `rapidocr_onnxruntime` / `scripts/ela_reveal.py` |
| 倒立屋 | RGB 最低位抽出 `IsCc_2019`（ISCC 2019 标记），按"倒立屋"规则反转 → `9102_cCsI`。 | `ctf info` / `ctf lsb --auto` / `PIL` / `RapidOCR` / `scripts/lsb_text.py` |

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
| 310085c4 | 用 `7z` 拆两层套娃、`ctf zip --unpseudo` 排除伪加密、`ctf zip --crack` 跑 rockyou 拿到口令 `fish`，解出 `flag{ev3n::y0u::bru7us?!}` | `ctf info` / `xxd` / `7z x` / `ctf zip --unpseudo` / `ctf zip --crack` / `scripts/zipcrypto_probe.py` |
| Misc-03 | FTP 明文里读到弱口令，按 `SIZE` 校验重组出四个文件，用 `test.key` 做 RSA 解密拿到 flag。 | `7z` / `scapy (venv)` / `xxd` / `pycryptodome` / `Python zlib` |
| cangbaoge | 用 16 进制定位 `IEND` 结束偏移（745648）与文件实际大小（827432）的 81784 字节差值， | `ctf info` / `ctf png` / `xxd` / `Python zipfile` / `PIL crop/resize` / `numpy` |
| catcatcat | `strings` 思路在 JPEG 字节里搜到口令 `catflag`，RabbitLegacy 解密后 basE91 解出一段 Ook!，翻成 Brainfuck 跑出 flag。 | `7z` / `ctf info` / `Python re` / `crypto-js (npm)` / `base91_decode.py` / `ook_decode.py` |
| core-dump-memory | core 的 `.rodata` 藏着一张 149 字节表，5 条流交错，第 4 条就是 flag。 | `xxd` / `scripts/elfcore.py` / `scripts/segstrings.py` / `scripts/deshuffle.py` / `scripts/verify_flag.py` / `ctf case` |
| download | 中央目录伪造了加密位，清除后免密解压得到 flag。 | `xxd` / `7z l` / `python zipfile` / `scripts/dump_headers.py` / `ctf zip --unpseudo` |
| f732347c | 一句话解法：GIF 的 9 帧先拼出一张九宫格图，图上只有口令提示 `ISCC`；真正的密文在 **GIF 尾标 `0x3B` 之后的 154 字节 base64** 里，解出来是 `Salted__` 包，用 **AE | `ctf info` / `7z l / 7z x` / `自写 GIF 块遍历` / `手写 LZW 解码` / `numpy + PIL` / `Braille 渲染` |
| file-floppy | 启动软盘镜像看屏幕，或静态解码内核绘制的字形指针，得到 `flag{ctfshow}`。 | `7z` / `file` / `Python + struct` / `capstone` / `decode_message.py` / `render_font.py` |
| flag-jpg | `Jphswin.exe`（JPHS 0.5）空口令 Seek `flag.jpg`，隐藏文件 38 字节： | `stegdetect` / `stegbreak` / `jpseek 0.3` / `Jphswin.exe（JPHS 0.5）` / `wine32 + Xvfb` / `xdotool` |
| gz-bf87ed29 | - | `任务` / `拆 gzip（含找追加数据）` / `拆 tar` / `wav 结构` / `时频图（无视觉环境）` / `调制谱 / 解调` |
| misc2-rar | 逐层口令：`2020`（doc）→ `welcome_to_payhelp`（RAR hint）→ `hello 2020!`（RAR flag）。 | `7z` / `rar5parse.py` / `python zipfile` / `fix_png_height.py` / `decode_hint.py` / `crypto-js + rabbit_legacy.js` |
| photo-rar | EXIF `XPComment=little stars` → doc 口令；doc 白色文字 `Hello friend!` → flag.png 口令；QR 内容即 flag。 | `file` / `7z` / `ctf exif` / `Pillow getexif` / `olefile + doc_text.py` / `pyzbar + qr_decode.py` |
| png-25-pieces | - | `zipfile` / `Pillow` / `自写 ASCII 降采样` / `行/列覆盖率剖面` / `scripts/grid_glyphs.py` / `scripts/digits.py` |
| rar附件1 | （30 字以内说清"用什么方法拿到了什么"） | - |
| vm-106-disk | - | `python zipfile` / `scripts/qcow2raw.py` / `mmap 魔数扫描` / `7z l` / `scripts/ext4dump.py` / `zlib.decompressobj(31)` |
| welcome2 | `welcome.png` 的 IEND 后附 ZIP，PNG 注释给 7z 口令，`thienc.txt` 是双层 hex，`secenc.txt` 是 Base64/32 循环，最后是 Ook! 标点 + 两段 BF | `ctf info` / `xxd` / `dd` / `7z` / `parse_thienc.py` / `decode_secenc.py` |
| zip-6686092e | - | `任务` / `ZIP 隐藏条目` / `PNG 结构` / `IDAT 剩余数据` / `行过滤隐写` / `位平面结构` |
| 解体 | 按 `Content-Range: bytes a-b/15` 把 12 个 1~2 字节的 206 响应体贴回偏移，得到 `flag{17uaji1l}`。 | `7z` / `capinfos` / `tshark -z io,phs / conv,ip` / `tshark -T fields` / `tshark --export-objects` / `tshark -z follow,tcp,ascii` |

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

### 310085c4

- 分类：misc
- 解法：用 `7z` 拆两层套娃、`ctf zip --unpseudo` 排除伪加密、`ctf zip --crack` 跑 rockyou 拿到口令 `fish`，解出 `flag{ev3n::y0u::bru7us?!}`，并用 `7z -p` 与 `zlib.crc32` 双路校验。
- flag：`flag{ev3n::y0u::bru7us?!}`
- 知识点：`ZIP-01`、`ZIP-02`、`ZIP-03`、`ZIP-04`、`ZIP-05`、`ZIP-06`、`CTF-01`
- 工具：`ctf info` / `xxd` / `7z x` / `ctf zip --unpseudo` / `ctf zip --crack` / `scripts/zipcrypto_probe.py`
- 30 秒识别：
  - **换成伪加密**：`ctf zip --unpseudo` 一次搞定，两处 bit0 都要清；`method=0` 的包清位后直接是明文。
  - **换成 WinZip AES（method=99）**：`bkcrack` 完全失效，走 `hashcat -m 13600`，或 `aes_zip_decrypt.py`；先看 extra 里的 `0x9901` 确认强度（AE-1/AE-2/AE-3）。
  - **换成已知明文攻击**：若拿到 ≥12 字节连续明文（比如同目录有未加密的同名文件），`bkcrack -C 包.zip -c 条目 -p 明文 -o 偏移` 比字典快几个数量级，且不需要知道口令。
  - **换成 bit3 数据描述符**：CRC 在主字段为 0、真实值在数据尾部描述符里，爆破时要靠 `--magic` 指定明文前缀，速度和可靠性都会掉。
- 坑：ctf info 报"文件名长度异常=2"；内层 7z 要密码；top-20000 全灭
- 别走：判断：属于「弱口令」套路，先拿小字典打，成本最低。；工具：`ctf zip --crack` —— 多进程 + 预筛，比手写 `zipfile.extractall` 循环快两个数量级；备选 `fcrackzip

### Excaliflag

- 分类：Misc
- 解法：ELA（重压 JPEG 求差）→ 差值图出现 −30° 斜向亮带 → 转正 OCR → `3DS{Gr4b_Only_th1s_B1ts}`。
- flag：`3DS{Gr4b_Only_th1s_B1ts}`
- 知识点：`STG-01`、`STG-02`、`STG-03`、`FOR-01`、`FOR-02`、`OCR-01`
- 工具：`ctf info` / `numpy / PIL` / `cv2` / `rapidocr_onnxruntime` / `scripts/ela_reveal.py`
- 30 秒识别：
  - **换成 JPEG 原图**：ELA 更直接，但要注意原图本身已有压缩史，需多试几个 quality（70/80/90）取对比最大的一张。
  - **文字被裁成小图贴上去**：ELA 亮区会是一个矩形块，块内纹理与周围不一致；此时看**块边界**而不是字形，再对块内做增强。
  - **换成"通道微调"型（某通道 +2）**：ELA 可能不明显，改做**单通道直方图 + 局部均值差**，或对通道做同态滤波。
  - **附件变成截图/二次转发图**：先确认像素没被重编码；若被微信/QQ 压过，ELA 会全图乱亮，这时只能靠题面提示或元数据。
- 坑：位平面全噪声；通道 XOR 无结构；Windows OCR 只读出 3D5…}

### Misc-03

- 分类：misc
- 解法：FTP 明文里读到弱口令，按 `SIZE` 校验重组出四个文件，用 `test.key` 做 RSA 解密拿到 flag。
- flag：`flag{haPPy_Use_0penSsI}`
- 知识点：`NET-01`、`FOR-01`、`NET-02`、`CRY-01`、`CRY-02`、`DOC-01`
- 工具：`7z` / `scapy (venv)` / `xxd` / `pycryptodome` / `Python zlib`
- 30 秒识别：
  - 包内出现成对的 `220/331/230` 三位应答 + 一堆高端口短流 → 立刻想到 FTP 抓包，先读 `USER/PASS`。
  - 跑出某个「128/256/512 字节、纯随机」的小文件，同目录还有 `*.key`/`*.pem` → 立刻想到 RSA 直接解密。
  - 包里有 7MB+ 的"正经文档" → 先当烟雾弹处理，全文关键词搜不到再考虑渲染。
  - 如果 FTP 换成 FTPS/SSH → 不再有明文口令，转向"证书/私钥泄漏"或"弱口令爆破"路线（`hydra` + 字典）。
- 坑：找 strings 命令；试图 ctf info 判 pcap；误读 TCP/50070

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

### catcatcat

- 分类：misc
- 解法：`strings` 思路在 JPEG 字节里搜到口令 `catflag`，RabbitLegacy 解密后 basE91 解出一段 Ook!，翻成 Brainfuck 跑出 flag。
- flag：`CATCTF{Th1s_V3ry_cute_catcat!!!}`
- 知识点：`ENC-01`、`CRY-01`、`CRY-02`、`STG-01`、`ENC-02`、`ENC-03`、`FMT-01`
- 工具：`7z` / `ctf info` / `Python re` / `crypto-js (npm)` / `base91_decode.py` / `ook_decode.py`
- 30 秒识别：
  - 图片 + 文本、文本以 `U2FsdGVkX1` 开头 → 口令加密，口令多半在图片里（先 `strings`，再 LSB）。
  - 文件名里出现具体名词/数字（兔子、91、猫、Ook）→ 逐条当成算法提示，而不是闲聊。
  - 解密后整段文本只由 3 个可打印记号重复组成 → 想到 Ook! / Brainfuck 方言 / 三进制。
  - 如果 basE91 换成 base92/base65536 → 仍按"字符集+无填充"识别，先查字母表再写解码器。
- 坑：解密算法；cat. cat! cat?；口令来源

### core-dump-memory

- 分类：misc
- 解法：core 的 `.rodata` 藏着一张 149 字节表，5 条流交错，第 4 条就是 flag。
- flag：`ALEXCTF{K33P_7H3_g00D_w0rk_up}`
- 知识点：`ELF-01`、`ELF-02`、`ELF-03`、`ELF-04`、`MEM-01`、`FMT-03`、`STG-11`、`VER-01`
- 工具：`xxd` / `scripts/elfcore.py` / `scripts/segstrings.py` / `scripts/deshuffle.py` / `scripts/verify_flag.py` / `ctf case`
- 30 秒识别：
  - 文件头 `7f 45 4c 46` 且 `e_type=04 00` → core dump，直接上 `elfcore.py`，别想 volatility。
  - core 里堆/栈几乎全零 → 别找运行期数据，去找 `.rodata` 常量表。
  - 一串「唯一一对花括号、右括号压尾」的长诱饵串 → 立刻做 stride 穷举。
  - 如果诱饵串换成 base64 字符集 → 先整体 base64 解一次，再对结果做 stride 穷举（两层：编码层 + 排布层）。
- 坑：判型；找数据；破局

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
- 别走：想用最权威的 openssl 直接解；openssl enc 支持 AES/DES/RC4 等，但不支持 Rabbit

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
- 别走：`node scripts/run_jsfuck.js work/x/file.txt` → `TYPE: undefined`；上一轮猜"纯表达式返回字符串"是错的；`undefined` 说明尾部那次取值落空

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

### f732347c

- 分类：misc
- 解法：一句话解法：GIF 的 9 帧先拼出一张九宫格图，图上只有口令提示 `ISCC`；真正的密文在 **GIF 尾标 `0x3B` 之后的 154 字节 base64** 里，解出来是 `Salted__` 包，用 **AES-256-CBC + MD5 KDF + 口令 ISCC** 连续解两层即得 flag。
- flag：`flag{DugUpADiamondADeepDarkMine}`
- 工具：`ctf info` / `7z l / 7z x` / `自写 GIF 块遍历` / `手写 LZW 解码` / `numpy + PIL` / `Braille 渲染`
- 30 秒识别：
  - 图片类题，`ctf info` 报的"结构结束位置"和文件大小对不上 → **先 dump 尾巴**（`rfind` 尾标）。
  - 尾巴文本以 `U2FsdGVkX18` 开头 → 无脑当 **OpenSSL `Salted__`**，先 `base64 -d` 再 `openssl enc -d -k <口令> -md md5` 遍历。
  - 多帧 GIF 每帧各占画面一块 → **九宫格拼图**，拼完先读图上的字（那通常是口令/提示）。
  - 文件名/题名和密码学谐音（Aesop→AES、Caesar→凯撒、Rabbit→Rabbit 密码）→ 直接按那个算法试。
- 别走：一开始认定"9 帧拼图 → 图上有 flag"，于是花大量时间做 ASCII/Braille 渲染、连通域分析、字体模板匹配、OCR（RapidOCR 三次全 ；图确实只是"画着 ISCC 的装饰画"，密文根本不在像素里。教训是——拼图题拼出图之后，要立刻问一句"图上有没有可读的字符串"，没有就转字节层。

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
- 别走：从 stegdetect 源码改出 `break_jphide_v5`，头部校验通过，`length=38`，但载荷 38 字节是随机值。；头部正确、空口令正确，但载荷流/头部长度处理与原版 GUI 不一致。

### gz-bf87ed29

- 分类：misc
- 解法：-
- flag：`PARTIAL: 未拿到 flag —— 结构与排除清单已完成，卡点见 STATUS.md`
- 工具：`任务` / `拆 gzip（含找追加数据）` / `拆 tar` / `wav 结构` / `时频图（无视觉环境）` / `调制谱 / 解调`
- 30 秒识别：
  - 上边界自然滚降 → 优先"内容"路线（语音/音乐识别）；
  - 下边界硬、上边界软 → 优先"高通掩盖低频载荷"（放大量低带）；
  - 两头都硬 → 优先"整体频谱搬移"（SSB 下移，扫描 Δf）；
  - 有明确离散音色码表（聚类类型数跳变）→ 直接读符号序列。
- 别走：8192 点谱自相关找谐波间距；工具：自写 `scripts/burst_pitch.py`

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
- 别走：第一版用 `'<HHHIIIIIIII'` 解 inode，读出来 `mode=0o40755 size=2869428224 links=524290`，明显；字段顺序凭记忆写错了 —— `i_gid` 在 0x18、`i_links_count` 在 0x1A，不在紧接 uid 的位置；`i_size` 只有低 32

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

### zip-6686092e

- 分类：misc
- 解法：-
- flag：`PARTIAL: 未拿到 flag —— 容器/像素/视觉三层已系统性排除，卡点见 STATUS.md`
- 工具：`任务` / `ZIP 隐藏条目` / `PNG 结构` / `IDAT 剩余数据` / `行过滤隐写` / `位平面结构`
- 30 秒识别：
  - 若有 alpha 通道且非常数 → 先做 alpha 平面可视化（最省事的一类）；
  - 若是 JPEG → 先看量化表与 DCT 直方图（JSteg/F5 的指纹），再做卡方；
  - 若有 palette → 先看调色板顺序与索引平面；
  - 若图很平滑且无隐写痕迹 → 尽早转向"内容语义"，别在像素层反复渲染。
- 别走：需要判断这到底是张什么照片；亮度图/饱和度图/局部方差图/Sobel 边缘图/高通残差图/2×2 半图/1:1 实体特写，逐个渲染读

### 倒立屋

- 分类：Misc
- 解法：RGB 最低位抽出 `IsCc_2019`（ISCC 2019 标记），按"倒立屋"规则反转 → `9102_cCsI`。
- flag：`9102_cCsI`
- 知识点：`STG-01`、`STG-04`、`STG-05`、`META-01`、`META-02`
- 工具：`ctf info` / `ctf lsb --auto` / `PIL` / `RapidOCR` / `scripts/lsb_text.py`
- 30 秒识别：
  - **换成 `IsCc_2019` 写在 bit1/bit2**：`ctf lsb --auto` 会自动排到前面；自写脚本时把 `& 1` 改成 `>>bit & 1` 即可。
  - **换成长文本（整段 LSB）**：抽出来先看是不是 ZIP/PNG 头（`PK`、`\x89PNG`），是就直接落盘。
  - **换成"倒立 + 压缩包"组合**：先按 LSB 取包，解压后再按题面规则反转内容或文件名。
  - **换成通道分离藏字（非 LSB）**：转去 `ctf lsb`/位平面 + 通道差值，或直接上 ELA 看压缩痕迹。
- 坑：转 180° 看不到 flag；抽出 IsCc_2019 后想直接提交；反转时把整段可打印串都反了

### 解体

- 分类：misc
- 解法：按 `Content-Range: bytes a-b/15` 把 12 个 1~2 字节的 206 响应体贴回偏移，得到 `flag{17uaji1l}`。
- flag：`flag{17uaji1l}`
- 知识点：`NET-21`、`NET-22`、`TOOL-31`、`FMT-12`、`FOR-05`
- 工具：`7z` / `capinfos` / `tshark -z io,phs / conv,ip` / `tshark -T fields` / `tshark --export-objects` / `tshark -z follow,tcp,ascii`
- 30 秒识别：
  - 如果分片不在 HTTP 而在 TCP 层（无应用协议）→ 改看 `tcp.seq` 连续性，用 `tshark -z follow,tcp,raw` 或 `tcpdesegment` 重组，注意 FIN/RST 提前结束导致的半截数据。
  - 如果换成 HLS/DASH 切片（`.ts`/`.m4s`）→ 按 m3u8 里 `EXTINF` 顺序拼，而不是按抓包顺序；文件名里的序号通常才是权威顺序。
  - 如果换成 DNS 隧道/ICMP 隧道 → `tshark -Y dns -T fields -e dns.qry.name` 抽子域名字符串，再按序号字段/时间排序拼接。
  - 如果服务端返回 `416 Range Not Satisfiable` → 那行 `Content-Range: bytes */总长` 直接白送文件长度，用来校准 buffer。
- 坑：拼碎片；重组结果乱码；缺 2 字节
