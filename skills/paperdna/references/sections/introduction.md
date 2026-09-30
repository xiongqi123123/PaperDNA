# 顶会论文引言写法规范

> 用途：论文写作 skill 的参考规范。读者是正在替用户写引言的 AI 助手，请按本文的结构、模板、步骤和检查清单去写。
> 证据来源：(1) 1040 篇 CVPR 2026 + ICCV 2025 精读笔记的精确统计（`references/corpus_stats.md`）；(2) 13 份分批归纳（CVPR2026 highlight / oral、ICCV2025 样本）。文中 "（X）" 表示原句或做法出自论文 X。凡是写"推荐"的地方，是从材料归纳出来的做法，不是统计结论。
> 英文模板中 X/Y/Z/A/B 为占位符，写作时替换成具体名词；带引号的整句是原文。
> 跨章节的写作原则和去 AI 味规则见 `references/word_style.md` 第 1 节和第 4 节，本文的模板也要遵守。

---

## 0. 一页速查

| 项目 | 规范值 | 依据 |
|---|---|---|
| 引言段数 | 写 5–6 段；允许 4–7 段 | 中位数 6，四分位 [5, 6, 6]；4–7 段合计 88.7% |
| 主序列 | 背景 → 局限 → 根因 → 洞察 → 方法（命名） → 结果预告 → 贡献列表 | 13 份材料共同骨架；没有一篇严格照搬三段 CARS |
| Figure 1 | 必须有，并且在引言正文中至少引用一次 | 91.3% 的论文第一页或引言有 teaser 图 |
| 贡献列表 | 默认用 bullet，3–4 条；放在末段 | bullet 74.4%，inline 25.0%，没有贡献列表的 0.6% |
| 贡献内容 | 至少包含"性能"，多数同时包含"能力"与"洞察" | 含 Performance 91.8%，含 Capability 79.1%，含 Insight 64.8% |
| 方法首次登场 | "To address …, we propose X, a Y that Z." | 13 份材料都把它列为最通用的命名句 |
| 最高频衔接 | However / Despite / While（转折），To this end / To address（目的），this gap / these limitations（回指） | 13 份材料都有记录 |

---

## 1. 引言的标准结构

### 1.1 段数（1040 篇统计）

| 段数 | 篇数 | 占比 |
|---|---|---|
| 1 | 1 | 0.1% |
| 3 | 29 | 2.8% |
| 4 | 176 | 16.9% |
| **5** | **303** | **29.1%** |
| **6** | **282** | **27.1%** |
| 7 | 162 | 15.6% |
| 8 | 53 | 5.1% |
| 9–13 | 34 | 3.3% |

执行规则：
- 默认写 **5 或 6 段**（合计 56.2%）。
- 只有 1 个核心想法、而且缺口可以一句话说清时，才压缩到 **3–4 段**（19.7%），例如 ChordEdit、CFT、HippoVLM、TriLite。
- **7–8 段**（20.7%）适合多组件或资源型论文：每个产出（模型/数据集/RL 框架/基准）各占一段，例如 OralGPT-Plus、PromptMoE、Molmo2、Textbook。
- 超过 8 段（3.3%）属于罕见情况，除非有多轮"方案→新缺口"循环（SMVS-TAG、ViT3、POLAR），否则不要写这么长。

### 1.2 功能段库（9 类）

| 代号 | 功能段 | 必需性 | 常与谁合并 |
|---|---|---|---|
| BG | 领域背景 / 任务定义 / 重要性 | 必需 | 紧凑式里与 GAP 合并 |
| GAP | 现有方法综述与局限 | 必需 | 常与 ROOT 合并（ChordEdit） |
| ROOT | 根因 / 挑战分析 | 强烈推荐 | 与 GAP 或 INS 合并 |
| INS | 核心洞察（观察、假设、类比、设问） | 强烈推荐 | 常与 MTH 合并；也常独立成段或加框 |
| MTH | 方法提出与命名 | 必需 | — |
| DET | 设计细节 / 组件展开 | 可选 | 常并入 MTH |
| RES | 结果预告 | 推荐 | 常并入 MTH 段尾或贡献末条 |
| CON | 贡献列表 | 必需（99.4%） | 放在末段 |
| REL | 资源发布 / 开源声明 / 意义收尾 | 可选 | 常作为贡献列表末条 |

### 1.3 段落功能序列（10 种排列，按优先级）

所有排列都是"背景 → 缺口 → 方案"的扩展。选择时先看故事类型（1.4），再看下面每种的适用场景。

| # | 名称 | 序列 | 适用场景 | 例证 |
|---|---|---|---|---|
| S1 | 标准线性式（默认） | BG → GAP → ROOT → INS → MTH(+DET) → RES → CON | 单一瓶颈、单一方法 | CDA-VSR、CAGS、FedHarmony、FastGS、DetGain、PHASE-Net |
| S2 | 紧凑三/四段式 | BG → GAP+ROOT → INS+MTH+RES(+inline CON) | 想法单一、篇幅紧 | ChordEdit、CFT、HippoVLM、GaussianVision、TriLite |
| S3 | 编号缺口镜像式 | BG → GAP 列出 (1)(2)(3) → MTH 按 (1)(2)(3) 逐条回应 → CON 按同样顺序 | 方法有 2–4 个模块，每个模块对应一条缺口 | HiLoRA 三缺陷↔三模块、FoleyDesigner"三线对齐"、CROWn、CHIRP、MorphSeek、VPDR ①② |
| S4 | 双线对称批评→汇合式 | BG → 路线 A 局限 → 路线 B 局限 → 归纳共同缺口 → MTH 合并两者 | 统一框架；方法结合两条技术路线 | CUPID（On one hand / On the other hand）、Sparfels（"marry the best of both worlds"）、Ov3R（"In both directions, however..."）、StableDepth、RetimeGS |
| S5 | 发现驱动 / 实证前置式 | BG → 预实验或可视化坐实问题 → ROOT → INS → MTH（命名推迟） | 发现-解释型；缺口不是文献里的共识 | ALG、TF-CADE（两段诊断实验）、Thinking in Uncertainty（Fig.1–3 实证链）、RALoc（"recall drops below 1%"）、ETCTrack、GW（18 个编码器实测） |
| S6 | 设问 / 研究问题驱动式 | BG → GAP → 设问（或 RQ1–3）→ "The answer is yes." / 逐条作答 → MTH | 挑战默认假设；分析类论文 | GECKO、MEDIC-AD（RQ1–3）、Web-SSL、SpatialTree（独立缩进问句）、SuP |
| S7 | 多轮排除 / 螺旋收窄式 | BG → 方案 1 的局限 → 方案 2 带来新障碍 → … → 本文 | 竞品多的领域；需要说明"为什么别的路不行" | HoloCine（decoupled 不行→holistic 有两个新瓶颈）、GameFactory（证伪直觉方案）、DisenQ（连续 3 次排除）、PGO-ACE、《No Calibration, No Depth, No Problem》 |
| S8 | 先立标准 / 任务合法性先行式 | BG → 提出理想方案须满足的 N 条标准或新任务定义 → 用标准逐一批评 → MTH | 新问题定义型 | LIDMark（"an ideal framework must…address three fundamental forensic questions"）、Phantom、GROC、SSMDG、HR-NVC |
| S9 | 资源型加长式 | BG → 瓶颈 → 数据缺口 → 数据 pipeline（多段）→ 模型/基准 → CON + 开源承诺 | 数据与基准型 | Molmo2、Textbook、SA-FARI、OLATverse、Derm1M、TMR |
| S10 | 加粗小标题 / 报告体 | 用 **Our approach.**、**Data:/Training:/Benchmark:** 等小标题代替过渡句 | 多产出论文；benchmark；报告型 | Cleaning the Pool、ReMoT、LATA、《水下SLAM》、When Understanding Becomes a Risk（RQ+Findings，无 bullet） |

