# plurality-llm-wiki

各言語で自律的に発達した Plurality 概念体系を、言語ごとに独立した wiki として持ち、それらをまたぐ「概念の文節化の差異」を観察・分析する多言語 wiki森。

> Wikipedia は言語間の概念の文節化の差異を observe するが、分析はしない。この wiki は分析もする。

## Language Wikis

各言語版は独立した GitHub プロジェクトとして運営され、別の admin / contributor が参加できる。本 repo (`plurality-llm-wiki`) はメタ層 (project 解説 + 言語間対応の registry + cross-language analyses) を担う。

- [plurality-llm-wiki-en](https://github.com/nishio/plurality-llm-wiki-en) — 英語 Plurality 言説の概念
- [plurality-llm-wiki-ja](https://github.com/nishio/plurality-llm-wiki-ja) — 日本語 Plurality 言説の概念

新言語を追加するには、`plurality-llm-wiki-<lang>` 命名で独立 repo を作り、本 repo の `correspondences.yaml` に該当言語 column を追加する。

## Cross-language Registry

[correspondences.yaml](../correspondences.yaml) — 言語間の概念対応データ。

```yaml
- en: Plurality
  ja: プルラリティ
- en: ~      # 英語に対応単語なし → 観察対象
  ja: <ja-only-concept>
```

`null` で表現した欠落を `python3 scripts/show_gaps.py` で列挙する。

## Concepts

(meta-wiki なので、個別概念は子 wiki 側に住む)

## Entities

## Sources

## Analyses

言語間で発見された文節化の差異を ad-hoc に記録していく場所。仮説検証は実運用の結果として自然に貯まることを期待し、無理に先取りしない。

### 同じ概念の文節境界 / 説明が違う

- [[role-vs-ideology-noun-split]] — テクノクラート vs テクノクラシー、リバタリアン vs リバタリアニズム — 日本語の外来語形態が concept space の文節化を駆動
- [[plural-voting-lineages]] — 多元投票 / Plural-Voting: JA は分人民主主義 (鈴木健) を主要セクションに、EN は Amartya Sen / Arrow 不可能性定理を冒頭に
- [[augmented-deliberation-examples]] — 拡張熟議 / Augmented-Deliberation: JA は安野貴博 2024 都知事選を canonical example に、EN は bridging algorithms 理論を主要セクションに
- [[quadratic-voting-framings]] — クアドラティック投票 / Quadratic-Voting: JA は鈴木健の 1/5/25 クレジット例で導入、EN は Licklider 信号検出理論で "なぜ二乗か" を justify
- [[plurality-definition-framings]] — プルラリティ / Plurality: JA は鈴木健経由で身体的・感覚的差異まで含む射程拡張を Open Question 化、EN は Mandarin 數位 のダブルミーニングを definition の中核に
- [[loanword-retention-patterns]] — 山形浩生訳が概念ごとに loanword 残し / 翻訳を選び分けるパターン (プルラリティ / クアドラティック投票はカタカナ、多元投票 / 液体民主主義は訳す)

### 言語コミュニティ固有の lineage (記録のみ、carving 差ではない)

- [[suzuki-ken-lineage]] — 鈴木健由来の 4 concept page (なめらかな社会とその敵 / 分人 / 分人民主主義 / PICSY) が JA 固有の理論系譜を形成
- [[japan-reverse-import]] — 安野貴博の 2024 東京都知事選由来のブロードリスニングが本書日本語版に逆輸入された pattern
