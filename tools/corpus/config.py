"""语料流水线的路径配置。语料很大，放在 NAS 上；用环境变量 PAPERDNA_CORPUS 覆盖根目录。"""
import os
from pathlib import Path

ROOT = Path(os.environ.get('PAPERDNA_CORPUS', '/Volumes/personal_folder/Paper/Temp/vibepaper'))
META = ROOT / '_meta'                 # 会议原始数据、论文选择结果、arXiv 查询缓存
RAW = META / 'raw'                    # fetch_sources.py 抓下来的会议页面与 JSON
SELECTION = META / 'selection.json'   # build_selection.py 的输出：入选论文及 PDF 地址
ARXIV_CACHE = META / 'arxiv_cache.json'
PAPERS = ROOT / 'topconf_papers'      # PDF：<会议>/<best|oral|highlight|spotlight>/<标题>.pdf，另有 manifest.csv/json
TEXT = ROOT / 'paper_text'            # extract_text.py 的输出：正文文本（截到参考文献之前）
NOTES = ROOT / 'paper_notes'          # 精读笔记：与 PDF 同名的 .md
LISTS = NOTES / '_lists'              # 精读工作流读取的待读清单 TSV
SYNTH = NOTES / '_synthesis'          # 汇总提炼：batches/、drafts/、stats.md
