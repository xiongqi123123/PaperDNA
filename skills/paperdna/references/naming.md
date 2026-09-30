# 顶会论文取名指南

**用途**：写论文的 AI 助手在拟标题、起方法名、写副标题、给子模块/数据集/现象命名、在摘要和引言里首次引入名字时，按本文执行。本文是取名的唯一来源，摘要、引言、句式库、叙事类型、用词风格几份规范里的取名问题都以本文为准。
**证据来源**：CVPR 2026 best/highlight + ICCV 2025 best/highlight/oral，共 1040 篇论文的标题与精读笔记。标题结构占比来自 4 批标题的分批归纳（各批数值不同，用区间表示，各类区间相加会超过 100%）；故事类型、摘要句数等数字来自 1040 篇的精确统计（`references/corpus_stats.md`）；标 **[重算]** 的数字是按同一批笔记的摘要逐句分析原句重新统计的。其余补充样本合并自摘要、引言、句式库、叙事类型、用词风格五份规范原有的取名章节（同样出自这 1040 篇的分批归纳）。
**使用约定**：文中 `X` 指方法名，`[...]` 指待填槽位。凡标"演示"的内容是为了说明流程而虚构的例子，不能当作证据引用。

---

## 0. 总纲：顶会的取名品味（先读这一节）

下面 9 条是从 1040 个标题里归纳出来的共同偏好，后面各节都是它们的具体展开。

1. **能不造名就不造名。** 单一贡献、理论分析、物理/几何类工作，顶档论文敢直接用描述式标题。
   - *Native and Compact Structured Latents for 3D Generation*（CVPR 2026 best）
   - *Spatially-Varying Autofocus*（ICCV best，无冒号、无方法名）
   - *Rectifying Magnitude Neglect in Linear Attention*
   - best/oral 档里"方法名: 副标题"的占比常略低于 highlight 档，highlight 档更依赖一个缩写把贡献点标出来。
2. **名字要表达论点。** 好的 backronym 本身就是一个英文单词，词义和卖点对得上：AIM（Amending Inherent Interpretability via Self-Supervised Masking，主题是可解释性）、CURE（医疗报告生成，寓意"治愈"）、DisCoRD（正文直接说破 "discord"，对应离散/连续之间的张力）。
3. **不要硬凑缩写。** 从单词中间抠字母凑成的名字属于公认的反面例子：ESSENTIAL（要从 integrAtion、Incremental 里各抠一个字母）、CHROME（从 consistEncy 里抠 E）、EXOTIC、MAGICIAN、GenErase、SAC-GNC、HccePose(BF)。读者看到名字，完全还原不出全称。
4. **优先沿用领域里已经成体系的后缀。** 用 `-GS`、`-3R`、`-Former`、`-VLA`、`-AD` 或版本号，读者一眼就能认出技术谱系，也最省力：AeroGS、AMB3R、StreamFormer、AVA-VLA、ActiveAD、CoTracker3。
5. **副标题是写给检索的关键词组合，不用来展示文采。** 结构几乎固定为"性质词 + 机制 + for/via + 任务"；Efficient / Adaptive / Unified / Robust / Training-Free 这类词反复出现。
6. **名字要短、读得出音、最好能带出一个意象。** 例如 ChordEdit、RayZer、TUNA、PRISM、Bokehlicious。
7. **三类取名失误最忌讳**：
   - 过长的术语堆砌：有个标题长达 137 个字符，却一个方法名都没有。
   - 硬凑缩写：见第 3 条。
   - 撞名：和领域里已有的术语撞（PGA、SCORE），或者和同一届的论文撞（两个 RAVEN；FoleyDesigner 和 FoleyDirector 同批出现）。
   - 其余反面情形（营销词、隐喻脱节、拼写错误、字母汤等）汇总在 §7。
8. **修辞预算只花在顶层名字上。** 主名负责被记住，子模块、损失和指标负责精确指代，用规整的描述性缩写（§5.1）。完全原创的方法才做双关或隐喻；建在知名模型上的方法老实写成"原名 + 前后缀"，不再强行双关。数据集和基准几乎都起一个好记的名字，因为要被后续工作引用；发现、分析、理论型论文常常不起名，把巧思留给标题。
9. **起名容易，统一使用难。** 名字在标题、摘要、正文、图表之间漂移，是反面案例中最常见的一类；名字确定后全篇严格复用，比取一个好名字更重要（§4.4）。

**一句话默认策略**：先判断这篇论文需不需要名字（见 §1.3）。需要的话，用 `X: [性质词] [核心机制] for [任务]`。X 优先考虑"领域后缀 + 核心机制词"的组合词，或者是一个本身有意义、全称和卖点对得上的真词缩写。

---

## 1. 标题结构

### 1.1 八种结构及占比

| # | 结构 | 占比（4 批区间） | 适用场景 |
|---|---|---|---|
| 1 | `X: 描述性副标题` | 约 50%–74%，绝对主流 | 提出新方法、新模型、新数据集 |
| 2 | 纯描述式，不造名，无冒号 | 约 26%–30% | 理论分析、单一贡献点、物理/几何问题、新任务定义；best 档的"自信型"标题 |
| 3 | `钩子短语: 正式副标题` | 约 8%–12% | 发现-解释型：前半句用反常识的断言或比喻，后半句交代技术内容 |
| 4 | `Beyond X: Towards Y` / `From X to Y` | 约 3%–4% | 强调范式转变 |
| 5 | `When/Where ...:` 陈述式悬念句 | 约 4% | 揭示失败模式、差距、盲区的分析型工作 |
| 6 | 问句 | 约 1%–2% | 标题本身就是研究问题，适合分析、质疑类论文 |
| 7 | `Rethinking/Revisiting X`（约 1%–3%）、`Towards X` 作主干（约 3%） | — | Rethinking 用来挑战既有假设；Towards 承认只是阶段性探索，更常嵌在副标题里，而不是放在开头 |
| 8 | 戏仿经典标题（meme） | 约 1% | 发现能用一句口号概括，并且能套上一个经典句式 |

### 1.2 各结构的正例、反例和写法

**结构 1：`X: 描述性副标题`**
- 正例：
  - *ChordEdit: One-Step Low-Energy Transport for Image Editing*
  - *LBM: Latent Bridge Matching for Fast Image-to-Image Translation*
  - *EVEv2: Improved Baselines for Encoder-Free Vision-Language Models*
  - *AIM: Amending Inherent Interpretability via Self-Supervised Masking*
- 写法：冒号前只放方法名，冒号后按 §3 的顺序写。LBM 的全称就是副标题开头的 "Latent Bridge Matching"，这是让缩写自解释的最省事的办法。
- 反例：冒号前的名字从副标题里反推不出来，比如 ESSENTIAL、CHROME 这类词中挖字母的名字。

**结构 2：纯描述式**
- 正例：
  - *Native and Compact Structured Latents for 3D Generation*
  - *Spatially-Varying Autofocus*
  - *Multi-View 3D Point Tracking*
  - *Rectifying Magnitude Neglect in Linear Attention*
- 写法：`[修饰] [核心对象] for/in [任务]`，或 `[动名词] [问题] in [对象]`，一般不超过 8 个词。
- 适用条件（满足一条即可）：
  - 贡献可以用一个名词短语说完；
  - 论文定义了一个新任务，任务名本身就是标题；
  - 论文是在修正一个现象（Rectifying ...）。
- 判断标准：贡献是不是一个**可以单独被引用的产物**（新方法、新表示、新框架、新数据集、新基准）。如果核心卖点是推导或发现本身、只优化了流程中的某个环节，或是理论/几何分析，就不为取名而取名，正文用 "our method / our framework" 指代。
- 更多样本：*Affine Perspective-Three-Point Problem*、*Certifiably Optimal Anisotropic Rotation Averaging*、*Registration beyond Points*、*Counting Stacked Objects*、*Self-Calibrating Gaussian Splatting*、*Solving Minimal Problems Without Matrix Inversion...*、*Simple but Effective Triplet-Based Compression Strategies...*、*Faithful Contouring*、*Uncalibrated SfM on a Sphere*、*Tiling artifacts and trade-offs*、*Compressed-Domain-Aware Online VSR*、*Modeling Saliency Dataset Bias*、*Optical Flow Matching*、*On the Recovery of Cameras from Fundamental Matrices*（正文只说 "a new iterative scheme"）。理论越重，包装越轻，也可以用 "On the X of Y"。

**结构 3：钩子短语 + 冒号**
- 正例：
  - *One Layer's Trash is Another Layer's Treasure: Adaptive Layer-wise Visual Token Selection in LVLMs*
  - *Mind the Gap: Preserving and Compensating for the Modality Gap in CLIP-Based Continual Learning*
  - *Heavy Labels Out! Dataset Distillation with Label Space Lightening*（带感叹号的标题很少见，只出现在 highlight/oral 档）
- 写法：钩子用习语改写（Trash/Treasure）或现成短语（Mind the Gap），而且要和核心发现同义；冒号后必须把任务和机制说全。
- 反例：钩子和发现无关，只图俏皮。

**结构 4：对仗式**
- 正例：
  - *Beyond Semantic Search: Towards Referential Anchoring in Composed Image Retrieval*
  - *From Contrast to Consistency: Rethinking Event-based Continuous-Time Optical Flow Estimation*
- 写法：X 是旧范式，Y 是新范式，两者必须是同一维度的对立（semantic vs referential，contrast vs consistency）。

**结构 5：When/Where 悬念句**
- 正例：
  - *When Pretty Isn't Useful: Investigating Why Modern Text-to-Image Models Fail as Reliable Training Data Generators*
  - *Where Culture Fades: Revealing the Cultural Gap in Text-to-Image Generation*
- 写法：`When/Where [反差现象]: [Investigating/Revealing] [现象] in [对象]`。冒号后用分析类动词开头。

**结构 6：问句**
- 正例：
  - *Is the Modality Gap a Bug or a Feature? A Robustness Perspective*
  - *What Do Visual Tokens Really Encode?*
  - *Does YOLO Really Need to See Every Training Image in Every Epoch?*
- 写法：问的是领域里默认成立的假设（"really need"、"really encode"），正文的答案通常是否定或出人意料的。可以在问句后接 `A [X] Perspective` 限定视角。
- 更多样本：*What does CLIP know about your camera?*、*Is Tracking really more challenging in First Person Egocentric Vision?*、*How to Take a Memorable Picture?*、*Too Vivid to Be Real?*、*Same or Not?*、*Rounded or Streamlined Head?*、*When Do Models Actually Decide*。问句标题用悬念做记忆点，副标题或正文要严谨。

**结构 7：Rethinking / Towards**
- 正例：
  - *Rethinking Dataset Distillation: Hard Truths About Soft Labels*
  - *Towards Scalable Spatial Intelligence via 2D-to-3D Data Lifting*
- 写法：`Rethinking [领域]: [具体被推翻的假设]`；`Towards [远期能力] via [本文手段]`。
- 更多样本：*Revisiting the Necessity of Full Accuracy*、*Rethinking Model Selection in VLM*、*Rethinking Key-frame-based Micro-expression Recognition*。
- 变体：`Rethinking X Through the Lens of Y`，用新工具重审旧问题（*Rethinking Model Selection in VLM Through the Lens of Gromov-Wasserstein Distance*）。`Towards X for Y` 常用于数据集或基础模型类，降低"问题已解决"的过度承诺（*Towards Foundational Models for Single-Chip Radar*、*Towards Generalized Multimodal Homography Estimation*）。

**结构 8：戏仿**
- 正例：
  - *CLIP Is Shortsighted*（戏仿 "X is all you need" 式的断言）
  - *A Frame is Worth One Token*
  - *Lidar Waveforms are Worth 40x128x33 Words*（这两个都戏仿 ViT 的 "An Image is Worth 16x16 Words"）
- 写法：只套用领域里人人都认识的经典句式，替换进去的数字或对象必须是论文的真实设定（40x128x33 就是真实的数据维度）。
- 更多样本：*A Style is Worth One Code*（CoTyle）；*TurboVSR: Fantastic Video Upscalers and Where to Find Them*（戏仿电影名《神奇动物在哪里》）。戏仿多在方法已有好记的简称时锦上添花，不是主要卖点。

### 1.3 选哪种结构（决策顺序）

1. 故事类型是**发现-解释型**（占 10.7%），核心产出是一个现象，而不是一个模块吗？
   - 是：用结构 3、5、6、8 中的一个。现象有反差就用 5，有习语可借就用 3，现象能归结成一个是非问题就用 6，能套上经典句式就用 8。
   - 否：进入第 2 步。
2. 贡献能否用一个名词短语说完，而且这个名词短语本身就足够新（新任务、新表示、新现象的修正）？
   - 是：用结构 2，不造名。
   - 否：进入第 3 步。
3. 论文的核心卖点是推翻一个旧范式吗？
   - 是：用结构 4 或 7（Rethinking）。
   - 否：进入第 4 步。
