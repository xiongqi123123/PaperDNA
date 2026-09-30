# 顶会论文的用词、风格与写作灵魂

> 用途：论文写作 skill 的参考规范，也是跨章节写作原则和去 AI 味规则的唯一来源。读者是正在写论文的 AI 助手：写摘要、引言、方法、实验、结论时，按本文档的原则、默认值、模板和检查清单执行；各章节的具体写法见 `references/sections/`，叙事类型见 `references/story_types.md`，给方法起名按 references/naming.md 执行。
> 证据来源：1040 篇 CVPR 2026 / ICCV 2025 论文精读笔记（best 9 篇、oral 195 篇、highlight 836 篇）的统计文件 `references/corpus_stats.md`，以及约 50 批"用词与风格"分批归纳合并后的 6 份汇总。括号里的论文名是出处。英文模板中的 X / Y / Z / N 是占位符，不是论文原句；标注了论文名的英文句子是论文原句或原词。第 1 节原则 11–15 和第 4 节是通用写作规范，没有逐条附语料出处。
> 优先级：第 1 节（写作原则）> 第 5 节（风格默认值）> 其余各节。规则之间冲突时，按"证据支撑的强度优先于修辞效果"裁决。
> 按需读取：写或改任何正文前读第 1 节和第 4 节；润色时读第 1、4、5 节；选词和定结论强度看第 2、3 节；定稿前按第 7 节逐条检查。
>
> 目录：0. 先看数字 ｜ 1. 写作灵魂：15 条原则 ｜ 2. 用词 ｜ 3. 需要警惕的词 ｜ 4. 去 AI 味：不要怎么写 ｜ 5. 风格参数 ｜ 6. 借鉴写法与常见问题 ｜ 7. 定稿前总检查清单

---

## 0. 先看数字：这些论文长什么样

| 维度 | 统计值（n=1040） | 对写作的含义 |
|---|---|---|
| 故事类型 | 瓶颈突破型 56.0%，新问题定义型 11.0%，统一框架型 10.8%，发现-解释型 10.7%，数据与基准型 7.0%，能力扩展型 2.4%，效率优化型 2.0%，理论分析型 0.2% | 默认按"瓶颈→方案→验证"写；各类型的取名差异见 references/naming.md |
| 摘要句数 | 中位数 8，四分位 [7, 9]；8 句 25.2%、7 句 19.8%、9 句 18.2%；少于 5 句或多于 11 句的合计不到 3% | 摘要默认写 8 句，允许 7–9 句 |
| 摘要第 1 句作用 | 背景 56.6%，背景+问题 21.2%，背景+缺口 7.3%，直接写方法 6.6% | 第 1 句写背景，最好同一句带出问题 |
| 摘要最后 1 句作用 | 资源发布 43.1%，结果+意义 17.9%，结果 12.0%，意义 10.4%，结果+泛化 6.1% | 最后一句写代码/数据发布；不发布资源就写"结果+意义" |
| 摘要五等分位置的主作用 | 第 1 段：背景 57%，问题 18%，缺口 11%；第 2 段：方法 44%，缺口 18%；第 3 段：方法 38%，设计细节 35%；第 4 段：结果 40%，方法 23%；第 5 段：结果 42%，资源发布 37%，意义 12% | 方法最迟在摘要前 40% 处出现 |
| 最常见摘要作用序列 | 背景→缺口→方法→设计细节→结果（2.5%）；背景→问题→方法→设计细节→结果（2.1%）；以上两种加"→资源发布"（1.9%、1.7%） | 序列极分散，单一模板占比不超过 2.5%，但骨架都是"背景→（问题/缺口）→方法→细节→结果" |
| 引言段数 | 中位数 6，四分位 [5, 6]；5 段 29.1%、6 段 27.1%、4 段 16.9%、7 段 15.6% | 引言默认写 5–6 段 |
| 贡献列表形式 | bullet 74.4%，行内 25.0%，没有贡献列表 0.6% | 默认用 bullet 贡献列表 |
| 第一页 teaser 图 | 有 91.3% | 默认准备 Figure 1，并在引言中引用 |
| 贡献类型组合 | Capability+Performance 24.9%，Insight+Performance+Capability 21.2%，Insight+Performance 19.6% | 过半论文把 Insight（洞察）列为贡献，只有性能提升的论文是少数 |

---

## 1. 写作灵魂：15 条原则

写任何章节都适用。默认读者是审稿人，他们关心五件事：新意是否清楚（novelty）、论证是否严谨（rigor）、能否复现（reproducibility）、结论有没有证据（evidence）、读的时候会不会困惑。下面的原则分别回应这五件事。

每条原则都附一个"检查动作"，写完一节就按它自查。

### 原则 1：新意在第一页交代清楚
- 摘要第 2/5 段就进入方法（占 44%），91.3% 的论文在第一页放了 teaser 图。读者不应该读到第二页才知道"你做了什么、和别人哪里不同"。
- 正例：`We propose X, a Y that Z`（ChordEdit），一句话同时给出名字、类别和机制；AMB3R 把反直觉的证据放在前面，再用短句反转："In practice, this is not the case."
- 反例：背景铺陈超过摘要一半，方法句出现在第 5 句以后；或者方法句只有"a novel framework"，没有写机制。
- 检查动作：只读摘要前 3 句和 Figure 1 的图注，能不能复述出"方法是什么 + 靠什么机制起作用"？不能就改。

