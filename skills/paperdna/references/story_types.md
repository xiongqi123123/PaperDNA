# 顶会论文叙事类型与行文逻辑

> **怎么用这份文档**（给正在写论文的 AI 助手）
> 1. 先用第 2 节的判断流程，为当前工作确定一个**主类型**，需要时再加一个**辅类型**。
> 2. 按第 3 节的共享原则搭好摘要、引言、方法、实验、结论的骨架。
> 3. 给方法、数据集、标题起名时，按 references/naming.md 执行（按叙事类型的取名差异见其中 §6）。
> 4. 翻到主类型章节，照着"叙事骨架 → 逐步写法 → 全文递进"去写，写完后逐条核对该章节和第 3.8 节的检查清单。
>
> 书名号《》里是真实论文标题或方法名，全部来自精读笔记。英文句式可以直接套用，但要替换成自己的内容。

---

## 0. 数据来源

- 样本：CVPR 2026 + ICCV 2025 的 1040 篇精读笔记。其中 Oral 195 篇、Highlight 836 篇、Best Paper 9 篇。
- 方向：CV 950 篇、自动驾驶 48 篇、具身智能 41 篇。自动驾驶和具身的样本较少，差异只能作参考。
- 各类型章节的例证来自对应类型的汇总批次。能力扩展型的规律基于约 20 篇精读，效率优化型基于 21 篇，理论分析型只有 2 篇，推广时要谨慎。

---

## 1. 总览

### 1.1 类型分布

| 叙事类型 | 全部 (n=1040) | 自动驾驶 (n=48) | 具身 (n=41) | CV (n=950) | Oral (n=195) | Best (n=9) |
|---|---|---|---|---|---|---|
| 瓶颈突破型 | 582 / 56.0% | 25 / 52.1% | 23 / 56.1% | 534 / 56.2% | 113 / 57.9% | 5 |
| 新问题定义型 | 114 / 11.0% | 9 / **18.8%** | 5 / 12.2% | 100 / 10.5% | 23 / 11.8% | 1 |
| 统一框架型 | 112 / 10.8% | 3 / 6.2% | 7 / **17.1%** | 102 / 10.7% | 17 / 8.7% | 1 |
| 发现-解释型 | 111 / 10.7% | 3 / 6.2% | 2 / 4.9% | 106 / **11.1%** | 21 / 10.8% | 1 |
| 数据与基准型 | 73 / 7.0% | 5 / **10.4%** | 4 / 9.8% | 64 / 6.7% | 15 / 7.7% | 1 |
| 能力扩展型 | 25 / 2.4% | 1 / 2.1% | 0 | 24 / 2.5% | 4 / 2.1% | 0 |
| 效率优化型 | 21 / 2.0% | 2 / 4.2% | 0 | 19 / 2.0% | 2 / 1.0% | 0 |
| 理论分析型 | 2 / 0.2% | 0 | 0 | 2 / 0.2% | 0 | 0 |

**三个方向的差异**
- **共性**：三个方向里瓶颈突破型都在 52%–56% 之间，是默认叙事。在 Oral 中它的占比（57.9%）也不低于整体（56.0%），说明这种叙事写好了同样能拿高评级。
- **自动驾驶**：新问题定义型（18.8%）和数据与基准型（10.4%）明显高于 CV（10.5%、6.7%），发现-解释型（6.2%）偏低。这个方向更奖励"提出新设定、新评测"。
- **具身智能**：统一框架型达到 17.1%，接近 CV 的 1.6 倍，常见的是把感知、规划、控制或多个子任务并进同一个模型。样本里没有能力扩展、效率优化和理论分析型。
- **CV**：分布与总体几乎一致。发现-解释型（11.1%）比另两个方向高出约一倍，纯机制分析和"反直觉发现"在 CV 更容易被接受。

### 1.2 一句话定义

| 类型 | 一句话定义 | 核心句式 |
|---|---|---|
| 瓶颈突破型 | 主流方法在某个可复现的环节上失效，我说清机制根因，再对症把它打通 | "X fails not because A, but because B." |
| 新问题定义型 | 让读者承认一个此前没被正视的问题（新任务、新设定、新失效或新评价标准），方法和数据用来证明它"值得做、做得了" | "we challenge such beliefs" |
| 统一框架型 | 把被割裂的任务、模态或路线合进同一个模型或表示，或把一族方法写进同一个形式，再指出它们的共同缺陷 | "Our central insight is that..." + "unifies" |
| 发现-解释型 | 核心贡献是一个被坐实的发现（现象、根因、错误假设或机制），方法只是这个发现的推论，甚至可以没有方法 | "Yet we observe a striking gap" |
| 数据与基准型 | 领域卡在缺数据或缺统一评测上，我找到了规模化获取标签或构造基准的办法 | "To address this gap, we introduce X" |
| 能力扩展型 | 在一个点名的前作或基座上，把能力扩展到新模态、新维度或新场景 | "we extend X by Y" / "unlike their method, which..., we..." |
| 效率优化型 | 在保持质量的前提下大幅降低时间、内存或 token，常以打破"效率与能力二选一"为卖点 | "linear-time complexity does not directly translate to fast inference" |
| 理论分析型 | 用定理、穷尽分类或形式证明，把领域里靠经验的做法升级为可证明的结论 | "X is a cornerstone of modern Y" + "largely heuristic" |

---

## 2. 如何为自己的工作选择叙事类型

### 2.1 判断流程

按顺序回答下面的问题，**第一个答"是"的就是主类型**。顺序从特征最强的类型排到最泛化的类型，因为瓶颈突破型能兜住几乎所有工作，放在最后。

```
Q1 论文的主要贡献是一种资源吗（数据集、基准、仿真环境、标注协议），
   而模型只是基线或配套？
   → 是：数据与基准型（§8）

Q2 核心贡献是定理、穷尽分类或形式证明，实验只用来验证理论？
   → 是：理论分析型（§11）

Q3 删掉方法部分，论文仍然有独立价值吗？
   或者：不先讲清楚某个发现，方法就显得武断？
   （判据：能用受控实验把"哪里不对"变成一条曲线或一个数字，
     并且这个发现反直觉、能一句话说完、能起专名）
   → 是：发现-解释型（§7）

Q4 读者需要先被说服"这个问题存在或值得做"吗？
   （第一条贡献是"提出/定义新任务、新设定"；需要给新缺陷命名；
     批评对象是整个子领域的默认假设，不是某个方法）
   → 是：新问题定义型（§5）

Q5 你在合并此前分开建模的任务、模态或路线吗？
   或者能把一族已有方法写成同一个公式？
   （判据：能画出一张能力打勾表，现有方法都有空格；
     统一之后能"免费"得到新能力）
   → 是：统一框架型（§6）

Q6 你的工作是在一个点名的前作或基座（VGGT、SAM、DINO、RayZer……）上，
   把它扩展到新模态、新维度或新场景吗？
   → 是：能力扩展型（§9）

Q7 唯一卖点是速度、内存或 token 数，并且质量不降？
   → 是：效率优化型（§10）
   → 如果你还能说清"为什么慢"的机制根因（例如《FlashVDM》发现
     耗时 75.8% 在 VAE 解码），更推荐写成瓶颈突破型，把效率当作瓶颈。

Q8 以上都不是：主流方法在某个具体环节失效，你能说清机制根因，
   并且方法模块和根因能逐条对应
   → 瓶颈突破型（§4）
```

### 2.2 容易混淆的边界

| 纠结 | 判断方法 |
|---|---|
| 瓶颈突破 vs 发现-解释 | 看引言里篇幅最大、最先让读者惊讶的是"诊断"还是"方案"。如果诊断实验要占一整段以上，还起了专名（如 Gradient Entanglement），就用发现-解释型。 |
| 瓶颈突破 vs 新问题定义 | 瓶颈突破型默认读者已经承认问题存在，只是没人解决；新问题定义型要先说服读者这个问题存在。 |
| 新问题定义 vs 数据与基准 | 卖点是"问题"本身就用前者，名字要朴素（《Counting Stacked Objects》）；卖点是"资源"就用后者，名字要好记，最好把规模数字写进去（Derm1M）。 |
| 统一框架 vs 能力扩展 | 统一框架型是把 N 条路线合成一条；能力扩展型是把一条路线往外延伸一个维度。名字上也能看出区别：Uni-/All in One/Meets 对应前者，Omni-/Wild-/Phys- + 前作名对应后者。 |
| 效率优化 vs 瓶颈突破 | 如果效率问题有机制根因，并且方案针对这个根因，就写成瓶颈突破型（《FastGS》《FlashVDM》都属于这一类）。只有在"二元对立被打破"本身是卖点时，才写成效率优化型（《Sparse-LaViDa》）。 |

### 2.3 类型组合

主类型决定引言骨架和贡献列表的第一条；辅类型只贡献一个段落、一种变体或一条贡献。**不要让两个类型平分引言**，否则读者抓不住主线。

| 组合 | 写法 | 实例 |
|---|---|---|
| 发现-解释 + 瓶颈突破 | 引言前半段用受控实验坐实一个反直觉发现，并给它起名；后半段把发现当作根因，引出对症的方法 | 《LitePT》（先证伪：SOTA 67% 参数是卷积 → 发现分工 → 方法名到第 4 段才出场）；《CorrCLIP》；《GRPO-Guard》 |
| 瓶颈突破 + 实证前置 | 在引言里放 pilot 实验，先坐实根因 | 《FlashVDM》（VAE 解码占 75.8%）、《ATCTrack》（29.9%→96.7%） |
| 新问题定义 + 数据与基准 | 按"任务定义 → 没有基准 → 没有模型"推进，贡献写成"问题 + 基准 + 基线"三件套 | 《PixDLM》；《DropletVideo》（概念 / 数据集 / 模型 / 开源四条线） |
| 数据与基准 + 方法 | 双缺口并行：数据缺口和方法缺口分两段论证，各对应一条贡献；或先建基准、测出负面结果，再引出方法 | EffectErase、EgoAVU、Derm1M；PanoEnv、GeoMMBench+GeoMMAgent（实测出新问题） |
| 统一框架 + 发现驱动 | 先用一张图或一个数字"看见"两派方法互补，再用统一方案兑现 | 《CD-Buffer》（交叉曲线）、《AToken》（19% rFID 下降）、《MotionCrafter》 |
| 统一框架 + 理论诊断 | 把前人方法写成同一个公式（相当于把前作收编为特例），再在这套语言下指出共同缺陷 | 《CFG-Ctrl》（统一为 `ut=KtΠt(e(t))`，都是线性控制律）、《SenCache》 |
| 理论分析 + 瓶颈突破 | 先指出一族改进"largely heuristic"，再用定理给出上界并替换公式 | 《C²FG》 |
| 能力扩展 + 发现 | 在扩展过程中意外发现某种能力有效，走"意外发现 → 假设 → 验证"闭环 | 《Chorus》（3DGS 预训练在点云任务上意外有效） |
| 新问题定义 + 瓶颈突破（双层缺口） | 上一代 SOTA 解决了老问题，却带来新瓶颈 | 《Heavy Labels Out!》（软标签有效，但存储代价太大）、《EcoSplat》 |