4. 其他情况一律用**结构 1（默认格式）**：`X: [性质词] [核心机制] for/via [任务]`。

**默认格式**：`X: [Adj] [Mechanism] for [Task]`。
故事类型中瓶颈突破型占 56.0%，统一框架型占 10.8%，数据与基准型占 7.0%，这三类合计约四分之三的论文，都适合用结构 1。

### 1.4 其他标题句式（无占比统计，按样本归纳）

下面这些句式在样本里反复出现，但没有分批占比。它们大多是结构 2–8 的变形，选用时仍按 §1.3 的决策顺序判断。

| 句式 | 样本 | 适合 |
|---|---|---|
| 宣言式（结论直接写进标题） | *SDE-Based GRPO Is Secretly Contrastive Learning*、*Visual Diffusion Models are Geometric Solvers*、*Mamba Learns in Context*、*The Scalability of Simplicity*、*Parallel Rigidity Matters for Bundle Adjustment* | 发现-解释、能力扩展 |
| 反直觉否定 | *Not All Frame Features Are Equal*、*Not All Birds Look The Same*、*No Calibration, No Depth, No Problem*、*No Pose at All*（押韵） | 瓶颈突破、新问题定义；卖点是去掉某个前提条件 |
| 对仗 / 口号 | *Two Losses, One Goal*、*Same Attention, Different Truths*、*Mask to Align, Weight to Disambiguate*、*Reinforce to Learn, Elect to Reason*、*Confound from All Sides, Distill with Resilience*、*One-Shot Flow, Any-Time Frame*（头韵）、*One Trajectory, One Token*、*THE MORE, THE MERRIER* | 发现-解释、统一框架 |
| 化用习语（不带冒号或作主标题） | *All Roads Lead to Rome*、*Seeing the Trees for the Forest*（反转成语）、*The Devil Is in Gradient Entanglement*、*The Midas Touch for Metric Depth*、*Hearing the Room Through the Shape of the Drum*（呼应经典反问题）、*Efficiently Reconstructing Dynamic Scenes One D4RT at a Time*（方法名嵌进习语） | 发现-解释；方法名本身能嵌入习语时 |
| `X Meets Y` | *Global SfM Meets Feedforward Reconstruction*、*Plant Taxonomy Meets Plant Counting* | 统一框架、两个领域交叉 |
| 强动词或姿态词开头 | *Unleashing Vecset Diffusion Model*、*Unstitching the Chimera*、*Scaling Language-Free Visual Representation Learning*、Taming X、*Keep It Frozen*、*Beyond Walking*、*Attend Before Attention*、*Brewing Stronger Features* | 想要画面感和传播力；Beyond 用于宣示突破默认限制 |
| 新造动词 | *SAM 3D: 3Dfy Anything in Images*、NERFIFY（-ify 后缀有产品感） | 能力扩展 |
| 类比句 | *Image as an IMU*（把"缺陷"重新定义为"信号"） | 一个比喻就能讲清方法 |
| 数字承诺 | *FastGS ... in 100 Seconds* | 瓶颈突破、效率优化 |
| 场景句 | *When Robots Should Say "I Don't Know"*、*Learning to See Through a Baby's Eyes* | 数据与基准、发现-解释 |
| 故事化 | *2.5 Years in Class* | 数据集的规模本身就是故事 |
| 玩梗 / 口语 | *Hoi!*、*I'm a Map!*、*LOTS of Fashion!*、*Heavy Labels Out!* | 数据集或趣味题 |
| 反差副标题 `X: A Yet B` | *LitePT: Lighter Yet Stronger Point Transformer* | 卖点是打破取舍 |
| 经典构词 `X from Y` | *Spectrum from Defocus* | 从一种信号恢复另一种量 |
| 对立 `A vs. B` | *Consensus vs. Controversy* | 两种观点或两类样本的对照分析 |
| 押韵 | *Mixture of Experts Guided by Gaussian Splatters Matters* | 可选的点缀 |

### 1.5 标题的配套规则

- **结构 1 的占比在部分类型里更高**：瓶颈突破型约七成、数据与基准型约八成用"方法名: 副标题"；有一批 20 篇里 17 篇用这种结构，另一批 20 篇近乎零例外。方法论文宁可副标题稍长，也要保证信息完整。
- **造了专名，标题第一个词通常就是这个专名**：Bokehlicious、BridgeDepth、CHROME、CObL、DisCoRD。
- **方法名尽量和标题核心名词绑定**，甚至同名（MeshSplatting、Mapping Networks），读者读了标题就知道方法叫什么。
- **标题双关可以倒推出方法名**：*I'm a Map!* → IMAP；*Reinforce to Learn, Elect to Reason* → RLER；*Heavy Labels Out!* → HeLlO；*LOTS of Fashion!* → LOTS。
- **也可以整句做标题，把名字留到正文**：*Same or Not?*、*When Robots Should Say "I Don't Know"*、*Not All Birds Look The Same*、*Beyond Single Images*；CoTyle 不出现在标题 *A Style is Worth One Code* 里。
- **修辞化标题要在正文呼应**：用了习语、疑问、断言之后，引言至少呼应一次标题的比喻。*Seeing the Trees for the Forest* 的引言写 "The trees are lost in the forest."；标题 "Diving into ..." 对应摘要 "We dive into ..."；FixTalk 全文反复用 tame/taming；宣言式标题的论文在图注和结论里复现标题原句（GROC 的 "See What We Cannot See"、SceneBench）。
- **标题可以比方法名更大胆**，但标题里的比喻同样要和机制对应。
- **"首个"之类的宣称写在贡献列表里**，很少写进标题。
- **标题造的词，正文要用它自称**（反例：Sparfels）。

---

## 2. 方法名的构造

### 2.1 七种构造方式

#### A. 首字母缩写凑成真词（backronym），最受青睐

- 正例：AIM、CARE（Cross-modal Adaptive Region Encoder）、CURE、GRACE、PRISM、TUNA、RARE、ZIM、GECKO、EVER。
- 构造步骤：
  1. 写出方法全称的候选词，4–6 个实词，覆盖"机制 + 对象 + 作用"。
  2. 列出和卖点语义相关的真词，4–5 个字母为佳，比如"修复"类卖点可以联想 CURE、CARE。
  3. 调整全称用词（换同义词、调语序），让每个词的**首字母**依次拼出目标词。
  4. 检查：只允许取首字母；介词和连词可以跳过；不允许从单词中间取字母。
  5. 检查：真词的词义和卖点对得上（AIM 对"可解释性的目标"，CURE 对医疗）。
- 反例：ESSENTIAL、CHROME、MAGICIAN、EXOTIC、GenErase、SAC-GNC、HccePose(BF)。
- 词义和卖点的几种对应方式（补充样本）：
  - 词义即机制：CLAMP（钳住，"traps harmful fine-tuning"）、ETCH（Equivariant Tightness Fitting，图注自陈 "resembles etching"，呼应贴合人体）、TEAR（撕裂安全防线，用于红队）、SABER（利刃，对抗攻击）、TRIDENT（三叉戟 ↔ 三模态）、CoIn（Coverage + Informativeness，一枚硬币的两面）、GLUEMAP（粘合两条路线 + SfM 建图）、SLiM（Salient Lightweight Matching，"苗条"呼应轻量）、NitroGen（暗示快）、STAC（谐音 stack，本身就是缓存机制）、PhyGaP（谐音 gap，呼应 "bridge the gap"）、GRACE（曲率 + 对齐化解矛盾）、ARGUS（希腊百眼巨人 ↔ 检测、警惕）、SAME（Sparse and Anchored Model Editing）、STCast（Cast 双关"预报"）、PR-MaGIC（呼应 training-free 的"魔法"）。
  - 词义即主题：CHIRP（鸟叫拟声词，用于鸟类行为数据集）、BioVITA（VITA 在拉丁语里是"生命"）、NABLA（NABirds Look-Alikes，又恰好是 ∇ 算子名）、SA-FARI（Segment Anything + safari，野生动物数据集）、MEDIC-AD（双关医疗）、DONUT（Dataset Of maNifold strUcTures，甜甜圈即流形）、GLINT（闪光 ↔ 玻璃透明材质）、FEAT（Fashion Editing And Try-on，双关"壮举"）、PiLoT（双关 UAV 的"飞行员"）、HOLO（恰是 hologram 的词根）。
  - 读成常见词或人名：MoRe（more）、OVRCOAT（overcoat）、PAS（pass）、LaSeRS（lasers）、HeLlO（Heavy Labels Out，读作 hello）、TiM（读作 Tim）、ZIM（Zero-shot Image Matting，像昵称）、JEGAL（像人名）、VENI（Variational Encoder for Natural Illumination，拉丁语"我来了"，又与竞品 RENI 押韵）。
  - 反讽：CoST 拼成 cost，反讽"降低成本"的主题；MEGA（Memory-Efficient 4D GAussian）用"巨大"命名一个省内存的方法。
  - 能还原成一句话：MTU3D = Move To Understand。
- 补充技巧：
  - 在全称里用大写字母标出取字位置，让读者可以验证缩写：TEAR ←"TEmporal-aware Automated Red-teaming"，UNCHA ←"UNcertainty-guided Compositional Hyperbolic Alignment"，BEA-GS ←"BEyond RAdiance Supervision"。
  - 可以调整词序或微调措辞来凑缩写，但不能牺牲可读性：VideoITG 的全称刻意写成 "Instructed Temporal Grounding for Videos"；"a discrete mask tokenizer" → SAMTok。
- 关于第 4 步的例外：样本里确有不严格取首字母的名字，例如 SEASON（Self-Diagnostic Contrastive Decoding，字母并不逐一对应）、RESCUE（取 charactErs 中间的字母）、HumanNOVA（从 siNgle-view / phOtorealistic / uniVersal / rApid 拼出 NOVA）、URICA（近似 Eureka）、TRIDENT ←"TRanscription-drug Informed latent Diffusion Embedding NeTwork"。本指南仍按第 4 步执行：只有真词和卖点对应极强时才考虑这样做，并且必须在全称里用大写标出取字位置；做不到就换构造方式。硬凑到读者无法还原的还有 CROWn（Coset-fibRated micrO-local…）；CUPID 被硬解为 "in-CUbe PIxel Distribution"，有汇总认为全文没有再呼应这个词义。

#### B. 谐音和双关

- 正例：
  - D4RT：4 谐音 for，同时暗含 "one day at a time"。
  - Gated KalmaNet：谐音 Kalman。
  - Hoi!：感叹号加谐音（荷兰语"你好" + HOI，即 human-object interaction 的缩写）。
  - SPDMark：正文直接写明 "pronounced 'SpeedMark'"。
  - DisCoRD：正文点破 "discord"，呼应离散/连续之间的张力。
  - Bokehlicious、TikZero、PanoLlama。
  - 补充样本：NeAR（near）、Selfi（selfie）、Wanderland（Wonderland）、3D-LATTE（拿铁）、CObL（读作 cobble ↔"拼出多层遮挡"）、Ov3R（over，同时致敬 DUSt3R 谱系）、AMB3R（读作 amber，呼应"保存 3D 场景"）、OMG-Bench（Online Micro Gesture / Oh My God）、CubiD（Cupid）、ReME（近 remedy）、SpeciaRL、SeeKer、LLMind（刻意读作 LLM）、Ditto（"同上/照做"，呼应指令式复刻编辑）、TWIN（双胞胎 ↔ 辨别相似图像）、AutoMoMa（叠词）。
- 构造步骤：
  1. 找出方法依赖的经典工具或概念名，比如 Kalman、Llama、Bokeh。
  2. 找一个和它发音接近、又能描述本文改动的词或数字（Net→KalmaNet，for→4）。
  3. 如果读音不直观，在正文首次出现处注明读法（参照 SPDMark 的做法）；如果双关就是论点，在正文里点破（参照 DisCoRD 的做法）。
- 风险：不注明读法的数字谐音，读者可能读不出来。

#### C. 组合词（两个实词拼接）

- 正例：
  - ChordEdit：chord + edit。
  - EcoSplat：eco + splat。
  - GazeGaussian、SwiftTailor、WikiCLIP、CaptionSmiths。
  - RayZer：ray + zero supervision，ICCV best。
  - ROAR：两个子模块的缩写拼接成一个词。
- 构造步骤：
  1. 选一个"特性词"：Eco（效率）、Swift（速度）、Gaze（输入信号）、Ray（表示）。
  2. 选一个"领域词或基座名"：Splat、Gaussian、Edit、CLIP、Tailor。
  3. 按"特性词 + 领域词"的顺序拼接，用驼峰大小写。
  4. 如果能再压出一层双关（RayZer 同时读作 "razor"，也暗含 zero），就更好。
