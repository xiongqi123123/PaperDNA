# Experiments（实验）

> **给正在写这一节的 AI 助手**：本规范来自 CVPR 2026 + ICCV 2025 共 1040 篇精读笔记的归纳，并合并了本 skill 早期的实验规范和 story_types.md 第 3.4–3.6 节中与实验有关的内容。书名号《》里是真实论文标题或方法名；英文句式可以直接套用，但要换成自己的内容。
> - 方法、模块、消融变体、数据集的取名，按 references/naming.md 执行。
> - 用词强度（significantly / SOTA / competitive / slightly 等）和结论措辞，按 references/word_style.md 执行，本文只给实验场景下的具体要求。
> - 所有数字必须来自用户的结果文件或用户提供的数据。**没有数字就留占位符（如 `[XX.X]`）并告诉用户，绝不编造。**

---

## 0. 速查

| 事项 | 默认做法 | 依据 |
|---|---|---|
| 整体骨架 | Setup → 主结果 → 消融 → 机制分析 / 泛化 / 效率 | 各批次笔记里最常见的层次；《CARE》《OSA》《LoftUp》《Backdoor Mitigation by D3》 |
| 节首 | 1–3 句路标句，预告各小节要回答的问题 | 《D4RT》《E-RayZer》《PanoEnv》《MoGA》 |
| 对应关系 | 贡献 i ↔ 方法 3.i ↔ 实验小节 / 表 i；每条贡献至少一个实验 | 8 份批次材料中最一致的规律；《ChordEdit》《PHASE-Net》《NoiseQuery》 |
| 小节标题 | 写成要回答的问题，或用 RQ1/Q1 编号复用引言表述 | 《VeriDou》RQ1–RQ5、《URICA》、《PAVAS》、《MTU3D》 |
| 可复现 | 单设 Setup / Implementation Details：数据集（含划分）、指标、基线、超参、硬件、训练时长 | 几乎所有论文都这样做；《No Calibration, No Depth, No Problem》四个子标题 |
| 基线 | 按 Related Work 的类别分组；说明为何选、是否重训、比较范围 | 《D4RT》《HiLoRA》《RawMetaDiff》《Learning Effective Sign Features》 |
| 主结果 | 先给结论句，再给具体数字（绝对值 + 增量） | "+11.4 AP"《Boosting VLM CDIOD》、"37.30% vs 74.05%"《OACIR》 |
| 消融 | 累加式（Baseline → +A → +B）或减法式（w/o A）；变体名与方法小节的模块名一致；顺序与引言挑战顺序一致 | 《PPCL》《MARCO》《MatAnyone2》《PiLoT》 |
| 机制实验 | 至少一处实验回答"为什么有效"，直接验证洞察本身 | 《LoftUp》Fig.8、《Dissecting GCD》5.4、《The Devil Is in Gradient Entanglement》 |
| 排除替代解释 | 参数量、训练时长、数据规模、外部先验等混淆因素各配一个对照 | 《Structure Matters》《DiverseGRPO》《No Calibration, No Depth, No Problem》 |
| 不利结果 | 不主动示弱，不说输。按 `references/anti_defensive.md` §3 的顺序处理：删 → 收缩主张 → 换口径 → 解释为取舍 → 重组实验 → 重构故事 → 最后才用一句事实性的话说明。表格数字照实，文字主张不越过表格 | 解释为取舍或换口径：《Radiance Meshes》《M3DLayout》《AT-VLA》；写法见 §3.8 |
| 数字一致 | 同一数字在摘要、引言、贡献、正文、表格、结论中写法一致 | 反例《AsymLoc》95% / 95.5% / 96% |
| 统计 | 只有做过显著性检验才写 significant；能报方差就报 | 早期规范；《FedHarmony》Wilcoxon、《D-Convexity》10 次配对 t-test |
| 表图 caption | 单独看得懂：比较了什么、指标方向（↑/↓）、最优标注方式 | 早期规范 |

---

## 1. 这一章要完成什么，与其他章节的分工

### 1.1 这一章的任务

实验章要把引言里的每一条论断**逐条兑现**。读者（审稿人）读这一章时会拿着贡献列表逐条核对。它需要回答四类问题：

1. **是否更好**：在公认的数据集、指标和强基线上，结果如何（主结果）。
2. **每个设计是否必要**：去掉或替换某个模块会怎样（消融）。
3. **为什么有效**：增益来自哪里，洞察本身是否成立（机制分析）。
4. **是否可信、适用范围多大**：提升是否来自不公平因素，泛化、效率如何（排除替代解释、鲁棒性）。

《NuWa》把这四类问题压成三段式："主结果证明有效 + 机理分析证明可信 + 消融证明每个设计都必要"。《LoftUp》的分工最清楚：5.1 回答整体是否更强，Tab.1/Fig.5/Fig.7 回答训练目标本身是否有效、能否迁移，Tab.4 回答架构本身是否更优，Tab.5 回答分辨率泛化，Tab.6 回答效率代价，Fig.8 的注意力可视化回答"为什么有效"，从"是否好"一层层推进到"为什么好"。

语料统计（`references/corpus_stats.md`，贡献类型组合）也说明了为什么四类证据都需要：1040 篇中，贡献里含 Performance 的有 955 篇（91.8%），含 Capability 的有 823 篇（79.1%），含 Insight 的有 674 篇（64.8%）。也就是说，**大约三分之二的论文声称提供了洞察**，这类论文只靠主表和消融是不够的，必须有直接验证洞察的机制实验。

### 1.2 与其他章节的分工

| 章节 | 分工与接口 |
|---|---|
| 引言 / 贡献列表 | 贡献列表定义了实验要兑现的清单。74.4% 的论文用 bullet 列贡献（`references/corpus_stats.md`），实验小节应能逐条对上。引言里提出的 RQ、"How to...?" 问句、挑战编号，实验里原样复用（《AdvDreamer》三段 "How to...?" ↔ ❶❷❸ 三个模块 ↔ RQ1–RQ3）。 |
| 方法 | 方法按问题驱动的求解链写，每个小节解决上一节遗留的问题（story_types §3.4）。实验的消融应沿着这条链逐环验证：变体名复用方法小节的模块名（《AT-VLA》Ex1 "With Adaptive Cross Attention"）。方法正文不预告消融（不写 "ablated in Sec. 4.3"，见 `references/workflow.md` 第 3 节），对应关系由实验这一侧建立。方法里提出的假设在实验中要有对应的消融（《Spherical Leech Quantization》Table 8 对应 Sec. 3.3 的假设）。 |
| 相关工作 | 基线按相关工作的分类分组，并在实验里点名回指（《D4RT》"4.2 对比 3.2 中的方法，4.3 对比 3.1 中的方法"；《RawMetaDiff》single-frame / generative / dual-frame 三组）。 |
| 摘要 / 结论 | 实验中的核心数字是摘要、引言、贡献、结论引用的唯一来源，四处必须一致（story_types §3.7）。结论里的主张不越过实验表格：不是第一的地方收缩主张，也不在结论里专门写一句输了（`references/anti_defensive.md` §3）。 |
| 局限 | 局限最多 2 条，每条写成"适用边界 + 方向"，放在结论之前的 Limitations 段或结论中间（`references/anti_defensive.md` §5）。实验里的不利结果按 §3.8 处理，不搬进局限。顶会论文多数不设独立 Limitations 小节，本 skill 的做法是最多 2 条、简短。具体写法见 references/sections/conclusion.md。 |
| 补充材料 | 可以放额外数据集、超参细节、更多可视化；失败案例和次要结果放这里即可；**不能**把某条贡献的唯一验证整体推过去（见 §4）。 |

