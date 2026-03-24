#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import argparse
from pathlib import Path
from typing import List, Dict, Set, Tuple, Optional


# -----------------------------
# Regex
# -----------------------------
CITE_RE = re.compile(
    r'\\cite[a-zA-Z*]*\s*(?:\[[^\]]*\]\s*)*(?:\[[^\]]*\]\s*)*\{([^}]*)\}',
    re.DOTALL
)

INPUT_RE = re.compile(r'\\(?:input|include)\{([^}]+)\}')

# Bib entry start: @article{key,
BIB_ENTRY_START_RE = re.compile(
    r'@(?P<type>[A-Za-z]+)\s*\{\s*(?P<key>[^,\s]+)\s*,',
    re.DOTALL
)


# -----------------------------
# Helpers
# -----------------------------
def strip_comments(text: str) -> str:
    """
    Remove LaTeX comments while preserving escaped \%.
    """
    out = []
    for line in text.splitlines():
        buf = []
        i = 0
        while i < len(line):
            if line[i] == '%':
                # count preceding backslashes
                bs = 0
                j = i - 1
                while j >= 0 and line[j] == '\\':
                    bs += 1
                    j -= 1
                if bs % 2 == 0:
                    break
            buf.append(line[i])
            i += 1
        out.append(''.join(buf))
    return '\n'.join(out)


def normalize_tex_path(base_dir: Path, raw_name: str) -> Path:
    p = Path(raw_name)
    if not p.suffix:
        p = p.with_suffix(".tex")
    if not p.is_absolute():
        p = base_dir / p
    return p.resolve()


def read_tex_recursive(tex_path: Path, seen: Optional[Set[Path]] = None) -> str:
    """
    Recursively expand \\input{} and \\include{}.
    """
    if seen is None:
        seen = set()

    tex_path = tex_path.resolve()
    if tex_path in seen:
        return ""
    seen.add(tex_path)

    text = tex_path.read_text(encoding="utf-8")
    text = strip_comments(text)
    base_dir = tex_path.parent

    def repl(match: re.Match) -> str:
        raw = match.group(1).strip()
        child = normalize_tex_path(base_dir, raw)
        if child.exists():
            return "\n" + read_tex_recursive(child, seen) + "\n"
        return match.group(0)

    return INPUT_RE.sub(repl, text)


def extract_cite_keys(text: str) -> List[str]:
    keys = []
    for m in CITE_RE.finditer(text):
        raw = m.group(1)
        for k in raw.split(','):
            k = k.strip()
            if k:
                keys.append(k)
    return keys


def extract_bib_entries(bib_text: str) -> Dict[str, str]:
    """
    Parse BibTeX entries by scanning brace depth from each @type{key,... start.
    Returns: {key: full_entry_text}
    """
    entries = {}
    pos = 0
    n = len(bib_text)

    while True:
        m = BIB_ENTRY_START_RE.search(bib_text, pos)
        if not m:
            break

        key = m.group("key").strip()
        start = m.start()

        # Find matching closing brace for the whole entry
        i = m.end() - 1
        depth = 0
        started = False
        while i < n:
            ch = bib_text[i]
            if ch == '{':
                depth += 1
                started = True
            elif ch == '}':
                depth -= 1
                if started and depth == 0:
                    end = i + 1
                    entries[key] = bib_text[start:end].strip() + "\n"
                    pos = end
                    break
            i += 1
        else:
            # malformed entry, stop scanning this one
            pos = m.end()

    return entries


def load_bib_entries(bib_paths: List[Path]) -> Dict[str, str]:
    merged = {}
    for p in bib_paths:
        text = p.read_text(encoding="utf-8")
        entries = extract_bib_entries(text)
        for k, v in entries.items():
            if k not in merged:
                merged[k] = v
    return merged


def clean_cite_commands_in_tex(original_tex: str, valid_keys: Set[str]) -> str:
    """
    Remove missing keys from \\cite{...}. If all keys are missing, remove entire cite command.
    """
    def repl(match: re.Match) -> str:
        full = match.group(0)
        raw = match.group(1)

        keys = [k.strip() for k in raw.split(',') if k.strip()]
        kept = [k for k in keys if k in valid_keys]

        if not kept:
            return ""  # remove entire cite command

        # rebuild only the final {..} part, keep command/options intact
        prefix_end = full.rfind('{')
        prefix = full[:prefix_end + 1]
        return prefix + ",".join(kept) + "}"

    return CITE_RE.sub(repl, original_tex)


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


