# Related Work（相关工作）写作规范

> **读者**：正在替用户写 Related Work 一节的 AI 助手。照着本文件写，写完用第 5 节的清单逐条自查。
>
> **数据来源**：CVPR 2026 + ICCV 2025 共 1040 篇精读笔记（Oral 195、Highlight 836、Best 9）。本章内容来自三份跨批次的"Related Work 写法"汇总，以及 `story_types.md` 各类型章节里与文献定位有关的条目。`references/corpus_stats.md` 里没有本章的专门统计（例如分组数、放在第几节的比例），下面说的"绝大多数""少数"都是汇总材料里的定性判断，不要当精确数字写进论文。
>
> **合并说明**：旧版 `sections/related_work.md` 的要求全部保留：按主题或技术路线分组、每组一段；段首概括共同思路、段尾说明区别；不写成 "A did X. B did Y." 式罗列，而是组织成指向缺口的论证链；比较写清假设、设定或代价上的差别；最接近的 1–3 篇单独比较；只引用 `.bib` 中已有的条目，描述要能在 `.paperdna/refs/` 笔记或用户提供的信息里找到依据，拿不准时标 `% TODO: verify`。`story_types.md` §3.4（方法）、§3.5（实验）、§3.6（局限与结论）的主体分别归 `sections/method.md`、`sections/experiments.md`、`sections/conclusion.md`；本文件只取其中与本章接口有关的四条：方法小节开头要交代遗留问题，所以 Related Work 末句要把问题交到方法手里（§3.6）；"首个框架"类声明必须有独立验证，所以对比表的每一列都要有实验兑现（§3.4）；局限要写成"失效场景 + 根因 + 方向"，这一要求同样用于描述前人工作的局限（§3.2）；本文自己的局限不要前置到 Related Work 里当反衬（§4）。"先直觉后公式"用于 Related Work 兼做背景铺垫的情形（§3.7）。
>
> **相关文件**：分组名、缺口名、方法名的取法和全文措辞统一见 `references/naming.md`；"first""novel""significantly"等词的用法和结论强度见 `references/word_style.md`。本文件不重复这些内容。
>
> 书名号《》里是真实论文标题或方法名；标注出处的英文句子是论文原句，X / Y / Z 是占位符。

---

## 0. 速查

| 事项 | 默认做法 | 依据 |
|---|---|---|
| 位置 | 第 2 节，紧跟引言 | 三份汇总一致：绝大多数论文放第 2 节，多个批次"无例外"。后置只在 §2.3 列的几种情况下用 |
| 分组维度 | 按**技术路线 / 子领域**分 2–4 组，每组一个小标题 | 三份汇总的"最稳定共性"。《SAM 3D》多视角重建 / 单视角生成式重建 / layout 估计；《FlowR》Geometric priors / Feed-forward methods / Generative priors |
| 何时改按本文维度分组 | 引言已经列出 2–3 条并列挑战或贡献，且每条都有独立文献群时，让小节与之一一对应 | 《PhysGM》三个子节对应引言三条局限；《AAA-Gaussians》三类伪影对应 3.2/3.3/3.4 |
| 每组段落结构 | 段首一句共同思路 → 代表作与具体差别 → 共性局限 → 段末一句定位本文 | 旧版规范；三份汇总的"三段式 + 显式对比句收束" |
| 定位句位置 | 默认每组末尾各一句（分散式）；组少、差别集中时可整节末尾统一收束一次 | 第 1 份汇总 §二 |
| 最接近的工作 | 1–3 篇单独点名，逐点写差别，必要时单开一段或一个小节 | 《Retrieve and Segment》"Closely related to our work is kNN-CLIP [18], but..."；《M2SFormer》专设 "Our approach" 小节 |
| 对比表 | 首创性或"能力覆盖更全"的声明，用一张能力 / 设定对比表坐实 | 《D4RT》Tab.2、《GeoMMBench》Table 1、《AD-GBC》Table 1、《GeoAgent》Tab.1 |
| 与引言的分工 | 引言给定性缺口判断，Related Work 用具体文献坐实、细化；不复述引言句子 | 《CARE》用 HIPT、ABMIL、CHIEF、TITAN 坐实引言 "existing region chunking remains crude" |
| 组间衔接 | 每组开头或上组末尾有过渡；不能只靠小标题硬切 | 三份汇总里出现频率最高的问题，点名论文 30 余篇 |
| 末句 | 交给方法："This limitation motivates our design of ..." / "We propose X to overcome these bottlenecks" | 《LVFace》《PhysGM》 |
| 篇幅不够 | 正文只留最相关文献，完整讨论放附录，并在开头一句说明 | 《ChordEdit》《Guiding a Diffusion Transformer with the Internal Dynamics of Itself》 |
| 引用 | 只用 `.bib` 已有条目；对前作的描述要有依据，拿不准标 `% TODO: verify` | 旧版规范 |

