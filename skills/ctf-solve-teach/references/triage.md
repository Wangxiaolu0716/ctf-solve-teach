# 60 秒判型决策树

拿到附件，按顺序问三个问题：**这是什么容器？里面还有什么？哪里对不上？**
判型错了，后面所有力气都白费，所以这一步宁慢不快。

---

## 0. 通用起手三件套（任何题都先跑）

```bash
ctf info artifacts/CHAL        # 哈希/熵/结构异常/flag 正则
ctf strings artifacts/CHAL -n 6 | head -50
ctf carve artifacts/CHAL -o work/carved
```

三条命令覆盖了 70% 杂项题的第一发现点：文件头尾对不上、藏了第二个文件、字符串里有可疑路径。

---

## 1. 未知文件 / 后缀可疑

1. 看头四字节，对照 magic 表（`ctf info` 已给出判定）。
2. 文件头自相矛盾（PK 头但叫 .png）→ 先复制成正确后缀再打开，**不要改原件**。
3. 大小异常：几 KB 的"图片"可能是纯文本改后缀。
4. 尾部有没有多余数据：`ctf info` 的"尾部"提示；或用十六进制看最后一个结构结束位置。
5. 结构正常但打不开 → 检查 CRC（PNG）或局部头（ZIP）。

判型依据优先级：**magic > 结构自检 > 扩展名 > 题面说法**。

## 2. 图片（png/jpg/gif/bmp/webp/ico）

| 征兆 | 下一步 |
|---|---|
| 打不开 / 解码报错 | `ctf png --fix`（CRC + 宽高反推）；JPEG 用 `ctf info` 看是否缺 EOI |
| **能打开，但文件比结束标记长** | **算差值**：`IEND+8` / `FFD9` / `%%EOF` 与文件实际大小的差 → 尾部附加数据，直接 `carve` |
| 能打开但看不到东西 | `ctf lsb --auto`；位平面分离（stegsolve）；通道差分 |
| 末尾有一大段高熵 | `ctf carve`，可能是拼接的 ZIP |
| 元数据空白但文件不大 | `ctf exif`，看 tEXt/iTXt 注释 |
| 两张图 | `ctf imgdiff A B` |
| 图片里有二维码 | zbar 扫；扫不出调对比度/反色/二值化 |
| GIF 多帧 | 逐帧导出，帧间差分，帧注释/延迟时间（可能是摩斯） |
| 颜色种类极少 | 调色板顺序、像素索引值可能是 ASCII |

常见组合拳：**改宽高 → 看全图 → LSB → 位平面 → 通道 → 拼接**。

## 3. 压缩包（zip/rar/7z/tar/gz）

1. `7z l` 先列目录（比解压宽容）。记下每个条目的**压缩方法、加密标志、CRC、大小**。
2. **先看 method 再决定打法**（这一步能省一小时）：

   | method | 名称 | 打法 |
   |---|---|---|
   | 0 | Store | 明文，直接读 |
   | 8 | Deflate | 常规解压 |
   | 1 | ZipCrypto | 伪加密 / 口令爆破 / bkcrack 明文攻击 |
   | **99** | **WinZip AES** | **见下面 3.3，hashcat 只破口令、不解文件** |

3. 加密标志 = 1 但能列 CRC → 先试伪加密修复：`ctf zip --unpseudo`。

### 3.1 WinZip AES（method=99）专项

**必须先认出它**，否则会拿 ZipCrypto 的套路白试半天：

- `ctf zip --no-auto` 或 `7z l` 显示 `method=99` / `AES-256`
- 条目比明文多出 `salt + 2 + 10` 字节（AE-256 是 16+2+10）
- bkcrack **完全无效**（它只针对 ZipCrypto 的 12 字节流密码）
- `zip2john` 的校验字节思路也不适用

打法顺序：

```bash
# 1) 先确认是 AES、看清楚强度
python library/zip/aes_zip_decrypt.py f.zip -l

# 2) 有线索口令 → 直接解（HMAC 校验，不会假命中）
python library/zip/aes_zip_decrypt.py f.zip -i flag.png -p 口令 -o out.png
python library/zip/aes_zip_decrypt.py f.zip --all -p 口令 --check   # 只验不落盘

# 3) 无口令 → 爆破（比 hashcat 慢但零配置；大字典还是上 hashcat -m 13600）
python library/zip/aes_zip_decrypt.py f.zip --all --brute --wordlist ../wordlists/top-20000.txt --check
python library/zip/aes_zip_decrypt.py f.zip --all --brute --digits 1 6 --check
```

口令来源优先级：文件名/注释/题面 → 同目录其它文件（常有一份明文线索）→ 字典 → 数字。

### 3.2 RAR5 结构解析

`unrar` 报错、或想知道里面到底几个文件 / 是否整档加密时，直接解析头：

```bash
python library/misc/rar5parse.py f.rar
```

看到 `ENCRYPTION` 块 = 整档加密要口令；看到多个 `FILE` 块 = 套娃，按名字继续拆。

> **坑**：RAR5 的 `HEAD_SIZE` 是**从 `HEAD_TYPE` 起算**的，不含 CRC 和 size 字段本身。
> 算头长度写成 `off+4+hs` 会差一个 vint 字节，后面全部错位，
> 表现为 `type` 变成 35、42958046 这类非法值。

### 3.3 其余