### 原则 2：强词必须和数字绑在一起
- 9/9 批次的一致铁律：state-of-the-art / significantly / consistently / outperforms 后面必须紧跟数字、对比对象或适用范围。
- 正例：`+0.3%, +2.2%, +2.9%`（TF-CADE）；`up to +2.7/+6.9 mAP`（DetGain）；效率 claim 直接给数字，不用形容词（Native and Compact Structured Latents，LagerNVS 的 "30FPS+"）。
- 反例："catastrophic" 对应的只是 +0.29 个百分点（AD-GBC）；"staggering 75%" 实际是 0.44%→0.11% 的小基数降幅（CausalVAD）；"remarkable 25.1% leap" 没说明是相对还是绝对增幅（ReMoT）。
- 不只是 SOTA 类强词：superior / significant / strong / effective 这类结论词同样要有数字、数据集、指标、实验设置或引用支撑。没有支撑时，改成具体描述或者删掉。
- 检查动作：全文搜索第 2.2 节列出的强词，每处出现都要在同一句或下一句找到数字；找不到就降级或补数字。

### 原则 3：一个概念只用一个词，一个量只用一个符号
- 术语漂移是 9/9 批次都点名的最高频细节问题。
- 一个概念只用一个主术语，在摘要、引言、方法、图表和实验中保持一致；符号同理，同一个量全文只用一个符号。不要为了避免重复而换说法，审稿人会以为那是另一个东西。
- 确定下来的术语写进论文仓库 `.paperdna/spec.md` 的术语表。
- 正例：批次 050 的论文整体上定名后缩写和词序始终不变，笔记把这种稳定本身评为一种品味。
- 反例：CFG-Ctrl 中 e(t) 有五种说法；EthoCLIP 的图模块有四种命名；DOSFMVC / DOSMFVC / DOSFMNVC 三种拼写混用；WIR3D 的核心方法先后被叫作 "visually meaningful curves / semantically-informed curves / 3D strokes / visually-informed curves"；IDGH 用 flawed / terrible / inaccurate / detective 四个词形容同一缺陷。
- 检查动作：建一张术语表（见 2.3 节），逐项全文搜索同义变体。

### 原则 4：不主动示弱，但主张不越过证据
- 本 skill 的口径见 `references/anti_defensive.md`：不说输，不主动罗列不足；遇到不利结果，按其第 3 节的顺序处理（删 → 收缩主张 → 换口径 → 解释为取舍 → 重组 → 重构故事 → 最后才直接说明）。
- 正例（收缩措辞，而不是示弱）：Janus-Faced Affinity Learning 在非最优子指标上用 "competitive"；E-RayZer、Cov2Pose 用 "comparable" 而不硬说 outperform。
- 反例（主张越过证据）：NRMF 写 "surpasses all prominent ... methods"，但 Table 4 中 VPoser 的 FID_p 更好；LRHDR 写 "outperforms previous methods"，Table 1 中 NECHDR 反超；Vanast 写 "across all metrics"，正文却承认 SSIM 只是 "comparable"。
- 检查动作：逐张表找出本方法不是第一的格子，确认正文没有在这些格子上声称领先；不需要逐格写一句"我们不如 X"。

### 原则 5：摘要、引言、正文的结论强度保持一致
- 反例：Gated KalmaNet、GenErase 的摘要都省略了正文里的 "on average"；HTNav 摘要写 "state-of-the-art across all scene levels"，实际 Val-Unseen SR 只有 17.69%。
- 正例：Gated KalmaNet 把提升严格限定在 "RAG and LongQA tasks"；3D Gaussian Hierarchies 默认用 comparable，只在局部指标上升级为 significantly。
- 检查动作：把摘要中每个结果 claim 和正文对应的表逐一对照；正文里有的限定语（on average / on most metrics / in the X setting），摘要里也必须保留。

### 原则 6：问题、贡献、实验一一对应
- 贡献列表 74.4% 用 bullet。多批次把"贡献列表即目录"列为复现率最高的借鉴写法：每条贡献都能在实验/消融章节找到对应的小节。
- 先确定每条贡献属于哪一类，它决定了实验需要证明什么（各类型的组合比例见第 0 节）：
  - **Insight**：新的发现或理解，需要分析性实验支撑。
  - **Performance**：在已有任务上做得更好，需要公平对比和消融实验。
  - **Capability**：做到以前做不到的事，需要展示新能力，并说明它的边界。
- 正例：AVGGT 用 Q1/Q2 给问题编号，再在消融里逐一回收验证；Gated KalmaNet、HyperGait、NG-GS 的挑战编号和贡献编号一一对应。
- 反例：贡献里写了 "generalizes to unseen domains"，实验里没有跨域实验；LegoOcc 的品牌隐喻和 Method 正文脱节。
- 检查动作：画一张"贡献 i → 实验小节/表格编号"的映射表，不允许有空行。

### 原则 7：先观察，后方案；先直觉，后公式
- 发现类动词（observe / find / reveal）和 propose 分工，形成"先发现后方案"的顺序（AVGGT、EgoXtreme）。
- 先给失败案例或 oracle 实验，再引出方法（RawMetaDiff；TF-CADE 的 Fig.1）。
- 公式遵循三步：先写一句直觉，再给编号公式，最后逐项解释符号，这几乎是所有批次的共识。
- 反例：一上来就是 Eq.(1)，没有一句话说明它要解决什么；或者先摆方法，读者不知道它针对的是什么现象。
- 检查动作：每个带编号的公式前一句是否在说"为什么需要它"？

