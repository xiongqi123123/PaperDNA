# Discussion / Limitations / Conclusion（讨论、局限与结论）写作规范

> **读者**：正在替用户写论文最后一节的 AI 助手。照着本文件写，写完用第 5 节的清单逐条自查。
>
> **数据来源**：CVPR 2026 + ICCV 2025 共 1040 篇精读笔记（Oral 195、Highlight 836、Best 9）。本章内容来自三份跨批次的"Discussion / Limitations / Conclusion 写法"汇总，以及 `story_types.md` 各类型章节里的"局限与结论"条目。`references/corpus_stats.md` 里没有本章的专门统计（例如有独立 Limitations 小节的比例），下面涉及的比例都是汇总材料里的估计，只能说明大致趋势，不要当精确数字写进论文。
>
> **口径**：如何对待不利结果、局限和自我评价，以 `references/anti_defensive.md` 为准（不利结果的处理顺序见其第 3 节，局限写法见第 5 节）。本文件与它冲突时，以它为准。
>
> **合并说明**：旧版 `sections/conclusion.md` 的要求保留：简短复述问题、方法、效果；不引入新的结论或新数字；不用 "In conclusion" / "In summary" 开头；局限写具体，写明适用边界；未来工作写具体方向，并与局限对应；不写 "we will explore more applications" 这类空话。其中局限部分已按 `anti_defensive.md` 调整为"最多 2 条，每条写成适用边界 + 方向"。`story_types.md` §3.6"局限与结论"的内容已全部并入本文件（§0、§3.1、§3.4、§4），各类型章节里的局限写法并入 §2.2。§3.4（方法）和 §3.5（实验）分别归 `sections/method.md` 和 `sections/experiments.md`，本文件只取其中与收尾有关的一条：结论用文字讲机制、不写公式（对应"先直觉后公式"）。
>
> **相关文件**：方法名、根因名的取法和全文措辞统一见 `references/naming.md`；hedge 词、结论强度、"significantly" 这类词的用法见 `references/word_style.md`（尤其原则 2、4、5、10、12 和 §2.2）；数字在摘要、引言、贡献、结论四处一致的要求见 `story_types.md` §3.7。本文件不重复这些内容。
>
> 书名号《》里是真实论文标题或方法名；标注出处的英文句子是论文原句，X / Y / Z 是占位符。

---

## 0. 速查

| 事项 | 默认做法 | 依据 |
|---|---|---|
| 要不要写局限 | 可以写，但**最多 2 条**，每条一两句 | 顶会论文多数不设独立局限小节（按类型统计的汇总估计约六到七成没有），而是不提、压成一两句或推给附录。本 skill 的做法是最多 2 条、简短（`anti_defensive.md` §5） |
| 默认结构 | 加粗 "**Limitations.**" 短段放在结论之前，最后一节是 Conclusion 一段（3–6 句）；页数紧时把局限一两句放在结论中间 | 《PRM》"5. Conclusion and Limitation"（局限在前，结论在后）；《ReFlex》"6 Limitations and Conclusion"；《STARFlow-V》"Conclusion and Limitations" |
| 结论首句 | 回收引言里定义方法的那句话："We introduced X, a [property] framework that solves [problem]." 然后补上摘要之外的信息 | 《ChordEdit》《Cross-Architecture Distillation》(RSD)《DSO》；story_types §3.6 |
| 开头用语 | 不用 "In conclusion" / "In summary" | 旧版规范 |
| 与摘要的关系 | 不逐句复述摘要；可呼应，但必须有摘要之外的信息（机制、覆盖范围、意义） | 反例：《Residual Diffusion Bridge Model》几乎逐句照抄摘要；《LaRender》《SparseFlex》结论首句与引言逐字重复 |
| 数字 | 不引入新数字；出现的数字必须与摘要、引言、实验一致 | 旧版规范；story_types §3.7 |
| 单条局限 | **适用边界 + 后续方向**，一两句；根因可以省略 | `anti_defensive.md` §5；《BridgeDepth》《SLARM》《FluoCLIP》 |
| 局限从哪来 | 方法的假设、依赖的外部组件、数据与采集条件、计算代价；挑与核心主张最相关、审稿人一定会想到的两条 | 《BiMotion》fixed-mesh assumption；《Ov3R》继承 3R 模型的位姿误差 |
| 不利结果 | 不主动示弱，不说输。按 `anti_defensive.md` §3 的顺序处理：删 → 收缩主张 → 换口径 → 解释为取舍 → 重组 → 重构故事 → 最后才直接说明。不在局限里重新提起正文已经收缩掉的比较 | 底线：结论里的主张不越过表格。反例：《Proxy-GS》正文说"效果因场景而异"，结论却写 "establishing a new state-of-the-art" |
| 未来工作 | 每条对应一条局限，写出具体技术路线或具体对象 | 《SLARM》《OccuFly》《PhyGaP》《FluoCLIP》 |
| 结尾句 | 全文最后一句落在意义上：有依据的意义陈述。不以局限收尾，也不用空泛的 "We hope ..." 收尾 | 反例：《Cubic Discrete Diffusion》《EnergyAction》《ESSENTIAL》 |
| 局限放附录 | 可以。详细讨论放补充材料，正文最多留 1–2 条，一句话写成"边界 + 方向" | 正例：《LBM》正文一句 "need to have access to existing couplings of images beforehand" |
| Discussion 小节 | 可选，不作为默认推荐。只在需要提炼发现、回答替代解释或说明伦理风险时使用；不用来展开局限 | 《CAD》Discussion 自问"提升是否只来自外部先验"；《Hearing the Room Through the Shape of the Drum》§8 单列社会影响 |

