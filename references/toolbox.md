# 工具箱：用途 / 命令 / 备选 / 什么时候别用

> 标 **[本机]** 的是本地便携工作台（把常用 CTF 工具统一装在一个目录）里现成的；标 **[通用]** 的需要自己装。
> 原则：**先用最笨的工具确认现象，再用聪明的工具下结论。**

---

## 1. 指纹与结构

| 工具 | 用途 | 典型命令 | 备选 | 什么时候别用 |
|---|---|---|---|---|
| `ctf info` **[本机]** | 哈希/熵/结构异常/flag 正则一屏出 | `ctf info f` | `file`、`xxd`、binwalk | 需要深度解析特定格式时（用专用工具） |
| `file` **[通用]** | 快速判类型 | `file -k f` | `ctf info` | 只看 magic，不看结构一致性 |
| `xxd` / HexFiend **[通用]** | 十六进制定位 | `xxd -l 256 f` | HxD、010 Editor | 大文件肉眼扫 |
| binwalk **[通用]** | 固件/容器签名扫描 | `binwalk -e f` | `ctf carve` | Windows 上装起来麻烦，优先用 carve |
| `ctf entropy` **[本机]** | 分块熵，找藏数据的位置 | `ctf entropy f -b 1024` | `binwalk -E` | 对纯文本文件没意义 |

## 2. 编码 / 转换

| 工具 | 用途 | 命令 | 备注 |
|---|---|---|---|
| `ctf dec` **[本机]** | 自动解码链 BFS（base/hex/url/rot/摩斯/零宽/bf） | `ctf dec "文本"` | 会给出每层结果，别只看最后一行 |
| CyberChef **[本机]** | 任意编码/加密可视化流水线 | 打开 `tools/CyberChef.html` | Magic 模式适合"不知道是什么编码" |
| `xxd -r -p` | hex → bin | `echo 414243 \| xxd -r -p` | |
| Python | 一切自定义转换 | — | 写进 `scripts/`，别用一次性管道 |

## 3. 图像

| 工具 | 用途 | 命令 | 备选 |
|---|---|---|---|
| `ctf png --fix` **[本机]** | CRC 校验 + 宽高反推修复 | `ctf png f --fix` | pngcheck、手工改 IHDR |
| `ctf lsb --auto` **[本机]** | 通道×位平面全扫，按 flag 命中排序 | `ctf lsb f --auto` | zsteg、stegsolve |
| `ctf imgdiff` **[本机]** | 两图逐像素差分 | `ctf imgdiff a.png b.png` | ImageMagick `compare` |
| stegsolve **[通用]** | 位平面浏览器（人眼找图） | GUI | 自己写 numpy |
| zsteg **[通用]** | PNG/BMP LSB 多规则扫描 | `zsteg -a f.png` | `ctf lsb` |
| zbar / pyzbar **[通用]** | 二维码/条码 | `zbarimg f.png` | 手机扫 |
| exiftool **[本机]** | 全格式元数据 | `exiftool f` | `ctf exif` |

## 4. 音频 / 视频

| 工具 | 用途 | 命令 |
|---|---|---|
| `ctf spec` **[本机]** | 频谱图导出 PNG | `ctf spec f.wav` |
| `ctf wavlsb` **[本机]** | WAV 采样最低位 | `ctf wavlsb f.wav` |
| `ctf dtmf` **[本机]** | 拨号音解码 | `ctf dtmf f.wav` |
| ffmpeg **[本机]** | 拆帧/转码/抽音轨 | `ffmpeg -i v.mp4 work/frame_%04d.png` |
| Audacity **[通用]** | 频谱视图、声道分离、变速 | GUI |

## 5. 压缩 / 口令

| 工具 | 用途 | 命令 | 关键点 |
|---|---|---|---|
| `ctf zip` **[本机]** | 结构/伪加密/字典/CRC | `ctf zip f.zip --crack wordlists/top-20000.txt --jobs 16` | 先 `--no-auto` 看结构再决定打法 |
| bkcrack **[本机]** | ZipCrypto 已知明文攻击 | `bkcrack -C f.zip -c inner.png -p plain.bin` | 需要 ≥12 字节已知明文（PNG 头 16 字节够） |
| hashcat **[本机]** | 各类哈希爆破 | `hashcat -m 17200 hash.txt dict` | **模式号选错等于白跑**，先 `hashcat --example-hashes` |
| john **[通用]** | 同上，自动识别 | `john --wordlist=d hash.txt` | |
| 7z **[本机]** | 万能解包 | `7z x f -owork/out` | 不认文件名编码时加 `-mcp=936` |

