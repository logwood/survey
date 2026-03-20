"""
批量获取 BibTeX 引用
从 2.md 中读取论文标题列表，依次查询 Semantic Scholar API 获取 BibTeX。
输出到 batch_bibtex_output.bib
"""

import re
import time
import requests
import sys

INPUT_FILE = r"c:\Users\ASUS\Desktop\ACM_Computing_Draft\preResearching\2.md"
OUTPUT_FILE = r"c:\Users\ASUS\Desktop\ACM_Computing_Draft\batch_bibtex_output.bib"

S2_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_PAPER  = "https://api.semanticscholar.org/graph/v1/paper"
DBLP_SEARCH = "https://dblp.org/search/publ/api"


def parse_titles(filepath):
    """从 md 文件中解析 '序号. 标题(venue year)' 格式的论文列表"""
    titles = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # 匹配 "1. Title(Venue Year)" 或 "1. Title (Venue Year)"
            m = re.match(r'^\d+\.\s+(.+?)[\s]*\(.*?\)\s*(?:done)?$', line)
            if m:
                title = m.group(1).strip()
                # 去掉尾部多余空格和冒号后的副标题保留
                titles.append(title)
            elif line and re.match(r'^\d+\.', line):
                # fallback: 去掉序号
                title = re.sub(r'^\d+\.\s+', '', line).strip()
                titles.append(title)
    return titles


def search_s2(title):
    """通过 Semantic Scholar 搜索论文并获取 BibTeX"""
    try:
        # Step 1: Search
        resp = requests.get(S2_SEARCH, params={
            "query": title,
            "limit": 3,
            "fields": "title,externalIds,year,venue,citationStyles"
        }, timeout=15)
        
        if resp.status_code == 429:
            print(f"  [S2] Rate limited, waiting 30s...")
            time.sleep(30)
            resp = requests.get(S2_SEARCH, params={
                "query": title,
                "limit": 3,
                "fields": "title,externalIds,year,venue,citationStyles"
            }, timeout=15)
        
        if resp.status_code != 200:
            return None, f"S2 HTTP {resp.status_code}"
        
        data = resp.json()
        papers = data.get("data", [])
        if not papers:
            return None, "S2 no results"
        
        # 找最匹配的 (简单标题匹配)
        best = papers[0]
        for p in papers:
            if p.get("title", "").lower().strip() == title.lower().strip():
                best = p
                break
        
        bibtex = best.get("citationStyles", {}).get("bibtex")
        if bibtex:
            return bibtex, f"S2 matched: {best.get('title', '?')[:60]}"
        
        # 如果 search 结果没有 bibtex，用 paper ID 再查
        paper_id = best.get("paperId")
        if paper_id:
            resp2 = requests.get(f"{S2_PAPER}/{paper_id}", params={
                "fields": "citationStyles"
            }, timeout=15)
            if resp2.status_code == 200:
                bibtex = resp2.json().get("citationStyles", {}).get("bibtex")
                if bibtex:
                    return bibtex, f"S2 matched (2nd): {best.get('title', '?')[:60]}"
        
        return None, f"S2 found but no bibtex: {best.get('title', '?')[:60]}"
        
    except Exception as e:
        return None, f"S2 error: {e}"


def search_dblp(title):
    """通过 DBLP 搜索论文并获取 BibTeX"""
    try:
        resp = requests.get(DBLP_SEARCH, params={
            "q": title,
            "format": "json",
            "h": 3
        }, timeout=15)
        
        if resp.status_code != 200:
            return None, f"DBLP HTTP {resp.status_code}"
        
        data = resp.json()
        hits = data.get("result", {}).get("hits", {}).get("hit", [])
        if not hits:
            return None, "DBLP no results"
        
        # 获取第一个结果的 BibTeX URL
        best = hits[0]
        info = best.get("info", {})
        url = info.get("url", "")
        
        if url:
            bib_url = url.rstrip("/") + ".bib"
            resp2 = requests.get(bib_url, timeout=15)
            if resp2.status_code == 200:
                return resp2.text.strip(), f"DBLP matched: {info.get('title', '?')[:60]}"
        
        return None, f"DBLP found but no bib URL: {info.get('title', '?')[:60]}"
        
    except Exception as e:
        return None, f"DBLP error: {e}"


def main():
    titles = parse_titles(INPUT_FILE)
    print(f"解析到 {len(titles)} 篇论文\n")
    
    results = []
    failed = []
    
    for i, title in enumerate(titles):
        print(f"[{i+1}/{len(titles)}] {title[:70]}...")
        
        # 先试 Semantic Scholar
        bibtex, msg = search_s2(title)
        print(f"  {msg}")
        
        if not bibtex:
            # 回退到 DBLP
            time.sleep(1)
            bibtex, msg = search_dblp(title)
            print(f"  {msg}")
        
        if bibtex:
            results.append(f"% Paper {i+1}: {title}\n{bibtex}")
            print(f"  ✓ Got BibTeX")
        else:
            failed.append((i+1, title))
            print(f"  ✗ FAILED")
        
        # Rate limiting: S2 allows ~100 req/5min
        time.sleep(3)
    
    # 写入输出文件
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"% Auto-generated BibTeX - {len(results)} entries\n")
        f.write(f"% Failed: {len(failed)} entries\n\n")
        f.write("\n\n".join(results))
    
    print(f"\n{'='*60}")
    print(f"成功: {len(results)}/{len(titles)}")
    print(f"失败: {len(failed)}/{len(titles)}")
    print(f"输出: {OUTPUT_FILE}")
    
    if failed:
        print(f"\n失败列表:")
        for num, t in failed:
            print(f"  {num}. {t}")


if __name__ == "__main__":
    main()
