---
type: analysis
summary: 多元投票 / Plural-Voting は両 wiki で同じ章 (5-6) を典拠とするが、JA は分人民主主義 (鈴木健) を主要セクションとして据え、EN は Amartya Sen / Arrow の不可能性定理を冒頭で引く。同じ概念に対する理論的祖先の選び方が違う。
sources:
  - https://github.com/nishio/plurality-llm-wiki-ja/blob/main/wiki/concepts/多元投票.md
  - https://github.com/nishio/plurality-llm-wiki-en/blob/main/wiki/concepts/Plural-Voting.md
---

# 多元投票 / Plural-Voting の理論的祖先が両言語で違う

## 観察

JA `多元投票` と EN `Plural-Voting` は同じ章 (本書 5-6 ⿻ Voting) を出典としており、列挙されるメカニズム (クアドラティック投票 / 液体民主主義 / Futarchy / eigenvoting など) もほぼ同一。だが、それぞれが「同章の中から何を引き出すか」が異なる。

## JA が立てた主要セクション「分人民主主義 (Divicracy)」

JA `多元投票.md` には独立した節「分人民主主義 (Divicracy)」がある。本書 5-6 多元投票の脚注を全文引用しつつ、ドゥルーズ → 鈴木健 → なめらかな社会とその敵 という系譜を「⿻ の多元投票の一例」として明示的に位置づける:

> LD とは異なり、分人民主主義は自分の票を他者に委ねるだけでなく、複数の政治課題に票を分散させることも認めている。…鈴木健 はこの概念を 2000 年代に導入し、2013 年の著書 なめらかな社会とその敵 で詳しく述べている。

JA agent が「本書脚注」だったこのリンクを「主要セクションを構成する material」と判断した。

## EN が立てた理論的接続「Amartya Sen / Arrow's Impossibility Theorem」

EN `Plural-Voting.md` は冒頭の definition で:

> The chapter cites Amartya Sen's observation that Arrow's Impossibility Theorem is dissolved once preference strength is admitted.

を引き、welfare economics における Arrow の不可能性定理を出発点として全章を位置づける。EN page には Sen / Arrow への言及があり、分人民主主義 / 鈴木健 への言及は **ゼロ**。

## 同じ章脚注からの選択

両 page は同じ本書脚注プールから読み取れる候補のうち、異なる footnote を「メインに引き上げる」判断をした。これは ingest agent の preference ではなく、**両言語コミュニティの概念空間 prior** によって駆動されている可能性が高い:

- JA: 鈴木健は日本語版解説執筆者であり、JA Plurality 言説の重要 node。`分人` 系譜の脚注は JA 言説にとって「すでに重要な接続」だった
- EN: Sen / Arrow は英語圏 social choice 理論の標準ルート。EN Plurality 言説にとって「すでに重要な接続」だった

## 帰結

両 page は同じ章を典拠としつつ、それぞれの言語コミュニティの理論的 prior に従って「多元投票」概念の theoretical hinterland を異なる方向に広げている。JA を読む者は分人と Plurality の接続を強く意識し、EN を読む者は welfare economics と Plurality の接続を強く意識する。

これは **同じ概念を異なる lineage に hook-up している** 例であり、`correspondences.yaml` の 1 行 `en: Plural-Voting ↔ ja: 多元投票` が示唆するよりも、両言語の概念空間における意味的近隣 (semantic neighborhood) は乖離している。

## Open Questions

- 両 page が言及しないが本書 5-6 章にある他の理論的祖先 (Penrose / Hanson / Lewis Carroll など) のうち、片側だけが詳述している項目はあるか
- 分人民主主義を EN 側に逆輸入する場合、`Plural-Voting` page の "Related concepts" に Divicracy を追加する形になるか、独立 concept page にするか
