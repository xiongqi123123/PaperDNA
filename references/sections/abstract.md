# 顶会论文摘要写法规范

> 数据来源：1040 篇 CVPR 2026 + ICCV 2025（best / oral / highlight）精读笔记。
> 标注 **[stats]** 的数字直接取自 `references/corpus_stats.md`；标注 **[重算]** 的数字是按同一批 1040 篇笔记里的"摘要逐句分析"原句重新统计的（例如词频、方法名出现在第几句）；其余结论出自 5 份分批归纳材料，每条后面附论文标题作为证据。
> 用法：写摘要时先看第 0 节的默认配置，再按第 1 节选骨架、第 2 节逐句填写、第 3 节核对细节，最后按第 5 节检查清单逐条自查。给方法取名见 references/naming.md。跨章节的写作原则和去 AI 味规则见 `references/word_style.md` 第 1 节和第 4 节，本文的模板也要遵守。

---

## 0. 默认配置（没有特殊理由时照此写）

| 项 | 默认值 | 依据 |
|---|---|---|
| 句数 | 8 句（可接受 7–9） | 中位数 8，四分位 [7, 9] [stats] |
| 平均句长 | 约 22 个英文词 | [重算] |
| 骨架 | 背景 → 问题/缺口 → 方法 → 设计细节 → 结果 → 资源发布 | 合并后最常见的骨架 [重算]，与第 1.4 节一致 |
| 首句 | 纯背景句，或"背景 + 问题"合句 | 背景 56.6%，背景+问题 21.2% [stats] |
| 方法名出现位置 | 第 3–4 句 | 第 3 句 27.5%，第 4 句 23.9% [重算] |
| 方法句写法 | `To address this, we propose [Name], a [category] that [mechanism].` | propose / introduce / present 三个动词覆盖约九成论文 [重算] |
| 数字 | 0–2 个，只放在结果句 | 76% 的摘要不含任何百分比或倍数 [重算] |
| 引用编号 [n] | 不写 | 仅 1.4% 的摘要出现 [重算] |
| 末句 | 有开源就写一句极短的资源句（约 6 个词）；没有开源就写结果+意义句 | 资源发布 43.1%，结果+意义 17.9% [stats] |

---

## 1. 摘要的标准结构

### 1.1 句数

- 中位数 **8**，四分位 **[7, 8, 9]**，最少 3 句，最多 15 句 [stats]。
- 分布：8 句 25.2%，7 句 19.8%，9 句 18.2%，6 句 11.9%，10 句 11.4%，5 句 5.3%，11 句 5.1%，12 句及以上不到 2% [stats]。**6–10 句合计 86.5%**。
- 按故事类型分，数据与基准型的中位数是 9 句（要多写规模和协议），其他类型都是 8 句 [重算]。
- 结论：写成 7–9 句。少于 6 句就是"方法直切式"（如 NitroGen 只有 5 句），这时每句都要高密度；超过 10 句通常说明设计细节写多了，应当删减。

### 1.2 各位置的作用分布（把摘要等分为 5 段）[stats]

| 位置 | 前三名作用 | 写作含义 |
|---|---|---|
| 第 1/5 段 | 背景 57%，问题 18%，缺口 11% | 开头只立场景和痛点，不讲方法 |
| 第 2/5 段 | 方法 44%，缺口 18%，设计细节 11% | 最迟在这一段亮出方法 |
| 第 3/5 段 | 方法 38%，设计细节 35%，洞察 8% | 讲清方法怎么做、为什么有效 |
| 第 4/5 段 | 结果 40%，方法 23%，设计细节 20% | 开始转向证据 |
| 第 5/5 段 | 结果 42%，资源发布 37%，意义 12% | 用结果 / 资源 / 意义收尾 |

也就是说，**前 1/5 讲问题，中间 3/5 讲方法，最后 1/5 讲证据**。方法类内容（方法、设计细节、洞察）占整篇摘要的一半左右。

### 1.3 首句与末句 [stats]

**首句作用**：背景 56.6%，背景+问题 21.2%，背景+缺口 7.3%，方法 6.6%，背景+方法 1.7%，背景+问题+缺口 1.4%，背景+意义 1.2%。**含背景的首句合计 90.0%**。

**末句作用**：资源发布 43.1%，结果+意义 17.9%，结果 12.0%，意义 10.4%，结果+泛化 6.1%，泛化+意义 3.8%，结果+泛化+意义 2.8%，意义+资源发布 1.1%。

**首句之后接什么**（936 篇以背景开头的摘要中）[重算]：第 2 个作用是问题的占 44%（415 篇），缺口 33%（312 篇），方法 17%（155 篇），根因 3%，洞察 2%。

### 1.4 最常见的作用序列

**原始序列极其分散**：取每句主作用、合并相邻重复后，1040 篇摘要一共有 656 种不同序列，排第一的也只占 2.5% [stats]。前几名是：

| 序列 | 篇数 | 占比 |
|---|---|---|
| 背景 → 缺口 → 方法 → 设计细节 → 结果 | 26 | 2.5% |
| 背景 → 问题 → 方法 → 设计细节 → 结果 | 22 | 2.1% |
| 背景 → 问题 → 方法 → 设计细节 → 结果 → 资源发布 | 20 | 1.9% |
| 背景 → 缺口 → 方法 → 设计细节 → 结果 → 资源发布 | 18 | 1.7% |
| 背景 → 问题 → 方法 → 结果 | 13 | 1.2% |
| 背景 → 问题 → 方法 → 设计细节 → 方法 → 结果 → 资源发布 | 12 | 1.2% |
| 背景 → 问题 → 缺口 → 方法 → 设计细节 → 结果 | 12 | 1.2% |

**合并后的骨架**（把问题和缺口视为一类、去掉设计细节，再合并相邻重复）[重算]：

| 骨架 | 占比 |
|---|---|
| 背景 → 问题/缺口 → 方法 → 结果 | 11.2% |
| 背景 → 问题/缺口 → 方法 → 结果 → 资源发布 | 9.2% |
| 背景 → 方法 → 结果 → 资源发布 | 2.9% |
| 背景 → 问题/缺口 → 方法 → 结果 → 意义 | 2.9% |
| 背景 → 问题/缺口 → 方法 → 结果 → 意义 → 资源发布 | 2.2% |
| 背景 → 问题/缺口 → 洞察 → 方法 → 结果 | 2.0% |
| 背景 → 方法 → 结果 | 2.0% |
| 背景 → 问题/缺口 → 根因 → 方法 → 结果 → 资源发布 | 1.4% |

**各作用的出现率**（一篇摘要里至少出现一次该主作用）[重算，基于 stats 序列表]：

| 作用 | 出现率 | 说明 |
|---|---|---|
| 结果 | 96.2% | 几乎必写 |
| 背景（作为首句） | 90.0% | 几乎必写 |
| 问题或缺口 | 79.6% | 问题 46.7%，缺口 49.7% |
| 设计细节 | 64.6% | 大多数会写 |
| 资源发布 | 45.6% | 有开源就写 |
| 方法出现两次及以上 | 38.7% | 即"方法 → 设计细节/洞察 → 方法"式地多次回到方法 |
| 洞察 | 28.1% | 在方法之前出现 10.2%，在方法之后出现 17.0% |
| 意义 | 24.5% | |
| 根因 | 17.1% | |
| 泛化 | 13.3% | |

**结论**：固定的只有"背景开头、问题/缺口居前、方法居中、结果居后"这条主干；洞察、根因、泛化、意义都是**可选插件**，按故事类型决定加不加。

### 1.5 八种排列模式（按需选一种）

