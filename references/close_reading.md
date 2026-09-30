# 范文精读

用户给出一篇论文，要求精读、拆解写法，或者要学习它的写作时使用。产出一份写作层面的精读笔记。本 skill 的叙事类型、摘要和引言写法、句式库、用词规范，都是从 1040 份这样的笔记中提炼出来的。

## 步骤

1. **获取正文**：按 `references/literature.md` 第 1 步读取 PDF。摘要和引言要逐句看清；参考文献和附录不需要精读。
2. **写笔记**：按 `templates/close_reading_note.md` 的模板逐节填写，YAML 头部各字段都要填。
   - 摘要的每一句、引言每一段的每一句都要进表格，英文原句完整照抄。
   - 分析要具体到这篇论文，每个判断都指向具体的句子或词，不写"逻辑清晰"这类空话。
   - `story_type` 按 `references/story_types.md` 第 2 节的判断流程选。
3. **保存**：
   - 用户在写自己的论文时：保存到论文仓库的 `.vibepaper/refs/<citekey>_reading.md`；
   - 否则：保存到用户指定的位置。
4. **汇报**：告诉用户这篇论文的故事类型、最值得借鉴的 2–3 个写法，以及笔记路径。

## 与现有规范对照

精读完成后，可以把笔记和规范对照，找出这篇论文的特别之处：

- 摘要作用序列和 `references/sections/abstract.md` 第 1 节的常见序列有何不同；
- 引言段落序列和 `references/sections/introduction.md` 第 1 节的哪种排列对应；
- 新出现的好句式，是否值得补进 `references/sentence_bank.md`（先问用户）。

## 批量精读

一次精读几十篇以上时，用工作流为每篇论文起一个 agent，每个 agent 按上面的步骤和模板写一份笔记，完成后再汇总。经验：

- 先把 PDF 统一转成文本（`scripts/parse_pdf.py --main-only`），agent 读文本，只在查看 Figure 1 和核对公式符号时读 PDF 页面；
- 下载语料、批量转文本、批量精读和汇总提炼的脚本与工作流见 `tools/corpus/`；
- 同时只跑一个工作流，多个工作流并行会触发服务端限流；
- Sonnet 的笔记质量与 Opus 相当，批量精读用 Sonnet 即可。