---

## 1. 这一章要完成什么，与其他章节的分工

### 1.1 四个任务

1. **收束（Conclusion）**：用两三句回收全文主张，即解决了什么问题、靠什么机制解决、效果如何，再说一句这说明了什么。结论只强化记忆点，最后一句落在意义上。
2. **划边界（Limitations，可选）**：最多 2 条，每条一两句，写出方法的适用边界（假设条件、依赖、代价）和后续方向。这不是自我审查报告，不主动示弱（`anti_defensive.md` §5）。
3. **指方向（Future Work）**：从局限推出具体的下一步，不写愿景。
4. **讨论（Discussion，可选）**：把实验里分散的现象提炼成几条结论，讨论替代解释或社会影响。

### 1.2 与其他章节的分工

| 章节 | 它负责的 | 本章不要重复的 | 本章要回收的 |
|---|---|---|---|
| 摘要 | 问题、方法、核心数字 | 不逐句复述 | 核心数字（口径一致） |
| 引言 | 方法定义句、洞察句、贡献列表 | 不重新铺背景和动机 | 方法定义句（同一措辞，见 `naming.md`）；贡献条数前后一致（反例：Bokehlicious 摘要说 threefold，结论只提到 two） |
| 方法 | 设计与假设 | 不再讲模块细节，不写公式 | 方法里的**假设**，这是局限最主要的来源 |
| 实验 | 证据、效率数字 | 不引入实验里没有的数字 | 核心数字和最强结果；主张强度与实际排名一致（不是第一的地方收缩主张，不专门写一句输了） |
| 附录 / 补充材料 | 失败案例、更多讨论 | — | 正文如写局限，最多 2 条 |

### 1.3 与实现一致，先讲直觉

- 结论里说的机制、适用范围和数字，都要能在实验表、代码或配置里找到对应（`word_style.md` 原则 12）。例如结论说"支持动态场景"，实验里就必须有动态场景的结果。
- 升华不能超出实验支撑范围。反例：《Curvature-Aware Captioning》结尾写 "laying a solid foundation for embodied AI applications"，正文却没有任何具身实验。
- 结论用文字讲清机制和洞察，不放公式；需要回指时用方法名或模块名。

---

## 2. 组织方式：常见结构及适用场景

### 2.1 五种常见结构

| 结构 | 形式 | 适用场景 | 例子 |
|---|---|---|---|
| A. 局限在前、结论收尾 | 加粗 "**Limitations.**" 短段或短小节放在 Conclusion 之前，1–2 条；最后一节是 Conclusion | **默认推荐**，篇幅允许时首选 | 《PRM》"5. Conclusion and Limitation"（局限在前，结论在后）；《ReFlex》"6 Limitations and Conclusion"；独立 Limitations 节的例子还有《RnG》第 5 节、《Rethinking Model Selection》第 7 节、《BUFFER-X》5.4、《NeuFrameQ》第 6 节、《STAC》"Limitation." 加粗小标题（这些论文的条数和位置各不相同，照搬时按本 skill 口径压到 2 条以内、放在结论之前） |
| B. 合并小节 | "Conclusion and Limitations" / "Conclusion and Future Works"，局限一两句嵌在结论中间，结论最后一句仍落在意义上 | 页数紧张时的默认做法 | 《STARFlow-V》《Gallant》"Conclusion & Limitations"；《DIMO》 |
| C. Discussion 节 + 短 Conclusion | Discussion 讲替代解释、适用条件、社会影响，Conclusion 做正面收束 | **可选，不作为默认推荐**。发现-解释型需要提炼发现；有伦理或隐私风险 | 《CAD》Discussion 自问"提升是否只来自外部先验"；《Hearing the Room Through the Shape of the Drum》第 8 节"Discussion and limitations"并单列社会影响 |
| D. 一段合一 | 一段里先收束、再用一两句写边界、最后回到结论和意义 | 篇幅极紧 | 《E-RayZer》"While our results are promising, we identify several limitations..." 之后接 "Despite these limitations, E-RayZer outperforms prior..." |
| E. 失败案例小节 | 实验末尾单列失败案例，配图 | **可选，不作为默认推荐**。失败案例放补充材料即可 | 《TriLite》4.8 "Failure cases and Future Directions"；《DeX-Portrait》Fig.12；《Fine-structure Preserved ISR》Fig.6 |

