"""抓取会议的论文列表、摘要和开放获取页面，存到 corpus/meta/raw/。已存在的文件跳过（加 --force 重新抓）。

各会议网站（CVPR/ICCV/ECCV/NeurIPS/ICML/ICLR）用同一套 MiniConf 系统：
    https://<站点>/static/virtual/data/<会议>-<年份>-orals-posters.json   论文列表，含 decision、eventtype、PDF/OpenReview 链接
    https://<站点>/static/virtual/data/<会议>-<年份>-abstracts.json       摘要（按论文 id）
CVF 会议（CVPR/ICCV）的 PDF 在 openaccess.thecvf.com；CVPR 的 JSON 只返回前 200 条，
oral 与 highlight 名单改从虚拟会场页面解析。新增会议时，在 SOURCES 里加几行，并在 build_selection.py 里写对应的解析逻辑。

注意：OpenReview 有浏览器验证，脚本拿不到 PDF；OpenReview 系会议（ICLR/ICML/NeurIPS）的 PDF 由 download.py 从 arXiv 找。
"""
import subprocess
import sys

from config import RAW

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
SOURCES = {
    # CVPR 2026
    'cvpr_oa.html': 'https://openaccess.thecvf.com/CVPR2026?day=all',
    'cvpr_abs.json': 'https://cvpr.thecvf.com/static/virtual/data/cvpr-2026-abstracts.json',
    'cv_virtual_2026_papers.html': 'https://cvpr.thecvf.com/virtual/2026/papers.html',
    'cv_virtual_2026_events_oral': 'https://cvpr.thecvf.com/virtual/2026/events/oral',
    'cv_highlights.html': 'https://cvpr.thecvf.com/virtual/2026/events/Highlights2026',
    # ICCV 2025
    'iccv2025.json': 'https://iccv.thecvf.com/static/virtual/data/iccv-2025-orals-posters.json',
    'iccv_oa.html': 'https://openaccess.thecvf.com/ICCV2025?day=all',
    # ECCV 2026
    'eccv2026.json': 'https://eccv.ecva.net/static/virtual/data/eccv-2026-orals-posters.json',
    'eccv-abs.json': 'https://eccv.ecva.net/static/virtual/data/eccv-2026-abstracts.json',
    # ICML 2026 / ICLR 2026 / NeurIPS 2025
    'icml2026.json': 'https://icml.cc/static/virtual/data/icml-2026-orals-posters.json',
    'icml-abs.json': 'https://icml.cc/static/virtual/data/icml-2026-abstracts.json',
    'iclr2026.json': 'https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json',
    'iclr-abs.json': 'https://iclr.cc/static/virtual/data/iclr-2026-abstracts.json',
    'neurips2025.json': 'https://neurips.cc/static/virtual/data/neurips-2025-orals-posters.json',
}


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    force = '--force' in sys.argv
    for name, url in SOURCES.items():
        dest = RAW / name
        if dest.exists() and not force:
            print(f'跳过 {name}（已存在）')
            continue
        r = subprocess.run(['curl', '-sfL', '--retry', '3', '--max-time', '180', '-A', UA, '-o', str(dest), url])
        print(f"{'OK  ' if r.returncode == 0 else 'FAIL'} {name}  {url}")


if __name__ == '__main__':
    main()