**组合的写作顺序**：辅类型如果是"发现"或"诊断"，放在主类型的根因位置；辅类型如果是"资源"，放在方法之后，作为第二条贡献；辅类型如果是"统一"，放在洞察位置，用一句 "unifies" 收束。

---

## 3. 所有类型共享的叙事原则

### 3.1 摘要：8 句、五段式

**统计事实（1040 篇）**
- 句数中位数是 8，四分位 [7, 9]。8 句占 25.2%，7 句占 19.8%，9 句占 18.2%。**默认写 7–9 句。**
- 第 1 句：纯背景 56.6%，背景+问题 21.2%，背景+缺口 7.3%，直接写方法 6.6%。
- 最后 1 句：资源发布（代码、数据开源）43.1%，结果+意义 17.9%，结果 12.0%，意义 10.4%。
- 把摘要五等分后，每段的主作用：

| 位置 | 前三名作用 | 写什么 |
|---|---|---|
| 第 1/5 | 背景 57%，问题 18%，缺口 11% | 1 句背景，最多再加 1 句问题 |
| 第 2/5 | 方法 44%，缺口 18%，设计细节 11% | 缺口或根因 1 句，然后方法名出场 |
| 第 3/5 | 方法 38%，设计细节 35%，洞察 8% | 2–3 句设计细节，每句一个模块 |
| 第 4/5 | 结果 40%，方法 23%，设计细节 20% | 带具体数字的结果 |
| 第 5/5 | 结果 42%，资源发布 37%，意义 12% | 泛化或意义，最后写开源 |

**高频作用序列**（取每句主作用，合并相邻重复）：
- 背景 → 缺口 → 方法 → 设计细节 → 结果（2.5%，最常见）
- 背景 → 问题 → 方法 → 设计细节 → 结果（2.1%）
- 以上两条末尾再加"资源发布"（1.9%、1.7%）

**模板（8 句）**
```
S1 背景：领域 + 用场景或数字证明重要。
S2 缺口/问题：点名主流路线在哪个环节失效（带数字或现象）。
S3 根因或洞察："We identify/observe that ..." （洞察句只占 8% 左右，写出来就是区分度）
S4 方法："We propose X, a ... that ..."
S5–S6 设计细节：每句一个模块，模块名与引言、方法小节一致。
S7 结果：具体数字，与引言、结论同一口径。
S8 意义或开源："Code and data will be released at ..."
```

各类型的差异：数据与基准型的最后一句几乎必定是资源发布；发现-解释型的 S3 要写成发现句；新问题定义型的 S2 可以直接写成规范性断言或反问。

### 3.2 引言：5–6 段

- 段数中位数是 6，四分位 [5, 6]。5 段占 29.1%，6 段占 27.1%，4 段占 16.9%，7 段占 15.6%。
- 贡献列表：bullet 形式 74.4%，行内 25.0%，不写 0.6%。**默认用 bullet。**
- 贡献类型：64.8% 的论文把 Insight 列为贡献之一，91.8% 包含 Performance，79.1% 包含 Capability；只有 Insight 的论文仅 0.9%。**即使是发现-解释型，也要给出性能或能力上的兑现。**

**6 段模板**
```
P1 重要性：场景 + 数字 / 产业锚点 + 引用。不写 "important"。
P2 现有路线与瓶颈：点名 2–4 个代表方法，每个只配一个病症，用 (i)(ii)(iii) 编号。
P3 根因：落到机制、公式或隐含假设，给它起名；可以放 pilot 实验或 Fig.1。
P4 洞察 + 方法名："Our key insight is that ..." → 隔 1–2 句 "Based on this, we propose X"。
P5 方法概要：每个模块对应一个根因或挑战。
P6 贡献列表（bullet）+ 核心数字。
```
洞察句放在第 3–5 段，这一点在八种类型里都一致。

### 3.3 根因、洞察、命名三件套

1. **根因写到机制层**：写"空间分辨率坍缩到 7×7"，不写"层数太深"；写 "These issues stem from evaluating pixel contributions independently."（《VX-CODE》），不写"能力不足"。
2. **给根因或发现起名**，方便全文回指：motion bias（《FPRL》）、rank collapse（《OSA》）、manifold drift（《GeoRK2》）、Gradient Entanglement。
3. **洞察独立成句**，用信号词："Our key insight is that ..." / "We observe that ..." / "The crux of our approach is ..." / "X should be A, not B"。
4. **方法名紧跟在洞察之后 1–2 句内出场**，并在摘要、引言、结论中用同一个措辞。
5. **先排除读者最先想到的朴素方案**：朴素方案证伪（《Dark3R》）、候选路线逐一排除（《No Calibration, No Depth, No Problem》连续 4 段）。

### 3.4 方法：问题驱动的求解链

所有类型共用的方法写法（问题驱动的求解链、先直觉后公式、设计理由、各类型的组织差异）已整理进 `references/sections/method.md`，见其第 0 节速查和第 2 节。

### 3.5 实验：贡献 i ↔ 方法 3.i ↔ 表 i

三层证据、排除替代解释、主张强度分级、各类型的实验侧重见 `references/sections/experiments.md` 第 0、2 节。

### 3.6 局限与结论

局限最多 2 条，每条写成"适用边界 + 方向"，放在结论之前的 Limitations 段或结论中间，不放在摘要、引言，不作为全文最后一句；结论不复述摘要，只强化记忆点，最后一句落在意义上。各类型的收尾重点见 `references/sections/conclusion.md` 第 0、2 节；不利结果和局限的处理以 `references/anti_defensive.md` 为准。顶会论文多数不设独立局限小节，本 skill 的做法是最多 2 条、简短。

### 3.7 Figure 1 与数字一致性

- 91.3% 的论文有 teaser 图（Figure 1），但八种类型的汇总里都反复出现"Fig.1 从未在引言正文被引用"的问题。**引言里必须有一句 "as shown in Fig. 1"。**
- 核心数字在摘要、引言、贡献、结论四处必须一致。反面例子：《AsymLoc》同时写了 95% / 95.5% / 96%；《Counterfactual VLA》摘要写 20.5%，正文是 14.7%。正面例子：《Event-based VDM》的 1.6×/18.9%、《AutoMoMa》的 60→5,000 trajectories/hour 在三处保持一致。
- 贡献条数要前后一致：《Harmonic Canvas》说 threefold，实际列了四条；Bokehlicious 摘要说 threefold，结论里只提到 two。

### 3.8 通用检查清单

- [ ] 摘要 7–9 句，第 1 句是背景（最多带问题），最后 1 句是结果、意义或开源
- [ ] 引言 5–6 段，洞察句在第 3–5 段，用了信号词
- [ ] 重要性用场景或数字证明，没有空泛的 "important"
- [ ] 根因写到机制层，并且有名字
- [ ] 方法名在洞察之后 1–2 句内出场，全文措辞统一
- [ ] 排除了读者最先想到的朴素方案
- [ ] 方法小节开头交代要解决的遗留问题，先直觉后公式
- [ ] 贡献 i ↔ 3.i ↔ 表 i，消融变体名与模块名一致
- [ ] 有排除替代解释的实验，也有验证洞察本身的机制实验
- [ ] 核心数字在摘要、引言、贡献、结论四处一致；贡献条数前后一致
- [ ] Fig.1 在引言正文被显式引用
- [ ] 措辞强度与实际排名一致：不是第一的地方收缩主张，不专门写一句输了（`references/anti_defensive.md` §3）
- [ ] 局限最多 2 条，写成"适用边界 + 方向"；摘要、引言里没有局限，局限不是全文最后一句
- [ ] 结论有摘要之外的新信息，最后一句落在意义上
- [ ] 定稿前检查拼写（反例：标题里的 RhythmGuassian、"soficsticated"、"that that"）

---

> 取名（标题格式、方法名构造、按叙事类型选命名风格、取名流程与避坑）见 references/naming.md，按叙事类型的取名差异见其中 §6。

---

## 4. 瓶颈突破型（56.0%）

### 4.1 定义与识别特征

主流方法在某个具体、可复现的环节上失效（精度、效率、泛化、一致性），你能说清失效的机制根因，并针对根因设计方案把它打通。满足下面三条就适合这类故事：
- 问题能用一张失败图或一个数字说清。例：《FastGS》用 "tens of minutes" 对比标题里的 100 Seconds；《DAP-MAE》数据变多，精度反而从 94.15% 降到 91.73%。
- 根因能落到公式、隐含假设或具体模块上。例：《MODIX》指向 RoPE 的 p_i=i；《Does YOLO...》指出训练默认"每张图贡献相等"。
- 方法模块能和根因逐条对应。

如果主要贡献是定义新任务、发布数据集或纯理论，应该换别的类型。

### 4.2 叙事骨架

**标准链**：领域重要性 → 现有路线与具体瓶颈 → 根因诊断 → 核心洞察 → 方法（问题驱动的求解链）→ 多层证据 → 意义与边界

| 变体 | 做法 | 适用情况 | 例 |
|---|---|---|---|
| 编号对称 | 瓶颈(1)(2) ↔ 模块(1)(2) ↔ 消融(1)(2) | 有 2–3 个彼此独立的瓶颈 | 《SD-IF》《ANTS》《Self-Calibrating GS》 |
| 二次转折 / 套娃 | 方案 A 解决表层问题后暴露更深的问题，再给方案 B | 方法本身分多级 | 《DirectFisheye-GS》、《WINS》→WINS-B→WINS-AB、《Reward Forcing》 |
| 朴素方案证伪 / 排除法 | 先否定直觉解或 2–3 条候选路线 | 读者会先想到简单解法 | 《Dark3R》《Interaction-Merged Motion Planning》《FloodDiffusion》 |
| 继承者叙事 | 只针对最近的前作做机制级逐点批评 | 工作是对某篇前作的直接改进 | 《E-RayZer》（引用 RayZer 自己的 Tab.7）、《MeshLLM》、《EVEv2》（批评自家前作） |
| 实证前置 | 在引言里放 pilot 实验或统计，先坐实根因 | 根因反直觉，需要数据说服 | 《FlashVDM》（VAE 解码占 75.8%）、《VRM》、《ATCTrack》（29.9%→96.7%） |
| 理论诊断 | 用定理证明必然失败或不可辨识，或把前作收编为特例 | 有形式化结果 | 《2D-LFM》《CIGPose》《B³-Seg》《On the Provable Importance of Gradients》 |
| 类比驱动 | 借认知科学或其他领域的机制立起洞察 | 洞察对读者陌生 | 《SEGA》（快/慢思考）、《HippoSense》、《STCast》 |
| 评测批判 | 指出现有评测协议本身有漏洞 | 旧指标掩盖了问题 | 《PPISP》（PSNR-CC）、《VMem》（cycle-trajectory） |

