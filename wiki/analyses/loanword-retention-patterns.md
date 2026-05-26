---
type: analysis
summary: 山形浩生訳の語彙選択を見ると、Plurality 本日本語版は概念ごとに loanword をカタカナで残すか、日本語に翻訳するかを系統的に選び分けている。残される語と訳される語の分かれ目に pattern がある。同じ概念の名前付けが両言語で違うことが、概念空間の文節を駆動している例。
sources:
  - https://github.com/nishio/plurality-llm-wiki-ja/blob/main/wiki/concepts/
  - https://github.com/nishio/plurality-llm-wiki-en/blob/main/wiki/concepts/
---

# 山形浩生訳の loanword 残し / 訳し分けパターン

## 観察

JA wiki の concept page 41 個のうち、EN page と意味的に対応する概念名を一覧にすると、**カタカナで loanword を残す** ものと **日本語に訳す** ものが明確に分かれている。

### カタカナで残された (loanword retention)
| JA | EN |
|---|---|
| プルラリティ | Plurality |
| クアドラティック投票 | Quadratic-Voting |
| クアドラティック資金調達 | Quadratic-Funding |
| クリエイティブなコラボレーション | Creative-Collaborations |
| ポスト表象コミュニケーション | Post-Symbolic-Communication |
| ブロードリスニング | (EN page なし — Augmented-Deliberation 内で言及) |
| スーパーモジュラリティ | (EN page なし) |
| ステークホルダー企業 | (EN page なし) |
| リバタリアニズム / リバタリアン | Libertarianism |
| テクノクラシー / テクノクラート | Technocracy |
| 一元論的アトム主義 | Monist-Atomism (アトムだけカタカナ) |

### 日本語に訳された (translation)
| JA | EN |
|---|---|
| 多元投票 | Plural-Voting |
| 拡張熟議 | Augmented-Deliberation |
| 適応型管理行政 | Adaptive-Administration |
| 没入型共有現実 | Immersive-Shared-Reality |
| 液体民主主義 | Liquid-Democracy |
| 社会市場 | Social-Markets |
| データ連合 | Data-Coalitions |
| つながった社会 | Connected-Society |
| 失われた道 | The-Lost-Dao |
| 狭い回廊 | Narrow-Corridor |
| デジタル民主主義 | Digital-Democracy |

## Pattern

訳す / 残す の分かれ目に、いくつかの規則性が観察できる:

### 1. 名前に固有な人物・コミュニティが紐ついている場合は残す
「クアドラティック投票」「リバタリアニズム」「テクノクラシー」「プルラリティ」 — これらは Glen Weyl / Ayn Rand 系譜 / 著名な ideology / 本書 eponym など、特定のコミュニティに紐ついた固有名詞性が強い。漢字熟語に置き換えると「概念が背負っている文脈」が一緒に消える。

実際 JA `クアドラティック投票.md` の Open Question は:
> 「クアドラティック投票」を漢字熟語に置き換えるか（例：「二乗投票」「平方根投票」「逓減比例投票」）。日本語版本文ではカタカナ「クアドラティック」のままが使われている。

と明示的に問題化している。これは訳すか残すかが意識的な curation 判断であったことを示す。

### 2. 形容詞 + 名詞構造で日本語に semantic equivalent がある場合は訳す
「Adaptive Administration → 適応型管理行政」「Immersive Shared Reality → 没入型共有現実」「Liquid Democracy → 液体民主主義」「Connected Society → つながった社会」 — これらは英語の形容詞 + 名詞構造を、日本語の同型の漢字熟語または和語に分解可能。意味の損失なく訳せるなら訳す方針。

### 3. メカニズム abbreviation は acronym のまま残す
GFM / AGI / DAO / PICSY — 内部展開した日本語訳は使われず、英字 acronym のまま page 化されている。これは abbreviation の英文 short form がコミュニティ内で既に流通している場合の判断。

### 4. 一元論的アトム主義のような mixed case
「Monist Atomism」を「一元論的アトム主義」と訳す際、Monist = 一元論的 (訳)、Atomism = アトム主義 (アトム部分のみ loanword) という mixed strategy が取られている。

JA `一元論的アトム主義.md` の Open Question:
> 「アトム」をそのまま使うか「原子」と訳すかで、日本語読者の感覚に差が出る可能性。山形浩生訳ではカタカナ「アトム主義」が選ばれている。

「原子主義」と訳すと物理学的な「原子」に意味がドリフトしてしまうため、カタカナ「アトム」を残すことで thinker の意味場 (Rand 的個人主義) を保つ判断。

## なぜこの観察が「面白い」か

`correspondences.yaml` の 1 行 `en: Quadratic-Voting ↔ ja: クアドラティック投票` は両者を「同じ概念」と claim するが、**JA 読者は「クアドラティック」という英語 loanword を媒介として QV にアクセスする**。漢字熟語に置き換えていれば、JA 読者は「平方根投票」「二乗投票」という日本語語彙だけで QV を語る世界線を生きたかもしれない。山形浩生はそれを採用しなかった。

これは「同じ概念でも、それを語る言語コミュニティの **語彙の手触り** が違う」という carving difference の最も微細なレイヤーであり、Wikipedia のような interlanguage-link システムからは observe できない。

逆に「液体民主主義」(Liquid Democracy) は JA で完全に翻訳されている。JA 読者は「液体」という日本語 metaphor で LD を語る。EN 読者は "Liquid" という英語 metaphor で LD を語る。同じ概念だが metaphor の言語が違う。

## Open Questions

- 訳す / 残す の判断は時系列で進化するか。たとえば「クアドラティック投票」が将来「平方根投票」に置き換わる可能性はあるか。逆に「液体民主主義」がカタカナに戻る可能性は
- 中国語版 / 韓国語版 / ドイツ語版 (zh / ko / de) でも同様の「loanword vs translation」分かれ目があるはず。多言語比較すれば、概念ごとに「翻訳しやすさ」のグラデーションが見えるかもしれない
- ブロードリスニングは JA で loanword (英語そのまま)。これは「broad listening」がまだ十分新しく日本語訳が定着していないからか、それとも意識的な loanword preservation か
