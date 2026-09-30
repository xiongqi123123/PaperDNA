"""把精读笔记切分成汇总工作流的批次文件，并计算可程序化的统计（stats.md）。

用法: python3 prep_synthesis.py CVPR2026 ICCV2025        # 参与汇总的会议
输出到 paper_notes/_synthesis/：
  batches/d1_<故事类型>_NNN.md  叙事类型（一句话概括、Story 逻辑、引言小结、全文递进）
  batches/d2a_abs_NNN.md        摘要逐句（§3）          batches/d2b_intro_NNN.md  引言（§4）
  batches/d3a_tpl_NNN.md        句式模板（§6）          batches/d3b_style_NNN.md  用词、风格、借鉴、不足（§7–§10）
  batches/d4_names_NNN.md       标题 + 方法名引入句      batches/d5_body_NNN.md    全文递进（§5，用于正文各章节）
  counts.json                   各类批次数（workflows/synthesis.js 与 sections_synthesis.js 的参数）
  stats.md                      统计（故事类型、贡献类型、摘要句数与作用序列、引言段数等）
"""
import json, re, collections, statistics, sys

from config import NOTES as N, SYNTH as S

CONFS = sys.argv[1:] or ['CVPR2026', 'ICCV2025']
B = S / 'batches'
B.mkdir(parents=True, exist_ok=True); (S / 'drafts').mkdir(exist_ok=True)

ROLES = ['背景', '问题', '缺口', '根因', '洞察', '方法', '设计细节', '结果', '泛化', '意义', '资源发布']
STORY = ['瓶颈突破型', '统一框架型', '新问题定义型', '发现-解释型', '数据与基准型', '能力扩展型', '效率优化型', '理论分析型']


def field(t, k):
    m = re.search(rf'^{k}:\s*"?(.*?)"?\s*$', t, re.M)
    return m.group(1).strip() if m else ''


notes = []
for conf in CONFS:
    for m in sorted((N / conf).rglob('*.md')):
        t = m.read_text(encoding='utf-8', errors='ignore')
        parts = re.split(r'^## (\d+)\.', t, flags=re.M)
        sec = {parts[i]: '## ' + parts[i] + '.' + parts[i + 1] for i in range(1, len(parts), 2)}
        st = field(t, 'story_type').split('/')[0].split('（')[0].strip()
        st = next((s for s in STORY if s in st), st)
        # 摘要逐句作用序列：解析 §3 表格第 3 列
        seq = []
        for row in re.findall(r'^\|\s*\d+\s*\|(.*)$', sec.get('3', ''), re.M):
            cols = row.split('|')
            if len(cols) >= 2:
                labs = [r for r in ROLES if r in cols[1]]
                seq.append('+'.join(labs) if labs else '其他')
        notes.append(dict(file=str(m.relative_to(N)), title=field(t, 'title'), conf=conf, tier=m.parent.name,
                          topic=field(t, 'topic'), story=st, contrib=field(t, 'contribution_type').replace(' ', ''),
                          abs_n=field(t, 'abs_sentences'), intro_n=field(t, 'intro_paragraphs'),
                          teaser=field(t, 'has_teaser_figure'), clist=field(t, 'contribution_list'), seq=seq, sec=sec))


def head(n):
    return f"### 《{n['title']}》（{n['conf']} {n['tier']}，方向 {n['topic']}，故事类型 {n['story']}）\n"


def write_batches(name, items, per, build):
    paths = []
    for k in range(0, len(items), per):
        p = B / f'{name}_{k // per + 1:03d}.md'
        p.write_text('\n\n---\n\n'.join(build(n) for n in items[k:k + per]), encoding='utf-8')
        paths.append(str(p))
    return paths


plan = {}
# 方向 1：按故事类型分组，每批 25 篇；取一句话概括、Story 逻辑、引言小结、全文递进结构
d1 = {}
for s in STORY:
    grp = [n for n in notes if n['story'] == s]
    d1[s] = write_batches(f'd1_{s}', grp, 25, lambda n: head(n) + n['sec'].get('1', '') + n['sec'].get('2', '')
                          + (re.search(r'### 4\.3.*', n['sec'].get('4', ''), re.S).group(0) if '### 4.3' in n['sec'].get('4', '') else '')
                          + n['sec'].get('5', ''))
plan['d1'] = d1
# 方向 2a：摘要逐句（§3），每批 30 篇；2b：引言（§4），每批 8 篇
plan['d2a'] = write_batches('d2a_abs', notes, 30, lambda n: head(n) + n['sec'].get('3', ''))
plan['d2b'] = write_batches('d2b_intro', notes, 8, lambda n: head(n) + n['sec'].get('4', ''))
# 方向 3a：句式模板（§6），每批 25 篇；3b：用词、风格、可借鉴、不足（§7–§10），每批 20 篇
plan['d3a'] = write_batches('d3a_tpl', notes, 25, lambda n: head(n) + n['sec'].get('6', ''))
plan['d3b'] = write_batches('d3b_style', notes, 20, lambda n: head(n) + ''.join(n['sec'].get(k, '') for k in '7 8 9 10'.split()))
json.dump(plan, open(S / 'plan.json', 'w'), ensure_ascii=False, indent=1)

