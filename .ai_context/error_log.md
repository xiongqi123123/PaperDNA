## Error Log
- **[Date] Error Type**: 
  - ❌ **Wrong**: 
  - ✅ **Right**: 
  - 🔒 **Instruction**: 

- **[2026-03-10] AI 风格词汇与机械过渡**
  - ❌ **Wrong**: 段首使用 “Furthermore / Moreover / Additionally / In conclusion”
  - ✅ **Right**: 通过复用上段关键词与论点自然承接段落
  - 🔒 **Instruction**: Never start a paragraph with mechanical transitions; prefer keyword linking.

- **[2026-03-10] 夸张形容词与副词**
  - ❌ **Wrong**: 使用 “paramount / crucial / revolutionary / vital” 等情绪化词
  - ✅ **Right**: 使用客观、可验证的描述（数据、约束、方法）
  - 🔒 **Instruction**: Replace hyperbolic modifiers with precise, objective phrasing.

- **[2026-03-10] 绝对化断言**
  - ❌ **Wrong**: “This proves that...”
  - ✅ **Right**: “These findings suggest... / The data indicates...”
  - 🔒 **Instruction**: Default to academic hedging; avoid absolute claims.

- **[2026-03-10] 僵尸名词（Nominalizations）**
  - ❌ **Wrong**: “perform an evaluation of...” 等 -tion/-ment/-ance 名词化堆砌
  - ✅ **Right**: 使用主动动词（evaluate, analyze, compare）
  - 🔒 **Instruction**: Prefer active verbs; reduce nominalizations.

- **[2026-03-10] 领域外隐喻/行话**
  - ❌ **Wrong**: “orthogonal” (物理/数学), “leverage” (商业), “ecosystem” (生物)
  - ✅ **Right**: 使用本领域等效词（independent, apply, system/environment）
  - 🔒 **Instruction**: Use plain English unless a term is defined in-domain.

- **[2026-03-10] 高频 AI 味词**
  - ❌ **Wrong**: delve / tapestry / testament / multifaceted / fosters / in summary / to summarize
  - ✅ **Right**: examine/investigate/explore/analyze；network/complex system/combination；demonstrates/highlights/shows；complex/varied/layered；promotes/encourages/builds；直接结论句
  - 🔒 **Instruction**: Search and replace these terms; delete rigid summary openers.

- **[2026-04-20] 松散模块并列叙事**
  - ❌ **Wrong**: 把方法写成互相割裂的 A+B+C 模块堆叠，缺少同一问题主线
  - ✅ **Right**: 以单一核心问题为轴，把各模块写成连续的 refinement / support chain
  - 🔒 **Instruction**: Prefer connected problem-to-solution narration over disconnected component listing.

- **[2026-04-20] 术语漂移**
  - ❌ **Wrong**: 为了避免重复频繁替换同一概念的术语，导致 reviewer 无法稳定映射
  - ✅ **Right**: 一个概念尽量固定一个主术语，必要时只保留清晰且受控的近义替换
  - 🔒 **Instruction**: Keep terminology stable across abstract, intro, method, figures, and experiments.

- **[2026-04-20] 无证据强结论**
  - ❌ **Wrong**: 使用 superior / significant / strong / effective 等结论词，但没有指标、实验或引用支撑
  - ✅ **Right**: 让数字、数据集、指标、设定或引用承担结论
  - 🔒 **Instruction**: Do not make strong claims without quantitative or cited support.

- **[2026-04-20] 技术表述脱离实现**
  - ❌ **Wrong**: 论文文字与代码实现、公式定义或实验设置不一致
  - ✅ **Right**: 关键机制、损失、变量和实验条件都应与真实实现对齐
  - 🔒 **Instruction**: Keep technical writing faithful to code, equations, and experiments.
