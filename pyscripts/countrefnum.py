#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple


# -----------------------------
# Regex patterns
# -----------------------------
HEADING_RE = re.compile(
    r'\\(?P<kind>section|subsection|subsubsection)\*?\s*\{(?P<title>(?:[^{}]|\\\{|\\\})*)\}',
    re.DOTALL
)

# Match \cite{...}, \citep{...}, \citet{...}, \citealp{...}, \citeauthor{...}, etc.
# Also supports optional arguments like \citep[see][chap.2]{key1,key2}
CITE_RE = re.compile(
    r'\\cite[a-zA-Z*]*\s*(?:\[[^\]]*\]\s*)*(?:\[[^\]]*\]\s*)*\{([^}]*)\}',
    re.DOTALL
)

INPUT_RE = re.compile(r'\\(?:input|include)\{([^}]+)\}')


# -----------------------------
# Data structure
# -----------------------------
@dataclass
class Node:
    kind: str
    title: str
    level: int
    heading_start: int
    content_start: int
    end: int = 0
    children: List["Node"] = field(default_factory=list)

    total_stats: Dict[str, Any] = field(default_factory=dict)
    direct_stats: Dict[str, Any] = field(default_factory=dict)


LEVEL_MAP = {
    "root": 0,
    "section": 1,
    "subsection": 2,
    "subsubsection": 3,
}


# -----------------------------
# Utilities
# -----------------------------
def strip_comments(text: str) -> str:
    """
    Remove LaTeX comments while preserving escaped \%.
    """
    out_lines = []
    for line in text.splitlines():
        buf = []
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == "%":
                # count preceding backslashes
                bs = 0
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    bs += 1
                    j -= 1
                # unescaped % starts a comment
                if bs % 2 == 0:
                    break
            buf.append(ch)
            i += 1
        out_lines.append("".join(buf))
    return "\n".join(out_lines)


def normalize_tex_path(base_dir: Path, raw_name: str) -> Path:
    p = Path(raw_name)
    if not p.suffix:
        p = p.with_suffix(".tex")
    if not p.is_absolute():
        p = base_dir / p
    return p.resolve()