### 4.3 逐步写法

**① 重要性**：用场景加引用、数字或产业锚点证明，不写 "important"。
- "Deformation is ubiquitous in ..."，后接三类应用，各配引用（《Event-based VDM》）
- "Nvidia AGX Orin ... offers only 3.4% of the computational resources of a Nvidia A100"（《SEELE》）
- 先承认成绩再划边界："achieve strong performance on test sequences *within the same dataset* used for training"（《BUFFER-X》）

**② 瓶颈**：点名最强的基线，配失败图或数字；用让步句，避免显得贬低前人。
- "Despite their effectiveness, these approaches universally focus on ..."（《DGA》）
- "X achieves Y. However, Z, as shown in Fig. 1(b)."
- 用 ✔/✗ 能力对比表代替文字综述（《OVI-MAP》《Gallant》）

**③ 根因**：写到机制层，把多个现象归到同一个根因，并给根因起名。
- "These issues stem from evaluating pixel contributions independently."（《VX-CODE》）
- "We argue that this tension stems from a shared design choice ..."
- "... address the symptom but not the underlying cause."（《FACE》）
- "We attribute this limitation to X, which is sufficient for Y but ineffective for Z."（《SuperDec》）
- 根因命名：motion bias（《FPRL》）、rank collapse（《OSA》）、attribute confusion（《LOTS of Fashion》）
- 佐证：统计量（《HyperGait》r=0.82）、定理（《TEMF》梯度方差）、亲身证词 "we failed to train it without NaNs"（《Gated KalmaNet》）

**④ 洞察**：放在引言第 3–5 段，信号句单独成句，紧接着给方法命名，再跟一条可验证的性质。
- "Our key insight is that ..." / "We observe that ..." / "The crux of our approach is ..."
- 再定义式："X fails not because A, but because B."（《SeDiR》）
- 设问式："Can we bypass per-scene optimization entirely?"（《PhysGM》）、"Is fully Gaussian noise needed?"（《PixelRush》）
- 常识对比："humans can't easily *generate* 3D shape models ... but they can *select*"（《SAM 3D》）

**⑤ 证据**：
- 三层证据：主表 → 逐组件消融（w/o 模块名）→ 验证洞察本身的机制实验。
- 排除替代解释：参数量对照（《OASIS》）、"只是加了噪声"对照（《SD-IF》Tab.7/8）、Discussion 自问"提升是否只来自外部先验"（《CAD》）。
- 在对自己不利的设置下仍然胜出："our evaluation setup is conservative"（《LLSA》）。
- 主张强度分级（《GPERT》：全面领先才写 SOTA，部分领先写 competitive）、具体比值（《SAM 3D》5:1）。失败案例可选，放补充材料即可（《PixelRush》《WeaveSeg》）。

取名建议见 references/naming.md §6.2（瓶颈突破型）。

### 4.4 全文递进

- **方法**：问题驱动的求解链（见 §3.4）。模块只有真正独立时才并列，并按数据流排序。
- **实验**：贡献 i ↔ 3.i ↔ 表 i；小节标题可以写成它回答的问题（《DocSeeker》4.3）或 Q1/Q2/Q3（《Moto》）。数据集、理论界、"首个框架"类贡献必须独立验证。
- **局限与结论**：局限最多 2 条，写到所修环节的"适用边界 + 方向"（《HairCUP》《Gallant》）。结论首句回收引言中定义方法的那句话，补上摘要之外的信息，最后一句落在意义上。

### 4.5 代表论文

1. **《Event-based Visual Deformation Measurement》**：两个挑战对称对应两个模块，1.6×/18.9% 贯穿摘要、贡献和结论，是标准范式。
2. **《DirectFisheye-GS》**："Even with a correct fisheye camera model, insufficient optimization ..."，挖出了第二层瓶颈。
3. **《E-RayZer》**：不铺陈文献，用前作 RayZer 自己的失败数据做机制级逐点批评。
4. **《Unleashing Vecset Diffusion (FlashVDM)》**：一张耗时分布图揭示瓶颈在 VAE 解码，而不在扩散采样。
5. **《CIGPose》**：用结构因果模型把"解剖学荒谬错误"形式化为后门路径问题。
6. **《Learning to Diversify and Focus (SD-IF)》**：两个瓶颈、两个模块、两组排除性实验，三层闭环。
7. **《WINS》**：WINS → 负载不均衡 → WINS-B → 层间差异 → WINS-AB，链式自我迭代。
8. **《AutoMoMa》**：60 → 5,000 trajectories/hour，新旧数字对撞构成全文钩子。

### 4.6 常见失误与检查清单

**常见失误**
- 贡献与实验错位：数据集或理论界没有独立验证（《Ditto》《Stable Mean Flow》）；贡献列表里有 "Extensive experiments..." 这类务虚条目；用词与数字不符（《SeeGroup》声称 "all metrics"，实际是 14/15）。
- 消融降幅被轻描淡写：《FlexMem》51.0→45.7，只写了 "minimal"。
- 宣称超出实验范围（《CAC》声称 "embodied AI"）；模块名前后不一致（《RAVEN》）。

**检查清单**（在 §3.8 基础上）
- [ ] 瓶颈能用一张图或一个数字表达，并点名了具体基线
- [ ] 根因落在机制、假设或公式上，并且有名字
- [ ] 洞察句在引言里已有支撑证据（pilot 实验、统计或定理）
- [ ] 证伪了读者最可能想到的朴素方案
- [ ] 数据集和理论贡献有独立实验
- [ ] 消融降幅的措辞与数字相符
- [ ] 方法名能读出来，呼应洞察或谱系

---

## 5. 新问题定义型（11.0%；自动驾驶 18.8%）

### 5.1 定义与识别特征

核心贡献是**让读者承认一个此前没被正视的问题**：新任务、新设定、新失效现象、新评价标准，或对旧问题的重新表述。方法和数据用来证明"这个问题值得做、而且做得了"。满足两条及以上时适用：
- 第一条贡献就是"提出/定义新问题"。例：《Towards Multimodal Domain Generalization with Few Labels》用 Fig.1(a) 画出既有范式各缺哪一块。
- 能给新设定或新缺陷起名：manifold drift（《GeoRK2》）、label correlation drift（《FedHarmony》）、Semi-Supervised Multimodal Domain Generalization。
- 在提出方法之前，要先用实验证明问题存在。例：《Unstitching the Chimera》做了 600 例人工审计，得到 34% 的占比和 κ=0.76。
- 贡献是"问题 + 基准 + 基线"组合：《PixDLM》按"任务定义 → 无基准 → 无模型"推进；《DropletVideo》分"概念 / 数据集 / 模型 / 开源"四条线。
- 质疑的是领域默认假设，不是某个具体方法：《Rethinking MER》。

### 5.2 叙事骨架

**标准链**：领域重要性 → 现有方法的具体瓶颈（点名文献，常配自建实证）→ 根因（落到一个机制或变量）→ 新问题 / 新概念命名 → 核心洞察 → 方法（问题驱动的求解链）→ 多层证据 → 意义与首创声明

| 变体 | 适用情况 | 例证 |
|---|---|---|
| 诊断实验先行 | 问题是否存在本身有争议 | 《FluoCLIP》先用与自身方法无关的 SF/SRCC 指标坐实现象；《Widget2Code》先跑 benchmark 再归因 |
| 质疑默认假设 | 批评对象是整个子领域的评测惯例 | 《Rethinking MER》连续用反问句质疑关键帧假设 |
| 解决方案自带新问题（双层缺口） | 上一代 SOTA 刚解决老问题 | 《Heavy Labels Out!》：软标签有效但存储代价太大；《EcoSplat》：feed-forward 快了，高斯数量却不可控 |
| 双层 CARS 嵌套 | 先要论证新硬件或新范式值得存在 | 《MetaScope》：先论证 metalens 可行，再论证其色差需要算法解决 |
| 逐一证伪候选路线 | 读者会想到多种"显然解法" | 《No Calibration, No Depth, No Problem》连续 4 段排除；《Magic Insert》三段排比驳斥稻草人；《LaRender》先驳斥"训练遮挡条件生成模型" |
| 先立评价标准 | 新范式下"什么算好"尚未约定 | 《Action Motifs》给出好表示的三条标准；《Image Diffusion Preview》给出 Fidelity/Efficiency/Consistency |
| 双线 / 三挑战并列 | 根因可拆成相互独立的子问题 | 《SCORE》视觉端与文本端对应 RAI 与 GCA；《AdvDreamer》三段 "How to...?" |
| 理论先行 | 洞察可以写成定理 | 《RaUF》Theorem 1/2；《QuadSync》Theorem 3.1 |
| 方案先行、洞察补证 | 机制直观，但要解释为何可行 | 《SliderEdit》先给滑块，再做 token 插值小实验补证 |

### 5.3 逐步写法

**1. 证明问题重要：钉死场景和数字。**
- 应用场景："smart glasses, battery life and heat dissipation"（《AsymLoc》）；"3–4 名设计师、3–4 周"（《GardenDesigner》）。
- 反直觉数字：《DINO Omnivore》摘要给出 RGB 与深度的余弦相似度 0.24，随机图像对为 0.26；《Understanding Task Transfer》对比 GPT-4o 的 60.04% 与人类的 95%。
- 规范性断言或反问开篇："4D generation should be diverse in terms of motion."（《DIMO》）；"But what speed can be achieved for a given light level?"（《Inter-Photon-Limited》）。
- 让可视化失败先于文字出场：《PAVAS》的锤子声频谱图；《ResiHMR》Fig.2 的幻觉肢体。

**2. 揭示瓶颈和根因：给出可以命名的机制。**
- 让步转折："While CAC ... can mitigate ..., it cannot recover the contrast loss induced by diffuse scattering."（《VeilGen》）
- "A rather than B"："the reasoning in current VLAs is largely descriptive rather than self-reflective"（《Counterfactual VLA》）；"resembles spatio-temporal point clouds rather than conventional 2D images"（《E²MN》）。
- 一句话技术归因："These methods fundamentally perform pixel-space regression."（《Where, What, Why》）
- 用物理公式或控制变量钉住根因：《FluoCLIP》用 d∝λ/NA 得出约 1.6× 的差异；《Multispectral Demosaicing》设想两台只差 CFA 的相机；《AntiPure》用三组小实验分别坐实三条根因。
- 以权威悲观论断为靶："[1] state that ... are useful only from a theoretical stand-point" → "we challenge such beliefs"（《QuadSync》）。
- 把缺陷命名为概念资产，方便后续工作引用（manifold drift）。

