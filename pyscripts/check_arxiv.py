#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
check_arxiv_bib.py

纯标准库版本：
- 不依赖 bibtexparser
- 不依赖 pyparsing

用法：
    python check_arxiv_bib.py refs.bib
    python check_arxiv_bib.py refs.bib --strict-authors
    python check_arxiv_bib.py refs.bib --json
    python check_arxiv_bib.py refs.bib --debug
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from typing import List, Optional, Tuple


ARXIV_API = "https://export.arxiv.org/api/query?id_list={}"
ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

# 新旧 arXiv ID
ARXIV_ID_RE = re.compile(
    r"(?:arXiv:)?([a-z\-]+(?:\.[a-z\-]+)?/\d{7}|\d{4}\.\d{4,5})(v\d+)?",
    re.I,
)

ABBREV_AUTHOR_TOKENS = {
    "others",
    "et al",
    "et al.",
    "and others",
}


@dataclass
class ArxivMeta:
    requested_id: str
    canonical_id: str
    title: str
    published_year: Optional[int]
    authors: List[str]
    journal_ref: Optional[str]


@dataclass
class CheckResult:
    key: str
    entry_type: str
    arxiv_id: Optional[str]
    status: str
    messages: List[str]


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip()


def normalize_title(text: str) -> str:
    text = (text or "").replace("{", "").replace("}", "")
    text = normalize_spaces(text).casefold()
    text = re.sub(r"[^\w\s]", "", text)
    return normalize_spaces(text)


def normalize_name(text: str) -> str:
    text = (text or "").replace("{", "").replace("}", "")
    text = normalize_spaces(text).casefold()
    text = re.sub(r"[^\w\s,.\-]", "", text)
    return normalize_spaces(text)


def strip_version(arxiv_id: str) -> str:
    return re.sub(r"v\d+$", "", arxiv_id, flags=re.I)


def parse_bib_entries(text: str) -> List[str]:
    """
    按字符扫描 BibTeX 条目，支持嵌套花括号。
    适用于：
        @article{...}
        @inproceedings{...}
        @misc{...}
    """
    entries = []
    n = len(text)
    i = 0

    while i < n:
        at = text.find("@", i)
        if at == -1:
            break

        # 找到类型后的第一个 { 或 (
        j = at + 1
        while j < n and text[j].isspace():
            j += 1

        while j < n and (text[j].isalnum() or text[j] in "_-"):
            j += 1

        while j < n and text[j].isspace():
            j += 1

        if j >= n or text[j] not in "{(":
            i = at + 1
            continue

        open_ch = text[j]
        close_ch = "}" if open_ch == "{" else ")"

        depth = 0
        k = j
        while k < n:
            ch = text[k]
            if ch == open_ch:
                depth += 1
            elif ch == close_ch:
                depth -= 1
                if depth == 0:
                    entries.append(text[at:k + 1])
                    i = k + 1
                    break
            k += 1
        else:
            # 未闭合，停止
            break

    return entries


def extract_entry_type_and_key(entry: str) -> Tuple[str, str]:
    m = re.match(r"@\s*([A-Za-z0-9_\-]+)\s*[\{\(]\s*([^,]+),", entry, re.S)
    if not m:
        return "<unknown>", "<unknown>"
    return m.group(1).strip(), m.group(2).strip()


def extract_field(entry: str, field: str) -> Optional[str]:
    """
    提取字段值，支持：
      field = { ...嵌套... }
      field = "..."
      field = bareword
      year = 2025
    """
    m = re.search(rf"(?i)\b{re.escape(field)}\b\s*=\s*", entry)
    if not m:
        return None

    i = m.end()
    n = len(entry)

    while i < n and entry[i].isspace():
        i += 1
    if i >= n:
        return None

    # { ... } 形式，支持嵌套
    if entry[i] == "{":
        depth = 0
        start = i + 1
        j = i
        while j < n:
            if entry[j] == "{":
                depth += 1
            elif entry[j] == "}":
                depth -= 1
                if depth == 0:
                    return entry[start:j].strip()
            j += 1
        return None

    # " ... " 形式
    if entry[i] == '"':
        start = i + 1
        j = start
        while j < n:
            if entry[j] == '"' and entry[j - 1] != "\\":
                return entry[start:j].strip()
            j += 1
        return None

    # 裸值，读到逗号或条目尾
    start = i
    j = i
    while j < n and entry[j] not in ",})":
        j += 1
    value = entry[start:j].strip()
    return value or None


