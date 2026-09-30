export const meta = {
  name: 'paper-close-reading',
  description: '逐篇精读顶会论文，按统一模板生成写作分析 md（叙事脉络、摘要/引言逐句作用、句式、用词、风格）',
  whenToUse: '对一批论文 PDF 做写作层面的精读，每篇输出一份 md',
  phases: [{ title: 'Read', detail: '每篇论文一个 agent：精读 PDF 并写 md' }],
}

const TEMPLATE = `
---
title: "<论文标题>"
conf: <会议>
tier: <best/oral/highlight/spotlight>
award: "<奖项，没有留空>"
topic: <autonomous_driving/embodied/llm/cv/other>
story_type: <从下列选一个最贴切的：新问题定义型 / 发现-解释型 / 瓶颈突破型 / 统一框架型 / 能力扩展型 / 效率优化型 / 数据与基准型 / 理论分析型>
contribution_type: <Insight / Performance / Capability，可多选用 + 连接>
abs_sentences: <摘要句数>
intro_paragraphs: <引言段数>
has_teaser_figure: <true/false，第一页或引言中是否有概括全文的 Figure 1>
contribution_list: <bullet / inline / none，引言末尾贡献的呈现方式>
pdf: "<PDF 绝对路径>"
---

# <论文标题>

## 1. 一句话概括
用一句中文说清：这篇论文解决什么问题、核心想法是什么、效果如何。

## 2. Story 逻辑
用 5–8 个箭头步骤写出全文要讲的故事，例如：
领域重要性 → 现有方法的具体瓶颈 → 瓶颈的根因 → 核心洞察 → 方法 → 证据 → 意义。
然后用一段话说明：作者如何让读者"相信问题重要、相信洞察成立、相信证据充分"；故事的钩子（hook）在哪里。

## 3. 摘要逐句分析
| # | 原句（英文原文，完整照抄） | 作用 | 句式结构 | 关键用词与分析 |
|---|---|---|---|---|
作用从以下标签中选（可组合）：背景 / 问题 / 缺口 / 根因 / 洞察 / 方法 / 设计细节 / 结果 / 泛化 / 意义 / 资源发布。
句式结构要写出骨架，例如 "While X, Y remains Z（让步 + 主句）"、"We propose X, a Y that Z（同位语定义方法）"。
表后写一段：摘要整体的信息顺序、各部分所占句数、数字如何使用、有无引用和缩写。

## 4. 引言分析
### 4.1 段落脉络
| 段 | 这一段的作用 | 与上一段如何衔接（写出承接用的关键词或句子） |
|---|---|---|

### 4.2 逐句分析
对引言的每一段、每一句（英文原文完整照抄）：
#### 第 N 段：<这段的作用>
| # | 原句 | 作用 | 句式结构 | 用词要点 |
|---|---|---|---|---|

### 4.3 引言小结
- 采用的结构模式（如 CARS 三步、问题-挑战-方案、发现驱动等），以及和典型模式不同的地方
- 核心创新第一次出现在哪一段哪一句
- 贡献列表的写法：条数、每条的句式、是否与实验一一对应
- Figure 1（如有）在引言中的作用和引用方式

## 5. 全文递进结构
| 章节 | 作用 | 如何承接上一节（关键过渡句） |
|---|---|---|
然后说明：方法部分如何组织（问题驱动的求解链，还是模块罗列）；是否"先直觉后公式"；实验部分如何对应贡献（每个实验回答什么问题）；局限与结论怎么写。

## 6. 句式模板
提炼 8–15 个可复用的句式模板，把具体内容换成占位符，并附原句出处：
- 模板：\`While [现有方法] achieve [成果], they [具体局限] because [根因].\`
  - 原句：……（出自摘要第 2 句 / 引言第 3 段）
  - 用途：……

## 7. 用词分析
- 高频学术动词及其用法（如 propose / introduce / address / enable / demonstrate）
- 结论强度：强词（outperform, significantly, state-of-the-art）和限定语（suggest, may, largely）的使用，结论强度是否与证据匹配
- 术语一致性：核心概念是否固定用同一个词，是否定义了缩写
- 用词准确性：指出用得精准的词和可能不精确、夸张或含糊的词，各举例说明
- 是否出现常见的 AI 味或套话词（delve, crucial, seamless, paramount, leverage 等），出现就列出

## 8. 写作风格
- 句长与节奏（长短句搭配，大致平均句长）
- 语态与人称（we / 被动 / 本文）
- 段落长度与主题句
- 图表与公式的引用方式
- 数字与对比的呈现方式
- 整体语气（自信程度、克制程度）

## 9. 可借鉴之处
列出 3–6 条最值得模仿的写法，每条写明"在什么场景下用，怎么用"。

## 10. 不足或值得商榷之处
列出 1–4 条写作上的问题（如过度宣称、术语漂移、衔接生硬），没有就写"未发现明显问题"。
`