### 原则 8：给现象起名字，并在全文复用
- 正例：IR-HGP 的 "baked-in shadow"；MeshRipple 的 "ripple / frontier / root" 自成一套词汇；Mechanisms of Object Localization 的 "containerization"；MoRel 的 "backward contamination"；SSMP 的 "semantic collapse"；借心理学实验命名的 "The Invisible Gorilla Effect"。通常第一次出现时加引号，之后作为专名直接使用。
- 反例：同一个现象在引言叫 "drift"，在方法里叫 "degradation"，在实验里又叫 "collapse"。
- 检查动作：论文的核心现象有没有一个 1–3 词的名字？它在摘要、引言、方法、实验中是否都出现了，且写法完全一样？

### 原则 9：用精确的词，不用大词
- 正例：用 mitigate / alleviate 表示"缓解而非消除"（Focus-to-Perceive、SaE、VMonarch 刻意不用 solve）；restores 表示"恢复"而不是"创建"能力（V²-SAM）；non-decreasing 精确表达"允许持平"（RiskProp）；"no weaker than" 严格对应定理条件（Taming Noise-Induced Prototype Degradation）。
- 反例："a significant advancement" 没有指标（Native and Compact Structured Latents）；"unifies all 4D tasks" 用了全称量词（D4RT）；"large-scale" 形容的只是 1.7K 病例的数据集（Gastric-X）；"training-free" 的 pipeline 里其实含有微调模型（Refracting Reality）。
- 检查动作：对照第 2.4 节的精准/不精准对照表替换。

### 原则 10：局限最多两条，写成"边界 + 方向"
- 语料中多数论文没有独立的 Limitations 小节。本 skill 的做法：局限最多 2 条，每条一两句，写成"适用边界 + 后续方向"，放在结论之前或结论中间，不作为全文最后一句（`references/anti_defensive.md` 第 5 节）。
- 正例：`We do not claim ...`（Visual Diffusion Models are Geometric Solvers）；`We focus on static scenes; handling dynamic objects is left for future work.`
- 反例：罗列一长串不足；"our method still has significant shortcomings" 这类情绪化自评；只写一句空泛的 "future work will explore more scenarios"。
- 检查动作：局限不超过 2 条；每条能看出边界是什么、下一步做什么。

### 原则 11：一条主线，方法是连续的求解链
- 全文按"问题 → 原因 → 方法 → 结果"推进。
- 方法要写成围绕同一个核心问题的连续求解链：每个设计都回应前一步留下的问题，而不是互不相关的 A + B + C 模块堆叠。
- 反例：方法一节依次介绍模块 A、B、C，彼此之间没有"因为 A 带来了什么问题，所以需要 B"的交代。
- 检查动作：对方法中的每个组件，能否用一句"因为 [前一步留下的问题]，所以需要它"说明它存在的理由？说不出就重写衔接，或考虑把它移出主线。

### 原则 12：与实现一致
- 关键机制、损失函数、变量、超参数和实验条件都要与代码和实验设置一致。
- 先读代码和实验记录再写；发现论文与代码不一致时，问用户以哪边为准，不要自行选一边。
- 检查动作：逐个核对正文中的公式、超参数取值和实验设置，每一项都能在代码、配置或实验记录中找到对应。

### 原则 13：减少读者的困惑时间
- 困惑时间（confusion time）指读者为弄懂内容而花掉的时间总和。
- 概念在第一次出现的地方就解释，不要让读者往后翻。
- 图表的 caption 要能单独看懂，关键说明放在图表附近。
- 检查动作：对每个新术语、新符号，确认第一次出现处就有定义或一句解释；只读图表和 caption，能否看懂它要说明什么。

### 原则 14：每句话都要有信息量
- 删掉与论证无关的历史回顾和重复陈述，每句话都应该让读者多知道一点东西。
- 检查动作：逐句问"删掉这句，读者会少知道什么？"答不出来就删。

### 原则 15：需要论述的地方写成段落
- 一段只讲一个核心点，由首句（主题句）定调；段落长度见第 5 节。
- 需要论述的地方写成段落，不要写成 bullet 列表。
- 例外：贡献列表默认用 bullet（74.4% 的顶会论文如此，见第 0 节和原则 6）。
- 检查动作：正文中除贡献列表以外的每个 bullet 列表，都检查它是否在承担论述；是的话改写成有逻辑衔接的段落。

---

## 2. 用词

### 2.1 高频动词用法表