---

## 2. 组织方式：常见结构及适用场景

### 2.1 默认骨架（四层递进）

```
4.1 Experimental Setup（Datasets / Baselines / Metrics / Implementation Details）
4.2 Main Results（与 SOTA 对比：定量表 + 定性图）
4.3 Ablation Study（逐组件；必要时再加设计选择对比、超参敏感性）
4.4 Analysis（机制分析 / 可视化 / 泛化 / 效率 / 鲁棒性，按需要取 1–3 项）
```

代表：《CARE》4.1→4.2→4.3；《CD-Buffer》4.1–4.5；《OSA》4.1–4.4；《GrOCE》5.2–5.6；《SEELE》4.2 整体效果 → 4.3 消融拆出 HP / CR 各自的加速倍数（2.8×、1.3×）和质量增量（0.23 dB / 0.03 dB PSNR）→ 4.4 超参数敏感性；《Wavelet-Driven》Table 1 主对比 → Table 2 真实数据泛化 → Table 3 模块消融 → Table 4–8 超参消融；《Backdoor Mitigation by D3》4.2 主结果 / 4.3 机制理解（t-SNE）/ 4.4 自适应攻击（主动设想最强反驳）/ 4.5 超参消融。

第 4 层按需要追加专门小节：诊断实验（《DUV-SLAM》4.3 Diagnostic）、应用展示（《WonderPlay》、《Video Motion Graphs》4.3 Applications）、防御评估、真实世界测试。失败案例小节可选，不作为默认推荐，通常放补充材料即可（正文单设的例子：《Clay-to-Stone》4.4 Qualitative Analysis and Failure Cases）。

### 2.2 四种组织手法（可叠加使用）

| 手法 | 做法 | 适用场景 | 例子 |
|---|---|---|---|
| RQ / 问题驱动 | 节首列出 Q1–Qn，每个小节回答一个 | 贡献 ≥3 条、实验类型多样；新问题定义型、数据与基准型 | 《VeriDou》RQ1–RQ5；《URICA》RQ1–RQ3 对应三条贡献；《SaPaVe》5 个 RQ；《Learning Effective Sign Features》Q1–Q6；《AbstainEQA》A–D |
| 问句小标题 | 小节标题直接写成问句 | 需要让审稿人一眼看到"这个实验证明什么" | 《MTU3D》"Does Vision-Language-Exploration Pre-training benefit navigation?"；Unsafe2Safe "Is Stage 1 reliable?"；《SENTINEL》"Is a large transformer necessary...?"；《Cleaning the Pool》"Does progressive filtering yield a higher-quality candidate pool?" |
| 方法-实验镜像 | 实验小节标题与方法小节标题一一对应 | 模块彼此独立、方法按模块组织；能力扩展型尤其常见 | 《Towards Generalized Multimodal Homography Estimation》4.2 "Training Data Synthesis" 与 3.2 完全一致；PET-DINO "3.2 AFVPG" ↔ "4.6 Table5"；《TokenSplat》4.2 按任务分小节 |
| 重复模板 | 多个任务，每个任务固定"数据集 → 指标与对比方法 → 结果"三段 | 一个方法覆盖多个任务 / 多个设定 | 《From Pairs to Sequences》五个小节重复同一模板；《LBM》6 个 image-to-image 任务，每个任务对应一类贡献 |

**RQ 加黑体结论句**：《AdvDreamer》每个 RQ 开头先给黑体 Take-away（如 "Emphatically not."）；数据集论文 Wanderland 每节开头先写 A1/A2/A3 加粗结论句再摆证据。审稿人扫读时只看这些句子就能拿到结论，推荐使用。

### 2.3 按故事类型的差异

先按 references/story_types.md 第 2 节确定主类型，再按下表调整实验侧重。

