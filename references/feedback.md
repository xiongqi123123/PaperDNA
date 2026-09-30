# 处理用户纠正

用户指出某处写得不对时，按以下顺序处理：

1. 判断这条纠正属于哪一类。
2. 写入对应的文件。
3. 按新规则改写刚才的文本。
4. 用一句话告诉用户记在了哪里。

| 纠正类型 | 例子 | 写入 |
|---|---|---|
| 措辞、语气、句式偏好 | "不要用 In summary"、"我习惯用 we，不用被动" | 在 `profile/error_log.md` 新增一条 |
| 新的 AI 味词 | "以后别用 intricate" | 在个人补充词表 `profile/ai_words.json` 加一条（格式同 `references/ai_words.json`，扫描脚本通过 `--extra` 读取），不必再写进 error_log。只有在维护 PaperDNA 仓库本身、要让所有用户生效时，才改 `references/ai_words.json` |
| 本篇论文的事实、术语、口径 | "我们的方法叫 X，不叫 Y"、"数据集用的是 v2 版" | `.paperdna/spec.md` 的术语表或决策记录 |
| 跨论文通用的术语、译法、单位 | "Bioimpedance 统一译为生物阻抗" | `profile/glossary.md` |
| 章节写法或论证方法 | "Related work 要按技术路线分组" | 对应的 `references/sections/*.md`，跨章节的原则写入 `references/word_style.md` 第 1 节。改之前先问用户 |
| 只针对这一处的修改 | "这句删掉" | 不记录 |

判断不了是否通用时，问用户："以后都这样，还是只改这一处？"

## error_log 条目格式

```
- **[YYYY-MM-DD] 错误类型**
  - ❌ Wrong: 刚才的写法
  - ✅ Right: 用户要的写法
  - 🔒 Instruction: 给以后的具体指令，要能检查，例如 "Never start a paragraph with 'Basically'"
```

## 维护

- error_log 中同一类条目积累到 3 条以上，或者某条已经稳定成为习惯时，建议用户把它合并进 `profile/style_profile.md`，并从 error_log 中删掉原条目。
- 发现两个文件中的规则互相冲突时，指出冲突并问用户，不要自行取舍。
