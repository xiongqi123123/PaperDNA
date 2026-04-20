# 本地 AI 风格检测方案 (Local AI Style Check)

本目录包含一套完全离线运行的学术论文 AI 痕迹检测工具，专为 LaTeX 源码设计。

## 🌟 功能特点
1. **完全离线**: 模型权重下载后本地运行，无需联网，保护论文隐私。
2. **LaTeX 深度清洗**: 内置双重清洗机制（正则 + AST 解析），完美剥离引用、公式、注释，只检测正文。
3. **中英文双语检测**:
   - 英文: 检测 "delve", "tapestry" 等 20+ 高频 AI 词汇。
   - 中文: 检测 "赋能", "重塑", "旨在" 等 20+ 高频 AI 词汇。
4. **困惑度 (PPL) 分析**: 使用 distilgpt2 模型计算文本困惑度，判断文本生成概率。

## 🚀 快速开始

### 1. 环境安装
确保 Python 3.8+，并安装依赖：
```bash
pip install -r requirements.txt
```

### 2. 运行检测脚本
```bash
python paper_ai_detector.py
```
首次运行会自动下载模型（约 300MB），之后即可离线使用。

### 3. 检测你的论文
打开 `paper_ai_detector.py`，取消底部的注释并修改路径：
```python
# 实际使用时，请取消下面两行的注释，并将 "./" 替换为你论文所在的绝对路径
folder_to_scan = "/path/to/your/latex/project"
detector.batch_process(folder_to_scan)
```
脚本会自动扫描该目录下所有的 `.tex` 文件。

## 📊 结果解读
- **高频词汇**: 出现 AI 惯用词汇（如 "delve", "paradigm shift", "值得注意的是"）。
- **PPL < 30**: 🚨 极高 AI 嫌疑（文本过于平滑，缺乏人类的随机性）。
- **30 < PPL < 55**: 🤔 存在润色痕迹。
- **PPL > 55**: ✅ 大概率为人类撰写。