# ---------- 统计 ----------
C = collections.Counter
out = [f'# {len(notes)} 篇精读笔记统计（{" + ".join(CONFS)}）\n']
def table(title, cnt, total=None, top=None):
    total = total or sum(cnt.values())
    out.append(f'## {title}\n\n| 取值 | 篇数 | 占比 |\n|---|---|---|')
    for k, v in cnt.most_common(top):
        out.append(f'| {k or "（空）"} | {v} | {v / total:.1%} |')
    out.append('')

table('故事类型', C(n['story'] for n in notes))
for tp in ['autonomous_driving', 'embodied', 'cv']:
    table(f'故事类型 — 方向 {tp}', C(n['story'] for n in notes if n['topic'] == tp))
for tr in ['best', 'oral', 'highlight']:
    table(f'故事类型 — 级别 {tr}', C(n['story'] for n in notes if n['tier'] == tr))
table('贡献类型组合', C(n['contrib'] for n in notes))
table('贡献列表形式', C(n['clist'] for n in notes))
table('第一页或引言中有 teaser 图（Figure 1）', C(n['teaser'] for n in notes))
for key, name in [('abs_n', '摘要句数'), ('intro_n', '引言段数')]:
    vals = [int(n[key]) for n in notes if n[key].isdigit()]
    out.append(f'## {name}\n\n中位数 {statistics.median(vals)}，四分位 {statistics.quantiles(vals, n=4)}，最小 {min(vals)}，最大 {max(vals)}\n')
    table(f'{name}分布', C(str(v) for v in vals))
# 摘要作用序列
seqs = [n['seq'] for n in notes if n['seq']]
table('摘要第 1 句的作用', C(s[0] for s in seqs))
table('摘要最后 1 句的作用', C(s[-1] for s in seqs))
prim = lambda r: r.split('+')[0]
compress = lambda s: ' → '.join(k for i, k in enumerate(map(prim, s)) if i == 0 or k != prim(s[i - 1]))
table('摘要作用序列（取每句主作用并合并相邻重复，前 30 种）', C(compress(s) for s in seqs), top=30)
pos = collections.defaultdict(C)
for s in seqs:
    L = len(s)
    for i, r in enumerate(s):
        pos[min(4, int(5 * i / L))][prim(r)] += 1
out.append('## 摘要各位置的主作用分布（把摘要等分为 5 段）\n\n| 位置 | 前三名作用 |\n|---|---|')
for k in range(5):
    tot = sum(pos[k].values())
    out.append(f'| 第 {k + 1}/5 段 | ' + '，'.join(f'{r} {v / tot:.0%}' for r, v in pos[k].most_common(3)) + ' |')
(S / 'stats.md').write_text('\n'.join(out), encoding='utf-8')
print('batches:', {k: (sum(len(v) for v in plan[k].values()) if isinstance(plan[k], dict) else len(plan[k])) for k in plan})
print({s: len(v) for s, v in d1.items()})

# 取名：标题 + 摘要或引言中首次引入方法名的句子，每批 260 篇
INTRO_RE = re.compile(r'\b(we (propose|introduce|present|develop|call|dub|term|name)|called|dubbed|named|termed|coined)\b', re.I)
rows = []
for n in notes:
    body = n['sec'].get('3', '') + n['sec'].get('4', '')
    sents = [r.split('|')[0].strip() for r in re.findall(r'^\|\s*\d+\s*\|(.*)$', body, re.M)]
    name_sent = next((x for x in sents if INTRO_RE.search(x)), '')
    rows.append(f"- [{n['conf']} {n['tier']} | {n['topic']} | {n['story']}] {n['title']}\n  - 方法名引入句：{name_sent[:400] or '（未找到）'}")
d4 = 0
for i in range(0, len(rows), 260):
    d4 += 1
    (B / f'd4_names_{d4:03d}.md').write_text('\n'.join(rows[i:i + 260]), encoding='utf-8')
# 正文各章节：全文递进（§5），每批 40 篇
d5 = write_batches('d5_body', notes, 40, lambda n: head(n) + n['sec'].get('5', ''))
counts = {'d1': {k: len(v) for k, v in d1.items()}, **{k: len(plan[k]) for k in ['d2a', 'd2b', 'd3a', 'd3b']}, 'd4': d4, 'd5': len(d5)}
json.dump(counts, open(S / 'counts.json', 'w'), ensure_ascii=False)
print('counts:', json.dumps(counts, ensure_ascii=False))