**不推荐的结构**：
- 以局限收尾：不单设结论，最后一节只写 "Limitations and Future Work"（《Learning Convex Decomposition via Feature Fields》"5. Limitations and Future Work"；《MeshLLM》编号 1–4 条；《Unified Vector Floorplan Generation》）。全文最后落在不足上，改用结构 A 或 B。
- 没有结论节，实验后直接进致谢（《MetaSpectra+》；《Vista4D》在 Applications 之后直接进 Acknowledgements）。
- 局限写成长清单，或在 Discussion 里逐条展开局限。

**选择规则**：
1. 默认选 A；页数紧就选 B 或 D。不论哪种结构，局限最多 2 条，每条一两句。
2. 需要讨论替代解释、社会影响时可以加 C，但它不是默认结构，也不用来展开局限。
3. 失败案例小节（E）可选，不作为默认推荐；失败案例放补充材料即可。
4. 附录可以放详细讨论；正文若写局限，只留最相关的 1–2 条。
5. 全文最后一句落在意义上，不以局限收尾。

### 2.2 按故事类型的差异

叙事类型的判断见 `story_types.md` 第 2 节。各类型收尾的重点不同（局限一律最多 2 条，写成"边界 + 方向"）：

| 类型 | 局限写到哪里 | 正例 | 反例 |
|---|---|---|---|
| 瓶颈突破型（56.0%） | 写到**所修环节的适用边界**：修好的环节依赖什么假设、在什么条件之外尚未覆盖 | 《HairCUP》局限各配一个 because；《Gallant》把边界落在 LiDAR 10Hz 的感知延迟上；归因模板 "We attribute this limitation to X, which is sufficient for Y but ineffective for Z."（《SuperDec》） | 结论的主张越过表格：只有部分指标领先，却写成全面领先（见 §4 第 2 条） |
| 新问题定义型（11.0%） | 写**新设定本身的假设**，挑最关键的一两条编号 | 《SceneMI》用 (i)(ii)(iii) 编号列假设（照搬时只取最关键的两条）；《FluoCLIP》一句里完成边界与方向；《Teeth Reconstruction》把依赖 SAM2 定性为正交技术可解（可用 Personalize-SAM 自动化）；结论常用 "paving the way for ..." 收尾 | 《FGAesQ》只写 "remains challenging"，读者不知道边界在哪 |
| 统一框架型（10.8%） | 写统一之后仍**覆盖不到的场景或模态** | "struggles with occluded structures in limited-view training and deformable scenes"（《HiNeuS》）；"may underperform under extremely fast dynamics"（《AeroGS》）；依赖针孔相机模型（《AAA-Gaussians》）；让步模板 "Although our study focuses on X, Y is modality-agnostic."（《SGDIR》《x2-Fusion》） | 《Residual Diffusion Bridge Model》结论几乎逐句照抄摘要；《MSPT》《GeniNav》《HR-NVC》结论与摘要或引言同构 |
| 发现-解释型（10.7%） | 写**发现成立的前提**（数据范围、模型族、设定）；可选设 Discussion 提炼发现 | 《GRPO-Guard》写明方法的作用边界（缓解而非消除 reward hacking）及其根因；《PercHead》把贡献升华为挑战一个假设 | 《KDAS》《ViT3》《FedAdamom》结论是摘要的同义改写；层层叠加限定语 "potentially / could be / a hint"、"seems plausible...may"，读起来心虚（`anti_defensive.md` §4） |
| 数据与基准型（7.0%） | 写到**数据集自身的覆盖范围**：规模、采集条件、覆盖场景 | 《EgoXtreme》依赖 OptiTrack，只能在室内专用场地采集；《Wanderland》采集频率 1 FPS、只建模静态环境，并给补救方向；《WorldLens》把评测发现写成 "Guidelines for Future World Model Design"；结论首句可呼应引言（"We introduced GeoMMBench..."），但后面必须有新信息 | — |
| 能力扩展型（2.4%） | 写扩展之后**仍未覆盖的部分**，克制而具体 | 《Anatomica》两点局限；《STARFlow-V》"(1) Latency (2) Data quality"，各配 future work | 《PET-DINO》"We hope this work can provide new insights..." 空泛收尾 |
| 效率优化型（2.0%） | 把局限绑定到**加速所依赖的设计假设** | 《AdaptVision》绑定"单一工具 / 固定 1/4 分辨率 / 两轮"；《Sparse-LaViDa》写明需要额外训练；《EDM》写明优势随分辨率升高而收窄；《ScoreLiDAR》《Turbo-GS》局限针对性强、不夸大 | 《SwiftTailor》《TurboVSR》只写 "we leave this for future work"，没说边界在哪 |
| 理论分析型（0.2%，仅 2 篇） | 写**定理成立的条件**：在定理处写明，局限段里一句话点出后续方向；不前置到引言 | 《C²FG》结论仅 5 句、不含数字，逐字呼应引言和贡献措辞；《PLMP》结论再点一次未来方向（partial visibility） | — |