def split_bib_authors(author_field: str) -> List[str]:
    if not author_field:
        return []
    parts = [normalize_spaces(x) for x in re.split(r"\s+and\s+", author_field)]
    return [p for p in parts if p]


def looks_abbreviated_author_list(authors: List[str]) -> bool:
    lowered = [a.casefold() for a in authors]
    for a in lowered:
        if a in ABBREV_AUTHOR_TOKENS:
            return True
        if "et al" in a:
            return True
    return False


def extract_arxiv_id(entry: str) -> Optional[str]:
    archiveprefix = extract_field(entry, "archiveprefix")
    eprint = extract_field(entry, "eprint")

    if archiveprefix and archiveprefix.casefold() == "arxiv" and eprint:
        m = ARXIV_ID_RE.search(eprint)
        if m:
            return (m.group(1) + (m.group(2) or "")).strip()

    candidates = [
        extract_field(entry, "eprint"),
        extract_field(entry, "journal"),
        extract_field(entry, "note"),
        extract_field(entry, "url"),
        extract_field(entry, "annote"),
    ]

    for value in candidates:
        if not value:
            continue
        m = ARXIV_ID_RE.search(value)
        if m:
            return (m.group(1) + (m.group(2) or "")).strip()

    return None


def fetch_arxiv_meta(arxiv_id: str, timeout: int = 20) -> ArxivMeta:
    url = ARXIV_API.format(urllib.parse.quote(arxiv_id))
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "check-arxiv-bib/1.0"
        },
    )

    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()

    root = ET.fromstring(raw)
    entry = root.find("atom:entry", ATOM_NS)
    if entry is None:
        raise ValueError(f"no arXiv entry found for {arxiv_id}")

    title = normalize_spaces(entry.findtext("atom:title", default="", namespaces=ATOM_NS))
    published = entry.findtext("atom:published", default="", namespaces=ATOM_NS)
    published_year = None
    if published[:4].isdigit():
        published_year = int(published[:4])

    authors = []
    for author_el in entry.findall("atom:author", ATOM_NS):
        name = author_el.findtext("atom:name", default="", namespaces=ATOM_NS)
        name = normalize_spaces(name)
        if name:
            authors.append(name)

    journal_ref = entry.findtext("arxiv:journal_ref", default="", namespaces=ATOM_NS)
    journal_ref = normalize_spaces(journal_ref) or None

    canonical_id = arxiv_id
    entry_id_url = entry.findtext("atom:id", default="", namespaces=ATOM_NS)
    if "/abs/" in entry_id_url:
        canonical_id = entry_id_url.split("/abs/", 1)[1].strip()

    return ArxivMeta(
        requested_id=arxiv_id,
        canonical_id=canonical_id,
        title=title,
        published_year=published_year,
        authors=authors,
        journal_ref=journal_ref,
    )


def compare_title(bib_title: Optional[str], api_title: str) -> Tuple[bool, str]:
    if not bib_title:
        return False, "missing bib title"

    if normalize_title(bib_title) == normalize_title(api_title):
        return True, "title OK"

    return False, f"title mismatch | bib='{bib_title}' | arXiv='{api_title}'"


def compare_year(bib_year: Optional[str], api_year: Optional[int]) -> Tuple[bool, str]:
    if not bib_year:
        return False, "missing bib year"
    if api_year is None:
        return False, "arXiv published year unavailable"

    try:
        y = int(bib_year)
    except ValueError:
        return False, f"invalid bib year: {bib_year}"

    if y == api_year:
        return True, "year OK"

    return False, f"year mismatch | bib={y} | arXiv={api_year}"


def compare_journal(bib_journal: Optional[str], arxiv_id: str) -> Tuple[bool, str]:
    if not bib_journal:
        return False, "missing bib journal"

    journal_norm = bib_journal.casefold()
    full_id = arxiv_id.casefold()
    base_id = strip_version(arxiv_id).casefold()

    if "arxiv" in journal_norm and (full_id in journal_norm or base_id in journal_norm):
        return True, "journal OK"

    return False, f"journal may not reference arXiv ID '{arxiv_id}' correctly"