| 模式 | 序列 | 适用 | 证据 |
|---|---|---|---|
| ① 标准漏斗式 | 背景 → 问题 → 缺口/根因 → 方法 → 设计细节 → 结果 → 意义/资源 | 瓶颈突破型，最常见 | 《ChordEdit》《CFG-Ctrl》《Gated KalmaNet》《FedSDR》《Similarity-as-Evidence》《DK-DDIL》《HiLoRA》 |
| ② 方法直切式 | 方法 → 设计细节 → 结果 → 资源 | 方法本身辨识度高，或是系统/基础模型 | 《D4RT》《SAM 3D》《CUPID》《Fresco》《NitroGen》《TokenSplat》《MeshLLM》 |
| ③ 发现-解释式 | 背景 → 缺口 → We observe/find → 洞察 → 方法 → 结果 | 反直觉发现型 | 《AVGGT》《Mind the Gap》《ARGUS》《StaMo》《The Invisible Gorilla Effect》 |
| ④ 枚举配平式 | "N 个局限"(1)/(2) ↔ "N 个设计" First/Second | 缺陷与设计一一对应 | 《CADC》《MHC-DUN》《TeHOR》《SpatialTree》《LoftUp》《GS-MoE》 |
| ⑤ 数据/基准堆叠式 | 重要性 → 缺口 → 资源命名 → 规模数字 → 协议 → 评测揭示差距 → 开源 | 数据与基准型 | 《CARD》《CHIRP》《VL-RouterBench》《UDC-VIT》《SceneScribe-1M》 |
| ⑥ 新任务命名式 | 下定义 → 新场景问题 → "a phenomenon we term X" → 方法 | 新问题定义型 | 《AsymLoc》《FedHarmony》《GlyphPrinter》《URICA》 |
| ⑦ 实证先行式 | 先用小规模调查数字证明问题真实存在 → 方法 | 需要先说服读者"问题存在" | 《When Robots Should Say "I Don't Know"》 |
| ⑧ 链式递进式 | 方法1 → 副作用 → 方法2 → 新缺口 → 方法3 | 多个贡献互相催生 | 《GaitMax》《Rethinking Dataset Distillation》 |

### 1.6 按故事类型的变体

故事类型分布 [stats]：瓶颈突破型 56.0%，新问题定义型 11.0%，统一框架型 10.8%，发现-解释型 10.7%，数据与基准型 7.0%，能力扩展型 2.4%，效率优化型 2.0%，理论分析型 0.2%。在 oral / best 中的比例与此基本一致（oral 里瓶颈突破型占 57.9%）。

各类型的摘要特征 [重算；"含洞察/根因"包括复合作用标签，如"问题+根因"]：

| 故事类型 | 篇数 | 首句即方法 | 含洞察 | 含根因 | 含 %/× 数字 | 末句含资源 | 末句含意义 |
|---|---|---|---|---|---|---|---|
| 瓶颈突破型 | 582 | 10% | 29% | 47% | 23% | 45% | 34% |
| 新问题定义型 | 114 | 7% | 38% | 32% | 18% | 39% | 37% |
| 统一框架型 | 112 | 11% | 31% | 34% | 22% | 44% | 42% |
| 发现-解释型 | 111 | 5% | **63%** | **50%** | 26% | 43% | 40% |
| 数据与基准型 | 73 | 7% | 21% | 36% | 26% | **67%** | 41% |
| 能力扩展型 | 25 | 12% | 16% | 20% | 12% | 32% | 40% |
| 效率优化型 | 21 | 0% | 38% | 29% | **62%** | 33% | 43% |

按类型写作的推荐骨架：

- **瓶颈突破型**：背景 → 问题（However…）→ 根因（This stems from…）→ 方法（To address this, we propose X…）→ 设计细节 ×1–2 → 结果 → 资源。近一半论文会写根因，这是这一类最有说服力的一句。范例：《ChordEdit》。
- **发现-解释型**：背景 → 缺口 → **分析动作**（we analyze / we perform a scalability analysis）→ **发现**（Our observations reveal that…）→ Based on these insights, we propose X → 结果 → 资源。63% 含洞察句，这是它和其他类型最明显的区别。可以先"假设"再"发现"：《ARGUS》用 "we hypothesize that…" → "Through extensive experiments, we discover that…" → "However, we also found that…"（根因）→ "To address this, we propose ARGUS"。范例：《Mind the Gap》《Rethinking Dataset Distillation》。
- **新问题定义型**：背景 → 现有设定的隐藏假设 → **新任务/新现象命名**（a phenomenon we term X / we redefine X as Y）→ 方法 → 结果。证据：《FedHarmony》"a phenomenon we term label correlation drift"，《URICA》"we redefine WSI retrieval as a semantically optimal matching problem"。
- **统一框架型**：背景 → 两条路线镜像批判（Existing methods either A or B）→ 统一方法 → 多任务结果 → 泛化。名字常带 Omni- / Uni-（见 references/naming.md）。末句含意义的比例最高（42%）。证据：《UniPart》《OminiControl》《AToken》。
- **数据与基准型**：重要性 → 资源缺口（no dataset contains… / A significant gap remains in providing a unified resource that…）→ 资源名 + 规模数字 → 采集/协议 → 评测揭示现有模型的差距 → 开源。**67% 以资源句收尾**；数字用规模而非精度。证据：《UDC-VIT》《SceneScribe-1M》《VS-Bench》《PAI-Bench》。
- **效率优化型**：**62% 含数字**，必须给倍数或百分比（"up to 3.52× … speedup"），并用 "without compromising / while maintaining" 交代质量没有下降。证据：《DDiT》《Proxy-GS》。
- **能力扩展型**：泛化出现率最高（52%），结尾用"exhibits competence across diverse domains, including A, B, C"一类列举句展示能力广度。证据：《NitroGen》。

---

## 2. 逐句写法（按作用）

每一节都包含：这句要完成什么 → 常见写法 → 句式模板（附原句和出处）→ 注意事项。原句照抄自论文摘要。

### 2.1 背景（Background）

**要完成什么**：用一句话立起领域或技术，并给出价值判断，为下一句的转折埋伏笔。**不带引用**，不讲历史。

**常见写法**：① 领域价值判断句（X is crucial for Y）；② 近期进展句（Recent advances in X have enabled Y）；③ 先扬后抑的让步句（X have achieved…, but/yet…），这种写法把背景和问题合成一句，占首句的 21.2% [stats]。首句最常见的两个开头词组是 "We present"（46 篇）和 "Recent advances"（28 篇）[重算]。

**模板**：

1. `Recent advances in [X] have [enabled / led to remarkable progress in] [Y].`
   - 原句："Recent advances in video generation have shown remarkable potential for constructing world simulators." —《ProPhy》
2. `[X] has become a [critical / crucial] [mechanism / technique] for [Y], with [evidence of adoption].`
   - 原句："Invisible watermarking has become a critical mechanism for authenticating AI-generated image content, with major platforms deploying watermarking schemes at scale." —《RAVEN》
3. `[X] remains a [formidable / long-standing / fundamental yet challenging] challenge in [field], [as / largely due to] [reason].`
   - 原句："Long-tailed image classification remains a long-standing challenge, as real-world data typically follow highly imbalanced distributions where a few head classes dominate and many tail classes contain only limited samples." —《Confusion-Aware Spectral Regularizer》
4. `[X] is [crucial / essential / fundamental] for [Y], enabling [Z].`
   - 原句："Long video understanding is essential for human-like intelligence, enabling coherent perception and reasoning over extended temporal contexts." —《Thinking with Drafts》
5. `The advent of [X] offers / has amplified [Y].`
   - 原句："The advent of one-step text-to-image (T2I) models offers unprecedented synthesis speed." —《ChordEdit》
6. `[X] have achieved [remarkable / impressive] [success / performance] in [Y], but / yet [limitation].`（背景+问题合句）
   - 原句："Vision-Language Models (VLMs) have achieved remarkable success in visual question answering tasks, but their reliance on large numbers of visual tokens introduces significant computational overhead." —《AdaptVision》
7. `[X] enables [capability] but suffers from / faces [problem].`（背景+问题合句）
   - 原句："Remote photoplethysmography (rPPG) measurement enables non-contact physiological monitoring but suffers from accuracy degradation under head motion and illumination changes." —《PHASE-Net》
8. `Despite [recent success of X], [Y] [remains limited / lags far behind].`（背景+缺口合句）
   - 原句："Despite advances in Multimodal LLMs (MLLMs), their ability to reason over 3D structures and temporal dynamics remains limited, constrained by weak 4D perception and temporal understanding." —《4D-RGPT》
9. `[Task] aims to enable [models] to [A] while [B].`（任务定义句）
   - 原句："Continual learning aims to enable models to learn sequentially from continuously incoming data while retaining performance on previously learned tasks." —《Mind the Gap》

**注意**：
- 背景只写 1 句，最多 2 句（第 2 句用来引出具体技术对象，如《Mind the Gap》第 2 句引出 CLIP）。
- 首句中出现的缩写要当场给全称（"one-step text-to-image (T2I) models"）。
- 形容词要能被下一句回收，例如《ChordEdit》首句的 "unprecedented synthesis speed" 被第 2 句的 "fails" 反转。
- 不要写"随着深度学习的发展"这类任何论文都能用的开头；主语必须是本文所在的具体技术或任务。

### 2.2 问题（Problem）

**要完成什么**：指出这个领域目前"坏在哪里"，要写出具体可见的失败现象或权衡，而不是泛泛的"仍有挑战"。