| 动词 | 用在哪 | 模板 / 例句 | 注意 |
|---|---|---|---|
| propose | 宣告整体方法，全文 1–3 次 | 模板：`We propose X, a Y that Z.`（ChordEdit 同构） | 只给整体方法用。Real-Time Streamable Talking Portrait 全文只用 1 次 propose |
| introduce | 子模块、新命名的概念、数据集、token 类型 | 模板：`We further introduce X, which ...` | 分工示例："propose 用于整体框架，introduce 用于具体 token 类型，design 用于机制掩码"（Sparse-LaViDa）；FRP 用 propose，其子模块 HGL 用 introduce（Hyperbolic Relational Prompts） |
| present | 比 propose 更克制地介绍工作 | 模板：`We present X, ...` | VeriDou 全篇偏好 introduce/present |
| design | 具体机制、损失、掩码 | 模板：`We design a X mask that ...` | 同 Sparse-LaViDa |
| construct / build / curate | 数据集、基准 | 模板：`We construct X, a benchmark of N ...` | 数据集贡献和方法贡献用不同动词（The More, the Merrier 的 Bird-MML；TRIDENT 的 MorphoGene） |
| address / tackle | 问题→方案的过渡 | `To address these challenges, we propose ...` | 9/9 批次复现率最高的过渡句；全文最多用 1–2 次，避免每节开头都用 |
| mitigate / alleviate | 缓解但没有根除 | 模板：`X mitigates Y by ...` | 比 solve / eliminate 诚实（Focus-to-Perceive、SaE、VMonarch） |
| enable / enabling | 手段→新能力 | `..., enabling O(1) per-frame complexity`（AMB3R） | 用分词状语；单篇 6–7 次就会显得模板化（NERFIFY） |
| demonstrate | 实验结论 | 模板：`Extensive experiments on A, B, and C demonstrate that X ...` | 主语常为 experiments，把结论客观化；强度低于 prove |
| achieve / outperform / surpass | 结果陈述 | `up to +2.7/+6.9 mAP`（DetGain）；模板：`X outperforms Y by N% on Z.` | 必须跟数字和对比对象；attain/achieve 只在实验部分用（Hermite RBF） |
| match / be comparable to / be competitive with | 打平或接近 | `matches or surpasses`（PGO 论文）；`comparable`、`trailing by X`（E-RayZer、Cov2Pose） | 非最优时用它，不要硬说 outperform |
| observe / find / reveal / re-examine | 引出发现 | 模板：`We observe that X, which suggests Y.` | 和 propose 形成"先发现后方案"（AVGGT、EgoXtreme、Neighbor GRPO） |
| suggest / indicate / hypothesize / posit | 机制归因、未验证的推测 | `we hypothesize`（GaussianVision）；posit（FRP） | 证据强度低于 demonstrate；不要用来软化实测结果，也不要用 suggest 引出强结论（NI-Tex 用 suggest 引出强结论，实际提升仅 4.8%） |
| leverage | 借用已有模型/先验 | 模板：`We leverage the X prior of Y to ...` | 必须带具体宾语；全文不超过 2 次，其余换成 use / exploit / build on / draw on（见第 3 节） |
| 个性化核心动词 recast / reformulate / decouple / distill / sidestep / revisit / bridge / resolve | 表达本文的独特动作 | `sidestep this issue`（MeshFlow）；recast（ChordEdit、Improved Mean Flows）；decouple（OVI-MAP）；distill（InstantViR）；bridge（CoordSpeaker）；resolve（Curvature-Aware Captioning）；revisit（Multigrain-aware） | 选一个和方法机制对应的动词贯穿全文，比泛用的 propose 更有记忆点 |

### 2.2 结论强度与限定语规则

**强度三级表**（按证据选词，不按想要的效果选词）：

| 证据情况 | 允许的词 | 必须同时出现 |
|---|---|---|
| 所有主表、所有主指标都第一 | state-of-the-art, consistently outperforms, significantly（仅限做了显著性检验时） | 具体数字 + 数据集/设置范围 |
| 多数指标第一，个别不是 | outperforms on most metrics, achieves the best overall ... | "most" 而非 "all"（Test-Time Multi-Prompt Adaptation 用 "most metrics"） |
| 打平或接近 | comparable, competitive, matches, on par with, trailing by N | 对比对象；如果有效率优势就写出来 |
| 机制解释、原因推测 | may, likely due to, suggests, we hypothesize | 不需要数字，但不能写成事实 |
| 首创声明 | to our knowledge, the first ... | 必须加 "to our knowledge"，并在相关工作里写清检索范围 |

**硬规则**：
1. 全称量词（all / every / any / across all metrics / fundamentally）只有在逐格核对了所有表格后才能用。反例：SpatialTree 写 "across all levels"，但 Table 3 有局部下降；PixelRush 写 "fundamentally break the conventional trade-off"，验证只覆盖两个模型。
2. 百分比必须说明是相对还是绝对；小基数的相对降幅要同时给绝对值（反例：CausalVAD、ReMoT）。
3. 摘要里的 claim 要保留正文中的所有限定语（on average / on X benchmark / under Y setting）。
4. 平均值不能用来夸大：有子集或子指标变差时，不写 all / consistently，把主张收缩到实际领先的范围（反例：AdaptVision、CARE、CD-Buffer、Fresco）。
5. 限定语用于机制归因和局限段，不用来软化实测结果；实测结果用数字说话。
6. 禁止在没有证据时使用 paradigm shift / a new paradigm / unprecedented / zero interference / does not suffer from any of the previous limitations（反例：GrOCE、ChordEdit、DiverseGRPO、RINO）。

### 2.3 术语一致性与缩写规则

**规则**：
1. 缩写首次出现时写"全称 (缩写)"，之后只用缩写。摘要和正文各展开一次。
2. 摘要、引言、方法小节标题、图注、结论中的全称必须逐字一致（反例：CIGPose 有三个全称版本；LRHDR 方法全称和第 3 节标题不一致；GeoRelight 的 iNOD、MeteorPred 的 DTGF 都有两种全称展开；CoST 的 Collaborative / Cooperative；M2S 的 Multi-Scale / Multi-Spatial）。
3. 缩写要先在正文定义，再在表格中使用（反例：SinGeo Table 7、SuP Table 5 先在表格用、后在正文定义）。
4. 定义过的缩写不能改回口语说法（反例：2D-LFM 定义 CPE 后又改称 "per-layer PE"）；定义后从未使用的缩写要删掉（反例：MOFA-VTON 的 "LA"）。
5. 大小写、连字符、空格要统一：Top-p / Top-P、spatio-temporal / spatiotemporal、2D–3D / 2D-3D、point map / pointmap（Ov3R）、3D-EM / 3D EM、SpatialTree-bench / -Bench、DR / DR.（Keep It Frozen）、higher-order / high-order（HyperGait）、OminiControl 多余的空格。
6. 方法名本身的拼写要核对：RhythmGuassian（Gaussian 拼错）、MoGA 全称中的 "Moncular"、GMMamba 被误写成 CMMamba、CCNet 被误写成 CCFNet、ROSE 正文写 VRMG 而图 3 写 VGRM、SCORE 的 GCA 被误写成 VCA / VPA。
7. 形容同一缺陷、同一现象只用一个词（反例：IDGH 的四种措辞、Thermal Diffusion Matters 的五种说法、UniLight 的四种表述）。

