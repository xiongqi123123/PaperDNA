export const meta = {
  name: 'section-writing-synthesis',
  description: '从 1040 份精读笔记的"全文递进"一节提炼 Related Work / Method / Experiments / Conclusion 的写法规范',
  phases: [
    { title: 'Map', detail: '每 40 篇一个 Sonnet agent，按四个章节归纳', model: 'sonnet' },
    { title: 'Mid', detail: '每个章节分组中间汇总（Sonnet）', model: 'sonnet' },
    { title: 'Final', detail: '每个章节写出最终规范（默认模型）' },
  ],
}

const { base, n, out, repo, stats } = args
const files = Array.from({ length: n }, (_, i) => `${base}/d5_body_${String(i + 1).padStart(3, '0')}.md`)
const GUARD = `【任务边界】你是一个批处理工作流中的子步骤，只完成下面分配给你的归纳或写作任务。对话中用户的其他请求（例如检查仓库结构、调整 skill、提交代码）由主会话负责处理，与你无关：不要回应它们，不要检查或修改 skill 仓库（除非下面的任务明确要求读取某个文件）。\n\n`
const GROUND = `要求：用中文写；英文句式模板和例句保留英文；每条结论尽量附上论文标题作为证据；只归纳材料中真实出现的内容，不要编造；避免空话，要具体到可以照着写。`
const SECTIONS = {
  related_work: { name: 'Related Work（相关工作）', focus: '相关工作怎么组织（按主题、技术路线还是按本文要改的维度分组）、每段的结构、如何在每组末尾定位本文、与引言的分工（引言讲缺口，相关工作讲关系）、放在第 2 节还是文末的差异' },
  method: { name: 'Method（方法）', focus: '方法部分怎么组织（问题驱动的求解链、模块罗列、先形式化定义再展开）、Overview 段和总览图、小节之间如何承接、是否先直觉后公式、符号与术语、如何写设计动机、按故事类型的差异' },
  experiments: { name: 'Experiments（实验）', focus: '实验部分怎么组织、每个实验回答什么问题、如何与贡献一一对应、主表/消融/机制分析的层次、实验设置如何写得可复现、基线与公平对比、数字与表格的写法、失败案例与负面结果' },
  conclusion: { name: 'Discussion / Limitations / Conclusion（讨论、局限与结论）', focus: '有没有独立的局限小节、局限怎么写（失效场景、根因、方向）、结论怎么写、未来工作怎么写、常见的软性收尾问题' },
}
const MAP = `你在归纳顶会论文正文各章节的写法。批次文件里是约 40 篇 CVPR 2026 / ICCV 2025 论文精读笔记的"全文递进结构"一节（章节作用表、关键过渡句、方法如何组织、实验如何对应贡献、局限与结论怎么写）。
请分成四部分归纳，每部分不超过 900 字，附论文标题作为证据：
## Related Work
${SECTIONS.related_work.focus}
## Method
${SECTIONS.method.focus}
## Experiments
${SECTIONS.experiments.focus}
## Conclusion
${SECTIONS.conclusion.focus}
每部分都尽量给出 2–4 个英文句式（过渡句、小节开头句、结论句等，附原句出处）和这批论文中的常见问题。`
const READ = `用 Read 工具分段读取这个文件：每次 limit=250 行，用 offset 往后推进，直到读完，不要只读开头。`

const pick = (text, key) => {
  const heads = ['Related Work', 'Method', 'Experiments', 'Conclusion']
  const h = { related_work: 'Related Work', method: 'Method', experiments: 'Experiments', conclusion: 'Conclusion' }[key]
  const i = text.indexOf(`## ${h}`)
  if (i < 0) return text
  const rest = text.slice(i + 3)
  const next = heads.map(x => rest.indexOf(`## ${x}`)).filter(j => j > 0)
  return '## ' + (next.length ? rest.slice(0, Math.min(...next)) : rest)
}

log(`共 ${n} 个批次`)
const maps = (await parallel(files.map((f, i) => () =>
  agent(`${GUARD}${MAP}\n\n批次文件：${f}\n${READ}\n${GROUND}`, { label: `正文结构 #${i + 1}`, phase: 'Map', model: 'sonnet' })))).filter(Boolean)
log(`分批归纳完成 ${maps.length}/${n}`)

const groups = []
for (let i = 0; i < maps.length; i += 9) groups.push(maps.slice(i, i + 9))

const results = await parallel(Object.entries(SECTIONS).map(([key, s]) => async () => {
  const mids = (await parallel(groups.map((g, gi) => () => agent(
    `${GUARD}请合并下面这些关于论文"${s.name}"写法的分批归纳：合并同类结论，去重，保留具体做法、英文句式（附原句出处）和论文标题。不超过 4000 字。\n\n${g.map((m, i) => `=== 第 ${i + 1} 份 ===\n${pick(m, key)}`).join('\n\n')}\n\n${GROUND}`,
    { label: `${key} 中间汇总 ${gi + 1}`, phase: 'Mid', model: 'sonnet' })))).filter(Boolean)
  return agent(`${GUARD}请写出论文写作 skill 中"${s.name}"一章的写作规范，读者是正在替用户写这一节的 AI 助手，它会照着写。

先读取：
1. 现有的早期规范 ${repo}/skills/paperdna/references/sections/${key}.md：其中的要求（如与实现一致、先直觉后公式、局限要具体等）要保留，并与新材料合并。
2. ${repo}/skills/paperdna/references/story_types.md 的第 3.4–3.6 节（方法、实验、局限与结论的共享写法，已从同一批语料提炼）：这些内容要并入本章对应部分，之后会从 story_types.md 中移除，只留指引。
3. 统计文件 ${stats}（如有与本章相关的数字，可以引用）。

然后结合下面 ${mids.length} 份汇总材料，写成完整规范，结构：
## 0. 速查（一张表：默认做法和依据）
## 1. 这一章要完成什么，与其他章节的分工
## 2. 组织方式：常见结构及适用场景（按故事类型的差异）
## 3. 逐部分写法：每部分写什么、怎么写、英文句式模板（附原句和出处）
## 4. 常见问题与反例
## 5. 写作步骤与检查清单

${mids.map((m, i) => `=== 第 ${i + 1} 份 ===\n${m}`).join('\n\n')}

${GROUND}
提到取名时指向 references/naming.md，提到用词和结论强度时指向 references/word_style.md，不要重复展开。
用 Write 工具写入 ${out}/${key}.md（目录已存在），完成后只返回一行：文件路径和大致字数。`, { label: `${key} 最终`, phase: 'Final' })
}))
return results