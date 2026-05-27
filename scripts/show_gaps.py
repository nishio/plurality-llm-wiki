"""Report cross-language gaps in correspondences.yaml + concept-page coverage.

Reads ../correspondences.yaml and the concept pages under each child wiki
(wikis/plurality-llm-wiki-<lang>/wiki/concepts/) and prints:

  1. Gaps: entries where one or more languages are null/missing
  2. Unmapped concept pages: pages that exist in a child wiki but appear in no
     correspondences.yaml row (review candidates — either add a row or mark
     other languages explicitly as ~)
  3. Pending pages: titles in correspondences.yaml that have no corresponding
     concept page in the child wiki yet — this is the normal sparse state when
     the registry runs ahead of child-wiki ingest, not an error. Each entry is
     a TODO for future ingest (or a candidate to retract to ~ if the
     annotation turns out unverifiable).

Usage: python3 scripts/show_gaps.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

PARENT = Path(__file__).parent.parent
CORR = PARENT / "correspondences.yaml"
WIKIS = PARENT / "wikis"
CHILD_PREFIX = "plurality-llm-wiki-"


def load_correspondences() -> list[dict]:
    if not CORR.exists():
        return []
    data = yaml.safe_load(CORR.read_text(encoding="utf-8")) or []
    if not isinstance(data, list):
        print(f"correspondences.yaml: expected list at top level, got {type(data).__name__}", file=sys.stderr)
        return []
    return data


def discover_child_languages() -> list[str]:
    if not WIKIS.exists():
        return []
    langs = []
    for child in sorted(WIKIS.iterdir()):
        if child.is_dir() and child.name.startswith(CHILD_PREFIX):
            langs.append(child.name[len(CHILD_PREFIX):])
    return langs


def child_concept_titles(lang: str) -> set[str]:
    """Return concept page stems (basename without .md) for the given language."""
    concepts_dir = WIKIS / f"{CHILD_PREFIX}{lang}" / "wiki" / "concepts"
    if not concepts_dir.exists():
        return set()
    return {p.stem for p in concepts_dir.glob("*.md")}


def main() -> int:
    entries = load_correspondences()
    langs = discover_child_languages()

    if not entries and not langs:
        print("(no correspondences.yaml entries and no child wikis discovered)")
        return 0

    # Gather titles per language as referenced in correspondences.yaml
    referenced: dict[str, set[str]] = {lang: set() for lang in langs}

    # 1. Gaps
    print("=" * 60)
    print(f"# Gaps in correspondences.yaml  ({len(entries)} entries, langs: {', '.join(langs) or 'none'})")
    print("=" * 60)
    gap_count = 0
    for i, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            print(f"  [entry {i}] not a mapping — skipping")
            continue
        missing = [lang for lang in langs if entry.get(lang) in (None, "")]
        for lang in langs:
            v = entry.get(lang)
            if v not in (None, ""):
                referenced[lang].add(str(v))
        if missing:
            gap_count += 1
            present = [f"{lang}={entry[lang]}" for lang in langs if entry.get(lang) not in (None, "")]
            print(f"  [{', '.join(present) or '(empty)'}] missing in: {', '.join(missing)}")
    if gap_count == 0:
        print("  (none — all entries cover all known languages)")
    print()

    # 2. Unmapped concept pages
    print("=" * 60)
    print("# Concept pages not referenced in correspondences.yaml")
    print("=" * 60)
    any_unmapped = False
    for lang in langs:
        pages = child_concept_titles(lang)
        unmapped = sorted(pages - referenced[lang])
        if unmapped:
            any_unmapped = True
            print(f"  [{lang}] {len(unmapped)} page(s):")
            for p in unmapped:
                print(f"    - {p}")
    if not any_unmapped:
        print("  (all concept pages are referenced)")
    print()

    # 3. Pending pages (registry-ahead state, not an error)
    print("=" * 60)
    print("# Pending pages (registry references a not-yet-created child-wiki page)")
    print("=" * 60)
    print("# Sparse coverage — registry annotations awaiting ingest. Each item")
    print("# is a TODO (create the page) or a candidate to retract to ~ (if")
    print("# the annotation cannot be verified in actual discourse).")
    any_pending = False
    for lang in langs:
        pages = child_concept_titles(lang)
        pending = sorted(referenced[lang] - pages)
        if pending:
            any_pending = True
            print(f"  [{lang}] {len(pending)} reference(s):")
            for p in pending:
                print(f"    - {p}")
    if not any_pending:
        print("  (every registry annotation has a corresponding child-wiki page)")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
