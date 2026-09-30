# Discussion / Limitations / Conclusion（讨论、局限与结论）写作规范

> **读者**：正在替用户写论文最后一节的 AI 助手。照着本文件写，写完用第 5 节的清单逐条自查。
>
> **数据来源**：CVPR 2026 + ICCV 2025 共 1040 篇精读笔记（Oral 195、Highlight 836、Best 9）。本章内容来自三份跨批次的"Discussion / Limitations / Conclusion 写法"汇总，以及 `story_types.md` 各类型章节里的"局限与结论"条目。`references/corpus_stats.md` 里没有本章的专门统计（例如有独立 Limitations 小节的比例），下面涉及的比例都是汇总材料里的估计，只能说明大致趋势，不要当精确数字写进论文。
>
> **合并说明**：旧版 `sections/conclusion.md` 的要求全部保留：简短复述问题、方法、效果；不引入新的结论或新数字；不用 "In conclusion" / "In summary" 开头；局限写具体，写明适用边界、失败情形和代价；未来工作写具体方向，并与局限对应；不写 "we will explore more applications" 这类空话。`story_types.md` §3.6"局限与结论"的内容已全部并入本文件（§0、§3.1、§3.4、§4），各类型章节里的局限写法并入 §2.2。§3.4（方法）和 §3.5（实验）分别归 `sections/method.md` 和 `sections/experiments.md`，本文件只取其中与收尾有关的两条：结论用文字讲机制、不写公式（对应"先直觉后公式"）；实验里的诚实分级和失败案例是局限的证据。
>
> **相关文件**：方法名、根因名的取法和全文措辞统一见 `references/naming.md`；hedge 词、结论强度、"significantly" 这类词的用法见 `references/word_style.md`（尤其原则 2、4、5、10、12 和 §2.2）；数字在摘要、引言、贡献、结论四处一致的要求见 `story_types.md` §3.7。本文件不重复这些内容。
>
> 书名号《》里是真实论文标题或方法名；标注出处的英文句子是论文原句，X / Y / Z 是占位符。

---

## 0. 速查

| 事项 | 默认做法 | 依据 |
|---|---|---|
| 要不要写局限 | **要写**，正文里至少写 2 条具体局限 | 三份汇总一致显示：只有约三成到一半的论文设独立 Limitations 小节或加粗小标题（按类型统计的汇总估计约六到七成没有独立小节），其余或不提、或压成一两句、或推给附录。这是常见现象，**不要模仿** |
| 默认结构 | Conclusion 一段（3–6 句）+ 加粗 "**Limitations.**" 段或 "Limitations and Future Work" 小节 | 《STARFlow-V》"Conclusion and Limitations"；《240FPS Stereo Vision》"Limitations:"；《EgoXtreme》"Limitations and future works" |
| 结论首句 | 回收引言里定义方法的那句话："We introduced X, a [property] framework that solves [problem]." 然后补上边界或代价 | 《ChordEdit》《Cross-Architecture Distillation》(RSD)《DSO》；story_types §3.6 |
| 开头用语 | 不用 "In conclusion" / "In summary" | 旧版规范 |
| 与摘要的关系 | 不逐句复述摘要；可呼应，但必须有摘要之外的信息（边界、代价、意义） | 反例：《Residual Diffusion Bridge Model》几乎逐句照抄摘要；《LaRender》《SparseFlex》结论首句与引言逐字重复 |
| 数字 | 不引入新数字；出现的数字必须与摘要、引言、实验一致 | 旧版规范；story_types §3.7 |
| 单条局限 | **失效场景 + 根因 + 方向**，能指到具体的表、图或数值更好 | 三份汇总一致认定的"黄金标准"；《BridgeDepth》《SLARM》《HairCUP》《Gallant》 |
| 局限从哪来 | 方法的假设、依赖的外部组件、数据与采集条件、计算代价、实验里已暴露的负面结果 | 《BiMotion》fixed-mesh assumption；《Ov3R》继承 3R 模型的位姿误差；《InstantViR》27.04 vs 34.91 |
| 负面结果 | 正文里承认过的弱项，结论和局限里也要出现 | 反例：《SeDiR》《CARE》《Proxy-GS》《SmokeSVD》 |
| 未来工作 | 每条对应一条局限，写出具体技术路线或具体对象 | 《SLARM》《OccuFly》《PhyGaP》《FluoCLIP》 |
| 结尾句 | 有依据的意义陈述，或克制的边界说明。"We hope ..." 只能放在局限之后，不能代替局限 | 反例：《Cubic Discrete Diffusion》《EnergyAction》《ESSENTIAL》 |
| 局限放附录 | 可以放详细版，但正文必须留 1–3 条最重要的，用一句话正面写出来 | 正例：《LBM》正文一句 "need to have access to existing couplings of images beforehand"；反例：《Agile Deliberation》《CIGPose》只写"见附录" |
| Discussion 小节 | 可选。发现-解释型、数据与基准型、有伦理风险的工作更需要；Discussion 讲了的局限，Conclusion 要呼应 | 《PhysGM》§5；《Hearing the Room Through the Shape of the Drum》§8；反例《Spatial-SAM》《MedLIME》 |

---

## 1. 这一章要完成什么，与其他章节的分工

### 1.1 四个任务

