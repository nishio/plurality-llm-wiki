---
type: analysis
summary: クアドラティック投票 / Quadratic-Voting は両 wiki で同じメカニズム (n² コスト) を扱うが、JA は鈴木健の summary (1/5/25 クレジット例) と Civilization VI の引用を冒頭に据え、EN は JCR Licklider の信号検出理論 (√N) を「なぜ平方なのか」の説明に据える。説明の重心が違う。
sources:
  - https://github.com/nishio/plurality-llm-wiki-ja/blob/main/wiki/concepts/クアドラティック投票.md
  - https://github.com/nishio/plurality-llm-wiki-en/blob/main/wiki/concepts/Quadratic-Voting.md
---

# クアドラティック投票 / Quadratic-Voting の説明重心が違う

## 観察

両 page は同じメカニズムを定義する — n 票投じるには n² のクレジットを消費する。Penrose の平方根投票への言及、Civilization VI、コロラド州議会、台湾総統杯ハッカソンといった実例リストもほぼ重なる。

だが「なぜ平方なのか」「メカニズムをどう introduce するか」の戦略が異なる。

## JA: 鈴木健の summary と Civilization VI を冒頭に

JA `クアドラティック投票.md` は仕組み説明の冒頭で、日本語版解説 (鈴木健) の以下の段落をそのまま引く:

> QV では、各参加者に与えられた「投票権（ボイスクレジット）」を自由に配分して複数票を投じることができるが、票を集中させるほど費用（クレジット消費）が二乗で増大する。たとえば、1 票なら 1 クレジットで済むところ、ある選択肢に 5 票投じるには 25 クレジットが必要となる。

つまり 1 → 1, 5 → 25 という具体例で読者を導入する。続いて 5-6 章冒頭の Civilization VI の引用が続き、ゲーム文脈で具体化される。

## EN: JCR Licklider の信号検出理論で「なぜ平方なのか」を justify

EN `Quadratic-Voting.md` は「Why squared cost」という独立セクションを持ち、本書が JCR Licklider 1948 の聴覚信号検出研究に遡って presents する justification を提示する:

> when *N* independent voters' signals are uncorrelated, they grow only as √N, while a single correlated signal grows as N. Thus a holder of stake should be awarded power that grows as the **square root** of their stake — equivalently, the **cost** of votes grows as the **square** of votes cast.

JA page は Penrose の平方根ルールに言及するが、Licklider の信号検出理論には触れない。EN page は Licklider を「なぜ二乗か」の理論的中核として据える。

## 同じ式、違う説明階層

両 page を読み比べると、QV という同じ式 (cost = n²) に対して、異なる説明階層が選ばれている:

| 層 | JA | EN |
|---|---|---|
| 動機づけ | 鈴木健の言葉でクレジット使い方を示す | Direction × strength を表現可能にする抽象的な記述 |
| 数値具体例 | 1 → 1、5 → 25 (1 章脚注より) | 言及なし |
| 起源 | Penrose、Civilization VI 冒頭引用 | Penrose + JCR Licklider 1948 |
| なぜ平方か | (省略) | 独立セクション「Why squared cost」 |
| 実装上の限界 | 言及なし | 独立セクション「Limits」: voters が完全に内部一致 + 互いに無相関のときだけ最適 |

## なぜ重心が違うか

JA agent は **読者に対して「メカニズムが具体的にどう動くか」を引き渡す** ことを優先した (1 票 → 1 クレジット、5 票 → 25 クレジット、Civilization VI ゲーム例)。EN agent は **読者に対して「なぜこの設計が選ばれたか」を justify する** ことを優先した (信号検出理論からの数学的根拠、限界条件)。

これは ingest agent の趣味の差にも見えるが、両 page は本書 5-6 章の同じ chapter から material を引いている。本書原文がすでに両方の説明資源を提供しており、agent が page にどちらを surface させるかを judgment で選んだ。JA 側は鈴木健の日本語版解説経由で「実用感」のある說明資源にアクセス可能だったため、それを優先した可能性が高い。

## 帰結

同じ QV メカニズムを学ぶ読者にとって、JA page を読むと「具体的にこういう投票方式」という mechanism understanding が得られ、EN page を読むと「なぜこの設計が theoretically grounded か」という justification understanding が得られる。

両者は補完関係であり、片方だけでは半分しか説明していない。

## Open Questions

- JA に Licklider の信号検出理論 justification を逆輸入する場合、page のどこに位置づけるか。「理論的背景」セクションを拡張するのが自然か
- JA の Open Question にある「クアドラティック」を漢字に置き換えるかの議論 ([[loanword-retention-patterns]] で詳述) は EN 側に対応する Open Question を持たない