---

## 3. 逐部分写法

默认顺序：Limitations 短段（最多 2 条，边界 + 方向）→ 结论首句 → 机制与证据 → 意义（全文最后一句）。结构 B、D 把局限一两句放在结论中间（机制与证据之后、意义句之前）。

### 3.1 结论首句：回收方法定义句，补上摘要之外的信息

**写什么**：方法名 + 类别 + 机制 + 解决的问题，与引言里定义方法的那句话用同一措辞（方法名措辞统一见 `naming.md`）。

**怎么写**：
- 可以呼应摘要或引言，但不能逐字照抄。呼应句的后半句，或者紧接的下一句，要带上摘要里没有的信息，例如关键机制、覆盖范围或意义（story_types §3.6）。
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

**注意**：强度词必须与实验排名一致。只拿到第二名的指标不能写成全面领先；"achieves true real-time, high-fidelity, and consistent..."（《ChordEdit》）这种全无保留的写法要避免。不是第一的地方收缩主张（"achieves the best results on 4 of 5 benchmarks"、"is competitive with X while being 3× faster"），不需要专门写一句"我们在这里不如 X"（`anti_defensive.md` §3）。强度和限定语的规则见 `word_style.md` §2.2。

### 3.3 意义句：升华到"说明了什么"，但不超出证据

**写什么**：这项工作改变了什么认识，或者把领域从哪里推到了哪里。

**三种可用写法**：
1. **认知层面**：把贡献从"效果更好"升华为"推翻了一个假设"。"This challenges the prevailing assumption that conventional image losses...are necessary for supervision"（《PercHead》）。
2. **范式定位**：用 "from X to Y" 说明转变。《Relightable Holoported Characters》(RHC)："marks a step change in human relighting—from static, replay-based, or pose-driven avatars ... to dynamic, photorealistic humans..."
3. **克制定位**：第一次做某件事时，定位为向某个目标迈出的一步。"GameFactory marks our first effort in this field"（《GameFactory》）；"an important step toward direct object pose estimation..."（《PoseGAM》）。

**边界**：
- 意义句的范围不能超出实验。反例：《Curvature-Aware Captioning》"laying a solid foundation for embodied AI applications"（无具身实验）；《Variance-Based Pruning》升华到 "democratization of deep learning"。
- 结论讲本文做成了什么，不要把篇幅花在他人方法的缺点上：《Towards Multimodal Domain Generalization with Few Labels》结论写 "highlighted the limitations of existing SSML, MMDG, and SSDG paradigms"，前人的局限应留在引言和 Related Work。

### 3.4 局限段：适用边界 + 方向（最多 2 条）

#### (1) 开篇句

局限只有一两句时，通常不需要开篇句，直接写边界。需要开篇句时，用中性的承接：
- "Despite its effectiveness, [Method] has several limitations that outline directions for future research."（《AdaptVision》）
- "While X delivers consistent gains across architectures and datasets, several limitations suggest fruitful avenues for future work."（《BoostSLT》）
- "While our results are promising, we identify several limitations and directions for future work"（《E-RayZer》）

只写两条时，把 "several" 换成具体的条数或直接删去。

#### (2) 单条局限的两个要素

每条局限回答两个问题：**方法在什么范围内成立 → 下一步往哪走**。根因可以省略；需要让读者看出边界从哪来时，用半句点到对应的假设或组件即可。

| 要素 | 写法要求 | 原句与出处 |
|---|---|---|
| 适用边界 | 写清方法依赖的假设、条件或范围，具体到场景类型、参数范围或组件 | "may compromise accuracy at high resolutions (≃2K)"（《BridgeDepth》）；"struggles with complex materials like glass or mirrors"（《SLARM》）；"exhibits limitations when applied to videos captured at extremely low frame rates"（《RetimeGS》）；"does not support topology-changing motion due to our fixed-mesh assumption"（《BiMotion》） |
| （可选）根因 | 半句点到机制或假设，说明边界从哪来 | "due to its reliance on photometric consistency"（《SLARM》）；"due to the inherent constraints of optical flow"（《RetimeGS》）；"due to deeper feature extraction layers"（《EDM》） |
| 方向 | 点名具体技术、模块或对象 | "Future work could address this via a stereo feature interaction module."（《BridgeDepth》）；"Future work will explore self-calibration and more realistic scene representations..."（《SLARM》）；"integrating techniques from the SLAM literature, such as global bundle adjustment"（《Ov3R》）；点名扩展对象 "(e.g., TransUNet or Swin-UNet)...this direction remains to be explored in future work."（《AD-GBC》） |

