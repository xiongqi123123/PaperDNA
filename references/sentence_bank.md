# 顶会论文句式库

> 数据来源：1040 篇 CVPR 2026 + ICCV 2025 精读笔记的统计（`references/corpus_stats.md`），以及 6 份分批汇总的句式与命名材料。
> 读者：正在写论文的 AI 助手。本文件是**写句子时的查表规范**，不是范文。
> 约定：模板中 `[方括号]` 为必须替换的占位符；"原句"只在汇总材料保留了原文时给出，其余只列出处论文标题。需要看原文时，按标题回查精读笔记，**不要自己补一个"原句"**。

---

## 0. 如何使用句式库

### 0.1 五步用法

1. **先定功能，再选模板。** 写每一句之前先回答："这句在段落里承担什么功能？"（背景 / 缺口 / 根因 / 洞察 / 方法 / 设计 / 动机 / 结果 / 对比 / 泛化 / 局限 / 过渡 / 图表 / 贡献）。功能定下来，再到对应小节找模板。一句话想同时做两件事时，按"主功能"选模板，次功能用从句补上（例如背景句后半接 `yet ...` 引出问题）。
2. **按位置核对功能是否合理。** 摘要和引言的功能分布有明确规律（见 0.2），写出来的功能序列与统计差得很远时，先检查结构，不要硬套句子。
3. **所有占位符都换成具体内容。** `[方法]` 换成方法名，`[指标]` 换成真实指标名加数字，`[场景]` 换成具体数据集或条件。替换后如果句子读起来仍像"在某领域取得了进展"这类空话，说明占位符填得太抽象，要重写。
4. **同一模板在一篇论文中最多用一次。** 同一骨架（如 `Our key insight is that ...`、`As shown in Fig. N, ...`、`consists of two key components`）全文出现第二次时，换同功能的另一条模板或改写句式。尤其注意"洞察""图表引用""泛化意义"三类，它们的高频骨架最容易重复。
5. **只借结构，不借结论。** 模板里的修饰语（`surprisingly`、`catastrophically`、`exceptional`、`step change`）只有在数据支撑时才保留；没有相应证据就删掉修饰语，只留骨架。

### 0.2 写之前先对照的结构统计（1040 篇）

**摘要**
- 句数：中位数 8（四分位 7–9）；8 句占 25.2%，7 句 19.8%，9 句 18.2%，6 句 11.9%，10 句 11.4%。写到 5 句以下或 12 句以上都属于少数（≤5 句合计约 6.4%，≥12 句合计约 2.0%）。
- 第 1 句作用：纯"背景" 56.6%，"背景+问题" 21.2%，"背景+缺口" 7.3%，直接以"方法"开头 6.6%。以背景（含背景+X）开头的合计 **90.0%**（936/1040）；约 30% 的首句在背景之后顺带抛出问题或缺口（通常用 `yet` / `but` / `while` 连接）。
- 最后 1 句作用："资源发布"（代码/数据开源）43.1%，"结果+意义" 17.9%，"结果" 12.0%，"意义" 10.4%，"结果+泛化" 6.1%。末句含"结果"的合计约 40.2%。
- 按位置（摘要五等分）的主作用：
  | 位置 | 前三名作用 |
  |---|---|
  | 第 1/5 | 背景 57%，问题 18%，缺口 11% |
  | 第 2/5 | 方法 44%，缺口 18%，设计细节 11% |
  | 第 3/5 | 方法 38%，设计细节 35%，洞察 8% |
  | 第 4/5 | 结果 40%，方法 23%，设计细节 20% |
  | 第 5/5 | 结果 42%，资源发布 37%，意义 12% |
- 作用序列高度分散（最常见的一种也只占 2.5%）。最常见的几种：
  - `背景 → 缺口 → 方法 → 设计细节 → 结果`（2.5%）
  - `背景 → 问题 → 方法 → 设计细节 → 结果`（2.1%）
  - `背景 → 问题 → 方法 → 设计细节 → 结果 → 资源发布`（1.9%）
  - `背景 → 缺口 → 方法 → 设计细节 → 结果 → 资源发布`（1.7%）
  
  结论：骨架固定为"背景 → 问题/缺口 → 方法 → 设计细节 → 结果（→ 资源发布）"，"根因""洞察""意义""泛化"是可选插槽，按故事需要插入。

**引言**
- 段数：中位数 6（四分位 5–6）；5 段 29.1%，6 段 27.1%，4 段 16.9%，7 段 15.6%。也就是说一般有 4–6 处段落过渡，第 11 节的过渡句大致也就用这么多次。
- 91.3% 的论文在第一页或引言里放了 teaser 图（Figure 1），所以引言里至少要写一次引用 Figure 1 的句子（第 12 节）。
- 贡献列表：bullet 形式 74.4%，行内段落形式 25.0%，不写贡献列表的只有 0.6%（第 13 节）。

**故事类型**（决定哪几节模板用得最多）
| 故事类型 | 占比 | 重点使用的小节 |
|---|---|---|
| 瓶颈突破型 | 56.0% | 2 缺口、3 根因、5 方法、8 对比 |
| 新问题定义型 | 11.0% | 1 背景、2 缺口（"no benchmark / no dataset"类）、10 意义 |
| 统一框架型 | 10.8% | 4 洞察（"from fragmented to unified"）、6 设计 |
| 发现-解释型 | 10.7% | 3 根因、4 洞察（观察/提问类）、12 图表 |
| 数据与基准型 | 7.0% | 2 缺口（缺数据）、7 结果（"even the best model only ..."）、10 意义 |
| 能力扩展型 / 效率优化型 / 理论分析型 | 2.4% / 2.0% / 0.2% | 7 结果（加速比）、9 泛化 |

