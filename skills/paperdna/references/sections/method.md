# 顶会论文方法章节（Method）写法规范

> 数据来源：1040 篇 CVPR 2026 + ICCV 2025（best / oral / highlight）精读笔记中关于方法章节的分批归纳（三份合并材料，覆盖约 25 个批次、300 余篇有详细方法分析的笔记），以及 `references/story_types.md` 原第 3.4–3.6 节（已并入本文）和原 `sections/method.md` 的六条要求（已并入本文）。
> 标注 **[stats]** 的数字直接取自 `references/corpus_stats.md`。标注 **[批次估计]** 的比例是各批次笔记各自估出来的区间，不是全样本精确统计，按"多数 / 少数"理解即可。书名号《》里是真实论文标题或方法名；英文例句是原句，句式模板里的 `X`、`[...]` 是待填槽位。
> 用法：动笔前先看第 0 节，按第 2 节选组织方式，按第 3 节逐部分写，写完按第 5 节清单自查。
> 相关文件：方法名、模块名、现象名的取法见 `references/naming.md`；"一个概念一个词、一个量一个符号""先观察后方案"等用词和结论强度问题见 `references/word_style.md`（原则 3、7、8）；实验如何对应方法小节见 `sections/experiments.md`；局限与结论的写法见 `sections/conclusion.md`；叙事类型的判断见 `references/story_types.md` 第 2 节。

---

## 0. 速查：默认做法和依据

| 项 | 默认做法 | 依据 |
|---|---|---|
| 整体组织 | **问题驱动的求解链**：每个小节解决上一小节留下或暴露出的具体问题，上一节的输出就是下一节的输入；不要写成 A + B + C 模块清单 | 三份材料一致的结论，各批次估计占 65%–90% [批次估计]；《E-RayZer》《Real-Time Neural Video Compression》《WINS》 |
| 章首 | 一段 Overview + 一张总览图，复述引言里的目标句，并用 "(Sec. 3.x)" 预告后面每个小节 | "几乎是标配"（三份材料一致）；《Native and Compact Structured Latents》《AAA-Gaussians》《StreamFormer》 |
| 记号 | 在方法主体前设 Preliminaries / Problem Formulation，统一符号；符号首次出现即定义，全文一个符号只表示一个东西，并与 spec 的术语与符号表一致 | 《SeDiR》《OVI-MAP》《Consensus-Driven Active Model Selection》；原 method.md 要求 |
| 小节开头 | 先重述上一节遗留的问题，或直接复用上一节的输出变量名 | 《Midas Touch》《HyperGait》《ComPose》《BA-Track》 |
| 公式段 | **先直觉后公式**：动机句 → 编号公式 → where 从句解释符号 / 一句话复述物理含义 | 各批次估计 75%–90% 以上的子模块这样写 [批次估计]；《RnG》《SenCache》《GrOCE》 |
| 例外 | 只有理论型、统一框架的形式化部分可以先给 Definition / Theorem，再用 "Intuition." / Remark 段补直觉 | 《AdaPrior》《2D-LFM》《FloodDiffusion》 |
| 设计理由 | 每个设计都说明"为什么不用更简单的做法"；最常用"朴素方案 → 具体失败原因 → 我们的方案"，并让这个理由在消融里有对应实验 | 《AAA-Gaussians》《Att-Adapter》《Mamba Learns in Context》；原 method.md 要求 |
| 收尾 | 用统一目标函数、训练 / 推理流程或 pipeline 小节把各部分串起来 | 《Scaling Dense Event-Stream Pretraining》式 (5)；《TF-CADE》4.4 |
| 与实现一致 | 模块名、损失、超参数、训练流程与代码一致；先读代码再写；不一致时问用户以哪边为准 | 原 method.md 要求 |
| 与实验对应 | 贡献 i ↔ 方法 3.i ↔ 表 i；消融变体用 "w/o 模块名"，模块名与方法小节完全一致 | story_types 原 §3.5；《Mamba Learns in Context》三组件与贡献列表严格对应 |
| 故事类型差异 | 瓶颈突破型写"诊断 → 对症"链；发现-解释型先设分析节再回指；统一框架型先形式化；数据与基准型写流水线、公式极少 | 瓶颈突破型占 56.0% [stats]；见第 2.6 节 |
| 细节去向 | 正文保留足以复现核心设计的公式和关键超参；补充材料只放补充，不放核心 | 反例《NitroGen》《AVGGT》几乎不用编号公式，细节全推给补充材料 |

---

## 1. 这一章要完成什么，与其他章节的分工

### 1.1 四个任务

1. **讲清做法**：读者读完能说出输入是什么、经过哪几步、输出是什么、用什么目标训练。总览图 + 路线图句负责全局，小节负责局部。
2. **讲清为什么这样做**：每个设计都要回答"它解决哪个具体问题""为什么不用更简单的做法"。这是方法章节与技术报告的区别。三份材料都观察到，顶会论文的设计动机几乎都通过**具体失败观察、反证实验或类比**引出，而不是"we design a module"直接开场。
3. **给出可复现的信息**：核心公式、关键超参数和训练流程写在正文。可以把推导、完整超参表放进附录，但核心设计不能只在附录出现。
4. **与实现一致**：方法章节写的是代码实际做的事。模块名、损失函数、超参数、训练流程都要与代码对得上。先读代码再写；代码与论文草稿描述不一致时，停下来问用户以哪边为准，不要自行选择。

### 1.2 与其他章节的分工