**操作步骤**：
1. 动笔前建一张术语表：`概念 | 唯一英文名 | 缩写 | 首次定义位置`。
2. 每写完一节，对照术语表检查新出现的名词短语，发现近义变体就替换。
3. 定稿前对每个缩写全文搜索：首现位置是否在表格/图之前；全称是否逐字一致；大小写和连字符是否统一。

### 2.4 精准用词 vs 不精准用词对照表

| 不精准（反例出处） | 问题 | 精准写法（正例出处） |
|---|---|---|
| inaccurate / flawed（笼统） | 没说错在哪 | coarse（精确指粒度）；underestimate（A Debiased Reconstruction-based Framework）；under-constrained（Fresco） |
| large deformation | 没有抓住几何本质 | non-isometric（NI-Tex） |
| correlated | 比定理弱 | monotonically related（Modality Gap；该文引言却又用 correlated，造成前后精度不一致） |
| black-box | 泛化 | opaque（How to Take a Memorable Picture） |
| increasing | 排除了持平 | non-decreasing（RiskProp） |
| create / enable 某能力 | 夸大了贡献 | restores（V²-SAM） |
| solve / eliminate | 夸大了效果 | mitigate / alleviate（Focus-to-Perceive） |
| avoid / overcome this issue | 泛化 | sidestep this issue（MeshFlow） |
| 笼统的 "affects" | 没说后果 | invalidate（FluoCLIP） |
| memory-efficient / long memory（笼统） | 缺少形象 | eidetic（Gated KalmaNet 形容 KV-cache） |
| stable / no drift（笼统） | 缺少可验证性 | drift-free（PiLoT）；field-free（Native and Compact Structured Latents） |
| after training（笼统） | 时机不清 | post hoc（DetGain） |
| average（笼统） | 没说权重 | time-weighted average（ChordEdit） |
| a significant advancement | 没有指标 | 直接写提升的数字 |
| unifies all X tasks | 全称量词 | unifies A, B, and C |
| large-scale（1.7K 病例，Gastric-X） | 规模夸大 | 直接写规模：`1.7K cases from N centers`（模板） |
| training-free（pipeline 实含微调模型，Refracting Reality） | 定义不符 | 写清哪个组件无需训练 |
| perfectly recovers（Seeing through Light and Darkness，指标并非满分） | 与数据矛盾 | 写数字 |
| understands X（拟人化，没有可解释性实验） | 断言过度 | 描述可测量的行为：`correctly localizes X in N% of cases`（模板） |
| powerful representation capability（重复 4 次） | 空洞 | 写出具体性质或实验现象 |
| frozen 与 full fine-tuning 混用 | 对照不清 | frozen 精确对应 full fine-tuning 对照组（TriLite） |
| operationalize（正例） | — | 把抽象洞察落为可执行的约束（Stabilizing Feature Geometry） |
| disentangles（正例） | — | disentangles camera/object motion（SceneScribe-1M） |

---

## 3. 需要警惕的词

**总体判断**：这批顶会论文的 AI 味整体较轻。delve / paramount / tapestry / boasts / testament / unlock / game-changer 在绝大多数批次中逐一检索都没有检出或密度极低（delve 全库只零星出现 3 处）；"delve + crucial + seamless + paramount 扎堆"在任何一批都没有出现。真正的风险集中在两处：**leverage 的重复使用**和**seamless(ly) 缺乏证据**。这类词主要集中在摘要开篇句和结论收尾句这两个"防守最松"的位置。