**常见写法**：`However` 转折句（34.4% 的摘要用到 "However" [重算]）；"suffer from / struggle to / remain hampered"；"face a trade-off"。

**模板**：

1. `However, [X]'s application to [Y] remains [severely hampered], as [Z] fails.`
   - 原句："However, their application to text-guided image editing remains severely hampered, as forcing existing training-free editors into a single inference step fails." —《ChordEdit》
2. `However, current [models] still struggle to [do Y], particularly when [condition].`
   - 原句："However, current models still struggle to produce physically consistent results, particularly when handling large-scale or complex dynamics." —《ProPhy》
3. `However, [X] suffer from [A] that [compromise B and limit C].`
   - 原句："However, current approaches combining Artificial Neural Networks (ANNs) and SNNs suffer from suboptimal architectures that compromise energy efficiency and limit tracking performance." —《SDTrack》
4. `[X] face a [core / critical] trade-off: they are either [A], [failing to …], or [B], [causing …].`
   - 原句："Existing guard-railing methods face a core trade-off: they are either rigid, failing to generalize to paraphrased or context-shifted prompts, or coarse, distorting unrelated content and fidelity." —《GenErase》
5. `[X] face a critical three-way trade-off between [A], [B], and [C].`
   - 原句："Fine-tuning approaches for Vision-Language Models (VLMs) face a critical three-way trade-off between In-Distribution (ID) accuracy, Out-of-Distribution (OOD) generalization, and adversarial robustness." —《The Geometry of Robustness》
6. `However, progress [in this field] is severely limited by [scarcity of resource].`（数据型常用）
   - 原句："However, progress in this field is severely limited by the scarcity of curated, ethically sourced facial data and the high similarity among phenotypes across different conditions." —《RDFace》
7. `Despite [recent advances], [X] suffer from [N] fundamental limitations.` —《TeHOR》（模板）
8. `[X] is crucial in [Y] but remains vulnerable to [Z].` —《Fractal Camouflage》（模板）
9. `Despite [W], [X] are prone to [V1] and, more critically, [V2].` —《ApET》（模板）

**注意**：
- 能写成两个具体失败模式就不要只写一个抽象词，例如《ChordEdit》："severe object distortion and a critical loss of consistency in non-edited regions"。
- 问题句里的关键词（如 "single inference step"）要在方法句或结果句里被回收，形成首尾对仗。
- 用 trade-off 表述问题时，后面的方法句要写成"两者兼得"（achieving A while maintaining B）。

### 2.3 缺口（Gap）

**要完成什么**：把矛头指向"现有方法"，说明它们具体缺了什么，从而给本文留出位置。与问题句的区别是：问题讲现象，缺口讲现有方法的局限。

**常见写法**：Existing X either…or… / neither…nor…；overlook / neglect；remains underexplored；枚举"two key challenges: 1)…2)…"；数据型写 "no dataset contains…"。

**模板**：

1. `Existing [X] either [A, which …], or [B, which …].`
   - 原句："Existing frameworks either train on image-based pretext tasks, which do not account for dynamic elements, or on video sequences for action-level reasoning, which does not scale to dense pixel-level prediction." —《Featurising Pixels from Dynamic 3D Scenes》
2. `Existing [X] neither [V1] nor [V2], leading to [Z].`
   - 原句："Existing U-shaped CNN or Transformer designs neither control alias injection at decimation nor explicitly align high-resolution evidence before decoder fusion, leading to unstable interfaces under device and protocol variability." —《CROWn》
3. `Most existing works overlook [X], a key factor in [Y].`
   - 原句："Most existing works overlook the inherent modality gap in CLIP, a key factor in its generalization and adaptability." —《Mind the Gap》
4. `While existing [methods] have achieved [promising performance], they typically overlook [X].`
   - 原句："While existing enhancement methods have achieved promising performance, they typically overlook the subjective nature of visual preferences." —《SDUIE》
5. `Existing [methods] face two key challenges: 1) [A], and 2) [B].`
   - 原句："Existing methods face two key challenges: 1) the semantic prior gap due to the lack of descriptive text annotations in gesture datasets, and 2) the difficulty in achieving coordinated multimodal control over gesture generation." —《CoordSpeaker》
6. `Although [X] has been widely studied in [A], [B] remain largely unexplored, thereby limiting [C].`
   - 原句："Although SSC has been widely studied in terrestrial domains such as autonomous driving, aerial settings like autonomous flying remain largely unexplored, thereby limiting progress on downstream applications." —《OccuFly》
7. `Existing approaches typically rely on [X], but [Y], leading to [Z].`
   - 原句："Existing approaches typically rely on multimodal large language models to infer user preferences, but the derived prompts or latent codes rarely reflect them faithfully, leading to suboptimal personalization." —《Premier》
8. `However, no [dataset] contains [property].`（数据型）
   - 原句："However, no dataset contains videos of real-world UDC degradation." —《UDC-VIT》
9. `Existing [X], designed primarily for [A], are unsuitable for [B], as they are [defect1], [defect2], or [defect3].`
   - 原句："Existing defenses, designed primarily for text-only LLMs, are unsuitable for countering these multimodal threats, as they are easily bypassed, modality-dependent, or generalize poorly." —《ARGUS》
10. `Yet, [its reliance on X] prevents [Y].`（短句缺口）
    - 原句："Yet, its reliance on text conditions prevents its use in unconditional generation." —《Guiding a Diffusion Model by Swapping Its Tokens》

**注意**：
- 缺口里列出几项（two / three），后面的设计细节就要对应给出几项（枚举配平式，证据：《CADC》《FedSDR》《CoordSpeaker》）。
- 缺口句里的并列缺陷最好与引言中的几类基线一一对应（《ARGUS》的三个并列形容词分别对应引言里的三类基线）。
- 不点名具体方法，写 "existing methods / current approaches" 即可；需要点名时直接写方法名，不写 [n]。

### 2.4 根因（Root cause）

**要完成什么**：解释问题"为什么会发生"，把现象归结到一个具体机制。这是瓶颈突破型最有说服力的一句（该类 47% 的摘要含根因 [重算]），根因也要能被你的方法直接"对症下药"。

**常见写法**：This stems from…；The root cause lies in…；We attribute this X to Y；…, a phenomenon we term X；This is because…。常与问题句合并："This failure manifests as [symptom], resulting from [cause]."

**模板**：

1. `This failure manifests as [symptom A] and [symptom B], resulting from [root cause].`
   - 原句："This failure manifests as severe object distortion and a critical loss of consistency in non-edited regions, resulting from the high-energy, erratic trajectories produced by naive vector arithmetic on the models' structured fields." —《ChordEdit》
2. `This stems from two key obstacles: [A], and [B].`
   - 原句："This stems from two key obstacles: the lack of volumetric interiors with coherent textures in GS representation, and the absence of fracture-aware simulation methods for Gaussians." —《GaussianFluent》
3. `The root cause lies in the fact that [X], while [enhancing A], [weakens B].`
   - 原句："The root cause lies in the fact that adaptive learning rate, while enhancing saddle-point escape, weaken the preference for flat minima." —《FedAdamom》（注意原句有主谓不一致 "rate … weaken"，照用时改为 weakens）
4. `We attribute this [inefficiency / degradation] to [specific cause], leading to [effect].`
   - 原句："We attribute this degradation to the loss of height information during multi-modal alignment, leading to deviations in sequence order." —《Height-Fidelity Dense Global Fusion》
5. `We posit this failure stems from [X], a problem we formalize using [tool].`
   - 原句："We posit this failure stems from spurious correlations learned from visual context, a problem we formalize using a Structural Causal Model (SCM)." —《CIGPose》
6. `…, [correlations …] inevitably deviate from [Y], a phenomenon we term [Name].`
   - 原句："Due to client-specific label spaces and varying co-occurrence patterns, correlations learned by individual clients inevitably deviate from the global structure, a phenomenon we term label correlation drift." —《FedHarmony》
7. `This limitation arises primarily because [existing approaches do A] and [neglect B].`
   - 原句："This limitation arises primarily because existing approaches respond isotropically to physical prompts and neglect the fine-grained alignment between generated content and localized physical cues." —《ProPhy》
8. `We investigate the root cause of these issues and show that they stem from [X].`
   - 原句："We investigate the root cause of these issues and show that they stem from the normalization layers within the neural networks." —《Tiling artifacts and trade-offs》
9. `However, we also found that [naive fix] could be coupled with [side effect], and [excess] harms [performance].`（发现型根因）
   - 原句："However, we also found that a naive defense direction could be coupled with a utility-degrading direction, and excessive intervention strength harms model performance." —《ARGUS》

