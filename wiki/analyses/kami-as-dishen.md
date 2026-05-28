---
type: analysis
summary: 唐鳳 / PDIS 周辺の zh-tw 翻訳者が「Kami」(日本神道の神) を「神明 / 土地公 / 神祇」等の通常訳語ではなく「地神」と訳した。利用可能な訳語候補の文化的含意を意図的に剥ぎ落とし、Civic-AI 文脈で必要な「在地・有界・可退場」という機能的な核だけを最小構成で再構築する翻訳戦略。
sources:
  - correspondences.yaml
  - https://github.com/nishio/plurality-llm-wiki-zh-tw/blob/main/wiki/concepts/地神.md
  - https://github.com/audreyt/civic.ai
---

# Kami → 地神: 意味の最小化による翻訳

## 観察

唐鳳の Civic-AI 体系では、特定の場所や共同体に紐づく境界のある AI agent を比喩する語として「Kami」(日本神道の神) が使われる。zh-tw 訳での「地神」採用は、利用可能だった訳語候補の中での意図的な選択。

選択肢:
- **神** (shén) — 一般的な「神 / 霊」、抽象的すぎる
- **神明** (shénmíng) — 一般の「神々」、仏教 / 民間信仰共通の常用語
- **神祇** (shénqí) — 文語的「神々と地霊」、文体的に formal すぎる
- **土地公** (tǔdìgōng) — 台湾 / 閩南民間信仰の土地神 figure、文化的に重い
- **カミ** (phonetic 音訳) — 仏教 (佛 = Buddha) のような音訳経路、不採用
- **地神** (dìshén) — 採用された訳

## 仕組み: 意味の最小化 (semantic minimization)

「地」+「神」の最小構成で、各候補が抱える文化的含意 (cultural baggage、付随する文化的意味) を意図的に脱ぎ捨てる:

- 神祇 / 神明 の文体的 formality を除く
- 土地公 の台湾ローカル文化的 image を除く
- 「神」だけだと localization (場所性) が消えるので「地」を必須要素として加える

結果として、場所に紐づいた spirit / agent という Civic-AI の機能的な核 (在地・有界・可退場) だけを残す。

## 仁工智慧 との対比 (操作の方向が逆)

両方とも唐鳳 / PDIS 周辺の翻訳だが、操作の方向 (operation 方向) が逆:

| 翻訳例 | 操作の方向 | 仕組み |
|---|---|---|
| 人工智慧 → 仁工智慧 | **意味を足す** | 既存語の一字を同音異字 (人→仁) に置換し、儒家の徳目を新たに召喚 |
| 神明 / 土地公 → 地神 | **意味を引く** | 既存訳語候補の文化的含意を全部脱ぎ、機能だけを残す |

両方とも「直訳経路を採らない」点で共通だが、足し算と引き算が対をなす。詳細は meta 分析 [[zh-tw-translation-strategies]] 参照。

## 3 言語の比較

「Kami」という同じ指示対象 (referent) を 3 言語がどう取り込むか:

| 言語 | 訳語 | 取り込みの仕方 |
|---|---|---|
| EN | **Kami** (loanword そのまま) | 日本側の異文化性 (exoticism) を意図的に invoke。神道の文化色ごと借入 |
| JA | 神 / カミ | native word、再翻訳の必要なし |
| zh-tw | **地神** | 文化的含意を全部脱ぎ捨てて、機能だけを残す |

EN と JA は **文化を含めた借入 / native 表現**、zh-tw は **機能を抽出した抽象化**。3 言語が同じ referent に対して全く違う semantic operation (意味的操作) を行っている。

## [[kanji-as-ja-zh-bridge]] の例外パターン

[[kanji-as-ja-zh-bridge]] は「字面共有が ja-zh の意味継承を可能にする」を中心観察として書いたが、Kami は **bridge が部分的にしか機能しない例**:

- 「神」は ja-zh 共有可能 (字面 + 一般的意味)
- ただし神道の Kami が持つ animistic / 場所固有 / 非超越的という側面は、zh の「神」(monotheist 神 / 仏教の神々) には全部 transfer (転移) できない
- だから「地」を補強 morpheme (構成要素) として加える → 地神

つまり kanji bridge は 100% transfer ではなく、ja-zh 間で「**何が transfer されて、何が再構築を要するか**」のミクロ判断が翻訳者ごとに発生する。地神 は再構築の事例。

## Open Questions

- 唐鳳 / 仁工智慧計畫の翻訳者は「地神」を選んだ理由について明示的な発言があるか? 本 analysis の解釈は推測の域を出ない
- 「地神」が中文圏 (台灣 / 香港 / 中国大陸) でどの程度定着しているか? 唐鳳一人の personal usage なのか、コミュニティ標準語に近づいているのか
- 「Kami」を「神」(generic) や「土地公」(localized) でなく「地神」と訳す類似事例が他の concept でも見られるか? 仁工智慧計畫 全体の翻訳戦略として一貫しているか
- 神道の Kami が持つ非超越性 (non-transcendence) が Plurality の democratic 側面と整合する一方、儒家の「天」概念は超越性を持つ。「地神」が「天」を意図的に避けて「地」を選んだとすると、これは Plurality の non-transcendence と整合的だが、同じ翻訳者が仁工智慧で儒家 (惻隠之心 = compassion) を召喚したのと張り合うか