边界与方向写在一两句里的例子：
- "Our method assumes a calibrated camera rig; extending it to uncalibrated setups is a natural next step."（`anti_defensive.md` §5）
- "We focus on static scenes; handling dynamic objects is left for future work."（`anti_defensive.md` §5）
- "our implementation may compromise accuracy at high resolutions (≃2K) where large disparity ranges strain the top-k hypothesis selection in the Disparity Proposal Network. Future work could address this via a stereo feature interaction module."（《BridgeDepth》）
- "But our Gaussian pose assumption is a key limitation, as the non-linear 2D-to-6D transformation challenges its coverage guarantees, which we will address by exploring more suitable distributions."（《Deterministic Object Pose Confidence Region Estimation》）

#### (3) 去哪里找局限

逐项翻一遍，挑与核心主张最相关、审稿人一定会想到的**两条**，其余不写：

| 来源 | 怎么找 | 例子 |
|---|---|---|
| 方法的假设 | 方法节里所有 "we assume"、固定超参数、固定结构 | 《BiMotion》fixed-mesh assumption；《DDiT》"for a given timestep, we use a fixed patch-size"；《Revisiting the Necessity of Full Accuracy》"it is limited to correcting non-translational noise"；《Cov2Pose》"does not explicitly handle object symmetries"；《Diffusion-Based Native Adversarial Synthesis》只在图像空间挖噪声、依赖扩散模型生成 on-manifold 样本 |
| 适用边界 | 实验覆盖了哪些设备、光照、领域 | "our conclusions are only applicable to smartphones and under good lighting conditions"（《RAW-Domain》）；"in domains such as graph learning...our conclusions do not yet transfer."（《FILTR》） |
| 依赖的外部组件 | 预训练模型、位姿、伪标签来源；可以把局限归因到底层组件 | "Ov3R inherits one of the limitations of 3R models, i.e., the suboptimal accuracy of the retrieved camera poses"（《Ov3R》）；"the generation of pseudo-labels is constrained by the LVLM"（《Learning to Track Instance...》）；依赖 GGHead 先验（《SketchFaceGS》）；位姿仍靠 COLMAP（《Thermal is Always Wild》） |
| 数据与采集 | 数据规模、多样性、采集设备和场地 | "due to the limited variety of leaf species in our DeformLeaf dataset, the model struggles to cover certain unique types of leaf deformations"（《NeuraLeaf》）；依赖 OptiTrack、只能在室内专用场地采集（《EgoXtreme》）；1 FPS、只建模静态环境（《Wanderland》） |
| 计算代价 | 推理时间、显存、训练成本、实时性 | "it currently cannot meet real-time requirements due to its iterative guidance"（《WorldForge》）；"a full evaluation...required 6.7 hours on a single NVIDIA GTX 4090 GPU"（《TouchDream》）；需要额外训练（《Sparse-LaViDa》）；LCD 调制器约 60Hz 的物理上限（《240FPS Stereo Vision》） |

实验里的不利结果不从这里进局限：按 `anti_defensive.md` §3 处理（删、收缩主张、换口径、解释为取舍、重组实验），也不在局限里重新提起正文已经收缩掉的比较。

#### (4) 需要时，用一个数字划清边界

- 一个数字能让边界的范围一目了然时再给：《Revisiting Geometric Obfuscation》(DCL) 用 "only 4/17,000 images in 7Scenes" 说明退化场景很少见；《Stereo Any Video》用 Table 6 的参数量和显存说明计算代价。
- 失败案例图可选，放补充材料即可（《DeX-Portrait》Fig.12；《Fine-structure Preserved ISR》Fig.6）。

#### (5) 两条局限的排版

- 用 First / Second 或 (i)(ii)，每条一句边界 + 一句方向：《OccuFly》局限各配补救（静态场景假设 → 4D Gaussian Splatting；标注需人工 → 更鲁棒的 2D 伪标签）；《SketchFaceGS》各附缓解方向，例如 "we aim to mitigate this with identity consistency losses or advanced encoders"。
- 方向可以引用一篇已有工作作为可行路径：《PhyGaP》引用 "GaussProbe in TransparentGS [24]"。
- 可以给**使用建议**，而不只是指出边界："We therefore recommend building S from a small set of well-established, complementary strategies rather than arbitrarily including numerous ones."（《Cleaning the Pool》）

#### (6) 措辞：中性，不自我削弱