1. **收束（Conclusion）**：用两三句回收全文主张，即解决了什么问题、靠什么机制解决、效果如何，再说一句这说明了什么。
2. **划边界（Limitations）**：主动写出方法在什么条件下失效、为什么、代价多大（计算量、数据需求、硬件依赖、假设条件）。坦诚反而能增加可信度（旧版规范）。《Single-Chip Radar》按"贡献—发现—局限"三段收尾，被笔记评为"主动暴露不足反而更可信"。
3. **指方向（Future Work）**：从局限推出具体的下一步，不写愿景。
4. **讨论（Discussion，可选）**：把实验里分散的现象提炼成几条结论，讨论适用边界、替代解释或社会影响。

### 1.2 与其他章节的分工

| 章节 | 它负责的 | 本章不要重复的 | 本章要回收的 |
|---|---|---|---|
| 摘要 | 问题、方法、核心数字 | 不逐句复述 | 核心数字（口径一致） |
| 引言 | 方法定义句、洞察句、贡献列表 | 不重新铺背景和动机 | 方法定义句（同一措辞，见 `naming.md`）；贡献条数前后一致（反例：Bokehlicious 摘要说 threefold，结论只提到 two） |
| 方法 | 设计与假设 | 不再讲模块细节，不写公式 | 方法里的**假设**，这是局限最主要的来源 |
| 实验 | 证据、失败案例、效率数字 | 不引入实验里没有的数字 | 排名不是第一的指标、失败案例图、运行时间和显存，这些是局限的证据 |
| 附录 / 补充材料 | 详细的失败案例、更多讨论 | — | 正文至少留最重要的 1–3 条局限 |

### 1.3 与实现一致，先讲直觉

- 结论里说的机制、适用范围和数字，都要能在实验表、代码或配置里找到对应（`word_style.md` 原则 12）。例如结论说"支持动态场景"，实验里就必须有动态场景的结果。
- 升华不能超出实验支撑范围。反例：《Curvature-Aware Captioning》结尾写 "laying a solid foundation for embodied AI applications"，正文却没有任何具身实验。
- 结论用文字讲清机制和洞察，不放公式；需要回指时用方法名或模块名。

---

## 2. 组织方式：常见结构及适用场景

### 2.1 六种常见结构

| 结构 | 形式 | 适用场景 | 例子 |
|---|---|---|---|
| A. 结论 + 独立 Limitations 节 | 两个编号节，或结论末尾加粗 "**Limitations.**" 段 | **默认推荐**，篇幅允许时首选 | 《RnG》第 5 节 Limitations；《Rethinking Model Selection》第 7 节；《BUFFER-X》5.4；《NeuFrameQ》第 6 节；《STAC》"Limitation." 加粗小标题 |
| B. 合并小节 | "Conclusion and Limitations" / "Limitations and Conclusion" / "Conclusion and Future Works" | 页数紧张时的默认做法 | 《STARFlow-V》《Gallant》"Conclusion & Limitations"；《ReFlex》"6 Limitations and Conclusion"；《PRM》"5. Conclusion and Limitation"（局限在前，结论在后）；《DIMO》 |
| C. 用 "Limitations and Future Work" 代替 Conclusion | 不单设结论，最后一节只写局限与方向 | 正文已把结论讲透，收尾以边界为主 | 《Learning Convex Decomposition via Feature Fields》"5. Limitations and Future Work"；《MeshLLM》编号 1–4 条；《Unified Vector Floorplan Generation》 |
| D. Discussion 节 + 短 Conclusion | Discussion 讲局限、替代解释、社会影响，Conclusion 做正面收束 | 发现-解释型；有伦理或隐私风险；局限较多需要展开 | 《PhysGM》第 5 节"Discussion"列三类局限配两条方向；《Hyperbolic Relational Prompts》第 6 节三条局限；《Hearing the Room Through the Shape of the Drum》第 8 节"Discussion and limitations"并单列社会影响；《MaGS》局限放在 4.5 Discussion |
| E. 一段合一 | 一段里先收束、再转折写局限、最后回到结论 | 篇幅极紧 | 《E-RayZer》"While our results are promising, we identify several limitations..." 之后接 "Despite these limitations, E-RayZer outperforms prior..." |
| F. 失败案例小节 | 实验末尾单列失败案例和方向，配图 | 生成、重建、视觉效果类工作 | 《TriLite》4.8 "Failure cases and Future Directions"；《DeX-Portrait》Fig.12 列两类真实失效场景；《Fine-structure Preserved ISR》Fig.6 |

**不推荐的结构**：
- 局限整段推给附录，正文只留一句指引（《TokenLight》"We discuss limitations and future work in the supplementary material."；《A Frame is Worth One Token》；《MoGA》；《InfiniteYou》；《SimScale》把局限、相关工作、broader impact 全部移出正文）。
- 没有结论节，实验后直接进致谢（《MetaSpectra+》；《Vista4D》在 Applications 之后直接进 Acknowledgements）。
- 结构 D 的风险是"两张皮"：Discussion 讲局限，Conclusion 只字不提（《Spatial-SAM》4.6 Discussion 谈了局限，结论不提；《MedLIME》Limitations 承认线性代理假设，Conclusion 却不回应）。选 D 时，Conclusion 里至少用一个从句回指最主要的局限。

**选择规则**：
1. 默认选 A；页数紧就选 B 或 E，但局限至少要有 2 条具体的。
2. 需要讨论替代解释、社会影响，或者局限超过 3 条时选 D。
3. 视觉生成或重建类工作可以另加 F，用失败案例图支撑局限。
4. 附录可以放详细版，正文必须保留最重要的局限。