| 词 | 在论文中的问题（出处） | 替换建议 |
|---|---|---|
| leverage | 最高频，半数以上论文出现；重复过多被点名：WorldMM 约 15 次，UIKA、Learning from Oblivion、Mocap-2-to-3 各 9 次以上，Mitigating Objectness Bias 5 次以上，PRISM 约 5 次，AdaSpark 4 次 | 全文不超过 2 次，且必须带具体宾语；其余换成 use / exploit / build on / draw on / harness，或直接写动作：`We initialize X with Y` |
| seamless(ly) | 第二高频，9/9 批次都出现，几乎总是缺乏量化支撑：ApET 5 次；D-Convexity 的推理开销实际增加约 12 倍却没在摘要提；3D Gaussian Hierarchies 实际修改了 CUDA kernel；AdvFractal 与自身消融矛盾；SEELE、TUNA、Urban-GS、ZoomEarth、GeoMMBench、HieraMamba、NaTex、PhysSkin 等至少 8 篇被点名 | 默认删除。确实是即插即用时，写出证据：`without modifying X`、`with N additional parameters`、`adds N ms latency`（模板） |
| crucial / crucially | 多数是单次使用且带具体宾语，可以接受；Omni2Sound 4 次，TRIDENT、SegEarth-R2 5–6 次；Prime Once 连续两句以 Crucially 开头 | 全文不超过 2 次；换成 key / necessary，或直接写后果：`without X, accuracy drops by N` |
| comprehensive | BioVITA 5 次，Baby's Eyes 4 次，没有新增信息 | 写出覆盖范围：`on N datasets spanning A, B, and C` |
| novel | MHC-DUN 约 7 次 | 删掉；新意靠"和谁不同"来体现：`Unlike X, which ..., our Y ...` |
| robust | 模板化重复 | 写出对什么扰动鲁棒以及扰动幅度 |
| holistic / versatile / high-fidelity / generalizable | 没有量化锚点，多篇重复出现 | 分别写出覆盖的维度、支持的任务列表、具体的保真指标、在哪些未见设置上测过 |
| simple yet effective | 套路化自评 | 用组件数、参数量、代码行数说明"简单"，用数字说明"有效" |
| state-of-the-art（没有数字） | 见 2.2 节 | 后面紧跟数字和基准名 |
| the first | 缺少穷尽检索：ENC-Bench 出现 3 次；FluoCLIP 仅对比了 2 个数据集；Keep It Frozen、LLMind、LOREAL、NAF、ReMoT、VRR-QA、SaE、Mechanisms of Object Localization 都被指出 | `To our knowledge, X is the first to ...`，并在相关工作中说明检索范围 |
| a new paradigm / paradigm shift | ChordEdit、DiverseGRPO、GrOCE | 写清改变了哪个具体假设：`X removes the need for Y` |
| unprecedented / holy grail / fundamentally break | RINO、NitroGen、PixelRush | 删除，改为数字对比 |
| catastrophic / staggering / remarkable leap | AD-GBC（+0.29 个百分点）、CausalVAD、ReMoT | 形容词强度必须和数量级匹配；小于 1 个百分点的变化不用情绪化形容词 |
| significantly（没做显著性检验） | 多篇 | 做了检验才用；否则写 `by N points` |
| innovatively / exceptional | GeoCoT 用 innovatively 2 次；多篇用 exceptional | 删除 |
| zero interference / does not suffer from any limitations | GrOCE、RINO | 改为可测量的表述，并把主张限定在实际验证过的范围 |
| delve / paramount / tapestry / boasts / testament / unlock / game-changer | 顶会论文中几乎不出现 | 一律不用；出现即视为 AI 生成痕迹 |

**扫描方法**：定稿前对上表每个词做全文计数。计数超过上限，或出现位置在摘要首句、结论末句，就逐一替换。计数用 `scripts/ai_style_scan.py` 完成（词表与上限以 `references/ai_words.json` 为准，见第 4.1 节），完整的自查步骤见第 4.9 节。

---

## 4. 去 AI 味：不要怎么写

适用于所有生成或改写的正文。本节讲"不要怎么写"；"应该怎么写"见第 1 节（原则）、第 2 节（用词与结论强度）和第 5 节（风格参数），第 3 节是顶会论文中高风险词的真实使用情况。

### 4.1 词表：`references/ai_words.json` 是唯一来源

词表只在 `references/ai_words.json` 里维护，`scripts/ai_style_scan.py` 也读这份词表；本文件只讲规则和判断方法，不重复列词。想新增或调整某个词，改 `ai_words.json`。

- `level: avoid`：默认不用。按 `suggest` 替换。如果是套话（如 "It is worth noting that"），整段删掉，让句子直接从实际内容开始。
- `level: review`：这些词在某些领域是正常术语，比如 robust（鲁棒性实验）、orthogonal（线性代数）、landscape（loss landscape）、显著（统计检验）。只有非术语用法才替换。
- 带 `max` 的是限量词：顶会论文里也常用，但不能反复出现，例如 leverage（24% 的顶会摘要用过）、crucial。novel、comprehensive 不是限量词，每次出现都会提示，默认删除（见第 7 节第 7 条）。同一文件不超过上限、并且每次都带具体宾语就可以保留；扫描脚本只在超过 `max` 次时才提示。
- 出现在引文、专有名称和数据集名称里的命中不改。

### 4.2 机械过渡

- ❌ 段首或句首用 Furthermore / Moreover / Additionally / In conclusion 衔接。
- ✅ 用上一段（句）的关键词或论点开头，让逻辑关系自己显出来。
- 例：上一段讲完"推理延迟高"，下一段写 "This latency comes mainly from ..."，而不是 "Moreover, ..."。
- 这条针对的是没有逻辑内容、只起"再加一条"作用的过渡词。表达真实转折、因果或对比的连接（However / Thus / In contrast / To this end）不在此列，但也不要每段都用；引言各位置的衔接写法见 `references/sections/introduction.md` 第 3 节。

### 4.3 夸张修饰

- ❌ paramount / revolutionary / vital 等带情绪的形容词和副词；crucial 这类限量词超过上限或没有具体宾语时同样算。
- ✅ 改成可以验证的描述：数字、约束、方法细节。
- 例：❌ "a crucial component" → ✅ "removing this component increases error by 4.2 points"。
- 形容词强度要和数量级匹配，见第 3 节 catastrophic / staggering 一行。

### 4.4 结论强度与证据匹配

- ❌ "This proves that ..."（定理证明以外的场合）。
- ✅ "These results suggest ..." / "The data indicates ..."。
- 有直接数据支撑时直接陈述结果，不要层层叠加 may / might。只有推断和推广时才用限定语。数学证明里的 "we prove" 不受这条限制。
- 按证据选词的强度三级表见第 2.2 节。

### 4.5 僵尸名词（名词化）

- ❌ "perform an evaluation of" / "conduct an analysis of" / "make a comparison between"。
- ✅ 改用动词：evaluate / analyze / compare。
- 中文同理：❌ "对…进行了分析" → ✅ "分析了…"。

### 4.6 领域外隐喻和行话

- ❌ ecosystem（生物）、orthogonal（非数学语境）；leverage（商业）属于限量词，全文不超过 2 次且带具体宾语（见第 3 节）。
- ✅ use / apply、system / environment、independent。
- 除非这个词在本领域有明确定义，否则用平实的说法（plain English）。