| 故事类型 | 实验顺序与侧重 | 特有的必备实验 | 例子 |
|---|---|---|---|
| 瓶颈突破型（56.0%） | 三层证据：主表（多数据集 × 多骨干 × 多指标）→ 逐组件消融（w/o 模块名）→ 验证洞察本身的机制实验 | 排除替代解释（参数量对照《OASIS》、"只是加了噪声"对照《SD-IF》Tab.7/8、Discussion 自问"提升是否只来自外部先验"《CAD》）；在对自己不利的设置下仍然胜出（"our evaluation setup is conservative"《LLSA》） | 《SD-IF》两个瓶颈、两个模块、两组排除性实验，三层闭环 |
| 新问题定义型（11.0%） | 先用与自身方法无关的诊断实验证明问题存在 → 方法有效 → 消融 | 一类质疑配一类证据（《IQA-Adapter》用 21 个 IQA 模型、GenEval、千人主观研究、参考图实验回应四类质疑）；拆开方法贡献与数据贡献（《OACIR》同一 SPRC 模型两个数据集训练，37.30% vs 74.05%）；自设劣势仍胜出（《CObL》对手用 oracle mask，自己不用）；反事实实验、人类基线、显著性检验 | 《4D-RGPT》一条贡献一张表；《PAVAS》问题当标题；《CounterPC》Table 2 按贡献顺序累加 |
| 统一框架型（10.8%） | 每条贡献一张表或一组消融；消融顺序复现引言挑战的列举顺序 | "统一"本身要有映射表、推导或实验证明（《CFG-Ctrl》Table 1 把前人方法映射进统一公式）；正反双向消融（"w/o Geometry vs. Joint Modeling"《GeoRelight》）；失败变体（《Optical Flow Matching》OFM-Naive EPE 在 15 以上）；显著性（《D-Convexity》10 次配对 t-test） | 《M2SFormer》Table 3/4；《PiLoT》按 "impossible triangle" 三维依次消融 |
| 发现-解释型（10.7%） | 主实验 → 归因 / 机制实验 → 鲁棒性或自适应攻击（《ARGUS》《D3》《BLiM》） | 从相关升级到因果：先观测再干预（《WSDT》Fig.3 → Fig.4）；用数字而不是"更高"（"0.613 vs 0.300"；《PCR》r=0.836）；跨底座复现（WSDT 在三个 SD 版本上）；至少一处干预或因果实验 | 实验小节标题复用贡献列表的措辞，让读者能对上号（引言里的贡献句不标章节号）；纯实证论文用 "Summary of findings"，每条括注对应图表（《Scaling Laws》） |
| 数据与基准型（7.0%） | **先证明数据可信**（人工核验一致性、R²）→ 证明基线或方法有效 → 消融 | 多条独立证据线（RDFace：landmark 相似度 + VLM 语义相似度 + 专家 Cohen's κ）；外部校准（PAI-Bench 用人类偏好 ELO 验证指标，Pearson r=0.918）；控制实验戳穿假提升（AbstainEQA 随机化视觉输入）；分层评测（零样本 → 迁移 / 微调 → 更难场景，NitroGen Fig.5–7） | GeoMMBench First/Second/Third 对应第 3/4/5 节；RealAppliance 5.2 用五个问句做小标题 |
| 能力扩展型（2.4%） | 方法-实验镜像；客观指标 + 用户研究 + 效率对比三重链（CoordSpeaker、FEAT） | 链式消融，每加一个模块给数字（FoleyDirector Tab.3：①Base → ②+STS → ③+RoPE → ④+Bi-Frame）；难量化的能力用定性图 + 视频补强（4D Primitive-Mâché） | HouseCrafter "3.2 Floorplan-guided..." ↔ "4.3 Ablation" |
| 效率优化型（2.0%） | 贡献逐条对应实验小节或消融表；消融表命名复用方法小节标题 | 速度、质量、内存、用户研究一起报（TurboVSR：DOVER + MUSIQ + user study + 4K 案例）；逐步消融复现构建过程（DeltaTok Step0→3）；效率单独成节兑现标题承诺（《Sparfels》Running Time 验证标题里的 "Fast"） | EDM Table 7 分 (a)(b)(c)(d) 对应四条贡献 |
| 理论分析型（0.2%，仅 2 篇） | 实验只用来验证理论，逐条对应贡献 | 覆盖面拉满并专挑强基线（《C²FG》五种骨架 × 四个数据集 × 两类采样器，专挑 "already difficult to improve" 的 SiT-XL/2 (REPA)）；用独立方法交叉验证（《PLMP》monodromy + Gröbner 基）；理论界要有"理论预测 vs 实测"对照（反例：《SADTR》《Stable Mean Flow》缺） | 《C²FG》Toy Example / Table 1 对应 "SOTA performance"，Table 3 对应 "versatility" |

---

## 3. 逐部分写法

### 3.1 节首路标句

**写什么**：1–3 句，说清本章要回答哪几个问题、分别在哪个小节。问题的数量和顺序与引言贡献列表一致（《PanoEnv》的三点预告与引言三条贡献一一对应）。

**怎么写**：
- 顺序式：先 Setup，再主结果，最后消融。
- 问题式：列出 (1)(2)(3) 或 Q1–Q3，适合贡献多样的论文。
- 定位式：把实验定位为某个洞察或贡献的实证支撑。

**句式模板**：
- "We first describe the experimental setups in Sec. 4.1. We then evaluate ... Finally, we ablate the key design choices ..."（《E-RayZer》）
- "After inspecting qualitative differences in capability in Sec. 4.1, we proceed with ... We conclude with a set of key ablations in Sec. 4.4."（《D4RT》）
- "In our experiments, we first compare our method to SotA baselines ... and then test the generalization capability ... In addition, we provide an ablation study"（《MoGA》）
- "In this section, we first present datasets used for multitask training (Sec. 4.1), followed by the implementation details (Sec. 4.2) ..."（《StreamFormer》）
- "This section starts with an overview of the datasets, comparison baselines, evaluation metrics, and implementation details."（《PRISM》）
- "Our experiments evaluate (1) the quality of ... (2) the zero-shot capability of ... (3) the effectiveness of ..."（《PanoEnv》）
- "We conduct experiments to answer the following research questions: (1) ... (2) ..."（ESSENTIAL；《Dissecting GCD》"we aim to answer the following questions. (1)…(4)…"）
- "We design experiments to study three key questions ... Q1) ... Q2) ... Q3)"（Enrich and Detect (ED-VTG)）
- "We address the following questions in our experiments: (1) ... (2) ... (3) ..."（《Guiding Diffusion-Based Articulated Object Generation》，三个问题直接对应三条贡献）
- "we articulate three research questions (RQ) to guide our experiments"（《URICA》）
- "We design our experiments to answer three key questions"（《Glove2Hand》）
- "We evaluate X across Y to answer Z primary questions."（《InfiniBench》："We evaluate InfiniBench to answer two primary questions"）
- "we assess MDS-VQA from three complementary angles: 1) ... 2) ... 3) ..."（《MDS-VQA》）
- "We conduct a comprehensive set of experiments to validate the three core contributions of UNIPIXIE."（《UniPixie》）
- "To validate the effectiveness of MEDIC-AD, we conduct a series of experiments corresponding to each stage of the proposed framework introduced in Sec. 3."（《MEDIC-AD》）
- "We evaluate the effectiveness and generalizability of CSaN ... as practical evidence for the joint game-decision insights underlying SaN"（《Selection-as-Nonlinearity》，把实验定位为理论洞察的实证支撑）
- "In this section, we conduct experiments ... to show its unique features regarding usability, diversity, efficiency, and extensibility."（《UnrealZoo》）
- "First, we apply ... Next, we show ... Also, we solve ... Lastly, we provide ..."（《Registration beyond Points》）

**注意**："In this section, we conduct a series of experiments to rigorously evaluate our proposed framework."（《SaPaVe》）、"We conduct a comprehensive set of experiments to systematically evaluate our proposed X."（《CausalVAD》）这类句子只能当第一句，后面必须跟具体问题清单，否则等于没说。预告顺序必须与实际顺序一致（反例：HumanNOVA 预告 Setup→Comparison→Ablation，实际是 Setup→Ablation→Comparison）。

### 3.2 实验设置（Setup / Implementation Details）

**写什么**：数据集（含划分）、评价指标、基线、实现细节。固定用小标题或加粗段首词分开，如《No Calibration, No Depth, No Problem》第 4 节的 Datasets / Baselines / Metrics / Implementation Details 四个子标题。

**(a) 数据集**
- 写清名称、规模、划分方式、是否为本文新建。本文新建的数据集要回指方法或数据章节："the production-sourced real-world HDR dataset that is introduced in Sec. 3.2"（《HDR-VLM》6.1 开篇）。
- 训练数据量是卖点时，在这里再报一次，与摘要呼应："We randomly sampled a training set of only 3-shot per dataset (18 images)"（《Dual-level Adapter》4.1）。
- 使用内部数据时，主动回应可复现性质疑（《D4RT》专设 "Training data" 段）。
- 句式："We evaluate our method on three popular optical flow benchmarks"（《MEMFOF》）；"We evaluate our method through continual learning tasks on five benchmark datasets"（《Mind the Gap》5.1）。

