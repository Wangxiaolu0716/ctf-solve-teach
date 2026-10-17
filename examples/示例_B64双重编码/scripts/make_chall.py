# -*- coding: utf-8 -*-
"""生成示例题目附件：base64(hex(flag))，写到 artifacts/_build_chall.txt。

在 示例_B64双重编码/ 目录下运行：
    python scripts/make_chall.py
"""
import base64
from pathlib import Path

flag = "flag{b4se_1s_n0t_encrypt10n}"
payload = base64.b64encode(flag.encode().hex().encode()).decode()

out = Path("artifacts/_build_chall.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(payload, encoding="utf-8")
print(f"written {out} ({len(payload)} bytes)")
print(payload)