### 2.2 按故事类型的差异

叙事类型的判断见 `story_types.md` 第 2 节。各类型收尾的重点不同：

| 类型 | 局限写到哪里 | 正例 | 反例 |
|---|---|---|---|
| 瓶颈突破型（56.0%） | 写到**根因机制的边界**：你修好的环节在什么条件下仍然会坏 | 《HairCUP》四条局限各配一个 because；《Gallant》在 Pile 地形约 80% 失败，归因于 LiDAR 10Hz 延迟；《TMFS》报告强湍流下 PSNR 仅 19.671；归因模板 "We attribute this limitation to X, which is sufficient for Y but ineffective for Z."（《SuperDec》） | 《SuP》"a promising extension rather than a core limitation"；《SeDiR》不提 P-AUROC 只排第二；《RS-vHeat》不提在 Tab.4/5/8 不如对手 |
| 新问题定义型（11.0%） | 写**新设定本身的假设**，逐条编号 | 《SceneMI》用 (i)(ii)(iii) 列假设；《FluoCLIP》一句里完成承认与方向；《Teeth Reconstruction》把依赖 SAM2 定性为正交技术可解（可用 Personalize-SAM 自动化）；结论常用 "paving the way for ..." 收尾 | 《FGAesQ》只写 "remains challenging"，没点出 AIGC 分支 0.709 低于 Natural 分支 0.779；《Agile Deliberation》局限全推附录；《Heavy Labels Out!》对 IPC=50 时逊于 RDED 只字未提 |
| 统一框架型（10.8%） | 写统一之后仍**覆盖不到的场景或模态**，以及统一带来的代价 | "struggles with occluded structures in limited-view training and deformable scenes"（《HiNeuS》）；"may underperform under extremely fast dynamics"（《AeroGS》）；依赖针孔相机模型（《AAA-Gaussians》）；让步模板 "Although our study focuses on X, Y is modality-agnostic."（《SGDIR》《x2-Fusion》） | 《Residual Diffusion Bridge Model》结论几乎逐句照抄摘要；《MSPT》《GeniNav》《HR-NVC》结论与摘要或引言同构；《SoccerMaster》《TUNA》《DPoser-X》正文承认的弱点结论不提 |
| 发现-解释型（10.7%） | 独立成段，写**发现成立的前提和失效区间**；常设 Discussion | 《LumiMotion》四条局限；《Combinative Matching》Fig.9 失败案例；《GRPO-Guard》写明无法消除 reward hacking 的根因；《PercHead》把贡献升华为挑战一个假设 | 《KDAS》《ViT3》《FedAdamom》没有独立局限，结论是摘要的同义改写；用 "potentially / could be / a hint"、"seems plausible...may" 回避局限 |
| 数据与基准型（7.0%） | 写到**数据集自身**：规模、标注者背景、采集条件、覆盖范围；也可以把局限前置 | 《EgoXtreme》依赖 OptiTrack，只能在室内专用场地采集；《Wanderland》采集频率 1 FPS、只建模静态环境，逐条给补救方向；DENALI 用 "Scope of this Work" 前置局限；《WorldLens》把评测发现写成 "Guidelines for Future World Model Design"；结论首句可呼应引言（"We introduced GeoMMBench..."），但后面必须有新信息 | 《ChartCap》《FPEM》完全不提局限；《M3DLayout》把指标落后说成"复杂度不匹配"；《VRR-QA》没提样本只有 1K、标注者就是作者本人 |
| 能力扩展型（2.4%） | 写扩展之后**仍未覆盖的部分**，克制而具体 | 《Anatomica》两点局限；《STARFlow-V》"(1) Latency (2) Data quality"，各配 future work | 《CoordSpeaker》《MEDIC-AD》《LEGION》(Appendix E)《HouseCrafter》推给附录；《HumanNOVA》用未来工作代替局限；《PET-DINO》"We hope this work can provide new insights..." |
| 效率优化型（2.0%） | 把局限绑定到**加速所依赖的设计假设**，并报告质量损失 | 《AdaptVision》绑定"单一工具 / 固定 1/4 分辨率 / 两轮"；《Sparse-LaViDa》承认需要额外训练；《EDM》承认优势随分辨率升高而下降；《DeltaTok》自曝 mean 分数 "modestly worse"；《ScoreLiDAR》《Turbo-GS》局限针对性强、不夸大 | 《SwiftTailor》《TurboVSR》只写 "we leave this for future work"；《VMonarch》《SigLino》完全不谈局限；《LinVideo》把局限写成"未来可进一步提速" |
| 理论分析型（0.2%，仅 2 篇） | 写**定理失效的区间**，最好前置到引言并辩护 | 《PLMP》把局限提前到引言第 7–8 段并主动辩护；《C²FG》结论仅 5 句、不含数字，逐字呼应引言和贡献措辞 | 《C²FG》把 t→0 的失效区间埋在 3.1 节末尾一句，容易被忽略 |

---

## 3. 逐部分写法

默认顺序：结论首句 → 机制与证据 → 意义 → 局限 → 未来工作 → 结尾句。结构 B 的《PRM》把局限放在结论之前，也可以。

### 3.1 结论首句：回收方法定义句，补上边界或代价

**写什么**：方法名 + 类别 + 机制 + 解决的问题，与引言里定义方法的那句话用同一措辞（方法名措辞统一见 `naming.md`）。