**(b) 评价指标**
- 沿用领域惯例时一句带过并引用："We follow prior HMR work and report standard pose and shape evaluation metrics"（《SAM 3D Body》7.1）。
- 新指标要**先直觉后公式**：先用一句话说明它衡量什么、为什么合理，再给定义，定义后再用自然语言复述含义（数据与基准型的做法："Intuitively, the router should place probability mass only on models that answer correctly..."，VL-RouterBench）。
- 每个指标注明方向（越高越好 / 越低越好），在表头用 ↑ / ↓ 标出。
- 缺 ground truth 只能做定性评估时，明说原因："Quantitative evaluation is not provided because of the lack of datasets containing pattern images with corresponding ground-truth distortions"（《Planar Affine Rectification》）。

**(c) 基线**（选取逻辑见 §3.6）
- 逐一介绍，或按类别分组介绍（《Consensus-Driven Active Model Selection》第 6 节单列 5 个 baseline；《DirectFisheye-GS》4.1 说明为何选 3DGS 原始版本、Fisheye-GS、3DGUT、Self-Cali-GS）。
- 写清每个基线的版本、是否由本文重新训练、超参数来源（早期规范）。

**(d) 实现细节**
- 必写：骨干 / 基座模型、关键超参、优化器与学习率、batch size、训练步数或时长、硬件。
- 写到可以照着复现的粒度，例子：
  - "rank=64, lr=5e-5, 600 steps"（《UnZipLoRA》）
  - 学习率 5×10⁻⁵、权重衰减 0.01（《Gastric-X》）
  - "8×H100 / DeepSpeed ZeRO-2 / 70K steps"（《Towards High-resolution Sketch Colorization》）
  - "Our SpecTemp framework consists of a 7B-parameter target MLLM and a 3B-parameter draft MLLM..."（《Thinking with Drafts》）
  - "We use the GroundingDINO-B model as the backbone"（《CountSE》）
  - λp=300, λk=0.1，稀疏率 0.3（《SAME》）；滑动窗口 V=16, s=4（《Geo4D》）；DCAT 层数 L=4 及损失权重（《CoMatch》）
  - 数据集采样比例、batch size、GPU 型号、训练时长（《VolumetricSMPL》）
  - 用了外部大模型时写出具体型号：DeepSeek-V3.2-Exp、Gemini-2.5Pro（《3DrawAgent》4.1）
  - 数据生成成本："we can generate both surfel and 3DGS maps for 600,000 scenes within 10 days"（《Mapping Priors》）
- 方法里有算法框时，超参在这里逐项落实（《ReMoT》4.1 Hyper-parameters 落实 Algorithm 1）。
- 用了显著性检验时，在这里写明检验方法（《Consensus vs. Controversy》第 5 节给分辨率、batch size、显著性检验方法）。
- 语气：平铺直叙，不需要过渡修辞（《VolumetricSMPL》《RALoc》4.1）。
- 句式："Our implementation strictly follows the experimental settings established in previous works"（《SparseWorld-TC》）；"For a fair comparison, we follow the identical evaluation pipeline with prior work [24]"（《Adaptive Dual Uncertainty》）。

### 3.3 主结果（Main Results / Comparison with SOTA）

**写什么**：主表（多数据集 × 多骨干 × 多指标）+ 定性对比图，回答"是否更好"。

**怎么写**：
1. **先给结论句，再给数字**。结论句的强度按 references/word_style.md 匹配实际排名：真实数据全面领先才写 SOTA，合成数据或部分领先写 competitive（《GPERT》）；"all metrics" 必须真是全部（反例：《SeeGroup》声称 all metrics，实际是 14/15）。
2. **数字写具体**：写 "reduces error by 15% (from 20.0 to 17.0)"，不写 "significantly outperforms"（早期规范）。同时给绝对值和增量，或给比值：
   - "+11.4 AP gain"（《Boosting VLM CDIOD》）；"82.57% vs 77.75%"（《SaE》）；"outperforms SOTA methods ... by up to 47.7%"（《Fine-VAD》）
   - "6.3× 加速、39.1% 模型缩减"（《SEELE》）；"仅 0.26% 可训练参数"（《DK-DDIL》）；"5.5ms vs MinusFace 68ms"、"6.86% absolute drop"（《LDP-Slicing》）
   - 写 "5:1" 这样的比值，不写 "significantly"（《SAM 3D》）
   - 用百分点报差值："improves by 10.54 and 7.85 percentage points"（RMIR）
   - 把误差换算成物理直觉：1.5 km 轨迹、3 cm 不确定度 → 0.002% 漂移，对比 ORB-SLAM3 的 0.6%（《Benchmarking Egocentric》）
3. **分段归因**：多个数据集时，逐个说明增益来自哪里，而不是只说"全面领先"（《Real-World Point Tracking》5.3 按 EgoPoints / RoboTAP / Kinetics / DAVIS 逐段归因）。
4. **数字后紧跟一句解释**：这个数字说明了什么、对应哪条贡献。
5. **定性图佐证定量**（DreamLayer Fig.8/9），图里指出具体看哪里。
6. **不利项按 §3.8 处理**：先收缩主张、换口径或解释为取舍，不单独写一句输了。

**句式模板**：
- "As shown in Tab. 1, our method achieves ..."（多篇通用）
- "As shown in Tab. X, our method achieves state-of-the-art results across all datasets ..."（《Diving into the Fusion of Monocular Priors》，只在确实全部领先时用）
- "As summarized in Table 1, X is the first method that is simultaneously ..."（《Find Any Part in 3D》，主表定位句）
- "Tab. 1 compares MVTracker against several baselines"（《Multi-View 3D Point Tracking》）
- "We evaluate X along two dimensions: (i) ...; and (ii) ..."（《Scalable Trajectory Generation》）
- "To validate the effectiveness of the proposed method, we conduct evaluations on three tasks."（《ReAttnCLIP》）
- "To fully validate the effectiveness of our proposed X, we conduct evaluations on pair-level tasks ..., and sequence-level tasks ..."（《From Pairs to Sequences》）
- "To demonstrate the effectiveness of our approach, we conduct quantitative evaluations ..."（《SenCache》）
- "We at first conduct a quantitative evaluation ..."（MaterialMVP 4.1）
- "Building upon the validation of high-fidelity image generation, we next assess ..."（《TRIDENT》4.2，把验证层级从"像不像"推进到"对不对"）
- "We do not aim for a state-of-the-art captioning model for each dataset."（《CaptionSmiths》4.1，主动声明目标，管理预期）

### 3.4 消融实验（Ablation Study）

**写什么**：证明每个设计都必要，且与 Method 中的设计选择一一对应。