可加的附加段：**防御性论证段**，提出方案后用一段专门回应"这不就是 X 吗"的质疑（Enrich and Detect）。

### 1.4 与故事类型的对应关系

故事类型分布（1040 篇）：瓶颈突破型 56.0%、新问题定义型 11.0%、统一框架型 10.8%、发现-解释型 10.7%、数据与基准型 7.0%、能力扩展型 2.4%、效率优化型 2.0%、理论分析型 0.2%。oral（57.9% 瓶颈突破）与 highlight（55.5%）的分布基本一致；autonomous_driving 方向新问题定义型更高（18.8%），embodied 方向统一框架型更高（17.1%）。

下表"推荐序列"一列是从材料归纳的对应关系，stats 里没有故事类型与引言序列的交叉统计。

| 故事类型 | 占比 | 推荐序列 | 引言重心 | 命名倾向（见 references/naming.md） | 例证 |
|---|---|---|---|---|---|
| 瓶颈突破型 | 56.0% | S1；多模块时用 S3；竞品多时用 S7 | ROOT 要具体到机制；INS 能直接推出方法 | 起专名（缩写 / backronym / 修饰词+基座） | DetGain、HiLoRA、ChordEdit、FluoCLIP |
| 新问题定义型 | 11.0% | S8 | 先证明新任务有独立价值，再说现有方法为什么答不了 | 给任务或问题正式命名，例如 "we call this the X (ABBR) problem" | Phantom、GROC、SSMDG、PfS、LIDMark |
| 统一框架型 | 10.8% | S4 | 两条路线各自的局限要对称写；汇合句要写明"同一个方案解决两边" | Omni- / Uni- 前缀 | CUPID、Sparfels、Ov3R、OmniDocLayout、UniPhys |
| 发现-解释型 | 10.7% | S5 或 S6 | 用自建实验代替文献转述作缺口证据；命名推迟 | 常不起方法名，只给"发现"命名；贡献引导句可用 "Our main findings are:" | ALG、TF-CADE、OVDG-SS、Consensus vs. Controversy、Mechanisms of Object Localization |
| 数据与基准型 | 7.0% | S9 | 数据缺口要具体到规模、标注、场景；结果预告写"现有方法离解决还很远" | 几乎必起名：领域+Bench、规模数字后缀 | EgoSound、ENC-Bench、GEOBench-VLM、Benchmarking Egocentric VI-SLAM |
| 能力扩展型 | 2.4% | S1 骨架，结果预告突出新能力（材料中没有专门样本） | 用"首次支持"或泛化规模作证据 | 同瓶颈突破型 | CrossHA（"trained on only 30 tasks…generalizes to over 800 tasks"）、URICA（"To our knowledge, this is the first approach to support Y."） |
| 效率优化型 | 2.0% | S1；GAP 写成 trade-off | 结果预告以倍数为主，并声明质量不降 | 同瓶颈突破型 | InstantViR（"this trade-off is not fundamental"）、SEATrack、LLSA（6.09×）、VolumetricSMPL（10×） |
| 理论分析型 | 0.2% | S6 或 S2 | 动词克制；贡献是推导或理解本身 | 常不命名 | C²FG（"we aim to provide a theoretical understanding…"）、P3P、Homaloidal parametrization |

### 1.5 贡献类型组合（决定贡献列表写什么）

| 组合 | 占比 |
|---|---|
| Capability+Performance | 24.9% |
| Insight+Performance+Capability | 21.2% |
| Insight+Performance | 19.6% |
| Insight+Capability+Performance | 14.1% |
| Performance+Capability | 10.1% |
| Insight+Capability | 4.8% |
| 其他 | 5.3% |

执行规则：贡献列表至少有一条性能证据（91.8% 的论文含 Performance）；洞察型贡献（64.8% 含 Insight）要单独成条，不要埋进方法条目。纯 Insight 的论文只占 0.9%，只有发现-解释型才考虑不给性能条目。

---

## 2. 逐段写法

每个功能段按同一格式说明：任务、段首句、段内句子顺序、段尾过渡、句式模板（附原句和出处）、注意事项。

### 2.1 领域背景段（BG）

**任务**：用 1 段（最多 2 段）告诉读者这个任务是什么、为什么重要、最近进展到哪里，并在段尾留下一个下段可以接住并反转的关键词。

**段首句，从以下 7 种里选 1 种**：
1. 任务定义式："X aims to …"（ETCTrack、CDA-VSR、FreqSIC）——最稳妥。
2. 重要性断言式："X is a fundamental task in Y, with broad applications such as A, B, and C."——配 2–3 个引用。
3. 趋势 / 时代式："Since the advent of …"、"Recent years have witnessed …"——适合热门方向。
4. 数字 / 事实式：用具体数据制造紧迫感——适合医学、交通、遥感、数据集论文。
5. 场景 / 具象式：用一个具体物理过程开篇——适合具身、感知类论文。
6. 警句 / 典故 / 类比式：一句短判断或生物类比——需要有后文呼应（SpiderCam 的跳蛛类比贯穿全文）。
7. 设问式："Is it possible to …?"——少用，全文最多一次。

**段内顺序**：
1. 定义或断言，附引用；
2. 应用场景，或技术演进时间线（"Traditionally … More recently …"，Rotation Averaging）；
3. 收窄到本文要处理的子问题；
4. 段尾写一个正面词或进展词（promising / remarkable progress），留给下段用 However 反转。

**段尾过渡**：以正面判断收尾，下段首句原词复现并反转。例如 ChordEdit 背景段以 "promising" 收尾，下一段用 "remains unmet" 反转；或用 "Despite its significance, X remains challenging and has received limited attention."（RGB-A）作为背景段尾句，直接引出 GAP。

**句式模板**：
1. "X aims to Y by Z, thereby achieving W."（FreqSIC）
   原句："Visual tracking aims to locate a target throughout a video sequence using its initial state from the first frame as reference."（ETCTrack）
