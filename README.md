# plurality-llm-wiki

[日本語版 README](README.ja.md)

A multilingual **wiki森** ("wiki forest") that hosts each language's Plurality discourse as an autonomous wiki, and observes how the same conceptual space gets carved differently across languages.

> Wikipedia *observes* interlanguage differences in how concepts are carved, but does not *analyze* them. This wiki森 also analyzes.

**Live site:** https://nishio.github.io/plurality-llm-wiki/

## Why this exists

Plurality — Audrey Tang and E. Glen Weyl's framework for "technology for collaboration across social difference" — is itself a project about diversity creating value. As the discourse develops in each language, communities carve up the conceptual space in subtly different ways: which concepts get named, which loanwords stick, which lineages get foregrounded.

Translating those wikis into one another would erase exactly the differences worth studying. So this project keeps each language wiki autonomous and treats the carving differences themselves as the object of analysis.

## Repository layout

This is the **parent repo**. It holds:
- the cross-language registry (`correspondences.yaml`)
- the meta-wiki (`wiki/`), where cross-language analyses live
- shared scripts and Quartz config for GitHub Pages

The language wikis are **separate GitHub repos**, each independently administered:

| Wiki | Repo | Live site |
|---|---|---|
| English | [nishio/plurality-llm-wiki-en](https://github.com/nishio/plurality-llm-wiki-en) | https://nishio.github.io/plurality-llm-wiki-en/ |
| Japanese | [nishio/plurality-llm-wiki-ja](https://github.com/nishio/plurality-llm-wiki-ja) | https://nishio.github.io/plurality-llm-wiki-ja/ |

Adding an Nth language is just: create `plurality-llm-wiki-<lang>`, then add that language column to `correspondences.yaml`.

## How it works

**Each language wiki is autonomous.** A concept page on the en side does not need a translation on the ja side, and vice versa. Concepts that exist in only one language are first-class observations.

**Interlanguage links are loose.** `correspondences.yaml` is the equivalent of Wikipedia's interlanguage links — a row asserts "these pages are about the same/related topic" without claiming content equivalence:

```yaml
- en: Plurality
  ja: プルラリティ

- en: ~                  # no English counterpart → recorded observation
  ja: <ja-only-concept>

- en: <en-only-concept>
  ja: ~
```

**Carving differences live in `wiki/analyses/`** of this parent repo — ad-hoc records of what was found in actual use, not pre-registered hypotheses.

## For contributors

- Operational details and page conventions: [CLAUDE.md](CLAUDE.md)
- Gap detection across the registry: `python3 scripts/show_gaps.py`
- Index/log regeneration: `python3 scripts/build_index_txt.py`, `python3 scripts/refresh_logs.py`

## License

Content under each wiki follows that wiki's own LICENSE. This parent repo's scripts and schema are open for reuse — see individual files for specifics.
