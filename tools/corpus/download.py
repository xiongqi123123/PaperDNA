"""按 corpus/meta/selection.json 下载论文 PDF 到 corpus/papers/。可重复运行：已下载且校验通过的文件会跳过。

python3 download.py direct          # CVF / ECVA 直链（6 线程）
python3 download.py arxiv           # 没有直链的论文（OpenReview 系、CVF 缺失）走 arXiv
python3 download.py arxiv --all     # 同上，并包括直链下载失败的论文（direct 结束后运行）
python3 download.py report          # 按磁盘状态生成 manifest.csv / manifest.json
"""
import csv
import difflib
import json
import queue
import re
import subprocess
import sys
import threading
import time
import urllib.parse
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from config import ARXIV_CACHE as CACHE, PAPERS as OUT, SELECTION
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
SECOND_TIER = {"CVPR2026": "highlight", "ICCV2025": "highlight", "ECCV2026": "spotlight",
               "ICML2026": "spotlight", "NeurIPS2025": "spotlight", "ICLR2026": "spotlight"}
TOPIC_TAG = {"autonomous_driving": "[AD] ", "embodied": "[Embodied] ", "llm": "[LLM] ", "cv": "", "other": ""}

log_lock = threading.Lock()


def log(msg):
    with log_lock:
        with open(OUT / "download.log", "a") as f:
            f.write(time.strftime("%H:%M:%S ") + msg + "\n")


def safe_name(title):
    t = re.sub(r'[\\/:*?"<>|\n\r\t]+', " ", title)
    return re.sub(r"\s+", " ", t).strip().rstrip(".")[:150]


def dest_of(p):
    tier = "best" if p["tier"] == "best" else ("oral" if p["tier"] == "oral" else SECOND_TIER[p["conf"]])
    p["tier_label"] = tier
    return OUT / p["conf"] / tier / (TOPIC_TAG[p["topic"]] + safe_name(p["title"]) + ".pdf")


def is_pdf(path):
    try:
        with open(path, "rb") as f:
            return f.read(5) == b"%PDF-" and path.stat().st_size > 50_000
    except OSError:
        return False


def is_direct(p):
    return bool(p.get("pdf")) and "openreview.net" not in p["pdf"]


def curl_download(url, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".part")
    r = subprocess.run(["curl", "-sfL", "--retry", "5", "--retry-delay", "5", "--retry-all-errors",
                        "--connect-timeout", "30", "--max-time", "600", "-A", UA, "-o", str(tmp), url],
                       capture_output=True, text=True)
    if r.returncode == 0 and is_pdf(tmp):
        tmp.rename(dest)
        return True, ""
    tmp.unlink(missing_ok=True)
    return False, f"curl exit {r.returncode}" if r.returncode else "不是 PDF"


def curl_get(url):
    r = subprocess.run(["curl", "-sf", "--retry", "4", "--retry-delay", "10", "--retry-all-errors",
                        "--max-time", "60", "-A", UA, url], capture_output=True)
    return r.stdout if r.returncode == 0 else None


# ---------- arXiv ----------
def arxiv_lookup(title):
    """按标题在 arXiv 搜索（先整句，再关键词），标题相似度 ≥ 0.9 时返回 PDF 地址（最新版）。"""
    ns = {"a": "http://www.w3.org/2005/Atom"}
    norm = lambda s: re.sub(r"[^a-z0-9]+", "", s.lower())
    words = re.sub(r"[^A-Za-z0-9 ]+", " ", title).split()
    queries = [f'ti:"{" ".join(words)}"', " AND ".join(f"ti:{w}" for w in [w for w in words if len(w) > 3][:8])]
    errored = False
    for q in queries:
        time.sleep(3)  # arXiv API 要求请求间隔 ≥ 3 秒
        data = curl_get(f"https://export.arxiv.org/api/query?search_query={urllib.parse.quote(q)}&max_results=5")
        if data is None:
            errored = True
            continue
        try:
            entries = ET.fromstring(data).findall("a:entry", ns)
        except ET.ParseError:
            errored = True
            continue
        for e in entries:
            if difflib.SequenceMatcher(None, norm(e.findtext("a:title", "", ns)), norm(title)).ratio() >= 0.9:
                aid = re.sub(r"v\d+$", "", e.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1])
                return f"https://arxiv.org/pdf/{aid}", False
    return None, errored


def run_arxiv(papers, include_direct):
    cache = json.load(open(CACHE)) if CACHE.exists() else {}
    todo = [p for p in papers if not is_pdf(dest_of(p)) and (include_direct or not is_direct(p))]
    log(f"ARXIV START todo={len(todo)} cached={sum(p['title'] in cache for p in todo)}")
    q = queue.Queue()

    def downloader():
        while True:
            item = q.get()
            if item is None:
                return
            p, url = item
            ok, err = curl_download(url, dest_of(p))
            log(f"{'OK(arXiv)' if ok else 'FAIL(arXiv)'} {p['conf']} {p['tier_label']} {p['title'][:70]}{'' if ok else ' :: ' + err}")

    threads = [threading.Thread(target=downloader) for _ in range(3)]
    for t in threads:
        t.start()
    for p in todo:  # 查询串行（限速），下载并行
        if p["title"] in cache:
            url = cache[p["title"]]
        else:
            url, errored = arxiv_lookup(p["title"])
            if url or not errored:  # 网络出错的不缓存，下次重试
                cache[p["title"]] = url
                json.dump(cache, open(CACHE, "w"), ensure_ascii=False)
        if url:
            q.put((p, url))
        else:
            log(f"MISS(arXiv) {p['conf']} {p['tier_label']} {p['title'][:70]}")
    for _ in threads:
        q.put(None)
    for t in threads:
        t.join()
    log("ARXIV DONE")


def run_direct(papers):
    todo = [p for p in papers if is_direct(p) and not is_pdf(dest_of(p))]
    log(f"DIRECT START todo={len(todo)}")

    def work(p):
        ok, err = curl_download(p["pdf"], dest_of(p))
        log(f"{'OK' if ok else 'FAIL'} {p['conf']} {p['tier_label']} {p['title'][:70]}{'' if ok else ' :: ' + err}")

    with ThreadPoolExecutor(6) as pool:
        list(pool.map(work, todo))
    log("DIRECT DONE")


def report(papers):
    cache = json.load(open(CACHE)) if CACHE.exists() else {}
    for p in papers:
        dest = dest_of(p)
        p["file"] = str(dest.relative_to(OUT))
        p["status"] = "ok" if is_pdf(dest) else "missing"
        p["source"] = p["pdf"] if is_direct(p) else cache.get(p["title"]) or ""
    fields = ["conf", "tier_label", "award", "topic", "title", "status", "file", "source"]
    with open(OUT / "manifest.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for p in sorted(papers, key=lambda x: (x["conf"], x["tier_label"], x["topic"], x["title"])):
            w.writerow(p)
    json.dump(papers, open(OUT / "manifest.json", "w"), ensure_ascii=False, indent=1)
    ok = sum(p["status"] == "ok" for p in papers)
    print(f"ok={ok} missing={len(papers) - ok}")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    papers = json.load(open(SELECTION))
    mode = sys.argv[1]
    if mode == "direct":
        run_direct(papers)
    elif mode == "arxiv":
        run_arxiv(papers, "--all" in sys.argv)
    elif mode == "report":
        report(papers)