| 章节 | 负责什么 | 与方法章节的接口 |
|---|---|---|
| 引言 | 问题、根因、洞察、方法名、贡献列表 | 方法章节的 Overview 复述引言的目标句；引言 P5 里"每个模块对应一个根因或挑战"的顺序，就是方法小节的顺序（story_types 原 §3.2）；根因与现象的名字全文一致（`word_style.md` 原则 8） |
| 预备 / 分析节 | 记号、背景方法回顾；发现-解释型的实证分析 | 方法各设计点显式回指分析结论："Based on the layer-wise analysis in Sec. 3, ..."（《AVGGT》） |
| 方法 | 每个设计、它的动机、它的公式 | 本文 |
| 实验 | 证据 | 贡献 i ↔ 方法 3.i ↔ 表 i；方法小节标题与消融小节标题同构（《PET-DINO》），但方法正文不写 "ablated in Sec. 4.3" 这类指向实验的引用（章节之间的引用规则见 `references/workflow.md` 第 3 节）。写法见 `sections/experiments.md` |
| 局限 / 结论 | 适用边界与后续方向（最多 2 条） | 方法里显式写出的假设和前提，是局限最主要的来源（见第 3.12 节）。写法见 `sections/conclusion.md` 和 `references/anti_defensive.md` §5 |
| 附录 / 补充材料 | 证明、完整推导、完整超参、额外细节 | 只补充，不替代；理论型"证明放附录、正文只留命题 + 直觉"（《Drainage》《D-Convexity》） |

### 1.3 动笔前要准备的东西

- 代码（或用户对实现的描述）：确认模块名、数据流、损失项及权重、训练阶段、推理流程。
- spec 里的术语与符号表：方法里新增的符号先登记再使用。
- 引言草稿的挑战列表 / 根因列表 / 贡献列表：方法小节要与它们一一对应。
- 消融实验清单：每个"为什么不用更简单的做法"的理由，最好能指到一个消融。

---

## 2. 组织方式：常见结构及适用场景

### 2.1 默认：问题驱动的求解链

后一小节的输入是前一小节的输出，或者是前一方案暴露出的新问题；末尾常以统一目标函数或 pipeline 收束。材料里有四种常见的链形：

**(a) 方案 → 新问题 → 再方案**（最典型的"链"）
- 《E-RayZer》：3.1 指出隐式 3D 的局限 → 3.2 给显式 3D 方案，但暴露训练不收敛的新问题 → 3.3 用课程学习解决。
- 《Real-Time Neural Video Compression》：intra 能力问题 → 两帧压缩 → 引入"双帧质量分配"新问题 → 双帧量化表解决 → 训练策略收尾。
- 《WINS》是"方法链的方法链"：提出 WINS → 发现负载不均衡 → WINS-B → 再发现权衡问题 → WINS-AB。
- 《ReFlex》4.2 针对"提取不准"给方案，4.3 针对"提取准了但编辑性下降"的新问题再给 adaptation。

**(b) 先诊断出多个缺陷 → 逐一对症**
- 《240FPS Stereo Vision from Monocular Mixed Spikes》先给成像模型，诊断出三类具体缺陷，再逐一设计对应模块。
- 《FUSER》3.2.1 列出 (i)–(iv) 四条局限，3.2.2–3.2.4 依次解决。
- 《MAGICIAN》列出 i)/ii)/iii) 三个挑战，3.3/3.4/3.5 逐一求解。
- 《Mirror Illusion Art》3.1 给统一优化目标后写 "during optimization, we identified four main challenges"，3.2–3.5 逐一解决。
- 《RALU》先用 Remark 1/2 诊断两类伪影，4.1/4.2 逐一解决。

**(c) 理想目标不可行 → 变换 → 可行解**
- 《DSO》3.1 给出不可优化的理想目标 → 3.2 用数学变换消去不可算项 → 3.3 解决"数据从哪来"。
- 《Vocabulary Scaling Law》目标函数 intractable → 子集重构为双层优化 → Theorem 证明贪心近似可用。
- 《Counting Stacked Objects》先写朴素公式 N=V/v → 指出 "fails to account for gaps between objects" → 修正公式 → 3.2/3.3 分别求解未知项。
- 《SeaCache》4.1 推导理论频率响应 → 4.2 解决"该表示不可直接用"的问题。

**(d) 沿阶段顺序、每阶段交接输出**
- 《D4RT》3.2 "This stage inputs bounding boxes and rotation distributions..." 直接承接 3.1 的输出。
- 《GrOCE》CONSTRUCT → IDENTIFY → SEVER，"IDENTIFY can be taken as a pre-processing component of SEVER"。
- 《BA-Track》Motion-Decoupled 3D Tracker → Bundle Adjustment → Global Refinement，3.3 用遗留问题过渡："BA processes only a sparse set of query points...we need global refinement"。

**适用**：瓶颈突破型（几乎全部）、效率优化型、多数新问题定义型。有明确"待解问题"的方法都默认用它。

### 2.2 并列大模块 + 模块内部小循环

模块之间没有因果依赖，但每个模块内部仍是"挑战 / 动机 → 解法"的小闭环。
- 《NitroGen》数据 / 评测 / 模型三个并列模块，每个模块内部先陈述挑战再给解法。
- 《ETCTrack》ATC 与 HIBlock 并列，各自先动机后公式。
- 《Easy3D》沿数据流排序（预处理 → 编码 → 点击编码 → 解码 → 融合 → 后处理），但每个模块内部都先对比基线局限再给设计。
- 《GENMO》3.1 模块罗列架构，3.2 用问题驱动写训练范式。

**适用**：统一框架型、多组件系统。**要求**：按数据流排序；模块内部必须有动机句；模块之间至少有一句交接（谁的输出送给谁）。

### 2.3 先形式化，再模块化 / 实例化

- 《Gallant》先用 POMDP 统一形式化，再按数据流模块化。
- 《SADTR》3.1 先给 Definition 1 的整体公式，再拆子模块。
- 《VS-Bench》先统一 POMG 形式化，再按三类场景展开。
- 《Cov2Pose》用 Φ=Ψθ2∘Γθ1 把问题拆成两个求解子节。
- 《WHU-MARS》"We first formalize...then present a unified single-branch baseline...and finally introduce..."。

