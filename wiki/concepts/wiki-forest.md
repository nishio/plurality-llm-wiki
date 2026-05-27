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

## Updates

### 2026-05-27: registry と child wiki の双方向遅延 pattern

運用してみると、`correspondences.yaml` (森の地図) と child wiki (木) の同期は **双方向に遅延しうる**:

**Registry が child wiki より先行する (pending pages)** ケース ── `show_gaps.py` section #3:

1. **新言語 column 追加直後**: 新言語 (例: `zh-tw`) を registry に追加するとき、既存 entries に対し annotation を一括で埋める。新言語の子 wiki はまだ populate されていない (or 存在すらしない)
2. **Index / 目次先行 annotate**: 新 source (本書の章立て等) を ingest するとき、目次から全章タイトルを registry に先入力。実 page ingest は時間がかかる
3. **Sibling 言語の予測的 annotate**: A wiki に new concept page を作った editor が、B / C wiki に同じ概念があると推測して registry に入れる (例: JA `分人` → `zh-tw: 分人` の字面読解 annotation)。実 B / C wiki page 化は後。**この pattern の annotation は弱く、後で検証が必要**
4. **上流 source の変更を先取り**: Plurality 本 upstream で章タイトル変更 → registry を新タイトルに更新 → child wiki page rename は別タスク

**Child wiki が registry より先行する (unmapped pages)** ケース ── `show_gaps.py` section #2:

- ある言語 wiki が独自 concept page を作ったが registry に反映していない (例: JA wiki の鈴木健 lineage を一度に register せずページだけ先に存在した瞬間)

**含意**: 両方向の遅延は **発展の偶然順序** によるもので、どちらも error ではない。むしろ:

- pending = 「ここに concept があるはずだから ingest しよう」という TODO
- unmapped = 「この page は他言語との対応をまだ考えてない」という review prompt

両方が常に 0 の状態は **発展が止まっている兆候** とも読めて、定常的に少し非ゼロな方が健全。森が育っている証拠。

`show_gaps.py` の label を「Dangling references」(壊れた参照のニュアンス) から「Pending pages」(register が先行している sparse 状態) に書き換えたのは、この understanding を tooling 側にも反映した変更 (parent commit `f483bd3`)。