**注意**：
- 根因句中的关键词要和方法句形成对仗：《ARGUS》根因写 "coupled with"，方法写 "decouples from"；《ChordEdit》根因写 "high-energy"，方法写 "low-energy"。
- 用 "a phenomenon we term X" 给根因命名，等于在摘要里多造一个可以被引用的概念（《FedHarmony》《OSA》）。
- 根因只写一个主因，最多两个；写三个以上就会显得是在猜。

### 2.5 洞察（Insight）

**要完成什么**：给出"换个角度看问题"的核心观点或实验发现，把问题桥接到方法。洞察出现在方法之前（10.2%）或之后（17.0%）都可以 [重算]：放在前面是"先讲道理再给方法"，放在后面是"方法先亮相，再解释它为什么有效"。

**常见写法**：Our key insight is that…（3.4% [重算]）；We observe / find / reveal that…（9.8% [重算]）；We recast / reformulate / redefine X as Y；Surprisingly, we find that…

**模板**：

1. `We recast [task] as [a new problem formulation].`
   - 原句："We recast editing as a transport problem between the source and target distributions defined by the source and target text prompts." —《ChordEdit》
2. `To address these limitations, we reformulate [X] as [an optimal Y problem] jointly guided by [A] and [B].`
   - 原句："To address these limitations, we reformulate visual token reduction as an optimal subset selection problem jointly guided by two complementary objectives: informativeness and coverage." —《CoIn》
3. `Our key insight is that [X] can be effectively captured through [mechanism], enabled by [trick].`
   - 原句："Our key insight is that spatial and semantic relationships among Gaussians can be effectively captured through a sparse attention mechanism, enabled by a Z-order strategy that organizes the unstructured Gaussian set into a spatially coherent sequence." —《Z-Order Transformer for Feed-Forward Gaussian Splatting》
4. `Our observations reveal that [X] effectively reflects [Y].`
   - 原句："Our observations reveal that the modality gap effectively reflects the extent to which pre-trained knowledge is preserved." —《Mind the Gap》
5. `Our analysis reveals [a clear division / a hidden trend]: [finding].`
   - 原句："Our analysis reveals a clear division of roles in the alternating global-frame architecture: early global layers do not form meaningful correspondences, middle layers perform cross-view alignment, and last layers provide only minor refinements." —《AVGGT》
6. `We find that [a straightforward implementation of X] fails to [Y].`
   - 原句："We find that a straightforward implementation of vanilla diffusion forcing (as proposed for video models) fails to model real motion distributions." —《FloodDiffusion》
7. `Surprisingly, we find that [a simple approach] yields reasonable results.`
   - 原句："Surprisingly, we find that a simple test-time training, which fine-tunes monocular depth foundation models on sparse depth measurements from sensors just as it is, yields reasonable results." —《Test-Time Prompt Tuning for Zero-Shot Depth Completion》
8. `Inspired by [X], we hypothesize that [Y] can be achieved by [Z].`（假设式，后面要接验证）
   - 原句："Inspired by activation steering research, we hypothesize that a robust, general defense independent of modality can be achieved by steering the model's behavior in the representation space." —《ARGUS》
9. `In this work, we redefine [X] as [Y], which necessitates [Z].`
   - 原句："In this work, we redefine WSI retrieval as a semantically optimal matching problem between arbitrary regions under spatial transformations, which necessitates a region-level representation that maintains semantic consistency." —《URICA》
10. `We identify two critical factors for [X]: [A] and [B].` —《LoftUp》（模板，后面接 "For A, we introduce…; For B, we propose…" 严格排比）

**注意**：
- 洞察句的动词决定了论文的气质：recast / reformulate / redefine 表示视角重构，observe / find / reveal 表示实证发现，hypothesize 表示需要后面验证。
- 发现-解释型论文的洞察句必须是一个可证伪的具体陈述（"X reflects Y"），不能写 "we gain insights into X"。
- 洞察之后紧接 "Based on this insight / these insights, we propose X"（《Mind the Gap》《SenCache》《SD-MIA》），因果链最清楚。

### 2.6 方法（Method）

**要完成什么**：给出方法名、方法类别和一句话机制。这是整篇摘要最固定的一句。

**常见写法**：同位语一次给全：`we [propose / introduce / present] Name, a [category] that [mechanism]`。三个动词的使用次数：propose 442，introduce 316，present 176 [重算]。36.8% 的摘要用 "To address / tackle / overcome / bridge…" 引出方法句 [重算]。20.8% 的摘要在方法句中写成"全称 (缩写)"的形式 [重算]。

**模板**：

1. `To address this problem, we introduce [Name], a [adj1], [adj2], and [adj3] method that [function].`
   - 原句："To address this problem, we introduce ChordEdit, a model agnostic, training-free, and inversion-free method that facilitates high-fidelity one-step editing." —《ChordEdit》
2. `We introduce [Name], a [category] for [task] that [key property / scale].`
   - 原句："We introduce NITROGEN, a vision-action foundation model for generalist gaming agents that is trained on 40,000 hours of gameplay videos across more than 1,000 games." —《NitroGen》
3. `We present [Full Name] ([ACRONYM]), a [category] that achieves [result] with only [minimal resource].`
   - 原句："We present Spectrum from Defocus (SfD), a chromatic focal sweep method that achieves state-of-the-art hyperspectral imaging with only two off-the-shelf lenses, a grayscale sensor, and less than one second of reconstruction time." —《Spectrum from Defocus》
4. `We introduce [Full Name] ([ACRONYM]), a [training-free / plug-and-play] [component] that [mechanism].`
   - 原句："We introduce Spectral-Evolution-Aware Cache (SeaCache), a training-free cache schedule that bases reuse decisions on a spectrally aligned representation." —《SeaCache》
5. `To bridge this gap, we present [Name], a [domain-oriented category] that [strengthens …] through [structure].`
   - 原句："To bridge this gap, we present MEDIC-AD, a clinically oriented VLM that strengthens these three capabilities through a stage-wise framework." —《MEDIC-AD》
6. `We present [Name], the first [category] that achieves both [A] and [B] across [scope].`
   - 原句："We present ATOKEN, the first unified visual tokenizer that achieves both high-fidelity reconstruction and semantic understanding across images, videos, and 3D assets." —《AToken》
7. `Based on this [analysis / finding], we propose [Full Name] ([ACRONYM]), a [category] that [mechanism].`
   - 原句："Based on this analysis, we propose Sensitivity-Aware Caching (SenCache), a dynamic caching policy that adaptively selects caching timesteps on a per-sample basis." —《SenCache》
8. `In this work, we present [Name], a [cost-efficient] method that addresses these challenges by [mechanism].`
   - 原句："In this work, we present NuWa, a cost-efficient method that addresses these challenges by deriving small ViTs from base ViTs for edge devices with specific class requirements." —《NuWa》
9. `To resolve this [dilemma], we propose a [descriptive phrase], termed [Name].`（仪式感命名）
   - 原句："To resolve this fundamental dilemma, we propose a streaming diffusion model for efficient infrared and visible video fusion, termed SDMFusion." —《Streaming Diffusion Model for Fast Infrared and Visible Video Fusion》
10. `This paper introduces [Name], a simple yet powerful [category] designed to [efficiently solve this task].`（方法直切式第 2 句）
    - 原句："This paper introduces D4RT, a simple yet powerful feedforward model designed to efficiently solve this task." —《D4RT》

**注意**：
- 同位语后面的形容词要直接对应前文的缺口：《ChordEdit》"training-free, inversion-free" 就是针对引言里基线"需训练 + 需反演"的缺陷。
- "the first" 出现在 13.1% 的摘要中 [重算]，用之前要确认限定语足够窄（"the first unified visual tokenizer that achieves both…"）。
- "novel" 出现在 33.6% 的摘要中 [重算]，属于高频空词，删掉通常不损失信息。
- 方法名的出场方式见第 3.2 节，取法见 references/naming.md。

### 2.7 设计细节（Design details）

**要完成什么**：用 1–3 句交代方法的关键组件和各自的作用，让读者知道"它具体怎么做"。64.6% 的摘要有这一句 [重算]。38.7% 的摘要在设计细节之后又回到方法句（"方法 → 设计细节 → 方法"）[重算]，常见做法是先说总体方法，再说组件，最后再补一句附加模块。

**常见写法**：Specifically, …；X consists of / comprises two [modules]: A and B；First, … Second, …；The core of X is …；Instead of A, we B；Concretely, …

**模板**：

1. `Specifically, we [introduce / construct] [component] [with property] to [purpose].`
   - 原句："Specifically, we introduce a pure transformer architecture with 4D rotary position embeddings to process visual inputs of arbitrary resolutions and temporal durations." —《AToken》