---

## 1. 这一章要完成什么，与其他章节的分工

### 1.1 四个任务

1. **划出坐标系**：把相关文献分成 2–4 条脉络，让读者知道本文站在哪条（或哪几条的交叉处）。例：《MeshSplatting》立于"可微渲染显式表示的演化"与"从图像重建网格"的交叉点；《GLINT》用 3DGS / 辐射分解 / 透明重建三组论证"分解式辐射传输"是未解决的交叉空白。
2. **坐实缺口**：引言里说"现有方法在 X 上失效"，这里用逐篇文献证明这句话成立。例：《RawMetaDiff》引言泛泛批评 "existing methods"，Related Work 末句点名 LSFNet、LSD2；《GEOBench-VLM》引言说 benchmark 不全面，第 2 节用 Table 1 量化坐实。
3. **划清边界**：对最接近的工作说清"看起来像，但不同在哪里"。例：《DiffPS》专段写 "Although DiffPS may appear conceptually similar to DMRNet [17]..., it fundamentally differs by..."。
4. **把问题交给方法**：最后一句留下一个方法要回答的问题，方法节第一句接住它（`story_types.md` §3.4 要求方法小节开头重述遗留问题）。

### 1.2 与其他章节的分工

| 章节 | 它负责的 | 本章不要做的 | 本章要呼应的 |
|---|---|---|---|
| 引言 | 定性的缺口判断、根因、洞察、贡献列表 | 不重复任务定义，不复述引言的评述句（反例：《BeautyGRPO》《ComPose》2.1 节再次给出任务定义；《FastGS》《Editprint》开篇几乎逐字复述引言） | 引言点过的根因名、缺口名（措辞一致，见 `naming.md`）；引言提到的前作要在这里展开 |
| Preliminary / Background | 符号、基础公式 | 不要在综述段里夹大段公式，除非有意合并（§3.7） | 如果合并，给出的符号要被方法节复用 |
| 方法 | 本文怎么做 | 不提前展开本文的模块细节 | 末句交出问题，方法首句接住 |
| 实验 | 与前作的数值比较 | 不在这里报本文的实验数字（少数论文预告结果，如《GECKO》"significantly outperforms Intra and matches TANGLE"，只在结果本身就是定位依据时用） | 这里点名的最接近工作，实验里要作为基线出现 |
| Limitations | 本文的失效场景 | 不把本文的局限前置到这里当反衬（反例：《Automated Model Evaluation for Object Detection》整节批评 BoS 三点局限） | — |
| 附录 | 完整文献讨论 | — | 正文开头说明"完整讨论见附录" |

### 1.3 与实现一致

- 写"Unlike X, our method does Y"之前，确认方法和代码里确实做了 Y，而且 X 确实没做（查 `.paperdna/refs/` 笔记或原文）。差别写错比不写更伤。
- 对前作局限的描述要具体到假设、设定或代价，和 `story_types.md` §3.6 对本文局限的要求一样：写"在什么场景失效、因为什么"。例：《ForestFormer3D》直接批评 ForAINet "tends to over-segment trees...fails to accurately identify small trees"；《EcoSplat》点明前作 "provide neither explicit control...nor a guaranteed, optimal trade-off"。
- 用 "first" / "unique" / "unexplored" 的声明，必须有检索依据，并在实验里有独立验证（`story_types.md` §3.5）；强度把握见 `word_style.md`。

---

## 2. 组织方式：常见结构及适用场景

### 2.1 六种常见结构