- 这是最稳妥的构造方式：可读、可搜，也能直接看出做的是什么。
- 两种变体（补充样本）：
  - **截断拼接（portmanteau）**：两个关键词各取一部分拼成新词，不追求缩写规范。StaMo（State + Motion）、TeFlow（Temporal + Flow）、CoTyle（Code + Style）、ComPose（Completion + Pose）、SinGeo（Single + Geo）、ImmerIris（Immersive + Iris）、SpeciaRL（Specific + RL）、NeuraLeaf（Neural + Leaf）、SuperDec（Superquadric + Decomposition）、HoloCine（Holistic + Cinema）、LaRender（Latent + Render，对应"遮挡的本质是体渲染"）、Snellcaster（Snell 定律 + raycasting）、SigLino（SigLIP + DINO，名字透露方法是二者的蒸馏）、Editprint（Edit + fingerprint）、Moto（Motion 截断，带"发动机"联想）。
  - **卖点词 + 任务词直拼（"命名即摘要"）**：AdaptVision、HyperGait、LensWalk、LumiMotion、NaTex（Native + Texture）、AdvFractal（Adversarial + Fractal）、GeoPredict、RobotSeg、MaskControl、NullSwap（让身份提取失效）、SparseWorld-TC、GMMamba（Group Masking + Mamba，直接暴露技术血统）。风险：CausalNet（Causal + Net）这类最保守，也最没个性。

#### D. 借后缀或版本号延续谱系

| 后缀 | 来源 | 例子 | 主要方向 |
|---|---|---|---|
| `-GS` / `Gaussian` | 3D Gaussian Splatting | AeroGS、CoRoGS、TokenGS、GazeGaussian | 3D 重建、渲染 |
| `-3R` | DUSt3R | AMB3R、Dark3R | 3D 重建 |
| `-Former` | Transformer | M2SFormer、StreamFormer | 通用 CV |
| `-VLA` | Vision-Language-Action | AVA-VLA | 具身 |
| `-AD` | Autonomous Driving | ActiveAD | 自动驾驶 |
| 版本号 / `++` / `-1` | 自家前作 | CoTracker3、EVEv2、OmniHuman-1、GFPack++ | 延续工作 |

补充样本（同一构造方式在更多谱系上的用法）：

| 谱系 | 例子 |
|---|---|
| `-GS` / `-Splat` / `-Splatting` | Proxy-GS、RetimeGS、Turbo-GS、DirectFisheye-GS、Scaffold-GS、Octree-GS；EcoSplat、TokenSplat、SPFSplat（与 pixelSplat、PF3plat 同脉）；RT-Splatting |
| `-3R` | Scal3R、Ov3R、CLIP3R（DUSt3R → MASt3R → Dark3R 的谱系） |
| `-Former` | ForestFormer3D、EgoPoseFormer、Prior2Former（仿 Mask2Former） |
| `-VLA` | AT-VLA、XL-VLA、FAN-VLA、LinkVLA、CF-VLA |
| SAM | E-SAM、Spatial-SAM、OmniSAM、SAMTok、V²-SAM、SAM 3D Body |
| VGGT / DINO / CLIP | VGGT-Segmentor、OmniVGGT、AVGGT（A = Accelerating）；PET-DINO、SignDINO、Object-DINO；FluoCLIP、CorrCLIP、WikiCLIP、MG-CLIP、ReAttnCLIP、DeBias-CLIP、DermLIP（仿 CLIP 的 -LIP 后缀） |
| DiT / Mamba / ViT / MAE / LoRA | PixelDiT、DDiT（Dynamic + DiT）；GMMamba、DA-Mamba、TE-VMamba；MuViT、ResidualViT；DAP-MAE、VideoGMAE；CLoRA、HiLoRA、FI-LoRA |
| GPT / LLM / RL 算法 | BrickGPT、OralGPT-Plus、PanoLlama；DTPO、RDPO（Revised + DPO）、MUPO（"a drop-in replacement of GRPO"）、EviGRPO、Neighbor GRPO、GRPO-Guard |
| 任务后缀 | -Track（SDTrack、SEATrack、ADTrack、BA-Track）、-Seg（R²-Seg、B³-Seg）、-Loc（AsymLoc、GT-Loc、RALoc）、-ReID（AS-ReID）、-Net（VideoNet 仿 ImageNet、3DReflecNet） |
| 生成式流行后缀 | -Crafter（TrajectoryCrafter、HouseCrafter、MotionCrafter）、-Gen（FabricGen） |
| 版本 / 扩展标记 | 版本号：MatAnyone 2、Molmo2、EgoPoseFormer v2、DexGraspNet 3.0、SegEarth-R2、FOR-instanceV2；符号：CAFE+、MetaSpectra+（呼应标题 "Hyperspectral+"）、UnrealCV+、BUFFER-X（"to signify that it is an extension of BUFFER"）、DPoser-X、DMDX；字母前后缀：E-RayZer（E = Explicit，对比基线 RayZer）、STARFlow-V（-V 表示扩展到视频）、Inf-SSM、Re-DMD（Rewarded + DMD）、OA-CBM（Object-Aware + CBM）、Generalized-CVO、GECKO-Zero；iMF（小写 i 仿产品迭代）；FuXi-RTM（沿用作者自有品牌） |

- 构造步骤：
  1. 确认本文确实建立在该谱系上（用 3DGS 表示才用 -GS，基于 DUSt3R 类的 pointmap 回归才用 -3R）。
  2. 用一个短前缀点出本文差异：Aero（场景）、Dark（条件）、Token（机制）。
  3. 如果是自家前作的升级，直接加版本号，不另起新名。同一方法的多个变体也用数字、+、-X 管理，不给每个变体重新取名，否则会加剧漂移。
- **方向前缀 + 基座名**：前缀本身就是方向标签，把"在谁基础上往哪里改"焊进名字。
  - 能力或定位前缀：Omni-（统一或任意：OmniVGGT、OmniSAM、Omni-3DEdit、Omni2Sound）、Uni-（统一：UniPhys、UniDxMD、UniLight、Uni3R、UniPart、UniPixie）、Wild-（真实复杂场景：WildRayZer）、Phys-（物理约束：PhysNAP）、Ada-（自适应：AdaPrior、AdaSpark）、Turbo- / Swift- / Sprint / Flash（提速：Turbo-GS、TurboVSR、SwiftTailor、SANA-Sprint、FlashVDM）、Co-（协同：CoMatch、CoTracker3、CoopTrack）、Re-（重审或重做：ReFlex、ReME、ReTracker）、Sparse-（Sparse-LaViDa）。
  - 领域前缀：Ego-（EgoSound、EgoAVU、EgoXtreme）、Fed-（FedHarmony、Fed-ADE、FedTSP）、Geo-（GeoAgent、GeoCoT、GeoMMBench）、Spatial-（SpatialScore、SpatialAgent、SpatialTree）、MV-（MV-RoMa）。
  - 在基线名前加限定词，名字本身就概括了创新点：CausalVAD、Counterfactual VLA、VolumetricSMPL、Stable Mean Flow、Improved Mean Flows、RS-vHeat（正文明写 "inspired by vHeat"）。
  - 前缀要对应机制，不是营销：TriLite 的 Tri- 对应"前景 / 背景 / 模糊"三分设计，子模块也叫 TriHead。
  - Re- 有歧义：ReCamMaster 的 Re 表示"重新"，RePoseD 的 Re 却表示 "Relative"。用这类前缀时要在正文说明含义。
- **借热门模板或致敬前作**：
  - "X Anything" 句式：UnReflectAnything、ZIM（"for Anything"）、AEMG（Any ElectroMyoGraphy）、PolarAnything、*Depth Any Endoscopy*、Stereo Any Video。
  - 改一个字母致敬：TAM ← CAM（只把 Class 换成 Token，正文写明 "different from CAM"）、DIIP ← DIP、ReAG ↔ RAG、C²FG ← CFG。
  - 仿写构词：DSO（Direct…Optimization，仿 DPO）、BRICKGPT（用 next-brick 类比 next-token）、MonoCoP / VideoCoF（XCoY）。
  - 反义或去除：UnZipLoRA（与 ZipLoRA 方向相反）、AntiPure、NormFree（直接写出去掉了什么）；致敬：SuperEvent（致敬 SuperPoint / SuperGlue）。
  - 理论或算法血缘：Gated KalmaNet（Kalman）、HamiPose（Hamiltonian）、GeoRK2（Runge-Kutta），制造"理论有源头"的可信感；FedAdamom（FedAdam + "om" 表示 momentum）；VMonarch 借 Monarch matrix（兼有帝王蝶意象）。
- 规则：借势时不再强行双关，读者要能一眼看出继承自谁。热门前缀容易撞名：有一批里 5 篇用 Omni-，还出现了 OmniDocLayout-1M 与 OmniDocLayout-LLM 的冲突。只有后缀、没有卖点词的名字缺少个性。

#### E. 数字与符号

- 上标双关：R²-Seg、U²Flow、C²FG。适合"两个同首字母的概念"，比如两个 R 开头的词。
- "2" 谐音 "to"：ISP2HRNet、O2MAG。适合表达"从 A 到 B"的转换。
- 规模直接写进名字：OmniFood8K、PETARSeg-11K。数据集和基准专用，把规模当卖点。
- 构造规则：符号和数字必须有含义，不能只当装饰。上标的名字要准备好纯文本写法，比如 R2-Seg，方便检索。
- 补充样本：
  - "4" 谐音 "for"：Point4Cast、VLM4RSDet、RF4D、LMM4LMM（同时自指"用 LMM 评测 LMM"）。
  - "2" 谐音 "to"：Talk2Move、Widget2Code、UI2Code、Glove2Hand、Omni2Sound、Cov2Pose、CA2D、Unsafe2Safe（标题即叙事）、Prior2Former（读作 "Prior to Former"）、StableText2Brick（沿用 text2img 式命名）。
  - 数字替换字母，制造视觉记忆点：AMB3R、D4RT、Scal3R、Ov3R；H2MM（2 代替重复的 H）。
  - 上标暗示重复、双重性或升级：V²-SAM、GM-R²（平方号双关 Representation + Registration）、B³-Seg、ViT³（= ViTTT）、U²Flow（模仿 U²-Net，双关 uncertainty + unsupervised）、x²-Fusion；C²FG 把全称里 Control、Classifier 两个 C 折成上标，保留业内熟知的 CFG 作词根，暗示"升级版"。
  - 维度写进名字：Geo4D、U4D、4D-RGPT、2D-LFM、WIR3D、MTU3D、E3Flow（SE(3)）、Λ24-SQ、Edit360（360° 全视角）。
  - 大写双关：GraspALL（Any Low-Light，同时读作"抓取所有种类"）。
  - 数据集的规模后缀见 §5.2。
- 风险：数字名的全称常常只在图注或结论出现一次，而且前后不一致。全称要在摘要或引言里完整给出一次。

#### F. 借典故或联想（多见于生成式和美学任务）

- 正例：
  - Batman：后门攻击，靠反差制造记忆点。
  - Lafite：借酒庄名。
  - Clair Obscur：借"明暗对照"。
  - Fresco：借壁画意象。
- 适用：生成、编辑、渲染、美学类任务，典故能对应到输出的视觉特征。
- 风险：名字不含技术信息，副标题必须把机制和任务写全。
- 补充样本（按意象来源）：
  - 物件或自然隐喻，对应机制：Chorus（多教师蒸馏 → 众声合唱）、MeshRipple（"涟漪"对应 BFS 式扩散）、Vector Prism（"much like a prism for vector graphics"）、WorldLens（用"镜头"隐喻评测本身）、BridgeDepth（连接单目与双目两种范式）、Diorama（西洋镜 ↔ 单视角室内建模）、Clay-to-Stone（泥到石，喻两阶段由软到硬）、FloodDiffusion（用"洪流"代替直白的 Streaming）、Chimera（缝合怪，配合标题动词 Unstitching）、4D Primitive-Mâché（谐音 papier-mâché 手工艺）、*The Midas Touch for Metric Depth*、DENALI（北美最高峰）、Harmonic Canvas、UnrealZoo（"动物园"比喻实体多样）、ChronoGS（Chrono = 时间）、FlashDepth（Flash 喻速度）。
  - 神话或人物：NuWa（女娲，"用基础模型塑造小模型"的造物隐喻）、MARCO（马可·波罗 ↔ 探索）、Janus-Faced Affinity Learning。
  - 职业或角色拟人（暗示"模拟专家工作流程"）：SwiftTailor（生成服装 = 裁缝）、DataTailor（量体裁衣式数据筛选）、FoleyDesigner / FoleyDirector / GardenDesigner、HouseCrafter、GameFactory、CaptionSmiths（铁匠锻造）、WorldForge、Wan-Weaver（编织呼应 interleaved）、SyncDreamer、ObjectMate、ObjectRelator、SENTINEL（哨兵）、Gallant、Matador、LEGION（军团气势）。
  - 生物或人体：HippoVLM（海马体，喻记忆机制）、SpiderCam（蜘蛛状多目相机）、Corvid、RAVEN、GECKO。
  - 品牌或流行文化：LOREAL（欧莱雅）、SEGA（游戏公司）、MikuDance（初音未来）、AAA-Gaussians（暗合"3A 大作"）、OralGPT-Plus（仿 ChatGPT Plus）、HairCUP（缩写即生活词 CUP）；Copernicus-FM / -Pretrain / -Bench 借欧盟计划名建立系列感。
