"""为某个会议生成精读工作流的待读清单 TSV（跳过已有完整笔记的论文；获奖与 oral 排在前面）。

用法: python3 make_worklist.py CVPR2026
输出一行 JSON：{"list": 清单路径, "n": 篇数}，把它作为 workflows/close_reading.js 的 args（再加 "label"）。
清单每行 9 列（制表符分隔）：序号、PDF、正文文本、笔记输出路径、会议、级别、奖项（"-" 表示无）、方向、标题。
"""
import json
import sys
from pathlib import Path

from config import LISTS, NOTES, PAPERS, TEXT

REQUIRED = ['## 3. 摘要逐句分析', '## 4. 引言分析', '## 6. 句式模板', '## 10.']


def complete(md):
    try:
        t = md.read_text(encoding='utf-8')
    except OSError:
        return False
    return t.startswith('---') and all(h in t for h in REQUIRED)


def main():
    conf = sys.argv[1]
    items = []
    for p in json.load(open(PAPERS / 'manifest.json')):
        if p['status'] != 'ok' or p['conf'] != conf:
            continue
        md = NOTES / Path(p['file']).with_suffix('.md')
        if complete(md):
            continue
        md.parent.mkdir(parents=True, exist_ok=True)
        items.append(dict(pdf=str(PAPERS / p['file']), txt=str((TEXT / p['file']).with_suffix('.txt')), md=str(md),
                          conf=p['conf'], tier=p['tier_label'], award=p.get('award') or '-', topic=p['topic'], title=p['title']))
    order = {'best': 0, 'oral': 1}
    items.sort(key=lambda x: (order.get(x['tier'], 2), x['md']))

    LISTS.mkdir(parents=True, exist_ok=True)
    path = LISTS / f'{conf}.tsv'
    with open(path, 'w', encoding='utf-8') as f:
        for i, x in enumerate(items, 1):
            f.write('\t'.join([str(i), x['pdf'], x['txt'], x['md'], x['conf'], x['tier'], x['award'], x['topic'], x['title']]) + '\n')
    print(json.dumps({'list': str(path), 'n': len(items)}, ensure_ascii=False))
    print(f'{conf}: 待精读 {len(items)} 篇', file=sys.stderr)


if __name__ == '__main__':
    main()