- 不确定时用 may 留余地："it assumes relatively smooth motion and may underperform under extremely fast dynamics or highly cluttered scenes"（《AeroGS》）。一条局限加一处限定就够，不层层叠加 may / potentially。
- 用 unless 写出条件："may fail to represent high-frequency details for very complex motions unless more control points are used"（《BiMotion》）。
- 写成前提条件："The main limitation...is that it requires a reasonable initialization for a subset of the cameras."（《On the Recovery of Cameras from Fundamental Matrices》）。
- 开放问题："remains an open problem"（《Electromagnetic Inverse Scattering》《E2EGS》）；"It remains an open question, however, whether..."（《Inter-Photon-Limited Videography》）。
- 不用自我削弱词：unfortunately、we must acknowledge、still lags far behind、limited improvement、only achieves（`anti_defensive.md` §4；`ai_words.json` 的"自我削弱"类别）。不写情绪化的自我评价（"我们的方法仍有很大不足"）。hedge 词的具体用法见 `word_style.md`。

#### (7) 哪些"正面转化"可以用，哪些是多余的辩护

局限已经写成中性的"边界 + 方向"，就不需要再贴标签或辩护；辩护越长，越把读者的注意力引向不足（`anti_defensive.md` §7：不主动扩大攻击面）。

| 可以用（有数据或逻辑支撑） | 不要用（多余的标签或辩护） |
|---|---|
| 同一属性的两面："While FlowEdit's strong structure preservation is beneficial for precise editing tasks, it can become a limitation when substantial modifications to large regions of the image are desired."（《FlowEdit》） | 贴"次要"标签："One minor limitation of our approach is that..."（《ANTS》） |
| 实验里确实能看到权衡时，定性为权衡（`anti_defensive.md` §3 第 4 步）：《R²-Seg》把 sensitivity 下降写成 "an explicit calibration trade-off" | 给局限改名："We consider this a promising extension rather than a core limitation"（《SuP》） |
| 先写清边界，再说明可以推广："As a direction for future work, the MLOO formulation is applicable to other population-based metrics beyond RMM."（《RLFTSim》） | 列完就否定："Nevertheless, these are not fundamental limitations and can be alleviated with better data and supervision"（《CUPID》）。有具体缓解路径时，直接写成方向 |
| 在局限之后向业界提建议："we hope this work encourages LiDAR manufacturers to make future sensing pipelines more programmable"（《Lidar Waveforms》） | 写完局限再用大段论证开脱：《PETAR》先说 "A feature of our method is the requirement of mask inputs..."，随即用 FDA-cleared 工具的可行性展开辩护 |
| 把评测发现写成正向准则（数据与基准型）：《WorldLens》"Guidelines for Future World Model Design" | 说成"大家都有这个问题"："A limitation of X is Y, a challenge widely shared by representative works in the field... Despite these challenges, X stands as a pioneering contribution."（《Derm1M》） |

### 3.5 未来工作：与局限一一绑定

**写什么**：每条方向都从一条局限推出，点名具体技术、对象或量级。

**模板**：
- 一句内完成边界与方向："While FluoCLIP assumes predefined stain categories, future work will explore automatic stain discovery..."（《FluoCLIP》）
- 逐条绑定：《SLARM》局限与未来工作逐条对应；《Thermal is Always Wild》两条局限各给根因（光度稳定未与重建联合优化；位姿仍靠 COLMAP）和方向（"future end-to-end formulations"、"more robust, thermal-aware pose estimation methods"）。
- 点名对象："Future work will extend AoD-IP to broader tasks (e.g., VQA and image generation) and explore more diverse datasets and architectures..."（《Authorize-on-Demand》）；"new evaluation benchmarks that more accurately reflect real-world long-context retrieval...(e.g., matching images to multi-paragraph document pages, such as textbooks and reports)"（《CLIP Is Shortsighted》）。
- 点名技术："adaptive scheduling of refinement depth, incorporating stronger physical priors...extending...to other dense correspondence problems"（《MorphSeek》）；anytime-valid e-processes / 更丰富的谱密度族 / 分布偏移扩展（《Spectral Conformal Risk Control》）。
- 给量级：从 "≈10 agents" 到 "≈100 agents"（《Unified Number-Free Text-to-Motion》）。
- 排比列 2–3 条："While our approach represents an advance in X, several avenues for future work remain. First..., Second..., Finally..."（《EventUPS》：非朗伯体表面、学习式组件、动态场景重建）；"A promising direction.../Another important avenue.../Finally, we envision..."（《BLADES》）。
- 划清边界："These optimizations are orthogonal to our current work"（《MeshLLM》）；"We leave developing effective sample ranking methods as future work."（《DexVLG》）。

