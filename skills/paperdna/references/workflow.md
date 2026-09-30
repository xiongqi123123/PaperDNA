# 完整写作流程

适用于：从零写一篇论文、写或重写一节、大改结构。润色一小段不需要走这个流程。

## 0. 准备论文工作区

- 确认论文仓库根目录和主文件（如 `main.tex`），不确定就问用户。
- 没有 `.paperdna/` 时按 SKILL.md 的说明创建。
- 找到代码和实验结果的位置（日志、csv、画表脚本），记到 spec 的"基本信息"里。

## 1. Spec

- 按 `templates/spec.md` 的结构填写 `.paperdna/spec.md`，已有的就在原基础上更新。
- 信息来源：用户、已有的 .tex 草稿、代码和结果文件。缺少关键信息（贡献、核心数字、投稿目标）时问用户，不要猜。
- **选故事类型**：按 `references/story_types.md` 第 2 节的判断流程确定主类型（必要时加一个辅类型），把该类型的叙事骨架套到本文，写进 spec 的"叙事骨架"，并找出钩子（反直觉的数字、现象或对比）。故事类型决定了摘要和引言的骨架、方法怎么组织、实验要证明什么。
- **定名字**：按 `references/naming.md` 的取名流程产出 3–5 个标题和方法名候选，和用户一起定稿，写进 spec。名字一旦确定，全文统一。
- 写整篇或大改结构时，spec 要经用户确认才能进入下一步。只写一节时，确认与这一节相关的条目即可。

## 2. 大纲

- 按 `templates/outline.yaml` 在 `.paperdna/outline.yaml` 写大纲：每节写明目标；每段写明论点（thesis）、证据和 DoD（验收条件）。
- DoD 必须能检查，例如"引用 X 的结论""给出 Table 2 的主要数字""使用术语 Y""不超过 N 词"。"写得清楚"这类无法判断的条件不算 DoD。
- 检查大纲的对应关系：每条贡献都要在 Introduction 中提出，在 Method 中有对应机制，在 Experiments 中有对应证据。
- 摘要和引言的大纲直接从 spec 的叙事骨架展开：摘要按 `references/sections/abstract.md` 第 1 节选作用序列，逐句写出每句的作用；引言按 `references/sections/introduction.md` 第 1 节选段落序列，逐段写出每段的功能。
- 大纲需要用户确认。

## 3. 写作（逐节进行）

对每一节：

1. 读 `references/word_style.md` 第 1 节（写作原则）和第 4 节（去 AI 味规则）、`references/sections/<节>.md`，以及 spec 和大纲中这一节的内容。
2. 涉及方法或实验时，先读对应的代码和结果文件，核对名称、公式、超参数和数字。
3. 按大纲逐段写，满足每段的 DoD，同时遵守文风画像、错题本和去 AI 味规则（`references/word_style.md` 第 4 节）。先确定每句话的功能，再到 `references/sentence_bank.md` 的对应类别里挑句式，替换成本文的具体内容；同一个句式在全文中不要反复使用。用词和风格参数遵循 `references/word_style.md` 第 2、5 节。
4. 直接写入论文文件（.tex 或 .md），并把大纲中这一节的 `status` 改为 `drafted`。
5. 写完按 `references/word_style.md` 第 4.9 节自查：运行扫描脚本，level=avoid 的命中全部处理，level=review 的命中逐条判断；再人工检查脚本查不出的项。

## 4. 审查

用 Agent 工具启动一个 general-purpose 子代理做独立审查。子代理看不到写作时的推理过程，能减少自己审自己时的放水。prompt 模板如下，其中 `<skill 目录>` 要替换成实际的绝对路径：

> 你是这篇论文的独立审稿人，只审查，不修改任何文件。
> 请读取：
> - `<skill 目录>/references/review.md`：审查标准和输出格式
> - `<skill 目录>/references/word_style.md`（第 1 节写作原则、第 4 节去 AI 味规则、第 7 节定稿前总检查清单）、`<skill 目录>/references/sections/<节>.md`
> - `<论文仓库>/.paperdna/spec.md` 和 `<论文仓库>/.paperdna/outline.yaml`
> - 待审文件：`<路径>`，范围是 `<节名>`
> 代码和结果在 `<位置>`，涉及方法或数字时请核对。
> 按 review.md 规定的格式返回审查结果。

审查结果里的阻断问题必须处理。

## 5. 修订

- 修正阻断问题后重新审查。最多进行 spec 中"最大修订轮次"规定的轮数，默认 3 轮。
- 达到上限仍有阻断问题时停下，把剩余问题列给用户决定。
- 审查通过后，把这一节的 `status` 改为 `reviewed`，并向用户汇报三件事：改了什么；哪些建议项没有改；还有哪些 TODO（缺引用、缺数据）。

## 6. 沉淀反馈

用户纠正写法或事实时，按 `references/feedback.md` 更新对应文件，然后把新规则用到当前文本上。