### 0.3 写完后的自检清单

- [ ] 每句都能说出它的功能标签；相邻两句功能不重复（除非是"方法 → 设计细节 → 方法"这种有意的展开）。
- [ ] 全文没有两个句子共用同一模板骨架。
- [ ] 所有 `[占位符]` 都已替换；没有残留 `X`、`Y`、`[方法]`。
- [ ] 每个"结果/对比"句都带具体数字、数据集名和基线名。
- [ ] 每个"根因/洞察"句都说出了具体机制，没有停在 "is challenging" 这一步。
- [ ] 强修饰词（catastrophically、remarkable、step change、paradigm shift）有数据或论证支撑，且全文最多用一两次。
- [ ] 摘要末句是资源发布、结果或意义之一；引言以 bullet 贡献列表收尾（或有意写成行内形式）。

---

## 1. 引出背景

**用途**：交代任务是什么、为什么重要、领域最近在往哪走。90.0% 的摘要以背景句开头。
**注意**：背景句不要只写"X 很重要"。最好的背景句在后半句已经埋下张力（`yet` / `but` / `due to`），为下一句的缺口做铺垫。一段引言里最多两句纯背景。

1. `[X] have emerged as the cornerstone of [Y].` ——《AMB3R》
2. `[X] has emerged as a prominent paradigm in [Y].` ——《ActiveAD》
   原句片段："...has emerged as a prominent paradigm in autonomous driving"
3. `[X] has recently emerged as a promising direction for [目标].` ——《ViT3》
4. `[任务] is a fundamental task in [领域A] (and [领域B]) that [核心功能].` ——《CD-Buffer》《Energy-GS》
5. `[X] is a fundamental [field] task that is essential for applications like [A] and [B].` ——《Kaleidoscopic Background Attack》
6. `[X] is a long-standing problem in [field] that solves for [A] and [B] from [C].` ——《Parallel Rigidity Matters》
7. `[X] is a longstanding topic in [领域A] and [领域B], with applications in [应用].` ——《GENMO》
8. `[X] is a challenging and long-standing [field] problem due to [根因].` ——《Shape of Motion》（背景句里直接带出根因）
9. `[X] is a fundamental requirement for [Y] but remains challenging in [场景].` ——《HOLO》（背景+问题）
10. `[X] are the safety-critical backbone of [Y], yet it remains unclear whether [Z] can reliably [V] them.` ——《ENC-Bench》（背景+缺口，适合基准类）
11. `[X] are known for their [强项], yet remain unexpectedly [弱项] due to [根因].` ——《Does YOLO Really Need...》
12. `Recent advances in [领域/任务] have achieved [具体成果].` ——《LF-BVN》
13. `[Field] has recently expanded from [已有设定] to [新设定], yet [新设定] poses distinct challenges.` ——《PixDLM》（适合新问题定义型）
14. `While [现有范式] achieve [优势], adapting it for [新任务] remains challenging.` ——《ReFlex》
15. `[Domain] play a vital role across numerous industries, including [A], [B], and [C].` ——《Video Motion Graphs》（纯重要性论证，慎用，后面必须紧跟具体问题）

---

## 2. 指出局限 / 缺口

**用途**：说明现有工作缺什么，给本文找到位置。摘要第 2/5 段有 18% 的句子是缺口句；最常见的摘要序列就是 `背景 → 缺口 → 方法`。
**注意**：缺口必须具体到"缺哪个维度 / 哪种能力 / 哪类数据"，并尽量说出后果（`leading to ...`、`which significantly limits ...`）。"remains underexplored"这类表述只有在确实没人做过时才用，而且要紧跟一个具体子问题。

1. `Existing [方法类别] typically assume [前提], to be able to [目标].` ——《Agile Deliberation》（揭示隐含假设）
2. `While [现有方法] demonstrate impressive results in [场景], they overlook [被忽略维度].` ——《GOR-IS》
3. `Prior work largely targets [X] while overlooking [Y], defined as [Z].` ——《Where Culture Fades》（在指出缺口的同时给出定义）
4. `Existing methods often overlook [X] while focusing on [Y], leading to [后果].` ——《Two Losses, One Goal》
5. `Existing [X] methods face a core trade-off: either [极端A], failing to [..], or [极端B], [..].` ——《GenErase》
6. `Existing [方法类别] trade off between [A] and [B], and lack [C].` ——《GLMap》
7. `[Method] provides [优势], yet lacks [根本限制].` ——《Understanding and Enforcing Weight Disentanglement》
8. `Despite the recent success of [X], [Y] lags surprisingly far behind [Z].` ——《3D-LATTE》
9. `While [X] have significantly contributed to automating [Y], accurately [Z] remains relatively underexplored.` ——《AnimalClue》
10. `Despite [背景进步], [核心维度/子环节] remains largely unexplored / understudied.` ——《IQA-Adapter》《When Confidence Fails》
11. `Thus, a critical gap remains: a [N] that jointly does [A] and [B] directly from [C].` ——《AeroGS》（冒号后直接描述"理想方法"的样子）
12. `However, existing methods remain unsatisfactory in several aspects: 1) [..]; 2) [..]; 3) [..].` ——《NullSwap》
13. `No benchmark systematically evaluates whether [X] possess [Y]—a critical capability gap as [Z].` ——《ENC-Bench》（基准类）
14. `There is currently no publicly available [X], which significantly limits [Y].` ——《OMG-Bench》（数据集类）
15. `A critical barrier is the lack of any large-scale, public dataset that provides [X] aligned with [Y].` ——《PETAR》（数据集类）

