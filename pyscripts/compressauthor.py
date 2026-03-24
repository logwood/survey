#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Trim long author lists in a .bib file.

Rule:
- If an entry has more than MAX_AUTHORS authors in its author field,
  replace it with: "<first author> and others"

This is BibTeX/biblatex-friendly and usually renders as "et al.".

Usage:
    python trim_bib_authors.py input.bib output.bib

Optional:
    python trim_bib_authors.py input.bib output.bib --max-authors 5
"""

import argparse
import re
from typing import List, Tuple, Optional


def split_authors(author_value: str) -> List[str]:
    """Split BibTeX author field on top-level ' and '."""
    authors = []
    buf = []
    depth = 0
    i = 0
    n = len(author_value)

    while i < n:
        ch = author_value[i]

        if ch == "{":
            depth += 1
            buf.append(ch)
            i += 1
            continue
        elif ch == "}":
            depth = max(0, depth - 1)
            buf.append(ch)
            i += 1
            continue

        # Only split on top-level " and "
        if depth == 0 and author_value[i:i+5] == " and ":
            authors.append("".join(buf).strip())
            buf = []
            i += 5
            continue

        buf.append(ch)
        i += 1

    tail = "".join(buf).strip()
    if tail:
        authors.append(tail)

    return authors


def read_balanced_value(text: str, start: int) -> Tuple[str, int, str]:
    """
    Read a BibTeX value starting at text[start], where text[start] is { or ".
    Returns:
        value_content, next_index_after_value, delimiter_type ('brace' or 'quote')
    """
    if start >= len(text):
        raise ValueError("Unexpected end of text while reading value.")

    opener = text[start]

    if opener == "{":
        depth = 1
        i = start + 1
        buf = []
        while i < len(text):
            ch = text[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return "".join(buf), i + 1, "brace"
            buf.append(ch)
            i += 1
        raise ValueError("Unbalanced braces in BibTeX value.")

    if opener == '"':
        i = start + 1
        buf = []
        escaped = False
        while i < len(text):
            ch = text[i]
            if escaped:
                buf.append(ch)
                escaped = False
            elif ch == "\\":
                buf.append(ch)
                escaped = True
            elif ch == '"':
                return "".join(buf), i + 1, "quote"
            else:
                buf.append(ch)
            i += 1
        raise ValueError("Unbalanced quotes in BibTeX value.")

    raise ValueError(f"Expected '{{' or '\"', got {opener!r}")


def find_author_field(entry_text: str) -> Optional[Tuple[int, int, str, str]]:
    """
    Find the author field in one entry.
    Returns:
        (value_start_index, value_end_index, value_content, delimiter_type)
    where value_start_index points to the opening { or " and value_end_index
    is the index after the closing } or ".
    """
    # Match author = { ... } or author = " ... "
    m = re.search(r'(?i)\bauthor\s*=\s*', entry_text)
    if not m:
        return None

    i = m.end()
    while i < len(entry_text) and entry_text[i].isspace():
        i += 1

    if i >= len(entry_text) or entry_text[i] not in ['{', '"']:
        return None

    value_content, end_idx, delim_type = read_balanced_value(entry_text, i)
    return i, end_idx, value_content, delim_type


def process_entry(entry_text: str, max_authors: int) -> str:
    found = find_author_field(entry_text)
    if not found:
        return entry_text

    value_start, value_end, author_value, delim_type = found
    authors = split_authors(author_value)

    if len(authors) <= max_authors:
        return entry_text

    first_author = authors[0].strip()
    new_value = f"{first_author} and others"

    if delim_type == "brace":
        replacement = "{" + new_value + "}"
    else:
        replacement = '"' + new_value + '"'

    return entry_text[:value_start] + replacement + entry_text[value_end:]


def split_entries(bib_text: str) -> List[str]:
    """
    Split a .bib file into chunks:
    - comments/preamble/string blocks are preserved as-is
    - each @... entry is isolated
    """
    chunks = []
    i = 0
    n = len(bib_text)

    while i < n:
        at = bib_text.find("@", i)
        if at == -1:
            chunks.append(bib_text[i:])
            break

        # Keep text before next entry
        if at > i:
            chunks.append(bib_text[i:at])

        # Find entry boundary
        j = at
        while j < n and bib_text[j] != "{":
            j += 1

        if j >= n:
            chunks.append(bib_text[at:])
            break

        depth = 0
        k = j
        while k < n:
            if bib_text[k] == "{":
                depth += 1
            elif bib_text[k] == "}":
                depth -= 1
                if depth == 0:
                    chunks.append(bib_text[at:k+1])
                    i = k + 1
                    break
            k += 1
        else:
            # Unbalanced entry, keep the rest unchanged
            chunks.append(bib_text[at:])
            break

    return chunks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sample-base.bib", help="Input .bib file")
    parser.add_argument("output_bib", help="Output .bib file")
    parser.add_argument("--max-authors", type=int, default=5,
                        help="Maximum number of authors before trimming (default: 5)")
    args = parser.parse_args()

    with open(args.input_bib, "r", encoding="utf-8") as f:
        bib_text = f.read()

    chunks = split_entries(bib_text)
    processed = []

    for chunk in chunks:
        if chunk.lstrip().startswith("@"):
            processed.append(process_entry(chunk, args.max_authors))
        else:
            processed.append(chunk)

    with open(args.output_bib, "w", encoding="utf-8") as f:
        f.write("".join(processed))


if __name__ == "__main__":
    main()