2. "X is a fundamental task in Y, with broad applications such as A, B, and C."（CDIOD/DGS）
   原句："Registration is a fundamental problem in CV, SLAM, and pose estimation."（Registration beyond Points）
3. "X has long been a central research topic in Y."（Fresco）
   原句："Reconstructing 3D structure from 2D observations has been a central challenge in computer vision since its inception."（2D-LFM）
4. "X have emerged as a vital technique/dominant framework in Y."（SEELE、Transition Models）
   原句："Pretrained foundation models have become the backbone of modern machine learning, offering powerful general-purpose representations [35]."（Cleaning the Pool）
5. "The advent of X, such as A [ref], B [ref], …, has introduced a new paradigm …"（ChordEdit，用列举引用增强可信度）
   原句："Since the advent of Large Language Models (LLMs)..., reasoning has emerged as a critical capability..."（MUPO）
6. 数字开篇原句："Cardiovascular diseases (CVDs) remain the leading cause of death worldwide [22]."（CMR-RD）；"Maritime transportation underpins over 90% of global trade, yet 26,000 marine casualties occurred..."（ENC-Bench）；"Forests, covering approximately 31% of Earth's land surface, are essential..."（ForestFormer3D）
7. 场景开篇原句："When a robot grasps an object, two coupled changes occur: proprioceptive transitions...and semantic transitions..."（CLaD）；"Newborns perceive a world that is blurry, desaturated, and continuously unfolding in time."（CATDiet）
8. 警句或典故原句："Motion is intrinsic to human experience."（NRMF）；"Jumping spiders accurately estimate distances using a brain the size of a poppy seed."（SpiderCam）；"Virtually, no word has drawn more attention than Sora in 2024."（TimeRipple）

**注意事项**：
- 首句要有信息量：给定义、数字或具体场景，不要写"X has attracted much attention"这类无主张的句子。
- 需要交代术语谱系时，在首句写清："Category discovery—first introduced as NCD and later extended to GCD—has recently emerged..."（EAGC）。
- 可以把前人的原话作为反驳对象引用（QuadSync 引用 "[1] state that 'Currently the quadrifocal...tensors are useful only from a theoretical stand-point.'"），这种开篇要求后文能正面推翻它。
- 背景拆成 2 段时，第 2 段应比第 1 段更具体，负责收窄（材料 6 的"背景收窄具体化"段）。

---

### 2.2 现有方法与局限段（GAP）

**任务**：把现有工作归成可以批评的类别，指出一个具体、可验证的缺口；段尾要落到下段会展开的那个缺口词上。

**段首句**：从以下 4 种里选：
- 分类式："X can be broadly grouped into two categories: A; and B."
- 让步式："Despite these advances, …" / "While X have achieved …, they …"
- 对立式："On one hand, … On the other hand, …"
- trade-off 式："X face a fundamental trade-off between A and B."

**段内顺序**：
1. 点名方法类别，附引用；
2. 中性描述其机制，并肯定它做到了什么；
3. 转折后给出技术性局限，最好点名具体方法和具体数据集；
4. 说明局限导致的后果；
5. 段尾用一个总结词（gap / trade-off / remains unexplored）或设问收束。

**变体**：
- 聚焦单一前作：只批评一篇最相关的工作（SGAD 批 MESA；CoopTrack 批 UniV2X）。
- 代际综述：按方法代际逐代指出局限，最后收窄到最相关竞品（UIKA）。
- 先排除读者可能想到的替代方案："Another trivial solution, though unexplored, could involve..."（LaRender）。
- 实证坐实：用预实验或可视化证明缺口确实存在，并配图（ETCTrack、ApET、CMR-RD）。

**段尾过渡**：写"remains a significant gap / largely underexplored / fundamental trade-off"，下段用 "This gap arises from …" 或 "The root cause …" 接住；也可以用设问收束："These limitations lead us to consider: Can we…?"（FoleyDirector）。

**句式模板**：
1. "X can be broadly grouped into two categories: A; and B."（CoRoGS）
   原句："Current approaches...predominantly fall into two categories, both inherited from Y and suffer from fundamental limitations."（Lafite）
2. 先肯定后付出代价："Existing one-step text-guided method [24] achieves fast performance by training dedicated networks, sacrificing model-agnostic flexibility..."（ChordEdit）
3. 先让步后批评："While effective in preserving key details, these approaches often lead to redundant selections with low information density."（CoIn）；"While these methods have achieved impressive results, they often rely on Z designed for A rather than B."（STRNet）
4. 对称双批评："On one hand, 3D generative models excel at generating a high-quality canonical 3D object O, while completely ignoring the camera pose θ."（CUPID）；"S1...maintain strong X but exhibit near-zero Y; S2...improve Y but suffer notable drops."（The Geometry of Robustness）
5. "Despite these diverse attempts, NF-based methods remain limited in their ability to use powerful, general-purpose architectures..., in contrast to many modern generative model families."（BiFlow）
6. 编号列举："However, both approaches exhibit inherent limitations: (1)...; (2)..."（LiteSense）；"Nevertheless, deep learning–based DIR still faces two obstacles: (i)..., and (ii)..."（MorphSeek）
7. 批评隐含假设："However, most existing IOD studies oversimplify real-world challenges, assuming incremental learning occurs within a single, general domain."（CDIOD/DGS）
8. 空白声明："So far, there does not exist any X approach that combines: (i)…(ii)…(iii)…"（3D Shape Matching）；"To the best of our knowledge, no existing X simultaneously provides both A and B."（OLATverse）

补充 trade-off 式原句："Existing approaches for cinematic video generation face a fundamental trade-off between generative flexibility and scene consistency."（CineScene）

**注意事项**：
- 局限必须是技术性的，并且能被实验验证。不要只写"效果不好"，要写清"在什么条件下、因为依赖什么、导致什么"（Uni3R："However, X are built upon Y, which is inherently designed for Z."）。
- 批评要点名。"Existing detectors bypass genuine 3D geometric understanding by relying on frozen foundation models tailored for other vision tasks..."（3PT）按"点名基线 + 技术选择 + 后果"组织。
- 这里列出几条缺口，后文就要有几个模块或几条贡献对应（S3）。
- 双线批评时，两段的句式和长度要对称，最后用一句归纳共同缺口："Thus, the entire field converges on a fundamental, yet flawed, compromise."（Transition Models）

---

### 2.3 根因 / 挑战段（ROOT）

**任务**：把"效果不好"推进到"为什么不好"，而且要落到机制、公式、统计量或被违反的假设上。根因要能直接推出洞察。

**段首句**：显式归因句，常用 "The root cause lies in …" / "This X arises from …" / "We identify that these failures stem from …"。

**段内顺序**：
1. 归因句；
2. 机制解释：可以给公式、数量级或控制变量实验；
3. 如果有多条根因，用 (1)(2)(3) 或 First/Second 编号，数量与后文模块一致；
4. 段尾写一句"违反了某个假设 / 缺少某样东西"的判断，作为洞察的入口。

