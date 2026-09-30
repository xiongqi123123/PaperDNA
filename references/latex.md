# LaTeX

## 编辑规则

- 不破坏 `\cite{}`、`\ref{}`、`\label{}`、公式环境和自定义宏；修改前后，引用键和标签的数量应该一致。
- 不添加与任务无关的宏包、格式或排版调整，也不加装饰性格式（粗体、颜色）。
- 改动最小化：只改需要改的句子，保留原有的换行习惯（例如一句一行），方便看 diff。
- 使用论文中已定义的宏（如 `\method{}`、`\eg`），不要把宏展开成纯文本。
- 新增图表引用时沿用论文已有的风格（`\cref`、`Fig.~\ref` 等）。

## 修复编译报错

1. **编译**：优先使用论文已有的方式（Makefile、latexmkrc 或用户说明）。没有的话用 `latexmk -pdf main.tex`；中文论文用 `latexmk -xelatex main.tex`。
2. **读日志**：在 `.log`（以及 `.blg`）中找第一个错误，后面的错误常常是它引起的。常见的有 `Undefined control sequence`、`Missing $ inserted`、`File not found`、`Citation undefined`。
3. **修复**：
   - 缓存问题：运行 `latexmk -c`，或删除 `.aux/.bbl/.blg/.out/.toc` 等中间文件。只删这些中间文件。
   - `.bib` 格式错误：定位到具体条目并修复，常见原因有缺逗号、`& % _` 没有转义、key 重复。
   - 缺宏包：告诉用户缺哪个包以及安装命令（如 `tlmgr install xxx`），不要自己安装。
4. **重新编译**：回到第 2 步。最多重复 3 轮，仍然失败就向用户报告。

## 报告格式

- 状态：成功 / 失败
- 根因：
- 修改：改了哪些文件、改了什么
- 剩余警告：如 overfull hbox、未定义的引用