2. `[Name] consists of two key steps: [A] and [B].`
   - 原句："UNO-Adapter consists of two key steps: unsupervised concept discovery and neural concept binder." —《Learning Latent Concepts for Detecting OOD Objects》
3. `[Name] utilizes a [unified architecture] to jointly infer [A], [B], and [C] from [input].`
   - 原句："D4RT utilizes a unified transformer architecture to jointly infer depth, spatio-temporal correspondence, and full camera parameters from a single video." —《D4RT》
4. `The core of [Name] is a novel [Module]: it first [step 1] and then [step 2].`
   - 原句："The core of CIGPose is a novel Causal Intervention Module: it first identifies confounded keypoint representations via predictive uncertainty and then replaces them with learned, context-invariant canonical embeddings." —《CIGPose》
5. `At its core are [Module (ABBR)] blocks, which utilize [X] to produce [Y].`
   - 原句："At its core are AnchorMambaPooling (AMP) blocks, which utilize Mamba's selective scanning to produce compact anchor tokens summarizing video content across scales." —《HieraMamba》
6. `Our approach leverages [A] to [goal 1] and [B] to [goal 2], introducing [a new perspective].`
   - 原句："Our approach leverages modality gap preservation to mitigate forgetting and modality gap compensation to enhance the capacity for new data, introducing a novel modality-gap-based perspective for continual learning." —《Mind the Gap》
7. `Instead of [conventional approach], we [new approach].`
   - 原句："Instead of modifying the hardware or optics of each individual camera, we encode high-speed scene dynamics by illuminating the scene with a rapid, sequential color coded sequence." —《Color-Encoded Illumination for High-Speed Volumetric Scene Reconstruction》
8. `We scale [X] through three key ingredients: 1) [A], 2) [B], and 3) [C].`
   - 原句："We scale embodied agents through three key ingredients: 1) an internet-scale video-action dataset constructed by automatically extracting player actions from publicly available gameplay videos, 2) a multi-game benchmark environment that can measure cross-game generalization, and 3) a unified vision-action model trained with large-scale behavior cloning." —《NitroGen》
9. `[Name] also introduces a lightweight [stage A] to [purpose], and a [stage B] to [purpose].`
   - 原句："ARGUS also introduces a lightweight injection detection stage to activate the defense on-demand, and a post-filtering stage to verify defense success." —《ARGUS》
10. `This strategy yields a [adj] [field / representation] that is inherently [stable], facilitating [capability].`（设计细节 + 结果）
    - 原句："This strategy yields a smoothed, variance-reduced editing field that is inherently stable, facilitating the field to be traversed in a single, large integration step." —《ChordEdit》

**注意**：
- 每个组件都要写"做什么 + 为了什么"（to mitigate forgetting / to enhance capacity），不要只罗列模块名。
- 子模块缩写一般不放进摘要；如果要放，必须当场展开（"AnchorMambaPooling (AMP)"）。子模块缩写在摘要中缺席、要读正文才能对上，是材料中列出的常见问题之一。
- 组件数要与缺口数一致（两个缺口对两个组件），这一点《LoftUp》"For A… For B…" 和《FixTalk》"两个 insight 对应两个模块" 都做到了。

### 2.8 结果（Results）

**要完成什么**：用证据证明方法有效。96.2% 的摘要都有结果句 [重算]。

**常见写法**：定性：Extensive experiments on X demonstrate that Y achieves state-of-the-art…（"state-of-the-art/SOTA" 出现在 42.6% 的摘要中，"extensive experiments" 29.3%，"outperform" 23.7% [重算]）。定量：outperforms X by N%；up to N×；while using M× fewer；respectively。

**模板**：

1. `Extensive experiments on [benchmarks] demonstrate that [Name] [produces more A, B, and C results] than existing state-of-the-art methods.`
   - 原句："Extensive experiments on physics-aware video generation benchmarks demonstrate that ProPhy produces more realistic, dynamic, and physically coherent results than existing state-of-the-art methods." —《ProPhy》
2. `Extensive experiments on [multiple benchmarks] demonstrate that our method outperforms existing approaches without requiring [extra resource].`
   - 原句："Extensive experiments on multiple benchmarks demonstrate that our method outperforms existing approaches without requiring additional replay data." —《Mind the Gap》
3. `[Name] achieves state-of-the-art results across [A, B, C], outperforming previous work by +[N] [metric], while using [M]× fewer [resource].`
   - 原句："INSID3 achieves state-of-the-art results across one-shot semantic, part, and personalized segmentation, outperforming previous work by +7.5 % mIoU, while using 3× fewer parameters and without any mask or category-level supervision." —《INSID3》
4. `When [fine-tuned], [X] transfers effectively to [unseen setting], achieving up to [N]% relative improvement in [metric] over [baseline].`
   - 原句："When fine-tuned, pre-training transfers effectively to unseen games, achieving up to 52% relative improvement in task success rates over models trained from scratch." —《NitroGen》
5. `In [hard scenario, e.g. dataset], [Name] achieves more than [N]× speedup over [baseline] while also improving [quality].`
   - 原句："In heavily occluded scenarios such as the MatrixCity Streets dataset, Proxy-GS achieves more than 2.5× speedup over Octree-GS while also improving rendering quality." —《Proxy-GS》
6. `[Name] improves [metric A] by +[a], boosts [metric B] by +[b], and reduces [metric C] by [c]%.`
   - 原句："CURE improves grounding accuracy by +0.35 IoU, boosts report quality by +0.192 CXRFEScore, and reduces hallucinations by 18.6%." —《CURE》
7. `On [benchmark], [Name] sets a new state-of-the-art, achieving [a]% and [b]% [metric] for [task A] and [task B], respectively.`
   - 原句："On the Ego–Exo4D benchmark, VGGT-S sets a new state-of-the-art, achieving 67.7% and 68.0% average IoU for Ego→Exo and Exo→Ego tasks, respectively, significantly outperforming prior methods." —《VGGT-Segmentor》
8. `It achieves up to [a]× and [b]× speedup on [model A] and [model B], respectively, without compromising [quality].`（效率型）
   - 原句："Extensive experiments demonstrate the effectiveness of our approach: it achieves up to 3.52× and 3.2× speedup on FLUX-1.Dev and Wan 2.1, respectively, without compromising the generation quality and prompt adherence." —《DDiT》
9. `[Name] is on par with or even outperforms [strong baselines] in [A, B, C].`（克制型）
   - 原句："Furthermore, comprehensive experiments demonstrate that it is on par with or even outperforms these large models in realism, vividness, and video quality." —《Real-Time Generation of Streamable Talking Portrait Video》（原句的句首过渡词可删）
10. `Our analysis reveals that [X] fail to convincingly outperform [baseline] in [settings].`（发现型结果）
    - 原句："Our analysis reveals that high-quality coresets fail to convincingly outperform the random baseline in both SL and SL+KD regimes." —《Rethinking Dataset Distillation》

**注意**：
- 数字的写法见第 3.3 节。
- "achieving A while maintaining / without compromising B" 是回应 trade-off 类问题的标准写法。
- 结论强度不能超过正文证据。材料中的反例：《AVGGT》摘要写 "matching or slightly improving"，但正文部分指标下降；《D4RT》摘要写 "sets a new state of the art … across a wide spectrum"，但表格里部分指标并非最优。有例外时改用 "competitive / on par with"，或把主张收缩到实际领先的范围。
- 摘要只建立问题、缺口、方案、最强结果和意义，不提不足、不写局限，也不专门写一句不如谁（`references/anti_defensive.md` §0、§3）。

### 2.9 泛化（Generalization）

**要完成什么**：说明方法在原任务之外也有效（跨域、零样本、即插即用、可迁移到其他模型）。13.3% 的摘要把泛化作为主作用 [stats 序列表重算]，能力扩展型最常用（52%）。

**模板**：

1. `Beyond [core task], [Name] attains strong performance on [other tasks], suggesting that [lesson].`
   - 原句："Beyond visual search, CodeV attains strong performance on a range of multimodal reasoning and math benchmarks, suggesting that explicitly supervising intermediate tool behavior is crucial for building trustworthy, agentic visual reasoning systems." —《CodeV》
2. `[Name] exhibits competence across diverse domains, including [A], [B], and [C].`
   - 原句："NITROGEN exhibits competence across diverse domains, including combat encounters in 3D action games, high-precision control in 2D platformers, and exploration in procedurally generated worlds." —《NitroGen》