**注意**：
- 方向句最好带上边界半句。《VIRD》只写 "Future work will extend this approach to more challenging 6-DoF pose estimation tasks..."，读者要自己推断方法限于 3-DoF 地面场景；改成 "We focus on 3-DoF ground-level scenes; extending to 6-DoF pose estimation is left for future work." 一句就同时交代边界和方向。《AIM》"We plan to extend AIM to Vision Transformers..."、《GECKO》"扩展到泛癌种"同理。
- 方向要具体，不写 "extend this work to other modalities" 这类空话（《SPDMark》"Future directions could extend this work to other generative modalities."）。

### 3.6 Discussion 小节（可选，不作为默认推荐）

**什么时候写**：发现-解释型需要把分散的现象提炼成几条结论；需要回答"提升是否来自别的因素"；有隐私、伦理风险。

**写什么**：
- **替代解释**：主动自问读者会怀疑的来源，例如 Discussion 里自问"提升是否只来自外部先验"（《CAD》），并用实验排除。
- **社会影响**：《Hearing the Room Through the Shape of the Drum》在 "Discussion and limitations" 里单列社会影响。伦理说明与技术边界分开写。
- **认识层面的收获**：对发现-解释型，把核心发现写成一句可以被引用的结论（参考《PercHead》的写法）。

**不写什么**：Discussion 不用来展开局限。局限按 §3.4 写在 Limitations 短段里，最多 2 条。

### 3.7 结尾句

全文最后一句落在意义上。按优先级选一种：
1. **有依据的意义陈述**（§3.3 的三种写法之一）。
2. **克制的收尾**："We believe that hierarchical material recognition can help intelligent systems perform more sophisticated tasks..."（《Hierarchical Material Recognition》）。

不以局限或未来工作收尾。不要用以下句子单独收尾（它们不含信息，替代不了意义句）："We hope this work will inspire future research on unified multimodal architectures."（《Cubic Discrete Diffusion》）；"We hope this dataset and analysis motivate future research to address these challenges."（《Beyond Single Images》）；"We hope this work provides valuable insights for the robotics community..."（《EnergyAction》）；"We hope this work inspires future research in video class-incremental learning."（《ESSENTIAL》）；"We anticipate that ZoomEarth will form the foundation for..."（《ZoomEarth》）。

### 3.8 骨架示例（结构 A，占位符替换成自己的内容）

```
\paragraph{Limitations.}
[Method] assumes [condition / assumption]; extending it to [broader setting] is a natural next step.
[Optional second: We focus on [scope]; [specific technique / object] is left for future work.]

\section{Conclusion}
We introduced [Method], a [property] framework that [solves problem] by [mechanism in words].
[One sentence: the key insight, e.g., "This gain is achieved not by sacrificing X, but by Y."]
Across [tasks/datasets], [Method] [result with the same number as in the abstract].
[One sentence of significance, bounded by the experiments — the last sentence of the paper.]
```

结构 B 把 Limitations 的一两句移到 "Across ..." 之后、意义句之前，意义句仍是最后一句。

---

## 4. 常见问题与反例

| # | 问题 | 反例 | 改法 |
|---|---|---|---|
| 1 | 结论是摘要、引言或贡献列表的同义复述 | 《RF4D》没有新内容也没有展望；《FlexMem》被批"第四次近似重复"；《ViT3》复现摘要三段式；《TeHOR》；《Discontinuity-aware Normal Integration》只有 3 句重述加 1 句致谢 | 首句回收定义句，后面加机制、覆盖范围、意义等摘要之外的信息 |
| 2 | 主张越过证据 | 《Proxy-GS》正文说"效果因场景而异""顶点噪声超过 5% 质量下降"，结论却写 "establishing a new state-of-the-art"；摘要或结论说全面领先，表格里并非如此 | 收缩主张（`anti_defensive.md` §3 第 2 步），措辞强度与实际排名一致；不需要专门写一句"我们在这里不如 X" |
| 3 | 局限写成长清单或自我否定 | "we must acknowledge that ... these results should be interpreted with caution"（`anti_defensive.md` §1 的防御性例句）；局限列到三四条以上 | 压到最多 2 条，每条一两句"边界 + 方向"；删掉自我削弱词 |
| 4 | 全文以局限收尾 | 最后一节只写 Limitations and Future Work（《Learning Convex Decomposition via Feature Fields》《MeshLLM》《Unified Vector Floorplan Generation》） | 局限移到结论之前，最后一句换成意义句（§3.7） |
| 5 | 只有方向、没有边界，或方向空泛 | 《SwiftTailor》《TurboVSR》只写 "we leave this for future work"；《SPDMark》"extend this work to other generative modalities" | 一句话同时写出边界和具体方向（§3.5） |
| 6 | 局限后面跟标签或大段辩护 | 《ANTS》"minor"；《SuP》"rather than a core limitation"；《CUPID》"not fundamental limitations"；《PETAR》大段开脱；《Derm1M》"widely shared" | 删掉标签和辩护，局限写成中性的边界 + 方向；有具体缓解路径时直接写成方向（§3.4(7)） |
| 7 | 局限写得太抽象 | 只写"还有改进空间"（旧版规范）；《FGAesQ》只写 "remains challenging"；《SAQN》"We anticipate that future work will address this issue." 一句带过；《Drainage》 | 写出具体的假设、条件或组件，再给具体方向 |
| 8 | 升华超出实验支撑 | 《Curvature-Aware Captioning》"embodied AI"；《Variance-Based Pruning》"democratization of deep learning" | 意义句只谈实验覆盖到的范围 |
| 9 | 用 we hope / we believe 的空话收尾 | 《Cubic Discrete Diffusion》《LLMind》《EnergyAction》《ViterbiPlanNet》《ActiveAD》《SenCache》；"a versatile representation, with promising properties that can benefit future applications..."（《Representing 3D Faces》） | 按 §3.7 换成有依据的意义句 |
| 10 | 语气过分自信，主张强于证据 | "ChordEdit achieves true real-time, high-fidelity, and consistent generative image editing."；"Extensive experiments demonstrate..."（《GeniNav》） | 按 `word_style.md` §2.2 调整强度，绑定到具体数字 |
| 11 | 结论花在他人方法的缺点上 | 《Towards Multimodal Domain Generalization with Few Labels》 | 结论讲本文做成了什么；前人的局限留在引言和 Related Work |
| 12 | 数字或贡献条数前后不一致 | 《AsymLoc》95% / 95.5% / 96%；《Counterfactual VLA》摘要 20.5%，正文 14.7%；Bokehlicious threefold vs two | 结论里的每个数字回查摘要和实验表 |
| 13 | 语法或逻辑瑕疵 | "Our work establishes opens up future research..."（《A Style is Worth One Code》） | 定稿前按 `word_style.md` §7 通读 |