**3. 核心洞察出场：引言第 3–4 段，显式标记。**
- "Our key insight is that ..."（《SliderEdit》《DIMO》）；"We observe that ..."（《U4D》）；"we hold that a more rational paradigm is ..."（《GraspALL》）。
- 重构句式："we reframe physics prediction not as a deterministic regression task, but as a problem of learning a controllable physical spectrum"（《UniPixie》）。
- 先写朴素直觉，再用 However 修正："not to maximize visual dependence globally but to evaluate ... regions relevant to the given situation"（《Draft and Refine》）。
- 类比："Inspired by how humans resolve ambiguous regions ..."（《U4D》）；《DINO Omnivore》借 NLP 多语言编码器；《Hierarchical Material Recognition》借"tree of life"。
- 对称反问收束两条路线："How can we build an SMPL-like model...?" / "How can we directly output a 4D object...?"（《DIMO》）
- 洞察成立后，另起一段列出 N 个工程障碍再逐条求解（《GM-R²》《Human-Centric MEF》）。

**4. 证据。**
- 系统扫描：多数据集 × 多骨干 × 多档设置（《EcoSplat》四档压缩比）。
- 拆开方法贡献与数据贡献：《OACIR》用同一个 SPRC 模型在两个数据集上训练，37.30% vs 74.05%。
- 自设劣势仍胜出：《CObL》的对手用 oracle mask，自己不用。
- 一类质疑配一类证据：《IQA-Adapter》用 21 个 IQA 模型、GenEval、千人主观研究和参考图实验，分别回应四类质疑。
- 反事实实验（《No Calibration》的 Pre-GS Comparison）、人类基线（《Counting Stacked Objects》）、显著性检验（《FedHarmony》Wilcoxon）。

取名建议见 references/naming.md §6.2（新问题定义型）。

### 5.4 全文递进

- **方法**：问题驱动的求解链。小节以 "Motivation" 开场（《FedSDR》），或写 "This motivates us to leverage ..."（《FILTR》），或在子问题末尾标注 "Motivation: ...(Sec. 4.1)"（《MetaScope》）。另一种写法是先写理想公式、指出不可解、再逐步修正：《CounterPC》从 Eq.1 走到 Eq.6；《Counting Stacked Objects》从 N=V/v 改为 N=γV/v。
- **实验**：一条贡献一张表（《4D-RGPT》）；RQ1/2/3（《SAME》《URICA》）；问题直接当标题："How well do existing models reflect physics?"（《PAVAS》）；消融按贡献顺序累加（《CounterPC》Table 2）。
- **局限与结论**：约七成没有独立 Limitations；本 skill 的做法是最多 2 条、简短。好做法：编号列出最关键的假设（《SceneMI》(i)(ii)(iii)，照搬时只取两条）；"边界 + 方向"合成一句："While FluoCLIP assumes predefined stain categories, future work will ..."；把局限框定为正交技术可解（《Teeth Reconstruction》依赖 SAM2，可用 Personalize-SAM 自动化）。结论与引言首句同构，常用 "paving the way for ..." 收尾。

### 5.5 代表论文

1. **《A Mixed Diet Makes DINO An Omnivorous Vision Encoder》**：用反直觉的相似度数字当钩子，借 NLP 历史类比说明跨模态对齐是必然方向，再用五重实验兑现。
2. **《No Calibration, No Depth, No Problem》**：逐一证伪四条候选路线，三重否定标题当钩子，Pre-GS 反事实实验堵住质疑。
3. **《Rethinking Key-frame-based Micro-expression Recognition》**：质疑整个子领域的评测假设，用可控误差和真实误差两类实验双重验证。
4. **《Heavy Labels Out!》**："上一代 SOTA 自己制造了新瓶颈"，标题和方法名 HeLlO 同时回应这个两难。
5. **《RaUF》**：用"哭脸 vs 笑脸"的 Figure 1 具象化冲突监督问题，再把洞察升格为 Theorem。
6. **《Understanding Task Transfer in Vision-Language Models》**：加框的研究问题句提出新问题，玩具表格讲清 PGF 度量，task persona 让发现好记。
7. **《AdvDreamer》**：三段 "How to...?" 对应 ❶❷❸ 三个模块和 RQ1–RQ3 三组实验，结构呼应最工整。

### 5.6 常见失误与检查清单

**常见失误**
- 数字口径不一：《AsymLoc》95% / 95.5% / 96%；《Counterfactual VLA》摘要 20.5%、正文 14.7%；《RCNMC》"12 个配置"与"9 个数据集"并存且未解释。
- 贡献与实验脱节：《GM-R²》的 Denoising-Agnostic 没有消融；《UPA-RFAS》宣称 "strong baseline for future defenses" 却没有防御实验；《VeilGen》只有定性图；《DropletVideo》缺少与 SOTA 的定量表。
- 贡献条数或句式不统一：《Harmonic Canvas》说 threefold 实际四条；《DIMO》第 4 条是无主谓的凑数条目；《Human-Centric MEF》只有一条用了被动语态。
- Fig.1 未被引用：《CounterPC》全文最大的钩子只出现在图注里；《Action Motifs》《BRICKGPT》同样如此。
- 局限空泛：《FGAesQ》只写 "remains challenging"，读者不知道边界在哪。
- 引言复述摘要（《SVLTrack》）、方法与实验之间无过渡（《BiPreManip》）、语病（《A Style is Worth One Code》"establishes opens up"）。

**检查清单**（在 §3.8 基础上）
- [ ] 问题重要性绑定了具体场景和可核验数字
- [ ] 新问题、新设定或新缺陷有名字
- [ ] 提出方法前，用与自身方法无关的诊断实验证明了问题存在
- [ ] 读者可能想到的显然解法已逐一排除
- [ ] 洞察有显式标记句，并有类比、反问或定理支撑
- [ ] 每条贡献都有对应的表格或消融；条数与措辞一致
- [ ] 命名与卖点匹配：新任务配朴素名，新系统配响亮缩写或双关

---

## 6. 统一框架型（10.8%；具身 17.1%）

### 6.1 定义与识别特征

三类工作适合写成统一框架型：
- **合并被割裂的任务、模态或路线**：《Ov3R》把 SLAM/3R 和开放词汇语义合在一起；《AToken》做统一视觉 tokenizer；《GT-Loc》统一 when 与 where；《Copernicus-FM》处理任意传感器。
- **把一族方法写进同一理论语言，再指出共同缺陷**：《CFG-Ctrl》把 CFG 系方法写成 `ut=KtΠt(e(t))`，指出它们都是线性控制律；《SenCache》用同一个敏感度框架解释 TeaCache/MagCache 为什么时成时败。
- **用一个机制同时补上两条技术脉络的缺口**：《Hermite RBF》（RayGauss 线与 HRBF 线）、《Global Structure-from-Motion Meets Feedforward Reconstruction》。

识别信号：标题里有 Unified / Unifying / All in One / Meets；引言能写出"两条路线各有短板"或"N 个子任务被分开建模"；能画出一张能力打勾表，现有方法都有空格（《RESCUE》《GRACE》《VeriDou》的 Table 1）；统一之后能"免费"得到新能力（《GT-Loc》的统一嵌入空间顺带支持检索）。

### 6.2 叙事骨架

**标准链**：领域重要性 → 点名现有方法的具体瓶颈 → 一句话说出根因 → 核心洞察（换一个角度看问题）→ 方法逐项兑现洞察 → 多层证据 → 统一或范式层面的意义

| 变体 | 适用情况 | 代表 |
|---|---|---|
| 双缺口收敛 / 双线汇流 | 两条脉络各自留白，一个方案同时补齐 | 《Ov3R》《Hermite RBF》（"Guided by these considerations"）《Omni2Sound》 |
| 统一视角重构 | 已有方法能写成同一形式 | 《CFG-Ctrl》《SenCache》 |
| 发现驱动 | 手上有反直觉的实证现象 | 《CD-Buffer》（Fig.1 交叉曲线）《AToken》（19% rFID 下降）《MotionCrafter》 |
| oracle 量化 | 能先做受控实验把上限数字化 | 《ComPose》（68.5%→91.7%，朴素两阶段只有 71.0% 且更慢） |
| 挑战–方案强对称 | N 个局限各对应一个模块 | 《MTU3D》（First/Second/Third 对 1)/2)/3)）《GeniNav》《FoleyDesigner》 |
| 双层递归 / 两代批判 | 方案本身又引出新问题 | 《POLAR》（"chicken-and-egg"）《UniPhys》《DPoser-X》《Vanast》（"Yet two challenges remain"） |
| 自我反驳 | "统一"的思路对，问题出在实现方式 | 《TUNA》（先论证统一表征更优，再用 "Nevertheless" 推翻） |
| 先定标准 | "统一"太抽象，难以核验 | 《All-in-One LIDMark》（Is it fake? / Where is it fake? / Whose is it?） |
| 历史翻案 | 某个经典工具被冷落 | 《Affine P3P》（"This paper revisits the P3P problem from ... broader historical and practical perspectives"） |
| 问题 / 假设先行 | 动机能压缩成一个可检验的问句 | 《RePoseD》《RnG》（"we hypothesize"）《SAMTok》（"How can we ... as simple as VQA training?"） |

### 6.3 逐步写法

**① 重要性：数字、物理事实或场景，不用形容词。**
- "covering approximately 31% of the Earth's land surface"（《ForestFormer3D》）
- 数量级反差："billions of parameters" vs "a few seconds"（《SenCache》）
- 《RARE》用针孔几何算出 20/30/40 m 处 0.36–1.43 m 的深度误差。
- 生活化失败：《Omni2Sound》里网球拍声被误判成烟花。
- 第二人称代入：《MTU3D》"想象你走进一个陌生房间找吃的"。

**② 瓶颈：点名 2–4 个代表方法，每个只配一个病症，用 (i)(ii)(iii) 编号。**
- "[X] handle specular surfaces but introduce noise in low-textured areas (Sec. 3.3)"（《HiNeuS》）
- 用 However / While / Conversely 区分三类方法（《CUBE》）。
- 先扬后抑："Although this strategy aligns well with streaming video requirements, the reliance on aggregating coarse historical information ... often leads to the loss of important fine-grained ... details."（《StreamFormer》）
- 失败写成画面："failing to produce realistic shadows or highlights"（《GeoRelight》）；《TAlignDiff》分子左移导致邻牙逆时针旋转。

**③ 根因：一句话归到同一个机制，这是"统一"的逻辑起点。**
- "The root of this dilemma is not architectural, but a learning objective."（《Transition Models》）
- "All the leading methods are derived from PDEs..."（《Discontinuity-aware NI》）
- 《NeAR》：资产生成假设渲染器固定，渲染器又在静态资产分布上训练，两者从未联合优化。
- 《D4RT》逐一批评 MegaSaM/VGGT/SpatialTrackerV2 后，用 "Crucially" 把共性缺陷抬升为致命问题。