- **隐喻要贯穿全文**：名字就是洞察时，隐喻要在摘要、Fig. 1、方法、结论里反复出现。MeshRipple 写 "akin to a ripple on a surface"，并用 ripple / frontier / root 自成一套词汇；Midas Touch 写 "Gold from a touch; meters from a hint"；FoleyDirector 的"导演"隐喻贯穿标题、Fig. 1 和结论；HouseCrafter 的隐喻词 "lift" 贯穿标题、摘要和贡献列表；BridgeDepth 通篇不提名字，只反复用隐喻动词 "bridges"。
- 补充风险：隐喻和机制不对应就显得生硬。LegoOcc 的品牌名与 Method 正文脱节；Circuit Mechanisms 的"胚胎发育梯度"类比被批评缺乏论证；LagerNVS 的双关与内容无关。只为好记、语义关联很弱的名字（Scone）要确认是有意为之。

#### G. 严格描述性缩写（透明可信型）

- 做法：不追求好读，只保证每个字母都能追溯到全称。读者是细分领域的专家，看重信息密度。
- 正例：HiLoRA、MFEN、MSPT、SADG、PLMP、GS-MoE、GRT、DCL（Dual Convergent Lines）、ResFit、OrthoReg、CasP、SACM、RDVQ、ETN、SDUIE、gQIR、AutoOcc；能从名字直接猜出结构的：PixelDiT、UNO-Adapter、ConvAttn（Convolutional Attention）、TVT（Transfer VAE Training）。
- 折中：MEMFOF 由 Memory-Efficient Multi-Frame Optical Flow 缩合成一个能读的词。
- 适用：工程或系统型贡献、医学、水下、遥感、3D 几何、理论方向。检测、优化、理论类论文偏纯技术缩写或不造名；生成、交互类论文偏隐喻和品牌化。
- 风险：多段连字符缩写虽然能拆解，但难读难记，是"技术描述压倒命名巧思"的典型失败：GOR-IS、AFoV-ERP、DC-CN、RR-DU、UPA-RFAS、MDCS-MoAME。

### 2.2 大小写规则（按样本归纳）

- 真词型 backronym 全大写：AIM、CARE、PRISM、GECKO。
- 组合词用驼峰：ChordEdit、EcoSplat、RayZer、SwiftTailor。
- 在组合词里保留已有专名的原始大小写：WikiCLIP、PanoLlama、TikZero。
- 大小写混排的缩写（DisCoRD、GenErase）只有在大写字母确实对应全称首字母、并且能拼出一个可读的词时才用。
- 版本号直接接在名字后面，不加空格：EVEv2、CoTracker3。
- 截断拼接的词可以用大写保留拼接痕迹：SinGeo（Single + Geo）、StaMo（State + Motion）。
- backronym 的全称里用大写标出取字位置（TEAR、UNCHA、HumanNOVA、LOREAL），读者才能验证缩写。
- 可以首次出现时用全大写，之后恢复正常大小写（SUPERFRUSTUM、RESFIT）；无论选哪种，全文要统一。

### 2.3 好名字的检查清单（逐项打勾，有一项不通过就换）

| 检查项 | 通过标准 | 反例 |
|---|---|---|
| 好读 | 能一口读出来：要么是真词，要么是 2 个音节以内的组合，要么正文注明了读法 | SAC-GNC、HccePose(BF) |
| 好记 | 不超过 10 个字母，或者由两个可识别的词根组成（样本中旗舰名多为 3–6 个字母，整体多在 2–8 个字符） | 过长的术语堆砌 |
| 可还原 | 从名字加副标题能反推出全称，缩写只取首字母 | ESSENTIAL、CHROME、MAGICIAN |
| 可搜索 | 名字加一个领域词搜索时结果不被淹没；带上标的名字有纯文本写法 | — |
| 不撞名 | 不和领域已有术语、知名方法重名，也不和同期工作重名或近名 | PGA、SCORE；两个 RAVEN；FoleyDesigner 和 FoleyDirector |
| 和机制有关联 | 名字里至少一个成分指向核心机制、表示或谱系 | 纯典故名如果副标题也不写机制，就不通过 |

表外还有两条同样一票否决的约束（详见 §7）：名字的响亮程度不能超过正文证据（不用 Super / Ultra / Mega / Magic 类营销词）；名字本身不能有拼写错误。

### 2.4 按技术处境选构造方式

先按 §1.3 确认需要造名，再按论文的技术处境选构造方式。按故事类型的差异见 §6。

| 处境 | 首选 | 例子 |
|---|---|---|
| 完全原创的核心方法 | A（backronym）或 F（隐喻）；倒推不自然就退回 C | CLAMP、Chorus、ChordEdit |
| 建在知名模型之上 | D：基座名 + 前后缀，不做双关 | VGGT-Segmentor、PET-DINO、E-SAM |
| 续作，或已有方法的扩展、变体 | D：版本号、+、++、-X、字母前缀 | E-RayZer、CoTracker3、BUFFER-X |
| 定位是统一或自适应 | D：Omni- / Uni- / Ada- 前缀 | OmniVGGT、UniPhys、AdaPrior |
| 属于某个热门范式 | D：谱系后缀 | Proxy-GS、Dark3R、AT-VLA |
| 与前作方向相反，或去掉了某个组件 | D：反义前缀或 -Free | UnZipLoRA、NormFree |
| 任务映射（X 生成 Y） | E：X2Y | Talk2Move、UI2Code |
| 维度或规模是卖点 | E：数字入名 | Geo4D、V²-SAM |
| 有强画面感的比喻 | F | MeshRipple、SwiftTailor |
| 工程、垂类、几何、多模块系统 | G | HiLoRA、GS-MoE、PLMP |
| 贡献不是可单独引用的产物 | 不造名（§1.2 结构 2） | 见 §4.2 变体 3 |

多份汇总的共同偏好：backronym（A）和描述性缩写或词根直拼（C、G）用得最多；"能读出来、像正常英文词、字面意思与领域有关"是压倒性的偏好。有一份汇总给出的偏好排序（仅这一份的判断）：读出真实单词并带双关 > 编码卖点（数字、后缀、版本号）> 纯功能缩写 > 延续品牌 > 子模块直白缩写 > 不命名。

### 2.5 名字的素材从哪里来

1. **从洞察句取词根**。名字的词根应取自引言中反复出现的核心洞察词：
   - DeltaWorld / DeltaTok 的 "Delta" 对应洞察"帧间差值低维"；
   - BridgeDepth 复用问题段的动词 "bridge"；
   - LF-BVN 的 "blind-view" 来自与 "blind-spot" 的类比；
   - DreamLayer 的 "layer" 贯穿全文；
   - ChordEdit 的 "Chord" 来自引言里的 "low-energy chord"。
2. **从洞察句挑一个核心动词或意象**：钳住（CLAMP）、蚀刻（ETCH）、涟漪（MeshRipple）、合唱（Chorus）、导演（FoleyDirector）、粘合（GLUEMAP）。
3. **用反义构词表达与被批评对象的对立**："Ada-" 前缀常与被批评对象的形容词构成反义（AdaPrior 对 "static class counts"）；NormFree 直接写出去掉了什么。
4. **写下 2–4 个关键词再组合**：机制词 + 对象词 + 卖点词，例如 ChordEdit = chord（低能量弦）+ edit。然后按 §2.1 的构造方式生成候选。

---

## 3. 副标题写法

### 3.1 信息顺序

**方法类（默认）**：`[性质/效率形容词] + [核心机制] + for / via / through + [任务/场景]`，机制在前，任务在后。
- *EcoSplat: Efficiency-controllable Feed-forward 3D Gaussian Splatting from Multi-view Images*
- *AnchorFlow: Training-Free 3D Editing via Latent Anchor-Aligned Flows*
- *LBM: Latent Bridge Matching for Fast Image-to-Image Translation*

**数据集/基准类**：任务优先，Benchmark 或 Dataset 前置。
- *WHU-MARS: A Multispectral Aerial-Ground Benchmark...*
- *GEOBench-VLM: Benchmarking Vision-Language Models...*
- 模板：`X: A [属性] [场景] Benchmark for [任务]`，或 `X: Benchmarking [被测对象] on [能力]`。
- 其他常见写法：`A Large-Scale [Dataset/Benchmark] for X`、`A Comprehensive Benchmark for X`、`Towards Comprehensive X`；揭短式副标题 "Exposing the Lack of ..."（OddGridBench）。副标题写了 Comprehensive 或 Large-Scale，正文就要有 Table 1 式的横向对比来支撑。

**统一框架类**：`X: A Unified [对象] for [范围]`。
- *AToken: A Unified Tokenizer for Vision*
- 也常写成 `X: A Unified Framework for …`（CROWn、D-Convexity、Drainage、ForestFormer3D），或把"统一"写进副标题动词（*GT-Loc: Unifying When and Where…*）。

**改进基线类**：`X: Improved Baselines for [对象]`。
- *EVEv2: Improved Baselines for Encoder-Free Vision-Language Models*

**介词选择**：
- `for` 接任务：for Image Editing。
- `via` 或 `through` 接手段：via Latent Anchor-Aligned Flows。
- `from` 接输入：from Multi-view Images。
- `in` 接研究对象：in Linear Attention、in LVLMs。
- `with` 或 `through` 接表示或额外信号：*GT-Loc: ... Through a Joint Embedding Space*；*LumiMotion: Improving Gaussian Relighting with Scene Dynamics*。

### 3.2 高频词及各自暗示的卖点

四批共同的高频词如下。副标题只选**一到两个**，并且要能在实验里兑现。

| 词 | 暗示的卖点 | 实验上必须兑现的内容 | 样本例 |
|---|---|---|---|
| Efficient / Efficiency- / Fast / One-Step | 更少的计算、步数或时间 | 速度或 FLOPs 对比表 | *EcoSplat: Efficiency-controllable...*；*LBM: ...for Fast Image-to-Image Translation*；*ChordEdit: One-Step...* |
| Training-Free | 不训练、即插即用 | 在多个基座上直接套用 | *AnchorFlow: Training-Free 3D Editing...* |
| Zero-Shot | 不需要目标域标注 | 未见类别或未见数据集上的结果 | — |
| Unified / Unifying | 一个模型覆盖多任务或多模态 | 覆盖多个任务的结果表 | *AToken: A Unified Tokenizer for Vision* |
| Scalable / Scaling | 性能随数据或模型规模增长 | scaling 曲线 | *Towards Scalable Spatial Intelligence via 2D-to-3D Data Lifting* |
| Adaptive / -aware | 按输入动态调整 | 自适应机制的消融 | *One Layer's Trash...: Adaptive Layer-wise Visual Token Selection in LVLMs* |
| Robust | 在扰动、噪声、分布偏移下保持稳定 | 扰动或 OOD 实验 | *Is the Modality Gap a Bug or a Feature? A Robustness Perspective* |
| Fine-Grained | 更细的粒度 | 细粒度指标或可视化 | — |
| Real-Time | 能在线部署 | FPS | — |
| Generalizable | 跨场景、跨数据集 | 跨域实验 | — |
| Towards | 阶段性探索，目标很远 | 不要求完整解决，但要给出明确的一步 | *Towards Scalable Spatial Intelligence...* |
| Rethinking / Revisiting | 挑战既有假设 | 推翻假设的对照实验 | *Rethinking Dataset Distillation: Hard Truths About Soft Labels*；*From Contrast to Consistency: Rethinking Event-based...* |
| Improved Baselines | 简单改进带来强基线 | 在同一设置下全面超过前作 | *EVEv2: Improved Baselines...* |

（"—" 表示合并材料只把它列为高频词，没有给出带这个词的具体标题，不要为它编造例子。）

副标题的**第一个形容词**通常就是核心卖点，例如 Open-Vocabulary、Rotation-Invariant、Coupled、Portable（*Portable Active Learning for Object Detection*）。

### 3.3 副标题避免的写法

1. **堆砌三个以上性质词**，例如 "Efficient, Robust and Generalizable Unified ..."。样本里只有正文首次引入句会并列三个性质词（ChordEdit 的 "model agnostic, training-free, and inversion-free"），副标题里不这么写。
2. **任务在前、机制在后的方法类副标题**。只有 Benchmark 或 Dataset 类才任务优先。
3. **缺少任务或场景**：副标题只写机制，读者不知道应用在哪里。
4. **用上面没有兑现的高频词**：写了 Real-Time 就必须有 FPS。
5. **标题过长**：要避免 137 字符级别的术语堆砌。

---

## 4. 方法名在摘要和引言中的首次引入

### 4.1 在摘要中的位置（统计依据）