4. 注释字段、文件名、时间戳都可能是提示（密码提示常在文件名里）。
5. 解出来是坏文件 → 回到第 2/3 节修文件。
6. 多卷/分卷：文件名尾部 `.001` `.part1`，先按序号拼接再解。


## 4. 音频（wav/mp3/flac）

| 征兆 | 打法 |
|---|---|
| 听着有杂音/电流声 | 频谱图 `ctf spec`，找画出来的字 |
| 完全静音但文件不小 | 采样 LSB `ctf wavlsb`；看波形是否有方波 |
| 拨号音 | `ctf dtmf` |
| 双声道差异 | 相减、分离左右声道 |
| 有节奏的滴答 | 摩斯解码（长短间隔） |
| 频谱尾部空白 | 可能藏了 SSTV / 图片 |

## 5. 视频

拆帧（ffmpeg）→ 帧差分 → 看字幕轨/元数据 → 检查尾部附加数据 → 音频轨单独按第 4 节处理。

## 6. 流量包（pcap/pcapng）

1. `tshark -r x.pcap -q -z io,phs` 看协议分布，先判断"这是什么流量"。
2. 常见四类：
   - **HTTP 传文件**：导出对象 / 追踪流，找 200 响应体里的文件
   - **USB HID**：键盘击键（`ctf usb`）、鼠标轨迹
   - **DNS/ICMP 隧道**：看子域名长度、payload hex
   - **明文协议**：FTP/IRC/Telnet 直接读
3. 统计先行：`-z endpoints,ip`、`-z conv,tcp` 找异常主机和内网交互。
4. 时间线：按 frame.time 排序，注意异常间隔（可能是时序编码）。

## 7. 内存镜像（vmem/raw/dmp）

1. 先拿基本信息：系统版本、进程列表、网络连接。
2. 高频考点顺序：**剪贴板 → 命令行历史 → 进程内存里的文件 → 浏览器历史/密码 → 注册表 → 文件系统恢复**。
3. 工具：MemProcFS（挂载成虚拟盘，直接翻）或 `vol.bat`（Volatility 风格命令）。
4. 找 flag 的粗暴但有效法：全镜像搜 `flag{`，再定位所属进程。

## 8. 文档（docx/xlsx/pptx/pdf）

1. docx/xlsx 本质是 ZIP，解包看 `word/document.xml`、`_rels`、`docProps`。
2. 隐藏内容：白字、极小字号、隐藏工作表/行、批注、页眉页脚。
3. 宏：`vbaProject.bin` 提出来反混淆。
4. PDF：对象流、增量更新（改过的旧版本还在文件里）、JS 动作、附件。

## 9. 磁盘镜像（dd/e01/vhd）

分区表 → 文件系统 → 已删除文件恢复（photorec/testdisk）→ 未分配空间搜字符串。
先用 `ctf strings` 粗扫一遍，常常直接命中。

## 10. 程序文件（exe/elf/apk/so/pyc）

1. `strings` 找 flag 附近的提示、错误信息、URL。
2. 查壳/编译器指纹（DetectItEasy、`file`）。
3. 能跑就跑，用假输入观察行为（注意沙箱/断网）。
4. 静态：Ghidra/IDA 反编译主逻辑；动态：x64dbg / gdb + 断点。
5. APK：`unzip` → `classes.dex` → jadx 反编译；so 库单独看。
6. pyc：`uncompyle6`/`decompyle3`，或用 `marshal` 手工读。

## 11. 网页 / 源码

1. 先看源码注释、`robots.txt`、`.git`、备份文件（`www.zip`、`.bak`、`~`）。
2. 目录爆破 + 接口提取（JS 里的 API 路径）。
3. 参数逐个试：注入、越权（改 id/role）、模板注入、文件包含。
4. 前端校验 = 没有校验，抓包直接改。

## 12. 纯文本 / 数字 / 密文

1. 先判"是编码还是加密"：编码 = 有固定字母表、长度规整；加密 = 高熵、无结构。
2. 编码级联用 `ctf dec` 自动 BFS。
3. 古典密码：先统计字母频率，再试凯撒/维吉尼亚/置换。
4. 现代密码：看给的参数（n,e,c / 明文对 / 盐），套已知攻击模板。
5. 数字序列：差分、模运算、OEIS、进制转换、ASCII 分组。

## 13. 无附件（题面即谜题）

读题面三遍，把每个名词当线索：数字、日期、人名、缩写、大小写、标点。
这类题答案通常是一个常识/协议/历史事实，web 搜索是合法工具。

---

## 卡死时的横向检查清单（按此顺序过一遍）

- [ ] 文件尾部 / 未分配空间 / 元数据
- [ ] 有没有第二个附件、隐藏文件、`.DS_Store`、`__MACOSX`
- [ ] 题面里的数字和单词是不是提示（大小写、下划线、缩写）
- [ ] flag 格式是不是和假设的不一样（有的题是 `DASCTF{...}`、`ctfshow{...}`）
- [ ] 是不是**动态实例题**（附件名是 UUID、flag 里带无意义长数字）→ 别人的 wp 值对你无效，必须自己这条链上拿
- [ ] 是不是需要提交"解码后的中间结果"而不是最终 flag
- [ ] 题目分类是否被我判错了（隐写题当密码题做）
- [ ] 有没有更简单的解释（出题人往往不坏）
