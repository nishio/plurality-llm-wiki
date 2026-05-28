---
type: analysis
summary: parent wiki に蓄積された 14 analyses を見渡し、観察された cross-language carving difference の type を分類する meta-meta 分析。翻訳戦略 type が最も多く観察され、概念境界・系譜選択・説明力点・canonical example・言語学的 affordance・ingest shape 等の type が発見済み。未観察の future type も列挙。
sources:
  - role-vs-ideology-noun-split.md
  - plural-voting-lineages.md
  - augmented-deliberation-examples.md
  - quadratic-voting-framings.md
  - plurality-definition-framings.md
  - loanword-retention-patterns.md
  - kanji-as-ja-zh-bridge.md
  - civic-ai-homophone-substitution.md
  - kami-as-dishen.md
  - zh-tw-translation-strategies.md
  - civic-ai-cross-language-shapes.md
  - suzuki-ken-lineage.md
  - japan-reverse-import.md
  - push-asymmetry-activity-vs-word.md
---

# 観察された cross-language carving 差異の type 分類

## 概要

本 wiki 森の `wiki/analyses/` には 2026-05 末時点で 14 分析が蓄積された。これらを見渡し、観察された「cross-language carving 差異」の type を分類する。同時に、まだ観察されていない future type を列挙して、次の analysis の方向を示唆する。

## 観察された 7 types

### Type A: 概念境界の articulation 差

ある概念をどこで切るか (隣接概念との境界) が言語で違う。

- [[role-vs-ideology-noun-split]] — JA は role noun (テクノクラート) と ideology noun (テクノクラシー) を別ページに、EN は 1 page にまとめる。境界の cut が JA で細かい
- [[plurality-definition-framings]] — Plurality 概念の外延 (どこまでが Plurality か) が JA / EN で違う。JA は鈴木健経由で身体的差異まで含む、EN は Mandarin 數位 の言語的根拠中心

### Type B: 理論的系譜の選択

ある概念の祖先として、どの理論家・どの先行概念を foreground するか。

- [[plural-voting-lineages]] — 多元投票の祖先選択: JA は分人民主主義 / 鈴木健、EN は Amartya Sen / Arrow's Impossibility Theorem

### Type C: Canonical example の選択

ある概念を illustrate する代表例として、どの empirical case を選ぶか。

- [[augmented-deliberation-examples]] — 拡張熟議の代表例: JA は安野貴博 2024 都知事選、EN は bridging algorithms 理論 + 選抜方法 trichotomy

### Type D: 説明の力点・抽象化レベル

概念の説明階層 (mechanism / justification / limits) のどこに力点を置くか。

- [[quadratic-voting-framings]] — クアドラティック投票の説明: JA は鈴木健の 1/5/25 クレジット具体例 (mechanism)、EN は Licklider 信号検出理論で「なぜ二乗か」(justification)

### Type E: 翻訳戦略

ある概念を別言語にどう移すかの戦略選択。**最も多く観察される type** (4 件)。

- [[loanword-retention-patterns]] — 山形浩生訳が概念ごとに loanword 残し (クアドラティック投票) vs 漢字訳 (多元投票) を選び分ける pattern
- [[civic-ai-homophone-substitution]] — Civic AI → 仁工智慧: 同音異字置換で儒家倫理を召喚
- [[kami-as-dishen]] — Kami → 地神: 意味の最小化で文化的含意を脱ぎ捨てる
- [[zh-tw-translation-strategies]] — 観察された 3 戦略 + 未観察 2 戦略の typology (meta)

### Type F: 言語学的 affordance

書記体系 (writing system) そのものが transfer / 変換を enable / block する形。

- [[kanji-as-ja-zh-bridge]] — 漢字の共有が ja-zh で意味継承を enable する観察。en-ja より dense になる経験的検証

### Type G: ingest shape の差 (知識の格納形式)

同じ source material から、各 wiki が異なる「形」で知識を構築する。

- [[civic-ai-cross-language-shapes]] — Civic AI を EN は source 横展開 (9 件)、zh-tw は concept hierarchy 縦展開 (7 件)、JA は void with touching mentions。同じ civic.ai upstream を読みながら形状が違う

## 別カテゴリ: 言語コミュニティ固有の lineage 記録

これらは厳密には「carving 差」ではなく、片言語固有の lineage / 歴史を記録した analysis。

- [[suzuki-ken-lineage]] — JA 固有の鈴木健由来 4 concept
- [[japan-reverse-import]] — 安野貴博 2024 都知事選由来のブロードリスニングが本書日本語版に逆輸入
- [[push-asymmetry-activity-vs-word]] — cross-language push のコスト非対称性 (運用論的観察)

これらは「ある言語にだけ存在する」事実の記録で、cross-language 比較分析というより一方向の lineage tracing。

## type ごとの観察頻度