---

## 5. 写作步骤与检查清单

### 5.1 写作步骤

1. **收集素材**：从引言抄出方法定义句和贡献条数；从摘要抄出核心数字；从方法节列出主要假设和依赖（局限的候选）；从实验节确认每个指标的实际排名（决定主张强度）以及运行时间和显存；与用户确认代码或实验记录里的数字（`word_style.md` 原则 12）。
2. **定结构**：按 §2.1 的选择规则选 A–E，按 §2.2 确认本类型的局限重点。
3. **筛局限**：从 §3.4(3) 的来源表里最多选 2 条，挑与核心主张最相关、审稿人一定会想到的。优先选：方法的核心假设 > 依赖的外部组件 > 计算代价 > 数据与采集条件。实验里的不利结果按 `anti_defensive.md` §3 处理，不搬进局限。
4. **逐条写**：每条写成"适用边界 + 方向"，一两句；根因需要时用半句带出。
5. **写结论**：首句回收定义句 → 机制与证据两三句 → 一句意义（不超出实验）。每个比较性主张回查表格，不是第一的地方收缩主张。
6. **写未来工作**：每条从一条局限推出，点名技术或对象；通常就是局限的后半句。
7. **写结尾句**：按 §3.7 选；最后一句落在意义上，不是局限，也不是空泛的 we hope / we believe。
8. **对照检查**：跑一遍 5.2 的清单。

### 5.2 检查清单

**结构**
- [ ] 局限不超过 2 条，放在结论之前的 Limitations 段或结论中间；摘要、引言里没有局限，局限不是全文最后一句
- [ ] 用了 Discussion 时，它没有用来展开局限

**结论**
- [ ] 首句回收了引言里的方法定义句，方法名措辞与全文一致（见 `naming.md`）
- [ ] 没有逐句复述摘要，有摘要之外的信息（机制、覆盖范围或意义）
- [ ] 没用 "In conclusion" / "In summary" 开头
- [ ] 没有新数字、新结论；出现的数字与摘要、引言、实验一致；贡献条数前后一致
- [ ] 机制用文字表述，没有公式
- [ ] 意义句的范围没有超出实验；强度词与实际排名一致（见 `word_style.md`）；不是第一的地方收缩了主张，没有专门写一句输了

**局限**
- [ ] 每条写成"适用边界 + 方向"，一两句
- [ ] 边界写到了具体的假设、条件或组件，不是"能力不足""还有改进空间"
- [ ] 没有自我削弱词（unfortunately、we must acknowledge、still lags far behind、limited improvement 等，见 `anti_defensive.md` §4），没有在局限里重提正文已经收缩掉的比较
- [ ] 没用 "minor"、"not fundamental"、"rather than a core limitation" 等标签，也没有大段辩护
- [ ] 有伦理或隐私风险时单独说明

**未来工作与结尾**
- [ ] 每条未来工作对应一条局限，点名了具体技术、对象或量级
- [ ] 方向句带上了边界，不是孤零零的 "we leave this for future work"
- [ ] 最后一句是有依据的意义陈述，不是局限，也不是单独的 "We hope this work will inspire..."