3. `Our method is training-free and zero-shot, enabling [high scalability].`
   - 原句："Furthermore, our method is training-free and zero-shot, enabling high scalability." —《ANTS》（原句的句首过渡词可删）
4. `The framework is plug-and-play and model-agnostic, seamlessly integrating with [existing pipelines].`
   - 原句："The framework is plug-and-play and model-agnostic, seamlessly integrating with existing gloss-based or gloss-free pipelines across languages." —《BoostSLT》
5. `Beyond [core setting], our approach scales effectively across diverse data sources, including [A], [B], and [C].`
   - 原句："Moreover, our approach scales effectively across diverse data sources, including real-world robot data, simulation, and human egocentric video." —《StaMo》（原句的句首过渡词可删）
6. `[Name] generalizes across [domain A] and [domain B] where [hard condition], and it achieves competitive performance on [benchmarks].`
   - 原句："UnReflectAnything generalizes across natural and surgical domains where non-Lambertian surfaces and non-uniform lighting create severe highlights and it achieves competitive performance with state-of-the-art results on several benchmarks." —《UnReflectAnything》
7. `Beyond [robust zero-shot X], it readily empowers [N] diverse downstream applications, seamlessly enabling [A, B, C].`
   - 原句："Beyond robust zero-shot 3D/4D generation, it readily empowers over a dozen diverse downstream applications, seamlessly enabling tasks like video editing, stabilization, and virtual try-on." —《Taming Video Models for 3D and 4D Generation》
8. `…while remaining compatible with [X] in a zero-shot manner.` —《GLMap》（模板）
9. `As a fully plug-and-play method, [Name] requires no retraining.` —《GeoRK2》（模板）

**注意**：
- 泛化要落到具体域或具体模型的名字上（natural and surgical domains；FLUX-1.Dev and Wan 2.1），不要只写 "various scenarios"。
- 泛化句常接在结果句之后，不要用 Furthermore / Moreover 开头；用 "Beyond [X], ..." 承接上一句的关键词，或直接以方法名作主语陈述（见 `references/word_style.md` 第 4.2 节）。

### 2.10 意义（Significance）

**要完成什么**：把结果上升到对领域的影响。24.5% 的摘要有意义句 [重算]，常与结果合写在末句（结果+意义占末句的 17.9% [stats]）。语气要克制：用 "a step toward / pave the way / a foundation for"，不要写 "solve"。

**模板**：

1. `[Our approach] represents a significant step toward [goal].`
   - 原句："Our approach represents a significant step toward eliminating non-differentiable post-processing." —《Differentiable Laplacian Matrix Guided Superpixel Segmentation》
2. `By [V-ing X], [Name] takes a step toward [long-term goal].`
   - 原句："By transforming reasoning traces from one-shot descriptions to causal self-correction signals, CF-VLA takes a step toward self-reflective autonomous driving agents that learn to think before they act." —《Counterfactual VLA》
3. `Our results pave the way for [new capability].`
   - 原句："Our results pave the way for interactive, instruction-driven image manipulation with continuous and compositional control." —《SliderEdit》
4. `…, providing a principled step toward [goal].`
   - 原句："Geometric analysis confirms that GRACE converges to flatter minima without feature distortion across distribution shifts, providing a principled step toward generalized robustness in foundation VLMs." —《The Geometry of Robustness》
5. `Overall, our findings challenge a growing assumption in [field], namely that [assumption].`（发现型）
   - 原句："Overall, our findings challenge a growing assumption in vision research, namely that progress in generative realism implies progress in data realism." —《When Pretty Isn't Useful》
6. `This performance saturation calls into question the widespread practice of [X].`（发现型）
   - 原句："This performance saturation calls into question the widespread practice of using soft labels for model evaluation, where unlike the HL setting, subset quality has negligible influence." —《Rethinking Dataset Distillation》
7. `In summary, [Benchmark] establishes a realistic foundation for evaluating [X] and highlights key gaps that future systems must address.`（基准型）
   - 原句："In summary, PAI-Bench establishes a realistic foundation for evaluating Physical AI and highlights key gaps that future systems must address." —《PAI-Bench》
8. `We hope this study and [artifact] can facilitate future work on [topic].`
   - 原句："We hope this study and the ViT3 baseline can facilitate future work on visual TTT models." —《ViT^3》
9. `A theoretically grounded and experimentally validated approach allows [Name] to deliver [A], finally achieving [goal stated in the problem sentence].`（首尾呼应）
   - 原句："A theoretically grounded and experimentally validated approach allows ChordEdit to deliver fast, lightweight and precise edits, finally achieving true real-time editing on these challenging models." —《ChordEdit》

**注意**：
- 最好的意义句会回收首句或问题句中的关键词（《ChordEdit》用 "finally achieving true real-time editing" 回收第 2 句的 "remains severely hampered"；《NitroGen》用 "generalist embodied agents" 回收首句）。
- "We believe our approach offers a significant advancement in…"（《Native and Compact Structured Latents》）这类空泛句可以用，但信息量低；优先写具体能力或具体范式转变。

### 2.11 资源发布（Resource release）

**要完成什么**：给出代码、数据或项目页链接。43.1% 的摘要以此收尾 [stats]，36.8% 的摘要含 URL [重算]。以资源收尾的末句中位长度只有 **6 个词** [重算]，和前面约 22 词的长句形成节奏反差。

**模板**（按频率从高到低）：

1. `Code is available at [URL].`
   - 原句："Code is available at https://github.com/CIVA-Lab/v-umlaut." —《Linear Fundamental Matrix Estimation from 7 or 5 Points》
2. `Our code is available at [URL].`
   - 原句："Our code is available at https://github.com/linlany/MindtheGap." —《Mind the Gap》
3. `Project page: [URL]`
   - 原句："Project page: https://heyumeng.com/SPARK-web/" —《SPARK》
4. `[Our code / The code] will be available at [URL].`（承诺型，投稿时未开源）
   - 原句："Our code will be available at https://github.com/ZeroNLP/ARGUS." —《ARGUS》
5. `We release [A], [B], and [C] to advance research on [X].`（资源 + 意义）
   - 原句："We release the dataset, evaluation suite, and model weights to advance research on generalist embodied agents." —《NitroGen》
6. `We release our code, model weights, an online demo, and [a new benchmark] at [URL].`
   - 原句："We release our code, model weights, an online demo, and a new challenging benchmark for in-the-wild 3D object reconstruction at https://ai.meta.com/sam3d ." —《SAM 3D》
7. `All [code and data] [are released / will be publicly released] at [URL].`
   - 原句："All code and data are released at https://github.com/OpenSenseNova/SenseNova-MARS." —《SenseSearch》
8. `The data, code, and model will be publicly available at [URL].`
   - 原句："The data, code, and model will be publicly available at https://haolinyanghlyang.github.io/SoccerMaster." —《SoccerMaster》
9. `Code is here.`（三个词的极简收尾）—《SPDMark》

**注意**：资源句不加修饰；如果还想表达意义，就写成模板 5 的 "We release … to advance research on …"，一句同时完成两个作用。

---

## 3. 关键细节

### 3.1 开头策略

| 策略 | 占比 | 写法 | 适用 | 证据 |
|---|---|---|---|---|
| 纯背景句 | 56.6% [stats] | 领域价值判断 / 近期进展 / "remains a challenge" | 默认 | 《D4RT》《Mind the Gap》《ProPhy》 |
| 背景 + 问题合句 | 21.2% [stats] | "X have achieved…, but/yet…" / "Despite X, Y…" | 想在第 1 句就制造张力 | 《AdaptVision》《PHASE-Net》《4D-RGPT》 |
| 背景 + 缺口合句 | 7.3% [stats] | "Despite the perceived success of X, recent evidence finds that…" | 发现型，挑战共识 | 《Rethinking Dataset Distillation》 |
| 方法直切 | 6.6% [stats] | "We introduce / present X, a…" | 方法自带辨识度、系统/基础模型 | 《NitroGen》《CUPID》《Fresco》《MeshLLM》 |

规则：
- 首句不写引用，也不写"随着……的发展"。
- 首句主语用具体技术名词（one-step T2I models, 3DGS, VLMs），不用 "deep learning"。
- 方法直切式要在前两句内把"为什么需要它"补上，或者像《D4RT》那样用 "sidesteps the heavy computation of…" 把缺口压进设计句里。

### 3.2 方法名如何引入

**位置** [重算]：第一次出现 "we propose / introduce / present" 的句子最集中在第 3 句（27.5%）和第 4 句（23.9%），所以**默认放在第 3–4 句**，前面刚好是 1 句背景 + 1–2 句问题/缺口。默认写法是同位语一次给全：`we propose Name (Full Name / ABBR), a [category] that [mechanism]`；名字只在这一句首次定义，之后全篇统一使用。