**④ 洞察：引言第 3–4 段。**
- "Our central insight is that..."（《AToken》）、"Crucially, we observe..."（《CrossHA》）、"X should be A, not B"（《RARE》）、"we hypothesize that..."（《RnG》）、"Surprisingly, ..."（《Linear N-Point Solver》）。
- 类比背书："This mirrors how humans perceive the world"（《CUPID》）；《AToken》借 LLM 的统一能力。
- 失败案例分析：《GT-Loc》先讲对比学习为什么在位置任务上成功，再讲为什么在时间任务上失效——"temporal neighbors often look nearly identical ... designating adjacent time points as negatives undermines effective alignment"。
- 先驳倒替代方案：《Omni-3DEdit》先设想一个 latent-space 方案再否掉。
- 洞察与命名两种顺序都可以：先洞察后命名（《CD-Buffer》）；先命名后回填洞察（《D4RT》）。

**⑤ 证明"统一"本身成立（最容易漏）。**
- 映射表：《CFG-Ctrl》Table 1 把前人方法逐一映射进统一公式。
- 推导复现：《Affine P3P》的推导逐字复现已有解。
- 反向解释：《SenCache》用同一框架解释竞品为什么成败。

**⑥ 证据。**
- 直觉图 + 理论 + 数值互相印证（《CFG-Ctrl》：相平面图 + Lyapunov 证明 + Table 2/3）。
- 正反双向消融："w/o Geometry vs. Joint Modeling"（《GeoRelight》）。
- 失败变体：《Optical Flow Matching》的 OFM-Naive EPE 在 15 以上。
- 假设–消融闭环：《Spherical Leech Quantization》Table 8 对应 Sec. 3.3 的假设。
- 显著性：《D-Convexity》10 次配对 t-test。
- 用词强度匹配证据：不是第一的地方收缩主张，或用 comparable / competitive with，不专门写一句输了（`references/anti_defensive.md` §3）。
- 反差钩子贯穿全文：《ReMoT》4B 胜 30B；《Transition Models》865M 胜 8B/12B；《DataTailor》的 "101.3%" 在摘要、引言、结论各出现一次。

取名建议见 references/naming.md §6.2（统一框架型）。

### 6.4 全文递进

- **方法**：问题驱动的求解链，段首复用上一节的变量名（《ComPose》；《x2-Fusion》"Benefiting from the tri-modal alignment..."）。先直觉后公式（反例：《ConFu》《BQ-SRC》《CUPID》公式先行）。模块多时"总览图 + 路线图句"（《AAA-Gaussians》）。沿数据流平铺模块（《Easy3D》《Uni3R》《UniLight》）只适合工程系统。
- **实验**：每条贡献一张表或一组消融（《M2SFormer》Table 3/4）；消融顺序复现挑战列举顺序（《PiLoT》按 "impossible triangle" 三维依次消融）；RQ 式小标题（《CrossHA》Q1–Q3、《VeriDou》RQ1–5）。额外实验要预先写进贡献（反例：《UniDxMD》4.5 节、《DataTailor》4.3 节）。
- **局限与结论**：局限最多 2 条，写成具体的适用边界——"struggles with occluded structures in limited-view training and deformable scenes"（《HiNeuS》）、"may underperform under extremely fast dynamics"（《AeroGS》）、依赖针孔相机模型（《AAA-Gaussians》）。让步模板："Although our study focuses on X, Y is modality-agnostic."（《SGDIR》《x2-Fusion》）

### 6.5 代表论文

1. **《CFG-Ctrl》**：用控制论语言统一 CFG 系方法，在这套语言下指出都是线性控制律，再给非线性解。"统一视角重构"范本。
2. **《Efficiently Reconstructing Dynamic Scenes One D4RT at a Time》**：用 "everything, everywhere, all at once" 钉死旧范式，讲从稠密解码到按需查询的范式转换。
3. **《CD-Buffer》**：一张交叉曲线图"看见"两派互补，再用统一的通道级 discrepancy metric 兑现。
4. **《Ov3R》**：双缺口收敛范本，一句 "unifies" 收敛，贡献、方法、实验呈总–分–分–总映射。
5. **《AToken》**：借 LLM 的统一能力建立信任，再反转指出视觉 tokenizer 碎片化，19% rFID 下降贯穿全文。
6. **《ComPose》**：oracle 实验和对朴素方案的反驳直接写进引言。
7. **《POLAR》**：先建立数据集优势，再指出数据集范式本身的天花板，引出模型方案，用 "chicken-and-egg" 收束两个贡献。
8. **《All in One》（LIDMark）**：把"统一"翻译成三个可验证的问题，先定评价标准再给方案。

### 6.6 常见失误与检查清单

**常见失误**
- 结论复述摘要：《Residual Diffusion Bridge Model》几乎逐句照抄；《MSPT》《GeniNav》《HR-NVC》结论与摘要或引言同构。
- Teaser 图悬挂：《CD-Buffer》《AToken》《MotionCrafter》《RnG》《POLAR》。
- 贡献与实验错位：《AeroGS》把 HSTD 和 Scale-Comp 合成一条；《SenCache》贡献 3、5 缺专门消融；《CFG-Ctrl》"统一"本身没有被实验量化；《UniPhys》数据集没做质量评测。
- 局限太抽象（《Drainage》）。
- 贡献条目注水：与标题重复（《MTU3D》）、前后重复（《RARE》）、只有定性描述（《Copernicus-FM》）、笔误（《M2SFormer》"that that"）。
- 引言与 Related Work 重复（《Unified Vector Floorplan Generation via Markup Representation》）。

**检查清单**（在 §3.8 基础上）
- [ ] 能用一句话说出被统一对象的共同根因
- [ ] 每个被批评的方法只配一个病症，并用 (i)(ii)(iii) 编号
- [ ] "统一"本身有映射表、推导或实验证明
- [ ] 额外实验已写进贡献列表
- [ ] 用词强度匹配证据；不是第一的地方收缩了主张
- [ ] 局限最多 2 条，写成"适用边界 + 方向"
- [ ] 名字与方法内核共振、不硬凑字母，副标题保留了可检索的任务描述

---

## 7. 发现-解释型（10.7%；CV 11.1%）

### 7.1 定义与识别特征

核心贡献是一个**被坐实的发现**（现象、根因、错误的隐含假设、机制），方法只是它"顺理成章的推论"，有时干脆没有方法。满足任意两条即适用：
- 能用受控实验或数学推导把"哪里不对"变成一条曲线或一个数字。例：《RALoc》"Yaw 超过 30° 后 recall 跌破 1%"。
- 发现反直觉，能写成一句话。例：《LitePT》SOTA 模型 67% 的参数其实是卷积。
- 能给发现起专名并全文复用：Gradient Entanglement、object recurrence prior。
- 方法的每个模块都能回指一条诊断结论。

判断标准：删掉方法，论文仍有独立价值（《Scaling Laws for Native Multimodal Models》《Mechanisms of Object Localization in VLMs》）；或删掉发现，方法就显得武断。

### 7.2 叙事骨架

**标准链**：领域重要性 → 现有范式或公认结论 → 具体瓶颈（量化）→ 排除肤浅归因 → 根因揭示并命名 → 核心洞察 → 对症的方法 → 分层证据 → 局限（可选，最多 2 条）→ 意义

| 变体 | 适用情况 | 代表 |
|---|---|---|
| 假设反驳式 | 对手方法有一条可明确指认的隐含假设 | 《CDAM》《Adaptive Low-Pass Guidance》 |
| 悖论钩子式 | 理论预期与实际表现之间有落差 | 《Selection-as-Nonlinearity》《Mechanisms of Object Localization》 |
| 共识反转式 | 领域有一个"大家都信"的结论 | 《When Pretty Isn't Useful》《Is Tracking really more challenging in First Person Egocentric Vision?》 |
| 排除法式 | 最直观的解释（如"数据不够"）需要先证伪 | 《Bokehlicious》；《ARGUS》两轮排除 |
| 两轮诊断-修复式 | 修复一个问题后暴露新问题 | 《GRPO-Guard》《Two Losses, One Goal》《When Confidence Fails》 |
| 揭秘重诠释式 | 能把旧方法解释成另一种已知范式 | 《Neighbor GRPO》《FlowEdit》 |
| 缺陷即资源式 | 公认缺陷在某些场景下反而有用 | 《FixTalk》《The Silent Assistant: NoiseQuery》 |
| 双问句并行式 | 机理和效率两个问题要一起回答 | 《AVGGT》（Q1/Q2）《When Understanding Becomes a Risk》（RQ1/RQ2） |
| 双线汇合式 | 两条此前被认为无关的文献线 | 《Is the Modality Gap a Bug or a Feature?》《Learning to See Through a Baby's Eyes》 |
| 结论前置式 | 纯实证研究，结论就是卖点 | 《Scaling Laws for Native Multimodal Models》《Generative Modeling of Weights》 |
| 涌现发现式 | 做 A 时意外发现 B 能力自然出现 | 《Video-GMAE》《UniPart》《StaMo》 |
| 受控平台式 | 没有单一发现，要逐个分解变量 | 《What Makes Good Synthetic Training Data for Zero-Shot Stereo Matching?》 |

### 7.3 逐步写法

**1. 立重要性**：领域定位句 + 缺口 + 具体数字。
- "KD has emerged as a pivotal technique for..."（《KDAS》）
- "Although these methods may help..., they do not sufficiently consider..."
- "it remains an open question whether..."（《Scaling Laws》）
- 落到应用后果：LumiMotion 写"无法用于 gaming/film making"；《Combinative Matching》一句话挂钩考古、医学影像、机器人、工业制造。也可以先认可共识再反转（《When Pretty Isn't Useful》）。

**2. 坐实瓶颈、下沉根因：亲自跑实验，不要只引用别人的局限。**
- 逐步引入干扰变量，观察指标单调变化（《CorrCLIP》Fig.2a/2b）。
- 自建指标：《EAGC》GDC/SOC；《Data Leakage Detection》实测 AICrowd 泄漏率 93.45%。
- 变量替换，把根因锁定到具体张量（《FixTalk》锁定到 f^d_4）。
- 数学推导：《When Confidence Fails》用泰勒展开。
- 排除法句式："Despite the superior quality of our dataset, we find that these models still lack sharpness..."（《Bokehlicious》）；"Ideally…However, our empirical analysis reveals…"（《GRPO-Guard》）

**3. 洞察出场：独立成句，引言第 3–5 段，与摘要同构。**
- "Our key insight is that..."（《Pluggable Pruning》）
- "We find a clear division of labour..."（《LitePT》）
- "they rely on a critical assumption…However, we argue that this assumption is flawed"（《CDAM》）
- "Yet we observe a striking gap"（《Selection-as-Nonlinearity》）
- "Interestingly, ..., we make an important discovery"（StaMo）
- "We argue that the issue is X rather than Y"
- **先给洞察，隔 1–2 句再揭晓方法名**（《CorrCLIP》《WSDT》《RALoc》）。激进设计用类比铺垫：《AVGGT》"aligning point clouds…needs only a few anchor points"；《CDAM》"in foggy weather, infrared images often contain more useful information"；《Combinative Matching》用榫卯类比。

