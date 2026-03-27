#!/usr/bin/env python3
r"""
prune_bib.py

Remove BibTeX entries that are not cited in one or more LaTeX .tex files.

Usage:
    python prune_bib.py survey.tex sample-base.bib -o pruned.bib
    python prune_bib.py survey.tex another.tex sample-base.bib -o pruned.bib

Features:
- Supports common citation commands such as:
  \cite, \citet, \citep, \citealt, \citealp, \citeauthor, \citeyear,
  \parencite, \textcite, \autocite, \footcite, \smartcite, \supercite,
  \nocite
- Handles multiple keys in one citation command, e.g. \cite{a,b,c}
- Keeps only BibTeX entries whose keys appear in the .tex files
- Writes the filtered .bib to the output file
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CITE_PATTERN = re.compile(
    r"""
    \\                                  # leading backslash
    (?:cite\w*|[A-Za-z]*cite[A-Za-z]*|nocite)   # citation-like command
    \s*
    (?:\[[^\]]*\]\s*){0,2}              # optional [..] [..]
    \{([^}]*)\}                         # citation keys
    """,
    re.VERBOSE,
)

ENTRY_START_PATTERN = re.compile(r'^\s*@\s*\w+\s*\{\s*([^,\s]+)\s*,', re.IGNORECASE)


def strip_comments(tex: str) -> str:
    """Remove LaTeX comments while keeping escaped percent signs."""
    return re.sub(r'(?<!\\)%.*', '', tex)


def extract_cite_keys_from_tex(tex_path: Path) -> set[str]:
    text = tex_path.read_text(encoding="utf-8")
    text = strip_comments(text)

    keys: set[str] = set()
    for match in CITE_PATTERN.finditer(text):
        raw = match.group(1).strip()
        if not raw:
            continue
        for key in raw.split(','):
            k = key.strip()
            if not k or k == '*':
                continue
            keys.add(k)
    return keys


def split_bib_entries(bib_text: str) -> list[str]:
    """
    Split a .bib file into top-level chunks. Non-entry text (comments, preamble)
    is preserved as separate chunks so the output remains usable.
    """
    chunks: list[str] = []
    n = len(bib_text)
    i = 0
    last = 0

    while i < n:
        if bib_text[i] == '@':
            if last < i:
                chunks.append(bib_text[last:i])

            start = i
            brace = 0
            in_entry = False
            while i < n:
                ch = bib_text[i]
                if ch == '{':
                    brace += 1
                    in_entry = True
                elif ch == '}':
                    brace -= 1
                    if in_entry and brace == 0:
                        i += 1
                        break
                i += 1

            chunks.append(bib_text[start:i])
            last = i
        else:
            i += 1

    if last < n:
        chunks.append(bib_text[last:])

    return chunks


def is_bib_entry(chunk: str) -> tuple[bool, str | None]:
    m = ENTRY_START_PATTERN.search(chunk)
    if not m:
        return False, None
    return True, m.group(1).strip()


def filter_bib(bib_path: Path, used_keys: set[str]) -> tuple[str, list[str], list[str]]:
    bib_text = bib_path.read_text(encoding="utf-8")
    chunks = split_bib_entries(bib_text)

    kept_chunks: list[str] = []
    kept_keys: list[str] = []
    removed_keys: list[str] = []

    for chunk in chunks:
        is_entry, key = is_bib_entry(chunk)
        if not is_entry:
            kept_chunks.append(chunk)
            continue

        assert key is not None
        if key in used_keys:
            kept_chunks.append(chunk)
            kept_keys.append(key)
        else:
            removed_keys.append(key)

    return ''.join(kept_chunks), kept_keys, removed_keys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove unused BibTeX entries based on cited keys in LaTeX files."
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="One or more .tex files followed by the source .bib file."
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output .bib file path."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if len(args.inputs) < 2:
        raise SystemExit("Please provide at least one .tex file and one .bib file.")

    *tex_files, bib_file = [Path(p) for p in args.inputs]

    for tex in tex_files:
        if tex.suffix.lower() != ".tex":
            raise SystemExit(f"Expected .tex input, got: {tex}")
        if not tex.exists():
            raise SystemExit(f"TeX file not found: {tex}")

    bib_path = bib_file
    if bib_path.suffix.lower() != ".bib":
        raise SystemExit(f"Expected final input to be a .bib file, got: {bib_path}")
    if not bib_path.exists():
        raise SystemExit(f"Bib file not found: {bib_path}")

    used_keys: set[str] = set()
    for tex in tex_files:
        used_keys.update(extract_cite_keys_from_tex(tex))

    filtered_text, kept_keys, removed_keys = filter_bib(bib_path, used_keys)

    output_path = Path(args.output)
    output_path.write_text(filtered_text, encoding="utf-8")

    print(f"Found {len(used_keys)} cited key(s) in {len(tex_files)} TeX file(s).")
    print(f"Kept {len(kept_keys)} BibTeX entrie(s).")
    print(f"Removed {len(removed_keys)} unused entrie(s).")
    if removed_keys:
        print("Removed keys:")
        for k in removed_keys:
            print(f"  - {k}")


if __name__ == "__main__":
    main()