> 其他引入方式（termed / dubbed、先讲道理再亮名、先亮代号、不命名）、完整位置统计和名字的取法见 references/naming.md §4。

### 3.3 数字与对比的写法

**总体克制**：76.3% 的摘要全篇不出现百分比或倍数 [重算]。含 % 的占 17.8%，含 ×/times 的占 8.1%，用 "up to N" 的占 4.2% [重算]。例外是效率优化型，62% 带数字。

**写法规则**：
1. 数字只放在结果句（规模数字可以放在方法句，如《NitroGen》"40,000 hours of gameplay videos across more than 1,000 games"）。
2. 每个数字绑定"对比对象 + 数据集/场景"："more than 2.5× speedup over Octree-GS … on MatrixCity Streets"（《Proxy-GS》）；"up to 52% relative improvement … over models trained from scratch"（《NitroGen》）。
3. 多指标或多基线用 respectively：《VGGT-Segmentor》《DDiT》《PersonaVLM》。
4. "增益 + 代价"成对写：`outperforming … by +7.5 % mIoU, while using 3× fewer parameters`（《INSID3》）；`improving IoU by over 9 points while using nearly half as many primitives`（《Residual Primitive Fitting》）。
5. 数字取最强且最稳的那一个，前面加 "up to" 限定（《NuWa》"by up to 29.00% in accuracy"）。
6. 数据集型论文用规模数字证明价值，不用精度数字（《SceneScribe-1M》《Derm1M》）。
7. 发现型论文可以用计数词体现系统性：`A subsequent systematic evaluation of five large-scale and four small-scale DD methods`（《Rethinking Dataset Distillation》）。
8. 不给数字时，结果句至少要写出比较对象和数据集范围（"on multiple benchmarks … without requiring additional replay data"），不能只写 "achieves good performance"。
9. 标题关键词是效率（如 "Efficiently"）时应当给数字。《D4RT》被笔记指出的遗憾是：正文里"比 VGGT 快 9 倍"本可以成为很强的钩子，摘要却一个数字都没给。

### 3.4 结尾策略

| 末句类型 | 占比 [stats] | 写法 |
|---|---|---|
| 资源发布 | 43.1% | 极短句：`Code is available at [URL].` |
| 结果 + 意义 | 17.9% | `…, finally achieving true real-time editing on these challenging models.` |
| 结果 | 12.0% | 以最强的数字结果收尾 |
| 意义 | 10.4% | `a step toward / pave the way for / challenge a growing assumption` |
| 结果 + 泛化 | 6.1% | `Beyond X, Y also…` |

规则：
- 有开源就把资源句放最后；结果和意义放在倒数第二句。
- 没有开源时，用意义句收尾，并回收首句或问题句中的关键词，做到首尾呼应（《Fed-ADE》《ChordEdit》）。
- 意义句忌写 "solve"，用 "a principled step toward / promising direction"。

### 3.5 缩写和引用

- **缩写**：自造缩写一律在首次出现时写成"全称 (缩写)"，之后全篇统一使用缩写（《Mind the Gap》"Contrastive Language-Image Pre-trained model (CLIP)"；《Rethinking Dataset Distillation》"hard-label (HL)"）。领域通用缩写（SOTA、VAE、3DGS、VLM、RL、SLAM、CLIP、SAM、NeRF）可以不展开。
- **缩写密度**：摘要里自造缩写不超过 2–3 个（主方法名加最多一两个核心概念）；子模块缩写留给正文。材料把"缩写密度过高"列为常见问题。
- **引用**：摘要中不写 [n]。只有 1.4% 的摘要带编号引用 [重算]，而且只在两种情况下出现：把关键发现归功于他人（《Rethinking Dataset Distillation》"recent evidence [20] finds that…"），或点名唯一的强基线（"only RDED [25] reliably outperforms…"）。其余情况直接写方法名（"outperforming Octree-GS"）。

### 3.6 高频词的取舍（[重算]，出现该词的摘要比例）

| 词 | 占比 | 建议 |
|---|---|---|
| state-of-the-art / SOTA | 42.6% | 可以用，但要跟上数据集或数字 |
| To address / tackle / overcome / bridge | 36.8% | 方法句的标准引导语 |
| However | 34.4% | 问题句的标准转折词，全篇只用一次 |
| novel | 33.6% | 高频空词，建议删除 |
| extensive experiments | 29.3% | 后面必须接 "on [benchmarks]" |
| outperform | 23.7% | 要写出比较对象 |
| the first | 13.1% | 限定语要足够窄 |
| we observe / find / reveal / identify | 9.8% | 洞察句的标志 |
| key insight / idea | 3.4% | 少用但效果好 |
| simple yet effective / powerful | 少量 | 《Mind the Gap》《D4RT》在用；要有实验支撑 "simple" |

---

> 取名（方法名、数据集和子模块命名、标题、名字的首次引入）见 references/naming.md。

---

## 4. 范例：完整摘要逐句拆解

### 范例 1：《ChordEdit: One-Step Low-Energy Transport for Image Editing》（CVPR 2026 Best Student Paper Honorable Mention，瓶颈突破型，8 句）

骨架：背景 → 问题 → 问题+根因 → 方法 → 洞察 → 方法 → 设计细节+结果 → 结果+意义

| # | 原句 | 作用 | 可学之处 |
|---|---|---|---|
| 1 | The advent of one-step text-to-image (T2I) models offers unprecedented synthesis speed. | 背景 | 10 个词立起背景；"unprecedented" 先扬，为转折蓄势；T2I 当场给出全称。 |
| 2 | However, their application to text-guided image editing remains severely hampered, as forcing existing training-free editors into a single inference step fails. | 问题 | "However … remains severely hampered, as … fails"；"single inference step" 与标题 One-Step 呼应。 |
| 3 | This failure manifests as severe object distortion and a critical loss of consistency in non-edited regions, resulting from the high-energy, erratic trajectories produced by naive vector arithmetic on the models' structured fields. | 问题+根因 | 两个可视化的失败模式 + "resulting from" 归因；提前抛出核心术语 "high-energy"；点名被批评的做法 "naive vector arithmetic"。 |
| 4 | To address this problem, we introduce ChordEdit, a model agnostic, training-free, and inversion-free method that facilitates high-fidelity one-step editing. | 方法 | 第 4 句出场（最常见的位置）；三个并列形容词就是三个卖点，对应基线的缺陷。 |
| 5 | We recast editing as a transport problem between the source and target distributions defined by the source and target text prompts. | 洞察 | "We recast X as Y" 重构视角。 |
| 6 | Leveraging dynamic optimal transport theory, we derive a principled, low-energy control strategy. | 方法 | "low-energy" 对应根因里的 "high-energy"，形成对仗。 |
| 7 | This strategy yields a smoothed, variance-reduced editing field that is inherently stable, facilitating the field to be traversed in a single, large integration step. | 设计细节+结果 | "single, large integration step" 回收第 2 句的失败条件。 |
| 8 | A theoretically grounded and experimentally validated approach allows ChordEdit to deliver fast, lightweight and precise edits, finally achieving true real-time editing on these challenging models. | 结果+意义 | "finally achieving" 回收第 2 句的 "remains hampered"，首尾呼应。 |

要点：全篇**零数字、零引用**，只有一个缩写（T2I）；靠三组关键词对仗（high-energy ↔ low-energy；single step fails ↔ single step traversed；hampered ↔ finally achieving）建立逻辑链。方法类内容占 4 句（4–7）。名字来源：引言里的 "seeking a low-energy chord to transport…"，名字本身就是机制的隐喻。

### 范例 2：《Mind the Gap: Preserving and Compensating for the Modality Gap in CLIP-Based Continual Learning》（ICCV 2025 highlight，发现-解释型，9 句）

骨架：背景 → 背景 → 缺口 → 方法（分析）→ 洞察 → 方法 → 设计细节+意义 → 结果 → 资源发布

