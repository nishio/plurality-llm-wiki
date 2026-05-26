---
type: analysis
summary: JA wiki は role noun (テクノクラート / リバタリアン) と ideology noun (テクノクラシー / リバタリアニズム) を別の concept page に分けている。EN wiki は ideology side のみ。日本語の loanword 形態が概念空間の文節化を駆動している例。
sources:
  - correspondences.yaml
---

# Role noun vs ideology noun の分離

## 観察

`correspondences.yaml` の `ja-only (en: ~)` セクションに、role noun の 2 ページが登場する:

| JA role | JA ideology (両側対応) | EN |
|---|---|---|
| `テクノクラート` | `テクノクラシー` ↔ `Technocracy` | (Technocracy のみ) |
| `リバタリアン` | `リバタリアニズム` ↔ `Libertarianism` | (Libertarianism のみ) |

つまり JA は「主義」と「主義者」を別の概念単位として ingest 段階で促進した。EN は「主義」一語に主義者の議論を含めた。

## 言語的基盤

日本語は外来語の `-cracy` / `-ism` 部分と `-crat` / `-ist` 部分を別のカタカナ語として独立に借用する慣習がある。`テクノクラシー` (technocracy) と `テクノクラート` (technocrat) はそれぞれ独立した借用語であり、字面の語幹も完全に分離している。

英語の方では `technocracy` と `technocrat` は同じ語幹を共有する derived form の関係にあり、`technocrats` という言及が `Technocracy` page の subsection で処理されることに違和感がない。

## なぜ価値ある観察か

JA wiki の構造は **テクノクラート についての議論 (彼らはなぜそう考えるか、誰がそうか) と テクノクラシー についての議論 (この ideology の論理構造、批判点) を構造的に separable にする**。実際に既存ページの本文を見ると、JA の `テクノクラート` page は人物例 (ピーター・ティール、サム・アルトマン 等の JA wiki entity ページ参照) の議論を中心とし、`テクノクラシー` は ideology の論理構造の議論を中心としている。

EN の `Technocracy` page は両方を兼ねるため、page の navigation が概念分析と人物分析の混合になる。

この差異は「同じ概念」が言語によって運用上どう分節化されるかの直接的な例であり、本 wiki森 が観察対象とする「diversity creates value」の典型例。

## 一般性の検討

この split は Plurality 固有ではなく日本語一般の慣習 (「フェミニズム / フェミニスト」「マルクス主義 / マルクス主義者」など) を反映している。つまりこの観察は Plurality 概念体系の独自性ではなく、**日本語 ingest が日本語の morphology に従って自動的に concept space を分節化する** という、言語横断 wiki 一般に発生する pattern を指している。

## Open Questions

- 他の `-ism / -ist` ペアに同じ split が起こりうるか? (実際の候補: `pluralism` / `pluralist` — Plurality 本では Plurality を `-ism` 化することへの賛否があり、`pluralist` 役割が存在する)
- EN wiki に逆方向で role/ideology split を導入する価値はあるか? (たとえば `Technocrats` page を作って人物議論を分離する)
- 中国語 / 韓国語版でも同様の split が起こるか? (一般に CJK は role noun と ideology noun を別字熟語にする傾向がある)
