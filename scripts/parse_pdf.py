#!/usr/bin/env python3
"""从本地 PDF 提取文本（PyMuPDF）。

用法:
    python3 parse_pdf.py <pdf> [--pages 1-10] [--main-only] [-o out.txt]

- 自动合并行尾断词连字符（"inher-\\nently" → "inherently"）。
- 每页前加 "=== Page N ===" 标记，方便按页引用。
- --main-only：截到正文末尾，去掉参考文献及之后的附录（在全文 30% 之后找第一个 References 标题）。
- 公式、上下标、特殊符号可能提取有误；需要逐字核对时，用 Read 工具看 PDF 页面。

依赖: pymupdf（pip install pymupdf）
"""
import argparse
import re
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("缺少 pymupdf，请先运行: pip install pymupdf")

REF_RE = re.compile(r"^\s*(?:\d+\.?\s*)?(References|REFERENCES|Bibliography)\s*$", re.M)


def parse_range(spec, n_pages):
    if not spec:
        return range(n_pages)
    start, _, end = spec.partition("-")
    start = max(int(start), 1)
    end = min(int(end) if end else start, n_pages)
    return range(start - 1, end)


def extract(path, pages=None, main_only=False):
    doc = pymupdf.open(path)
    text = "\n".join(
        f"=== Page {i + 1} ===\n" + doc[i].get_text("text", flags=pymupdf.TEXT_DEHYPHENATE)
        for i in parse_range(pages, len(doc)))
    if main_only:
        m = next((m for m in REF_RE.finditer(text) if m.start() > len(text) * 0.3), None)
        if m:
            text = text[:m.start()] + "\n=== 参考文献及之后的内容已省略 ===\n"
    return text


def main():
    ap = argparse.ArgumentParser(description="从 PDF 提取文本（PyMuPDF）")
    ap.add_argument("pdf")
    ap.add_argument("--pages", help="页码范围，如 1-10 或 3")
    ap.add_argument("--main-only", action="store_true", help="去掉参考文献及之后的内容")
    ap.add_argument("-o", "--output", help="写入文件而不是输出到终端")
    args = ap.parse_args()

    path = Path(args.pdf)
    if not path.is_file():
        sys.exit(f"找不到文件: {path}")
    text = extract(path, args.pages, args.main_only)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"已写入 {args.output}（{len(text)} 字符）")
    else:
        print(text)


if __name__ == "__main__":
    main()
