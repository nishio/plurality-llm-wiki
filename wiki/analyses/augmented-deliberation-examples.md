---
type: analysis
summary: 拡張熟議 / Augmented-Deliberation は両言語で同じ章 (5-4) を出典とするが、JA は安野貴博の 2024 東京都知事選を主要事例セクションとして据え、EN は bridging algorithms の理論と選抜方法 (election / sortition / administration) の三項対立を引く。同じ概念に対する代表例の選び方が違う。
sources:
  - https://github.com/nishio/plurality-llm-wiki-ja/blob/main/wiki/concepts/拡張熟議.md
  - https://github.com/nishio/plurality-llm-wiki-en/blob/main/wiki/concepts/Augmented-Deliberation.md
---

# 拡張熟議 / Augmented-Deliberation の canonical example が両言語で違う

## 観察

両 page とも同じ問題設定から始まる: 「多様性と帯域幅のトレードオフ」/ "the historic trade-off between diversity of voices and bandwidth of conversation"、ハーバート・サイモン引用、Andrew Trask の broad listening attribution。

だが「拡張熟議とはどういう実践か」を読者に示すために選ばれる canonical な事例と理論枠組みが両 page で大きく異なる。

## JA: 安野貴博 / 東京都知事選を主要事例として据える

JA `拡張熟議.md` は「代表的システム」一覧の後に、独立セクション「安野貴博と東京都知事選」を立てる:

> 2024 年の東京都知事選挙では、安野貴博 候補が…Talk to the City で視点を可視化し…AI のバーチャルアバターを（AI あんの）YouTube に展開することで、「ブロードリスニング」のインタラクティブな形を示した。

このセクションが page の中盤を占め、独立した「ブロードリスニング」節がそれに続く。JA agent は「拡張熟議とは何かを最も具体的に示す例 = 2024 東京都知事選」という構造で page を組んだ。

## EN: bridging algorithms と選抜方法の理論枠組みを主要セクションとして据える

EN `Augmented-Deliberation.md` は同様のシステム列挙の後に、二つの理論的セクションを置く:

1. **Bridging algorithms** — Cass Sunstein の *#republic* を引いて、エンゲージメント最適化アルゴリズム (フィルターバブル) と bridging 最適化アルゴリズム (cross-cleavage 合意を持ち上げる) の対比を論じる。Community Notes が現代 internet 上の最大規模の Plurality 実装だと主張する
2. **Selection of participants** — 拡張熟議は誰の声を会話に入れるかの方法と組み合わさるとして、Election / Sortition / Administration の三項対立を明示し、それぞれの legitimacy / expertise / participation トレードオフを述べる

EN agent は「拡張熟議とは何かを最もよく説明する枠組み = bridging アルゴリズムの理論 + 民主主義における選抜方法の分類」という構造で page を組んだ。**安野貴博 / 東京都知事選への言及はゼロ**。

## 同じ概念の異なる "shape"

両 page は同じ拡張熟議概念を扱うが、page を読み終わった後の概念の「形」が異なる:

- **JA を読んだ後**: 拡張熟議とは、Polis / Talk to the City / Cortico などのツールを使い、**実際に選挙キャンペーンや市民参加に応用される実践** であり、その最も elaborated な現代事例が 2024 東京都知事選
- **EN を読んだ後**: 拡張熟議とは、**bridging アルゴリズムという特定の technical design choice** を、**Election/Sortition/Administration という古典的選抜トリレンマ** に組み込む試み

JA は実践事例で概念を grounded させる。EN は理論枠組みで概念を situate させる。これは ingest agent の判断差ではなく、両言語コミュニティの discourse 上の prior の差を反映していると考えられる:

- JA Plurality discourse は 2024 都知事選を経て「拡張熟議は選挙に応用できる」という共通理解をすでに持っている
- EN Plurality discourse は bridging algorithms vs engagement という X / Community Notes 系の議論を共通理解として持っている

## 帰結

`correspondences.yaml` の 1 行 `en: Augmented-Deliberation ↔ ja: 拡張熟議` は両 page が同じ章を出典としていることを示すが、両 page を読み比べた読者は「拡張熟議とは何か」について微妙に違う mental model を持つことになる。

## Open Questions

- 「bridging algorithms」は JA で類似訳語 (ブロードリスニング とは異なる) を持つか。JA wiki が今後この技術を扱うとき、どの語彙で carve するか
- 安野貴博 / 東京都知事選の事例を EN 側に逆輸入する場合、`Augmented-Deliberation` page のどこに位置づけるか — bridging algorithms の応用事例か、別カテゴリ (electoral 応用) を立てるか
