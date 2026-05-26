# Log

> 直近 7 日分のみ。全件 compact 履歴は [log.txt](log.txt)、それより古い entry の詳細は `git log -- wiki/log.md` で参照。
> 更新は `python3 scripts/refresh_logs.py` で log.txt と log.md を再生成する。

## [2026-05-26 22:30] filing-back | 同じ概念の文節境界 / 説明差を扱う 5 analysis を追加


両 wiki の対応 page pair を実際に読み比べて、同じ概念に対する両言語の articulation 差を 5 件 analysis 化:

- [[plural-voting-lineages]]: 多元投票 ↔ Plural-Voting (理論的祖先の選び方)
- [[augmented-deliberation-examples]]: 拡張熟議 ↔ Augmented-Deliberation (canonical example)
- [[quadratic-voting-framings]]: クアドラティック投票 ↔ Quadratic-Voting (説明の重心)
- [[plurality-definition-framings]]: プルラリティ ↔ Plurality (概念の外周)
- [[loanword-retention-patterns]]: 山形浩生訳のカタカナ残し / 翻訳の選び分け

なお既存 [[suzuki-ken-lineage]] と [[japan-reverse-import]] は「同じ概念の境界差」ではなく「JA 固有 lineage 記録」として index.md でセクション分離。

## [2026-05-26 21:00] filing-back | 子 wiki の ingest と correspondences.yaml 整備から得た cross-language carving observations



両子 wiki への Plurality 本 ingest (EN: source + 36 concepts + 45 entities、JA: source + 41 concepts + 35 entities) と correspondences.yaml への全 79 concept 登録から、3 つの文節化差異の pattern を analyses/ にページ化:

- [[suzuki-ken-lineage]]: JA 固有の鈴木健由来 lineage 4 concept
- [[role-vs-ideology-noun-split]]: 日本語の外来語形態が drive する concept split
- [[japan-reverse-import]]: 本書執筆後の日本コミュニティ実践が JA 版に逆輸入される pattern
