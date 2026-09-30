#!/usr/bin/env python3
"""扫描论文中的 AI 味用词。

用法:
    python3 ai_style_scan.py <文件或目录>... [--words PATH] [--level avoid] [--ppl]

- 目录会递归扫描 .tex / .md / .txt 文件，跳过以 . 开头的目录。
- .tex 会先去掉注释、公式、代码与表格环境、\\cite / \\ref / \\label 等，只检查正文，
  行号与源文件一致。
- 词表默认读取 ../references/ai_words.json；--extra 追加个人补充词表（格式相同，可重复使用，文件不存在时跳过）。带 max 字段的是"限量词"：同一文件内不超过 max 次不报，超过才全部列出。
- 退出码：有命中为 1，无命中为 0，出错为 2。
- --ppl 额外计算每个文件的困惑度（需要 torch 与 transformers，首次运行会下载 distilgpt2）。
  只适用于英文；学术文本本身困惑度偏低，这个数字只能作参考，不能单独用来判断是否 AI 生成。
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

DEFAULT_WORDS = Path(__file__).resolve().parent.parent / "references" / "ai_words.json"
EXTENSIONS = {".tex", ".md", ".txt"}

# 整段跳过的 LaTeX 环境：公式、代码、表格主体
SKIP_ENVS = {
    "equation", "equation*", "align", "align*", "alignat", "alignat*",
    "gather", "gather*", "multline", "multline*", "eqnarray", "eqnarray*",
    "displaymath", "math", "verbatim", "lstlisting", "minted",
    "tabular", "tabular*", "tabularx", "algorithmic",
}

# \begin{env} / \end{env} / \[ / \] / $$；排除 \\[2pt] 这类换行命令
TEX_TOKEN_RE = re.compile(r"\\begin\{([^}]+)\}|\\end\{([^}]+)\}|(?<!\\)\\\[|(?<!\\)\\\]|\$\$")
TEX_COMMENT_RE = re.compile(r"(?<!\\)%.*$")
TEX_INLINE_MATH_RE = re.compile(r"(?<!\\)\$.*?(?<!\\)\$|\\\(.*?\\\)")
TEX_REF_RE = re.compile(
    r"\\(?:cite[a-zA-Z]*|[cC]?ref|eqref|autoref|pageref|label|url|href|"
    r"includegraphics|input|include|bibliography[a-z]*)\*?(?:\[[^\]]*\])*\{[^}]*\}"
)
TEX_COMMAND_RE = re.compile(r"\\[a-zA-Z@]+\*?")
MD_INLINE_RE = re.compile(r"`[^`]*`|(?<!\\)\$.*?(?<!\\)\$")


def clean_tex_lines(lines):
    """逐行清洗 LaTeX，返回与源文件行号一一对应的正文（整行被跳过时为空串）。"""
    out = []
    skip_depth = 0      # 位于 SKIP_ENVS 环境中的嵌套层数
    in_display = False  # 位于 \[ ... \] 或 $$ ... $$ 中
    for raw in lines:
        line = TEX_COMMENT_RE.sub("", raw)
        kept = []
        pos = 0
        for m in TEX_TOKEN_RE.finditer(line):
            if not skip_depth and not in_display:
                kept.append(line[pos:m.start()])
            pos = m.end()
            begin_env, end_env = m.group(1), m.group(2)
            if begin_env is not None:
                if begin_env in SKIP_ENVS:
                    skip_depth += 1
            elif end_env is not None:
                if end_env in SKIP_ENVS and skip_depth:
                    skip_depth -= 1
            elif m.group(0) == "\\[":
                in_display = True
            elif m.group(0) == "\\]":
                in_display = False
            else:  # $$
                in_display = not in_display
        if not skip_depth and not in_display:
            kept.append(line[pos:])
        text = " ".join(kept)
        text = TEX_INLINE_MATH_RE.sub(" ", text)
        text = TEX_REF_RE.sub(" ", text)
        text = re.sub(r"\\\\(?:\[[^\]]*\])?", " ", text)  # 换行命令 \\ 与 \\[2pt]
        text = re.sub(r"\\([%&_#$])", r"\1", text)         # 转义字符 \% \& 等
        text = TEX_COMMAND_RE.sub(" ", text)
        text = re.sub(r"[{}~]", " ", text)
        out.append(re.sub(r"\s+", " ", text).strip())
    return out


def clean_md_lines(lines):
    """去掉 Markdown 代码块、行内代码与公式，保持行号。"""
    out = []
    in_fence = False
    for raw in lines:
        if raw.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else MD_INLINE_RE.sub(" ", raw).strip())
    return out


def load_rules(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    rules = []
    for r in data["rules"]:
        flags = re.IGNORECASE if r.get("lang") == "en" else 0
        try:
            regex = re.compile(r["pattern"], flags)
        except re.error as e:
            raise ValueError(f"词表中 {r.get('id')} 的正则有误: {e}")
        rules.append({**r, "regex": regex})
    return rules


def iter_files(paths):
    for p in map(Path, paths):
        if p.is_dir():
            for f in sorted(p.rglob("*")):
                rel_parts = f.relative_to(p).parts
                if f.is_file() and f.suffix in EXTENSIONS and not any(s.startswith(".") for s in rel_parts):
                    yield f
        elif p.is_file():
            yield p
        else:
            raise ValueError(f"路径不存在: {p}")


def scan_file(path, rules, level):
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    cleaned = clean_tex_lines(lines) if path.suffix == ".tex" else clean_md_lines(lines)
    hits = []
    for lineno, text in enumerate(cleaned, 1):
        if not text:
            continue
        for r in rules:
            if level and r["level"] != level:
                continue
            for m in r["regex"].finditer(text):
                start, end = max(0, m.start() - 30), min(len(text), m.end() + 30)
                snippet = ("…" if start else "") + text[start:end] + ("…" if end < len(text) else "")
                hits.append((lineno, r, m.group(0), snippet))
    # 带 max 的规则是"限量词"：同一文件内不超过 max 次时不报，超过时全部列出
    per_rule = Counter(h[1]["id"] for h in hits)
    hits = [h for h in hits if "max" not in h[1] or per_rule[h[1]["id"]] > h[1]["max"]]
    return hits, cleaned


_ppl_model = None


def perplexity(text):
    """用 distilgpt2 计算困惑度（滑动窗口），文本少于 30 词返回 None。"""
    global _ppl_model
    if len(text.split()) < 30:
        return None
    try:
        import torch
        from transformers import GPT2LMHeadModel, GPT2TokenizerFast
    except ImportError:
        raise RuntimeError("--ppl 需要 torch 与 transformers：pip install torch transformers")

    if _ppl_model is None:
        tok = GPT2TokenizerFast.from_pretrained("distilgpt2")
        model = GPT2LMHeadModel.from_pretrained("distilgpt2").eval()
        _ppl_model = (tok, model)
    tok, model = _ppl_model
    ids = tok(text, return_tensors="pt").input_ids
    max_len, stride = model.config.n_positions, 512
    nlls, prev_end = [], 0
    for begin in range(0, ids.size(1), stride):
        end = min(begin + max_len, ids.size(1))
        input_ids = ids[:, begin:end]
        target = input_ids.clone()
        target[:, : -(end - prev_end)] = -100
        with torch.no_grad():
            nlls.append(model(input_ids, labels=target).loss)
        prev_end = end
        if end == ids.size(1):
            break
    return torch.exp(torch.stack(nlls).mean()).item()


def main():
    ap = argparse.ArgumentParser(description="扫描论文中的 AI 味用词")
    ap.add_argument("paths", nargs="+", help="文件或目录")
    ap.add_argument("--words", default=str(DEFAULT_WORDS), help="词表 JSON 路径")
    ap.add_argument("--extra", action="append", default=[], help="追加的个人补充词表（可重复；不存在则跳过）")
    ap.add_argument("--level", choices=["avoid", "review"], help="只显示某一级别的命中")
    ap.add_argument("--ppl", action="store_true", help="额外计算困惑度（仅供参考）")
    args = ap.parse_args()

    rules = load_rules(args.words)
    for extra in args.extra:
        if Path(extra).is_file():
            rules += load_rules(extra)
    counter = Counter()
    level_count = Counter()
    n_files = 0
    for path in iter_files(args.paths):
        n_files += 1
        hits, cleaned = scan_file(path, rules, args.level)
        for lineno, r, matched, snippet in hits:
            cap = f"（全文上限 {r['max']} 次，已超出）" if "max" in r else ""
            print(f"{path}:{lineno}  [{r['level']}] {r['category']}: {matched!r}{cap} → {r['suggest']}")
            print(f"    {snippet}")
            counter[r["id"]] += 1
            level_count[r["level"]] += 1
        if args.ppl:
            ppl = perplexity(" ".join(t for t in cleaned if t))
            if ppl is not None:
                print(f"{path}: 困惑度 {ppl:.1f}（仅供参考）")

    total = sum(counter.values())
    print()
    if total:
        print(f"共 {total} 处（avoid {level_count['avoid']}，review {level_count['review']}），扫描了 {n_files} 个文件。")
        print("最常见：" + "，".join(f"{k} ×{v}" for k, v in counter.most_common(8)))
    else:
        print(f"未发现命中，扫描了 {n_files} 个文件。")
    return 1 if total else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # 出错统一返回 2，与"有命中"区分
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(2)