| 结构 | 做法 | 适用场景 | 例 |
|---|---|---|---|
| **A. 技术路线并列（默认）** | 2–4 条并列脉络，脉络内再按局限或时间排序 | 大多数情况 | 《SAM 3D》；《Ov3R》3D Reconstruction（Offline/SLAM/3R-driven）+ 3D Semantics（Closed-Vocab/Open-Vocab）；《EDM》Sparse/Dense/Semi-Dense；《RawMetaDiff》单帧低光增强 / 双曝光融合 / 扩散式修复 |
| **B. 通用 → 细分收窄** | 从大领域逐层收到本文的具体设定 | 本文的设定是某个大任务的特殊子问题 | 《GROC》通用计数 → 遥感计数 → 多模态计数；《SGAD》经典特征匹配 → 多阶段匹配 → Area-to-Point 匹配；《Fast Globally Optimal 3D Shape Matching》可高效求解的匹配问题 → 3D 形状匹配 → 几何一致的 3D 形状匹配 |
| **C. 对齐本文贡献 / 挑战** | 每个小节对应引言的一条挑战或贡献，段末用 "Our X ..." 收尾 | 引言有编号的 2–3 条挑战，且每条有独立文献群 | 《PhysGM》；《MATLAT》2.1/2.2/2.3 对应引言 "two key challenges"；《Towards a Unified Copernicus Foundation Model》数据集 / 模型 / 基准对应三条局限；《HairCUP》《Corvid》《CasP》；《MacTok》三主题恰好对应方法三组件 |
| **D. 编年体** | 按时间线讲一条技术的演进 | 本文是某条技术线的下一步 | 《MoGA》2.1 节 PIFu → 2D 扩散 → 多视图扩散 → SMPL 正则化；《2D-LFM》"We trace this evolution to identify the core tradeoff that motivates our approach." |
| **E. 数据集综述 + 方法综述** | 两条线分别坐实"数据缺口"和"方法局限"，常配对比表 | 数据与基准型 | 《M3DLayout》《MV-Fashion》《ENC-Bench》；《SceneScribe-1M》Table 1 对比十余个数据集 |
| **F. 精确定位** | 不做泛综述，只对比一两篇最相关工作 | 工作是对某篇前作的直接改进，或问题很窄 | 《Consensus vs. Controversy》只对比 Meding et al. 和 Conwell et al. |

**选择规则**
1. 默认用 A。组数 2–4，组名用技术路线名，不用"Other methods"。
2. 引言里已经有编号挑战 (i)(ii)(iii)，且每条挑战都能找到 3 篇以上文献，就用 C，让小节顺序与引言顺序一致（《SinGeo》的三个小节顺序就对应引言问题展开的顺序）。
3. 本文是某个子设定上的工作，用 B；每收窄一层，都要说明上一层的方法为什么不能直接搬过来。
4. 数据与基准型用 E，并配一张对比表。
5. 可以组合：A 或 B 之后，再单开一段或一个小节写最接近的工作（《M2SFormer》三条路线外专设第 4 小节 "Our approach"）。
6. 各组详略要大致相当。核心组展开、边缘组一笔带过会显得不均（反例：《MedLIME》《MeshRipple》《OMG-Bench》《NI-Tex》）。边缘组确实不重要，就并进其他组或移到附录。

### 2.2 按故事类型的差异

以下按材料中出现的例子归类。故事类型的判断见 `story_types.md` §2。

| 故事类型 | Related Work 的重点 | 例 |
|---|---|---|
| 瓶颈突破型 | 结构 A；每组末句指出这组方法共有的瓶颈，最好与引言的根因同名。工作是对某篇前作的直接改进时（"继承者叙事"），可以只对最近的前作做机制级逐点批评 | 《Dual-level Adapter》三条线落脚同一根因；《E-RayZer》引用 RayZer 自己的 Tab.7 |
| 新问题定义型 | 用文献坐实"这个问题没人正视"或"默认假设不成立"；定位句多用空白收束型或反驳假设型 | 《LOREAL》"...remains unexplored."；《Rounded or Streamlined Head》"our experiments reveal this assumption to be fragile"；《AdvDreamer Unveils》开篇 "In contrast to previous works, our study specifically investigates..." |
| 统一框架型 | 两条或多条被割裂的脉络各写一组，最后说明本文把它们合起来；常配能力对比表 | 《Ov3R》双线；《D4RT》前馈 3D 重建 + 2D 到 3D 点跟踪，"In contrast, our approach unifies these tasks within a single architecture." 并附 Tab.2；《Circuit Mechanisms》"Our work is unique in that we unite these two views" |
| 发现-解释型 | 可以后置到发现之后；可以按"问题成因 / 效果 / 消除方法"分组；末尾可给出本文要证明的命题 | 《Is the Modality Gap a Bug or a Feature?》三分法 + 末尾给命题；《Mechanisms of Object Localization in VLMs》放第 4 节；《What Do Visual Tokens Really Encode?》放第 8 节 |
| 数据与基准型 | 结构 E + 对比表；每类数据集写清优劣如何影响本文的设计，不只列清单 | 《GeoMMBench》Table 1；《AnimalClue》Table 1 以"通用识别 + 五类痕迹"分组；《GEOBench-VLM》 |
| 能力扩展型 | 点名被扩展的前作或基座，引用它自己的局限原句，再说本文往哪个维度扩展 | 《Anatomica》整段引用并反驳 Kadry et al.[30] "was limited to globally defined..."；《Point4Cast》"Unlike these approaches, our method can also predict 3D pointmaps of the scene for unseen future timesteps." |
| 效率优化型 | 定位句写清前作在效率与质量或可控性之间的取舍 | 《EcoSplat》"Despite of their advancements in efficient rendering, the aforementioned approaches provide neither explicit control...nor a guaranteed, optimal trade-off..." |
| 理论分析型 | 需要先统一记号时，可先 Preliminaries 或后置 Related Work | 《Spherical Leech Quantization》(Λ24-SQ) 放第 6 节；《TUNA》先证明后综述，放第 4 节 |