**段尾过渡**：用 8 词左右的短句收束，例如 "Thus, the optimal band is sample-dependent."（MFEN），或 "Taken together, these observations suggest that the obstacle...is the lack of..."（PixelDiT），下段用 "Our key insight is …" 或 "To this end, …" 接住。

**句式模板**：
1. "The root cause lies in the editing field computed via naive differencing."（ChordEdit）
2. "This behavior arises from X."（FluoCLIP，接公式 d∝λ/NA）；原句："This issue arises because the intra-slide invariance objective limits..."（GECKO）
3. 编号归因："We identify that these failures stem from three tightly coupled issues: (1)…(2)…(3)…"（IR-HGP）；"This gap persists due to two fundamental challenges. First,... Second,..."（DetGain）
4. 排除式归因 not…but…："This discrepancy is attributed not to a lack of algorithmic innovation, but to inherent limitations in data scale..."（Go to Zero）；"The root of this dilemma is not architectural, but a learning objective."（Transition Models）；"This limitation arises not only from A, but more fundamentally from B."（The Midas Touch for Metric Depth）
5. 假设归因："X rely on the key assumption that Y, which may not hold in Z."（Generalized-CVO）；"However, these methods assume that dynamics arise mainly from geometric motion, and therefore struggle when..."（RetimeGS）
6. 控制变量排除："This drift arises even when dataset class frequencies remain fixed, indicating that the dominant source of bias...is the model-induced prior rather than the count-based prior."（AdaPrior）
7. 量化根因："Specifically, more than 90% of the visual tokens have attention scores below 10⁻³, indicating that..."（Thinking with Drafts）；"An N×N determinant may involve up to N! terms, leading to factorial growth..."（FFT-Based Interpolation）
8. 跨领域类比："This mirrors tokenization in natural language processing: patch chunks are like character-level tokens—fine-grained yet myopic."（CARE）

**注意事项**：
- 根因段是可选段，但根因句是必需的。紧凑式里它可以只占 GAP 段的最后一句（ChordEdit）。
- 可以用图证明根因："As illustrated in Fig. 1, existing reinforcement learning–based post-training methods...are dominated by majority classes..."（CMR-RD）。
- 需要引用他人提出的概念时标上引用："We posit the root cause is visual confounding [30]..."（CIGPose）。
- 如果要给新发现的问题命名，就在这一段做（见 references/naming.md §5.4），例如 "We refer to these underexplored issues in X as Y (abbr)."（EAGC）。

---

### 2.4 核心洞察段（INS）

**任务**：用一句话给出"换个角度看问题"的判断。这句话是全文的创新点，方法应当能从它直接推出。

**段首句**：用显式标志词，选以下之一：
- "Our key insight / key observation / key idea is that …"
- "We argue / posit / hypothesize that …"
- "We adopt a different perspective … and recast X as Y."
- 设问："This raises a critical question: …?"

**段内顺序**：
1. 洞察句；
2. 说明洞察从哪里来：观察、类比、预实验或引用 Fig.；
3. 说明这个洞察意味着什么（"This insight inspires a new approach: we can V1…and V2…"，PRIMED）；
4. 过渡到方法命名。

**段尾过渡**：用 "Building on this insight, …" / "Motivated by this, …" / "Based on these insights, …" 进入 MTH。设问式要在下段首句直接回答："The answer is yes."（GECKO）或 "We answer this question with X, a new framework that..."（FedTSP）。

**句式模板**：
1. "Our key insight is that a token's intrinsic information can be effectively captured by its linear approximation error."（ApET）
2. 对比式洞察："Unlike prior approaches that align static states across modalities, our key insight is that consistency should be enforced over transitions."（CLaD）
3. "Our key observation is that multi-period scene reconstruction is neither static nor smoothly dynamic — it is discrete in periods but shared in major structure."（ChronoGS）
4. 视角转换："We adopt a different perspective from simple vector arithmetic and recast the editing problem from the principled perspective of dynamic optimal transport..."（ChordEdit）；"In this work, we start from a different perspective: X."（UniPart）
5. 立场："We argue that the representation space offers rich information beyond optimizer designs."（Rep-MTL）；"We posit that one key factor underlying this limitation is…"（ForeAct）
6. 设问："This raises a critical question: Are ground-truth novel-view poses truly indispensable...?"（No Pose at All）；"If this path is so clearly superior, why has it not yet dominated?"（Lafite）；"We investigate a fundamental question: Is language supervision necessary to pretrain visual representations?"（Web-SSL）
7. 类比作证据："This mirrors how humans perceive the world: as illustrated in Fig. 1, we readily infer that the image captures the plush toy from its left frontal side."（CUPID）；"Similar to the 80/20 rule, an observation is: A but B; while C but D."（SparseOIT）
8. 条件式或极简式："For mixed signals from two views, if we introduce temporal optical modulation to one view, the variations will provide strong cues for effectively decoupling binocular videos."（240FPS Stereo）；"Our key insight is simple: motion = content + style."（RoboPerform）

补充两种反直觉写法："Interestingly, we find that pruning certain weights can increase the accuracy..."（NuWa）；"Our results, however, suggest otherwise."（MotionCrafter，六个词完成反转）。

**注意事项**：
- 洞察可以独立成段、加框或加粗，并且位置可以提前（2D-LFM 的 Core Insight 框；ConFu 加框问句；SpatialTree 独立缩进问句；UniPart 全文加粗钩子）。
- 设问全文最多用 1 次（DMDX 全篇只有一个问句，DIMO 也只有一次）。多份材料指出，大量引言完全不用问句，只靠关键词回指和因果连词过渡，所以设问不是必需的。
- 洞察的关键词要成为方法名或模块名的词根（DeltaWorld / DeltaTok 的 "Delta" 对应洞察"帧间差值低维"），见 references/naming.md §2.5。
- 动词强度要与证据强度匹配：有实验支撑时用 find / observe，推测时用 posit / hypothesize（ALG："We hypothesize that X is caused by Y, preventing Z."）。

---

### 2.5 方法概述段（MTH + DET）

**任务**：一句话给出方法名和定性描述，然后说明核心机制，再逐个展开组件，每个组件回应一条根因。

**段首句（固定骨架）**：
`[目的状语], we [propose/introduce/present] [Name] ([Full Name]), a/an [定性形容词] [类别名词] that [核心机制].`

**段内顺序**：
1. 命名句（同位语定性，例如 training-free / lightweight / the first …）；
2. 核心机制一句；
3. 组件：用 First / Second / Finally，或 (1)(2)(3)，与 ROOT/GAP 的编号镜像对应；
4. 嵌入 "(see Fig. N)" 或 "(Fig. 1)"；
5. 段尾回收根因段的原词，形成闭环（材料 7："段尾回收根因词汇闭环"）。

**段尾过渡**：接 "Extensive experiments …" 进入 RES；或接 "In summary, our contributions are …" 直接进入 CON。