**4. 证据：主实验 → 归因/机制实验 → 鲁棒性或自适应攻击**（《ARGUS》《D3》《BLiM》）。
- 从相关升级到因果：先观测再干预（《WSDT》Fig.3 → Fig.4；《ReME》用 GT 参考集做 oracle）。
- 给数字：相关系数（《PCR》r=0.836），"0.613 vs 0.300" 而不是"更高"。
- 跨底座复现（WSDT 在三个 SD 版本上）。

取名建议见 references/naming.md §6.2（发现-解释型）。

### 7.4 全文递进

- **方法**：问题驱动的求解链（LDP-Slicing 4.2→4.3），衔接句 "While X aims to…may still fall short…"。先直觉后公式；理论驱动型可以 Theorem → Proof sketch → Intuition（《AdaPrior》）。如果用模块罗列，每个模块要对应一条编号 Finding（《KDAS》4 个 Finding 映射到 2 个模块）。
- **实验**：实验小节标题复用贡献列表的措辞（引言里的贡献句不标章节号）；消融逐项累加（《Pluggable Pruning》Baseline→+LP→+DP→+WP）；纯实证论文用 "Summary of findings" 代替贡献列表（《Scaling Laws》），引言里的发现条目不括注图表。
- **局限与结论**：局限最多 2 条，写出发现成立的前提和后续方向（《GRPO-Guard》写明方法的作用边界及其根因）；失败案例可选，放补充材料即可（《Combinative Matching》Fig.9）。

### 7.5 代表论文

- **《CorrCLIP》**：先用悬念句提出"类间相关性到底是利是弊"，再用受控实验裁决。
- **《LitePT》**：先证伪 SOTA（67% 参数是卷积），再通过受控实验发现分工，方法名延迟到第 4 段。
- **《GRPO-Guard》**：两轮"诊断 → 修复"，用 "Ideally…However" 制造预期落差。
- **《Bokehlicious》**：自建高质量数据集后重跑 SOTA，问题依旧，排除"数据问题"，锁定"隐式学习范式"。
- **《ARGUS》**：两轮排除旧防御和 RepE，再用五个编号 Finding 层层建立"安全子空间"假设。
- **《FixTalk》**：把公认缺陷"身份泄露"反转为可利用的资源，直接驱动第二个模块的设计。
- **《Scaling Laws for Native Multimodal Models》**：结论前置，不起方法代号。
- **《The Invisible Gorilla Effect》**：借认知心理学命名统计偏差，用规模实证、反事实排除、机制解释三级证据支撑。

### 7.6 常见失误与检查清单

**常见失误**
- 结论只是摘要的同义改写（《KDAS》等六篇、《ViT3》《FedAdamom》）。
- 结论层层叠加限定语："potentially / could be / a hint"、"seems plausible...may"，读起来心虚（`references/anti_defensive.md` §4）。
- 贡献与消融颗粒度错位：《CSL》合并成一条贡献、消融拆成三项；《STAC》三条贡献对应四个组件。
- 贡献悬空：ASO 的 Mechanism Analysis、《AdaPrior》的收敛性只在附录验证。
- Figure 1 未被引用（《AVGGT》《STAC》《WSDT》）。
- 把复杂现象简化为单一根因却不承认这种简化；引言与方法大段重复（《A Unified Interpretation》）；贡献数前后不一（Bokehlicious threefold vs two）。

**检查清单**（在 §3.8 基础上）
- [ ] 瓶颈由自己的受控实验或推导坐实，并给出具体数字
- [ ] 最直观的替代解释已被实验排除
- [ ] 发现有专名，比方法名更早出场
- [ ] 方法名在洞察之后出场，每个模块都能回指一条诊断
- [ ] 至少有一处干预或因果实验，不止于相关性
- [ ] 贡献、实验小节、消融行三者颗粒度一致（对应关系用于规划，引言里不标章节号）
- [ ] 结论和局限没有层层叠加的限定语，也没有自我削弱词

---

## 8. 数据与基准型（7.0%；自动驾驶 10.4%）

### 8.1 定义与识别特征

主要贡献是一种**资源**（数据集、评测基准、仿真环境、标注协议），基线模型、诊断方法、配套 agent 只是辅助。故事是："领域卡在缺数据或缺统一评测上，我们找到了规模化获取标签或构造基准的办法。"满足任意两条即适用：
- 根本瓶颈是缺数据或缺评测协议，不是缺算法。
- 能用 Table 1 和已有数据集逐维度对比，本文是唯一全打勾的一行（EgoSound、RealAppliance、Derm1M）。
- 用现有模型在新基准上一测，就得到反直觉的负面结果（GEOBench-VLM 最好成绩只有 41.7%，只比随机猜测高一倍；RefAV 发现 VLM 失灵）。
- 标注来源本身有巧思，能讲成洞察：NitroGen 利用游戏主播为炫技叠加在画面上的手柄显示拿到动作标注。

### 8.2 叙事骨架

**主链**：领域重要性 → 现有数据或基准的具体瓶颈 → 根因（缺数据、缺协议、评测里有混淆变量）→ 核心洞察（怎样规模化获取标签或构造基准）→ 资源三件套（数据、标注或评测协议、基线）→ 分层证据 → 意义（开源，指出后续方向）

| 变体 | 适用情况 | 代表 |
|---|---|---|
| 双缺口并行 | 数据缺口和方法缺口都成立，分两段论证，各对应一条贡献 | EffectErase、EgoAVU、Derm1M |
| 双循环嵌套 | 资源和方法都是主贡献，引言把"背景→缺口→方案"走两遍 | OMG-Bench、CT-ScanGaze |
| 实测出新问题 | 先建基准测现有模型，负面结果变成第二个缺口，再引出方法或 agent | PanoEnv、GeoMMBench+GeoMMAgent |
| 漏斗式排除 | 近似工作多，先排除一类路线，再逐个拆最接近的工作 | CARD（5 段）、MIORe（连续 5 段点名 GoPro、KITTI 等） |
| 实证前置 | 问题是否存在有争议，先做小规模问卷或诊断 | AbstainEQA（50 人问卷）、3DReflecNet（48 组材质扫描） |
| 现象或场景驱动 | 任务新、文献少，从生活场景切入 | AlbumBench、SegEarth-R2、DENALI |
| 先给资源再自我戳破 | 已有数据集直接拿来用没效果 | RelayFlow-4K |
| 链式尝试 | 要证明简单补救不够 | VideoNet：基准表现差 → few-shot 补不了 → post-training 可以 |
| 范围声明 | 适用范围容易被误读 | 在基准设计处正面写清评测范围（测什么、在什么设定下测），不写成不足，也不放进引言；DENALI 的 "Scope of this Work" |

### 8.3 逐步写法

**1. 重要性：只用能核实的数字或场景。**
- 行业或流行病学数字："1.19 million deaths per year"（CARD）、"90% of global trade"（ENC-Bench）、"Waymo completing more than a million rides per week"（RefAV）。
- 场景代入："Imagine you are walking in a park..."（SegEarth-R2）；"Every time you take a photo, your phone shoots out a grid of lasers"（DENALI）。
- 跨学科背书：OddGridBench 借心理物理学的 just noticeable difference 和 pop-out 效应，先证明人能做到，再指出 MLLM 从没被测过。
- 说这项能力"被遗忘了"：VideoNet 引用 1992 年研究，称动作识别是 "forgotten task"。"不再被评测"比"做得差"更有紧迫感。

**2. 瓶颈和根因：点到具体对象，最好定量。**
- 点名："[X] only bridges the image modality"（BioVITA 评 TaxaBind）；RealAppliance 逐个点出 PartNet-Mobility、CheckManual、ArtVIP 的缺陷。
- 编号枚举："First, ... Second, ... Finally, ..."（SpatialScore、ChartCap）。
- Table 1 逐列打勾，一整列叉号比文字更有说服力。
- 受控诊断：EgoAVU 用 200 个片段测出 Qwen2.5-Omni 音频错误率 54.3%；3DReflecNet 把"光度一致性假设失效"量化为 5.82 dB PSNR 损失。
- 反问替读者发问："Do interaction-force predictors generalize to human videos?"（Hoi!）；"How do we know…"（ChartCap Fig.1）。
- 双层缺口：SceneBench 先说模型在长视频上失效，再指出现有基准把时间粒度和内容变化混在一起。

**3. 洞察：引言第 3–5 段，紧跟痛点句。**
- 标准句式："To address/bridge this gap, we introduce X, ..."
- 设问："We ask: what if VLMs were trained on data that rewards fine-grained visual understanding?"（Same or Not?）
- 目标枚举：RMIR 先列四条互相冲突的 desiderata，方法部分回指 "Our approach directly addresses the four desiderata from Section 1."
- 框架先行：RealAppliance 先搭 appearance / functionality / manual 三个维度，缺陷、对比表、任务都按这个顺序展开。
- 口号贯穿："to enable models that can hear, not just see"（EgoSound）；"See What We Cannot See"（GROC）在标题、摘要、结论反复出现。

**4. 证据。**
- 分层：零样本能力 → 迁移或微调收益 → 更难场景（NitroGen Fig.5–7）；RefAV 用五级 baseline 阶梯把分数从 13.3 推到 50.1。
- 多条独立证据线：RDFace 同时用 landmark 相似度、VLM 语义相似度、专家 Cohen's κ。
- 预先反驳：Same or Not? 用通用 VQA 和纯文本基准排除"对齐税"；FINER 加测 8 个幻觉基准和 6 个通用能力基准。
- 外部校准：PAI-Bench 用人类偏好 ELO 验证指标，Pearson r=0.918。
- 控制实验戳穿假提升：AbstainEQA 随机化视觉输入，证明 SFT 的提升是假的。
- 反直觉发现：图像复原后人眼看着更好，姿态估计却变差（EgoXtreme）。
- 用百分点报差值："improves by 10.54 and 7.85 percentage points"（RMIR）。

取名建议见 references/naming.md §6.2（数据与基准型）。

### 8.4 全文递进

- **方法组织**三种：模块罗列（纯资源论文最常用：SA-FARI 七步流水线、PAI-Bench 三条对称赛道、RDFace 4.1–4.5）；问题驱动的求解链（有新算法时："simply discarding low-confidence triplets is insufficient... To address this, ..."，RMIR 3.1.5）；混合结构（整体平铺，模块内部先动机后流程：NitroGen、OmniFood8K；先写 Overview 用 (1)(2)(3) 编号再展开：Real-IISR）。20 篇里有 14 篇方法部分几乎没有公式，靠流程图和伪代码。有训练目标或新指标时先直觉后公式："Intuitively, the router should place probability mass only on models that answer correctly..."（VL-RouterBench），公式后再用自然语言复述含义。
- **实验顺序**：先证明数据可信（人工核验一致性、R²）→ 证明基线或方法有效 → 消融。每条贡献一节或一张表：GeoMMBench 的 First/Second/Third 对应第 3/4/5 节；RealAppliance 5.2 节用五个问句做小标题；Wanderland 每节开头先写 A1/A2/A3 加粗结论句再摆证据。
- **局限与结论**：局限最多 2 条，写到数据集自身的覆盖范围（EgoXtreme：依赖 OptiTrack、只能在室内专用场地；Wanderland：采集频率 1 FPS、只建模静态环境，并给补救方向）；也可写成指南（WorldLens "Guidelines for Future World Model Design"）。结论首句可以呼应引言核心句（"We introduced GeoMMBench..."），但后面必须有新信息。