**(a) 开头句：先给动机，再说怎么消融**
- "To verify the contribution of each proposed component, we conduct component-wise ablation experiments."（《E2EGS》）
- "To assess the contribution of each component in our training pipeline"（《CURE》）
- "In this section, we perform multiple ablations to assess the impact of our design choices."（《ResidualViT》）
- "Comprehensive ablation studies are performed to analyze the effectiveness of our proposed mechanisms."（《SFP》）
- "We divide our method into two modules to analyze their individual contributions."（《Energy-GS》）
- "Since the generative avatar prior is the key to our method, we focus on ablations that evaluate its effectiveness."（《MoGA》4.3）
- "To show the importance of our formulation for X, we first implement a baseline model ..."（《FlowR》）
- "To validate the design of our temporally-hard negative (Sec. 3.2), we conduct an ablation study in Tab. 3."（《SEASON》，点名回指方法小节）
- "To verify the sampling–alignment hypothesis that underlies CROWn:"（《CROWn》，把消融写成假设检验）
- "Table 4 presents a comprehensive analysis on the design of VideoITG, directly supporting our key contributions."（《VideoITG》）

**(b) 四种消融结构**

| 结构 | 写法 | 适用 | 例子 |
|---|---|---|---|
| 累加式 | Baseline → +A → +B → Full，每行给数字 | 模块按求解链逐步叠加；想展示"贡献累加曲线" | 《PPCL》Baseline→+LP-a→+LP→+LP-b→+DP→+WP-text→+WP-ffn→+Fine-tuning；《MARCO》41.8→49.6→52.5→64.7→67.5；《LVFace》MR-All 97.27%→98.49%；《CADC》M0→M3；DisenQ Table 3 |
| 减法式 | Full → w/o A → w/o B | 模块彼此独立，要证明缺一不可 | 《MatAnyone2》Table 3 (a)→(d)；《STAC》逐一移除 AC/SC/CB/CO |
| 设计选择对比 | 同一位置换成替代方案 | 不仅问"有没有用"，还问"是不是最优" | 《HamiPose》"Keypointwise Gating vs Unified Gating""Hamiltonian Optimization vs Conventional Solvers"；《Multi-View 3D Point Tracking》kNN vs triplane |
| 正交 / 分组消融 | 两个因素交叉，或按贡献分 (a)(b)(c)(d) 组 | 贡献包含多个独立维度 | 《RiskProp》三种标注策略 × 两个损失；EDM 按 (a)(b)(c)(d) 四组对应四条贡献；《Cov2Pose》Table 5 (A)(B)(C) 对应三个设计点 |

之后可以加超参敏感性（《SEELE》4.4；《Wavelet-Driven》Table 4–8）。

**(c) 写作规则**
- **变体名与方法模块名一致**，用"w/o 模块名"或"+模块名"命名；取名规则见 references/naming.md。变体用统一字母或编号标注，方便正文交叉引用（《FEAT》(a)–(f)；《AT-VLA》Ex0–Ex4）。
- **消融顺序与引言挑战、方法小节顺序一致**（《PiLoT》按 "impossible triangle" 三维依次消融）。
- **颗粒度一致**：贡献条目、方法小节、消融行三者一一对应。反例：《CSL》合并成一条贡献、消融拆成三项；《STAC》三条贡献对应四个组件；FoleyDirector 把 3 个组件压成 1 条贡献。
- **逐行给数字并解释**：每个组件带来多少增益（"+0.2 AP 来自 CIM，+1.5 AP 来自 GNN"《CIGPose》）。
- **降幅措辞与数字相符**：51.0→45.7 不能写 "minimal"（反例《FlexMem》）。
- **异常现象要讨论**：性能饱和、拐点、组合反而更差，都要给解释或列为边界（反例：《Keep It Frozen》RMB 超过 12 层性能饱和未讨论；《Premier》线性组合反而更差但未提适用边界）。
- **"失败的替代方案"是正面证据**：用消融证伪一个看似合理的直觉方案，反过来证明方法的必要性（《Diffusion-Based Native Adversarial Synthesis》；《Energy-GS》Figure 6(a)(b)(c) 与 Figure 7 的 "multi-shell" 现象，展示只做梯度流重设不做能量对齐会陷入局部极小）。

**句式模板**：
- "From Rows Ex0–Ex4 in Tab. 3, we verify the contribution of each proposed component across four contact-rich tasks"（《AT-VLA》）
- "As illustrated in Tab. 4, it is necessary to introduce ENS ..."（《ANTS》）
- "Ablation experiments were performed to assess the contribution of each proposed module."（《U²Flow》）
- "To evaluate the impact of each component"（GOR-IS）

### 3.5 机制分析与可视化

**写什么**：回答"为什么有效"，直接验证引言里的洞察，而不是再报一遍数字。部分论文消融充分但止步于"数字更好"，没有解释机制（CoopTrack、Height-Fidelity），这是常见短板。

**怎么写**：
- **闭环式**：用引言定义的诊断指标，走"提出问题 → 量化 → 解决 → 再验证"的闭环。《The Devil Is in Gradient Entanglement》用 GDC/SOC 指标完成这个闭环，被笔记认为是说服力最强的一节。
- **多角度解释增益来源**：《Dissecting GCD》5.4 用信息论（von Neumann 熵）、t-SNE 可视化、类别数估计三个角度解释"增益从哪来"。
- **可视化呼应方法动机**：《MetaScope》5.4 的定性分析呼应方法部分的物理动机；《LoftUp》Fig.8 注意力可视化；DiffPS 的 timestep 消融（Fig.5）呼应方法部分的性质分析。
- **层级递进**：VRM 按"性能验证 → 机制验证 → 可视化验证"对应三条贡献。
- **常用工具**：t-SNE、注意力图、频谱、oracle 实验、干预实验（story_types §3.5）。发现-解释型要从相关升级到因果，先观测再干预（《WSDT》Fig.3 → Fig.4；《ReME》用 GT 参考集做 oracle）。
- **副作用检查**：验证提升没有以牺牲其他能力为代价（《Thinking in Uncertainty》用 GPT-5 评估文本质量，检查降低幻觉是否牺牲流畅度；Same or Not? 用通用 VQA 和纯文本基准排除"对齐税"）。

**句式模板**：
- "To assess how a model's region of interest influences OOD detection ..."（《The Invisible Gorilla Effect》4.1）
- "To validate that LLSA effectively reduces computational complexity, we train Pixel DiTs ..."（《Trainable Log-linear Sparse Attention》5.1）

### 3.6 基线选取与排除替代解释

**写什么**：说明对比公平，并主动排除"提升其实来自别处"的解释。

