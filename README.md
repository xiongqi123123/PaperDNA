# VibePaper

个人论文写作 skill（Claude Code）：按自己的文风写论文，并把每次纠正沉淀下来。

写作规范（叙事类型、摘要与引言写法、句式库、用词与风格、取名）提炼自 1040 篇 CVPR 2026 / ICCV 2025 获奖、oral 与 highlight 论文的逐篇精读笔记，数字都有统计依据（`references/corpus_stats.md`）。

## 安装

把仓库链接到 Claude Code 的个人 skill 目录：

```bash
ln -s "$(pwd)" ~/.claude/skills/vibepaper
```

然后创建个人画像目录（它不进 git，只保存在本地）：

```bash
cp -r templates/profile profile
```

在 Claude Code 中输入 `/vibepaper` 可以手动调用。写论文、改论文时它也会自动触发。

## 首次使用

1. **提取文风**：提供 3–5 篇自己写的论文，然后说"用 vibepaper 分析这几篇，更新我的文风画像"。
2. **开始写作**：在论文仓库里说"帮我写 introduction"。第一次使用时，skill 会在论文仓库中创建 `.vibepaper/` 目录（spec、大纲、文献笔记），建议把它一起纳入 git 管理。

## 目录

```
SKILL.md                 入口：文件分类、必读文件、任务路由、硬规则
references/
  workflow.md            完整流程：spec（故事类型、取名）→ 大纲 → 写作 → 独立审查 → 修订
  story_types.md         8 种叙事类型：如何选、骨架、逐步写法、代表论文、检查清单   ┐
  sections/abstract.md   摘要写法：句数、作用序列、逐句模板、范例、检查清单        │
  sections/introduction.md 引言写法：段落功能序列、逐段模板、衔接、检查清单        │ 提炼自
  sentence_bank.md       句式库：按写作功能分 13 类的英文模板与原句                │ 1040 篇
  word_style.md          写作原则、用词、结论强度、去 AI 味、风格参数、检查清单    │ 顶会论文
  naming.md              取名：标题结构、方法名构造、首次引入、取名流程            │
  corpus_stats.md        语料统计（故事类型、摘要与引言结构等）                    ┘
  ai_words.json          AI 味与空洞用词表（唯一来源，扫描脚本也读它；支持限量词）
  sections/related_work.md / method.md / experiments.md / conclusion.md
                         正文各章节：组织方式、按故事类型的差异、逐部分写法与句式、检查清单（同样提炼自语料）
  review.md              审查标准与输出格式
  close_reading.md       范文精读（笔记模板见 templates/close_reading_note.md）
  literature.md          文献阅读与证据整理
  latex.md               LaTeX 编辑与编译报错修复
  proofread.md           语法拼写校对
  style_extraction.md    从样本提取文风
  feedback.md            用户纠正写到哪里
  thesis.md              学位论文补充
profile/                 个人画像（所有论文共用；不进 git，首次使用从 templates/profile/ 复制）
  style_profile.md       文风画像
  error_log.md           错题本
  glossary.md            跨论文术语表
templates/               复制到论文仓库 .vibepaper/ 的模板
scripts/
  ai_style_scan.py       去 AI 味扫描（只依赖标准库）
  parse_pdf.py           PDF 转文本（PyMuPDF：合并断词、按页标记、可截到参考文献前）
tools/corpus/            维护用的语料流水线：抓取 → 选论文 → 下载 → 转文本 → 精读 → 汇总（skill 运行时不用）
```

## 维护约定

**每条规则只写在一个文件里。** 想改某类规则时，按下表找到对应的文件：

| 想改的内容 | 文件 |
|---|---|
| 禁用或慎用某个词 | `references/ai_words.json` |
| 去 AI 味的判断方法 | `references/word_style.md` 第 4 节 |
| 某个章节怎么写 | `references/sections/<节>.md` |
| 叙事类型与故事骨架 | `references/story_types.md` |
| 可复用句式 | `references/sentence_bank.md` |
| 用词、结论强度、风格参数 | `references/word_style.md` 第 2、3、5 节 |
| 标题与方法名 | `references/naming.md`（取名的唯一来源，其他文件只放指引） |
| 跨章节的写作与论证原则 | `references/word_style.md` 第 1 节 |
| 审查时查什么、按什么格式输出 | `references/review.md` |
| 我自己的语气和习惯 | `profile/style_profile.md` |
| 具体的纠正记录 | `profile/error_log.md`（同类条目积累多了，合并进 style_profile） |

## 脚本

```bash
# 扫描整个论文目录；--level avoid 只看必须改的项
python3 scripts/ai_style_scan.py path/to/paper
# 额外输出困惑度（需要 pip install torch transformers；只作参考）
python3 scripts/ai_style_scan.py path/to/paper --ppl
```

有命中时退出码为 1，可以接到 pre-commit 或 CI 中使用。

## 来源

基于 [AI-Vibe-Writing-Skills](https://github.com/donghuixin/AI-Vibe-Writing-Skills)（MIT）重构，主要改变：

- 只支持 Claude Code：13 个角色 prompt 合并为按需加载的 `references/`，审查改由独立子代理完成，单篇论文的状态放在论文仓库的 `.vibepaper/`。
- 写作规范改为语料驱动：叙事类型、摘要与引言、句式、用词、取名、各章节写法，全部提炼自 1040 篇 CVPR 2026 / ICCV 2025 论文的逐篇精读笔记（流程见 `tools/corpus/`）。
- 本地检测改为只依赖标准库的扫描脚本，词表统一在 `ai_words.json`，支持限量词；去掉了逐句 AI 分数、第三方检测 API 与 MinerU。

## License

MIT，保留上游的版权声明，见 [LICENSE](./LICENSE)。