### 4.7 句式节奏

- ❌ 每句都是中等长度、结构对称的平衡句。
- ✅ 关键结论用短句强调，复杂论述用长句展开。句长的默认值见第 5 节。

### 4.8 具体性

- ❌ 泛泛而谈、换到任何一篇论文里都成立的句子。
- ✅ 补上具体的数字、方法名、研究者、约束条件或变量范围。
- 如果补不出来，这句话可能没有信息量，考虑删掉（原则 14）。

### 4.9 自查步骤

1. 运行 `python3 scripts/ai_style_scan.py <文件或目录>`：avoid 命中全部处理，review 命中逐条判断，限量词超过 `max` 时逐个删减。
2. 通读一遍，人工检查脚本查不出来的第 4.2–4.8 节：脚本只能匹配词和固定搭配，查不出机械过渡是否真的缺少逻辑、夸张程度是否与数字匹配、句式是否单调、句子是否空泛。

---

## 5. 风格参数（可执行默认值）

| 参数 | 默认规范 | 依据 / 例句 |
|---|---|---|
| 摘要长度 | 8 句（允许 7–9） | 中位数 8，四分位 [7, 9] |
| 摘要结构 | 第 1 句背景（最好带出问题）→ 第 2–3 句问题/缺口 → 第 3–4 句方法 → 第 4–6 句设计细节 → 第 6–7 句结果 → 第 8 句资源发布或"结果+意义" | 五等分位置的主作用分布；最后一句资源发布 43.1% |
| 摘要里的数字 | 最多给 1–2 个最关键的数字或倍数；其余写成定性结论 + 基准名 | 多批次："摘要/引言定性、正文表格定量"的分工几乎逐字重复 |
| 引言段数 | 5–6 段 | 中位数 6，5 段 29.1%，6 段 27.1% |
| 贡献列表 | bullet，3 条左右，每条对应一个实验小节 | bullet 74.4% |
| Figure 1 | 必须有，并在引言第 1–2 段引用 | 91.3% |
| 句长 | 平均 25–35 词；论证用长句（25–50 词，含从句/分词状语/同位语），转折或收束用短句（6–15 词）；每段至少一个短句 | `In practice, this is not the case.`（AMB3R）；`Two obstacles make this challenging.`（Counterfactual VLA） |
| 人称与语态 | 本文的贡献动作用 we + 主动语态；背景、他人工作和客观机制用被动或第三人称；方法名可以作主语（`SAME consistently achieves ...`）；几乎不用 "this paper" 作主语 | 9 批一致 |
| 段落 | 段首句就是主题句；一段只讲一件事；超过约 8 句就拆段；论述写成段落而不是 bullet，贡献列表除外（原则 15） | 段首主题句是最一致的习惯；过长不分段被多篇点名 |
| 数字与对比 | 对比句式：`from X to Y (+Z)`、`up to N×`、`outperforms Y by N%`；进阶：`72.40→76.21`（GeoAgent）、`92.40±0.11 (+0.43)`；相对/绝对明确标注 | 多批次 |
| 图表引用 | `As shown in Fig. X, ...` 或把 `(Fig. X)` 嵌在句尾；每张图表在正文中至少被引用一次，并说明要看什么 | 多批次 |
| 公式 | 直觉句 → 编号公式 → 逐项解释符号 | 几乎全部批次的共识 |
| 语气 | 自信但克制：强结论配数字，机制和边界判断配 hedge 词；不主动示弱，主张不越过证据（`references/anti_defensive.md`） | 9 批一致 |
| Limitations | 最多 2 条，每条写"适用边界 + 后续方向"，放在结论之前或结论中间 | 本 skill 口径（`references/anti_defensive.md` 第 5 节） |
| 校对重点 | 摘要、贡献列表、图注（语法拼写错误集中在这些地方：主谓不一致 "misalignment ... degrade"、"our approach generate"，冠词缺失，"the the"，LaTeX 残留） | Mirror Illusion Art、MedLIME、PixelRush、TMFS |

---

## 6. 最值得借鉴的写法（按场景）与最常见的问题

### 6.1 按场景的借鉴写法

| 场景 | 写法 | 模板 / 出处 |
|---|---|---|
| 摘要第 1 句 | 背景和问题写在同一句 | 背景+问题 21.2%，是背景之外最常见的首句作用 |
| 摘要方法句 | 名字 + 类别 + 机制，一句写完 | `We propose X, a Y that Z.`（ChordEdit） |
| 摘要结尾 | 资源发布；或结果 + 意义 | `Code and data will be released at ...`（模板）；资源发布 43.1% |
| 引言立论 | 反直觉证据前置，再用短句反转 | AMB3R：`In practice, this is not the case.` |
| 引言提出挑战 | 用短句立靶子，再对挑战编号 | `Two obstacles make this challenging.`（Counterfactual VLA）；AVGGT 的 Q1/Q2 |
| 引言动机 | 先给失败案例或 oracle 实验（放在 Fig.1） | RawMetaDiff；TF-CADE |
| 引言过渡 | 问题到方案只用一次过渡句 | `To address these challenges, we propose ...` |
| 贡献列表 | bullet，每条可对应到实验小节 | 74.4% 用 bullet；"贡献列表即目录" |
| 方法 | 先直觉后公式；给现象和组件起专名并全篇复用 | MeshRipple 的 ripple/frontier；IR-HGP 的 baked-in shadow |
| 方法（动词） | 选一个和机制对应的招牌动词贯穿全文 | recast（ChordEdit）、bridge（CoordSpeaker）、decouple（OVI-MAP） |
| 实验：结果 | 强词 + 数字 + 范围；用箭头或括号标增量 | `up to +2.7/+6.9 mAP`（DetGain）；`72.40→76.21`（GeoAgent） |
| 实验：效率 | 给可验证的具体数字，不用形容词 | Native and Compact Structured Latents；LagerNVS "30FPS+"；GenTract 用具体倍数替代 significantly |
| 实验：不利结果 | 按 `references/anti_defensive.md` 第 3 节处理；必须提及时用中性比较措辞 | `comparable` / `competitive with`（E-RayZer、Janus-Faced Affinity Learning）；把优势限定到具体条件 |
| 讨论：归因 | 强证据用 demonstrate，弱证据用 suggest / hypothesize | GaussianVision、PGO 论文 |
| 局限 | 边界 + 方向，一两句 | `We do not claim ...`（Visual Diffusion Models are Geometric Solvers）；`We focus on X; Y is left for future work.` |
| 标题与正文呼应 | 标题中的比喻在引言里再用一次 | Seeing the Trees for the Forest 的引言写 `The trees are lost in the forest.` 呼应标题；Diving into ... ↔ `We dive into ...` |