| Type | 件数 | 説明 |
|---|---|---|
| E. 翻訳戦略 | 4 | 最多 |
| A. 概念境界 | 2 | |
| C. Canonical example | 1 | |
| D. 説明の力点 | 1 | |
| G. Ingest shape | 1 | |
| B. 理論的系譜 | 1 | |
| F. 言語学的 affordance | 1 | |

## なぜ翻訳戦略 type が突出して多いか — 仮説

Type E (翻訳戦略) が他 type と比べて 4 倍密集している理由:

1. **翻訳選択は title 単位で discoverable**: 各概念ページの title (例: クアドラティック投票 vs 平方投票) を見るだけで翻訳戦略の差が visible になる。深い読解を要しない
2. **Plurality 本が bilingual edition を持つ**: en / zh-tw / ja で同じ章タイトルがどう翻訳されたかが obvious に比較可能
3. **翻訳戦略は反復可能 pattern**: 1 例見つかれば「他にも同じ pattern があるはず」と探せる
4. **Type A-D, F-G は body 読解が必要**: 概念ページの本文を読み比べないと差が見えない。コスト高

つまり **observed typology は実際の差異頻度ではなく観察コストの低さを反映している**。Type A-G の真の分布は、もっと多くの analysis を作ってみないと分からない。

## 未観察の future types

将来 analysis として書ける可能性のある type:

### Type H: connotation / register 差

ある概念に対応する語が複数言語にあるが、それぞれが背負う connotation / 文化的含意が違う。

- 既に [[words-as-public-goods-lt]] Updates 「公開サイト vs Live site vs 公開網站」で連想的に観察済 (analyses 化されていないが)
- 未 analysis 化の候補: 「プルラリティ vs Plurality vs 多元」が各言語で背負う authoritative weight 差

### Type I: 同一 source の引用頻度・引用箇所差

3 言語 wiki が同じ source (例: 本書の特定章) を、どの concept page から、何回引用しているか — 同じ章が言語によって違う重要度を持つ。

未観察。後で集計してみる価値あり。

### Type J: 概念 lifespan / dormancy 差

ある概念が、ある言語で active に議論されているが、別言語では dormant な状態。

- 例えば「分人民主主義」は JA で active、zh-tw / EN で dormant
- 「Network State」は EN で active、JA / zh-tw で dormant
- 双方向の dormancy を可視化する analysis 候補

### Type K: ingest velocity 差

新しい概念 (post-book) が各言語に届く速度の差。

- 既に [[push-asymmetry-activity-vs-word]] で hypothesis 化されているが、empirical 検証は未完
- Civic AI / 仁工智慧 / (JA: void) は ingest velocity 差の生きた事例

### Type L: 同一言語内 dialect / 地域 差

zh-tw と zh-cn の差、ja の関東 vs 関西 / 標準語 vs 方言、en の British vs American。本 wiki 森は zh-tw 子 wiki を持つが zh-cn なし、ja は標準語のみ。

将来 zh-cn / ko / es / de 子 wiki を追加するときに observable。

### Type M: 翻訳者 agency の cross-source 一貫性

同じ翻訳者 (例: 山形浩生) が複数 source を翻訳するとき、戦略の一貫性 / 揺れがあるか。

- 既に [[loanword-retention-patterns]] が部分的に touch している
- より systematic な比較が future analysis 候補

## meta 観察: 本 typology 自体の限界

本 typology は 14 analysis を「事後的に」分類した結果。新しい analysis が増えると type 自体が変化する可能性がある。具体的には:

- 既存 type の中に sub-type が見つかる (例: Type E の「同音異字置換」と「意味の最小化」は両方とも translation 戦略だが操作の方向が逆)
- 既存 type を merge すべき場合がある
- 全く新しい type が emerge する

本ページ自身が `## Updates` で増分更新される設計で、`carving-types-typology.md` という単一文書として固定するのではなく、観察の蓄積に従って evolve する design。

## Open Questions

- 14 analysis のうち、複数 type に該当する page はあるか? 例えば [[civic-ai-cross-language-shapes]] は Type G (ingest shape) だが、translation 経路の差 (仁工智慧 採用) という Type E 要素も含む。type は mutually exclusive ではない
- 「同一言語内の carving 揺れ」(例: JA の「Plurality」を「プルラリティ」とも「多元性」とも表記する) は本 typology の対象になるか? 現状は cross-language carving に focus しているが、within-language carving も観察可能
- 各 type を見つけるために最も効率的な手順は何か? (1) title level scan (Type E 発見に最強)、(2) source citation 集計 (Type I 発見に有効)、(3) body 読解比較 (Type A-D 発見に必要、コスト高)
- 本 typology を量的に拡張 (例: 100 analysis 蓄積後) すると、新 type が emerge するか、それとも既存 type の sub-divide のみが起きるか