### 2.3 位置

- **默认第 2 节**。
- **后置到实验之后、结论之前**：适合要先亮出实证发现或完整方法体系，才能反衬前人工作的论文。例：《SAM 3D》第 5 节、《NitroGen》第 5 节（在 Limitations 之后）、《SANA-Sprint》《SummDiff》第 5 节、《CT-ScanGaze》第 6 节、《VeriDou》第 6 节、《Confusion-Aware Spectral Regularizer》第 7 节。后置时要写开头过渡句，反例是《Straighten Viscous Rectified Flow》，与实验章节间无过渡，结构突兀。
- **Preliminaries 在前**：方法依赖的数学工具需要先建立时用。《WINS》先设 Preliminary（Sec.2）再做 Related Work（Sec.3）；《CLaD》先在 2.1/2.2 补扩散模型公式记号；《Exemplar-Free Continual Learning for SSM》因为要先建立 Grassmann 流形工具，把 Related Work 挪到方法之后。风险：综述开头与 Preliminaries 结尾重复（反例：《Learning Visual Hierarchies in Hyperbolic Space》）。
- **正文极简 + 附录完整**：篇幅紧时用，开头一句说明（§3.1）。

---

## 3. 逐部分写法

### 3.1 开篇句：承接引言，说明这一节要找什么

写法：一句话说明这一节沿什么线索回顾、要论证什么，最好承接引言的最后一个论点。不要写成"本节回顾相关工作"。

- "We trace this evolution to identify the core tradeoff that motivates our approach."（《2D-LFM》，承接引言末句 "Our work revives this principle within scalable architectures"）
- "In contrast to previous works, our study specifically investigates..., addressing a crucial gap..."（《AdvDreamer Unveils》，开篇即定位）
- "We discuss with the most relevant literature here and provide a more discussion in Supplementary Material."（《Guiding a Diffusion Transformer with the Internal Dynamics of Itself》）
- "We provide a full discussion of related work in the Appendix."（《ChordEdit》，正文只做极简归类）

反例："In this section, we review related works that focus on accelerating both the training and inference of 3DGS"（《FastGS》，复述引言，没有论点）；《RAVEN》用综述式总起句直接切入，与引言没有衔接。

也可以不写总起句，直接进入第一个小节，但那时第一个小节的段首句要承担这个作用。

### 3.2 每组的段落：共同思路 → 代表作与差别 → 共性局限 → 定位句

**(1) 段首句：概括这组工作的共同思路。** 写成一句有主语的判断，而不是 "Many works have studied X [1-10]."

- "In the field of 3DGS [11,22,32], joint optimization methods can be categorized into two types."（《Energy-GS》，先给这组内部的分类）
- 通用模板："A line of work [a, b, c] addresses X by Y."

**(2) 代表作：按局限或时间排序，写清差别在哪里。** 每篇或每小组配一个具体特征（假设、输入、监督方式、代价），不要 "A did X. B did Y. C did Z."。一组 3–6 篇代表作即可，不追求全。

**(3) 共性局限：写到机制或假设层。** 和写本文局限一样具体：在什么场景失效，因为什么。
- "most existing methods adopt a local view, treating concepts as isolated entities"（《GrOCE》，重申并展开引言论断）
- "existing methods generally treat the attention map as a whole..."（《ReAttnCLIP》，末句重申，直接过渡到方法拆解）
- "However, these methods often assume class-agnostic grounding to be reliable; our experiments reveal this assumption to be fragile, motivating..."（《Rounded or Streamlined Head》，指出隐含假设并反驳）

**(4) 段末定位句：一句话钉住本文。** 按想强调的东西选句式：