**适用**：统一框架型、新问题定义型、需要一套统一记号支撑多个组件的方法。

### 2.4 发现驱动：分析 / Pilot Study → 按发现逐条设计

- 《What to Distill?》先做 Pilot Study 得到四条 Finding，再一一对应设计模块。
- 《Diffusion Image Prior》3.3 先用 Q1/Q2 实证得出"两阶段现象"，3.4 才设计停止准则。
- 《FedAdamom》第 4 节先给三个逃逸时间定理诊断根因，第 5 节才提出方法。
- 《EVEv2》"Preliminary studies indicate that earlier variants struggle to fully harness X due to Y. To overcome this, we transform..."。

**适用**：发现-解释型；瓶颈突破型里根因需要实验坐实的情况。

### 2.5 流水线 / 工程流程罗列

- 《Hoi!》硬件 → 采集协议 → 后处理 → 标注。
- 《Derm1M》Step 1–5 平铺数据构建流程；《LVBench》采集 → 任务定义 → QA 生成 → 质控；《SA-FARI》Data Collection → Species Annotation → …。
- 《M3DLayout》《MV-Fashion》先统一问题形式化，再并列给出若干独立基线，公式极少。
- 《RealAppliance》按 Step 1–4 推进，用接口伪代码代替数学表达；《InfiniBench》全文无公式，用流程图 + 编号步骤代替因果推导。

**适用**：数据与基准型、系统 / 工程型。这是"先直觉后细节"对"先直觉后公式"的替代。**要求**：每一步仍写"为什么需要这一步"（例如质控步骤要说明它排除了什么错误）。

### 2.6 定义 → 定理 → 统一

- 《Drainage》《D-Convexity》"定义 → 定理 → 与已有工作统一"，证明放附录，正文只留命题 + 直觉。
- 《PLMP》以 Definition / Theorem / Proposition 为骨架，定理证明链代替传统实验章节。
- 《AD-GBC》反复用"朴素方案 → 证明失效（Theorem）→ principled 解"三段式。

**适用**：理论分析型（样本仅 2 篇 [stats]，规律仅供参考）；其他类型里带理论保证的部分。

### 2.7 按故事类型选择

| 故事类型 | 占比 [stats] | 方法章节的默认组织 | 例子 |
|---|---|---|---|
| 瓶颈突破型 | 56.0% | 2.1 求解链：诊断具体缺陷 → 逐一对症 → 统一目标函数；常见"解决 A → 暴露 B → 解决 B" | 《240FPS Stereo Vision》《E-RayZer》《HamiPose》《Reward Forcing》《Revisiting the Necessity of Full Accuracy》；《ViterbiPlanNet》《GuideFlow》《CausalVAD》"诊断 → 通用原则 → 落地模块" |
| 新问题定义型 | 11.0% | 先给正式 Definition，再用对称小节"先点名尚未解决的具体缺口，再给方案" | 《Widget2Code》《ZoomEarth》《SABER》；《DreamOmni2》《Designing to Forget》；《FILTR》第 3 节 "Do 3D encoders understand topology?" |
| 统一框架型 | 10.8% | 2.3 先形式化再模块化，或 2.2 总览 + 模块并列；章节名常直接对应贡献列表条目；常在核心方法后加应用 / 下游适配小节 | 《SLARM》《ReMoT》《AToken》《GLMap》《CoST》《OminiControl》；《NaTex》3.3 Applications |
| 发现-解释型 | 10.7% | 2.4：先专设分析节（常命名为 Observation / Verification 而非模块名），方法各设计点显式回指分析结论 | 《AVGGT》；《Is the Modality Gap...》"From Sec. 3 we conclude that...Theorems 3.4 and 3.5 provide us with a tool to do so"；《Improving Motion in Image-to-Video Models》Observation → Hypothesis → Diagnosis；《FlowEdit》理论重解 → 合成实验反驳 → 新 ODE |
| 数据与基准型 | 7.0% | 2.5 流水线或"任务 → 指标"平行结构；公式极少或为零；基线部分并列 | 《EgoSound》《EgoXtreme》《Hoi!》《PanoEnv》《GEOBench-VLM》；《PAI-Bench》三赛道内部结构完全对称；《MIORe》先建问题空间分类学再展示覆盖 |
| 能力扩展型 | 2.4% | 用并列案例模板重复同一骨架 | 《Visual Diffusion Models are Geometric Solvers》三个案例共享 "Problem Statement → Existing Methods → Method → Evaluation" |
| 效率优化型 | 2.0% | "profiling 发现瓶颈 → 给方案"的链 | 《VMonarch》3.4 节标题即用 profiling 引出 |
| 理论分析型 | 0.2% | 2.6 定义 → 定理 → 统一；公式 / 定理占比远大于直觉文字 | 《PLMP》《Registration beyond Points》《RePoseD》 |

**选择步骤**：
1. 确定主故事类型（`references/story_types.md` 第 2 节）。
2. 问自己：我的每个模块是不是在回答上一个模块留下的问题？是 → 2.1；模块之间确实独立 → 2.2（模块内部仍写小循环）。
3. 需要一套记号贯穿多个模块，或要把多个任务写进同一形式 → 在前面加 2.3 的形式化小节。
4. 根因要靠实验或定理坐实 → 在方法前（或方法第一节）加 2.4 的分析节。
5. 核心贡献是数据或基准 → 2.5，但每一步仍写动机。

---

## 3. 逐部分写法

一个完整的方法章节通常依次包含：章首 Overview（3.1）→ Preliminaries / 问题形式化（3.2）→ 若干设计小节，每个小节由"承接句（3.3）→ 设计动机（3.4）→ 先直觉后公式（3.5）→ 收尾 / 引出下一问题（3.6）"组成 → 统一目标与训练 / 推理（3.7）。第 3.8–3.10 节是特定类型才有的部分，第 3.11–3.12 节是贯穿全章的要求。