def compare_authors(
    bib_author_field: Optional[str],
    api_authors: List[str],
    strict: bool = False,
) -> Tuple[bool, str]:
    if not bib_author_field:
        return False, "missing bib authors"
    if not api_authors:
        return False, "arXiv author list unavailable"

    bib_authors = split_bib_authors(bib_author_field)
    if not bib_authors:
        return False, "missing bib authors"

    abbreviated = looks_abbreviated_author_list(bib_authors)

    if abbreviated and not strict:
        first_bib = normalize_name(bib_authors[0])
        first_api = normalize_name(api_authors[0])

        if first_bib == first_api:
            return True, "authors OK (abbreviated bib list; first author matched)"
        return False, f"first author mismatch | bib='{bib_authors[0]}' | arXiv='{api_authors[0]}'"

    bib_norm = [normalize_name(a) for a in bib_authors]
    api_norm = [normalize_name(a) for a in api_authors]

    if bib_norm == api_norm:
        return True, "authors OK"

    return False, f"authors mismatch | bib_count={len(bib_authors)} | arXiv_count={len(api_authors)}"


def check_entry(entry: str, strict_authors: bool = False, debug: bool = False) -> CheckResult:
    entry_type, key = extract_entry_type_and_key(entry)

    title = extract_field(entry, "title")
    author = extract_field(entry, "author")
    year = extract_field(entry, "year")
    journal = extract_field(entry, "journal")
    arxiv_id = extract_arxiv_id(entry)

    if debug:
        debug_msgs = [
            f"DEBUG title={title!r}",
            f"DEBUG author={author!r}",
            f"DEBUG year={year!r}",
            f"DEBUG journal={journal!r}",
            f"DEBUG arxiv_id={arxiv_id!r}",
        ]
    else:
        debug_msgs = []

    if not arxiv_id:
        return CheckResult(
            key=key,
            entry_type=entry_type,
            arxiv_id=None,
            status="SKIP",
            messages=debug_msgs + ["no arXiv ID found in eprint/journal/note/url"],
        )

    try:
        meta = fetch_arxiv_meta(arxiv_id)
    except Exception as e:
        return CheckResult(
            key=key,
            entry_type=entry_type,
            arxiv_id=arxiv_id,
            status="ERROR",
            messages=debug_msgs + [f"arXiv lookup failed: {e}"],
        )

    messages = list(debug_msgs)
    failures = 0
    warnings = 0

    ok, msg = compare_title(title, meta.title)
    messages.append(msg)
    failures += 0 if ok else 1

    ok, msg = compare_year(year, meta.published_year)
    messages.append(msg)
    failures += 0 if ok else 1

    ok, msg = compare_journal(journal, arxiv_id)
    messages.append(msg)
    failures += 0 if ok else 1

    ok, msg = compare_authors(author, meta.authors, strict=strict_authors)
    messages.append(msg)
    if not ok:
        warnings += 1

    status = "OK"
    if failures > 0:
        status = "FAIL"
    elif warnings > 0:
        status = "WARN"

    return CheckResult(
        key=key,
        entry_type=entry_type,
        arxiv_id=arxiv_id,
        status=status,
        messages=messages,
    )


def print_results(results: List[CheckResult]) -> None:
    for r in results:
        print("=" * 80)
        print(f"[{r.status}] key={r.key} type={r.entry_type} arxiv_id={r.arxiv_id}")
        for m in r.messages:
            print(f"  - {m}")

    print("=" * 80)
    total = len(results)
    ok = sum(1 for r in results if r.status == "OK")
    warn = sum(1 for r in results if r.status == "WARN")
    fail = sum(1 for r in results if r.status == "FAIL")
    skip = sum(1 for r in results if r.status == "SKIP")
    error = sum(1 for r in results if r.status == "ERROR")
    print(f"Summary: total={total}, OK={ok}, WARN={warn}, FAIL={fail}, SKIP={skip}, ERROR={error}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("bibfile", help="path to .bib file")
    parser.add_argument("--strict-authors", action="store_true", help="require full author list exact match")
    parser.add_argument("--sleep", type=float, default=3.0, help="seconds between arXiv API calls")
    parser.add_argument("--json", action="store_true", help="print JSON instead of text")
    parser.add_argument("--debug", action="store_true", help="print extracted fields for debugging")
    args = parser.parse_args()

    try:
        with open(args.bibfile, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"failed to read {args.bibfile}: {e}", file=sys.stderr)
        sys.exit(1)

    entries = parse_bib_entries(text)
    if not entries:
        print("no BibTeX entries found", file=sys.stderr)
        sys.exit(2)

    results: List[CheckResult] = []
    for idx, entry in enumerate(entries):
        results.append(check_entry(entry, strict_authors=args.strict_authors, debug=args.debug))
        if idx != len(entries) - 1 and args.sleep > 0:
            time.sleep(args.sleep)

    print_results(results)


if __name__ == "__main__":
    main()