### 6.2 最常见问题（按出现频次排序）与检查方法

| # | 问题 | 频次 | 检查方法 |
|---|---|---|---|
| 1 | 修辞强度超出数据量级（全称量词、情绪化形容词、未加限定的 "the first"、相对/绝对混淆） | 9/9 批次 | 全文搜索第 3 节的词和 all / every / first / significantly，逐条找数字支撑；形容词强度和数量级不匹配就降级 |
| 2 | 防御性写作：自我削弱词、层层叠加的限定语、罗列不足、结论末尾自我否定 | 本 skill 口径 | 扫描脚本"自我削弱"类别清零；按 `references/anti_defensive.md` 第 7 节逐句自查 |
| 3 | 术语和缩写全文漂移 | 9/9 批次，最高频的细节问题 | 按 2.3 节术语表逐项全文搜索；核对摘要、方法标题、图注、结论中的全称 |
| 4 | 摘要比正文说得更强（丢掉 on average 等限定语，省略不利指标） | 多批次（LF-BVN、LRHDR、SignDINO、Gated KalmaNet、GenErase、HTNav） | 把摘要每个 claim 与对应表格对照，限定语逐一回填 |
| 5 | 平均值夸大：用 all / consistently 覆盖了局部下降 | 多批次 | 每张表逐格标出非第一的格子，确认正文没有在这些格子上声称领先 |
| 6 | 套话集中在摘要首句和结论末句 | 两个批次专门指出 | 单独重读这两句，删除 seamless / comprehensive / novel / crucial |
| 7 | 语法拼写错误集中在摘要、贡献列表、图注 | 多批次 | 对这三处单独做一遍主谓一致、冠词、重复词、LaTeX 残留检查 |
| 8 | 贡献与实验没有一一对应 | 多批次（作为借鉴项的反面） | 画"贡献 → 实验小节"映射表，不允许空行 |

---

> 取名（方法名、子模块名、数据集名、标题模板、命名的一致性检查）见 references/naming.md。

---

## 7. 定稿前总检查清单（按顺序执行）

1. [ ] 摘要 7–9 句；第 1 句写背景（最好带出问题）；方法最迟在第 3–4 句出现；最后一句写资源发布或"结果 + 意义"。
2. [ ] 引言 5–6 段；Figure 1 已在引言中引用；bullet 贡献列表中的每一条都能映射到实验小节，且实验证明的内容与贡献类型（Insight / Performance / Capability）相符（原则 6）。
3. [ ] 全文按"问题 → 原因 → 方法 → 结果"推进；方法各组件构成连续的求解链，而不是模块堆叠（原则 11）。
4. [ ] 公式、超参数、实验设置与代码和实验记录一致；不一致处已问过用户（原则 12）。
5. [ ] 每个强词（state-of-the-art / significantly / consistently / outperforms / all / the first）都有数字、范围或 "to our knowledge"。
6. [ ] 摘要中的限定语与正文一致；没有在不领先的指标上声称领先。
7. [ ] 第 3 节的词表计数：leverage ≤ 2，crucial ≤ 2，seamless(ly) = 0（除非附有量化证据），novel / comprehensive / paradigm / unprecedented = 0。
8. [ ] 按第 4.9 节完成去 AI 味自查：`scripts/ai_style_scan.py` 的 avoid 命中已全部处理、review 命中已逐条判断；人工检查过第 4.2–4.8 节。
9. [ ] 术语表逐项全文搜索，没有同义变体，大小写和连字符统一；符号和缩写前后一致。
10. [ ] 每个编号公式前面有一句直觉说明，后面有逐项的符号解释；每个新概念在第一次出现处就有解释（原则 13）。
11. [ ] 核心现象有专名，并在摘要、引言、方法、实验中复用。
12. [ ] 局限最多 2 条，写成"边界 + 方向"；全文没有自我削弱词，结论最后一句落在意义上（`references/anti_defensive.md` 第 7 节）。
13. [ ] 方法名、子模块名、数据集名通过 references/naming.md 的检查清单（§2.3、§4.4、§7）。
14. [ ] 摘要、贡献列表、图注单独校对一遍语法和拼写。
15. [ ] 所有 `\ref` 和 `\cite` 都能正确解析；图表按顺序在正文中被引用，caption 能单独看懂。
16. [ ] 满足匿名要求：作者信息、致谢、自引的措辞、代码链接。
17. [ ] 符合页数限制和模板格式。