---

## 3. 揭示根因

**用途**：解释现有方法**为什么**失败。这是区分"发现问题"和"理解问题"的一句，瓶颈突破型（56.0%）和发现-解释型（10.7%）论文最依赖它。
**注意**：摘要里单独用一句讲根因的论文不多（例如 `背景 → 问题 → 根因 → 方法 → 设计细节 → 结果 → 资源发布` 只有 4 篇，占 0.4%），根因主要写在引言第 2–3 段。根因句必须指向一个**机制**（耦合、假设失效、误差累积、分布差异），不能写成"因为问题很难"。写完根因，下一句应该自然引出洞察或方法。

1. `The fundamental limitation of [X] is not [常见归因], but [重新归因的根因].` ——《SeDiR》（先否定常见看法，再给出真正原因）
2. `We argue that the issue is [A] rather than [B].` ——《Where Culture Fades》
3. `The cause of this difficulty lies in the fact that [X], where [Y] inevitably [V] [Z].` ——《Batman》
4. `We posit this failure stems from [根因], a problem we formalize using [理论工具].` ——《CIGPose》
5. `This gap is a consequence of [机制差异]: [A] has [属性1], while [B] has [属性2].` ——《Gated KalmaNet》
6. `These failures stem from [N] tightly coupled issues: (1) [标签]: [机制说明]; (2) [..].` ——《IR-HGP》
7. `Existing [X] offer [优点], but rely on [机制], which causes [失效现象], a phenomenon known as [命名].` ——《OSA》（顺带给现象命名）
8. `Because [X] is nonlinear, small errors in [A] compound into visible artifacts like [B].` ——《NeAR》（误差累积型根因）
9. `They assume that [A], yet this correlation often breaks in practice.` ——《CoSMo3D》（假设失效型根因）
10. `The core challenge lies in decoupling [纠缠的X] from [纠缠的Y].` ——《GLINT》
11. `This challenge of [做某事] is mainly due to [根因A] and [根因B].` ——《Wan-Weaver》
12. `We attribute this [discrepancy] to the fact that [根因], [推论].` ——《ViT3》《Variance-Based Pruning》
13. `We identify a critical bottleneck: [具体机制] fail to [目标], leading to [后果1] and [后果2].` ——《LVFace》
14. `This difficulty arises from differences in [A] and [B] between [X] and [Y], so a simple plug-and-play approach fails.` ——《ReFlex》（同时否定"直接套用"的朴素做法）
15. `Why does [X] [fail / occur]? [机制解释].` ——《When Do Models Actually Decide》（设问式，发现-解释型常用）

---

## 4. 提出洞察

**用途**：给出让方法成立的关键观察或视角转换，把"根因"和"方法"连起来。摘要第 3/5 段有 8% 的句子是洞察句。
**注意**：`Our key insight is that ...` 是最高频的骨架（下面有 5 条），**全文最多出现一次**。洞察要能用一句话说清，而且要可验证：最好后面紧跟图或实验来支撑（见第 12 节）。"洞察"和"方法"不要写成同一句话，洞察讲"观察到什么"，方法讲"所以做什么"。

1. `Our key insight is that [对象]'s [属性] can be effectively captured by / through [代理指标/机制], enabled by [具体技术].` ——《ApET》《Z-Order Transformer》
2. `Our key insight is that [X] is not uniform, but rather [Y].` ——《Pluggable Pruning》（否定均匀性假设）
3. `Our key insight is that [观察到的性质] can [产生的效果] when [满足的条件].` ——《WikiCLIP》
4. `Our key insight is to [操作A] and [操作B].` ——《GOR-IS》
5. `Our key insight is to reformulate [问题A] as [问题B的形式], where [约束条件].` ——《GENMO》（问题重述型）
6. `The key insight of our [方法] is to [X], rather than following the standard protocol of [Y].` ——《RayZer》
7. `At the heart of our solution is a key insight: [insight], which we call [term].` ——《Counting Stacked Objects》（给洞察命名）
8. `A key observation is that [现象] is [连续性质] and not purely [离散性质].` ——《Keep It Frozen》
9. `We observe that [现象] gradually [V] in [过程], effectively serving as a natural [目标术语].` ——《CFG-Ctrl》（把副产物重新解释成信号）
10. `The key finding is that [X] defines a [Y] in [Z].` ——《Neighbor GRPO》
11. `Therefore, the key is not to [朴素目标] globally but to [精确目标].` ——《Draft and Refine with Visual Experts》
12. `We propose shifting the paradigm from fragmented [X] to unified [Y].` ——《D4RT》（统一框架型专用）
13. `We therefore raise a more fundamental question: rather than [常规做法], can we [替代做法]?` ——《StaMo》
14. `We ask the question: "Do [X] due to [A], or [B]?"` ——《Scaling Language-Free Visual Representation Learning》（发现-解释型：用二选一的提问引出实验）
15. `Motivated by our empirical observation that [现象], we introduce a [方法] that [效果].` ——《Removing Cost Volumes》（把洞察和方法接在一句里，适合摘要）

---

## 5. 提出方法