- 摘要句数中位数为 8，四分位 [7, 8, 9]，最常见的是 8 句（25.2%）。
- 摘要按长度五等分后：
  - 第 1/5 段的主作用：背景 57%，问题 18%，缺口 11%；
  - 第 2/5 段"方法"占 44%，是方法名首次出现最集中的位置；
  - 第 3/5 段：方法 38%，设计细节 35%。
- 摘要第 1 句的作用：背景 56.6%，背景+问题 21.2%，背景+缺口 7.3%。以"方法"开头的只有 6.6%，加上背景+方法 1.7%、问题+方法 0.8%、方法+意义 0.7% 等组合也只有一成左右。
- 按摘要原句逐句重算 [重算]：第一次出现 "we propose / introduce / present" 的句子序号为第 1 句 10.2%，第 2 句 10.1%，**第 3 句 27.5%，第 4 句 23.9%**，第 5 句 10.7%，第 6 句 4.4%，第 7 句及以后 3.0%；另有 10.2% 的摘要不用这三个动词（用 develop、termed，或全程不点名）。

**执行规则**：在 8 句摘要里，方法名放在第 2–4 句首次出现（最集中在第 3–4 句），也就是交代完背景和缺口之后的第一句。只有在方法名本身就是任务名、或论文是纯资源发布时，才考虑在第 1 句引入。

### 4.2 引入句式

三种主谓语在四批里频次排序一致：**we propose（约 45–50%）＞ we introduce（约 25–30%）＞ we present（约 10–15%）**。

**骨架模板**：

> "We introduce X, a [性质形容词组] [framework/method/model] that [核心机制]."

样本原句：
> "We introduce ChordEdit, a model agnostic, training-free, and inversion-free method that facilitates high-fidelity one-step editing."
>
> "We present RayZer, a self-supervised multi-view 3D Vision model trained without any 3D supervision."

**变体 1：先给全称，再在括号里给缩写**（适合 backronym；20.8% 的摘要写成"全称 (缩写)" [重算]）：

> "... we propose [Full Name] (X), which ..."
>
> 样本："Gigapixel Vision-Concept Knowledge Contrastive pretraining (GECKO)"

同类写法：
- 取名自信、朗朗上口的缩写，直接在方法句里用同位语一次给全：`we propose Name (Full Name / ABBR), a [category] that [mechanism]`（SeaCache、SfD、SenCache、ASO、FINER、SACM、RDVQ）。
- `We propose [Full Name], or [ACRONYM], a novel [pipeline] that [核心机制].`（ETCH）
- `X (for '[full name]')`，名字后面立即解释全称（CUPID："we introduce CUPID (for 'in-CUbe PIxel Distribution'), a probabilistic reconstruction framework..."）
- `We present [Method], an [首字母对应全称] [类型] framework.`（ApET）

**变体 2：用显式命名动词 termed / dubbed / named / called**（各批出现频率不均：batch1 未见 dubbed，batch4 常见；合计 7.1% 的摘要用 termed / dubbed / named / we call 类词 [重算]）：

> "... a novel [类别] method ..., dubbed X."
>
> 样本："a novel distillation method... dubbed ScoreLiDAR"；"we can treat as an intrinsic edge field... termed the Event Edge Space"

同类写法：`we propose a [descriptive phrase], termed Name`（SDMFusion、ImmerIris、SuperFrustum）；`Our approach, coined X (ABBR), leverages…`；`hereby named [缩写]`；`we refer to our approach as "[Name]"`。

**变体 3：不宣布名字**。部分纯理论或分析型论文的摘要首句不专门"宣布"命名，直接陈述发现。结构 2、3、5、6 的论文可以这样写。
- 摘要全程用描述性说法指代：《Heuristic Self-Paced Learning》全篇不提 HeuSCM，只说 "an autonomous class scheduler"；《Rethinking Model Selection in VLM》写 "our proposed inference-only metric"；《Spatially-Varying Autofocus》写 "our design/technique"；《LaRender》《Explaining Human Preferences via Metrics》同样不点名。
- 名字只留给代码仓库：《A Linear N-Point Solver》的方法名只出现在 GitHub 链接里；《Global SfM Meets Feedforward Reconstruction》的仓库名叫 gluemap。
- 这种命名策略与全篇克制措辞（写 "competitive" 而非 "outperforms"）是一致的写作姿态。

**变体 4：先讲道理再亮名，并交代命名理由（命名即论证）**。发现或推导写完之后才命名，命名句顺带解释机制：
- `We name our method [Name] for its ability to [能力，用首字母对应的词].`（StaMo："We name our method StaMo for its ability to learn generalizable robotic Motion from compact State representation..."）
- `…which we term [Name]`（SimScale）；CoST 到摘要倒数第二句才给全称和缩写。
- `Since [机制], [it is named / we refer to our method as] [Name].`（Transition Models："Since the training objective is to learn the transitions between any state to a previous state, it is named Transition Models (TiM)."；Learning Robust Stereo Matching）
- `Because [设计特点], we call it [名称], or [缩写] for short.`（CObL，正文自称 "Concurrent Object Layers, or CObL"）
- `We name our approach X to signify that it is an extension of Y.`（BUFFER-X）
- `As suggested by the name, [新方法] operates in the opposite direction of [前作].`（UnZipLoRA）
- `We refer to this approach as "[Name]" because …`（《Just-in-Time Digital Twins》）
- 隐喻名配一句解释：`much like a [隐喻物] for [领域]`（Vector Prism："much like a prism for vector graphics"）
- 家族名解释构成：`'GF' stands for our method GameFactory and 'Minecraft' refers to the game name`（GameFactory）；结构上模仿经典命名时点明区别：`TAM ... different from CAM`
- 也可以用脚注解释名称由来（SEELE）。命名动机写一次即可。

**变体 5：先亮代号，全称留给正文**。摘要只用缩写，不展开，制造悬念：ARGUS（全称到正文第 5 节才补出）、D4RT（全称只在 Fig. 1 图注）、GLINT、LILA、Traq。多见于隐喻或诗意型名字。风险：全称从不展开会被点名（TMFS 的核心缩写、THDR3K 都没有展开）。

**选择规则**：
- 方法名是组合词或真词：用骨架模板，`X,` 后接同位语。
- 方法名是 backronym，且全称没有出现在标题里：用变体 1，让全称在摘要里完整出现一次。
- 命名对象不是一个"方法"，而是概念、空间或表示：用变体 2 的 termed（参照 Event Edge Space）。
- 名字的由来本身就是论点（名字由根因或洞察直接推出）：用变体 4。
- 同位语里的性质形容词，要和副标题的高频词保持一致。副标题写了 Training-Free，同位语里就要出现 training-free（参照 ChordEdit）。
- 首创声明可以和命名句绑定："we propose AT-VLA, which, for the first time, achieves a balance…"（AT-VLA；MEMFOF、SAFE-GRPO 同样把 "the first" 放进命名句）。只在确实首创时这样写。
- 摘要里自造缩写不超过 2–3 个（主方法名加最多一两个核心概念）；子模块缩写留给正文。并非所有能缩写的概念都要在摘要里正式命名（BiPreManip、CAAM、VITA 把次要概念留到引言展开）。

### 4.3 引言中的引入

- 引言段数中位数为 6，四分位 [5, 6, 6]。5 段和 6 段合计 56.2%。
- 贡献列表：74.4% 用 bullet，25.0% 写在段落里。
- 91.3% 的论文在第一页或引言中有 teaser 图（Figure 1）。

**执行规则**：
1. 方法名在引言里第一次出现时，重复摘要里的同位语句式，可以换一个动词，比如摘要用 propose，引言用 introduce。缩写型名字要再给一次全称。
2. 贡献 bullet 的第一条以方法名开头："We propose X, ..."。
3. 引入名字之后，引言剩下的段落只用 X 指代本方法，不再用 "our method" 和 X 交替。
4. 名字在方法段（MTH）首次登场，放在洞察句之后；§4.2 的各种句式在引言里同样适用。发现驱动的论文可以把命名推迟（到贡献列表或方法正文），但同一篇里摘要和引言的展开时机要一致（反例：DreamShot 的核心缩写 RACL 延后到引言才展开，和其他缩写不一致）。
5. 沿用前人术语时附引用编号，和本文原创的名字区分开（"Best-of-Many (BoM) [5]"）。

### 4.4 全文名称一致性清单

- [ ] 标题、摘要、引言、方法节标题、实验表格、图注里的 X 拼写和大小写完全一致（EVEv2 不能在别处写成 EVE-v2）。
- [ ] 全称只在摘要和引言各完整出现一次，之后只用缩写。
- [ ] 子模块如果也有名字，在方法节首次出现时同样用"全称（缩写）"引入。子模块名不要和主名形成近名，例如同一篇里的 FoleyDesigner 和 FoleyDirector。
- [ ] 带上标或特殊符号的名字（R²-Seg），在正文里统一用同一种排版。
- [ ] 版本号延续前作时，在引言里明确写出和前作的关系（EVEv2 的副标题 "Improved Baselines" 已经交代了这层关系）。
- [ ] 需要注明读法的名字（参照 SPDMark），在第一次出现处注明，之后不再重复。
- [ ] 全称在摘要、引言、方法小节标题、结论中逐字一致。这是各份汇总里出现频率最高的可改进项。反例：FaithC / FCT / Faithful Contouring 三名并存；CIGPose 有三个全称版本；MCT 先后写成 Multi-Condition / Multimodal-Condition Transformer；PPE 写成 Physical / Physics Parameter Estimator；CoST 的 Collaborative / Cooperative；AdaSpark、Authorize-on-Demand 的全称表述不一致。
- [ ] 主名拼写在全文和图表中一致。反例：DreamOmni2 与 "Dreamomni2"；VMonarch / VideoMonarch；CCNet / CCFNet；GMMamba / CMMamba；DOSFMVC / DOSMFVC / DOSFMNVC；FloodDiffusion 的方法名与标题措辞不一致。
- [ ] 图表中的模块名与正文一致。反例：LensWalk 的 "Stitched Verify" 在图表中变成 "Stitch Verify" / "Stitch"；ROSE 的 VRMG / VGRM；SCORE 的 GCA 被误写为 VCA / VPA；SEGA 的 FR / RF module 互相写错；RaUF 的 BDAF、RoboPerform 的 ResMoE 与 ∆MoE 前后不一；《RAVEN》的模块名前后不一致。
- [ ] 同一概念在摘要和正文用同一个名字。反例：AVGGT 摘要写 "mean-fill component"，正文写 "mean component"。
- [ ] 每个定义过的缩写在后文都被使用，否则删除定义（反例：MOFA-VTON 的 "LA"）。
- [ ] 组合缩写说明了拼接逻辑（反例：OVRCOAT 由 OVR + COAT 拼成，但没有解释来由）。
- [ ] 缩写至少在摘要或引言里展开一次（反例：TMFS、THDR3K 从未展开；CHROME、CODA、CLoRA、DIMO 在正文中没有括注展开）。
- [ ] 名字里的隐喻词在摘要到引言中至少再出现一次（正例见 §2.1 F 的"隐喻要贯穿全文"）；但不要重复到失去效果（AD-GBC 连用三次 "catastrophic" 的同根词；AMB3R 的 "cornerstone" 只用一次，是克制的正例）。

---

## 5. 子模块、数据集、家族与现象的命名

主名之外，论文里还有子模块、损失、指标、数据集、基准，以及需要被反复指代的现象。它们的命名规则和主名不同：越靠近读者视线越讲究，越往内部越朴素。

### 5.1 子模块