**命名句模板**：
1. "To overcome these challenges, we introduce ChordEdit, a training-free, inversion-free and lightweight method..."（ChordEdit）
2. "To address these limitations, we introduce NITROGEN, an open foundation model...trained on 40,000 hours."（NitroGen）
3. "To this end, we introduce CUPID (for 'in-CUbe PIxel Distribution'), a probabilistic reconstruction framework..."（CUPID，名字后面立即解释全称）
4. "In this paper, we propose LF Blind-View Network (LF-BVN), a novel self-supervised framework for LF denoising."（LF-BVN）
5. "Based on these insights, we build LagerNVS, a Latent Geometry model for Real-time NVS (Fig. 1)."（LagerNVS）
6. 先否定对手前提再命名："In this work, we argue that this trade-off is not fundamental. …we introduce X."（InstantViR）；合并式："We propose to marry the best of both worlds — namely MASt3R and 2DGS."（Sparfels）
7. 先讲道理后命名："Since the training objective is to learn the transitions between any state to a previous state, it is named Transition Models (TiM)."（Transition Models）
8. 理论论文的克制写法："In this paper, we aim to provide a theoretical understanding of the difference between conditional and unconditional outputs..."（C²FG）

**组件展开模板**：
- "First, to ensure X, we introduce Y (ABBR). Second, we observe that...Finally, while A effectively enforces B, it inevitably introduces C."（WorldForge：用 "we observe" 把经验发现和设计区分开）
- "In the latent space, we introduce a X..." / "In the noise space, we propose a Y..."（RGB-A，两个组件用对称句式）
- "Unlike previous methods that split the input into two regions..., the proposed X module introduces..."（TriLite）
- "Instead of predicting Gaussian means as depths along camera rays, we directly regress their 3D coordinates."（TokenGS，用对比式代替同位语式）
- "Building upon this dataset, we introduce FluoCLIP…"（FluoCLIP，Building upon 表示贡献之间有依赖）

**注意事项**：
- 全文只用一个主动词。CLaD 在这里用 "suggest"，全文其他地方用 "propose"，材料把它列为不一致的反例。
- 首次登场要写"全称 (缩写)"，之后全文只用缩写（Soft-Braid Refiner (SRefiner)，材料 13）。
- 常把 "the first" 放在命名句里一起宣称（MEMFOF："the first multi-frame optical flow method..."；SAFE-GRPO："the first flow-based reinforcement learning framework…"）。只有在确实首创时才写，并可加 "To the best of our knowledge"。
- 定性词用精确限定语（training-free、Confidence-Guided、Content-Aware），不要用 revolutionary / breakthrough 这类营销词（材料 2、3、6 都指出样本中没有 Super/Ultra/Mega/Magic 类词）。
- 方案会带来新问题时，先承认再给子方案（GaitMax → CDLoss → GCaption；LinkVLA 先扬后抑引出下一机制）。

---

### 2.6 结果预告段（RES）

**任务**：用 1–3 个具体数字证明方法有效，数字要和实验表格一致。常与 Fig. 1 绑定。

**段首句**：从以下选：
- "Extensive experiments on A, B, C demonstrate that X …"
- "As shown in Figure 1, X …"
- "Despite its simplicity, X surpasses …"

**段内顺序**：
1. 实验范围（多少个数据集或任务，哪些基准）；
2. 主结果数字，写相对提升或倍数；
3. "while maintaining …"，说明没有牺牲其他指标；
4. 可选：泛化或首创结论。

**段尾过渡**：直接接贡献引导句。

**句式模板**：
1. 与表格逐一对应："3PT exceeds the performance of prior methods on 12/13 detection datasets, with 68.8% and 31.8% relative improvements on BOP-Industrial and BOP-H3."（3PT）
2. 倍数加 up to："Our method yields up to 8× and 10× speedups on VGGT and π3, respectively."（AVGGT）
3. 准确率加压缩率："When applied to LLaVA-1.5-13B model, CoIn achieves an average accuracy of 91.0% across 9 benchmarks with 94.4% visual tokens reduced."（CoIn）
4. 两全式："...outperforming top holistic reconstruction models by over 3 dB PSNR while matching the geometric accuracy of state-of-the-art monocular estimators."（CUPID）
5. 多指标 respectively："Compared to DepthCrafter, we achieve 13× faster inference, improving accuracy by 13.2%, 86.8%, 39.3%, 8.2%, respectively."（StableDepth）
6. 简单却更强："Despite its simplicity, X surpasses Y across established benchmarks, including A, B, C."（TriLite）
7. 挂 Fig. 1："As shown in Figure 1, TiM shows superior performance across different NFEs, resolutions, and aspect ratios."（Transition Models）；"As a preview, X substantially boosts Y, as illustrated in Fig. 1."（Inf-SSM）
8. 泛化或强基线："Experimental results demonstrate that X, despite being trained on only 30 tasks, successfully generalizes to over 800 tasks."（CrossHA）；"Even in this setting, C2FG yields further gains in both FID and IS scores while maintaining other metrics."（C²FG）

**注意事项**：
- 要限定比较范围，避免过度宣称："…representing the state-of-the-art performance among single-X-based methods."（HyperGait）
- 引言只建立问题、缺口、方案、最强结果和意义，不提本文的不足或局限，也不预告哪里不如对手（`references/anti_defensive.md` §0）。
- 同一句里可以用两种强度的动词，与实际结果对应："...is comparable to state-of-the-art reflection-aware methods...while it better estimates the albedo..."（PhyGaP）
- 数据与基准型论文预告的是"问题有多难"："Top methods developed by academia are still far from solving this benchmark."（Benchmarking Egocentric VI-SLAM）；"Comprehensive evaluation across 25 LMMs exposes key challenges: 1)...2)...3)..."（Multi-Crit）
- 用规模作证据也可以："We evaluate the pretrained model on 33 downstream tasks."（CARE）
- 统一框架型要让两边的指标对称出现："...achieves state-of-the-art performance on multimodal understanding and generation benchmarks (e.g. 61.2% on MMStar and 0.90 on GenEval)."（TUNA）

---

### 2.7 贡献列表段（CON）

**任务**：把全文交付物列成 3–4 条，每条独立可验证，顺序与前文缺口 / 模块一致。

**形式选择（1040 篇统计）**：bullet 74.4%（默认）｜inline 25.0%（篇幅紧，或贡献之间是递进关系）｜none 0.6%（不要选）。

**引导句（任选其一，属于低信息量的结构标记，不要改写成花哨句子）**：
- "Our contributions are summarized as follows:"
- "In summary, our (main) contributions are (as follows / threefold):"
- "Overall, the contributions of this paper are as follows:"
- "To summarize, our contributions are as follows:"（LagerNVS）
- "This paper makes the following contributions:"（GFPack++）
- "In a nutshell, our contributions are summarized as follows:"（VeilGen）
- 发现型："Our main findings are:"（Mechanisms of Object Localization）