**用途**：正式引出本文方法（或数据集、基准），给出名字和一句话定义。这是摘要第 2/5 段（44%）和第 3/5 段（38%）的主功能。
**注意**：固定结构是"动词 + 方法名 + 同位语 `a [类别] that [核心功能]`"。名字只负责好记，语义交给同位语（命名句式见 references/naming.md §4.2）。`the first ...` 只在确实能论证"首个"时使用，并且要限定范围（`the first [category] for [setting]`）。

1. `In this paper, we present / propose [方法全称] ([缩写]), a novel framework for [任务] that [机制].` ——《GOR-IS》
2. `We introduce [X] ([ACRONYM]), a [Y] that [Z].` ——《CROWn》《CUPID》
3. `We present [Method], an [首字母对应全称] [类型] framework.` ——《ApET》（用全称解释缩写）
4. `We present [Method Name] ([ABBR]), a method for [task].` ——《EVER》（最简版）
5. `In this work, we propose [X], a [Y] that [Z].` ——《RaUF》
   原句片段："...a spatial uncertainty field learning framework..."
6. `In this work, we propose [全称] ([缩写]), a [类别] that operates by: (i) [..]; (ii) [..]; and (iii) [..].` ——《MOSAIC》（方法句里直接列出机制）
7. `To address [问题], we introduce [方法名], a [A]/[B]/[C] method that [核心功能].` ——《ChordEdit》
8. `To bridge this gap, we propose [方法名] ([缩写]), the first [方法类别] tailored for [目标场景].` ——《PGA》
9. `In this paper, we present [Method], the first (end-to-end) [category / framework] for [task] (tailored for [domain]).` ——《CubiD》《ForestFormer3D》
10. `This paper proposes [方法名], the first [新范式类型] that [核心能力] without [被消除的旧组件].` ——《FUSER》
11. `We introduce [X], the first approach for [V-ing] [Z].` ——《BRICKGPT》
12. `Therefore, we propose [Method], a simple and effective [category] that actively [does X] on [target].` ——《OrthoReg》（强调简单）
13. `We propose [Full Name], or [ACRONYM], a novel [pipeline] that [核心机制].` ——《ETCH》
14. `To address these challenges, we introduce [X]: instead of [V-ing 旧做法], we [V 新做法].` ——《ReFlex》（方法句里带对比）
15. `We introduce [X], the first large-scale, publicly available [Y] that [Z].` ——《PETAR》（数据集/基准类）

---

## 6. 描述设计与动机

摘要第 3/5 段里设计细节占 35%。本节分两部分：6A 讲"由哪些部分组成"，6B 讲"为什么这样设计"。**两者要搭配使用**：每写一个组件，都要有一句说明它为什么不能换成更朴素的做法。

### 6A. 描述设计（组成与流程）

**用途**：交代方法由几个组件或阶段构成，各自负责什么。
**注意**：组件数量写明（two / three），每个组件用"名称 + 功能"成对出现。`consists of [N] key components` 是最高频的骨架，全文只用一次；第二次描述结构时改用阶段式（第 8–9 条）或核心式（第 10–11 条）。

1. `[方法] consists of two core components: (1) [组件A], which [功能]; and (2) [组件B], which [功能].` ——《SocialNav》《CycleManip》
2. `It consists of three synergistic components: (1) [..]; (2) [..]; and (3) [..].` ——《GrOCE》
3. `Our pipeline consists of three key modules: [A], [B], and [C].` ——《RayletDF》
4. `[X] comprises two key components to achieve [A] and [B]: (i) [C], a [D] that [E]; and (ii) [F], a [G] that [H].` ——《Ov3R》（每个组件自带同位语定义）
5. `Our approach consists of two key components: 1) [X] that [Y], and 2) [Z] to [W].` ——《LEADER》
6. `[X] decomposes [大问题] into i) [子模块1], and ii) [子模块2].` ——《MapReduce LoRA》（分解式）
7. `Central to our approach is [核心算法], which decouples [目标] into two components: (1) [..]; (2) [..].` ——《AdaptVision》
8. `First, [component1] [V1]s. Second, [component2] [V2]s. Finally, [component3] [V3]s.` ——《MEDIC-AD》
9. `The first is [阶段A] ... This is followed by [阶段B] ... The final stage is [阶段C].` ——《VGGT-Segmentor》
10. `At the core of [X] is [Y], a [Z] that [核心机制].` ——《VolumetricSMPL》
11. `[方法]'s core innovation is a strategy for [做X]: (1) [..] (2) [..] (3) [..].` ——《GuideFlow》
12. `[方法] combines [组件1] with [组件2]: [组件1] ensures [效果1], while [组件2] enhances [效果2].` ——《SANA-Sprint》（组合式，一句讲清分工）
13. `Internally, we [A] within [B], allowing [C]. Externally, [D] provides [E] to [F].` ——《Depth Any Endoscopy》（内外两层结构）

### 6B. 说明动机（为什么这样设计）

**用途**：说明为什么不用更简单的做法，或者为什么这个设计恰好适合本问题。
**注意**：最有说服力的写法是"先摆出朴素做法，再指出它的具体副作用"（第 1–4 条）。副作用必须具体（destroys [属性]、causes [现象]），不能只写"效果不好"。`Rather than` / `Instead of` / `Unlike` 这类对照骨架各自最多用一次。