1. **功能描述优先，不求好读**。先写完整功能短语，再压成缩写：teacher-prior adaptive masking (TPAM)、cross-view masked feature completion (CVMFC)、Script-Guided Temporal Fusion Module (SG-TFM)、Valid Region Focus Module (VRFM)、Task-Aware Region Guidance (TARG)。能拼读更好：SET、ALR、BASS（Bio-inspired Adaptive Sampling Strategy）、DTPO（Decoupled Turn Policy Optimization）、ARKD（Asymmetric Relational Knowledge Distillation）。
2. **两级命名体系**：主名是"门面"，子组件用二级缩写，例如 CADC 下的 UGAQ / ADGIC / BFATC，TF-CADE 的 ACA / CCR，THERIS 的 TDIM / TSSM，Urban-GS 的 AJAD / CAP / GLO，V²-SAM 的 V²-Anchor / V²-Visual。也有论文只编号不命名（MHC-DUN）。
3. **同一篇内用统一模板**："形容词（-guided / -aware）+ 功能词 + Network / Module"，例如 DiffPS 的 DGRPN / MSFRN / SFAN，DreamLayer 的 CACA / LSSA / IRH；CADC 的三个子模块统一用 "X-Guided/Adaptive Y" 句式；Adapt-Net / Cloth-Net 统一用"功能词 + Net"。Module / Loss / Block 这类后缀直接说明组件角色。
4. **对称成对，方便配对记忆**：SPTP / UPTP / APTP 只替换首个形容词（命名本身就是论证）；EcoSplat 的 PGT / IGF；FEAT 的 DDI / OGNF；GMMamba 的 IMM（intra-）/ CSS（cross-）；MetaScope 的 OIA / OCC（共享 "Optics-informed" 前缀）；DA-Mamba 的 Image-Aware / Object-Aware SSM；VeilGen（生成）/ DeVeiler（去除）；孪生模块同构押韵 EMI / EDI；Consensus-Driven / Disagreement-Aware；MCM / PTM 长度与构词对称，服务段落排比；RFA / FAO 首尾呼应。
5. **首字母或词根与主名同源**：SMSTracker 的 SMF / SGI / DKF 都以 S 开头；Wave-Pose3D 的 SWGM / WPE / WMV / WPO / WDAD 都含 W；THERIS 的 TDIM / TSSM / TFM Loss 都从 Therm- 词根来；TriLite 的子模块叫 TriHead；CausalNet 的 CAB / CMPLM 都以 Causal 开头。
6. **隐喻延续**：SwiftTailor → PatternMaker / GarmentSewer；MeshRipple 的 ripple / frontier / root；SEGA 借认知科学"快 / 慢思考"双系统理论统一 CE / FR 模块。
7. **把批评前作的用词直接变成模块名**：MaterialMVP 的 MCAA。
8. **子模块不做双关，不抢主名的风头**。并非所有能缩写的概念都要正式命名。例外：值得单独被引用的子发明可以单独起名，例如 AEMG 内部的 Neuromuscular Contraction Tokenizer (NCT)。
9. **评估指标倾向不缩写**，名字直接等于定义（"average stray pixel count"）。
10. **风格可以二选一，但同一篇内要统一**：GaitMax 的子组件 CDLoss、GCaption 不共享词根，功能可读性优先于品牌一致性；ObjectRelator 的 MCFuse 与 XObjAlign 风格并不统一，属于好记优先于规则。
11. **避免字母汤**：模块太多、缩写套缩写会增加阅读负担（SeDiR 的 CFGT / C3L / GGD；《MoRel》的 ARBB 内含 GCA / KfA / PWD）。

### 5.2 数据集与基准

数据集和基准几乎都要起名，因为需要被反复引用和检索。常见写法：

1. **主名 + 规模数字**（效仿 ImageNet-1K，规模即卖点）：Derm1M（1,029,761）、SceneScribe-1M、DropletVideo-10M、OpenLVD200M、Ditto-1M、SceneSplat-7K、GenPoster-100K、EvalMi-50K、WMGStereo-150k、MicroMat-3K、NutritionSynth115K、CHTR-110K、ActiveViewPose-200K、VideoITG-40K、RelayFlow-4K、SpecTemp-80K、WorldLens-26K、I/Q-1M、GS-ScanNet40、TPC-268、THDR3K、MotionMillion。仿 LLM 的规模命名：PETAR-4B、PETARSeg-11K。
2. **用途词 + Bench / Eval**：AlbumBench、TGI-Bench、VS-Bench、GeoMMBench、ENC-Bench、InfiniBench、PAI-Bench、MemBench、R4D-Bench、RealAppliance-Bench、VL-RouterBench、OMG-Bench、MP-Bench（对应方法 MeteorPred）、GEOBench-VLM（领域 + Bench + 评测对象）、LVBench。缺点是辨识度低、容易撞名，只用通用后缀不够。
3. **其他身份后缀**：-Verse（GardenVerse、OLATverse，营造宏大感）、-Set / -Net 区分数据和方法（OpenDanceSet / OpenDanceNet，POLAR / POLARNet）、-Mix（FluoMix）、-X（Gastric-X）、-Fly（OccuFly）、-Net 沿用 ImageNet 惯例（VideoNet、3DReflecNet）。
4. **标明血缘**：在已有数据集名上加差异化定语，保留可追溯性：HR-MMSearch、SA1B-Matte、COCO-3D、PolarStanford-ORB、MP3DObject（Matterport3D + Object）、Dynamic RealEstate-10K、SegEarth-R2、UnrealCV+。
5. **把设备写进名字**，增强真实采集的说服力：FLIR-IISR。
6. **比方法名更口语化**："域词 + 具象名词"，例如 DentalProbe；也可以起可爱名（BiLiLo），或故意用无关的日常词加强记忆（FINER / FILTR 的配套基准叫 DONUT）。
7. **backronym 呼应数据主题**（数据与基准型里最受偏爱）：CHIRP、BioVITA、NABLA、SA-FARI、OMG-Bench。
8. **缩写读不通就用朴素描述名**：CARD、MV-Fashion、Gastric-X、RealAppliance、PETAR、SA-3DAO。好记的双关名是加分项，不是必需品。
9. 规则：规模后缀要和实际规模一致，缩写要有展开（反例：THDR3K 始终没有展开全称）。

### 5.3 家族化命名（一篇论文有多个产出时）

主方法、子模块、数据集、基准共享词根，读者只看名字就知道有"数据 + 方法"几条线。

1. **共享词根，只换角色后缀**：SpatialScore / SpatialCorpus / SpatialAgent；Copernicus-Pretrain / -FM / -Bench；WorldLens → WorldLens-26K → WorldLens-Agent；Wan-Weaver → WeaverBench；FluoCLIP ↔ FluoMix；FoleyDirector → DirectorSound → DirectorBench；SoccerMaster（模型）/ SoccerFactory（数据流水线）；BioVITATrain / BioVITAModel / BioVITABench；GeoMMBench / GeoMMAgent；CT-ScanGaze / CT-Searcher；OpenDance → OpenDanceSet / OpenDanceNet；PETAR → PETARSeg-11K / PETAR-4B；ArtHOI → ArtHOI-RGBD / ArtHOI-Wild；FGAesthetics（数据集）与 FGAesQ（模型）；MemFeed / MemCoach / MemBench；HUG-MVD / HUG-GR → HUG3D；Ditto ↔ Ditto-1M；RINO ↔ RINONet；SemVideo ↔ SemMiner；MeshFlow / MeshVAE / MeshRipple；UnionCut / UnionSeg；NeuraLeaf 与子资源 DeformLeaf；CineBrain → CineSync；Widget2Code → WidgetFactory；CHTR → G-HTR；Unified Motion Flow (UMF) ↔ P-Flow / S-Flow。
2. **共享字头或组成三件套**：F-Bench / FaceQ / F-Eval 共享 "F" 字头；CFD / CFM / CFR 是数据集-指标-方法三件套；4D-RGPT 家族（P4D / TPE / R4D-Bench）；GameFactory 的配套数据集 GF-Minecraft（方法缩写 + 场景名）。
3. **基础名 + 任务后缀**：AMB3R-VO / AMB3R-SfM；3PT-D / 3PT-R；PAI-Bench-G / -C / -U 用单字母区分赛道；AdaSpark → AdaS-Attn / AdaS-FFN；InfiniteYou → InfU → InfuseNet。
4. **方法论共性外显**：TokenGS / TokenLight / TokenSplat 都用 "Token" 表示"用可学习 token 统一表示"。
5. **变体用标签管理**：GECKO-Zero、KBAnat / KBAopt，不给每个变体重新取名。
6. 风险：家族越大，漂移风险越高；同一词根下的变体名要互相区分清楚（反例：OmniDocLayout-1M 与 OmniDocLayout-LLM 冲突）。子模块名也不要和主名形成近名（§4.4）。

### 5.4 现象、问题与概念的命名

规律：**发现新问题时用描述性短语或比喻；提出新方法时用缩写或专有名词**。给现象、根因、失效模式或洞察起一个 1–3 词的名字，便于全文反复指代，也让概念本身成为可被引用的名词。发现-解释型论文里，这个名字比方法名更早出场、更好记（§6.2）。

- **样本**：Inter-Category Entanglement (ICE)、manifold drift、label correlation drift、motion bias、rank collapse、attribute confusion、transfer collapse、background bias、baked-in shadow、containerization、backward contamination、semantic collapse、weak-independence、object recurrence prior、controversy space（Consensus vs. Controversy）、geo-guided amodal reasoning、Perfection Gap Factor（度量名）、Gradient Entanglement、The Invisible Gorilla Effect、Selective Amnesia（用"失忆症"统摄全文定位）、Vocabulary Scaling Law。
- **起名方式**：
  - 借经典实验或既有概念：The Invisible Gorilla Effect（借认知心理学实验）；Vocabulary Scaling Law（借 scaling law 的权威联想，并与方法 SVFT 分开命名）。
  - "X-as-Y" 结构让名字本身成为论点：Selection-as-Nonlinearity、Similarity-as-Evidence。
  - 新设定名 = 形容词 + 已有术语：Heterogeneous Incremental Learning；Inter-Photon-Limited 仿照 diffraction-limited。
  - 洞察名派生方法名：先定义 Selection-as-Nonlinearity (SaN)，再 "Guided by SaN, we introduce CSaN, …"。
- **引入句式**：
  1. "We define this phenomenon as Inter-Category Entanglement (ICE)—a state in which..."（SeDiR；"define" 全文只用这一次，用来标记正式命名）
  2. "…leading to what we refer to as manifold drift."（GeoRK2）
  3. "We observe/argue/hypothesize that X, a phenomenon we term Y."（The Invisible Gorilla Effect）；`a phenomenon we term [label correlation drift]`（FedHarmony）
  4. `[..], a phenomenon known as [命名].`（OSA）
  5. "We refer to these underexplored issues in X as Y (abbr)."（EAGC）
  6. "We address this problem using Y; we call this the X (ABBR) problem."（PfS）；`We term this the [X] challenge`（Selection-as-Nonlinearity）
  7. `At the heart of our solution is a key insight: [insight], which we call [term].`（Counting Stacked Objects，给洞察命名）；"…which we refer to as geo-guided amodal reasoning."（GROC，命名式洞察）
  8. "…which we refer to as Y in the remainder of this text."（术语约定）
- **规则**：
  - 比喻型现象名首次出现时加引号并给定义（"ghost points"、"crescent-shaped"、"surface noise"），之后作为专名直接使用。
  - 沿用前人术语时附引用编号，和本文原创术语区分。
  - 名字在摘要、引言、方法、实验中写法完全一样（与 §4.4 相同的一致性要求）。

---

## 6. 不同故事类型、不同方向的取名差异

### 6.1 按故事类型（1040 篇分布 → 推荐结构）

| 故事类型 | 占比 | 推荐标题结构 | 方法名倾向 | 样本依据 |
|---|---|---|---|---|
| 瓶颈突破型 | 56.0% | 结构 1 | 组合词或 backronym，副标题写"机制 for 任务" | *ChordEdit: One-Step Low-Energy Transport for Image Editing*；*LBM: ...* |
| 新问题定义型 | 11.0% | 结构 2（任务名即标题），或结构 1 | 新任务名本身就是名字 | *Multi-View 3D Point Tracking*；*Spatially-Varying Autofocus* |
| 统一框架型 | 10.8% | 结构 1，副标题带 Unified | 短名，常是单个真词或组合词 | *AToken: A Unified Tokenizer for Vision* |
| 发现-解释型 | 10.7% | 结构 3 / 5 / 6 / 8 | 常常不造名；造名时放在冒号后的副标题里 | *One Layer's Trash...*；*Mind the Gap...*；*When Pretty Isn't Useful...*；*What Do Visual Tokens Really Encode?*；*CLIP Is Shortsighted* |
| 数据与基准型 | 7.0% | 结构 1，Benchmark 或 Dataset 前置 | 名字里带规模或 Bench 后缀 | *WHU-MARS: A Multispectral Aerial-Ground Benchmark...*；*GEOBench-VLM: Benchmarking...*；OmniFood8K；PETARSeg-11K |
| 能力扩展型 | 2.4% | 结构 1，或者结构 7（Towards） | 延续谱系后缀，或加版本号 | *Towards Scalable Spatial Intelligence via 2D-to-3D Data Lifting* |
| 效率优化型 | 2.0% | 结构 1，副标题带 Efficient / Fast / One-Step / Training-Free | 可用 Eco、Swift 等带效率意味的特性词 | EcoSplat、SwiftTailor、*AnchorFlow: Training-Free...* |
| 理论分析型 | 0.2% | 结构 2 或 6 | 不造名 | *Rectifying Magnitude Neglect in Linear Attention*；*Is the Modality Gap a Bug or a Feature? A Robustness Perspective* |

说明：合并材料只明确指出钩子式标题"多见于发现-解释型"。表中其他行是按故事类型的产出形态对应过去的推荐，样本例证明这种写法存在，不代表那篇论文一定属于该故事类型。

按级别看，best 档（9 篇）、oral 档（195 篇）、highlight 档（836 篇）的故事类型分布都接近总体：瓶颈突破型分别占 55.6%、57.9%、55.5%。所以级别差异主要不在故事类型，而在标题风格：best 和 oral 档更常用纯描述式，highlight 档更常造缩写。

### 6.2 各故事类型的补充要点

