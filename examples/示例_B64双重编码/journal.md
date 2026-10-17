# 解题日志 · 示例_B64双重编码

> 规则：每个步骤一段，边解边写，攒到最后回忆会失真。
> 字段：现象 → 判断 → 工具 → 命令 → 输出 → 解读 → 知识点 → 下一步。
> 失败的命令必须留，那是最贵的教材。

## 阶段 0 · 初筛

### 步骤 1 · 判型：这是编码不是加密

- 现象：文件 76 字节，单行，字符集只有 `A-Za-z0-9+/=`，末尾有 `=` 填充。
- 判断：Base 家族编码（套路：编码级联的第一层）。
- 工具：`ctf info` + `file` —— 先用最笨的工具确认"没有容器结构"，避免一上来就跑解码器。
- 命令：
```bash
ctf info artifacts/_build_chall.txt
file artifacts/_build_chall.txt
```
- 输出（关键行）：
```text
file: ASCII text, with no line terminators
size      : 76 bytes (0.1 KiB)
entropy   : 4.133 bits/byte
magic     : unknown
```
- 解读：熵 4.13 bits/byte 说明是纯文本，不是压缩/加密数据；`=` 填充是 base64 的强特征。
- 知识点｜Base64 的 3→4 映射：每 3 字节（24 bit）切成 4 个 6 bit 值，查 64 字符表；
  不足 3 字节时用 `=` 补齐。所以长度必为 4 的倍数，且 `=` 只出现在末尾。
- 结论/下一步：直接上自动解码链，让工具穷举一层组合。

## 阶段 1 · 自动解码链

### 步骤 2 · ctf dec 跑 BFS

- 现象：需要试 base64/hex/rot13 的多种组合，手算容易漏。
- 判断：编码级联（套路：套娃），用 BFS 而不是猜。
- 工具：`ctf dec` —— 它把每层结果按"flag 命中可能性"打分排序，比手工试快；
  备选 CyberChef Magic 也行，但要手动拖流水线。
- 命令：
```bash
ctf dec "$(cat artifacts/_build_chall.txt)"
```
- 输出（关键行）：
```text
[1.00] input>base64: '666c61677b623473655f31735f6e30745f656e637279707431306e7d'
[3.00] input>base64>hex: 'flag{b4se_1s_n0t_encrypt10n}'
```
- 解读：第一层 base64 解出的是十六进制串（56 个 hex 字符）；再 hex 解码得到 flag。
  评分 3.00 的那条就是命中，同层的 rot13/rot47 是噪音分支。
- 知识点｜为什么"再解一层"是常见设计：单一编码太容易被工具秒掉，出题人叠两层成本很低，
  但对人的直觉是干扰——人往往解完第一层看到 `666c6167` 还以为是乱码。
  识别技巧：解出来的串如果**只有 0-9a-f 且长度为偶数**，就是 hex。
- 结论/下一步：手工复算一遍确认，不盲信工具的"命中"。

### 步骤 3 · 手工复算，验证闭环

- 现象：工具说命中，但教学场景要能自己推。
- 判断：验证闭环（MISC-03），每个结论都要有一个"错了就会失败"的检验。
- 工具：Python（标准库）—— 两行就能验证，不需要装任何东西。
- 命令：
```bash
python -c "import base64;h=base64.b64decode(open('artifacts/_build_chall.txt').read()).decode();print(bytes.fromhex(h).decode())"
```
- 输出（关键行）：
```text
flag{b4se_1s_n0t_encrypt10n}
```
- 解读：与工具结果一致，且 flag 格式符合题面假设 → 闭环成立。
- 知识点｜`bytes.fromhex` 与 `base64.b64decode` 的区别：前者要求输入是偶数长度、
  只含 0-9a-fA-F；后者按 6 bit 查表，容忍换行。用错一个就报 `ValueError`，
  这个报错本身就是判断依据。
- 结论/下一步：写 flag.txt，整理文档。

## 弯路记录

- 一开始直接对原文件跑 `ctf xor`，白跑一次：xor 爆破的输出分布没有出现可读文本，
  说明这不是异或。教训：**先判"编码 vs 加密"**（见 knowledge-index MISC-04）。