1. `A naïve approach would be to [简单做法], but this proves insufficient, as it causes [具体副作用].` ——《AAA-Gaussians》
2. `A trivial solution could [捷径做法], but would consequently destroy [被牺牲的核心属性].` ——《Omnivorous Vision Encoder》
3. `While it is intuitive to [naive choice], this imposes [side effect] that limits [downstream property].` ——《Wanderland》
4. `Recognizing that [standard technique] is often too [limitation] for [setting], we introduce a novel [component].` ——《ZoomEarth》
5. `Rather than using a fixed [基线做法], we define a [新概念] that collectively captures [性质].` ——《Batman》
6. `Rather than [朴素做法], we mimic the behavior of [专家角色], who [真实行为].` ——《Gastric-X》（借领域专家的工作方式来论证设计）
7. `Rather than enforcing [X] as a hard constraint, we treat [Y] as [Z]. This brings key benefits: [..].` ——《PAD-Hand》
8. `Instead of [V-ing 常规做法], [方法] introduces [新机制] by [V-ing 具体操作].` ——《Guiding a Diffusion Model by Swapping Its Tokens》
9. `Unlike previous approaches that [做法A] or [做法B], [X] operates by [做法C], allowing [新自由度].` ——《AIM》
10. `By using [X] rather than [Y] directly, we mitigate [Z] caused by [W].` ——《I'm a Map!》
11. `We employ [具体技术] as our [模型角色] because it naturally restricts [变量] to become [期望性质].` ——《SAFT》（"because it naturally ..."：技术的固有属性刚好满足需求）
12. `While [设计选择] may cause [代价] in [一般场景], in [特定场景], [代价被抵消的理由].` ——《TurboVSR》（解释为合理取舍：说明为什么代价在本场景可以接受，见 `references/anti_defensive.md` §3 第 4 步）

---

## 7. 陈述结果

**用途**：用数字说明方法效果。摘要第 4/5 段有 40%、第 5/5 段有 42% 的句子是结果句；约 40.2% 的摘要末句含结果。
**注意**：结果句必须包含"基准名 + 指标名 + 数字 + 比较对象"。优先写**绝对值 + 相对提升**（第 9 条的写法）。如果结果推翻了某个常见看法，在同一句里点出来（第 10 条）。`Extensive experiments demonstrate` 开头的句子全文最多一句。

1. `On [Benchmark], our model outperforms [N] SOTA methods by [X]% and [Y]%, and reduces [Z] by [A]% and [B]%.` ——《EgoPoseFormer v2》
2. `On the [基准数据集], [方法] sets a new state-of-the-art, achieving [X]% and [Y]% [指标], significantly outperforming prior methods.` ——《VGGT-Segmentor》
3. `Through extensive experiments on [数据集], we outperform existing approaches by [X]% in [指标1] and [Y] dB in [指标2].` ——《GOR-IS》
4. `[X] achieves [指标] improvements of [A]% to [B]% on [benchmark1] and [C]% to [D]% on [benchmark2].` ——《ReFlex》（给区间）
5. `Comprehensive experiments demonstrate SOTA performance, notably reducing [指标] by [N]% on [数据集1] and [M]% on [数据集2].` ——《BridgeDepth》
6. `[X] achieves a [metric] score of [A], significantly outperforming [B] ([C]) and [D] ([E]).` ——《Where Culture Fades》（基线数字放在括号里）
7. `[X] achieves up to [N]% relative improvement over [基线], given a fixed resource budget.` ——《NitroGen》（限定比较条件）
8. `Our method consistently outperforms all baselines, despite using only [更少资源], demonstrating not only [A] but also [B].` ——《Native and Compact Structured Latents》
9. `It achieves an average success rate of [X]%, a +[Y]% absolute improvement over the [基线] baseline.` ——《ForeAct》
   原句："It achieves an average success rate of 87.4%, a +40.9% absolute improvement over the π0 baseline."
10. `This [N]% reduction in [指标] ([A]→[B]) challenges the conventional wisdom that [常见看法].` ——《AToken》
    原句："This 19% reduction in rFID (0.26→0.21) challenges the conventional wisdom that unified models must sacrifice quality for generality."
11. `Despite its simplicity, [X] sets a new state of the art on [Y] (+[N]% [metric]) and delivers clear gains on [Z] and [W].` ——《OVRCOAT》
12. `[X] delivers exceptional efficiency, an [A] speedup over [B] while maintaining [C].` ——《PixelRush》（效率型：加速 + 质量保持）
13. `With these [N] improvements combined, our final [系统] achieves a [X]× speedup, reducing [指标] from [A] to [B].` ——《FlashVDM》
14. `Extensive experiments show [方法] accelerates [指标] from [A] to [B] ([n]×) vs. [基线].` ——《Distilling Diffusion Models》
15. `Even the best model, [模型名], achieves only [X–Y]% accuracy while humans achieve more than [Z]%.` ——《HanDyVQA》（基准类：用"最强模型也不行"来证明基准有难度）

---

## 8. 与基线对比

**用途**：不只报告数字，而是解释本文**为什么**比基线好、好在哪种条件下、代价是否更低。
**注意**：对比句要点名具体基线，并指出**差异来源**（机制、资源、监督）。不是全面领先时收缩主张：写清实际领先的范围，持平的项用 on par with / comparable to（第 3、7 条），不专门写一句落后（`references/anti_defensive.md` §3、§4）。`In stark contrast` / `fails catastrophically` 只用在差距确实悬殊时。