**条目顺序（推荐粒度）**：①框架整体 / 核心洞察 →②核心机制或模块 →③数据 / 基准（如有）→④实验证据（含数字）。这个顺序也对应 1.5 中 Insight / Capability / Performance 三类贡献。

**条目模板**：
1. 同位语式（最常见）："We propose/introduce X, a Y that Z."
2. 子模块级："We design/develop X that extracts Y and Z."（HyperGait）
3. 首创声明："To the best of our knowledge, we are the first to..."（Talk2Move）；"We introduce X,...that, to the best of our knowledge, has not been previously explored."（TriLite）
4. 加粗标签开头："**New problem.**" "**Comprehensive benchmark.**" "**Novel insights.**" "**Effective framework.**"（SSMDG）
5. inline 序数："First, we propose X...Second, we introduce Y...Finally, we design Z."（Sparse-LaViDa）；"To summarize: (i) we introduce…; (ii) we enable…; (iii) we propose…; (iv) we achieve…"（Enrich and Detect）
6. 无主语名词短语式："A data capture pipeline for…" "A multi-view dataset for…"（Hoi!）；"A ... framework that..." "An ... memory that..."（Spatial-SAM）
7. 实验末条："Extensive experiments demonstrate that X achieves state-of-the-art…"（FreqSIC、FreM；常与摘要末句同构）
8. 一条内部分号并列："We introduce X (ABBR), which: Generalizes...; leverages...; Extends...; provides..."（BQ-SRC）

**注意事项**：
- 条目动词要有变化：CausalNet 依次用 propose / conduct / present / demonstrate；Gallant 按强度分层 propose > verify > develop。
- 末条可以换成过去时表示"已验证"："The proposed solver achieved higher numerical stability"（FFT-Based Interpolation）。
- 编号缺口 (i)(ii)(iii) 要与贡献条目镜像对应（CROWn、CHIRP）。
- 数据与基准型把开源承诺写进末条（Derm1M、TMR）。摘要末句作用为"资源发布"的占 43.1%，引言贡献列表末条可以与之呼应。
- 反例：引导句漏词的病句 "Contributions of this paper are summarized follows."（OOD，漏了 "as"）。

---

## 3. 衔接手法

### 3.1 段与段之间

| 手法 | 什么时候用 | 可直接套用的句式 | 出处 |
|---|---|---|---|
| 关键词回指（顶真） | 任何两段之间，首选 | "This gap …" / "These limitations …" / "To address these challenges, …" / "all the aforementioned limitations" | BridgeDepth、MeshSplatting、RESCUE |
| 原词反转 | BG→GAP | 上段尾 "…is promising." → 下段首 "However, …remains unmet." | ChordEdit |
| 让步转折 | BG→GAP；GAP 内部 | "However, …" / "Despite these advances, …" / "While X …, Y …" / "Yet …" / "Nevertheless, …" | 几乎所有论文的 GAP 段 |
| 目的状语 | GAP/ROOT→MTH | "To this end, …" / "To address this, …" / "To bridge this gap, …" / "Motivated by this, …" / "Inspired by this, …" / "Guided by X, …" | CAGS、EgoXtreme、ENC-Bench、Selection-as-Nonlinearity |
| 因果收束 | ROOT→MTH | "…nonviable. Thus, we propose AIM…" / "This motivates us to …" | AIM |
| 递进依赖 | MTH 内部多产出之间 | "Building upon this dataset, we introduce …" / "Based on this, we propose the … framework." | FluoCLIP、PRIMED |
| 设问—回答 | INS→MTH | 段末 "Can we …?" → 下段首 "The answer is yes." 或 "We answer this question with X, …" | GECKO、FedTSP |
| 对比 | GAP→MTH；MTH 内部 | "In contrast, …" / "Unlike previous methods that …, we …" / "Instead, in this paper, we introduce …" | AdvFractal、Omni-3DEdit、SFP |
| 数字预告—编号兑现 | GAP→ROOT→MTH→CON | "…faces two distinct challenges." → "Challenge 1 / Challenge 2" 或 "To address challenge ❶ … For challenge ❷ …" | GECKO、GSV2X、《水下SLAM》 |
| 对仗段首标签 | 双线批评 | "On the model side … / On the data side … / On the optimization side …"；"A line of research … / Another line of research …" | UltraFlux、RLER、RetimeGS |
| 归纳收束 | 多条局限→根因 | "Taken together, these challenges reveal …" / "Altogether, …" / "Thus, the entire field converges on a fundamental, yet flawed, compromise." | URICA、UltraFlux、Transition Models |
| 情绪反转词（少用） | 缺口→希望 | "Fortunately, …" / "Encouragingly, pre-trained VLMs …" / "Interestingly, …" | GROC、HDR-VLM、FixTalk |
| 图证衔接 | GAP 或 INS | 上段 "As illustrated in Fig. 1 right, …"，下段开头重复其中的批评用语 | CoRoGS |
| 加粗小标题硬切换 | 问题陈述→方案 | "**Our approach.**" | Cleaning the Pool |
| 命名对仗回指 | 方法名与前作相对 | "As suggested by the name, UnZipLoRA operates in the opposite direction of ZipLoRA." | UnZipLoRA |

### 3.2 句与句之间

- **指代词固化问题实体**：一个问题在第一次出现后，后续一律用 "This paradigm / These predicted trajectories / This decoupling" 指代（GraspALL、GeoPredict、AL-GCD）。
- **冒号制造停顿**："This overlooks a crucial aspect of physical reality: ambiguity."（UniPixie）；"The critical flaw in this design is X: Y."（GeoRelight）
- **Specifically 展开**：先写判断句，再用 "Specifically, …" 给数字或机制（Thinking with Drafts、GeoRK2）。
- **"not A, but B" 排除式**：先排除读者的默认解释（Go to Zero、Transition Models）。
- **"while" 两全**：结果句和机制句都用 "…, while maintaining …" 说明没有牺牲其他指标。
- **术语全篇不换词**：同一个概念在摘要、引言、图注、贡献中用同一措辞。反例：摘要写 "medium"、正文变成 "moderate"（材料 8）；同一机制在摘要、正文、贡献列表出现三种叫法（Dual-branch Distilled Transformer）。
- **类比连接**："Similarly / Analogously"（Differentiable Room Acoustic Rendering）；"Conceptually aligned with...RAFT"（HypoDepth）。

### 3.3 按位置的过渡句速查

| 位置 | 句式 |
|---|---|
| BG → GAP | "However, X remains largely underexplored." / "Despite these advances, existing work has not explored X." / "Despite its significance, X remains challenging and has received limited attention." |
| GAP → ROOT | "This gap persists due to two fundamental challenges." / "We identify two key reasons. First, … Second, …" / "This is because …" |
| ROOT → INS | "In this work, we posit/argue that …" / "We revisit this assumption and reveal an overlooked issue: …" / "This raises a critical question: …?" |
| INS → MTH | "Building on this insight, we propose …" / "Motivated by this perspective, we propose …" / "Based on these insights, we build …" |
| GAP → MTH（跳过 ROOT/INS） | "To address these limitations, we propose X, a Y that Z." |
| MTH → RES | "Extensive experiments on A, B, and C demonstrate that …" / "As shown in Fig. 1, …" |
| RES → CON | "Our contributions are summarized as follows:" |