### 3.1 章首 Overview 段与总览图

**写什么**：1 句复述引言的目标（输入 → 输出）；1 句引用总览图；1–3 句路线图，用 "(Sec. 3.x)" 预告小节顺序。后面各小节与图中各部分一一对应。

**原句**：
- "Our objective is to generate high-resolution 3D assets with arbitrary shape topology... An overview of our approach is presented in Fig. 2."（《Native and Compact Structured Latents》，目标句 + 引图）
- "As illustrated in Fig. 2, our proposed FPRL is a cognition-inspired hierarchical framework that emulates the clinical examination process..."（《FPRL》，引图时顺带给出设计隐喻）
- "Our HUG3D framework operates in three main stages, as illustrated in Fig. 2."（《Human Interaction-Aware 3D Reconstruction》）
- "As Figure 2 shows, the framework comprises three key components"（《OctMem-Agent》）
- "Figure 2 illustrates the pipeline of our method. We first extract...(Sec. 3.2)...losses (Sec. 3.6)."（《SuP》）
- "Sec. 3.2 introduces our novel adaptive 3D filter...; Sec. 3.3 contains our perspective correct bounding approach...; Finally, Sec. 3.4 proposes..."（《AAA-Gaussians》）
- "We begin by formulating the problem in Sec. 3.1. Next, Sec. 3.2 describes...followed by...in Sec. 3.3. Finally, in Sec. 3.4, we elaborate on training..."（《StreamFormer》）
- "In the following, we first revisit X...and discuss its limitations (Sec. 3.1)."（《E-RayZer》，路线图里直接点出"先指出局限"）
- "We first review...(Sec. 3.2)...We then describe our core contributions...(Sec. 3.3)...Finally, we present...(Sec. 3.5)."（《MV-RoMa》）
- "We next detail our approach along three aspects: (1)...; (2)...; and (3)..."（《SLARM》）
- "We begin with the preliminaries (3.1), followed by...(3.2) and...(3.3)."（《AVA-VLA》）

**模板**：
```
Given [input], our goal is to [output / objective restated from Intro]. An overview of X is shown in Fig. 2.
We first [revisit / formulate ...] (Sec. 3.1). Next, we [component 1, solving problem 1] (Sec. 3.2).
Since [component 1 leaves problem 2], we further [component 2] (Sec. 3.3). Finally, we describe [training / inference] (Sec. 3.4).
```
路线图里就写出"为什么需要下一步"（如《E-RayZer》的 "discuss its limitations"），比单纯列章节号更好。

### 3.2 Preliminaries / Problem Formulation

**写什么**：任务的输入输出、记号、要回顾的基础方法（只回顾后文要改动或复用的部分）。后文所有符号从这里取。

**原句与做法**：
- "Given a streaming RGB-D sequence..., our goal is to incrementally construct: (i)...(ii)..."（《OVI-MAP》）
- "We start with the problem statement for open-set face recognition (FR)...followed by the motivation for LVFace..."（《LVFace》）
- "Formally, the objective of normal integration is to recover a surface..."（《Discontinuity-aware Normal Integration》）
- 用 Definition 1/2 定义任务（《Authorize-on-Demand》）；用集合论定义任务 C=(F,G)（《NERFIFY》）；先给 y=F_R∘F_D(x) 作为式 1（《CHROME》）。
- Preliminary 只讲后文要用的基座：《Scal3R》讲 VGGT 与 TTT；《MEDIC-AD》3.1 先给通用 VLM 公式 Eq.1，后面逐步在它上面打补丁。

**要求**：
- 符号首次出现即定义，并与 spec 的术语与符号表一致；同一个符号不能表示两个东西（`word_style.md` 原则 3）。
- 新术语一旦定义，后文严格复用，它起的是"贯穿全文的黏合剂作用"（《Vocabulary Scaling Law》《When Do Models Actually Decide》）。
- Preliminaries 这一小节允许"先公式后解释"（《MVQA》Preliminaries 先公式后解释，正文 3.3/3.4 则先直觉后公式；《SAQN》Problem Statement 先给 Eq.1 再补文字），但设计小节不要这样写。

**模板**：
```
Given [input symbols with shapes], our goal is to [predict / construct] [output symbols], such that [constraint].
Formally, [task definition / Eq. (1)], where [symbol] denotes [...].
We build on [base method], which [one-sentence mechanism] (Eq. (2)). Its limitation relevant to us is that [...].
```

### 3.3 小节开头：承接句

**写什么**：第一句交代本小节要解决的问题从哪里来。三种来源：上一节的输出、上一节暴露的不足、前面分析节的结论。

**(a) 复用上一节的输出**
- "given the geometry-enhanced keypoint features F_geo"（《ComPose》，段首复用上一节的变量名）
- "Using the aligned feature maps from the previous step"（《Selfi》3.2）
- "We now employ our 3D tracker above to recover the camera poses..."（《BA-Track》3.2）
- "Having established a powerful latent representation for 3D textures, we now detail the generative process..."（《Lafite》）
- "With X established, we turn to..."（《Mocap-2-to-3》）
- "Building on the continuous concept fusion strategy in Sec. 3.2, DisTok progressively learns..."（《Breaking Semantic Boundaries》）
- "We implement the function Φ in Eq. (1) using..."（《CoRoGS》，显式回指公式）

**(b) 承认上一步的不足**
- "Section 3.1 provides coarse metric depth ... but leaves residual pixel-level errors."（《Midas Touch》）
- "While the Global Head ... overlooks ... To address this, we propose ..."（《HyperGait》）
- "However, such formulation also introduces a limitation...To address this, we introduce..."（《MoRe》）
- "While energy-based composition enables knowledge transfer...generated bimanual actions may violate coordination constraints"（《EnergyAction》）
- "Although MoAME captures inter-modal correlations, it still introduces redundancy..."（《MDCS-MoAME》）
- "Although Ms is now fused into F′s, it has not yet interacted sufficiently...Therefore, we introduce..."（《VGGT-Segmentor》）
- "While X enables Y, naively applying it to Z leads to inefficient planning"（《Visual-RRT》）