1. `[基线] fails catastrophically when [条件变化]. In contrast, [方法]—which has [关键机制]—achieves [具体数值].` ——《Omnivorous Vision Encoder》
2. `[Baseline]'s [metric] deteriorates from [X] to [Y]. In stark contrast, [Ours] demonstrates exceptional stability [..].` ——《CausalVAD》
3. `Our method exceeds prior work on all [X] except for [Y], where we are roughly on par with [Z].` ——《CLIP Is Shortsighted》（收缩主张：写清领先范围和持平的项）
4. `Compared to [baseline], ours achieves a higher/lower [metric] of [value], reflecting [interpretation].` ——《GardenDesigner》（数字后接解读）
5. `[Method] achieves [metric1], significantly higher than [baseline1/2/3], improving [x]×–[y]×.` ——《PRISM》
6. `Crucially, on [场景], [方法] improves by +[X]%, while [基线] gains only +[Y]%.` ——《AReS》（比较提升幅度）
7. `Our approach achieves comparable performance to the state-of-the-art [基线名], despite significantly less [资源].` ——《MoRe》（持平但更省资源）
8. `[X] consistently matches or outperforms [同类方法], while effectively narrowing the [差距] to [更强基线].` ——《ViT3》（跨类别对比：用 narrowing the gap 的中性说法）
9. `This is remarkable, since [方法] did not use [某种监督/资源]—in contrast to [基线], which leveraged [资源] for training.` ——《Featurising Pixels...》
10. `In contrast, our approach uses a simpler design that does not require [技巧A], [技巧B], or [技巧C] for training.` ——《CoTracker3》（以简单取胜）
11. `Unlike [代表性前作], which requires [限制], our method generalizes to [范围] without [额外代价].` ——《LoftUp》《Radiant Foam》
12. `Compared to [基线], our method achieves [核心能力] via [机制], agnostic to [干扰因素].` ——《Registration beyond Points》
13. `Where [baseline] misidentifies [A] as [B], [ours] correctly identifies these as [C].` ——《Curvature-Aware Captioning》（定性对比，常配图）
14. `This is [N]× greater in [A] and [M]× broader in [B] than any existing [Y] to date.` ——《SA-FARI》（数据集规模对比）
15. `As suggested by the name, [新方法] operates in the opposite direction of [最相关前作].` ——《UnZipLoRA》
    原句："As suggested by the name, UnZipLoRA operates in the opposite direction of ZipLoRA."

---

## 9. 泛化与意义

**用途**：说明结果不限于一个设定（泛化），以及这项工作对领域意味着什么（意义）。摘要末句中"意义"占 10.4%，"结果+意义" 17.9%，"结果+泛化" 6.1%，"泛化+意义" 3.8%。
**注意**：泛化句要列出**跨了什么**（数据集数量、骨干网络数量、任务种类）。"范式转变"类句子（第 6、7、13 条）全文**只选一条**，并且只有在本文确实改变了问题的做法时才用。数据与基准型论文的意义句通常落在"为后续研究奠定基础 / 开放资源"上（第 11、12 条）。

1. `[方法] yields consistent improvements across [N] benchmarks when integrated into [M] strong backbones, demonstrating generalization.` ——《AD-GBC》
2. `[Method] consistently alleviates [problem] across multiple [variants], diverse [backbones], and various [tasks]. This demonstrates robustness, scalability, and general applicability.` ——《GRPO-Guard》
3. `Extensive experimental results show that [X] achieves state-of-the-art performance on [Y], and exhibits strong generalization ability on [Z].` ——《LMM4LMM》
4. `By leveraging [某种先验/资源], [X] can be trained using only [受限的监督信号] while generalizing well to [目标场景] in a [方式] manner.` ——《Geo4D》
5. `The method is both [属性A]-agnostic and [属性B]-agnostic, enabling [应用范围].` ——《SeaCache》
6. `By [核心能力], our work shifts the paradigm from [旧范式] to [新范式], paving the way for [愿景].` ——《HoloCine》
7. `[Component] marks a step change in [field]—from [旧范式] to [新范式].` ——《Relightable Holoported Characters》
8. `By [核心机制转变], [方法] takes a step toward [长期愿景] that [终极能力].` ——《Counterfactual VLA》（比"范式转变"更克制）
9. `This challenges the prevailing assumption that [常规假设] are necessary for [任务].` ——《PercHead》
10. `This work serves as a proof of concept, offering a compelling [X] alternative to the [Y]-dominated trend.` ——《Scaling Language-Free Visual Representation Learning》
11. `By establishing the first rigorous [X], we open a new research frontier at the intersection of [A] and [B].` ——《ENC-Bench》
12. `By [V-ing X] and [V-ing Y], we envision [BENCHMARK] as a foundation for future research on [领域].` ——《VS-Bench》
13. `These contributions together signal a new paradigm of [领域]—advancing from [旧范式] to [新范式].` ——《Visual Chronicles》
14. `By releasing our [工具/资源] alongside [数据集], we aim to set a new standard for [研究方向].` ——《Multi-View 3D Point Tracking》（资源发布 + 意义，对应 43.1% 以资源发布收尾的摘要）
15. `We hope this work encourages moving from [X] toward [Y].` ——《PHASE-Net》（谦逊式收尾；只能跟在一句有依据的意义陈述之后，不能单独作为全文最后一句，见 `sections/conclusion.md` §3.7）

---

## 10. 局限：适用边界 + 方向