---

## 4. 关键元素

### 4.1 核心创新出现的位置

- **标准位置**：洞察句位于 ROOT 之后、方法命名句之前。在 5–6 段引言中，洞察和命名通常出现在第 3–4 段（材料 2 的标准六段：背景→局限→根因→洞察→方法→贡献）。
- **先洞察后命名**：洞察是"想法"，命名是"产品"，先出现洞察。可以两级命名，先给范式或概念一个不带缩写的名字，下一段才给出缩写（CAGS 先称 "Hierarchical Multi-scale Paradigm"；HippoVLM 先提 "HippoSense"，模型名晚一句出现）。
- **洞察独立醒目**：可以独立成段、加框或加粗（2D-LFM Core Insight 框；ChronoGS 用 "We define…" 加 "Our key observation…" 独立成段）。
- **延迟命名**：发现驱动型可以把命名推迟到贡献列表（FedAdamom），或推迟到方法正文（RALoc 在引言里不提数据集缩写）。
- **完全不命名**：当核心创新就是洞察句本身时，可以不起专名（P3P）。
- **与摘要对照**：摘要 5 等分后，第 2/5 段的主作用中"方法"占 44%，说明创新在摘要前 40% 就出现了。引言也应在前半部分让读者知道"本文换了什么视角"，不要拖到最后一段。

### 4.2 Figure 1 的引用

91.3% 的论文在第一页或引言有 teaser 图。引言中引用 Fig. 1 的 6 种用法：

| 用法 | 位置 | 句式 / 例证 |
|---|---|---|
| 图证缺口 | GAP | "As illustrated in Figure 1, IGPP suffers from two core drawbacks."（VPDR）；"As illustrated in Fig. 1, existing reinforcement learning–based post-training methods...are dominated by majority classes..."（CMR-RD） |
| 图证洞察 / 类比 | INS | "This mirrors how humans perceive the world: as illustrated in Fig. 1, …"（CUPID）；"as illustrated in Fig.2(a)"（Scone） |
| 挂在命名句上 | MTH | "…we build LagerNVS, a Latent Geometry model for Real-time NVS (Fig. 1)."（LagerNVS）；"As shown in Figure 1, our framework, called X (...), is capable of..."（RESCUE） |
| 结果预告 | RES | "As shown in Figure 1, TiM shows superior performance …"（Transition Models）；"Fig. 1 features our work."（Wan-Weaver，极简） |
| 一图分段引用 | GAP 与 INS 分别引用 | Fig. 1(a)(b) 分别在缺口段和洞察段引用，形成问题→方案闭环（SCORE、SGAD、DUO）；"upper half of Fig.1" / "lower half of Fig.1"（See-NeRF） |
| 多段连引 / 逐条配图 | 多段 | ReME 的 Fig. 1b 在三段中连续引用；ForestFormer3D 每条挑战配 Fig. 1(a)(b)(c) |

执行规则：Fig. 1 在引言中至少引用 1 次，推荐 2 次，分别对应"问题"和"方案/结果"；图注要能单独读懂。

### 4.3 贡献列表写法（结构层面）

- 放在引言末段；bullet 是默认形式（74.4%）。
- 3 条最常见（"threefold"），不超过 4 条。
- 每条以 We + 动词开头，或用加粗标签开头；条目之间动词要有变化。
- 贡献列表必须能与前文的缺口编号一一对应。
- 性能条目几乎必有（91.8%），洞察条目在 64.8% 的论文中出现。
- 首创声明加 "To the best of our knowledge"（ActiveAD、Talk2Move），作为降低风险的套句。
- 贡献之后可以加一句路线图或开源声明（材料 6 的"意义升华 / 路线图"）。

---

> 取名（起不起名、构造方式、子模块与数据集命名、现象命名、标题）见 references/naming.md。引言里名字的登场写法用第 2.5 节的命名句模板：在方法段首次写"全称 (缩写)"并配同位语，之后只用缩写；其他登场句式见 references/naming.md §4。

---

## 5. 范例：段落级拆解

说明：以下拆解由汇总材料中出现的原句和结构描述重建。材料没有给出的句子标为［材料未给出］，写作时不要当作原文引用。

### 范例 1：ChordEdit（S2 紧凑三段式，瓶颈突破型）

| 段 | 功能 | 关键句（原文） | 写法要点 |
|---|---|---|---|
| P1 | BG | "The advent of one-step text-to-image (T2I) models, such as SD-Turbo [28], SwiftBrush-v2 [5]..., has introduced a new paradigm..." | 用列举引用建立可信度；段尾以正面词 "promising" 收束，给下段留下反转点 |
| P2 | GAP + ROOT | "Existing one-step text-guided method [24] achieves fast performance by training dedicated networks, sacrificing model-agnostic flexibility..." → 用 "remains unmet" 反转上段的 "promising" → "The root cause lies in the editing field computed via naive differencing." | 先肯定再说代价（sacrificing）；根因只用一句，而且落在具体操作上（naive differencing） |
| P3 | INS + MTH + RES + inline CON | "We adopt a different perspective from simple vector arithmetic and recast the editing problem from the principled perspective of dynamic optimal transport..." → "To overcome these challenges, we introduce ChordEdit, a training-free, inversion-free and lightweight method..." → "...achieving state-of-the-art efficiency while maintaining high background preservation and semantic fidelity." | 洞察用"换视角 + recast"；命名句带三个限定语；结果用两全式（efficiency while maintaining fidelity）；贡献 inline |

可以照搬的结构：
1. 背景段尾写正面词，下段首句原词反转；
2. 根因一句，接在局限之后；
3. 洞察句把旧做法（vector arithmetic）作为对照；
4. 命名句的定性词与根因相对（naive → principled）。

### 范例 2：GECKO（S6 设问 + 编号镜像往返式，瓶颈突破型）

| 段 | 功能 | 关键句（原文） | 写法要点 |
|---|---|---|---|
| P1 | BG | "There has been a surge in foundational models (FMs) in the...domain, scaling..." | 趋势式开篇 |
| P2 | GAP（数字预告） | "However, this pretraining paradigm faces two distinct challenges..." | 先预告"两个挑战"，后文用小标题 Challenge 1 / Challenge 2 回收 |
| P3 | ROOT | "This issue arises because the intra-slide invariance objective limits..." | 归因到训练目标的机制 |
| P4 | INS（设问） | "To this end, we ask: Can we...?" 紧接 "The answer is yes." | 设问后立即作答，不拖到下一段 |
| P5 | MTH | ［材料未给出命名句原文］；名字 GECKO 是 backronym（谐音壁虎） | 方案按 Challenge 1 / 2 逐一拆回（材料 11："挑战编号→展开→设问汇合→方案逐一拆回"） |
| P6 | CON | "In summary, our main contributions are:" | 贡献与两个挑战对应 |

