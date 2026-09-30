---
name: paperdna
description: 学术论文写作与修改助手，规范提炼自 1040 篇 CVPR 2026 / ICCV 2025 获奖、oral 与 highlight 论文。用于构思论文的叙事与故事线，撰写、重写、润色或审查论文与学位论文章节（Abstract、Introduction、Related Work、Method、Experiments、Conclusion），起标题和方法名，编辑 LaTeX 论文与修复编译错误，去除 AI 味与防御性写作，精读范文学习写法，阅读文献 PDF 并整理为可引用的证据，以及维护个人文风画像和错题本。Use when the user drafts, revises, polishes, proofreads or reviews an academic paper or thesis (LaTeX or Markdown), plans a paper's story, names a method or titles a paper, asks to reduce AI tone or defensive, self-undermining writing, close-reads exemplar papers, or wants to read papers as evidence for writing.
---

# PaperDNA

按用户的个人文风写论文，并把每次纠正沉淀下来，下次不再犯。

本 skill 目录：`${CLAUDE_SKILL_DIR}`。本文件和 references 中出现的 `references/`、`templates/`、`scripts/` 都相对这个目录。

**个人画像目录**（本文件和 references 中写作 `profile/` 的地方都指它）：
- 通常是 `${CLAUDE_PLUGIN_DATA}/profile/`。这是插件的持久数据目录，插件更新时保留；插件安装目录会随更新整体替换，不要把个人数据写进 skill 目录。
- 如果上一行显示的是未替换的字面量 `${CLAUDE_PLUGIN_DATA}`（没有作为插件加载），改用 `${CLAUDE_SKILL_DIR}/profile/`。
- 目录不存在时，先把 `templates/profile/` 整个复制过去。

## 文件分三类

| 类别 | 位置 | 内容 | 更新方式 |
|---|---|---|---|
| 写作规范 | `references/`、`templates/`、`scripts/` | 通用规则、章节写法、模板、脚本 | 用户维护；要改先问用户 |
| 个人画像 | 个人画像目录 `profile/`（见上） | 文风画像、错题本、跨论文术语表、个人补充词表 `ai_words.json` | 按 `references/feedback.md` 更新 |
| 单篇论文状态 | 论文仓库的 `.paperdna/` | spec、大纲、文献笔记 | 写作过程中随时更新 |

论文仓库指用户当前论文所在的目录（包含主 `.tex` 或 `.md` 文件）。需要 `.paperdna/` 而它不存在时：从 `templates/` 复制 `spec.md` 和 `outline.yaml` 过去，并创建 `refs/` 目录。

## 动笔前必读

1. `profile/style_profile.md`：文风画像
2. `profile/error_log.md`：错题本
3. `references/word_style.md` 第 4 节：去 AI 味规则
4. `references/anti_defensive.md` 第 0 节：不写防御性论文（不主动示弱，局限最多 2 条）
5. 论文仓库中存在 `.paperdna/spec.md` 时也要读。其中的术语、数字和约束优先于其他所有规则。

## 按任务选择

| 任务 | 另外读取 | 做法 |
|---|---|---|
| 润色或改写一段、几句 | `references/word_style.md` 第 1、5 节 | 直接改；改完运行扫描脚本；列出改了哪些地方 |
| 写或重写一节 | `references/sections/<节>.md`（先读第 0 节速查）、`references/word_style.md` 第 1 节（写作原则）、`references/sentence_bank.md` 中对应的类别 | 按 `references/workflow.md` 第 3–5 步 |
| 写或改摘要、引言 | `references/sections/abstract.md` 或 `introduction.md`（先读第 0 节速查，再读需要的部分） | 先按 spec 的故事类型选作用序列或段落序列，再逐句写 |
| 构思故事、决定怎么讲这篇论文 | `references/story_types.md`（先读第 1–3 节，再读所选类型的章节） | 结果写进 spec 的故事类型和叙事骨架 |
| 起标题、给方法取名 | `references/naming.md` | 产出 3–5 个候选，说明各自的取舍 |
| 从零写一篇，或大改结构 | `references/workflow.md` | 完整流程：spec（含故事类型和取名）→ 大纲 → 写作 → 审查 |
| 审稿式自查 | `references/review.md` | 用独立子代理审查（见 workflow 第 4 步） |
| 压缩篇幅、处理不利结果、让论文更有说服力、rebuttal 前自查 | `references/anti_defensive.md` | 按不利材料的处理顺序和"不给审稿人递刀子"自查清单执行 |
| 精读一篇范文，学习它的写法 | `references/close_reading.md` | 按精读模板写笔记 |
| 读文献或 PDF | `references/literature.md` | |
| 语法和拼写校对 | `references/proofread.md` | 改动最小化 |
| LaTeX 编辑或编译报错 | `references/latex.md` | |
| 学位论文 | 另外读 `references/thesis.md` | |
| 从样本提取文风 | `references/style_extraction.md` | |
| 用户纠正写法或事实 | `references/feedback.md` | |

章节文件：`abstract.md`、`introduction.md`、`related_work.md`、`method.md`、`experiments.md`、`conclusion.md`（含 Discussion 和 Limitations）。

`story_types.md`、`sections/` 下的全部章节文件、`sentence_bank.md`、`word_style.md`、`naming.md` 是从 1040 篇 CVPR 2026 / ICCV 2025 获奖、oral 和 highlight 论文的逐篇精读笔记中提炼的，数据来源和统计见 `references/corpus_stats.md`。这几份文件都比较长，按需读取相关章节，不必每次通读。

## 硬规则

- 不编造引用、数据或实验结果。缺依据的地方写 `% TODO: ...` 并告诉用户。只引用 `.bib` 中已有或用户提供的文献。
- 技术描述要与代码、公式和实验设置一致。论文仓库或用户指定的位置有代码和结果时，先读再写。
- 编辑 `.tex` 时不破坏 `\cite{}`、`\ref{}`、`\label{}` 和公式环境，也不做与任务无关的排版改动。
- 大范围重写（跨段落的结构调整，或用户说"重写"）时，先给出修改方案：目标、影响哪些段落、对应的 DoD 变化。用户同意后再动笔。
- 已确定的决定（术语、口径、结构）写进 `.paperdna/spec.md` 的决策记录，不要只留在对话里。

## 脚本

- 去 AI 味扫描。只依赖 Python 标准库，词表读自 `references/ai_words.json`，再追加个人画像目录里的补充词表：
  `python3 ${CLAUDE_SKILL_DIR}/scripts/ai_style_scan.py <文件或目录>... --extra <个人画像目录>/ai_words.json`
  有命中时退出码为 1。加 `--level avoid` 只看必须改的项；加 `--ppl` 会额外输出困惑度，这项需要 torch 和 transformers，结果只作参考。
- PDF 转文本（需要 pymupdf）：
  `python3 ${CLAUDE_SKILL_DIR}/scripts/parse_pdf.py <pdf> --main-only [-o out.txt]`
  逐句引用和通读全文时读提取出的文本，比读 PDF 页面图像省得多；看图表版式、核对公式和特殊符号时，用 Read 工具读 PDF 对应页（需要 poppler 的 pdftoppm）。