**用途**：在结论之前的 Limitations 段或结论中间，用一两句说明方法的适用边界，并指出后续方向。
**注意**：最多 2 条，每条一两句，写成"适用边界 + 后续方向"，根因可以省略（`references/anti_defensive.md` §5）。不放在摘要、引言里，不作为全文最后一句。不用自我削弱的写法（unfortunately、we must acknowledge、still lags behind、limited improvement），不写情绪化的自我评价，也不在局限里重提正文已经收缩掉的比较。不要写成变相夸奖（例如"我们的方法只在 N 个数据集上验证过"）。常用写法两种：划定适用范围（第 1–4 条）、说明依赖的假设并给出方向（第 5–13 条）。

1. `[系统] is limited to being a [能力定位], not designed to [超范围能力1], [能力2] or [能力3].` ——《NitroGen》
2. `Our approach is tailored to [适用场景]. It is not designed for [超出范围的场景].` ——《Clay-to-Stone》
3. `Scope of this Work. We evaluate [具体条件] in [受控设定] [..]; this does not directly reflect [更广泛的真实场景].` ——《DENALI》（单独成段的"Scope"小标题；放在基准设计处或结论之前，不放进引言）
4. `We focus on [场景]; handling [更广的场景] is left for future work.` ——`anti_defensive.md` §5
5. `Our method assumes [前提]; extending it to [放宽前提的设定] is a natural next step.` ——`anti_defensive.md` §5
6. `A limitation is [constraint]; [assumption] may not hold in [failure condition]. Future work includes [A] and [B].` ——《Generalized-CVO》
7. `[X] requires [前提条件]. Therefore, it cannot be trivially applied to [反例场景].` ——《NeoVerse》
8. `While [property] is beneficial for [use case], it can become a limitation when [opposite use case].` ——《FlowEdit》（同一属性的两面）
9. `While acceptable for [场景A], it hinders [场景B]. A promising direction is [改进方向].` ——《Inside-Out》
10. `While our method achieves SOTA performance, several limitations remain. First, it does not explicitly [未建模因素], leading to [后果].` ——《GOR-IS》（只写两条时把 several 换成具体条数）
11. `A remaining limitation is that [具体场景]; we believe this can be mitigated in future work.` ——《FEAT》
12. `This study constructs the first [X], but does not explore [Y]. This will be investigated along with [Z] in future work.` ——《SDTrack》
13. `The main limitation of our method is [specific limitation]. [..] We leave this for future work.` ——《FlashDepth》

---

## 11. 段落过渡

**用途**：连接引言各段（引言中位数 6 段，所以一般有 4–6 处过渡），让"缺口 → 方法""观察 → 提问""前提 → 新洞察"之间的转换有逻辑承接。
**注意**：按过渡类型选模板，不要每段都用 `To this end`。以下按类型分组：缺口转方法（1–6）、设问（7–11）、转折/反驳（12–14）、递进（15）。

**缺口 → 方法**
1. `To this end, we introduce [方法], a [类型] that corrects [问题] both during and after [阶段].` ——《AdaPrior》
2. `To this end, we augment [existing framework] with a lightweight module designed for [goal].` ——《GenHOI》
3. `To this end, we leverage [某设计], which is designed with [特性] for [目的].` ——《ReTracker》
4. `Motivated by these limitations, we introduce [方法], a novel framework comprising (i) [..], (ii) [..], (iii) [..].` ——《BioVITA》
5. `Building on these observations, we introduce [Method], addressing [限制] via [Module1] and [Module2].` ——《FixTalk》
6. `Different from the above works, we propose a new approach: [核心差异点].` ——《FabricGen》（从相关工作过渡到本文）

**设问**
7. `This raises a central question: Can we [A] while retaining [B], and do so without [C] or [D]?` ——《LATA》
8. `Therefore, the question arises: How can we [核心研究问题]?` ——《DLF》
9. `If this path is so clearly superior, why has it not yet dominated?` ——《Lafite》（反问式，下一段回答障碍）
10. `This has led us to rethink [X]: is the default use of [Y] in line with practical requirements?` ——《Rethinking Key-frame-based...》
11. `This gap in understanding motivates our work. To move from description to explanation, we must address [N] questions.` ——《Understanding and Enforcing Weight Disentanglement》（发现-解释型：把缺口转成待回答的问题列表）

**转折 / 反驳**
12. `However, [X] are no silver bullet.` ——《Global SfM》（短句转折，用在大段肯定之后）
13. `In this work, we argue that this trade-off is not fundamental.` ——《InstantViR》（紧跟 trade-off 型缺口，第 2 节第 5–6 条）
14. `We depart from [旧范式] to propose a new paradigm of [新范式].` ——《One Trajectory, One Token》

**递进**
15. `Having shown that [已证明的前提], our final insight is that [新洞察].` ——《LiDAR系统设计》（多段层层推进的洞察，最后一层用这句收束）

---

## 12. 引用图表与公式

**用途**：让读者去看图表，并且**告诉读者应该从图里看到什么结论**。91.3% 的论文有 teaser 图（Figure 1），引言里至少会引用一次。
**注意**：`As shown in Fig. N` 后面必须接一个具体结论（谁比谁高、哪种方法在哪里失败），不能只写 `shows the results`。`As shown/illustrated in` 这个骨架全文会出现多次，所以要轮换第 1、2、5、11、14 条这类**不以 As shown 开头**的写法。
**公式**：6 份汇总材料中**没有**收录引用公式的句式，这里不提供模板，也不要凭空编造；需要时回查精读笔记中的方法章节。

**Figure 1 / teaser 图**
1. `Figure 1 highlights a consistent and surprising failure mode: when [condition], [system] produce [具体负面结果].` ——《2D-LFM》（用图 1 展示失败模式来引出问题）
2. `As shown in Fig. [N], no existing [Y] excels universally; some achieve [A] but [B], while others [C] yet [D].` ——《WorldLens》（用图展示现有方法的 trade-off）