**(c) 回指分析结论**
- "Based on the layer-wise analysis in Sec. 3, the early global attention layers do not contribute…"（《AVGGT》）
- "As discussed in Sec. 3.3, it is essential to design a fixed masking scheme..."（《LF-BVN》）
- "Based on the observations in Sec. 4, we introduce STAC..."（《STAC》）
- 每个子问题末尾写 "Motivation: ...(Sec. 4.1)"，直接点名对应章节（《MetaScope》）。

**(d) 挑战清单，统一预告后续小节**
- "Challenges. (1)...(2)... To address these challenges, we introduce..."（《GardenDesigner》《GenHOI》）
- "This architectural choice is powerful, but it introduces three core technical challenges. First...Second...Finally..."（《GeoRelight》，每个挑战对应后面一个小节）

**模板**：
```
While [previous component] [achieves A], it [still lacks / introduces B]. To address this, we introduce [component].
Given [output variable of previous section], we [next operation].
Based on [finding / observation] in Sec. [N], we [design choice].
[Design] is effective, but it introduces [k] challenges. First, ... Second, ... We address them in Sec. 3.x–3.y.
```
**注意**：回指尽量用自然语言说出"上一节留下了什么"，只写 "As mentioned in Sec. X" 会显得生硬（见第 4 节问题 5）。

### 3.4 设计动机：为什么这样做、为什么不用更简单的做法

每个设计选择都要给出理由，理由最好能在消融实验里找到支撑。材料中反复出现的七种写法：

**(1) 朴素方案 → 具体失败原因 → 我们的方案**（最常用）
- "A naive choice would sort tokens directly by their distances to c...but neglects local spatial continuity"（《Mamba Learns in Context》）
- "a simple approach would be to fuse every expert's score map... However, evaluating all experts on every image would be both costly..."（《PromptMoE》）
- "swapping the entire amplitude can cause severe artifacts..."（《MFEN》，反证式引出公式）
- "Directly applying the same face deformation strategy fails to fully leverage the unique characteristics of eyeball rotational motion"（《GazeGaussian》）
- "Directly prompting MLLMs to generate icons is unreliable, often causing semantic hallucinations…"（《Widget2Code》）
- 《AAA-Gaussians》3.2 先描述 naïve approach 为何导致 Gaussian 过度透明；《Att-Adapter》3.2.1 给朴素 MLP 版本并报告过拟合，3.2.2 再引入 CVAE。
- 《StableDepth》3.2：先给直觉方案 → 实验发现会降低精度 → 再给改进方案（实验倒逼修正）。

**(2) 先报告观察，再给假设**
- "We observe that significant color changes typically arise from two sources"（《LumiMotion》）
- "We empirically found that the original CFG may yield unexpected results...We hypothesize the underlying reason is that..."（《DeX-Portrait》）
- "we observe that the model learns only generic preferences...caused by overfitting of the preference adapter"（《Premier》）
- "we empirically find that simply treating...is insufficient"（《OpenDance》4.2）
- 《Adaptive Depth Lightweight RGB-T Tracking》先用 Figure 展示 score map 饱和现象，再逐层删除反证，排除简单方案。

**(3) 批评现有方法的具体缺陷**
- "Existing methods…however, under X condition…To address/overcome this, we propose…"（《Wavelet-Driven》《WorldMM》《SafeDrive》反复出现）
- "Existing methods are fundamentally limited by (i)... and (ii)..."（《OpenDance》4.1）
- "existing methods leverage the Gram matrices...but we find that this leads to collapsed inter-class knowledge"（《VRM》）
- "Unlike previous detector-free methods [57, 63]..."（《EDM》）；"Unlike existing methods conditioned on text, images, or masks, our adapters uniquely condition..."（《IQA-Adapter》）
- "Rather than fine-tuning the CLIP text encoder, which may cause semantic drift, we keep it frozen..."（《FluoCLIP》，把被放弃的方案和放弃原因写在同一句）
- 《SegEarth-R2》4.2 逐条批评 InstructSeg 与 SegEarth-R1，再引出自己的方案（先破后立）。

**(4) 理想目标不可行 → 退而求其次**
- "Directly using SEA-filtered outputs in the cache metric is not practical...We therefore seek an input-side proxy"（《SeaCache》）
- 《Kaleidoscopic Background Attack》理想损失不可反传 → 定义坐标流场 → 给出可行替代。

**(5) 独立的 "Motivation." / "Solution." 小标题**
- 《MetaScope》《Noise-Modeled Diffusion》《RhythmGuassian》都用固定小标题；《VolumetricSMPL》"The Challenge: Balancing Efficiency and Expressiveness" → 方案 → "Advantages of NBW"。

**(6) 设问句**
- "Why is this an issue?"（《RDPO》）；"Why Use Trained Networks?"（《Variance-Based Pruning》）

**(7) 类比、生活化例子、具体数字**
- "Consider a human playing tennis..." → "We formalize this intuition by learning cross-modal latent dynamics..."（《CLaD》）
- 用 "evidence-based medicine" 作类比（《MedLIME》）
- "a car has four wheels below the body frame, which can be recovered even from a partial view"（《DiffRefine》）
- "if a voxel contains 95 LiDAR points and only 5 Gaussians..."（《Mapping Priors》，用具体数字说明朴素平均融合的问题）
- 用戴眼镜、放杯子的失败场景说明纯 2D 记忆不可行（《Embodied VideoAgent》）