# -----------------------------
# Main
# -----------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Extract cited BibTeX keys, compare against .bib, prune missing keys, and/or generate a reduced .bib."
    )
    parser.add_argument("tex", help="Main .tex file")
    parser.add_argument("bib", nargs="+", help="One or more .bib files")
    parser.add_argument("--out-bib", default="", help="Write a reduced .bib containing only cited entries present in bib")
    parser.add_argument("--out-tex", default="", help="Write a cleaned .tex copy with missing citation keys removed")
    parser.add_argument("--report", default="", help="Write a plain text report")
    args = parser.parse_args()

    tex_path = Path(args.tex).resolve()
    bib_paths = [Path(x).resolve() for x in args.bib]

    # 1) Read tex recursively
    expanded_tex = read_tex_recursive(tex_path)
    cited_keys_in_order = extract_cite_keys(expanded_tex)
    cited_keys = set(cited_keys_in_order)

    # 2) Read original main tex for optional rewrite
    original_main_tex = tex_path.read_text(encoding="utf-8")

    # 3) Load bib entries
    bib_entries = load_bib_entries(bib_paths)
    bib_keys = set(bib_entries.keys())

    # 4) Compare
    existing_used = sorted(cited_keys & bib_keys)
    missing_used = sorted(cited_keys - bib_keys)
    unused_bib = sorted(bib_keys - cited_keys)

    # 5) Print summary
    print("=" * 80)
    print(f"TEX: {tex_path}")
    print("BIB FILES:")
    for p in bib_paths:
        print(f"  - {p}")
    print("=" * 80)
    print(f"Total cited key mentions : {len(cited_keys_in_order)}")
    print(f"Unique cited keys        : {len(cited_keys)}")
    print(f"Bib entries loaded       : {len(bib_keys)}")
    print(f"Used and found in bib    : {len(existing_used)}")
    print(f"Missing cited keys       : {len(missing_used)}")
    print(f"Unused bib entries       : {len(unused_bib)}")
    print("=" * 80)

    if missing_used:
        print("Missing cited keys:")
        for k in missing_used:
            print(f"  {k}")
        print("=" * 80)

    # 6) Write reduced bib
    if args.out_bib:
        out_bib = Path(args.out_bib).resolve()
        reduced_text = "\n\n".join(bib_entries[k].rstrip() for k in existing_used) + "\n"
        write_text(out_bib, reduced_text)
        print(f"Reduced bib written to: {out_bib}")

    # 7) Write cleaned tex
    if args.out_tex:
        out_tex = Path(args.out_tex).resolve()
        cleaned_tex = clean_cite_commands_in_tex(original_main_tex, bib_keys)
        write_text(out_tex, cleaned_tex)
        print(f"Cleaned tex written to: {out_tex}")

    # 8) Write report
    if args.report:
        out_report = Path(args.report).resolve()
        lines = []
        lines.append(f"TEX: {tex_path}")
        lines.append("BIB FILES:")
        for p in bib_paths:
            lines.append(f"  - {p}")
        lines.append("")
        lines.append(f"Total cited key mentions : {len(cited_keys_in_order)}")
        lines.append(f"Unique cited keys        : {len(cited_keys)}")
        lines.append(f"Bib entries loaded       : {len(bib_keys)}")
        lines.append(f"Used and found in bib    : {len(existing_used)}")
        lines.append(f"Missing cited keys       : {len(missing_used)}")
        lines.append(f"Unused bib entries       : {len(unused_bib)}")
        lines.append("")
        lines.append("=== Missing cited keys ===")
        for k in missing_used:
            lines.append(k)
        lines.append("")
        lines.append("=== Used keys found in bib ===")
        for k in existing_used:
            lines.append(k)
        lines.append("")
        lines.append("=== Unused bib keys ===")
        for k in unused_bib:
            lines.append(k)

        write_text(out_report, "\n".join(lines) + "\n")
        print(f"Report written to: {out_report}")


if __name__ == "__main__":
    main()