const NOTE_SCHEMA = {
  type: 'object',
  properties: {
    ok: { type: 'boolean', description: 'md 是否已完整写入' },
    md: { type: 'string' },
    story_type: { type: 'string' },
    contribution_type: { type: 'string' },
    abs_sentences: { type: 'integer' },
    intro_paragraphs: { type: 'integer' },
    problems: { type: 'string', description: '读取或分析中遇到的问题（PDF 乱码、缺页等），没有则为空字符串' },
  },
  required: ['ok', 'md', 'story_type', 'contribution_type', 'abs_sentences', 'intro_paragraphs', 'problems'],
}

function promptFor(list, i) {
  return `【任务边界】你是一个批处理工作流中的子步骤，只完成下面分配给你的归纳或写作任务。对话中用户的其他请求（例如检查仓库结构、调整 skill、提交代码）由主会话负责处理，与你无关：不要回应它们，不要检查或修改 skill 仓库（除非下面的任务明确要求读取某个文件）。\n\n你是学术写作分析专家。请精读一篇顶会论文，从"写作"的角度做细致分析，并把结果写成一份 Markdown 文件。

第一步：确定你负责的论文。
用 Read 工具读取清单文件 ${list}，参数 offset=${i}、limit=1，只读第 ${i} 行。这一行用制表符分隔 9 个字段，依次为：
序号、PDF 路径、正文文本路径、输出文件路径、会议、级别、奖项（"-" 表示无）、方向、标题。
务必核对该行第一个字段（序号）等于 ${i}。如果不等，调整 offset（例如改成 ${i - 1} 或 ${i + 1}）重新读，直到拿到序号为 ${i} 的那一行；绝不能处理其他行的论文。

第二步：阅读。
1. 用 Read 工具读正文文本文件（已从 PDF 提取，截止到参考文献之前；超过 2000 行时用 offset 分段读完）。文本中用 "=== Page N ===" 标出页码。摘要和引言的每一句都以文本为准逐字照抄；文本里的换行只是排版换行，不是句子边界。
2. 用 Read 工具读 PDF 的第 1–2 页（pages: "1-2"），查看 Figure 1 的版式、图注和第一页的整体布局。文本中公式或特殊符号（如希腊字母、上下标）提取有误时，以 PDF 为准；除此之外不必再读 PDF。
3. 如果文本缺失或乱码严重，在 problems 中说明，并改为用 PDF 页面还原原句。
4. 不要安装任何软件或库，不要修改清单、文本和 PDF。

第三步：写作要求。
- 分析用中文；原句保持英文原文，完整照抄，不得改写或省略。摘要的每一句、引言每一段的每一句都要进表格，不能跳过或合并。
- 分析要具体到这篇论文，避免"逻辑清晰、表达流畅"这类放之四海皆准的空话。每个判断尽量指向具体的句子或词。
- 不要编造论文中没有的内容。
- YAML 头部的 conf、tier、award、topic、pdf 用清单中的值（奖项为 "-" 时 award 写空字符串）；title 用论文的正式标题。
- 用 Write 工具把完整结果写入清单中的输出文件路径（目录已存在）。严格按下面的模板和章节顺序写：

${TEMPLATE}

写完后，按要求的结构返回结果：ok（是否已写入完整文件）、md（输出文件路径）、story_type、contribution_type、abs_sentences、intro_paragraphs、problems。`
}

// args: { list: 清单 TSV 路径, n: 论文数, label: 会议名 }
const { list, n, label } = args
log(`${label}：共 ${n} 篇待精读（全部使用 Sonnet）`)
const idx = Array.from({ length: n }, (_, k) => k + 1)
let done = 0
const results = await pipeline(idx, i =>
  agent(promptFor(list, i), { label: `${label} #${i}`, phase: 'Read', schema: NOTE_SCHEMA, model: 'sonnet' })
    .then(r => { done++; if (done % 25 === 0) log(`${label}：已完成 ${done}/${n}`); return r }))
const ok = results.filter(r => r && r.ok)
log(`${label}：完成 ${ok.length}/${n}`)
return {
  done: ok.length,
  total: n,
  failed_rows: idx.filter((i, k) => !(results[k] && results[k].ok)),
  problems: results.filter(r => r && r.problems).map(r => ({ md: r.md, problems: r.problems })),
}