### 8.5 代表论文

- **NitroGen**：意外的数据来源（主播叠加的手柄显示）解决了动作标注贵的问题；三条贡献与摘要、正文小节严格三级对应。
- **RMIR**：先列四条冲突的 desiderata，方法逐条兑现，"目标枚举 → 逐一兑现"闭环范本。
- **RealAppliance**：开头搭好三维评价框架，缺陷、Table 1、实验任务都沿用。
- **AbstainEQA**（When Robots Should Say "I Don't Know"）：问卷证明问题存在 → 借 Norman 认知失误理论搭分类体系 → 控制实验证伪 SFT 的提升。
- **CARD**：五段漏斗式排除，逐步收窄到本文方案。
- **EgoSound**：一句口号贯穿全文，Table 1 一整列叉号直接证明缺口。
- **RefAV**：方法藏在五级 baseline 阶梯的最后一级，逐级上涨的分数讲完整个论证。

### 8.6 常见失误与检查清单

**常见失误**
- 贡献条数和实验对不上：MV-Fashion 5 条贡献只有 3 个实验小节；3DReflecNet 声称五项任务，两项推迟到补充材料。
- 贡献不透明地合并或重复：Real-IISR 把三个模块塞进一条；OccuFly 先叙述一遍方案又用列表重讲。
- Figure 1 引而不用：CARD、EgoSound、PAI-Bench。
- 提出竞争性假设却不去区分：PAI-Bench。
- 章节衔接跳跃：Real-IISR 在方法末尾突然插入数据采集。
- 拼写赶工：EgoAVU "soficsticated"、RDFace "dserves"。

**检查清单**（在 §3.8 基础上）
- [ ] Table 1 逐维度对比已有资源，本文是唯一全勾的一行
- [ ] 根因有诊断实验或受控实验的数字支撑
- [ ] 洞察句紧跟痛点句（"To address this gap, we introduce..."）
- [ ] 实验先证明数据可信，再证明方法有效，最后做消融
- [ ] 预先回应"过拟合新基准""牺牲通用能力"类质疑
- [ ] 局限（最多 2 条）写到数据集自身的覆盖范围（规模、标注者背景、采集条件），并给出补救方向
- [ ] 名字能读、能拆回全称；系列产出共享前缀；需要强调规模时把数字写进名字
- [ ] 摘要最后一句写明开源地址或发布计划

---

## 9. 能力扩展型（2.4%）

### 9.1 定义与识别特征

在一个**点名的前作或基座**上，把能力扩展到新模态、新维度（时间、视频、4D）或新场景（in-the-wild、物理约束）。识别信号：
- 能写出 "we extend X by Y"，X 是唯一或最相关的前作：Anatomica 点名 Kadry et al.[30]、4D Primitive-Mâché 点名 SuperPrimitive、PhysNAP 点名 NAP、STARFlow-V 点名 STARFlow。
- 方法名天然是"方向前缀 + 基座名"：OmniVGGT、PET-DINO、WildRayZer、OmniSAM。
- 新能力可能难以量化，需要定性图或视频补强（4D Primitive-Mâché 的 object permanence）。

### 9.2 叙事骨架

**标准链**：背景重要性 → 现有方法现状 → 具体瓶颈（常编号）→ 瓶颈根因 → 核心洞察 → 方法（与瓶颈一一对应）→ 证据（与贡献一一对应）→ 意义、首尾呼应

| 变体 | 适用情况 | 代表 |
|---|---|---|
| 前作继承定位式（本类最典型） | 有唯一或最相关的前作，用 "we extend X by Y" 占据研究空间 | Anatomica、4D Primitive-Mâché、PhysNAP、STARFlow-V |
| 双层缺口式 | gap 可拆成"操作层面"和"能力 / 范式层面"两层 | AutoOcc、HouseCrafter（两轮文献漏斗）、MEDIC-AD（RQ1–3 并列子故事） |
| 反问句钩子式 | 用 "Can we...?" 做从问题到方案的枢纽 | OmniSAM、FoleyDirector、WildRayZer（"First.../Second..." 反问） |
| 发现驱动 / 转折句式 | 不摆 gap，直接给视角转折 | Geo4D "we suggest starting instead from..."；《Visual Diffusion Models are Geometric Solvers》"we take a different perspective" |
| 模板化重复 | 多个并列案例共享同一方法 | 《Visual Diffusion Models are Geometric Solvers》三个 NP-hard 问题共享同一 U-Net 和叙事模板 |

### 9.3 逐步写法

**1. 重要性**
- 应用场景枚举，逐个配引用（Anatomica）。
- 可比数字制造反差：AutoOcc "4k+ human hours"；HumanNOVA "800K vs a few thousand"。
- 历史地位或权威赛事背书："first posed in 1911"、"CG:SHOP 2019"（《Visual Diffusion Models are Geometric Solvers》）。
- 用具体失败案例图代替空泛断言，放进首页的 Figure 1（FEAT 用失败案例图说明问题）。

**2. 瓶颈与根因**
- 编号拆解 (I)(II) / (i)(ii)（LEGION、PET-DINO）。
- 点名前作原句指认局限："was limited to globally defined..."（Anatomica 对 Kadry et al.[30]）。
- 根因落到机制：OmniVGGT 指出深度是稠密逐像素的局部线索，位姿是全局属性，两者性质不同。

**3. 洞察**
- 跨领域类比："This multiplicity naturally forms a distribution, which makes the problem especially well suited to diffusion models"
- 反直觉转折："Here, we suggest starting instead from..."（Geo4D）
- 与最近工作精确对比："unlike their method, which..., we..."

**4. 证据**
- 客观指标 + 用户研究 + 效率对比三重链（CoordSpeaker、FEAT）。
- 链式消融，每加一个模块给数字（FoleyDirector Tab.3：①Base → ②+STS → ③+RoPE → ④+Bi-Frame）。
- 难量化的能力用定性图 + 呼吁看视频补强（4D Primitive-Mâché）。

取名建议见 references/naming.md §6.2（能力扩展型）。

### 9.4 全文递进

- **方法**：几乎全部是问题驱动的求解链，先一句自然语言讲动机再给编号公式。
- **实验**：方法小节标题与实验小节标题同构，形成"方法-实验镜像"（PET-DINO "3.2 AFVPG" ↔ "4.6 Table5"；HouseCrafter "3.2 Floorplan-guided..." ↔ "4.3 Ablation"）。
- **局限与结论**：局限最多 2 条，克制而具体（Anatomica 两点；STARFlow-V "(1) Latency (2) Data quality" 各配 future work）。

### 9.5 代表论文

- **《Anatomica》**：教科书式"前作定位"，整段引用并反驳 Kadry et al.[30] "was limited to globally defined..."，方法就是对这个局限的精确延伸。
- **《FoleyDirector》**：隐喻钩子 + 反问句 + 链式消融；把用户包装成"Foley 导演"，Fig.1 对话气泡具象化问题，消融表逐组件给 F1 提升。
- **《Visual Diffusion Models are Geometric Solvers》**：反差标题 + 三案例模板，用历史权威（1911 年提出、CG:SHOP 赛事）撑住重要性。
- **《Chorus》**：命名与方法内核合一，"意外发现 → 假设 → 验证"闭环（3DGS 预训练在点云任务上意外有效）。
- **《4D Primitive-Mâché》**：诗意命名 + 前作继承 + 新能力首创；先命名再溯源（SuperPrimitive），难量化的 object permanence 用定性图和视频补强。

### 9.6 常见失误与检查清单

**常见失误**
- 贡献列表与组件或实验粒度不对齐：FoleyDirector 把 3 个组件压成 1 条贡献；MEDIC-AD 贡献按框架 / 机制 / 评测横切，RQ 按三种能力纵切，二者只部分对应。
- Figure 1 未被引用：FEAT、OmniVGGT、Chorus、4D Primitive-Mâché、PET-DINO。
- 叙事顺序与写作顺序错位：HumanNOVA 引言"先数据后模型"，方法正文"先模型后数据"；实验预告顺序（Setup→Comparison→Ablation）与实际顺序（Setup→Ablation→Comparison）不一致。
- 软性收尾冲淡结论：PET-DINO "We hope this work can provide new insights..."、LEGION 呼吁式收尾。

**检查清单**（在 §3.8 基础上）
- [ ] 点名了被扩展的前作或基座，并引用它自己的局限原句
- [ ] 用一句 "we extend X by Y" 或 "unlike their method, which..., we..." 定位
- [ ] 根因落到机制（如"局部线索 vs 全局属性"）
- [ ] 方法小节标题与实验小节标题同构
- [ ] 每个组件一条贡献，不压缩
- [ ] 引言的讲述顺序与方法、实验的实际顺序一致
- [ ] 难量化的新能力有定性图或视频补强
- [ ] 名字是"方向前缀 + 基座名"或与引言钩子互文的隐喻

---

## 10. 效率优化型（2.0%）

### 10.1 定义与识别特征

在保持质量的前提下，大幅降低时间、内存或 token 开销。最有力的卖点是**打破"效率与能力二选一"**（《Sparse-LaViDa》：Block Diffusion 牺牲双向上下文换速度，本文证明二者可兼得）。

与瓶颈突破型的边界：如果能说清"为什么慢"的机制根因，并且方案对症，更推荐写成瓶颈突破型（《FastGS》《FlashVDM》）。本类适用于：效率本身就是全部故事，或者核心是把已有加速工具迁移到新架构或新模态时的"错配"。

### 10.2 叙事骨架

**主链**：领域重要性 → 现有方法瓶颈 → 瓶颈根因 → 核心洞察 → 方法设计 → 多维证据 → 局限（可选，最多 2 条）→ 意义

| 变体 | 做法 | 代表 |
|---|---|---|
| 总-分-总 | 先编号列瓶颈 (i)(ii)(iii)，逐条展开，再给对应解法 | DeltaTok |
| 双设问链 | 先问"要不要变"，再问"怎么变" | DDiT："should every step be the same?" → "how to determine optimal patch size?" |
| 发现驱动 + 两级缺口 | 先给大缺口，再给已有工具用到新领域时暴露的具体挑战 | VMonarch（稀疏 / 线性两类局限 → MonarchAttention 用于视频的 3 个挑战）；ScoreLiDAR（图像蒸馏技术未验证适用 LiDAR） |
| 先朴素基线再改进 | 暴露基线的代价后升级 | Test-Time Prompt Tuning（先微调 → 轻量视觉提示）；AdaptVision（vanilla GRPO 暴露问题 → DTPO） |
| 跨学科类比迁移 | 认知科学或生物学类比单独成段作为洞察来源 | LLMind（中央凹视觉）、AdaptVision（主动视觉） |