## 6. 流量

| 工具 | 用途 | 命令 |
|---|---|---|
| tshark | 统计/过滤/导出 | `tshark -r a.pcap -Y "http.request" -T fields -e http.host -e http.request.uri` |
| Wireshark | 追踪流、导出对象 | GUI：追踪 → TCP/UDP 流 |
| `ctf usb` **[本机]** | USB HID 键盘/鼠标解码 | `ctf usb kb.pcap`、`ctf usb m.pcap --mouse` |
| NetworkMiner **[通用]** | 自动提取文件/凭证 | GUI |

## 7. 内存 / 磁盘取证

| 工具 | 用途 | 命令 |
|---|---|---|
| MemProcFS **[本机]** | 内存镜像挂载为虚拟盘 | `MemProcFS.exe -device mem.raw -mount M:` 然后翻 `M:\pid\` |
| `vol.bat` **[本机]** | Volatility 封装 | `vol -f mem.raw windows.pslist` |
| testdisk / photorec **[本机]** | 分区修复 / 文件恢复 | `photorec_win.exe mem.raw` |
| `ctf strings` **[本机]** | 粗暴全盘搜 flag | `ctf strings mem.raw -n 6 -f flag` |

## 8. 文档

| 工具 | 用途 |
|---|---|
| unzip / 7z | docx/xlsx/pptx 解包看 XML |
| olevba / oletools | 提取并反混淆 VBA 宏 |
| pdf-parser / peepdf | PDF 对象、JS、增量更新 |
| LibreOffice | 转格式、看隐藏内容（另存为时留意） |

## 9. 逆向

| 工具 | 用途 | 备注 |
|---|---|---|
| `strings` | 第一手线索 | 先看错误信息、URL、flag 片段 |
| DetectItEasy **[通用]** | 查壳/编译器/熵 | 决定"要不要脱壳" |
| Ghidra **[通用]** | 免费反编译 | 大二进制首选 |
| IDA Free | 交互体验好 | |
| x64dbg / gdb+pwndbg | 动态调试、改内存 | 配合断点看参数 |
| Frida | 运行时 hook（移动端/桌面） | 绕过校验、抓明文 |
| jadx **[通用]** | APK 反编译 | 看 `classes.dex` |
| uncompyle6 | pyc 反编译 | 版本要对得上 |

## 10. Web

| 工具 | 用途 | 命令 |
|---|---|---|
| 浏览器 DevTools | 改包、看 JS、断点 | F12 |
| ffuf **[通用]** | 目录/参数爆破 | `ffuf -u http://T/FUZZ -w wordlist` |
| dirsearch **[通用]** | 目录扫描 | `dirsearch -u http://T` |
| sqlmap **[通用]** | SQLi 验证 | `sqlmap -u "http://T/p?id=1" --batch` |
| Burp / Caido | 拦截改包 | 前端校验全靠它 |
| `curl` | 复现请求 | `curl -i -X POST -d @body` |

## 11. 密码 / 数学

| 工具 | 用途 |
|---|---|
| CyberChef | 古典密码、可视化尝试 |
| quipqiup | 单表替换求解 |
| RsaCtfTool **[通用]** | RSA 参数已知攻击一把梭 |
| SageMath | 有限域、格、离散对数 |
| Python + pycryptodome | 自定义脚本 |

## 12. 工具选型三问（每次都要答）

1. **这个工具能看到什么，别的工具看不到？**（例：stegsolve 能同时看 8 个位平面，`ctf lsb` 只给字符串命中）
2. **它的失败模式是什么？**（例：字典爆破没命中，是口令难还是压缩方式不支持？）
3. **有没有更便宜的验证？**（例：先 `--no-auto` 看结构，再决定要不要跑 20 分钟爆破）
