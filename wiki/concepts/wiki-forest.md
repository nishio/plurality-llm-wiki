---
type: concept
summary: 各言語の wiki を独立した「木」として並存させ、それらが共存する場 (forest) を横断観察の対象とする多言語 wiki architecture。Wikipedia の interlanguage link が前提とする「同一概念の翻訳対応」を弱めて「同じ/関連する話題の主張」だけに留めることで、文節化の差異そのものを観察可能にする。
sources:
  - words-as-public-goods-lt.md
---

# Wiki forest (wiki森)

## 定義

**Wiki forest (wiki森)** とは、各言語の wiki を独立した「木」として並存させ、それらが共存する場 (forest) を横断観察の対象とする多言語 wiki architecture を指す。本 repo (`plurality-llm-wiki`) はこの概念の参照実装。

英語名は **wiki forest**、日本語名は **wiki森**。本 repo では両方を等価に用いる (README.md / CLAUDE.md 参照)。

## メタファーの分解

| Forest の構成要素 | 本 architecture での対応 |
|---|---|
| 個々の木 (tree) | 各言語の独立 wiki (`plurality-llm-wiki-en`, `plurality-llm-wiki-ja`, ...) |
| 木の自律性 | 各言語 wiki は独立 GitHub repo として運営され、別 admin / contributor が参加できる |
| 森全体 (forest) | 言語横断で wikis が共存する場 (本 parent repo) |
| 木の間の空間 | 言語間の「文節化の差異」が観察可能になる空間 |
| 森の地図 | `correspondences.yaml` (言語間対応 registry) |
| 森の観察記録 | `wiki/analyses/` (言語間の文節化差異の ad-hoc 分析) |

## なぜ「翻訳された 1 つの wiki」ではなく「森」か

[[words-as-public-goods-lt]] より、各言語コミュニティは概念空間を独自の仕方で文節化する。これを 1 つの canonical wiki に翻訳統合すると、**翻訳の過程で文節化の差異そのものが消えてしまう**。

Wikipedia の interlanguage link は各言語版を独立に運営する点で本 architecture に近いが、対応は「同一概念の翻訳対応」と暗黙に前提されており、対応欠落 (片言語にしか概念がない状態) は first-class な観察対象にはならない。

Wiki forest は:

1. **木の自律性を最大化**: 各言語 wiki は他言語の翻訳である必要がない。片方にしか存在する概念は単に対応がないだけで、stub を置く必要もない。
2. **対応の主張を弱める**: `correspondences.yaml` の row は「同じ/関連する話題」を主張するだけで、内容の等価性は主張しない。
3. **欠落を first-class observable に**: `~` (null) で対応欠落を明示し、`scripts/show_gaps.py` で列挙する。**void が観察対象になる**。
4. **差異を分析対象に**: `wiki/analyses/` で文節化の差異を ad-hoc に記録する。Wikipedia は文節化の差異を observe するが分析はしない、という Wikipedia との明示的な差別化点。

## N 言語への拡張

森への新しい木の植樹は最小コスト:

1. `plurality-llm-wiki-<lang>` 命名で独立 repo を作る
2. `correspondences.yaml` に該当言語 column を足す

既存木の構造を変える必要はない。これは Wikipedia の interlanguage link 追加と同じ shape の操作。

## 自己言及性

本 architecture が観察対象とする Plurality (Audrey Tang / Glen Weyl の「社会的差異を超えた協働の技術」) は、それ自体が「diversity が価値を生む」プロジェクト。Wiki forest はこの主題を architecture レベルで体現する設計になっている (差異を平坦化せず、差異の観察を価値の源泉とする)。

## 関連

- [[words-as-public-goods-lt]] — 本 architecture の発想の根底となる西尾 LT (2024-01-03)
- `correspondences.yaml` — 森の地図 (言語間対応 registry)
- `wiki/analyses/` — 森の観察記録 (文節化差異の ad-hoc 分析)

## Open Questions

- 「森」のメタファーは、各 wiki 間の interaction (栄養循環、共生関係) まで含意するか? 現状は単に「並存」しているだけで、cross-wiki の有機的 interaction は薄い。
- 木の数が増えた場合 (N 言語)、`correspondences.yaml` の row 単位の管理は scale するか? 言語別の dense / sparse な対応 pattern を可視化する別表現が要るかもしれない。