**(a) 基线选取**
- 与相关工作的分类呼应（《HiLoRA》Baselines 列出的 9 个基线直接对应引言第 3 段提到的方法类别）。
- **声明比较范围**，预防"为何不比某方法"："For fair comparison, we only include gloss-free SLT methods that do not leverage any external sign language datasets for pretraining."（《Learning Effective Sign Features》）
- 无法对比的方法说明原因："[56,107] did not release source code, preventing us from including such an experiment"（《Triplet-Based Compression》脚注）；"it is difficult to compare methods using the exact same training data and methodology due to prohibitive data usage licenses, unclear descriptions of training data, and lack of training code"（《SAM 3D Body》）。
- **无同类工作时自建基线**并说明："As our system is entirely novel, with no existing open-source methods available for direct comparison ..."（《Video Motion Graphs》）；《Vanast》构造 16 种两阶段基线组合；《MIORe》自建最大改造版本 baseline；《CHTR》Table 4 专门说明 baseline modification。
- **与更强条件的基线比**：《Missing No More》与 10 个需要真实 IR 输入的 SOTA 比，验证无 IR 时依然可用；《CObL》的对手用 oracle mask。
- 统一协议：所有基线在同一数据集重新训练（《CineScene》）；复现前作实验协议（《Outlier-Aware PTQ》4.1）。
- 句式："To ensure a fair comparison"（《UNCHA》）。

**(b) 排除替代解释**：每一个审稿人可能提出的混淆因素，配一个对照实验。

| 可能的质疑 | 对照做法 | 例子 |
|---|---|---|
| 只是参数变多 | 参数量对齐的对照 | 《Structure Matters》4.5；《OASIS》 |
| 只是训练更久 | 相同训练预算对比 | 《DiverseGRPO》Discussion |
| 只是数据更多 / 数据更好 | 同一模型换数据训练，或同数据同 backbone 对比 | 《Scaling Language-Free》Question 2 用 ImageNet 对照；《OACIR》37.30% vs 74.05%；《ROSE》"相同数据、相同 backbone" |
| 增益来自某个外部组件 | 反事实实验，剥离该组件 | 《No Calibration, No Depth, No Problem》Pre-GS Comparison 排除 3DGS 带来的增益；《CAD》Discussion 自问是否只来自外部先验 |
| 只是加了噪声 / 正则 | 对应的朴素对照 | 《SD-IF》Tab.7/8 |
| 依赖特定大模型 / 架构 | 换底座复现 | 《FedTSP》对比 GPT-4o / Claude / Gemini / LLaMA3；WSDT 三个 SD 版本；《SuP》把 DSAM 接到 GeoTransformer / PEAL / ColorPCR |
| 只是过拟合某个数据集 | 跨域 / 跨数据集泛化 | 《SMoEStereo》4.2.1 Cross-domain + 4.2.2 Joint Generalization |
| 扩大规模牺牲了小场景 | 专门在小设定上测 | 《Long-LRM》"Low-resolution, sparse-view reconstruction" |
| 大模型是否必要 | 针对性对照 | DexVLG 6.3.2 针对 MultiGraspLLM；《SENTINEL》"Is a large transformer necessary...?" |
| 两个效应混在一起 | 设计协议把它们拆开 | 《Is Tracking really more challenging...》用同步双视角协议 (SOPE) 拆开视角效应与域效应；《Retrieve and Segment》Fig.6 closed-set 对比排除"offline 训练"混淆 |
| 某组件本身的贡献不清楚 | 三方比较 | 《Knowledge Distillation for LIC》4.3 teacher / vanilla / KDIC 三方比较剥离蒸馏本身的贡献 |
| 提升是假的 | 控制实验戳穿 | AbstainEQA 随机化视觉输入，证明 SFT 的提升是假的 |
| 方法对手太弱 | 自适应攻击 / 最强反驳 | 《Backdoor Mitigation by D3》4.4 |

**超参公平性**：只在一个数据集上调参，再 "uniformly set" 给所有基线和数据集时，要讨论迁移风险（反例：《The Devil Is in Gradient Entanglement》未讨论）。

### 3.7 泛化、鲁棒性与效率

- **泛化**：跨数据集、跨架构、跨输入设定（《SinGeo》5.4 跨架构泛化；《RnG》4.3.2 泛化到任意输入视角数；《ReAttnCLIP》plug-and-play 泛化；《HG-Lane》4.4 对 CLRNet 加入 / 不加入生成数据前后对比）。
- **效率**：贡献里提到"高效""轻量""simple yet effective"或标题里有 "Fast"，就必须有 FLOPs / 延迟 / 内存数字（《Few-Shot Pattern Detection》FLOPs 3.04T vs 5.08T / 4.72T；《Sparfels》Running Time 单独成节；《ViterbiPlanNet》Parameter / Sample Efficiency）。反例：《Missing No More》贡献 3 声称低开销，全文无 FLOPs 数据。
- **量化代价**："each additional retrospective stage adds about 0.07 G FLOPs and 0.03 s of latency"（《Recover to Predict》）。代价数字照实进表；代价小时，可以把它写成优势（开销低）。
- **人工成本可以量化**：《CountSE》标注每张图的耗时 "11.1s" / "0.7s"。
- **鲁棒性和效率实验要写进贡献列表**，否则就是"锦上添花"（反例：《CoST》4.6 / 4.7 鲁棒性与推理速度不在贡献列表；《UniDxMD》4.5 节、《DataTailor》4.3 节）。

### 3.8 不利结果与失败案例

**原则**：不主动示弱，不说输。实验不是结果仓库，每个实验都要承担论证职责（`references/anti_defensive.md` §6）。遇到对本文不利的结果，按 `anti_defensive.md` §3 的顺序处理，能在前一步解决就不走到后一步；只有无法回避、并且确实影响核心结论时，才用一句事实性的话说明。

**底线**：
- 表格和数字照实，不删改、不挑选对自己有利的子集；领域公认的主指标照常报告。
- 文字里的主张不越过表格：本方法不是第一的格子，不在文字里声称领先（反例：《SeeGroup》声称 "all metrics"，实际是 14/15），也不需要专门写一句"我们在这里不如 X"。
- 不编造解释：让步句里的"语境"必须是真的机制解释或真实的设计取舍，不是借口。把负面结果一律用 "This suggests that..." 正面带过（《ProGait》步态分类准确率 37%–45%、双视角融合反而降准）会削弱可信度。

**处理顺序在实验章里的写法**：

1. **删除或移到补充材料**：与核心主张无关的不利设置、次要数据集，不进正文主线。
2. **收缩主张**：把 "outperforms all methods" 收缩为实际范围。
   - "with the sole exception of D3 still outperforming AsymLoc by 0.1% on Scannet@20°"（《AsymLoc》）
   - "ranking second ... delivering a close runner-up performance"（《Sequential keypoint density estimator》）
   - 用中性的比较措辞：comparable to / competitive with / on par with / within 0.3 points of（`anti_defensive.md` §4）