以下按故事类型汇总各类型样本中的命名习惯，是对 §6.1 表格的展开。"降级"指什么时候放弃造名、改用纯描述。

**瓶颈突破型**
- 标题约七成是 `方法名: A/An + 形容词 + 名词 + for/via + 任务`。
- 名字点出洞察：backronym（CLAMP、ETCH、CURE、DUO = Dual Uncertainty Optimization、DisCoRD）或隐喻（Clay-to-Stone、MeshRipple、Midas Touch、LensWalk、Vector Prism）。
- 标题可以用反直觉断言或数字承诺（*Not All Frame Features Are Equal*、*FastGS ... in 100 Seconds*）。
- 两级命名：主名好记，子模块用能拼读的功能缩写（SET、ALR），数据集名直接报规模（DexGraspNet3.0）。
- 降级：理论或几何越重，包装越轻，用 "On the X of Y" 或纯描述标题。

**新问题定义型**
- 新设定和新缺陷要起概念名（§5.4）：Heterogeneous Incremental Learning、Inter-Photon-Limited、manifold drift、label correlation drift。
- 嵌入范式缩写，表明是对某范式的改造：ActiveAD、CF-VLA、U²Flow、U4D；BRICKGPT 暗示 next-brick 与 next-token 的类比。
- 把核心机制压缩成名字：LaRender、NullSwap、Snellcaster、Cog-Expo（cognition + exposure）；X2Y 映射：Widget2Code、CoTyle（Code-to-Style）。
- 组件名可以拟人化或用"形容词 + Driven/Aware"：Consensus-Driven / Disagreement-Aware（SAME、SSMDG）、"semantic bridge"（Scone）；task persona 分 donor / pirate / sponge / sieve 四类，让发现好记；反义文字游戏 KNOW / KNOWN。
- 数据集名 = 任务缩写 + 功能后缀或规模：SconeEval、VideoITG-40K、DRSeg。
- 标题用否定、反差或重构：*No Calibration, No Depth, No Problem*、*Too Vivid to Be Real?*、*Unstitching the Chimera*、*Beyond Walking*、Rethinking ...、口号式 *Heavy Labels Out!*。
- 核心规则：卖点是新任务本身时，朴素命名更显严谨（*Counting Stacked Objects*、度量名 Perfection Gap Factor）；卖点是系统时，才需要响亮的缩写或双关。

**统一框架型**
- 标题以 `短名: A Unified Framework for …` 为主，副标题首个形容词就是核心洞察。
- 把"统一"写进名字，名字与故事类型同构：Uni- 前缀（UniDxMD、UniPhys、UniLight、Uni3R）、*All in One*、*GT-Loc: Unifying When and Where…*、X Meets Y（*Global SfM Meets Feedforward Reconstruction*）。
- 用表示"粘合、两面"的 backronym：GLUEMAP、CoIn；其他与语义共振的 backronym：REFINE、TUNA、GRACE、RARE（用大小写标出取字位置）。
- 叙事化主标题：*Keep It Frozen*、*Reinforce to Learn, Elect to Reason*、*Mask to Align, Weight to Disambiguate*、*THE MORE, THE MERRIER*、*SpatialTree: How Spatial Intelligence Branches Out*。
- 名字可以还原成句：MTU3D = Move To Understand。
- 降级：偏理论或偏工程改进时用纯描述，服务精确检索，靠句首形容词点卖点（*Affine Perspective-Three-Point Problem*、*Spectral Conformal Risk Control*、*Portable Active Learning for Object Detection*）。

**发现-解释型**
- **给发现起名**，这个名字比方法名更早出场、更好记：借经典实验（*The Invisible Gorilla Effect*）、蹭既有概念（*Vocabulary Scaling Law*）、用 "as" 拼接两个概念（*Selection-as-Nonlinearity*）。
- 标题用设问、宣言、化用习语或对仗（§1.2 结构 3/5/6/8、§1.4）；"专名: 功能副标题" 也常见（*LitePT: Lighter Yet Stronger Point Transformer*、*RiskProp: Collision-Anchored...*）。
- 方法名：backronym（STAC、EAGC、IMAP ← *I'm a Map!*）；谐音（Bokehlicious、SpeciaRL、ReME、SeeKer）；致敬前作（TAM ← CAM、DIIP ← DIP；Object-DINO、GRPO-Guard、AVGGT）；子领域后缀（RALoc、CorrCLIP）；Ada- 前缀（AdaPrior、AdaSpark）；拟人或动作词（Guard、Miner、FixTalk，与标题 "Taming" 呼应）；隐喻贯穿（CATDiet、LumiMotion、TimeRipple）；数据集也可以起可爱名（BiLiLo）。
- 专名紧跟在洞察首次陈述之后 1–2 句内出场，在摘要、引言、结论中措辞一致。
- 降级：纯机制解剖、没有新方法、结论前置的纯实证论文，用纯描述标题，不起方法代号，让发现本身当卖点（*Scaling Laws for Native Multimodal Models*、*Mechanisms of Object Localization in Vision–Language Models*）。

**数据与基准型**
- 标题约 80% 是"专名 + 冒号 + 描述性副标题"（副标题写法见 §3.1）。另一路是整句做标题、资源名留到后文揭晓（§1.5）。
- 缩写恰好读成真词、和数据主题呼应最受偏爱（CHIRP、BioVITA、NABLA、SA-FARI、Hoi!、OMG-Bench）。
- **系列共享前缀是本类最一致的习惯**（§5.3）。
- 规模数字写进名字；-Bench / -Eval 辨识度低、容易撞名；-Net 沿用 ImageNet 惯例（§5.2）。
- 取名与论证配套：宣言式标题的论文在图注和结论里反复复现标题原句（GROC、SceneBench）；副标题写 Comprehensive / Large-Scale 的论文，正文依赖 Table 1 式横向对比。
- 降级：缩写读不通就用朴素描述名（CARD、MV-Fashion、Gastric-X、RealAppliance），或长标题（*Towards Foundational Models for Single-Chip Radar*）。

**能力扩展型**
- 标题范式高度统一：`[造词/缩写]: [描述性副标题]`（*OmniVGGT: Omni-Modality Driven...*、*Chorus: Multi-Teacher Pretraining...*、*gQIR: Generative Quanta Image Reconstruction*）。
- **继承式命名是本类首选**：前缀 + 知名基线名，把"在谁基础上扩展"焊进名字：OmniVGGT（VGGT）、PET-DINO（DINO）、STARFlow-V（STARFlow）、WildRayZer（RayZer）、PhysNAP（NAP）、OmniSAM（SAM）。
- 维度标签：Geo4D、4D Primitive-Mâché、STARFlow-V 的 "V"，把扩展维度焊进名字。
- 隐喻或拟人名与引言钩子互文：FoleyDirector、HouseCrafter、Chorus（合唱 = multi-teacher，与方法内核一致）、4D Primitive-Mâché、*Hearing the Room Through the Shape of the Drum*、LEGION；backronym：FEAT、MEDIC-AD。
- 纯技术缩写：ETN、SDUIE、gQIR、AutoOcc，多见于医学、水下、遥感等强调准确描述的方向。
- 不造词时两种子风格：谦逊式 "Towards..."（*Towards Generalized Multimodal Homography Estimation*）；主张式 "X are Y"，标题本身就是反差论断（*Visual Diffusion Models are Geometric Solvers*）。

**效率优化型**
- "速度隐喻 + 基座名"模板：Turbo-（Turbo-GS、TurboVSR，涡轮喻提速）、Swift-（SwiftTailor）、Delta-（DeltaTok / DeltaWorld，取"差量"的数学含义）；基座名沿用被改造的模型（Sparse-LaViDa、TE-VMamba、ResidualViT）。
- 借核心数学工具命名：VMonarch（Monarch matrix）；SLiM 双关"纤细 / 高效"；拼接造词强调融合：SigLino = SigLIP + DINO(v3)。
- 子模块用能读的首字母缩略词：DTPO、ARKD、BASS。
- 不起花名也常见：MEMFOF 由全称直接缩合成能读的词；*Real-Time Generation of Streamable Talking Portrait...* 全文没有方法简称。
- 标题玩梗（DeltaTok 的 "A Frame is Worth One Token"、TurboVSR 的 "Fantastic Video Upscalers and Where to Find Them"）只在方法已有好记简称时锦上添花。

**理论分析型**（仅 2 篇，规律仅供参考）
- 标题结构：`[简称] + 分隔符 + [全称] + via/for [机制或场景]`。
  - *C²FG: Control Classifier-Free Guidance via Score Discrepancy Analysis* = [简称]: [全称] via [方法机制]
  - *PLMP – Point-Line Minimal Problems for Projective SfM* = [简称] – [全称] for [应用场景]
- 借壳改写：C²FG 保留业内熟知的 CFG 作词根（见 §2.1 E），直接服务"站在巨人肩膀上做改进"的定位。
- 纯描述：PLMP 直接取研究对象四个关键词的首字母，不做双关，服务"严谨穷尽分类"的数学气质。
- 共同点：简称都能脱离全称独立读出，长度 4–5 个字符，方便后续文献直接引用。
- 理论越重，包装越轻；也可以用 "On the X of Y" 或纯描述标题。

### 6.3 按方向

**自动驾驶**（样本 48 篇，量少，只作倾向参考）
- 故事类型：瓶颈突破型 52.1%，**新问题定义型 18.8%**（总体为 11.0%），数据与基准型 10.4%（总体为 7.0%）。
- 取名习惯：
  - 风格工程化、直白，硬件或表示词直接写进名字：Radar、LiDAR、BEV。
  - 用 `-AD` 作品牌词根：ActiveAD。
  - 命名动词常见 dubbed：ScoreLiDAR。
  - 也有戏仿标题：*Lidar Waveforms are Worth 40x128x33 Words*。
- 执行：
  - 名字里保留传感器或表示词（LiDAR、Radar、BEV），前面加一个表示本文机制的前缀。
  - 新问题定义型比例高，任务或设定名要准确，可以直接作标题主干。
  - 数据集论文用 `X: A [传感器组合] Benchmark for [驾驶任务]`。

**具身智能**（样本 41 篇，量少，只作倾向参考）
- 故事类型：瓶颈突破型 56.1%，**统一框架型 17.1%**（总体为 10.8%），新问题定义型 12.2%。
- 取名习惯：
  - 偏爱 "Embodied" 这个标签。
  - 用 `-VLA` 作品牌词根：AVA-VLA。
  - 喜欢拟人化的能动动词作标题：*Go to Zero*、*Move to Understand a 3D Scene*。
- 执行：
  - 统一框架型比例高，副标题优先考虑 `A Unified ... for Embodied [任务]`。
  - 基于 VLA 的工作用 `[前缀]-VLA`。
  - 发现或能力类工作可以用"动词短语作标题"（Move to Understand ...），把智能体的行为写成标题。

**CV（通用视觉，950 篇，主体样本）**
- 故事类型：瓶颈突破型 56.2%，发现-解释型 11.1%，统一框架型 10.7%，新问题定义型 10.5%。
- 取名习惯：
  - 3D 重建和渲染最依赖谱系后缀（`-GS`、`-3R`）。
  - 通用架构用 `-Former`。
  - 视觉语言方向常把基座名嵌进名字：WikiCLIP、PanoLlama。
  - 生成和美学方向最常借典故：Lafite、Clair Obscur、Fresco、Bokehlicious。
  - 发现-解释型的钩子式、问句式、戏仿式标题几乎都出自 CV，例如 CLIP、LVLM、T2I 模型的分析工作。
- 执行：
  - 先判断有没有适用的谱系后缀，有就优先用。
  - 生成和编辑任务可以用意象名，但副标题必须把机制和任务写全。
  - 分析基础模型的工作，优先考虑结构 3、5、6、8。

---

## 7. 反面清单

下面每一条都来自样本中的真实反例。§2.3 的检查清单管"一个名字够不够好"，本节管"哪些做法一票否决"。