**怎么写**：
- 可以呼应摘要或引言，但不能逐字照抄。呼应句的后半句，或者紧接的下一句，要带上摘要里没有的信息，例如适用条件或代价（story_types §3.6）。
- 发现-解释型、数据与基准型可以回到研究问题本身，不必以方法名开头。
- 不用 "In conclusion" / "In summary" 开头（旧版规范）。

**模板**：
- "We introduced [Method], a [property] framework that solves [problem]." ——原句："We introduced ChordEdit, a training-free, inversion-free framework that solves the instability of one-step image editing."（《ChordEdit》）
- "We introduced RSD, a simple approach for cross-architecture knowledge distillation based on redundant knowledge suppression."（《Cross-Architecture Distillation》）
- "We presented DSO, a novel framework for generating physically sound 3D objects by leveraging feedback from a physics simulator"（《DSO》，直接呼应摘要首句）
- "In this work, we introduced MEMFOF, ..."（《MEMFOF》；《GENMO》《Long-LRM》《LBM》等十余篇同构）
- "We have introduced a novel graph-Laplacian loss..."（《Differentiable Laplacian》，与引言 "we propose a graph-Laplacian (LAP) loss" 首尾呼应）
- 回到研究问题："In [this] paper, we investigated the question of which vision encoder..."（《Rethinking Model Selection》）

**反例**：《LaRender》"In conclusion, we proposed a novel non-parametric mechanism, Latent Rendering..." 与引言几乎逐字重复，还用了 "In conclusion" 开头；《SparseFlex》结论首句与引言第 4 段几乎逐字重复。

### 3.2 机制与证据：两三句讲清"靠什么、到什么程度"

**写什么**：核心洞察或机制（文字表述，不写公式）、覆盖的任务或场景、一两个核心数字。

**怎么写**：
- 数字只用已经在摘要或实验里出现过的，口径一致。《Event-based Visual Deformation Measurement》的 1.6×/18.9% 贯穿摘要、贡献和结论；《DataTailor》的 "101.3%" 在摘要、引言、结论各出现一次。
- 用具体规模代替空泛的"高效""可扩展"：《Efficient Unrolled Networks》用 "handles volumes as large as 501³ on a single GPU" 收尾。
- 需要说明收益从哪来时，用让步收束句排除读者担心的代价。

**模板**：
- "This speed/gain is achieved not by sacrificing [X], but by [Y]."（《ChordEdit》）
- 三段式（总述 → 覆盖的任务 → 意义）："This shows a step towards a scalable, unified, and generalizable feed-forward 3D perception system."（《AMB3R》）

**注意**：强度词必须与实验排名一致。只拿到第二名的指标不能写成全面领先；"achieves true real-time, high-fidelity, and consistent..."（《ChordEdit》）这种全无保留的写法要避免。强度和限定语的规则见 `word_style.md` §2.2。

### 3.3 意义句：升华到"说明了什么"，但不超出证据

**写什么**：这项工作改变了什么认识，或者把领域从哪里推到了哪里。

**三种可用写法**：
1. **认知层面**：把贡献从"效果更好"升华为"推翻了一个假设"。"This challenges the prevailing assumption that conventional image losses...are necessary for supervision"（《PercHead》）。
2. **范式定位**：用 "from X to Y" 说明转变。《Relightable Holoported Characters》(RHC)："marks a step change in human relighting—from static, replay-based, or pose-driven avatars ... to dynamic, photorealistic humans..."
3. **克制定位**：第一次做某件事时，承认只是起点。"GameFactory marks our first effort in this field"（《GameFactory》）；"an important step toward direct object pose estimation..."（《PoseGAM》）。

**边界**：
- 意义句的范围不能超出实验。反例：《Curvature-Aware Captioning》"laying a solid foundation for embodied AI applications"（无具身实验）；《Variance-Based Pruning》升华到 "democratization of deep learning"，却没有具体讨论局限。
- 不要只谈"他人方法的局限"：《Towards Multimodal Domain Generalization with Few Labels》结论写 "highlighted the limitations of existing SSML, MMDG, and SSDG paradigms"，却没有反思自身边界。

### 3.4 局限段：失效场景 + 根因 + 方向

#### (1) 开篇句

- "Despite its effectiveness, [Method] has several limitations that outline directions for future research."（《AdaptVision》）
- "Despite strong results, our method has several limitations: ..."（《Learning Scene Coordinate Reconstruction》）
- "While our results are promising, we identify several limitations and directions for future work"（《E-RayZer》）
- "While the results are encouraging, there are still limitations to overcome."（《STARFlow-V》）
- "While X delivers consistent gains across architectures and datasets, several limitations suggest fruitful avenues for future work."（《BoostSLT》）
- "Despite its success, Gallant does not yet achieve a 100% success rate"（《Gallant》，开篇就给量化缺口）
- 初探性工作："As our research represents an initial step in this area, the scope of our experiments could be further expanded."（《Rethinking Model Selection》）

#### (2) 单条局限的三要素

每条局限都要能回答三个问题：**在什么条件下失效 → 为什么 → 怎么改**。

