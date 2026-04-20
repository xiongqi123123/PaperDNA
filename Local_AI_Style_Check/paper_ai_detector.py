import os
import re
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from pylatexenc.latex2text import LatexNodes2Text

class LocalPaperDetector:
    def __init__(self, model_id="distilgpt2"):
        print(f"[*] 初始化本地模型 '{model_id}' (首次运行会自动下载，后续完全离线)...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = GPT2TokenizerFast.from_pretrained(model_id)
        self.model = GPT2LMHeadModel.from_pretrained(model_id).to(self.device)
        self.model.eval()
        print(f"[*] 模型已加载至设备: {self.device}")
        
        # 英文高频词正则库 (English AI Buzzwords)
        self.ai_buzzwords_en = [
            r"\bdelve(?:s|d)?\b", r"\btapestry\b", r"\blandscape\b", r"\bunderscore(?:s|d)?\b",
            r"\bcrucial\b", r"\bparadigm shift\b", r"\bnuanced\b", r"\btestament\b",
            r"\bnavigat(?:e|ing)\b", r"\brobust\b", r"\bdemystify\b", r"\bpivotal\b",
            r"\bintricate\b", r"\bseamless(?:ly)?\b", r"\bcornerstone\b", r"\bparamount\b",
            r"\bsynergy\b", r"\bvital\b", r"\bunprecedented\b", r"\bshed light on\b"
        ]

        # 中文高频词正则库 (Chinese AI Buzzwords)
        # 根据用户提供的高频词正则补充：(毋庸置疑|不可否认的是|值得注意的是|综上所述|在.*?的背景下|旨在|深入探讨|凸显了|赋能|重塑|彰显|鲁棒|显著的|前所未有的|错综复杂的|全面的|画卷|织锦|里程碑|双刃剑|基石)
        self.ai_buzzwords_cn = [
            r"毋庸置疑", r"不可否认的是", r"值得注意的是", r"综上所述", r"在.*?的背景下", r"旨在", 
            r"深入探讨", r"凸显了", r"赋能", r"重塑", r"彰显", r"鲁棒", r"显著的", 
            r"前所未有的", r"错综复杂的", r"全面的", r"画卷", r"织锦", r"里程碑", r"双刃剑", r"基石"
        ]

    def clean_latex(self, tex_content):
        """清洗 LaTeX 源码，极度激进地剔除公式、引用和格式标签"""
        # 1. 移除所有注释
        text = re.sub(r'(?m)%.*$', '', tex_content)
        
        # 2. 正则预处理：暴力删除 cite, ref, label, eqref, autoref
        text = re.sub(r'\\(?:cite|ref|label|eqref|autoref)\{.*?\}', '', text)
        
        # 3. 正则预处理：暴力删除常见的数学环境和行内公式
        text = re.sub(r'\\begin\{equation\}.*?\\end\{equation\}', '', text, flags=re.DOTALL)
        text = re.sub(r'\\begin\{align\}.*?\\end\{align\}', '', text, flags=re.DOTALL)
        text = re.sub(r'\$.*?\$', '', text) # 行内公式 $...$
        text = re.sub(r'\\\+.*?\\\]', '', text, flags=re.DOTALL) # 块公式 \[...\]

        # 4. 使用 pylatexenc 进行深度解析，剥离剩余的格式标签 (如 \textbf, \textit)
        try:
            plain_text = LatexNodes2Text(math_mode='remove').latex_to_text(text)
        except Exception as e:
            print(f"  [警告] LaTeX 深度解析遇到语法错误，回退到基础正则模式。详情: {e}")
            plain_text = text

        # 5. 清理多余的空格和换行
        plain_text = re.sub(r'\s+', ' ', plain_text).strip()
        return plain_text

    def scan_buzzwords(self, text):
        """扫描高频词 (中英文)"""
        found_words = []
        
        # 扫描英文
        for pattern in self.ai_buzzwords_en:
            matches = re.findall(pattern, text, flags=re.IGNORECASE)
            if matches:
                found_words.extend([m.lower() for m in matches])
        
        # 扫描中文
        for pattern in self.ai_buzzwords_cn:
            matches = re.findall(pattern, text)
            if matches:
                found_words.extend(matches)
                
        return list(set(found_words))

    def calculate_perplexity(self, text):
        """计算文本困惑度 (PPL)"""
        # 过滤掉太短的片段 (如标题、作者列表)，这些算 PPL 没有意义
        if len(text.split()) < 30:
            return None

        encodings = self.tokenizer(text, return_tensors="pt").to(self.device)
        max_length = self.model.config.n_positions
        stride = 512
        seq_len = encodings.input_ids.size(1)

        nlls = []
        prev_end_loc = 0
        for begin_loc in range(0, seq_len, stride):
            end_loc = min(begin_loc + max_length, seq_len)
            trg_len = end_loc - prev_end_loc
            input_ids = encodings.input_ids[:, begin_loc:end_loc]
            target_ids = input_ids.clone()
            target_ids[:, :-trg_len] = -100

            with torch.no_grad():
                outputs = self.model(input_ids, labels=target_ids)
                neg_log_likelihood = outputs.loss

            nlls.append(neg_log_likelihood)
            prev_end_loc = end_loc
            if end_loc == seq_len:
                break

        if not nlls:
            return 0.0
            
        ppl = torch.exp(torch.stack(nlls).mean())
        return ppl.item()

    def process_file(self, filepath):
        """处理单个 .tex 文件"""
        filename = os.path.basename(filepath)
        print("\n" + "-"*60)
        print(f"📄 正在分析: {filename}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                raw_tex = f.read()
        except Exception as e:
            print(f"  [错误] 无法读取文件: {e}")
            return

        # 执行 LaTeX 清洗
        clean_text = self.clean_latex(raw_tex)
        
        if not clean_text or len(clean_text.split()) < 30:
            print("  [跳过] 剔除代码和公式后，剩余有效文本过短。")
            return

        buzzwords = self.scan_buzzwords(clean_text)
        ppl = self.calculate_perplexity(clean_text)

        # 打印词汇报告
        if buzzwords:
            print(f"  ⚠️  [高频词汇] 发现了 {len(buzzwords)} 个典型 AI 词汇: {', '.join(buzzwords)}")
        else:
            print("  ✅  [高频词汇] 干净。未发现明显 AI 套话。")

        # 打印 PPL 报告
        if ppl is not None:
            print(f"  📊  [困惑度 PPL] 得分: {ppl:.2f}")
            if ppl < 30:
                print("  🚨  [综合判定] AI 生成概率极高 (文本可预测性强，缺乏人类长短句节奏)。")
            elif ppl < 55:
                print("  🤔  [综合判定] 存在润色痕迹 (包含典型的 AI 句式结构)。")
            else:
                print("  ✅  [综合判定] 大概率为人类撰写 (用词具有跳跃性和多样性)。")

    def batch_process(self, folder_path):
        """批量处理文件夹"""
        print(f"\n[*] 扫描目录: {folder_path}")
        tex_files = [f for f in os.listdir(folder_path) if f.endswith('.tex')]
        
        if not tex_files:
            print("未找到任何 .tex 文件。")
            return
            
        print(f"共找到 {len(tex_files)} 个 .tex 文件，开始逐一检测...")
        for file in tex_files:
            self.process_file(os.path.join(folder_path, file))
        print("\n" + "="*60)
        print("[*] 批量检测完成。")

if __name__ == "__main__":
    detector = LocalPaperDetector()

    # 【测试演示】内置一段带 LaTeX 标签的学术摘要
    test_tex = r"""
    \section{Introduction}
    % This is a comment that should be removed
    In the rapidly evolving landscape of continuous cerebrovascular health monitoring, leveraging wireless sensing technologies is paramount \cite{wang2025}.
    This paper delves into the intricate mechanisms of wearable bioimpedance sensors. It is crucial to underscore that robust data collection
    forms the cornerstone of our proposed system, especially for managing conditions like TIA. Furthermore, navigating the complexities of
    24-hour monitoring offers a paradigm shift in pervasive healthcare \ref{fig:architecture}.
    
    \begin{equation}
    Z = \sqrt{R^2 + (X_L - X_C)^2}
    \end{equation}
    
    As shown in Equation 1, the impedance is calculated seamlessly.
    值得注意的是，本研究旨在通过重塑现有的框架来赋能医疗健康。
    """
    
    print("\n>>> 开始运行自测试模块 (解析一段包含引用、公式的 LaTeX 文本)...")
    clean_test_text = detector.clean_latex(test_tex)
    print(f"\n[清洗后的纯文本预览]:\n{clean_test_text}\n")
    
    buzzwords = detector.scan_buzzwords(clean_test_text)
    ppl = detector.calculate_perplexity(clean_test_text)
    print(f"高频词汇: {buzzwords}")
    print(f"PPL 得分: {ppl:.2f}")
    
    # ---------------------------------------------------------
    # 实际使用时，请取消下面两行的注释，并将 "./" 替换为你论文所在的绝对路径
    # folder_to_scan = "./"
    # detector.batch_process(folder_to_scan)
    # ---------------------------------------------------------