| 类型 | 何时用 | 原句（出处） |
|---|---|---|
| 差异对比 | 本文与这组方法在做法上有明确不同 | "In contrast, our approach unifies these tasks within a single architecture."（《D4RT》）<br>"Unlike these approaches, MODIX requires no retraining..."（《MODIX》）<br>"In contrast, we propose using the curve sketch to construct a dual-region mask..."（《MOFA-VTON》）<br>"Our work departs from these RL-based methods by shifting the optimization paradigm from pairwise to sequence-level supervision..."（《From Pairs to Sequences》） |
| 让步转折 | 前作有进展，但缺了本文要的那个性质 | "Despite of their advancements in efficient rendering, the aforementioned approaches provide neither explicit control...nor a guaranteed, optimal trade-off..."（《EcoSplat》）<br>"While our method is also learning-based, it is an end-to-end feed-forward framework..."（《Electromagnetic Inverse Scattering》）<br>"Our work falls into the category of event-only 3DGS methods...however, with several significant differences"（《Geometric-Photometric Event-based 3DGS Ray Tracing》） |
| 空白收束 | 这组方法都没碰本文的设定 | "None tackle asymmetric local feature matching."（《AsymLoc》）<br>"Despite these advancements, addressing the LR challenge through prompt learning for VLMs remains unexplored."（《LOREAL》）<br>"none of the existing methods effectively regulate the scope of patch interactions"（《CorrCLIP》） |
| 缺口坐实 | 引言已命名缺口，这里回指 | "This is precisely the gap our method aims to bridge."（《BEA-GS》）<br>"Our work fills this gap by introducing a conditional Diffusion model as a generative illumination prior."（《IR-HGP》）<br>"This highlights the need for disentangling category-specific semantics while preserving geometric consistency—a challenge our method directly addresses."（《SeDiR》）<br>"Our work aims to bridge this gap by achieving fine-grained motion fidelity with real-time generation efficiency."（《Real-Time Generation of Streamable Talking Portrait》） |
| 首创 / 唯一 | 有检索依据支持本文是第一个 | "To the best of our knowledge, this is the first work to leverage Q-Former for feature disentanglement."（《DisenQ》）<br>"To our knowledge, UnReflectAnything is the first work to combine monocular geometry, Fresnel-aware specular rendering, and randomized lighting..."（《UnReflectAnything》）<br>"Departing from prior works that address siloed aspects of personalization for MLLMs...we introduce PersonaVLM..."（《PersonaVLM》） |
| 互补 / 继承 | 本文与这组方法不冲突，而是补充或沿用 | "Our work complements.../bridges.../follows..."（《Scaling Language-Free Visual Representation Learning》）<br>"following the vanilla VLA GO-1 [10], we adopt this manner"（《AT-VLA》） |
| 直接引出方法 | 这组是最后一组，或定位句要落到具体设计 | "To address this, we design a cross-view distillation and adaptive masking strategy"（《Cross-View Distillation》）<br>"We therefore propose two a posteriori solutions, RaTE and MapReduce LoRA, to address reward conflict."（《MapReduce LoRA》）<br>"In this paper, we address this limitation by replacing self-attention with convolutions..."（《EDM》） |

写定位句时注意：
- 定位句要说本文**做了什么不同的事**，不要只说"我们更好"。
- 首创句用一次就够，多处重复 "first" 会显得用力过猛（反例：《FILTR》）；强度把握见 `word_style.md`。
- 多组都用同一个句式会显得僵硬（§3.8）。

### 3.3 最接近的工作：单独点名，逐点区分

最接近的 1–3 篇要单独拿出来比（旧版规范），做法是"缩小包围圈"：先说这组方法整体的局限，再点名最接近的一篇，说它看起来解决了问题，最后说它实际关注的是另一件事或另一个设定。

- "Closely related to our work is kNN-CLIP [18], but..."（《Retrieve and Segment》）
- "Closest to our work are LightLab [41] and..."（《TokenLight》）；"Closest to our approach, ADOP's [25]..."（《PPISP》）
- "The method most directly aimed at content and style separation is B-LoRA [6]"（《UnZipLoRA》）
- "Closer to our setting are the works in [15, 77]..."（《Beyond Losses Reweighting》，接着拆解它们实际关注灾难性遗忘而非 MTL 泛化，所以仍然不同）
- "This work is more related to this later paradigm, but involves learning with virtual knowledge in a different context...and for a different problem."（《VRM》）
- "Our method differs from Geo4D in two aspects."（《MotionCrafter》，先报差别条数再逐条写）
- "Although DiffPS may appear conceptually similar to DMRNet [17]..., it fundamentally differs by..."（《DiffPS》，预先回应审稿人的"这不就是 X 吗"）