### 10.3 逐步写法

**1. 重要性：用具体开销数字。**
- "a 2048×1024 image yields 2,678 vision tokens"（AdaptVision）
- "30 minutes for a 5s video"（Talking Portrait / TurboVSR）
- "8GB at FullHD, 25+GB at WQHD"（MEMFOF）
- 配一句让步式反差："linear-time complexity does not directly translate to fast inference"（TE-VMamba）

**2. 瓶颈与根因**
- 编号 (i)(ii)(iii) 把"低效"拆成可验证的原因（DeltaTok）。
- "错配"框架：方法为 A 架构设计，搬到 B 架构上产生具体冲突。TE-VMamba：ViT 剪枝法破坏 SSM 的方向性和递归结构；ScoreLiDAR：图像加速技术未验证 LiDAR 几何结构。

**3. 洞察**：先给一句朴素直觉，单独成句，用 "Our key insight / We observe that..." 标出，方法部分再给数学形式化。
- "consecutive frames differ only in structured, low-dimensional ways"（DeltaTok）
- 21 篇几乎全部是"先直觉后公式"。

**4. 证据**
- 逐步消融复现构建过程（DeltaTok 的 Step0→3）。
- 多维交叉验证：速度、质量、内存、用户研究一起报（TurboVSR：DOVER + MUSIQ + user study + 4K 案例）。

取名建议见 references/naming.md §6.2（效率优化型）。

### 10.4 全文递进

- **方法**：几乎全部是问题驱动的求解链，每小节先指出上一步遗留的新问题再给解法，段尾常点明局限为下一节铺垫（Turbo-GS 3.1→3.2→3.3；LinVideo selective transfer → ADM）。少数先给统一优化目标再拆子设计（LLMind：Eq.1 总目标 → BASS + CSF）。
- **实验**：贡献逐条对应实验小节或消融表，句式模板 "We propose/introduce X, a Y that Z"；消融表命名复用方法小节标题（EDM Table 7 分 (a)(b)(c)(d) 对应四条贡献）。
- **局限与结论**：局限最多 2 条，绑定到设计假设：推荐像 AdaptVision 那样写明"单一工具 / 固定 1/4 分辨率 / 两轮"，或像 Sparse-LaViDa 写明"需要额外训练"；ScoreLiDAR、Turbo-GS 给出了针对性、不夸大的局限。只写 "we leave this for future work"、不说边界在哪（SwiftTailor、TurboVSR）不推荐。

### 10.5 代表论文

- **《DeltaTok / DeltaWorld》**：(i)(ii)(iii) 拆瓶颈 → 连续三段逐条展开 → "总-分-总"给方案，消融用同一张表逐步复现构建过程。
- **《DDiT》**：两层递进设问（要不要同等精细？怎么决定？）代替直接抛方案。
- **《TE-VMamba》**：一句反直觉转折（线性复杂度 ≠ 低延迟）开篇，"错配"框架定位根因。
- **《LLMind》**：整段跨学科类比（人眼中央凹）前置到引言正文，而不是留给 Related Work。
- **《Sparse-LaViDa》**：把"效率"与"能力保留"塑造成此前互斥的两个目标，核心贡献是证明二者可兼得。

### 10.6 常见失误与检查清单

**常见失误**
- 贡献与根因未一一对应，需要读者自己梳理（DeltaTok 三条根因对两条贡献）。
- 图文数字不一致，引言复述的数字与 Figure 标注错位（Sparse-LaViDa 在编辑、数学推理两项）。
- 拼写瑕疵（TurboVSR 结尾 "ratio" 误写 "ration"）。
- Figure 1 未被引用（TE-VMamba、SwiftTailor、LinVideo）。

**检查清单**（在 §3.8 基础上）
- [ ] 重要性段落给出了具体开销数字（token 数、分钟、GB）
- [ ] 有一句打破默认预期的反差句，或把效率与能力塑造成二元对立
- [ ] 根因用编号拆解或"错配"框架说清
- [ ] 每条根因都有对应的贡献
- [ ] 证据同时覆盖速度、质量、内存，必要时加用户研究
- [ ] 报告了至少一处质量下降或优势衰减的场景
- [ ] 引言、Figure、表格中的加速比和质量数字一致
- [ ] 名字体现提速意象（Turbo- / Swift- / Delta-）或借用核心数学工具

---

## 11. 理论分析型（0.2%，仅 2 篇，规律仅供参考）

### 11.1 定义与识别特征

用定理、穷尽分类或形式证明，把领域里靠经验的做法升级为可证明的结论，实验只用来验证理论。两种形态：
- **理论上界 → 替换公式**：《C²FG》指出 CFG 的六种改进都是 heuristic，用四个定理把直觉锻造成指数衰减上界，再给出新公式。
- **穷尽分类 + 证明方法升级**：《PLMP》对未标定相机的 point-line minimal problems 做系统分类，把以往只能靠"强数值证据"判断的非最小性，升级为可形式证明的代数命题。

### 11.2 叙事骨架

**主链**：领域基石的重要性 → 现有方案是 heuristic 或不完整的 → 揭示被忽视的根因或缺口 → 理论洞察登场（定理 / 命题）→ 把洞察转成可操作的方法 → 多维度系统实验 → 意义与应用延伸

| 变体 | 结构 | 代表 |
|---|---|---|
| 单贡献线性链 | CFG 重要 → 六种改进都是 heuristic → "overlook a fundamental aspect" → Theorem 1–4 → 方法 → 实验 | 《C²FG》 |
| 双贡献并列 | 背景 → 缺口 → 贡献 1（完整分类）→ 贡献 2（形式化证明方法）→ 应用场景 | 《PLMP》（原文还在引言里写了局限声明和辩护，本 skill 不采用，局限放在结论之前） |

### 11.3 逐步写法

**1. 重要性：把研究对象和"大家都在用的地基"挂钩。**
- "X is a cornerstone of modern Y"（《C²FG》："CFG is a cornerstone of modern conditional diffusion models"）
- "a large number of X has to be solved in this scheme"（《PLMP》把 minimal problem 与 RANSAC 挂钩）

**2. 瓶颈与根因**
- 批判路线：先密集罗列同类改进制造"都在打补丁"的感觉（《C²FG》一口气列出 Interval Guidance、FDG、CFG++、TFG、β-CFG、RAAG），再一句话点破共因："largely heuristic and motivated by empirical observations rather than rigorous theory"、"overlook a fundamental aspect of CFG's design"。
- 覆盖空白路线：《PLMP》"已有完整分类只覆盖标定相机，未标定情形更常见，却无人系统枚举"。

**3. 洞察**：引言先用自然语言点出结论（"the difference...is strictly monotonically decreasing"）；方法部分先直觉后公式——《PLMP》用 Example 4.8 的具体 8-camera 案例手把手演示，再抽象为 Definition 4.7 / Proposition 4.9；《C²FG》用 "Intuitive Motivation" 段落先讲道理，再给公式 (14)。

**4. 证据**
- 数字具体、可核验（《PLMP》：291、73、285、434、149、130/19）。
- 用独立方法交叉验证（monodromy + Gröbner 基）。
- 覆盖面拉满，并专挑强基线：《C²FG》五种骨架 × 四个数据集 × 两类采样器，专挑 "already difficult to improve" 的 SiT-XL/2 (REPA)。
- 证明覆盖的范围写清楚、不夸大（《PLMP》对 19 个问题写明 "we study their equations explicitely after eliminating variables"）。

取名建议见 references/naming.md §6.2（理论分析型）。

### 11.4 全文递进

- **方法**：问题驱动的求解链。《PLMP》：先证必要条件 balanced（Sec.3）→ Jacobian 检验筛 minimal（Sec.4.1–4.2）→ stabilizer 理论证非最小（Sec.4.3）→ 计算 degree（Sec.5）；并在上一节末尾预告路线图（"Section 3 classifies...Section 4 determines...Section 5 computes..."）。
- **实验**：逐条对应贡献。《C²FG》的 Toy Example / Table 1 对应 "SOTA performance"，Table 3（多采样步数、SDE/ODE）对应 "versatility"，SiT-XL/2 (REPA) + interval guidance 的结果专门对应 "orthogonal design enhances even exceptionally strong baselines"。
- **局限与结论**：定理成立的条件在定理处写明（《C²FG》在 3.1 节末尾说明 "the theoretical bounds...become singular as t→0...we simply disregard this regime"）；局限最多 2 条，一句话点出适用区间和后续方向，放在结论之前，不前置到引言。结论可以极短、逐字呼应引言和贡献措辞（《C²FG》仅 5 句、不含数字），也可以再点一次未来方向（《PLMP》的 partial visibility）。

### 11.5 代表论文

- **《C²FG: Control Classifier-Free Guidance via Score Discrepancy Analysis》**：用"CFG 是基石却纯凭经验"的反差做钩子，四个定理把定性直觉锻造成指数衰减上界，再用五骨架四数据集两采样器验证。"理论上界 → 替换公式"的范本。
- **《PLMP – Point-Line Minimal Problems for Projective SfM》**：用"7 点在 3 条线上、任意多视角都能唯一线性重建"这一反直觉结果做钩子，把非最小性判断从数值证据升级为形式证明。"穷尽分类 + 证明方法升级"的代表。

### 11.6 常见失误与检查清单

**常见失误**（从两篇笔记中提炼出的隐患）
- 贡献长度不均衡：《C²FG》三条贡献里"实验"一条堆了 SOTA、versatility、strong baseline、FID gains 四层信息，引言正文却缺少同等篇幅的铺垫，显得是临时补上的。
- Teaser 图错位：《C²FG》的 Figure 1 是理论验证曲线（MSE / 余弦相似度），真正的流程示意图 Figure 2 不在第一页，也没被引言引用。

**检查清单**（在 §3.8 基础上）
- [ ] 重要性句把研究对象挂到"地基"上（cornerstone / 被大量调用）
- [ ] 罗列了同类改进并一句话点破共因（heuristic / overlook），或清楚说明覆盖空白
- [ ] 每个定理或命题前有具体例子或 Intuitive Motivation 段落
- [ ] 关键结论有独立方法交叉验证
- [ ] 实验专挑最强、最难提升的基线
- [ ] 定理成立的条件在定理处写明；局限不前置到引言
- [ ] 贡献条目篇幅均衡，每条在引言正文都有铺垫
- [ ] 简称 4–5 个字符、能独立读出，保留被改进对象的词根