**模板**：
```
A naive solution is to [simple approach]. However, [concrete failure: phenomenon / number / figure].
We observe that [phenomenon] (Fig. N). We hypothesize that this is because [mechanism].
Rather than [alternative], which [drawback], we [our choice].
Ideally, we would [ideal objective]; however, [why intractable]. We therefore [tractable surrogate].
```
**要求**：失败原因要写到机制层（"neglects local spatial continuity"），不写"效果不好"；这里说出的失败，实验里要有对应的消融或对比（贡献 i ↔ 方法 3.i ↔ 表 i）。

### 3.5 公式段：先直觉，后公式

**标准三段式**：一两句自然语言动机 → 编号公式 → where 从句解释符号，或公式后一句话复述它的含义。每个编号公式的前一句都要说明"为什么需要它"。

**公式前的直觉句（原句）**：
- "Intuitively, reconstruction should guide the generation process, but generation should not interfere with reconstruction."（《RnG》，后接掩码矩阵公式）
- "Intuitively, sensitivity captures how 'stiff' or 'smooth' the network function is around a given input"（《SenCache》，再给 Jacobian 定义）
- "Intuitively, when the input undergoes a certain transformation, the model's output transforms in a corresponding manner."（《E3Flow》，再给等变性定义）
- "Intuitively, flat minima are those where neighboring points also exhibit low loss values"（《Beyond Losses Reweighting》）
- "Our approach relies on the insight that contrast of a patch as a function of depth is often smooth and, more importantly, unimodal"（《Spatially-Varying Autofocus》，再引出二分搜索）
- "Our key insight is to avoid correspondence altogether"（《CoSMo3D》，后接 Eq.3）
- "Our key insight is that visual loss Lrender serves as an implicit goal proximity measure."（《Visual-RRT》）
- "Our core idea is to predict an imagined future observation..."（《ForeAct》3.2）
- "Our core insight is to design an autoregressive style generator...To realize this generator, we first train a discrete style codebook"（《A Style is Worth One Code》）
- "The act of taking a photograph maps a 3D object to a set of 2D pixels...We seek to invert this map"（《SAM 3D》）
- "Such a shift acts like a subtle camera motion"（《RAVEN》4.2.2，用比喻引出 warping 公式）
- "To address this lack of granularity, we aim to introduce perturbations that are strong enough...yet fine-grained enough..."（《Guiding a Diffusion Model by Swapping Its Tokens》）
- "once q is fully contained in the cone, the loss becomes zero, preventing further fine-grained alignment"（《UNCHA》，先指出旧公式的缺陷再给改进公式）
- "We will now formalize our method."（《MEMFOF》，显式标记从直觉切换到公式）

**公式后的解释句（原句）**：
- "Intuitively, nodes that are closer to ct in the local subgraph receive higher activation..."（《GrOCE》）
- "where e^{-k(ω_x²+ω_y²)t} functions as an adaptive filter..."（《RS-vHeat》，补物理解释）
- "this design keeps each set of primitives centered and active between two input frames"（《RetimeGS》）

**模板**：
```
Intuitively, [what the component should do, in plain words]. We formalize this as
    [Eq. (k)]
where [symbol_1] denotes [...], and [symbol_2] is [...]. In effect, Eq. (k) [physical meaning / what it encourages / when it becomes zero].
```

**例外（可以先公式后直觉）**：
- 理论型、统一框架的形式化部分：先 Definition / Theorem，再用 "Intuition." / Remark / "Physical interpretation." / "Intuitive Understanding." 段补直觉（《AdaPrior》每个 Theorem 后紧跟 "Intuition."；《2D-LFM》先给投影公式与 Proposition；《FloodDiffusion》；《HiNeuS》；《Test-time Adaptation for Foundation Medical Segmentation》3.3）。
- Preliminaries / Problem Formulation（见 3.2）。
- 即使在这些例外里，也要紧跟一句直觉，如《Scaling-Aware Data Selection》Eq.4 后紧跟 "Intuitively, ai represents…"。

**不要模仿**：《GRPO-Guard》公式密度极高、直觉只是穿插；《Plug-and-Play IMVC》"简短动机 → 立刻给优化目标公式"；《NERFIFY》《AdaPrior》这类写法门槛更高。除非是理论型，否则默认先直觉。

**无公式的类型**：数据与基准型、纯经验 scaling 研究可以几乎不用公式（《Scaling Language-Free Visual Representation Learning》靠 "suggests/indicates" 定性推理推进），但仍要"先直觉后细节"：先说这一步为什么需要，再给具体规则、阈值或流程。

### 3.6 小节收尾：说清得到了什么、留下了什么

小节末尾交代本节的输出（下一节会用到的变量），以及它还没解决的问题。这句话就是下一节的开头。
- "Note here that solving (10) still requires the global forward operator and its adjoint"（《Efficient Unrolled Networks》4.1 末，直接抛出下一节的问题）
- "Up to this point, the model captures geometric and temporal patterns, but remains agnostic to motion dynamics. In the next section, we introduce a mechanism..."（《PAD-Hand》）
- "BA processes only a sparse set of query points...we need global refinement"（《BA-Track》3.3）

**模板**：
```
Up to this point, [what we have: output variable / capability], but [what is still missing]. In the next section, we [next step].
Note that [remaining requirement / cost], which we address in Sec. 3.x.
```

### 3.7 统一目标函数、训练与推理

**写什么**：把各小节的损失合成一个总目标（写出权重），交代训练阶段和推理流程。这是链的收束点。
- 《Scaling Dense Event-Stream Pretraining》诊断 Event-domain Semantic Collapse → Activation Mask Constraint → Structure-aware Alignment Loss → 统一损失式 (5)。
- 《TF-CADE》4.2/4.3 分别解决训练 / 推理两阶段缺陷，4.4 串成 pipeline。
- 《CountSE》Overview → SES → CEF → Loss，层层递进后以 Loss 收尾。
- 《MeteorPred》《OmniFood8K》按编码器并列后以 Fusion / Loss 收尾（模块清单式，不构成链）。