排版：差别有 2–3 条时，可以像《FINER》那样在段末用三点列表总结区别；差别更多或最接近工作本身就是一个方向时，可以单开小节（《M2SFormer》"Our approach"）。能力扩展型要引用被扩展前作自己的局限原句（《Anatomica》）。

这里点名的工作，实验里要作为基线出现；如果无法比较（代码未开源、设定不同），在实验节说明原因。

### 3.4 对比表：用表坐实首创或覆盖面

当定位的要点是"本文同时具备 A、B、C 三个性质，而前作各缺一两个"，或"本数据集在规模、标注类型上覆盖更全"时，一张表比三段文字更有说服力。

- 能力对比：《D4RT》Tab.2；《GeoAgent》Tab.1；《AD-GBC》Table 1。
- 数据集 / 基准对比：《GeoMMBench》Table 1；《SceneScribe-1M》Table 1（十余个数据集）；《AnimalClue》Table 1；《GEOBench-VLM》。

做法：
1. 行是最接近的 5–10 篇工作加上本文，列是本文贡献声明里的性质或设定（输入模态、是否前馈、是否需要逐场景优化、标注类型、规模等）。
2. 列名与引言贡献列表的措辞一致。
3. 每一列都要在实验里有独立验证（`story_types.md` §3.5）；表里打勾的性质，文字和实验不能与之矛盾。
4. 表后用一两句话读表，不要只放表（反例：《LMM4LMM》复述同一张表格和数字，属于重复）。

### 3.5 组间衔接：显式过渡或术语复现

"小标题硬切"是三份汇总里出现最多的问题。两种修法：

- **显式过渡句**：在下一组开头说明为什么要看这组，或它与上一组的关系。可用 "A second thread of research..." / "In parallel, several recent works..."（《Mechanisms of Object Localization in VLMs》用这类短语分组；汇总指出它仍缺一句说明两条线关系的话，写时要补上）。
- **术语复现**：让同一个根因名或缺口名出现在每组末句，读者自然知道各组在围绕同一个问题展开。例：《FluoCLIP》"stain-dependent" 在 2.1、2.2 两小节末句都出现；《HieraMamba》靠 "AMP"、对比目标等关键词复现做隐性过渡；《Dual-level Adapter》三条线都落脚同一根因。

术语复现要求术语本身已经在引言里定名（见 `naming.md`）。

### 3.6 收尾：把问题交给方法

整节最后一句（或最后一组的定位句）要留下一个方法节会回答的问题，方法节第一句接住它。

- "We propose PhysGM to overcome these bottlenecks"（《PhysGM》，这句直接变成 Method 开头主语，衔接无缝）
- "This limitation motivates our design of learning dynamics that explicitly stabilize ViT training through progressive optimization."（《LVFace》）
- "To address these issues, we introduce two key designs."（《GFPack++》，衔接进方法部分）
- "we observe that both paradigms generalize poorly on driving-related OVDG-SS tasks, which motivates us to develop a more robust framework"（《OVDG-SS》/S2-Corr）
- 发现-解释型可以在末尾直接给出本文要证明的命题，充当引言与方法之间的桥（《Is the Modality Gap a Bug or a Feature?》）。
- 后置到文末时，末句可以收束全文贡献："In this paper, we provide further evidence that visual embeddings have been partially aligned with the language model's input embedding space via EmbedLens."（《What Do Visual Tokens Really Encode?》）

末句也可以重新引用引言的 Figure 1 加强论点（《Cov2Pose》末段）。

### 3.7 兼做背景铺垫时：先直觉后公式

方法建立在某个基座模型或数学工具上时，Related Work 可以兼做背景：
- 合并小节："Related Work and Background"（《Cov2Pose》）；"Prior Work and Preliminaries"（《Gated KalmaNet》）。
- 在综述里直接给出基座的符号：《Dark3R》2.1 节给出 MASt3R 的符号体系（Eq.1–3），供第 3 节复用。
- 或在 Related Work 与 Method 之间单独插一节 Preliminary/Background，形成"综述 → 形式化 → 方法"的桥（《OralGPT-Plus》《PoseD-Flow》）。

写法要求：
1. 先用一句话说明为什么要引入这些符号（本文在哪一步用到），再给公式，公式后补一句物理含义（`story_types.md` §3.4 "动机句 → 公式 → 物理含义句"）。
2. 这里定义的每个符号都要在方法节被使用，符号与方法节一致（`word_style.md` 原则 3）。
3. 不写与本文无关的教科书式定义（反例：《Dataset Distillation via VLM》的 Preliminaries 纯定义罗列，未回指引言）。
4. 小节标题要表明它兼做背景，否则读者会困惑为何综述里出现公式。

