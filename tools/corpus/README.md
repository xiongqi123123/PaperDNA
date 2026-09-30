# 语料流水线

用来维护 skill 的写作规范：下载顶会论文 → 转文本 → 逐篇精读写笔记 → 汇总提炼成 `skills/paperdna/references/` 中的规范。skill 运行时用不到这里的任何文件。

语料放在 NAS 上，根目录默认是 `/Volumes/personal_folder/WorkTemp/vibepaper_skill/`（skill 仓库上一级的 `Temp` 是指向它的软链接），可用环境变量 `PAPERDNA_CORPUS` 覆盖。目录结构见 `config.py`。

当前语料：CVPR 2026 + ICCV 2025 共 1040 篇获奖、oral、highlight 论文，都已有精读笔记；另有 ECCV 2026、NeurIPS 2025、ICML 2026、ICLR 2026 的 PDF 与少量笔记。

## 步骤

所有命令在本目录下运行。

| 步骤 | 命令 | 产出 |
|---|---|---|
| 1. 抓会议数据 | `python3 fetch_sources.py` | `corpus/meta/raw/`：论文列表、摘要、开放获取页面 |
| 2. 选论文 | `python3 build_selection.py` | `corpus/meta/selection.json`：入选论文、级别、方向、PDF 地址 |
| 3. 下载 PDF | `python3 download.py direct`，同时运行 `python3 download.py arxiv`；两者结束后 `python3 download.py arxiv --all` 补漏，最后 `python3 download.py report` | `corpus/papers/` 与 `manifest.csv/json` |
| 4. 转文本 | `python3 extract_text.py`（需要 pymupdf） | `corpus/text/`：正文截到参考文献之前 |
| 5. 精读 | `python3 make_worklist.py CVPR2026`，把输出的 `{list, n}` 加上 `label` 作为参数运行 `workflows/close_reading.js` | `corpus/notes/<会议>/<级别>/*.md`，模板同 `skills/paperdna/templates/close_reading_note.md` |
| 6. 汇总预处理 | `python3 prep_synthesis.py CVPR2026 ICCV2025` | `synthesis/batches/`、`counts.json`、`stats.md` |
| 7. 汇总提炼 | 运行 `workflows/synthesis.js`（参数 `counts`、`base`、`stats`、`drafts`）与 `workflows/sections_synthesis.js`（参数 `base`、`n`、`out`、`repo`、`stats`） | `synthesis/drafts/`：叙事类型、摘要、引言、句式库、用词风格、取名；`synthesis/drafts/sections/`：正文各章节 |
| 8. 并入 skill | 审读草稿，核对引用的论文和数字，复制到 `skills/paperdna/references/`，把 `stats.md` 复制为 `skills/paperdna/references/corpus_stats.md` | |

工作流脚本在 Claude Code 里用 Workflow 工具运行，参数是 JSON（例如 `{"list": ".../CVPR2026.tsv", "n": 710, "label": "CVPR2026"}`）。

## 经验

- **OpenReview**（ICLR、ICML、NeurIPS）有浏览器验证，脚本下载不到 PDF，不要尝试绕过；`download.py` 会按标题去 arXiv 找，约 20% 找不到。arXiv API 要求请求间隔至少 3 秒，查询结果缓存在 `corpus/meta/arxiv_cache.json`。
- 网络下载用 curl，系统自带 Python 的 SSL 库较旧，长时间下载时容易断连。
- **一次只跑一个精读工作流**。六个会议同时跑（约 100 个并发 agent）会触发服务端限流；限流失败的 agent 有时已经写好了笔记，重新运行 `make_worklist.py` 只会列出真正缺笔记的论文。
- 精读用 Sonnet 即可，质量与 Opus 相当，每篇约 9 万 token；汇总的最终一步用默认模型。
- **每个 agent 提示词开头都要有"任务边界"说明**（三个工作流脚本里的 `GUARD`）。工作流子 agent 能看到对话中用户最新的请求，如果它和工作流任务不同，子 agent 会转而回应用户请求。曾有一次 26 个分批 agent 全部去检查仓库结构，整轮作废。
- 工作流参数不要内嵌大清单（会占满上下文），用清单文件路径 + 行号的方式让每个 agent 自己读取。
- 汇总草稿中引用的论文标题和数字要用脚本核对；最终汇总的 agent 能运行代码，"[重算]" 标注的数字是它从笔记原句重新统计的。
- 新年份：更新 `fetch_sources.py` 的 URL、`build_selection.py` 的奖项名单（AWARDS）和各会议的解析规则。