**要求**：损失项名称、权重、训练阶段划分与代码一致；超参数取值写正文或指明附录位置。

**模板**：
```
The overall training objective is
    L = L_[a] + λ_1 L_[b] + λ_2 L_[c],
where λ_1 and λ_2 balance [...]. We train X in [k] stages: [...]. At inference, [...].
```

### 3.8 发现-解释型：分析节写法

- 分析节放在方法之前（或作为方法第一节），标题写成观察或问题，而不是模块名（《FILTR》"Do 3D encoders understand topology?"；《Selection-as-Nonlinearity》《The Devil Is in Gradient Entanglement》《TimeRipple》）。
- 结构用 Observation → Hypothesis → Diagnosis（《Improving Motion in Image-to-Video Models》），或 Pilot Study → Finding 1–k（《What to Distill?》《VRM》）。
- 分析结论要给名字（取名见 `references/naming.md`），方法里每个设计点显式回指："From Sec. 3 we conclude that...Theorems 3.4 and 3.5 provide us with a tool to do so"（《Is the Modality Gap...》）。
- 设计点与发现一一对应；如果某个设计没有对应的发现，要单独写出它的动机。

### 3.9 数据与基准型：流水线写法

- 按"数据收集 → 筛选 → 标注 → 质控 / 生成"或"任务 → 指标"的平行结构组织（《EgoSound》《EgoXtreme》《Hoi!》《SA-FARI》）。
- 每一步写：做什么、为什么需要、排除了什么问题、规模或数量。
- 基线部分：先统一问题形式化，再并列给出几个基线（《M3DLayout》《MV-Fashion》）；基线之间可以按难度递增排列，每引入下一个前先指出前一个的具体局限，核心方法作为最后一环（《RefAV》五个 baseline）。
- 可以用伪代码、流程图、编号步骤代替公式（《RealAppliance》《InfiniBench》），但不能只罗列组件而不说理由（《UnrealZoo》被笔记描述为"系统组件说明书"式）。

### 3.10 应用 / 下游适配小节

统一框架型常在核心方法后加应用小节（《NaTex》3.3 Applications）。这类小节的论证密度往往明显低于核心方法，容易显得"为完整性而写"。要求：
- 每个应用说明需要改动什么、为什么核心方法能直接支持它；
- 每个应用在实验里有对应结果，否则删掉或移到附录；
- 多个应用 / 案例共享同一骨架（《Visual Diffusion Models are Geometric Solvers》的 "Problem Statement → Existing Methods → Method → Evaluation"）。

### 3.11 与实现一致、可复现

- 先读代码再写。模块名、损失函数、超参数、训练流程逐项核对；代码与草稿不一致时问用户以哪边为准。
- 模块名在摘要、引言、方法小节标题、总览图标注、消融表里完全一致（取名规则见 `references/naming.md`）。
- 正文保留核心公式和关键超参。反例：《NitroGen》《AVGGT》几乎不用编号公式，细节全推给补充材料，牺牲了正文的可复现性。
- 数据与基准型：写清规模、来源、标注协议、质控标准。

### 3.12 与实验、局限的接口

（合并自 story_types 原 §3.5–3.6。实验和局限的完整写法见 `sections/experiments.md` 和 `sections/conclusion.md`，这里只写方法章节要为它们准备什么。）

- **不引用实验**：方法正文不写 "ablated in Sec. 4.3"、"as shown in Table 5"，也不写实验结果数字；下面的对应关系只用于规划（章节之间的引用规则见 `references/workflow.md` 第 3 节）。
- **贡献 i ↔ 方法 3.i ↔ 表 i**：每条贡献对应一个方法小节，每个方法小节对应一个实验小节或一张表。消融变体用 "w/o 模块名" 命名，消融顺序与引言列举挑战的顺序一致。《Mamba Learns in Context》3.2–3.4 三个组件与贡献列表严格对应。
- **设计理由要能被验证**：3.4 节写下的"朴素方案为什么失败"，实验里要有"朴素方案 vs 我们的方案"的对照；洞察本身要有机制实验支撑（t-SNE、注意力图、频谱、oracle、干预实验）。64.8% 的论文把 Insight 列为贡献 [stats]。
- **方法里说出的额外能力都要有实验**：写进方法的应用、泛化声明、效率声明，事先要写进贡献列表，实验里有独立验证。
- **把假设写明**：方法依赖的前提（传感器、数据条件、先验、计算预算）在方法里写出来，局限一节才能从中挑出最相关的 1–2 条，写成"**适用边界 + 方向**"，而不是泛泛而谈。正面例子：《HairCUP》局限各自配了 because；《Gallant》把边界落在 LiDAR 10Hz 的感知延迟上；EgoXtreme 写明"依赖 OptiTrack，只能在室内专用场地采集"。顶会论文多数不设独立的 Limitations 小节；本 skill 的做法是局限最多 2 条、简短（`references/anti_defensive.md` §5）。
- **结论回收方法**：结论首句回收引言里定义方法的那句话，补上摘要之外的信息（机制、覆盖范围或意义），不复述摘要；最后一句落在意义上。

---

## 4. 常见问题与反例