### 3.8 句式变换：避免每组末尾套同一模板

同一句式在多组末尾重复会显得机械：《ArtHOI》2.1、2.2 末句均用 "our work advances..."；《SAMTok》《STAC》每子类结尾都是 "Unlike the above approaches, our..."；《GeoPredict》每子节末尾都是 "To address this gap, we introduce GeoPredict..."；《The Geometry of Robustness》每段末尾都是 "Our proposed GRACE framework addresses this limitation by..."；《AutoOcc》《Diorama》多处 "In contrast, we..."；《Differentiable Room Acoustic Rendering》几乎每子类结尾都是 "Different from all of them, we incorporate..."。这些论文的定位都清楚，问题在于形式僵化。

做法：各组从 §3.2(4) 表里选不同类型的定位句；或像《Does YOLO Really Need to See Every Training Image in Every Epoch?》那样有意做排比，每句换一个引导词、各写出具体差别：
- "Unlike curriculum and self-paced learning, which..."
- "In contrast to dataset pruning, which..."
- "Different from dataset distillation, which..."

### 3.9 骨架示例（结构 A，三组；占位符替换成自己的内容）

```
\section{Related Work}
% 开篇句（可选）：We review [领域] along [N] lines that bear on [引言中的根因名].

\paragraph{[路线 1 名].}
A line of work [a,b,c] addresses [任务] by [共同思路].
[a] ... [具体特征]; [b, c] further ... [具体特征].
These methods assume [假设], which breaks when [场景] because [原因].
In contrast, [本文做法的不同点，一句].

\paragraph{[路线 2 名].}
[过渡：为什么要看这条线 / 与路线 1 的关系].
...
Despite these advances, [本文要的性质] remains unexplored.   % 换一种定位句

\paragraph{[最接近的工作 / 路线 3].}
Closest to our work is [X], which also [相同点]. However, [X] [不同点 1]; moreover, [不同点 2].
[可选：Table~\ref{tab:compare} summarizes these differences.]
[末句：This limitation motivates ... / We propose Y to ...]
```

---

## 4. 常见问题与反例

| 问题 | 表现 | 反例 | 修法 |
|---|---|---|---|
| 组间无过渡，小标题硬切 | 各小节之间没有任何衔接，读者不知道为何要看下一组 | 《Batman》《AD-GBC》《4D-RGPT》《BioVITA》《CoLoR》《CineScene》《GlyphPrinter》《LOREAL》《MV-RoMa》《PixelRush》《Radiance Meshes》《Recovering Physically Plausible HOI》《FedAdamom》《UniFusion》《SAM 3D Body》《PoseGAM》《GROC》《A Linear N-Point Solver》《BUFFER-X》《Derm1M》《ForestFormer3D》等 | §3.5：显式过渡句或术语复现 |
| 与引言重复 | 读来像"展开版摘要"，没有新文献或新细节 | 《BeautyGRPO》《Compressed-Domain-Aware Online VSR》（作者自承"与引言内容有重叠"）《DreamShot》《FastGS》《Editprint》《From Selection to Scheduling》《Fresco》《Scalable Feature Matching》（第 2 段与引言第 2 段高度重复）《Scone》《SenseSearch》（末句几乎复述引言措辞）《RALoc》《SRefiner》 | 引言只写定性判断；Related Work 补上具体文献名、具体假设和代价。写完后把两节并排读一遍，删掉重复句 |
| 纯罗列 | "A did X. B did Y."，没有共性局限，与方法动机呼应弱 | 《PGA》《Radiance Meshes》；数据集型论文常把数据集综述写成清单 | §3.2：每组必须有共性局限和定位句；数据集要写优劣如何影响本文设计 |
| 定位句模板化 | 每组末尾同一句式 | 《ArtHOI》《SAMTok》《STAC》《GeoPredict》《The Geometry of Robustness》 | §3.8 |
| 首创声明过多 | 多处 "first"，显得用力过猛 | 《FILTR》 | 全节最多一处首创句，并用对比表或实验支撑；见 `word_style.md` |
| 各组详略不均 | 核心组展开，边缘组一两句带过 | 《MedLIME》《MeshRipple》《OMG-Bench》《NI-Tex》 | 边缘组并入其他组或移到附录 |
| 分组与贡献对应不清 | 读者看不出某段综述服务于方法的哪个设计 | 汇总中有个别论文被指出此问题 | 用结构 C，或在每组定位句里点出对应的模块名 |
| 局限前置 | 把本文应在 Limitations 讲的对比内容放到这里反衬自己 | 《Automated Model Evaluation for Object Detection》整节批评 BoS 三点局限 | 这里只写前作局限；本文局限留给 Limitations（见 `sections/conclusion.md`） |
| 核心洞察未埋伏笔 | 方法里的关键设计动机在综述中毫无铺垫 | 《LayerTracer》的 "Spatiotemporal consistency" | 在最相关一组的共性局限里点出这个性质的缺失 |
| 开篇无衔接 | 综述式总起句直接切入，或直接回到领域史起点 | 《RAVEN》《Modeling Saliency Dataset Bias》 | §3.1 |
| 后置但无过渡 | 放到实验之后，却没有说明为何此时回顾 | 《Straighten Viscous Rectified Flow》 | 后置时开头一句说明"在看到 X 的结果后，我们把本文放回文献中定位" |
| 与 Preliminaries 重复 | 综述开篇与前一节结尾同义重复 | 《Learning Visual Hierarchies in Hyperbolic Space》 | 合并两节，或删去重复句 |
| 对前作描述无依据 | 凭印象写前作做了什么或没做什么 | — | 查 `.paperdna/refs/` 笔记；拿不准标 `% TODO: verify`（旧版规范） |