可以照搬的结构：
1. "two distinct challenges" 的数字预告，由后文编号小标题回收；
2. 设问和作答写在同一处；
3. 方案、贡献与挑战的顺序完全一致。

### 补充对照：Transition Models（S4 双线批评，先讲道理后命名）

材料给出的关键句按功能排列如下（段落划分依据材料 6 对其"双层 / 双线批评式"的描述推定）：
- 背景："X have emerged as a vital technique/dominant framework in Y."（模板形式）
- 双线归纳："Thus, the entire field converges on a fundamental, yet flawed, compromise."
- 根因："The root of this dilemma is not architectural, but a learning objective."
- 命名："Since the training objective is to learn the transitions between any state to a previous state, it is named Transition Models (TiM)."
- 结果："As shown in Figure 1, TiM shows superior performance across different NFEs, resolutions, and aspect ratios."

要点：
1. 根因用 not…but… 排除读者的默认猜测（"是架构问题"）；
2. 名字直接由根因（learning objective = transitions）推出，把命名当成论证的一部分；
3. 结果预告挂在 Fig. 1 上。

---

## 6. 写引言的步骤与检查清单

### 6.1 步骤（按顺序执行）

**Step 0｜输入准备**：动笔前先写出以下 7 项，缺任何一项先向用户确认：
- (a) 故事类型（第 1.4 节 8 类之一）；
- (b) 一句话核心洞察；
- (c) 根因条数 N，以及每条根因的机制；
- (d) 方法模块，数量等于 N 或与 N 对应；
- (e) 主结果的 2–3 个数字（来自实验表格）；
- (f) Fig. 1 画什么：问题对比、方法示意，还是结果对比；
- (g) 是否起名（references/naming.md §1.3）。

**Step 1｜选骨架**：按故事类型从 1.3 选序列（S1–S10），定段数（默认 5–6），并为每段写一行功能标签。

**Step 2｜先写洞察句（INS）**：它决定了局限和根因要怎么写，所以最先写。

**Step 3｜起名**：按 references/naming.md §8 的流程完成，写出"全称 (缩写)"和一句同位语定性。

**Step 4｜倒推 ROOT 与 GAP**：从洞察反推"现有方法违反了什么假设 / 缺少什么"。GAP 的编号条数 = ROOT 条数 = 模块数 = 贡献中的方法条数。

**Step 5｜写 BG**：选一种段首句（2.1），段尾留下正面词。

**Step 6｜写 GAP 与 ROOT**：点名具体方法和数据集；根因要落到机制、公式、统计量或假设；需要时用图或预实验证明。

**Step 7｜写 MTH（+DET）**：用固定骨架的命名句，组件按编号镜像展开，嵌入 Fig. 引用，段尾回收根因原词。

**Step 8｜写 RES**：数字与表格逐一核对；用 up to / respectively / while maintaining；限定比较范围。

**Step 9｜写 CON**：选 bullet 或 inline；用引导句加 3–4 条；顺序为框架/洞察 → 机制 → 数据/基准 → 实验；动词要有变化。

**Step 10｜衔接检查**：逐个段首检查它是否接住了上一段的末尾（第 3 节的表）。

**Step 11｜按 6.2 的清单逐条勾验。**

### 6.2 检查清单

**结构**
- [ ] 段数在 4–7 之间（默认 5–6）；超过 8 段时，每一段都有独立功能。
- [ ] 包含 BG、GAP、MTH、CON 四个必需功能；ROOT 至少有一句。
- [ ] 所选序列与故事类型相符（1.4）。
- [ ] 贡献列表在末段。

**背景段**
- [ ] 首句是定义、断言（附引用）、数字、场景或典故之一，而不是没有主张的泛泛句子。
- [ ] 段尾有能被下段反转或回指的关键词。

**局限与根因**
- [ ] 局限点名了具体方法或方法类别，并附引用。
- [ ] 每条局限都是技术性、可验证的，写清了条件、依赖和后果。
- [ ] 至少有一个显式归因句（root cause / arises from / stem from / is because）。
- [ ] 根因落到了机制、公式、统计量或被违反的假设上。
- [ ] 编号的局限条数 = 根因条数 = 方法模块数 = 贡献中的方法条数。

**洞察**
- [ ] 有一句显式洞察句（key insight / observe / argue / posit / recast）。
- [ ] 方法能从洞察句直接推出；方法名或模块名的词根来自洞察句。
- [ ] 设问全文不超过 1 处，并且在同一段或下一段段首作答。
- [ ] 动词强度与证据强度匹配（find/observe 对应有证据；posit/hypothesize 对应推测）。

**方法与命名**
- [ ] 命名句符合 "To address …, we propose X (Full Name), a/an [定性] [类别] that …"。
- [ ] 首次出现写"全称 (缩写)"，之后只用缩写。
- [ ] 主动词（propose / introduce / present）全文统一。
- [ ] "the first" 只在确实首创时使用，并可加 "To the best of our knowledge"。
- [ ] 没有 Super / Ultra / Magic / revolutionary / breakthrough 类词。
- [ ] 名字能读出，长度不超过 8 个字符，没有辅音堆砌，没有字母汤。
- [ ] 名字在标题、摘要、引言、图注、表格、贡献中的大小写和拼写完全一致。
- [ ] 借用他人的术语附了引用编号。

**结果预告**
- [ ] 至少有 1 个具体数字（相对提升、倍数、绝对值）。
- [ ] 数字与实验表格一致。
- [ ] 用 "up to" / "respectively" / "while maintaining" 或限定比较范围，避免绝对化。
- [ ] 引言里没有本文的局限或不足。

**Figure 1**
- [ ] 有 teaser 图（91.3% 的论文有）。
- [ ] 引言正文中引用了 Fig. 1 至少 1 次，推荐在问题处和方案/结果处各一次。

**贡献列表**
- [ ] 使用标准引导句之一。
- [ ] 3–4 条；默认用 bullet（74.4%）。
- [ ] 至少一条性能证据（91.8% 含 Performance）；有洞察时单列一条（64.8% 含 Insight）。
- [ ] 条目动词不重复；顺序与前文缺口编号一致。
- [ ] 数据与基准型的末条包含开源或发布承诺。

**衔接**
- [ ] 每个段首都有衔接标记：回指词、转折词、目的状语、对比词或设问作答之一。
- [ ] GAP → MTH 之间有目的状语（To this end / To address / To bridge this gap）或因果连词（Thus / This motivates us to）。
- [ ] 同一概念全文用同一措辞，没有术语漂移。
- [ ] 段首的衔接标记是有逻辑内容的回指、转折、因果或对比，不是 Furthermore / Moreover / Additionally 这类机械过渡（`references/word_style.md` 第 4.2 节）。
- [ ] 语法无误，例如引导句不漏 "as"。
