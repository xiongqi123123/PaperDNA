import gradio as gr
import subprocess
import os
import shutil

def process_pdf(pdf_file):
    if pdf_file is None:
        return "请先上传 PDF 文件。"

    # 获取上传文件的路径
    pdf_path = pdf_file.name
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_dir = os.path.join(os.getcwd(), "mineru_output", base_name)
    
    # 确保输出目录存在且清空旧数据
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # 构建 MinerU (magic-pdf) 命令行指令
    # -m auto 强制使用模型解析，保证高精度排版
    # 使用绝对路径确保调用正确环境中的 magic-pdf
    magic_pdf_cmd = os.path.join(os.getcwd(), "mineru_venv", "bin", "magic-pdf")
    if not os.path.exists(magic_pdf_cmd):
        magic_pdf_cmd = "magic-pdf" # fallback

    command = [
        magic_pdf_cmd,
        "-p", pdf_path,
        "-o", output_dir,
        "-m", "auto"
    ]

    try:
        # 执行命令
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # 寻找生成的 Markdown 文件
        md_file_path = None
        for file in os.listdir(output_dir):
            if file.endswith(".md"):
                md_file_path = os.path.join(output_dir, file)
                break
        
        if md_file_path:
            with open(md_file_path, "r", encoding="utf-8") as f:
                md_content = f.read()
            return f"✅ 解析成功！输出目录: {output_dir}\n\n### 预览内容:\n{md_content[:2000]}...\n\n(由于篇幅限制，仅展示前 2000 字符，完整内容请查看输出目录)"
        else:
            return f"⚠️ 解析完成，但未找到 Markdown 文件。控制台输出:\n{result.stdout}"

    except subprocess.CalledProcessError as e:
        return f"❌ 解析失败！请检查 MinerU 是否安装并配置正确。\n错误信息:\n{e.stderr}\n\n标准输出:\n{e.stdout}"

# 构建 Gradio 可视化界面
with gr.Blocks(title="MinerU 高精度 PDF 解析器") as app:
    gr.Markdown("## 📄 MinerU 本地高精度 PDF 解析器")
    gr.Markdown("基于 OpenDataLab MinerU，强制使用深度学习模型进行版面分析，保留作者、公式与表格布局。")
    
    with gr.Row():
        with gr.Column():
            pdf_input = gr.File(label="拖拽或点击上传 PDF 文件", file_types=[".pdf"])
            submit_btn = gr.Button("开始高精度解析", variant="primary")
        
        with gr.Column():
            output_text = gr.Markdown(label="解析结果预览")

    submit_btn.click(
        fn=process_pdf,
        inputs=[pdf_input],
        outputs=[output_text]
    )

if __name__ == "__main__":
    # 确保安装了 gradio: pip install gradio
    print("正在启动可视化界面，请在浏览器中打开提供的本地链接...")
    app.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