| # | 原句 | 作用 | 可学之处 |
|---|---|---|---|
| 1 | Continual learning aims to enable models to learn sequentially from continuously incoming data while retaining performance on previously learned tasks. | 背景 | 教科书式任务定义句，用 while 把"学新 + 不忘旧"两个目标压进一句。 |
| 2 | With the Contrastive Language-Image Pre-trained model (CLIP) exhibiting strong capabilities across various downstream tasks, there has been growing interest in leveraging CLIP for continual learning in such scenarios. | 背景 | 第 2 句背景把领域收窄到具体对象 CLIP，并当场展开缩写。 |
| 3 | Most existing works overlook the inherent modality gap in CLIP, a key factor in its generalization and adaptability. | 缺口 | "overlook X, a key factor in Y"：用同位语给被忽视的概念做重要性背书。 |
| 4 | In this paper, we analyze the variations in the modality gap during the fine-tuning of vision-language pre-trained models. | 方法（分析） | 发现型论文的"方法"先是一个分析动作。 |
| 5 | Our observations reveal that the modality gap effectively reflects the extent to which pre-trained knowledge is preserved. | 洞察 | 一个可证伪的具体陈述（X reflects Y），是全文的理论根基。 |
| 6 | Based on these insights, we propose a simple yet effective method, MG-CLIP, that improves CLIP's performance in class-incremental learning. | 方法 | "Based on these insights" 衔接因果；名字 MG-CLIP 属于血缘继承式（E 类）。 |
| 7 | Our approach leverages modality gap preservation to mitigate forgetting and modality gap compensation to enhance the capacity for new data, introducing a novel modality-gap-based perspective for continual learning. | 设计细节+意义 | 两个模块各带目的（preservation → forgetting；compensation → new data），正好对应第 1 句的两个目标。 |
| 8 | Extensive experiments on multiple benchmarks demonstrate that our method outperforms existing approaches without requiring additional replay data. | 结果 | 用 "without requiring additional replay data" 交代优势成立的前提。 |
| 9 | Our code is available at https://github.com/linlany/MindtheGap. | 资源发布 | 极短收尾。 |

要点：标题本身是双关钩子（方法之外不另造名，把巧思放进标题），方法名则是朴素的血缘式 MG-CLIP，说明"标题负责记忆点，方法名负责信息"。设计细节的两个模块与首句的双重目标一一对应。

### 范例 3：《NitroGen: An Open Foundation Model for Generalist Gaming Agents》（CVPR 2026 best，方法直切 + 资源型，5 句）

骨架：方法 → 设计细节 → 结果+泛化 → 结果+泛化 → 资源发布+意义

| # | 原句 | 作用 | 可学之处 |
|---|---|---|---|
| 1 | We introduce NITROGEN, a vision-action foundation model for generalist gaming agents that is trained on 40,000 hours of gameplay videos across more than 1,000 games. | 方法 | 首句即方法（占 6.6% 的写法）；规模数字放在第一句，立刻建立"互联网规模"的印象。 |
| 2 | We scale embodied agents through three key ingredients: 1) an internet-scale video-action dataset constructed by automatically extracting player actions from publicly available gameplay videos, 2) a multi-game benchmark environment that can measure cross-game generalization, and 3) a unified vision-action model trained with large-scale behavior cloning. | 设计细节 | "three key ingredients: 1)…2)…3)…" 与引言的三条贡献一一映射。 |
| 3 | NITROGEN exhibits competence across diverse domains, including combat encounters in 3D action games, high-precision control in 2D platformers, and exploration in procedurally generated worlds. | 结果/泛化 | 克制动词 "exhibits competence"，用三个具体任务类型支撑"多样性"。 |
| 4 | When fine-tuned, pre-training transfers effectively to unseen games, achieving up to 52% relative improvement in task success rates over models trained from scratch. | 结果/泛化 | 全篇唯一的性能数字，写全了"up to + 相对 + 指标 + 对比基线"。 |
| 5 | We release the dataset, evaluation suite, and model weights to advance research on generalist embodied agents. | 资源发布/意义 | 三个产出对应第 2 句的三个组成部分；"generalist embodied agents" 回收首句。 |

要点：5 句也能讲完整个故事，但前提是方法本身自带辨识度（基础模型 + 开源）。整篇没有背景句，缺口隐含在"规模"之中。数字集中在第 1 句（规模）和第 4 句（性能）。整篇没有出现任何缩写和引用编号。

---

## 5. 写摘要的步骤与检查清单

### 5.1 步骤

1. **定故事类型**：瓶颈突破 / 发现-解释 / 新问题定义 / 统一框架 / 数据与基准 / 效率优化 / 能力扩展。按第 1.6 节选骨架。
2. **列素材卡片**（每项一句中文）：
   - 领域和对象是什么（背景）
   - 具体坏在哪里：一两个可见的失败现象（问题）
   - 现有方法缺了什么（缺口，数一数有几项）
   - 为什么会这样（根因，只要一个主因）
   - 你换了什么视角或发现了什么（洞察）
   - 方法名 + 类别 + 一句话机制（方法）
   - 对应缺口数量的组件，每个组件"做什么 + 为了什么"（设计细节）
   - 最强、最稳的 1–2 个数字，以及它们的对比对象和数据集（结果）
   - 跨域 / 零样本 / 即插即用（泛化，可选）
   - 有无开源链接
3. **给方法取名**：按 references/naming.md 的取名流程生成并自检。
4. **按骨架逐句写**：每个作用从第 2 节的模板里选一个套用，填入具体技术名词。默认 8 句：背景 1 + 问题/缺口 1–2 + 方法 1 + 洞察或设计细节 1–2 + 结果 1–2 + 资源或意义 1。
5. **加对仗与回收**：问题句的关键词在方法句或结果句中回收（hampered ↔ finally achieving）；根因句的动词在方法句中反转（coupled ↔ decouples；high-energy ↔ low-energy）；末句回收首句的大目标。
6. **压缩**：删掉 novel、significantly 这类没有支撑的强调词；把句长控制在约 22 词；把"背景 + 问题"或"方法 + 设计细节"能合并的合成一句；总句数落在 7–9。
7. **对照正文核实**：每个断言（SOTA、the first、数字、泛化）都要在正文中找到对应的表或节。

### 5.2 检查清单（逐条打勾）

**结构**
- [ ] 句数在 6–10 之间（首选 7–9）
- [ ] 第 1 句是背景（或背景+问题）；若首句即方法，确有理由（系统 / 基础模型 / 辨识度高）
- [ ] 前 1/5 讲问题，方法最迟在第 2/5 段出现，最后 1/5 给结果 / 资源 / 意义
- [ ] 含问题或缺口句（79.6% 的摘要都有）
- [ ] 含结果句（96.2% 的摘要都有）
- [ ] 瓶颈突破型写了根因；发现-解释型写了洞察（"we observe / find / reveal that…" 或 "Our analysis reveals…"）
- [ ] 缺口列出 N 项时，设计细节也对应给出 N 项

**方法句与命名**
- [ ] 方法名出现在第 3–4 句附近（第 2–5 句也可接受）
- [ ] 用同位语一次给出：名字 + 类别 + 机制（we propose X, a Y that Z）
- [ ] 同位语中的形容词与前文缺口一一对应
- [ ] 名字能读出来，通过 references/naming.md 的检查清单
- [ ] 借势已有模型时，名字里保留原名
- [ ] 数据集 / 基准名带规模数字或 -Bench，且与方法名同一词根（如有）
- [ ] 摘要中自造缩写不超过 2–3 个；子模块缩写不进摘要，或进了就当场展开
- [ ] 名字、术语在摘要和正文中完全一致

**数字与对比**
- [ ] 数字不超过 2–3 处，集中在结果句（规模数字可放在方法句）
- [ ] 每个数字都绑定了对比对象和数据集 / 场景
- [ ] 多指标用 respectively；效率型写了"增益 + 质量不降"（while maintaining / without compromising）
- [ ] 效率优化型给出了倍数或百分比
- [ ] SOTA / the first / outperform 的强度与正文证据一致；有例外时改用 competitive / on par with
- [ ] 摘要里没有局限、不足或自我削弱的句子

**措辞**
- [ ] 没有 [n] 引用编号（除非是在把关键发现归功于他人）
- [ ] 首次出现的缩写都写了"全称 (缩写)"；通用缩写（SOTA、3DGS、VLM）不展开
- [ ] "However" 只用一次，放在问题句
- [ ] 没有以 Furthermore / Moreover / Additionally 开头的句子；已按 `references/word_style.md` 第 4.9 节完成去 AI 味自查
- [ ] 删掉了没有信息量的 novel、significantly、extensive（extensive 后面没有具体基准时）
- [ ] 至少一组关键词对仗或首尾呼应
- [ ] 没有主谓不一致、拼写错误（材料中高频：is/are 误用于复数主语，exisiting）

**结尾**
- [ ] 有开源：末句是约 6 个词的资源句（Code is available at [URL].）
- [ ] 无开源：末句是结果+意义或意义句，并回收了首句的关键词
- [ ] 意义句没有用 "solve"，而是用 step toward / pave the way / foundation for