3. **换评价口径**：换成更能体现本文价值的维度，前提是新口径确实是本文的目标（`anti_defensive.md` §2 第 3 条）。
   - "While 3DGS achieves higher quality, it suffers from popping artifacts ..."（《Radiance Meshes》，把比较落到一致性这一本文目标上）
   - "We do not aim for a state-of-the-art captioning model for each dataset."（《CaptionSmiths》4.1，主动声明目标）
4. **解释为目标差异或合理取舍**（只在属实时用）：
   - 《M3DLayout》把 FID 的差距解释为目标差异，再转正面："This is primarily because ... whereas our method generates scenes with more than 12 objects ..."
   - "EDM's significant relative efficiency advantage declines moderately with increasing image resolution ... However, semi-dense matchers generally achieve optimal performance without requiring extremely high resolutions."（EDM）
   - 《AT-VLA》Unscrew Lid 任务：基线在理想抓取姿态下测试，本文设定下抓取可能打滑，差距来自测试条件，给出具体机制
   - "due to the trade-off between distortion in different areas, ..."（《PriOr-Flow》，把差距落到取舍上）
5. **重组实验**：让优势成为表格、图和正文叙述的中心，次要结果移到补充材料。
6. **直接说明**（最后一步）：一句事实，不加情绪化修饰；归因没有实验支撑时用 likely / might / We hypothesize，不要写成定论（"a slight decrease is observed ... might be due to ..."《StolenLoRA》；"We hypothesize that ..."《Stochastic Gradient Estimation》）。

**消融里的非单调现象**：饱和、拐点、组合反而更差，给一句机制解释即可（"A possible explanation is that overly distant frames introduce noisy or less relevant motion, outweighing the benefits of a longer context."《TeFlow》）。

**失败案例（可选，不作为默认推荐）**：需要时放补充材料即可，正文不必单设小节。写法：具体输入 / 场景 + 错成什么样 + 机制归因，最好配图并指到子图。可参考的写法（原文多在正文，照搬时放补充材料）：
- 《2D-LFM》4.4 "Failure cases: monocular depth ambiguity"："limbs may flip in depth, extreme foreshortening can shorten limbs, and occluded landmarks may collapse"
- 《Clay-to-Stone》4.4："a flip-top bottle cap is misclassified as a slide cap"
- 《Retrieve and Segment》："RNS incorrectly segments part of an orange towel as a swimsuit, likely due to insufficient contextual information..."
- 《UniPart》："For inputs with high structural complexity, our joint generation of geometry and segmentation may fail..."
- 《Find Any Part in 3D》5.2.4 "Failure Modes"：微波炉被 voxel 下采样误分割
- 《Combinative Matching》把失败模式对应到 Fig.9 具体子图并给改进建议；《PR-MaGIC》4.4 配 Fig.7 给四类失败场景
- 《Vector Prism》5.3 用具体反例说明边界（闪电被定义为单个原子级 `<path>`，无法响应 "shatter into pieces"）

**与局限的关系**：局限最多 2 条，写成"适用边界 + 方向"，见 `references/sections/conclusion.md` §3.4；实验里的不利结果不搬进局限，也不在结论里重新提起已经收缩掉的比较。

### 3.9 数字、表格与图

- **数字来源**：只用结果文件或用户提供的数据，与表格逐一核对。缺数字时留占位符，不补、不估、不四舍五入改口径。
- **一致性**：同一数字在正文、表格、摘要、引言、贡献、结论中写法一致（小数位、单位、百分数还是百分点）。正面例子：《HG-Lane》19.75% / 8.63% / 38.8% 三处一致；《ForeAct》结论复现 "87.4%、0.33s"；《CURE》复现 "+0.35 IoU, 18.6%"；《Event-based VDM》1.6× / 18.9%。反面例子：《AsymLoc》结论 "保留超过 96%"、摘要 "up to 95%"、贡献 "95.5% / 93%"；《Counterfactual VLA》摘要 20.5%、正文 14.7%。
- **caption 单独可读**：看完 caption 就知道比较了什么、在什么设定下、指标越高越好还是越低越好（↑/↓）、最优和次优如何标注（加粗 / 下划线），全文统一。
- **表的分工写在正文**：每张表对应一个问题。《ResidualViT》：Table 1 回答每个架构组件贡献多少，Figure 4 回答 interleave factor 如何权衡精度和成本。
- **方差与显著性**：笔记指出多数论文数字对比多、很少讨论方差或统计显著性。能多次运行就报均值 ± 标准差；只有做过检验才写 significant，并写出检验方法（《FedHarmony》Wilcoxon；《D-Convexity》10 次配对 t-test）。
- **定性图**：与定量结果配对出现，图中标出应看的区域；难以量化的能力可以提示读者看补充视频（4D Primitive-Mâché）。

### 3.10 小节之间的过渡

- 从主结果到消融、从消融到机制分析，都要有一句显式过渡，交代"上一节证明了什么，这一节要回答什么"。反例：《MOFA-VTON》仅靠标题切换。
- 方法章到实验章也需要衔接。反例：《Dataset Distillation via VLM》4.1 直接用 "We evaluate our method on ..." 独立起头。
- 过渡句可以复用"已验证 X，接下来验证 Y"的结构："Building upon the validation of high-fidelity image generation, we next assess ..."（《TRIDENT》）。

---

## 4. 常见问题与反例