| 要素 | 写法要求 | 原句与出处 |
|---|---|---|
| 失效场景 | 具体到场景类型、参数范围或数值 | "may compromise accuracy at high resolutions (≃2K)"（《BridgeDepth》）；"struggles with complex materials like glass or mirrors"（《SLARM》）；"exhibits limitations when applied to videos captured at extremely low frame rates"（《RetimeGS》）；"some generated animations exhibit background distortions and artifacts"（《MikuDance》） |
| 根因 | 写到机制或假设层，说明是哪个组件或哪条假设导致的 | "where large disparity ranges strain the top-k hypothesis selection in the Disparity Proposal Network"（《BridgeDepth》）；"due to its reliance on photometric consistency"（《SLARM》）；"due to the inherent constraints of optical flow"（《RetimeGS》）；"does not support topology-changing motion due to our fixed-mesh assumption"（《BiMotion》）；"the 3D-agnostic challenge in image animation, making scene reconstruction in dynamic cameras an ill-posed problem"（《MikuDance》）；"due to deeper feature extraction layers"（《EDM》） |
| 方向 | 点名具体技术、模块或对象 | "Future work could address this via a stereo feature interaction module."（《BridgeDepth》）；"Future work will explore self-calibration and more realistic scene representations..."（《SLARM》）；"integrating techniques from the SLAM literature, such as global bundle adjustment"（《Ov3R》）；点名扩展对象 "(e.g., TransUNet or Swin-UNet)...this direction remains to be explored in future work."（《AD-GBC》） |

三要素写在同一句里的完整例子：
- "our implementation may compromise accuracy at high resolutions (≃2K) where large disparity ranges strain the top-k hypothesis selection in the Disparity Proposal Network. Future work could address this via a stereo feature interaction module."（《BridgeDepth》）
- "SLARM currently requires accurate camera poses and struggles with complex materials like glass or mirrors due to its reliance on photometric consistency."（《SLARM》，接着逐条给方向）
- "But our Gaussian pose assumption is a key limitation, as the non-linear 2D-to-6D transformation challenges its coverage guarantees, which we will address by exploring more suitable distributions."（《Deterministic Object Pose Confidence Region Estimation》）

因果链写法：《SuperEvent》写成"训练数据来自真实序列 → 运动方向存在偏置 → 强运动下描述子匹配性能下降"，根因一路追到数据。

#### (3) 去哪里找局限

逐项翻一遍，通常能找到 2–4 条真实局限：

| 来源 | 怎么找 | 例子 |
|---|---|---|
| 方法的假设 | 方法节里所有 "we assume"、固定超参数、固定结构 | 《BiMotion》fixed-mesh assumption；《DDiT》"for a given timestep, we use a fixed patch-size"；《Revisiting the Necessity of Full Accuracy》"it is limited to correcting non-translational noise"；《Fully Decentralized Certified Unlearning》5 点局限各对应正文一个假设；《Cov2Pose》"does not explicitly handle object symmetries"；《Diffusion-Based Native Adversarial Synthesis》只在图像空间挖噪声、依赖扩散模型生成 on-manifold 样本 |
| 适用边界 | 实验只覆盖了哪些设备、光照、领域 | "our conclusions are only applicable to smartphones and under good lighting conditions"（《RAW-Domain》）；"in domains such as graph learning...our conclusions do not yet transfer."（《FILTR》） |
| 依赖的外部组件 | 预训练模型、位姿、伪标签来源；可以把局限归因到底层组件 | "Ov3R inherits one of the limitations of 3R models, i.e., the suboptimal accuracy of the retrieved camera poses"（《Ov3R》）；"the generation of pseudo-labels is constrained by the LVLM"（《Learning to Track Instance...》）；依赖 GGHead 先验，稀有配饰处理受限（《SketchFaceGS》）；位姿仍靠 COLMAP（《Thermal is Always Wild》） |
| 数据与采集 | 数据规模、多样性、采集设备和场地 | "due to the limited variety of leaf species in our DeformLeaf dataset, the model struggles to cover certain unique types of leaf deformations"（《NeuraLeaf》）；依赖 OptiTrack、只能在室内专用场地采集（《EgoXtreme》）；1 FPS、只建模静态环境（《Wanderland》） |
| 计算代价 | 推理时间、显存、训练成本、实时性 | "it currently cannot meet real-time requirements due to its iterative guidance"（《WorldForge》）；"a full evaluation...required 6.7 hours on a single NVIDIA GTX 4090 GPU"（《TouchDream》）；"due to computational resource constraints, we have not yet performed an exhaustive...analysis"（《MODIX》）；需要额外训练（《Sparse-LaViDa》）；LCD 调制器约 60Hz 的物理上限（《240FPS Stereo Vision》） |
| 实验中已暴露的弱项 | 排名不是第一的指标、提升最小的设置、消融里的超参数敏感性、失败案例 | 《BiPreManip》Pliers 25%/29% 的弱项；《CARE》"ROI features do not outperform WSI features across all tasks"；《Stable Mean Flow》超参数高度敏感；《SmokeSVD》正文承认 "slightly lower" |

#### (4) 用证据支撑局限

- **数字**：《InstantViR》用 LeanVAE 版 4× 超分 PSNR 27.04 vs 原版 34.91 说明代价；《Revisiting Geometric Obfuscation》(DCL) 用 "only 4/17,000 images in 7Scenes" 说明退化场景很少见，让局限的严重程度可以判断。
- **图表**：《DeX-Portrait》Fig.12 失败案例；《Fine-structure Preserved ISR》Fig.6；《TrajectoryCrafter》三条局限各配根因和失败案例图；《Stereo Any Video》用 Table 6 的参数量和显存支撑效率局限。

