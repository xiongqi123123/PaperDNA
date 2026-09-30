"""从 _meta/raw/ 的会议数据中选出 best / oral / highlight(spotlight) 论文，按标题和摘要分类主题（自动驾驶、具身、LLM、CV），
解析 PDF 地址，输出 _meta/selection.json。

奖项名单（AWARDS）来自各会议官方公告，需要每年手动更新。选择规则见文件末尾"分类与筛选"：
视觉会议全收；ML 会议只收 CV、自动驾驶、具身方向，LLM 只收 oral。
"""
import difflib
import html
import unicodedata
import json
import re
from collections import Counter

from config import RAW, SELECTION

D = str(RAW) + "/"


def norm(t):
    t = unicodedata.normalize("NFKD", html.unescape(t or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", t)


def fuzzy_get(idx, n, cutoff=0.9):
    """精确匹配失败时按相似度匹配标题（处理连字符、特殊字符差异）。"""
    if n in idx:
        return idx[n]
    m = difflib.get_close_matches(n, idx.keys(), n=1, cutoff=cutoff)
    return idx[m[0]] if m else None


def acronym_get(idx_titles, title):
    """标题在 camera-ready 中改过时，按冒号前的方法名（至少 5 个字符）唯一匹配。"""
    head = title.split(":")[0].strip()
    if ":" not in title or len(head) < 5:
        return None
    hits = [pdf for t, pdf in idx_titles if t.split(":")[0].strip().lower() == head.lower()]
    return hits[0] if len(hits) == 1 else None


def load(f):
    return json.load(open(D + f))


OA_TITLES = {}


def oa_index(fname, base):
    t = open(D + fname).read()
    idx = {}
    for href, title in re.findall(r'<dt class="ptitle"><br><a href="([^"]+)">(.*?)</a></dt>', t, re.S):
        pdf = href.replace("/html/", "/papers/").replace(".html", ".pdf")
        idx[norm(title)] = base + pdf
        OA_TITLES.setdefault(fname, []).append((html.unescape(title), base + pdf))
    return idx


AWARDS = {
    "CVPR2026": {
        "Efficiently Reconstructing Dynamic Scenes One D4RT at a Time": "Best Paper",
        "Native and Compact Structured Latents for 3D Generation": "Best Student Paper",
        "NitroGen: An Open Foundation Model for Generalist Gaming Agents": "Best Paper Honorable Mention",
        "SAM 3D: 3Dfy Anything in Images": "Best Paper Honorable Mention",
        "ChordEdit: One-Step Low-Energy Transport for Image Editing": "Best Student Paper Honorable Mention",
    },
    "ICCV2025": {
        "Generating Physically Stable and Buildable Brick Structures from Text": "Best Paper (Marr Prize)",
        "FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models": "Best Student Paper",
        "Spatially-Varying Autofocus": "Best Paper Honorable Mention",
        "RayZer: A Self-supervised Large View Synthesis Model": "Best Paper Honorable Mention",
    },
    "ICML2026": {
        "The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models": "Outstanding Paper",
        "High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions": "Outstanding Paper",
        "Position: The Alignment Community is Unintentionally Building a Censor's Toolkit": "Outstanding Position Paper",
        "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes": "Honorable Mention",
        "Motion Attribution for Video Generation": "Honorable Mention",
        "How much can language models memorize?": "Honorable Mention",
        "A Random Matrix Perspective on the Consistency of Diffusion Models": "Honorable Mention",
        "To Grok Grokking: Provable Grokking in Ridge Regression": "Honorable Mention",
        "Position: AI/ML Deepfake Research is Misaligned with AI Generated Non-Consensual Intimate Imagery (AIG-NCII)": "Position Paper Honorable Mention",
    },
    "ICLR2026": {
        "Transformers are Inherently Succinct": "Outstanding Paper",
        "LLMs Get Lost In Multi-Turn Conversation": "Outstanding Paper",
        "The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm": "Honorable Mention",
    },
    "NeurIPS2025": {
        "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)": "Best Paper (D&B)",
        "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free": "Best Paper",
        "1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities": "Best Paper",
        "Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training": "Best Paper",
        "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?": "Runner-up",
        "Optimal Mistake Bounds for Transductive Online Learning": "Runner-up",
        "Superposition Yields Robust Neural Scaling": "Runner-up",
    },
}

# ---------- 主题分类 ----------
RE_DRIVING = re.compile(
    r"autonomous driving|self-driving|\bdriving\b|autonomous vehicle|\bvehicles?\b|\btraffic\b|lidar|nuscenes|waymo|carla\b|"
    r"\bbev\b|bird'?s[- ]eye|occupancy|motion forecasting|trajectory prediction|\blanes?\b|pedestrian|\bradar\b|argoverse|kitti|nuplan|navsim",
    re.I)
RE_EMBODIED = re.compile(
    r"embodied|\brobots?\b|robotic|vision-language-action|\bvlas?\b|humanoid|locomotion|dexterous|grasp|"
    r"robot manipulation|manipulation (?:task|polic)|sim-to-real|visual navigation|vision-language navigation|imitation learning",
    re.I)
RE_VISION = re.compile(
    r"\bimages?\b|\bvideos?\b|visual|\bvision\b|\b3d\b|point cloud|segmentation|object detection|gaussian splatting|nerf|radiance field|"
    r"\bpixels?\b|camera|pose estimation|depth estimation|multimodal|multi-modal|\bvlms?\b|\bmllms?\b|text-to-image|diffusion transformer|"
    r"optical flow|stereo|photograph|rendering|avatar|scene", re.I)
RE_LLM = re.compile(
    r"large language model|\bllms?\b|language models?|reasoning|chain-of-thought|rlhf|instruction[- ]tun|preference optimization|"
    r"in-context learning|\btokens?\b|transformers?\b|attention|alignment|reward model", re.I)


def classify(title, abstract, topic):
    text = f"{title}. {abstract or ''}"
    if RE_DRIVING.search(text):
        return "autonomous_driving"
    if RE_EMBODIED.search(text):
        return "embodied"
    if (topic or "").startswith("Computer Vision") or RE_VISION.search(text):
        return "cv"
    if RE_LLM.search(text) or "Language Models" in (topic or ""):
        return "llm"
    return "other"


papers = []


def add(conf, tier, title, pdf, abstract="", topic="", award=None, pid=None):
    papers.append(dict(conf=conf, tier=tier, title=html.unescape(title).strip(), pdf=pdf, abstract=abstract,
                       topic_field=topic, award=award, id=pid))


# ---------- CVPR 2026 ----------
cv_oa = oa_index("cvpr_oa.html", "https://openaccess.thecvf.com")
cv_abs = load("cvpr_abs.json")
papers_html = open(D + "cv_virtual_2026_papers.html").read()
cv_title2pid = {norm(t): pid for pid, t in re.findall(r'href="/virtual/2026/poster/(\d+)">([^<]+)', papers_html)}
oral_html = open(D + "cv_virtual_2026_events_oral").read()
cv_orals = {norm(t): t for t in re.findall(r'href="/virtual/2026/oral/\d+"[^>]*>\s*([^<]{8,300}?)\s*<', oral_html)}
hl_html = open(D + "cv_highlights.html").read()
cv_hls = {norm(t): t for t in re.findall(r'href="/virtual/2026/(?:poster|oral)/\d+"[^>]*>\s*([^<]{8,300}?)\s*<', hl_html)}
cv_awards = {norm(k): (k, v) for k, v in AWARDS["CVPR2026"].items()}
seen = set()
for group, tier in [(cv_awards, "best"), (cv_orals, "oral"), (cv_hls, "highlight")]:
    for n, t in group.items():
        if n in seen or n in ("viewfulldetails",):
            continue
        title, award = (t if isinstance(t, tuple) else (t, None))
        pid = cv_title2pid.get(n)
        seen.add(n)
        add("CVPR2026", tier, title, fuzzy_get(cv_oa, n) or acronym_get(OA_TITLES["cvpr_oa.html"], title), cv_abs.get(pid, "") if pid else "", award=award, pid=pid)

# ---------- ICCV 2025 ----------
ic_oa = oa_index("iccv_oa.html", "https://openaccess.thecvf.com")
ic = load("iccv2025.json")["results"]
ic_aw = {norm(k): v for k, v in AWARDS["ICCV2025"].items()}
seen = set()
for x in ic:
    n = norm(x["name"])
    dec = (x.get("decision") or "").lower()
    tier = "best" if n in ic_aw else ("oral" if dec == "oral" else "highlight" if dec == "highlight" else None)
    if not tier or n in seen:
        continue
    seen.add(n)
    add("ICCV2025", tier, x["name"], fuzzy_get(ic_oa, n) or acronym_get(OA_TITLES["iccv_oa.html"], x["name"]), x.get("abstract", ""), award=ic_aw.get(n), pid=x["id"])

# ---------- ECCV 2026 ----------
ec = load("eccv2026.json")["results"]
ec_abs = load("eccv-abs.json")
ec_poster_pid = {norm(x["name"]): x["id"] for x in ec if x["eventtype"] == "Poster"}
seen = set()
for et, tier in [("Oral", "oral"), ("Spotlight", "highlight")]:
    for x in ec:
        n = norm(x["name"])
        if x["eventtype"] != et or n in seen:
            continue
        seen.add(n)
        pid = ec_poster_pid.get(n, x["id"])
        add("ECCV2026", tier, x["name"], x.get("paper_pdf_url"), ec_abs.get(str(pid), ec_abs.get(str(x["id"]), "")), pid=pid)


# ---------- OpenReview 系：ICML 2026 / ICLR 2026 / NeurIPS 2025 ----------
def or_pdf(x):
    m = re.search(r"forum\?id=([\w-]+)", x.get("paper_url") or "")
    return f"https://openreview.net/pdf?id={m.group(1)}" if m else None


def openreview_conf(conf, fname, absf, tier_of):
    rows = load(fname)["results"]
    absd = load(absf) if absf else {}
    aw = {norm(k): (k, v) for k, v in AWARDS[conf].items()}
    best = {}
    for x in rows:
        n = norm(x["name"])
        tier = "best" if n in aw else tier_of(x)
        if not tier:
            continue
        rank = {"best": 0, "oral": 1, "highlight": 2}[tier]
        cur = best.get(n)
        # 同一论文可能同时有 oral 事件和 poster 事件：取最高层级，并优先保留带 PDF 的记录
        if cur is None or rank < cur[0] or (rank == cur[0] and not or_pdf(cur[1]) and or_pdf(x)):
            best[n] = (rank, x, tier)
    for n, (_, x, tier) in best.items():
        if not or_pdf(x):
            # 回退：找同标题的其他记录的 openreview 链接
            for y in rows:
                if norm(y["name"]) == n and or_pdf(y):
                    x = {**x, "paper_url": y["paper_url"]}
                    break
        abstract = x.get("abstract") or absd.get(str(x["id"]), "")
        add(conf, tier, x["name"], or_pdf(x), abstract, x.get("topic") or "",
            award=aw[n][1] if n in aw else None, pid=x["id"])


icml_orals = {norm(x["name"]) for x in load("icml2026.json")["results"] if x["eventtype"] == "Oral"}
openreview_conf("ICML2026", "icml2026.json", "icml-abs.json",
                lambda x: "oral" if norm(x["name"]) in icml_orals else
                ("highlight" if x.get("decision") == "Accept (spotlight)" else None))
openreview_conf("ICLR2026", "iclr2026.json", "iclr-abs.json",
                lambda x: "oral" if x.get("decision") == "Accept (Oral)" else None)
openreview_conf("NeurIPS2025", "neurips2025.json", None,
                lambda x: "oral" if (x.get("decision") or "").lower() == "accept (oral)" else
                ("highlight" if (x.get("decision") or "").lower() == "accept (spotlight)" else None))

# ---------- 分类与筛选 ----------
CV_CONFS = {"CVPR2026", "ICCV2025", "ECCV2026"}
for p in papers:
    p["topic"] = classify(p["title"], p["abstract"], p["topic_field"])
    if p["conf"] in CV_CONFS and p["topic"] in ("llm", "other"):
        p["topic"] = "cv"  # 视觉会议的论文统一视为 CV 大方向
    if p["tier"] == "best":
        p["selected"] = True
    elif p["conf"] in CV_CONFS:
        p["selected"] = True
    elif p["topic"] in ("autonomous_driving", "embodied", "cv"):
        p["selected"] = True
    elif p["topic"] == "llm":
        p["selected"] = p["tier"] == "oral"  # LLM 只取 oral，控制比例
    else:
        p["selected"] = False

sel = [p for p in papers if p["selected"]]
print("全部候选", len(papers), "入选", len(sel), "缺 PDF", sum(1 for p in sel if not p["pdf"]))
print(Counter((p["conf"], p["tier"]) for p in sel))
print(Counter(p["topic"] for p in sel))
print(Counter((p["conf"], p["topic"]) for p in sel))
print("缺PDF示例:", [(p["conf"], p["title"]) for p in sel if not p["pdf"]][:15])
SELECTION.parent.mkdir(parents=True, exist_ok=True)
json.dump(sel, open(SELECTION, "w"), ensure_ascii=False, indent=1)