**用图展示现有方法的失败**
3. `As shown in Fig. [N], [prior method]'s [output] suffers from [failure mode], hindering / yielding [consequence].` ——《SGAD》《PGA》
4. `As illustrated / shown in Fig. [N]([x]), [具体失败/成功案例].` ——《WorldMM》

**用图支撑观察或洞察**
5. `As illustrated in Figure [N], based on [Y], [A] account for only about [P]%, whereas [B] occupy roughly [Q]%.` ——《PaddleOCR-VL》（用统计图给出比例）
6. `As shown in Fig. [X], [观察/证据] reveals that [具体现象].` ——《GLMap》《STRNet》
7. `As shown in Fig. [N], [X] exhibits significantly higher [Y] than [Z], thereby providing [W].` ——《ReFlex》
8. `As illustrated in Fig. [n], the distance between [A] and [B] is significantly smaller than the distance between [C] and [B].` ——《ESSENTIAL》（特征空间距离）

**多面板 / 多要点图**
9. `As shown in Figure [N], [面板A] illustrates [X], [面板B] presents [Y], and [面板C] highlights [Z].` ——《Gastric-X》
10. `As illustrated in Figure [N], [现象总述]. First, [..]; Second, [..]; Third, [..].` ——《WeaveSeg》
11. `As illustrated in Fig. [N] ([row/col 位置]), [X] evaluates whether a model can [Y].` ——《GeoMMBench》（基准类：逐格说明任务）

**表格 / 消融**
12. `As shown in Table [X], adding [组件] consistently improves the baseline across all metrics.` ——《EffectErase》
13. `Comparing Table [X] (a) and (b), we observe a substantial improvement from [N1] to [N2] [指标], showing the importance of [Z].` ——《RobotSeg》
14. `Removing / Without [模块], [具体失败案例], e.g., [举例] (see Fig. [N]).` ——《SPARK》（消融结论在前，图号放在括号里）
15. `The result is a substantial [reduction/improvement] in [指标], enabling [新能力] (see Figure [X]).` ——《MeshRipple》

---

## 13. 贡献列表

**用途**：在引言末尾列出本文贡献。统计显示 bullet 形式 74.4%，行内段落形式 25.0%，不写的只有 0.6%。**默认用 bullet**。
**贡献类型的搭配**（1040 篇）：含 Performance 的 91.8%，含 Capability 的 79.1%，含 Insight 的 64.8%。最常见的组合是 Capability+Performance（24.9%）、Insight+Performance+Capability（21.2%）、Insight+Performance（19.6%）。按记录顺序，Insight 排在第一位的占 60.7%。
**写法规则**：
1. 一般写 3 条，结构为：①洞察/发现（Insight） → ②方法/数据集/基准（Capability） → ③实验结果（Performance）。数据与基准型论文把②换成资源本身。
2. 每条以强动词开头（We identify / We propose / We introduce / We construct / Extensive experiments show），同一动词不重复。
3. 每条都要可验证：洞察条写出现象，方法条写名字和核心机制，结果条写基准和幅度。
4. 贡献列表的措辞不要照抄摘要，至少换掉句式骨架。

**注意**：汇总材料里明确属于"贡献列表"的句式只有第 1 条。第 2–12 条原本出现在引言或摘要的其他位置，按贡献类型整理在这里，改写成 bullet 时可以直接套用骨架。

**引导句**
1. `In summary, we make [N] main contributions. First, [..]. Second, [..]. Finally, [..].` ——《What Makes Good Synthetic Training Data》（行内形式的标准写法）

**Insight 条**
2. `We identify a critical bottleneck: [具体机制] fail to [目标], leading to [后果1] and [后果2].` ——《LVFace》
3. `We posit this failure stems from [根因], a problem we formalize using [理论工具].` ——《CIGPose》（发现 + 形式化）
4. `At the heart of our solution is a key insight: [insight], which we call [term].` ——《Counting Stacked Objects》

**Capability 条（方法）**
5. `We propose [全称] ([缩写]), the first [方法类别] tailored for [目标场景].` ——《PGA》
6. `[X] comprises two key components to achieve [A] and [B]: (i) [C], a [D] that [E]; and (ii) [F], a [G] that [H].` ——《Ov3R》

**Capability 条（数据集 / 基准）**
7. `We introduce [X], the first large-scale, publicly available [Y] that [Z].` ——《PETAR》
8. `This is [N]× greater in [A] and [M]× broader in [B] than any existing [Y] to date.` ——《SA-FARI》（规模论证，接在数据集条后）
9. `By establishing the first rigorous [X], we open a new research frontier at the intersection of [A] and [B].` ——《ENC-Bench》

**Performance 条**
10. `Extensive experimental results show that [X] achieves state-of-the-art performance on [Y], and exhibits strong generalization ability on [Z].` ——《LMM4LMM》
11. `On [Benchmark], our model outperforms [N] SOTA methods by [X]% and [Y]%, and reduces [Z] by [A]% and [B]%.` ——《EgoPoseFormer v2》

**资源 / 收束条**
12. `By releasing our [工具/资源] alongside [数据集], we aim to set a new standard for [研究方向].` ——《Multi-View 3D Point Tracking》

---

> 取名（要不要起名、命名策略、标题结构、名字第一次出现时的命名句式）见 references/naming.md。