#### (5) 多条局限的排版

- 用 First / Second / Finally 编号，每条一个三要素：《Spectrum from Defocus》列四条，每条配 "which could be improved with..."；《SketchFaceGS》三条各附缓解方向，例如 "we aim to mitigate this with identity consistency losses or advanced encoders"；《TrajectoryCrafter》用 Firstly / Secondly / Finally。
- 假设类局限用 (i)(ii)(iii)（《SceneMI》），或编号 1–4（《MeshLLM》）。
- 局限与方向逐条对应：《PhyGaP》三类局限对应 (a)–(d) 未来方向，并引用 "GaussProbe in TransparentGS [24]" 作为可行路径；《OccuFly》三点局限各配补救（静态场景假设 → 4D Gaussian Splatting；标注需人工 → 更鲁棒的 2D 伪标签）。
- 可以给**使用建议**，而不只是指出问题："We therefore recommend building S from a small set of well-established, complementary strategies rather than arbitrarily including numerous ones."（《Cleaning the Pool》）

#### (6) 措辞：诚实，但不绝对化

- 不确定时用 may 留余地："it assumes relatively smooth motion and may underperform under extremely fast dynamics or highly cluttered scenes"（《AeroGS》）。
- 用 unless 写出条件："may fail to represent high-frequency details for very complex motions unless more control points are used"（《BiMotion》）。
- 原因不确定就直说："we cannot definitively pinpoint the source of the problem"（《Processing and acquisition traces》，同时说明重训练成本高、模型常用私有数据）；"The main limitation...is that it requires a reasonable initialization for a subset of the cameras."（《On the Recovery of Cameras from Fundamental Matrices》）。
- 开放问题："remains an open problem"（《Electromagnetic Inverse Scattering》《E2EGS》）；"It remains an open question, however, whether..."（《Inter-Photon-Limited Videography》）。
- 用 limitation 这个词，不用 "remaining issue" 之类的软化说法（反例：《DynFaceRestore》）。hedge 词的具体用法见 `word_style.md`。

#### (7) 哪些"正面转化"可以用，哪些是淡化

| 可以用（有数据或逻辑支撑） | 不要用（削弱局限分量） |
|---|---|
| 同一属性的两面："While FlowEdit's strong structure preservation is beneficial for precise editing tasks, it can become a limitation when substantial modifications to large regions of the image are desired."（《FlowEdit》） | 贴"次要"标签："One minor limitation of our approach is that..."（《ANTS》） |
| 实验里确实能看到权衡时，定性为权衡：《R²-Seg》把 sensitivity 下降写成 "an explicit calibration trade-off" | 改口径："We consider this a promising extension rather than a core limitation"（《SuP》） |
| 先写清局限，再说明可以推广："As a direction for future work, the MLOO formulation is applicable to other population-based metrics beyond RMM."（《RLFTSim》） | 列完就否定："Nevertheless, these are not fundamental limitations and can be alleviated with better data and supervision"（《CUPID》）。只有在给出具体缓解路径时才能这样收，否则删掉 |
| 在局限之后向业界提建议："we hope this work encourages LiDAR manufacturers to make future sensing pipelines more programmable"（《Lidar Waveforms》） | 承认之后用大段论证削弱：《PETAR》先说 "A feature of our method is the requirement of mask inputs..."，随即用 FDA-cleared 工具的可行性为其开脱 |
| 把评测发现写成正向准则（数据与基准型）：《WorldLens》"Guidelines for Future World Model Design" | 说成"大家都有这个问题"："A limitation of X is Y, a challenge widely shared by representative works in the field... Despite these challenges, X stands as a pioneering contribution."（《Derm1M》） |

### 3.5 未来工作：与局限一一绑定

**写什么**：每条方向都从一条局限推出，点名具体技术、对象或量级。

**模板**：
- 一句内完成承认与方向："While FluoCLIP assumes predefined stain categories, future work will explore automatic stain discovery..."（《FluoCLIP》）
- 逐条绑定：《SLARM》局限与未来工作逐条对应；《Thermal is Always Wild》两条局限各给根因（光度稳定未与重建联合优化；位姿仍靠 COLMAP）和方向（"future end-to-end formulations"、"more robust, thermal-aware pose estimation methods"）。
- 点名对象："Future work will extend AoD-IP to broader tasks (e.g., VQA and image generation) and explore more diverse datasets and architectures..."（《Authorize-on-Demand》）；"new evaluation benchmarks that more accurately reflect real-world long-context retrieval...(e.g., matching images to multi-paragraph document pages, such as textbooks and reports)"（《CLIP Is Shortsighted》）。
- 点名技术："adaptive scheduling of refinement depth, incorporating stronger physical priors...extending...to other dense correspondence problems"（《MorphSeek》）；anytime-valid e-processes / 更丰富的谱密度族 / 分布偏移扩展（《Spectral Conformal Risk Control》）。
- 给量级：从 "≈10 agents" 到 "≈100 agents"（《Unified Number-Free Text-to-Motion》）。
- 排比列 2–3 条："While our approach represents an advance in X, several avenues for future work remain. First..., Second..., Finally..."（《EventUPS》：非朗伯体表面、学习式组件、动态场景重建）；"A promising direction.../Another important avenue.../Finally, we envision..."（《BLADES》）。
- 划清边界："These optimizations are orthogonal to our current work"（《MeshLLM》）；"We leave developing effective sample ranking methods as future work."（《DexVLG》）。