---

## 5. 写作步骤与检查清单

### 5.1 写作步骤

1. **收集素材**：从引言抄出根因名、缺口名、编号挑战、贡献列表和已经提到的前作；从 `.bib` 和 `.paperdna/refs/` 列出可用文献，给每篇记一行"它做了什么、假设了什么、代价是什么"。
2. **定结构**：按 §2.1 的选择规则选 A–F，按 §2.2 确认本类型的重点，按 §2.3 确认位置（默认第 2 节）。
3. **分组**：把文献分成 2–4 组，给每组起一个技术路线名；标出最接近的 1–3 篇。
4. **写每组的共性局限**：一句话，写到假设、设定或代价，最好和引言根因同名。
5. **写每组的定位句**：从 §3.2(4) 选句式，各组不重复；确认句中说的"本文不同点"在方法和代码里确实存在。
6. **写最接近工作的比较**：按 §3.3 逐点写差别；需要时做对比表（§3.4），表列与贡献措辞一致。
7. **写组间过渡和开篇句**：§3.1、§3.5。
8. **写末句**：把问题交给方法（§3.6），然后检查方法节首句是否接得上。
9. **去重**：把引言和本节并排读，删掉复述句；本节每段都应有引言里没有的文献名或细节。
10. **对照检查**：跑一遍 5.2 的清单。

### 5.2 检查清单

**结构**
- [ ] 默认放在第 2 节；若后置或先写 Preliminaries，有明确理由，且开头有过渡句
- [ ] 分 2–4 组，组名是技术路线名；用结构 C 时，小节顺序与引言挑战顺序一致
- [ ] 各组详略大致相当，没有一笔带过的边缘组
- [ ] 最接近的 1–3 篇被单独点名比较

**每组段落**
- [ ] 段首一句概括这组的共同思路，不是 "Many works have studied X"
- [ ] 代表作不是 "A did X. B did Y." 式罗列，每篇配了具体特征
- [ ] 共性局限写到了假设、设定或代价，不是"性能有限"
- [ ] 段末有定位句，说的是本文**做法**的不同，而不只是"更好"
- [ ] 各组定位句的句式有变化，没有同一模板重复三次以上

**与其他章节**
- [ ] 没有复述引言的句子或任务定义；每段都有引言里没有的文献名或细节
- [ ] 根因名、缺口名、方法名与引言措辞一致（见 `naming.md`）
- [ ] 组间有过渡句或术语复现，没有纯靠小标题硬切
- [ ] 末句把问题交给方法，方法节首句接得上
- [ ] 这里点名的最接近工作在实验里作为基线出现，或说明了无法比较的原因
- [ ] 没有把本文自己的局限前置到这里
- [ ] 兼做背景时，先说明为何需要再给公式，给出的符号在方法节被使用

**声明与引用**
- [ ] "first" / "unique" / "unexplored" 全节最多一处，有检索依据，并有对比表或实验支撑（强度见 `word_style.md`）
- [ ] 对比表的每一列都在实验里有验证，表后有一两句读表
- [ ] 所有引用都在 `.bib` 里；对前作的描述能在 `.paperdna/refs/` 或用户材料中找到依据，拿不准的地方标了 `% TODO: verify`
- [ ] "Unlike X, we do Y" 中的 Y 确实在方法和代码里实现了
- [ ] 正文精简时，开头一句说明完整讨论在附录