| # | 问题 | 表现 | 反例 / 出处 | 怎么改 |
|---|---|---|---|---|
| 1 | 模块清单代替求解链 | 模块之间没有因果连接，读者只能靠贡献列表的出场顺序推断组织逻辑 | 《DreamLayer》CACA / LSSA / IRH 三模块；《LayerTracer》六个小节与引言"三条洞察"的对应不完全显式 | 每个小节开头加承接句（3.3），说明它解决哪个问题、用到上一节的什么输出；确实独立的模块按 2.2 写，模块内部补动机 |
| 2 | 公式先行、没有直觉 | 一上来就是 Eq.(1)，读者不知道它要解决什么 | 《AdaPrior》《NERFIFY》门槛更高；《GRPO-Guard》公式密度极高；《Plug-and-Play IMVC》动机后立刻给优化目标 | 非理论型一律改成三段式（3.5）；理论型每个定理后加 "Intuition." 段 |
| 3 | 先列困难再给方案，但没有直觉 | 列了三点技术困难就直接给表示方式，没有说为什么这个方案能解决 | 《NeuFrameQ》先列三点技术困难再引出点云表示 | 困难清单后加一句核心洞察："Our key insight is that ..."，再给方案 |
| 4 | 正文不可复现 | 几乎没有编号公式，细节全推给补充材料 | 《NitroGen》《AVGGT》 | 核心设计的公式和关键超参写回正文 |
| 5 | 跨节回指生硬 | 只写 "Sec. X"，不说那里得到了什么 | 三份材料共同指出的问题 | 写成 "Based on the layer-wise analysis in Sec. 3, the early global attention layers do not contribute…"（《AVGGT》）这样带内容的回指 |
| 6 | 应用小节论证稀薄 | 统一框架型的应用 / 下游适配小节密度明显低于核心方法，像"为完整性而写" | 统一框架型常见（材料指出） | 按 3.10 补"改什么、为什么能直接支持"，并在实验里给结果；否则移到附录 |
| 7 | 设计没有理由 | "We design a module X" 直接开场，没有说为什么不用更简单的做法 | 与 3.4 的正例相对 | 补一个朴素方案及其具体失败原因，最好指向消融 |
| 8 | 失败原因不到机制层 | "效果不好""不够鲁棒" | 与《Mamba Learns in Context》"neglects local spatial continuity" 相对 | 写出失败的机制；能给数字就给（《Mapping Priors》"95 LiDAR points and only 5 Gaussians"） |
| 9 | 符号 / 术语漂移 | 同一现象在引言、方法、实验里叫法不同；一个符号表示两个量 | 见 `word_style.md` 原则 3、8 | 设 Preliminaries，符号登记进 spec 的术语表，全文复用 |
| 10 | 与代码不一致 | 模块名、损失权重、训练阶段与实现对不上 | 原 method.md 要求 | 先读代码；不一致时问用户以哪边为准 |
| 11 | 数据 / 基准型只罗列组件 | 像系统说明书，没有每一步的理由 | 《UnrealZoo》"系统组件说明书"式 | 按 3.9 每步写"为什么需要、排除了什么" |
| 12 | 方法说了、实验没验证 | 方法里的应用、泛化、效率声明没有对应实验 | 见 `sections/experiments.md` 特殊贡献一行 | 方法小节与实验小节一一对应（3.12） |

---

## 5. 写作步骤与检查清单

### 5.1 写作步骤

1. **读实现**：读代码或用户的实现说明，列出模块、数据流、损失项及权重、训练阶段、推理流程、关键超参数。发现与草稿描述不一致的地方，先问用户。
2. **对齐上游**：从引言草稿取出目标句、根因 / 挑战列表、贡献列表、现象名和方法名；从 spec 取术语与符号表。
3. **定类型与结构**：按 2.7 选组织方式。写出小节标题列表，每个标题旁边注明"它解决的问题"和"它的输入来自哪一节"。有一个小节注不出来，就说明它是清单式模块，要么补出因果，要么按 2.2 处理。
4. **画总览图并写 Overview**（3.1）：图中每个部分对应一个小节。
5. **写 Preliminaries**（3.2）：登记所有符号。
6. **逐小节写**：承接句（3.3）→ 设计动机（3.4）→ 先直觉后公式（3.5）→ 收尾并引出下一问题（3.6）。
7. **写统一目标与训练 / 推理**（3.7）。
8. **类型专属部分**：分析节（3.8）、流水线（3.9）、应用小节（3.10）按需添加。
9. **对接实验与局限**（3.12）：给每个方法小节配上对应的实验 / 消融；把方法依赖的假设整理出来，供局限一节挑选最相关的 1–2 条。
10. **按 5.2 清单自查**。

### 5.2 检查清单

**结构**
- [ ] 章首有 Overview 段：复述引言目标句、引用总览图、用 "(Sec. 3.x)" 预告小节顺序
- [ ] 总览图的各部分与小节一一对应
- [ ] 每个小节的开头交代它要解决的问题从哪里来（上一节的输出 / 不足，或分析节的结论）
- [ ] 小节之间是求解链；确实并列的模块按数据流排序，且模块内部有动机
- [ ] 末尾有统一目标函数或训练 / 推理流程把各部分串起来
- [ ] 组织方式与故事类型匹配（2.7）

**动机与公式**
- [ ] 每个设计都说明了为什么不用更简单的做法，失败原因写到机制层
- [ ] 每个编号公式的前一句在说"为什么需要它"，后面有 where 从句或一句话解释含义
- [ ] 只有理论型 / 形式化部分先公式后直觉，且定理后紧跟 "Intuition." 或 Remark
- [ ] 数据与基准型的每一步都写了理由

**一致性**
- [ ] 所有符号首次出现即定义，与 spec 的术语与符号表一致，没有一个符号表示两个东西
- [ ] 方法名、模块名、现象名与摘要、引言、图、消融表完全一致（`references/naming.md`、`word_style.md` 原则 3、8）
- [ ] 模块名、损失函数、超参数、训练流程与代码一致；不一致处已问过用户
- [ ] 跨节回指说出了被回指的内容，而不只是 "Sec. X"

**对接**
- [ ] 贡献 i ↔ 方法 3.i ↔ 表 i；每个设计理由在实验里有对应的对照或消融
- [ ] 方法正文没有引用实验章节、实验图表或实验数字
- [ ] 方法里提到的应用、泛化、效率声明在实验里都有验证
- [ ] 方法依赖的假设已写明，局限一节能从中挑出 1–2 条写成"适用边界 + 方向"
- [ ] 核心公式和关键超参在正文，附录只作补充