**注意**：
- 未来工作不能代替局限。反例：《VIRD》"Future work will extend this approach to more challenging 6-DoF pose estimation tasks..." 只是间接承认方法局限于 3-DoF 地面场景；《AIM》"We plan to extend AIM to Vision Transformers..." 暗示只在 CNN 上验证过；《GECKO》把局限于单一癌种写成"扩展到泛癌种"。这类句子前面应先有一句正面承认。
- 未来工作要回应实验里已暴露的弱项。反例：《SPDMark》"Future directions could extend this work to other generative modalities."，却没回应 ModelScope 上 denoising/blur 分数偏低、payload 越大鲁棒性越差的权衡；《Plant Taxonomy》只列扩展物种和时序标注，没回应长尾样本不均衡。

### 3.6 Discussion 小节（可选）

**什么时候写**：发现-解释型需要把分散的现象提炼成几条结论；需要回答"提升是否来自别的因素"；有隐私、伦理风险；局限较多需要展开。

**写什么**：
- **替代解释**：主动自问读者会怀疑的来源，例如 Discussion 里自问"提升是否只来自外部先验"（《CAD》）。
- **适用边界与局限**：《PhysGM》第 5 节列三类局限配两条方向；《Hyperbolic Relational Prompts》第 6 节列三条（层级建模的社会复杂性、二元性别假设、计算开销）。
- **社会影响**：《Hearing the Room Through the Shape of the Drum》在 "Discussion and limitations" 里单列社会影响。伦理说明不能代替技术局限。
- **认识层面的收获**：对发现-解释型，把核心发现写成一句可以被引用的结论（参考《PercHead》的写法）。

**与 Conclusion 的衔接**：Discussion 里的主要局限，Conclusion 要用一个从句回指，避免"讨论求真、结论造势"（反例：《Spatial-SAM》《Unsupervised Multi-Scale Segmentation》《Urban-GS》）。

### 3.7 结尾句

按优先级选一种：
1. **最重要的局限 + 方向**，作为全文最后一句（《FluoCLIP》式一句话）。
2. **有依据的意义陈述**（§3.3 的三种写法之一）。
3. **克制的收尾**，只放在局限之后："We view our experiments as a hint to the potential of our algorithm and encourage further investigation..."（《Is the Modality Gap...》）；"We believe that hierarchical material recognition can help intelligent systems perform more sophisticated tasks..."（《Hierarchical Material Recognition》）。

不要用以下句子单独收尾（它们不含信息，也不能代替局限）："We hope this work will inspire future research on unified multimodal architectures."（《Cubic Discrete Diffusion》）；"We hope this dataset and analysis motivate future research to address these challenges."（《Beyond Single Images》）；"We hope this work provides valuable insights for the robotics community..."（《EnergyAction》）；"We hope this work inspires future research in video class-incremental learning."（《ESSENTIAL》）；"We anticipate that ZoomEarth will form the foundation for..."（《ZoomEarth》）。

### 3.8 骨架示例（结构 B，占位符替换成自己的内容）

```
\section{Conclusion and Limitations}
We introduced [Method], a [property] framework that [solves problem] by [mechanism in words].
[One sentence: the key insight, e.g., "This gain is achieved not by sacrificing X, but by Y."]
Across [tasks/datasets], [Method] [result with the same number as in the abstract].
[One sentence of significance, bounded by the experiments.]

\paragraph{Limitations.}
Despite its effectiveness, [Method] has several limitations.
First, [Method] may [failure] when [condition], because [root cause tied to an assumption/component]
(Fig./Tab. [k]); [specific technique] could address this.
Second, [cost: runtime / memory / data requirement], since [reason]; [specific direction].
[Optional: the weakest reported result, stated with its actual rank.]
```

---

## 4. 常见问题与反例