def read_tex_recursive(tex_path: Path, seen: Optional[set] = None) -> str:
    """
    Recursively expand \input{} and \include{}.
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
        raw_name = match.group(1).strip()
        try:
            child = normalize_tex_path(base_dir, raw_name)
            if child.exists():
                return "\n" + read_tex_recursive(child, seen) + "\n"
        except Exception:
            pass
        return match.group(0)

    return INPUT_RE.sub(repl, text)


def remove_table_envs(text: str) -> str:
    """
    Remove table and table* environments.
    """
    patterns = [
        re.compile(r'\\begin\{table\*?\}.*?\\end\{table\*?\}', re.DOTALL),
    ]
    for pat in patterns:
        text = pat.sub("", text)
    return text


def extract_cites(text: str) -> Dict[str, Any]:
    matches = list(CITE_RE.finditer(text))
    keys = []
    for m in matches:
        raw = m.group(1)
        for k in raw.split(","):
            k = k.strip()
            if k:
                keys.append(k)

    return {
        "cite_cmds": len(matches),
        "key_mentions": len(keys),
        "unique_keys": len(set(keys)),
        "unique_key_list": sorted(set(keys)),
    }


def text_without_child_ranges(text: str, parent_start: int, parent_end: int, child_ranges: List[Tuple[int, int]]) -> str:
    """
    Extract parent body excluding all child heading spans.
    child_ranges should be sorted, non-overlapping.
    """
    pieces = []
    cursor = parent_start
    for cstart, cend in child_ranges:
        if cstart > cursor:
            pieces.append(text[cursor:cstart])
        cursor = max(cursor, cend)
    if cursor < parent_end:
        pieces.append(text[cursor:parent_end])
    return "".join(pieces)


# -----------------------------
# Tree building
# -----------------------------
def parse_headings(text: str) -> List[Node]:
    nodes = []
    for m in HEADING_RE.finditer(text):
        kind = m.group("kind")
        title = m.group("title").strip()
        nodes.append(Node(
            kind=kind,
            title=title,
            level=LEVEL_MAP[kind],
            heading_start=m.start(),
            content_start=m.end(),
        ))
    return nodes


def assign_node_ends(nodes: List[Node], text_len: int) -> None:
    for i, node in enumerate(nodes):
        node.end = text_len
        for j in range(i + 1, len(nodes)):
            if nodes[j].level <= node.level:
                node.end = nodes[j].heading_start
                break


def build_tree(nodes: List[Node], text_len: int) -> Node:
    root = Node(
        kind="root",
        title="__ROOT__",
        level=0,
        heading_start=0,
        content_start=0,
        end=text_len,
    )

    stack = [root]
    for node in nodes:
        while stack and stack[-1].level >= node.level:
            stack.pop()
        stack[-1].children.append(node)
        stack.append(node)

    return root


def compute_stats(node: Node, text: str) -> None:
    # total span: from content_start to end (includes descendants)
    total_text = text[node.content_start:node.end]
    node.total_stats = extract_cites(total_text)

    # direct span: subtract child spans
    child_ranges = [(c.heading_start, c.end) for c in node.children]
    child_ranges.sort()
    direct_text = text_without_child_ranges(text, node.content_start, node.end, child_ranges)
    node.direct_stats = extract_cites(direct_text)

    for child in node.children:
        compute_stats(child, text)


# -----------------------------
# Reporting
# -----------------------------
def node_to_dict(node: Node) -> Dict[str, Any]:
    return {
        "kind": node.kind,
        "title": node.title,
        "total": {
            "cite_cmds": node.total_stats.get("cite_cmds", 0),
            "key_mentions": node.total_stats.get("key_mentions", 0),
            "unique_keys": node.total_stats.get("unique_keys", 0),
        },
        "direct": {
            "cite_cmds": node.direct_stats.get("cite_cmds", 0),
            "key_mentions": node.direct_stats.get("key_mentions", 0),
            "unique_keys": node.direct_stats.get("unique_keys", 0),
        },
        "children": [node_to_dict(c) for c in node.children],
    }


def print_tree(node: Node, indent: int = 0) -> None:
    if node.kind != "root":
        pad = "  " * indent
        print(
            f"{pad}[{node.kind}] {node.title}\n"
            f"{pad}  total : cmds={node.total_stats['cite_cmds']}, mentions={node.total_stats['key_mentions']}, unique={node.total_stats['unique_keys']}\n"
            f"{pad}  direct: cmds={node.direct_stats['cite_cmds']}, mentions={node.direct_stats['key_mentions']}, unique={node.direct_stats['unique_keys']}"
        )
    for c in node.children:
        print_tree(c, indent + (0 if node.kind == "root" else 1))


def flatten_nodes(node: Node, rows: List[Dict[str, Any]], parent_path: str = "") -> None:
    if node.kind != "root":
        path = f"{parent_path} > {node.title}" if parent_path else node.title
        rows.append({
            "path": path,
            "kind": node.kind,
            "total_cite_cmds": node.total_stats["cite_cmds"],
            "total_key_mentions": node.total_stats["key_mentions"],
            "total_unique_keys": node.total_stats["unique_keys"],
            "direct_cite_cmds": node.direct_stats["cite_cmds"],
            "direct_key_mentions": node.direct_stats["key_mentions"],
            "direct_unique_keys": node.direct_stats["unique_keys"],
        })
        parent_path = path

    for c in node.children:
        flatten_nodes(c, rows, parent_path)


# -----------------------------
# Main
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Count LaTeX citation statistics by section hierarchy.")
    parser.add_argument("texfile", type=str, help="Main .tex file")
    parser.add_argument("--exclude-tables", action="store_true", help="Remove table/table* environments before counting")
    parser.add_argument("--json-out", type=str, default="", help="Write JSON output to a file")
    args = parser.parse_args()

    tex_path = Path(args.texfile).resolve()
    text = read_tex_recursive(tex_path)

    if args.exclude_tables:
        text = remove_table_envs(text)

    # whole document stats
    whole = extract_cites(text)

    # hierarchy stats
    nodes = parse_headings(text)
    assign_node_ends(nodes, len(text))
    root = build_tree(nodes, len(text))
    compute_stats(root, text)

    # print summary
    print("=" * 80)
    print(f"FILE: {tex_path}")
    print(f"EXCLUDE TABLES: {args.exclude_tables}")
    print("=" * 80)
    print("WHOLE DOCUMENT")
    print(f"  cite_cmds    : {whole['cite_cmds']}")
    print(f"  key_mentions : {whole['key_mentions']}")
    print(f"  unique_keys  : {whole['unique_keys']}")
    print("=" * 80)
    print("HIERARCHY")
    print_tree(root)
    print("=" * 80)

    if args.json_out:
        rows = []
        flatten_nodes(root, rows)
        payload = {
            "file": str(tex_path),
            "exclude_tables": args.exclude_tables,
            "whole_document": {
                "cite_cmds": whole["cite_cmds"],
                "key_mentions": whole["key_mentions"],
                "unique_keys": whole["unique_keys"],
                "unique_key_list": whole["unique_key_list"],
            },
            "hierarchy": rows,
            "tree": node_to_dict(root),
        }
        out_path = Path(args.json_out).resolve()
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"JSON written to: {out_path}")


if __name__ == "__main__":
    main()