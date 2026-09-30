"""把 topconf_papers 下所有 PDF 转成文本（正文到参考文献为止），存到 paper_text/ 同名 .txt。"""
import json, re, sys
from multiprocessing import Pool
from pathlib import Path
import pymupdf

from config import PAPERS as O, TEXT as T
REF_RE = re.compile(r'^\s*(?:\d+\.?\s*)?(References|REFERENCES|Bibliography)\s*$', re.M)

def extract(rel):
    src, dst = O/rel, (T/rel).with_suffix('.txt')
    if dst.exists() and dst.stat().st_size > 2000:
        return rel, 'skip', 0
    try:
        doc = pymupdf.open(src)
        pages = [f'=== Page {i + 1} ===\n' + p.get_text('text', flags=pymupdf.TEXT_DEHYPHENATE) for i, p in enumerate(doc)]
        text = '\n'.join(pages)
        # 在全文 30% 之后找第一个"References"标题，之后（参考文献与附录）截掉
        m = next((m for m in REF_RE.finditer(text) if m.start() > len(text) * 0.3), None)
        if m:
            text = text[:m.start()] + '\n=== 参考文献及之后的内容已省略 ===\n'
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding='utf-8')
        return rel, 'ok' if len(text) > 5000 else 'short', len(text)
    except Exception as e:
        return rel, f'error: {e}', 0

if __name__ == '__main__':
    rels = [p['file'] for p in json.load(open(O/'manifest.json')) if p['status'] == 'ok']
    with Pool(8) as pool:
        res = pool.map(extract, rels, chunksize=8)
    from collections import Counter
    print(Counter(r[1].split(':')[0] for r in res))
    print('short/error:', [(r[0], r[1]) for r in res if r[1] not in ('ok', 'skip')][:20])
    sizes = sorted(r[2] for r in res if r[2])
    print('chars median', sizes[len(sizes)//2], 'p90', sizes[int(len(sizes)*.9)], 'max', sizes[-1])