| # | 问题 | 反例 | 改法 |
|---|---|---|---|
| 1 | 完全不写局限，全程自信 | 《Learning Diffeomorphism》从头到尾没有局限、失败案例和未来工作；《CasP》《CoMatch》《CountSE》《CounterPC》《GT-Loc》《VMem》《VRM》 | 按 §3.4(3) 的来源表找 2–4 条真实局限 |
| 2 | 局限整段推给附录，正文只留指引 | "Limitations and future work are discussed in the appendix."（《Agile Deliberation》，被笔记点评为"值得商榷"）；《CIGPose》《Concept-Guided Fine-Tuning》《ETCH》《Stable-Sim2Real》《Soft Local Completeness》 | 正文用一句话写出最重要的局限，再指向附录；参考《LBM》 |
| 3 | 结论是摘要、引言或贡献列表的同义复述 | 《RF4D》没有新内容也没有展望；《FlexMem》被批"第四次近似重复"；《ViT3》复现摘要三段式；《TeHOR》；《Discontinuity-aware Normal Integration》只有 3 句重述加 1 句致谢 | 首句回收定义句，后面加边界、代价、意义等摘要之外的信息 |
| 4 | 回避实验中已出现的负面结果 | 《SeDiR》P-AUROC 只排第二；《BiPreManip》Pliers 25%/29%；《Proxy-GS》正文承认"效果因场景而异""顶点噪声超过 5% 质量下降"，结论却写 "establishing a new state-of-the-art"；《CHTR》局限藏在 6.3 节失败案例分析；《Contrastive Test-Time Composition of Multiple LoRA》8 个 LoRA 时显存和耗时上升未提 | 把实验里非第一的指标、失败案例列进局限，措辞强度与实际排名一致 |
| 5 | 用"未来工作"代替"局限" | 《LinVideo》"as a future direction, would allow our method to achieve an enhanced speedup ratio"；《SwiftTailor》《TurboVSR》《RALoc》（全文不出现 limitation） | 先正面写 "A limitation of X is ..."，再给方向 |
| 6 | 承认之后立刻淡化 | 《ANTS》"minor"；《SuP》"rather than a core limitation"；《CUPID》"not fundamental limitations"；《PETAR》大段开脱；《Derm1M》"widely shared" | 删掉淡化句，改为给出具体缓解路径（§3.4(7)） |
| 7 | 局限写得太抽象 | 只写"还有改进空间"（旧版规范）；《FGAesQ》只写 "remains challenging"；《SAQN》"We anticipate that future work will address this issue." 一句带过；《Drainage》 | 补齐失效场景、根因、方向，最好带数字或图 |
| 8 | 局限与结论"两张皮" | 《MedLIME》；《Spatial-SAM》；《Urban-GS》 | 结论里用从句回指主要局限 |
| 9 | 升华超出实验支撑 | 《Curvature-Aware Captioning》"embodied AI"；《Variance-Based Pruning》"democratization of deep learning" | 意义句只谈实验覆盖到的范围 |
| 10 | 用 we hope / we believe 的空话收尾 | 《Cubic Discrete Diffusion》《LLMind》《EnergyAction》《ViterbiPlanNet》《ActiveAD》《SenCache》；"a versatile representation, with promising properties that can benefit future applications..."（《Representing 3D Faces》） | 按 §3.7 的优先级换成局限或有依据的意义句 |
| 11 | 语气过分自信，没有限定语 | "ChordEdit achieves true real-time, high-fidelity, and consistent generative image editing."；"Extensive experiments demonstrate..."（《GeniNav》） | 按 `word_style.md` §2.2 调整强度，绑定到具体数字 |
| 12 | 只谈他人方法的局限 | 《Towards Multimodal Domain Generalization with Few Labels》 | 至少写一条自身的局限 |
| 13 | 数字或贡献条数前后不一致 | 《AsymLoc》95% / 95.5% / 96%；《Counterfactual VLA》摘要 20.5%，正文 14.7%；Bokehlicious threefold vs two | 结论里的每个数字回查摘要和实验表 |
| 14 | 语法或逻辑瑕疵 | "Our work establishes opens up future research..."（《A Style is Worth One Code》） | 定稿前按 `word_style.md` §7 通读 |

---

## 5. 写作步骤与检查清单

### 5.1 写作步骤

1. **收集素材**：从引言抄出方法定义句和贡献条数；从摘要抄出核心数字；从方法节列出所有假设和固定设计；从实验节列出排名不是第一的指标、失败案例图、运行时间和显存；与用户确认代码或实验记录里的数字（`word_style.md` 原则 12）。
2. **定结构**：按 §2.1 的选择规则选 A–F，按 §2.2 确认本类型的局限重点。
3. **筛局限**：从 §3.4(3) 的来源表里选 2–4 条对读者最重要的。优先选：实验里已暴露的弱项 > 方法的核心假设 > 计算代价 > 数据与采集条件。
4. **逐条写三要素**：每条写成"失效场景 + 根因 + 方向"，能指向表、图或数值的就指出来。
5. **写结论**：首句回收定义句 → 机制与证据两三句 → 一句意义（不超出实验）。
6. **写未来工作**：每条从一条局限推出，点名技术或对象。
7. **写结尾句**：按 §3.7 选；如果用了 we hope / we believe，确认前面已经有具体局限。
8. **对照检查**：跑一遍 5.2 的清单。

### 5.2 检查清单

**结构**
- [ ] 正文里有至少 2 条具体局限（独立小节、加粗段落或合并小节均可），不是只写"见附录"
- [ ] 用了结构 D 时，Conclusion 回指了 Discussion 里的主要局限

**结论**
- [ ] 首句回收了引言里的方法定义句，方法名措辞与全文一致（见 `naming.md`）
- [ ] 没有逐句复述摘要，有摘要之外的信息（边界、代价或意义）
- [ ] 没用 "In conclusion" / "In summary" 开头
- [ ] 没有新数字、新结论；出现的数字与摘要、引言、实验一致；贡献条数前后一致
- [ ] 机制用文字表述，没有公式
- [ ] 意义句的范围没有超出实验；强度词与实际排名一致（见 `word_style.md`）

**局限**
- [ ] 每条局限都有失效场景、根因、方向
- [ ] 根因写到了机制、假设或具体组件，不是"能力不足""还有改进空间"
- [ ] 正文里承认过的弱项（非第一的指标、失败案例、超参数敏感性）在局限或结论里都出现了
- [ ] 至少一条局限有数字、表或图支撑
- [ ] 没用 "minor"、"not fundamental"、"rather than a core limitation"、"remaining issue" 等淡化措辞；只在给出具体缓解路径时才说局限可缓解
- [ ] 有伦理或隐私风险时单独说明，且没有用它代替技术局限

**未来工作与结尾**
- [ ] 每条未来工作对应一条局限，点名了具体技术、对象或量级
- [ ] 没有用未来工作句代替局限
- [ ] 最后一句不是单独的 "We hope this work will inspire..."