| # | 反面做法 | 反例 | 改法 |
|---|---|---|---|
| 1 | 硬凑缩写：从单词中间抠字母，或为了凑词把全称写得不通顺 | ESSENTIAL、CHROME、EXOTIC、MAGICIAN、GenErase、CROWn（Coset-fibRated micrO-local…）；CUPID 被评为硬解 | 换真词或换构造方式（§2.1 A 第 4 步） |
| 2 | 读不出来：辅音堆砌、多段连字符缩写 | SAC-GNC、HccePose(BF)、DOSFMVC、LRHDR、UWMCH、GOR-IS、AFoV-ERP、DC-CN、RR-DU、UPA-RFAS、MDCS-MoAME | 改成真词、组合词，或正文注明读法 |
| 3 | 字母汤：模块缩写过多，缩写里再套缩写；摘要里自造缩写过多，子模块缩写挤进摘要 | SeDiR 的 CFGT / C3L / GGD；《MoRel》的 ARBB 内含 GCA / KfA / PWD | 子模块留给正文；次要概念不正式命名（§5.1） |
| 4 | 撞名或近名：和已有术语、知名方法、同期工作重名；只用通用后缀；热门前缀扎堆 | PGA、SCORE；两个 RAVEN；FoleyDesigner 和 FoleyDirector；MoRe 与 MoRel 两篇独立论文都用 "Mo + 短后缀"；一批里 5 篇用 Omni-；只叫 XXBench | 检索"名字 + 领域词"，加一个表示卖点的词根 |
| 5 | 营销词或名字比证据响亮：用 Super / Ultra / Mega / Magic 类词（样本中没有）；名字承诺的范围超出实验 | 带 "Master"、"Magic" 的 SoccerMaster、MagicBokeh 恰好出现在结论强度偏高、套话多的论文里；《CAC》声称 "embodied AI" | 名字越响亮，正文越要克制；诙谐代号配克制措辞反而效果好（Matador） |
| 6 | 双关或隐喻和内容无关、和机制脱节 | LagerNVS；LegoOcc 的品牌名与 Method 正文脱节；Circuit Mechanisms 的"胚胎发育梯度"类比缺乏论证 | 名字里至少一个成分指向机制（§2.3） |
| 7 | 借势已有模型时仍然强行双关，读者看不出它继承自谁 | — | 写成"原名 + 前后缀"（§2.1 D） |
| 8 | 拼写错误进入名字或专名 | RhythmGuassian（Gaussian 拼错）、SpaitalAgent、MoGA 全称中的 "Moncular" | 定稿前逐个核对名字拼写 |
| 9 | 名字在标题、摘要、正文、图表之间不一致；标题造了词正文却不用 | 见 §4.4 的反例；Sparfels | 按 §4.4 逐项检查 |
| 10 | 缩写从不展开，或展开时机不一致 | TMFS、THDR3K；DreamShot 的 RACL | 摘要或引言中展开一次，之后只用缩写 |
| 11 | 过长的术语堆砌，标题很长却没有一个可引用的名字 | 137 个字符的标题 | 按 §1.3 决定造名或改用纯描述短标题 |
| 12 | 隐喻词重复到失去效果 | AD-GBC 连用三次 "catastrophic" 的同根词 | 隐喻点题一两次即可（AMB3R 的 "cornerstone" 只用一次） |

---

## 8. 取名流程

### 8.1 输入

写论文的 AI 助手在开始取名前，先从论文中提取以下 6 项：

1. **故事类型**：从 §6.1 的 8 类中选一类。
2. **核心机制**：用一个名词短语描述，比如 "latent bridge matching"。
3. **任务/场景**：比如 "image-to-image translation"。
4. **主卖点**：从 §3.2 中选一到两个高频词，并确认实验里能兑现。
5. **技术谱系**：确认是否建立在 3DGS、DUSt3R、VLA、Transformer、自家前作之上。
6. **方向**：自动驾驶、具身，还是 CV。

### 8.2 步骤

**第 1 步：选结构**。按 §1.3 的决策顺序确定标题结构。如果结果是结构 2，也要准备一个带名字的结构 1 版本作为对照。

**第 2 步：写副标题**。按 §3.1 的顺序写 `[卖点词] [核心机制] for [任务]`。写出两个版本，一个用 for 接任务，一个用 via 接手段。

**第 3 步：生成方法名候选**。每种适用的构造方式各产出一个，至少覆盖三种：
- A. backronym：写全称，再找首字母能拼出的、语义相关的真词。
- C. 组合词：特性词 + 领域词。
- D. 谱系后缀：前缀 + `-GS` / `-3R` / `-VLA` / `-AD` / `-Former`，只在确实属于该谱系时才用。
- 可选：B 谐音、E 数字符号、F 典故、G 描述性缩写。
- 先按 §2.4 看技术处境适合哪几种，按 §2.5 从洞察句里取词根。

**第 4 步：组合成 3–5 个完整标题候选**。至少包括：
- 默认格式 1 个；
- 一个换了构造方式的结构 1；
- 一个非结构 1 的版本（纯描述式，或故事类型允许时用钩子式）。

**第 5 步：逐项检查**。对每个候选跑一遍 §2.3 的 6 项清单和 §3.3 的 5 条禁忌，把结果填进表格；再对照 §7 的反面清单，命中任何一条就淘汰。

**第 6 步：挑选**。
1. 淘汰有任何一项不通过的候选。
2. 在剩下的候选里，按"和机制有关联 > 可还原 > 好读 > 好记"的优先级排序。
3. 如果论文属于新问题定义型或理论分析型，而纯描述式候选通过了全部检查，优先选纯描述式（总纲第 1 条）。

**第 7 步：写首次引入句**。按 §4.2 写摘要里的引入句，放在第 2–4 句。同位语里的性质词要和副标题一致。

**第 8 步：撞名自查**。在论文和代码检索里搜"名字 + 领域词"。发现同名或近名（参照 RAVEN、FoleyDesigner/FoleyDirector），就退回第 3 步。

**第 9 步：给其余产出命名**。按 §5 给子模块、数据集或基准、核心现象命名：子模块用功能直读的缩写，数据集与主名共享词根，现象起 1–3 词的专名。最后把所有名字写进术语表，按 §4.4 做一致性检查。

### 8.3 演示 1（虚构论文，仅用于演示流程）

**输入**：
- 故事类型：效率优化型。
- 核心机制：在前馈式 3D Gaussian Splatting 中，按视角可见性剪枝冗余高斯。
- 任务：从稀疏多视图图像做前馈 3D 重建。
- 主卖点：Efficient（高斯数量和显存大幅下降）。
- 谱系：3DGS。
- 方向：CV。

**第 1 步**：效率优化型，核心产出是一个模块，不是一个现象，贡献也不是单一名词短语就能说完，因此选结构 1。另备一个结构 2 作对照。

**第 2 步**：
- 版本 1：Visibility-Aware Gaussian Pruning for Efficient Feed-forward 3D Reconstruction
- 版本 2：Efficient Feed-forward 3D Gaussian Splatting via Visibility-Aware Pruning

**第 3 步**：
- A. backronym：全称 "Visibility-Informed Efficient Gaussian Splatting"，首字母是 VIEGS，拼不成真词。改为 "Pruning Redundant Unseen Gaussians for Efficient Splatting"，首字母 PRUGES，也不是真词，放弃 A。
- C. 组合词：Prune + Splat 得到 PruneSplat；Lean + Splat 得到 LeanSplat（Lean 暗示精简，和 EcoSplat 同一构造方式）。
- D. 谱系后缀：Vis + GS 得到 VisGS。

**第 4 步：候选**：
1. LeanSplat: Efficient Feed-forward 3D Gaussian Splatting via Visibility-Aware Pruning
2. PruneSplat: Visibility-Aware Gaussian Pruning for Efficient Feed-forward 3D Reconstruction
3. VisGS: Visibility-Aware Pruning for Efficient Feed-forward Gaussian Splatting
4. Visibility-Aware Pruning for Compact Feed-forward 3D Gaussian Splatting（结构 2）

**第 5 步：检查**：

| 候选 | 好读 | 好记 | 可还原 | 可搜索 | 不撞名 | 关联机制 | 备注 |
|---|---|---|---|---|---|---|---|
| LeanSplat | ✓ | ✓ | ✓（Lean 对应精简） | ✓ | 需检索 | ✓（精简 + Splat 谱系） | 构造方式同 EcoSplat |
| PruneSplat | ✓ | ✓ | ✓ | 风险："prune splat" 是通用词组，搜索时容易被淹没 | 需检索 | ✓ | 可搜索性偏弱 |
| VisGS | ✓ | ✓ | 一般（Vis 可以理解为 vision 或 visibility） | 风险：歧义 | 需检索 | ✓ | 可还原性不通过 |
| 纯描述式 | ✓ | ✗（没有简称，引用时不方便） | — | ✓ | ✓ | ✓ | 这是模块型贡献，不符合"不造名"的条件 |

**第 6 步**：VisGS 在可还原项上不通过，被淘汰。LeanSplat 和 PruneSplat 都能保留，LeanSplat 更好搜、意象更好，选 **LeanSplat: Efficient Feed-forward 3D Gaussian Splatting via Visibility-Aware Pruning**。

**第 7 步：摘要第 2–3 句的引入**：
> "We introduce LeanSplat, an efficient feed-forward 3D Gaussian Splatting framework that prunes redundant Gaussians according to their cross-view visibility."

同位语里的 "efficient" 和副标题的 Efficient 对应。

**第 8 步**：检索 "LeanSplat Gaussian"。如果已有同名工作，就退回备选 PruneSplat。

### 8.4 演示 2（虚构论文，仅用于演示流程）

**输入**：
- 故事类型：发现-解释型。
- 核心发现：多传感器 BEV 检测模型在雨雾天气下，几乎不利用 Radar 分支，性能几乎全部来自相机和 LiDAR。
- 核心机制：提出一种按天气重新分配模态权重的训练策略来修复这个问题。
- 任务：恶劣天气下的 3D 目标检测。
- 主卖点：Robust。
- 谱系：BEV 融合。
- 方向：自动驾驶。

**第 1 步**：发现-解释型，核心产出首先是一个现象，走结构 3、5、6、8。
- 现象有反差：Radar 恰恰是为恶劣天气准备的，却在恶劣天气下被忽略，适合结构 5（When）。
- 现象可以归结成一个是非问题：适合结构 6。
- 也准备一个结构 1 版本，以防修复方法才是主贡献。

**第 2 步：副标题**：
- 分析型：Revealing Radar Neglect in Multi-Sensor BEV Detection
- 方法型：Weather-Adaptive Modality Reweighting for Robust BEV Detection

**第 3 步：方法名**：
- 组合词：Radar 是领域硬件词，可以直接写进名字，得到 RadarWake（唤醒被忽略的 Radar）。
- 谱系后缀：Rain + AD 得到 RainAD，参照 ActiveAD 的构造方式。

**第 4 步：候选**：
1. When Radar Goes Silent: Revealing Modality Neglect in Multi-Sensor BEV Detection under Adverse Weather（结构 5）
2. Does BEV Fusion Really Use Radar in Bad Weather?（结构 6，参照 *Does YOLO Really Need to See Every Training Image in Every Epoch?*）
3. RadarWake: Weather-Adaptive Modality Reweighting for Robust BEV Detection（结构 1）
4. RainAD: Robust Multi-Sensor BEV Detection via Weather-Adaptive Modality Reweighting（结构 1）

**第 5 步：检查**：

| 候选 | 好读 | 好记 | 可还原 | 可搜索 | 不撞名 | 关联机制 | 备注 |
|---|---|---|---|---|---|---|---|
| 1 When Radar Goes Silent | ✓ | ✓ | — | ✓ | ✓ | ✓（发现和对象都在标题里） | 冒号后有任务、对象和条件 |
| 2 问句 | ✓ | ✓ | — | ✓ | ✓ | 只讲了现象，没提修复方法 | 适合纯分析论文 |
| 3 RadarWake | ✓ | ✓ | ✓ | ✓ | 需检索 | ✓ | 标题里没有体现"发现" |
| 4 RainAD | ✓ | ✓ | 一般（-AD 常被理解为端到端驾驶系统，本文只做检测） | 需检索 | 需检索 | 谱系误导 | 不通过：只有属于该谱系时才能用这个后缀 |

**第 6 步**：RainAD 因谱系误导被淘汰。故事类型是发现-解释型，发现是主贡献、修复方法是次要贡献，所以选 **候选 1**。修复方法在正文里用 RadarWake 命名，作为次级名字。

**第 7 步：摘要引入**：
- 按 §4.2 的变体 3，摘要首句不宣布名字，先陈述发现。
- 在"方法"位置（第 2/5 段）写：
> "Building on this finding, we propose RadarWake, a weather-adaptive modality reweighting strategy that restores the contribution of radar under adverse weather."

**第 8 步**：分别检索标题关键短语 "Radar Goes Silent" 和名字 "RadarWake"，都没有冲突后再定稿。

---

## 附：最终输出前的速查清单

- [ ] 已按 §1.3 判断过：这篇论文需不需要造名。
- [ ] 标题结构和故事类型匹配（§6.1、§6.2）。
- [ ] 方法名通过 §2.3 的 6 项检查，没有命中 §7 的反面清单。
- [ ] 副标题的顺序是"性质词 + 机制 + for/via + 任务"；数据集和基准类的顺序是"任务/Benchmark 前置"。
- [ ] 副标题的高频词不超过两个，并且每个都有对应的实验兑现。
- [ ] 方法名在摘要第 2–4 句用 propose / introduce / present 引入，同位语和副标题的用词一致。
- [ ] 全文名称的拼写、大小写和符号一致；子模块名不和主名形成近名。
- [ ] 已检索撞名，包括领域术语和同期工作。
- [ ] 子模块、数据集、核心现象已按 §5 命名：子模块功能直读，数据集与主名共享词根，现象有专名。
