---
type: analysis
summary: zh-tw が Plurality 関連用語を翻訳する際に採る複数の戦略を類型化 (typology)。現時点で 3 戦略 (直訳・同音異字置換・意味の最小化) が観察され、潜在的に 2 戦略 (既存哲学概念での再 framing・音訳) が観察待ち。将来の事例追加で 5 戦略 typology が拡張される想定の meta 分析。
sources:
  - correspondences.yaml
  - https://github.com/nishio/plurality-llm-wiki-zh-tw
---

# zh-tw の Plurality 用語翻訳戦略 — 類型

## 観察された 3 戦略 (2026-05 時点)

zh-tw 子 wiki の populate 中に観察された翻訳戦略を 3 つに分類。

### 1. 直訳経路 (literal calque / 直訳)

英語の構造を漢字熟語に直接対応させる standard 戦略。Plurality 本中文版の章タイトルや一般概念で広く用いられる。

例:
- Plural Voting → **多元投票** (en と ja と zh-tw で完全同字)
- Quadratic Voting → **平方投票** (quadratic = 平方)
- Quadratic Funding → **平方融資**
- Liquid Democracy → **流動民主**
- Augmented Deliberation → **擴增審議**
- Social Markets → **社會市場**
- Connected Society → **連結社會**
- Narrow Corridor → **狹窄走廊**

これは大半の concept で採られる既定 (default) 戦略。漢字熟語の構成原理が英語複合語と類似しているため、低コストで成立する。

### 2. 同音異字置換 (homophone substitution / 同音替字)

既存の漢字熟語の一字を同音異字に置き換えて、新たな意味層 (儒家 / 仏教等) を召喚する創造的 (creative) 戦略。詳細は [[civic-ai-homophone-substitution]] 参照。

例:
- 人工智慧 (AI) → **仁工智慧** (Civic AI): 人 (rén,「人が作る」) → 仁 (rén, 儒家の徳目 benevolence)

操作の方向: **意味を足す** (新たな哲学的 layer を追加召喚)

### 3. 意味の最小化 (semantic minimization)

利用可能な訳語候補の文化的含意 (cultural baggage、付随する文化的意味) を意図的に脱ぎ捨て、機能的な核だけを最小構成で残す戦略。詳細は [[kami-as-dishen]] 参照。

例:
- Kami (日本神道) → **地神** (神明 / 土地公 / 神祇等の文化的 baggage を避け、「地」+「神」で在地性 (場所性) だけを保持)

操作の方向: **意味を引く** (既存の文化的 layer を意図的に削除)

## 3 戦略の関係

| 戦略 | 漢字の活用 | 創造性 |
|---|---|---|
| 1. 直訳経路 | 既存漢字熟語の構成原理を活用 | 低 |
| 2. 同音異字置換 | 漢字の表意性 (ideographic affordance) を creative に活用 | 高 |
| 3. 意味の最小化 | 漢字の組み合わせ自由度を活用 | 中 |

(2) と (3) は既定の直訳経路を意図的に脱出する、翻訳者の judgement (判断) を必要とする。

## 未観察の候補戦略

将来発見されうる可能性として 2 つを記録しておく:

### 4. 中文既存哲学概念での再 framing (philosophical re-framing)

中文の既存哲学伝統 (儒家 / 道家 / 法家 / 墨家等) の概念で Plurality 関連語を再 frame する戦略。Plurality 本 3-3 章で「大同」(孫文経由) との接点が示唆されているが、まだ独立 page にはなっていない。例えば Plurality 全体を「大同」と訳す試みがあれば、これは戦略 4 に相当する。

戦略 (2) との違い: (2) は字面の一部を置き換えるが、(4) は語そのものを既存概念に置き換える。

### 5. 音訳 (phonetic loanword)

「卡米」(kǎmǐ, Kami の音訳) のような phonetic 経路。仏教用語 (佛 = Buddha, 涅槃 = Nirvana) の翻訳経路に類似する。現状の zh-tw では未観察だが、神道概念で採られ得る選択肢だった。「地神」が選ばれたことの裏返しで、音訳路線を意図的に避けたことになる。

戦略 (3) との違い: 音訳は意味成分をゼロにする (純粋音表記)、意味の最小化は最小の意味成分を残す。

## ja との対比

JA も同様の戦略類型を持つが、各戦略の分布が違う:

| 戦略 | zh-tw | ja |
|---|---|---|
| 直訳経路 | 多用 (多元投票、平方投票…) | 多用 (拡張熟議、液体民主主義…) |
| 同音異字置換 | 仁工智慧 (1 例観察) | 漢字 pun は希、カタカナ化が代替経路 |
| 意味の最小化 | 地神 (1 例観察) | データ連合 / なめらか等で漢字最小構成 |
| 既存哲学概念での再 framing | 未観察 | 逆方向 (JA → 本書) で 鈴木健の「分人 / なめらか」が起きている |
| 音訳 | 未観察 | カタカナ loanword (プルラリティ / クアドラティック投票…) として日常的 |

JA の支配的 (dominant) 戦略はカタカナ化 (音訳の variant、外来語マーカーとして機能)、zh-tw は直訳経路。zh-tw が同音異字置換と意味の最小化という創造的な漢字 affordance を活用しているのに対し、JA は表意性よりもカタカナの「外来語マーカー」機能を多用している。詳細は [[loanword-retention-patterns]] 参照。

## Open Questions

- 戦略 4 (既存哲学概念での再 framing) を意識的に試みると、Plurality がどう中文圏で再 articulate されるか
- 唐鳳 / PDIS の翻訳者が複数戦略を使い分ける基準は何か。場合ごとに intuitive (直観的) に選んでいるのか、それとも明示的なルールがあるか
- 3 戦略が「同じ概念」に同時適用可能な場合 (例: Civic AI の zh-tw 訳に直訳 (公民 AI) と同音置換 (仁工智慧) の両方が成立する) どちらが community に定着するか。観察対象
- 戦略 5 (音訳) が中文圏で採られにくい理由 — 漢字の表意性が strong すぎて pure phonetic 化への pressure が低い? 仏教用語のような大規模翻訳事業が無い限り音訳路線は採られにくいか
- 第 6 戦略があり得るか? 例: 字義の上位概念で抽象化する、native 既存語に強引に押し込める、等