| # | 问题 | 反例 | 改法 |
|---|---|---|---|
| 1 | 贡献没有对应实验 | 《MeshFlow》贡献 3 无对应小节；《Missing No More》声称低开销但无 FLOPs；《Fed-ADE》理论部分无经验 regret 曲线；《Scalable Dual Fingerprinting》贡献 2 的效率声明无量化；《Heuristic Self-Paced Learning》贡献 1 无单一对应实验 | 写完贡献列表后逐条找对应的表 / 图 / 小节，找不到就补实验或删改贡献 |
| 2 | 数据集、理论界、"首个框架"类贡献没有独立验证 | 《Ditto-1M》数据集质量无独立定量实验；《UltraFlux》只做静态统计；《Stable Mean Flow》误差上界无数值验证；《SADTR》缺"理论预测 vs 实测"；DiffPS 首创性只靠文献对比；《UniPhys》数据集没做质量评测；《CFG-Ctrl》"统一"本身没被量化 | 数据集做人工核验 / 下游收益；理论界画预测与实测对照；"统一"给映射表或对照实验 |
| 3 | 核心卖点缺受控消融，只能从横向对比推断因果 | 《SparseWorld-TC》"去 BEV / 去 token" | 为卖点单独设计 w/o 或替换实验 |
| 4 | 贡献的唯一验证被推到附录 | 《SliderEdit》贡献 2（PPS loss）；3DReflecNet 声称五项任务，两项推迟到补充材料；《Diving into Monocular Priors》《CorrCLIP》多处 "detailed in the supplementary" | 每条贡献至少在正文有一张表或一段结论；附录只放补充细节 |
| 5 | 实验超出贡献列表（锦上添花） | 《CoST》4.6 / 4.7；《HDW-SR》β 灵敏度消融不对应任何贡献；《UniDxMD》4.5、《DataTailor》4.3 | 要么写进贡献，要么降为分析小节并说明目的 |
| 6 | 引言强调的效果没有定量实验 | 《Radiant Foam》光线追踪反射 / 折射只有定性图；《VeilGen》只有定性图；《DropletVideo》缺与 SOTA 的定量表 | 至少补一组定量对比；无 GT 时说明原因（《Planar Affine Rectification》） |
| 7 | 贡献条数与实验对不上 | MV-Fashion 5 条贡献只有 3 个实验小节；MEDIC-AD 贡献按框架 / 机制 / 评测横切，RQ 按能力纵切，只部分对应 | 按贡献顺序重排实验小节 |
| 8 | 措辞强于数字 | 《SeeGroup》"all metrics" 实为 14/15；《FlexMem》51.0→45.7 写成 "minimal"；《CAC》声称 "embodied AI" 超出实验范围 | 按 references/word_style.md 调整强度，写出实际比例 |
| 9 | 数字口径不一致 | 《AsymLoc》95% / 95.5% / 96%；《Counterfactual VLA》20.5% vs 14.7% | 定稿前全文搜索每个核心数字 |
| 10 | 在文字里专门说输，或把不占优的指标设成主战场 | "our method still lags far behind X on Y"、"unfortunately, ..."（`references/anti_defensive.md` §4 列出的自我削弱写法） | 按 §3.8 的顺序处理：收缩主张、换口径、解释为取舍，次要结果移到补充材料；表格数字照实 |
| 11 | 消融中的异常只报数字 | 《Keep It Frozen》PSN 参数占比、RMB 超 12 层饱和；《Premier》线性组合更差 | 每个非单调现象给一句解释或列为边界 |
| 12 | 消融止步于"数字更好" | CoopTrack、Height-Fidelity | 加一组机制实验（§3.5） |
| 13 | 小节之间无过渡 | 《MOFA-VTON》；《BiPreManip》方法与实验之间无过渡；《Dataset Distillation via VLM》《Derm1M》4.1 生硬起头 | 每个小节首句交代它回答的问题（§3.10） |
| 14 | 超参只在一个数据集调好就统一使用 | 《The Devil Is in Gradient Entanglement》 | 说明调参来源，或补敏感性实验 |
| 15 | 预告顺序与实际顺序不一致 | HumanNOVA | 写完后回头改路标句 |

---

## 5. 写作步骤与检查清单

### 5.1 写作步骤

1. **列对应表**。从引言拿到贡献列表（和 RQ / 挑战编号），从方法拿到小节与模块名，从用户的结果文件拿到所有表格。做一张"贡献 i ↔ 方法 3.i ↔ 实验小节 / 表 i"的对应表；有贡献找不到实验，先告诉用户，不要硬写。
2. **确定故事类型**，按 §2.3 决定实验顺序和必备实验（例如数据与基准型先证明数据可信）。
3. **列质疑清单**。站在审稿人角度写出 3–5 个"提升是否只是因为……"的问题，在用户已有实验里找对照（§3.6 表格）；缺的列给用户，建议补做。
4. **定骨架和小节标题**：默认四层（§2.1），选用 RQ / 问句标题 / 方法-实验镜像 / 重复模板（§2.2）。
5. **写 Setup**：数据集（含划分）→ 指标（新指标先直觉后公式）→ 基线（分组、版本、是否重训、比较范围）→ 实现细节（骨干、超参、硬件、时长）。
6. **写主结果**：结论句 → 具体数字（绝对值 + 增量）→ 逐数据集归因 → 定性图 → 不利项按 §3.8 处理。
7. **写消融**：动机开头句 → 按方法顺序逐行给数字 → 解释每行 → 讨论异常。
8. **写机制分析、泛化、效率**：每个小节首句写它回答的问题。
9. **（可选）失败案例**：需要时放补充材料，写具体场景 + 错误表现 + 机制归因。
10. **最后写节首路标句**，确保与实际小节顺序一致；补齐小节之间的过渡句。
11. **回填其他章节**：把最终数字同步给摘要、引言、贡献、结论；确认结论里的主张不越过实验表格。

### 5.2 检查清单

**对应关系**
- [ ] 每条贡献至少对应一个实验小节或一张表，能在正文找到，不只在附录
- [ ] 贡献、方法小节、消融行三者颗粒度一致；消融变体名与方法模块名一致（取名见 references/naming.md）
- [ ] 消融顺序与引言挑战、方法小节顺序一致
- [ ] 数据集、理论界、"首个框架"、"统一"、"高效"类贡献都有独立验证
- [ ] 鲁棒性、效率等额外实验已写进贡献列表，或明确标为分析
- [ ] 路标句预告的顺序与实际顺序一致

**证据层次**
- [ ] 有主表（多数据集 / 多骨干 / 多指标，按论文实际情况）
- [ ] 有逐组件消融，并给出每个组件的增量
- [ ] 至少一处实验直接验证洞察本身（机制实验），不止于"数字更好"
- [ ] 最可能的替代解释（参数量、训练时长、数据、外部组件）已被对照实验排除
- [ ] 按故事类型补齐必备实验（§2.3）

**可复现**
- [ ] 数据集含划分；指标注明方向；新指标先直觉后公式
- [ ] 基线写明版本、是否重训、超参来源、比较范围和未比较的原因
- [ ] 实现细节含骨干、关键超参、学习率、batch size、步数 / 时长、硬件

**数字与表图**
- [ ] 所有数字来自用户结果文件，与表格逐一核对；缺失处留了占位符并已告知用户
- [ ] 核心数字在摘要、引言、贡献、正文、结论中写法一致
- [ ] 没有无检验的 significant；措辞强度与实际排名相符（见 references/word_style.md）
- [ ] 降幅、代价的措辞与数字相符
- [ ] caption 单独可读，标明指标方向和最优标注方式，全文统一
- [ ] 每张表 / 图在正文被引用，并说明它回答什么问题

**不利结果与底线**
- [ ] 表格和数字照实，领域公认的主指标照常报告；文字主张不越过表格，不是第一的地方收缩了主张
- [ ] 不利结果按 §3.8（`references/anti_defensive.md` §3）的顺序处理，没有专门写一句输了，没有自我削弱词
- [ ] 解释为目标差异或取舍时，解释属实；无实验支撑的归因用了 likely / We hypothesize
- [ ] 消融中的饱和、拐点、非单调现象都有讨论

**行文**
- [ ] 节首有路标句；每个小节首句交代它回答的问题
- [ ] 主结果与消融、消融与分析之间有显式过渡句
- [ ] Setup 平铺直叙，没有空泛的修辞句
