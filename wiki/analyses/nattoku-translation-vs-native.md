---
type: analysis
summary: 「納得」を Plurality 本 JA 版で grep すると 2 回しか出ない。本書原稿が英語で書かれたため翻訳経路 (EN → JA) では 納得 が呼び込まれない。一方、native JA デジタル民主主義文書 (team-mirai 衆院選 2026 マニフェスト、plurality-japanese Scrapbox) では 40 回以上出現。翻訳経路の比較と native discourse の収集は別の方法論で、それぞれ違う carving を surface する。
sources:
  - https://github.com/nishio/plurality-llm-wiki-ja/blob/main/raw/PLURALITY_Japanese.pdf
  - https://github.com/nishio/plurality-llm-wiki-ja/blob/main/raw/plurality-japanese.json
  - https://github.com/nishio/plurality-llm-wiki-ja/blob/main/raw/team-mirai-manifesto-09-living-admin.md
  - https://github.com/nishio/plurality-llm-wiki-ja/blob/main/raw/team-mirai-manifesto-10-digital-democracy.md
  - words-as-public-goods-lt.md
  - habermas-blocks-pluralization.md
---

# 「納得」: 翻訳経路と native discourse の 2 方法論

## 観察の起点

[[words-as-public-goods-lt]] (2024-01) は「英語に『納得』の対応語が無い」を void の代表例として主張した。本 analysis ではこの主張を 4 言語の Plurality 本訳と JA native sources で empirical に検証する。

## Step 1: 翻訳経路の比較 — 4 言語の Plurality 本

JA 本書全文 (約 600 ページ) を grep すると、「納得」は **2 箇所のみ**:

| Context | JA | EN | zh-tw | DE |
|---|---|---|---|---|
| 5-6 章「⿻ 投票の限界」 | 「**納得**いく妥協」 | "a **sense of** compromise" | 「達成妥協」 | 「der **Kompromiss**」(単独) |
| 6-0 章「⿻ から現実へ」 | 「直感的に**納得**できる」 | "**While intuitive**" | 「為**直覺**性質」 | 「intuitiv **nachvollziehbar**」 |

観察:
- EN は context-dependent paraphrase で「納得」layer を partial に表現 ("sense of" / "intuitive")
- zh-tw は両 context で「納得」layer を脱落させる (もっとも EN に忠実な直訳)
- **DE は context 2 で「nachvollziehbar」を採用** — これは「心の中で辿って理解できる」という構造で 納得 の core に最も近い

LT 仮説は EN について正しい (真の void) が、foreign 全般に void かは疑わしい (DE には partial coverage)。

## Step 2: native JA discourse の収集

ユーザー指摘:「本書原稿は英語で書かれているので、JA 版の『納得』頻度は本来の JA-native frequency を反映していない」。検証:

| Source | 性質 | 「納得」occurrences |
|---|---|---|
| Plurality 本 JA 版 (約 600 ページ) | 翻訳 (EN→JA) | 2 |
| a.txt (Plurality 日本論考 overview) | 集約 writing | 0 |
| **team-mirai 衆院選 2026 マニフェスト 9, 10 章** | **native 政党文書** | **3** |
| **plurality-japanese Scrapbox** (1421 ページ) | **native コミュニティ議論** | **40 occurrences across 24 pages** |

Plurality 本 JA 版 (2) と plurality-japanese Scrapbox (40) で **20 倍の頻度差**。

## 質的に critical な findings

### Scrapbox に「納得」専用 page が存在

> **「テクノロジーに対する不信感が募る時代に、納得感のためのテクノロジーを考える」**

「納得感のためのテクノロジー」が概念単位として確立されている。

### team-mirai マニフェストは「納得」を mission-critical に使う

- 「国民が自ら『**使って納得できる**』投票体験」(9 章 投票制度)
- 「対立する利害の間から『**誰もが納得できる**第三案』を熟議によって導き出し、建設的な合意形成を実現」(10 章 デジタル民主主義)
- 「より透明で**納得感**ある意思決定を支えます」(10 章)

つまり **デジタル民主主義の目的そのもの** が「納得」で articulate されている。EN なら "consensus" / "buy-in" / "legitimacy" / "satisfaction" など複数語で分散される concept が、JA では「納得」一語に統合されている。

## 結論: ユーザー仮説の支持

> 「『納得』の出現頻度が低いのは、そもそもこの書籍の原稿が英語で書かれたから。日本語やドイツ語でのデジタル民主主義に関する記述を集めるとこれらの単語が頻出するかも」

**強く支持される**:
- JA 翻訳本 2 occurrences vs JA native sources 43+ occurrences (20 倍以上の差)
- 「納得」は JA-native デジタル民主主義言説のキー概念だが、EN → JA 翻訳 flow ではほぼ呼び込まれない
- 翻訳経路だけ見ると「JA でも納得は希」と誤った結論に至る

## 方法論的含意 — 2 つの異なる比較手法

本 wiki 森が cross-language carving を観察する際、2 つの方法論がある:

| 手法 | 何が見えるか | 何が見えないか |
|---|---|---|
| **翻訳経路の比較** (1 source → N 言語) | 翻訳者の戦略・block / activation 経路、term-by-term mapping | source language が持たない概念は、どの翻訳にも現れない |
| **Native discourse の収集** (各言語が自前の vocabulary で書いたもの) | 各言語コミュニティが自然に articulate する概念、native の頻出語 | 比較対象が異なる topic を扱う場合があり、直接比較が困難 |

両方が必要で、それぞれ違うものを surface する:
- 翻訳経路は **訳語選択** の差を見せる (e.g., [[civic-ai-homophone-substitution]], [[kami-as-dishen]], [[habermas-blocks-pluralization]])
- Native discourse は **言語固有の頻出概念** を見せる (e.g., 本 analysis の「納得」)

[[words-as-public-goods-lt]] 元 LT の主張 (「納得が EN に void」) は **後者の方法論** に基づく観察だった。LT の中で著者 (西尾) は Code for Japan の議論で出た「納得」発言を起点にしていて、これは native JA discourse の実例。LT 仮説は native JA frequency を実際に観察した結果として正しい。

本 wiki 森の各子 wiki は、翻訳経路の source (Plurality 本) と native discourse の source (Scrapbox / team-mirai / civic.ai 等) の両方を持っているのが理想。現状:

| 子 wiki | 翻訳 source | Native discourse source |
|---|---|---|
| JA | Plurality 本 JA 版 | ✓ plurality-japanese Scrapbox (1421p) + team-mirai-manifesto (11 章) + 各種 |
| EN | Plurality 本 (原書 EN) | △ civic.ai / Vitalik / 上流 PR 等 (一部 native) |
| zh-tw | Plurality 本 zh-tw 版 | △ g0v / PDIS / civic.ai 中文版 (一部 native) |
| DE | Plurality 本 DE 版 | ✗ 不足 (de wishlist に追加対象) |

DE wiki に native ドイツ語デジタル民主主義文書を集めることで、「nachvollziehbar」が native DE 言説でどれだけ頻出するか、Habermas 系学術文献の vocabulary を carving 分析できるか — observable になる。

## Open Questions

- DE native デジタル民主主義文書を集めると、「nachvollziehbar」は実際にどれだけ頻出するか? Habermas 系学術文献 / Decidim Deutschland / Bundestag AI 戦略文書 を ingest して empirically 確認したい
- zh-tw native discourse でも「納得」相当 (e.g., 「認同」「服氣」「心服口服」) が頻出するか?
- EN native discourse で「納得」の core (subjective acceptance + understanding) を一語で articulate する語はあるか? "buy-in" は近いが軽すぎる、"sense-making" は process 寄り、"acceptance" は accepting だけで understanding を含まない
- 翻訳経路と native discourse の両方を持つ言語 (現状 JA がほぼ唯一) でしか、本 analysis のような methodological 比較ができない。EN / zh-tw / DE で同じ比較を可能にするには、各言語の native ingest を deepen する必要がある

## Updates

### 2026-06-02: 「納得」3 言語比較研究ノートからの refinement ([[nattoku-research-notes]])

西尾の GPT 補助調査 ([[nattoku-research-notes]]) から、本 analysis を 2 点 refine:

**1. DE「Nachvollziehbarkeit」の partial coverage は私の以前の表現より精密に必要**

以前は「DE の Nachvollziehbarkeit が 納得 core に最も近い」と書いたが、empirical に refined すると:

| 概念 | 焦点 | 含む要素 |
|---|---|---|
| nachvollziehbar | **対象側** (説明・判断・行動) | 道筋を追える (retrace) |
| 納得できる | **主体側** (理解する人の内面) | 道筋を追える **+ 自分の中に受け入れる** |

つまり Nachvollziehbarkeit は **納得 の retrace 構造のみを覆い、acceptance 構造は別の語 (überzeugend / einleuchtend / überzeugt sein) に分散している**。両者は重なるが同じではない (例: 「理解はできるが納得はできない」 = 「Ich kann es nachvollziehen, aber ich bin nicht einverstanden」)。

「partial coverage」claim 自体は正しいが、**部分的に覆っている内容** が retrace 側であって acceptance 側ではない、と精密化が必要。

**2. ZH も真の void が empirical 確認された**

ZH-tw subagent が翻訳本では「達成」「直覺」で 納得 layer を脱落させていた事実は既知だったが、native ZH discourse でも単一対応語がないことが確認:

- 中心 phrase: 「**不只是听懂了，而是觉得有道理，心里也能接受**」
- 文脈別に「觉得有道理 / 想通了 / 接受 / 认可 / 信服 / 服气 / 不服 / 明白 / 说得通」と分散
- 「納得感」は中文で一語にしにくいと明示

つまり EN と ZH は両方 **真の void** (multiple paraphrases、single equivalent なし)。

### 4 言語の最終的 void topography (refined)

| 言語 | 「納得」coverage | mechanism |
|---|---|---|
| EN | 真の void | 文脈別 paraphrase: be convinced / accept / make sense / buy-in / be satisfied |
| ZH | 真の void | 文脈別 paraphrase: 觉得有道理 / 想通了 / 接受 / 认可 / 信服 / 服气 |
| DE | **構造的 partial overlap** | nachvollziehbar = retrace のみ、acceptance は別語 (überzeugend / einleuchtend) |
| JA | 単一語で完全 carve | 納得 = retrace + acceptance を統合 |

JA は **retrace + acceptance を一語に統合した稀な carving** を持つ。これは 字義 (納 = take in/accept + 得 = grasp/realize) と古語 「のうとく」(仏教語、初出 1184: 他物を受け入れて自己のものにする) の構造的継続性に支えられている。

### 方法論的観察の追加

本 refinement は **「partial coverage」という coarse な categorization では捉えきれない構造差** が言語間にあることを示す。Type N (理論伝統 activation/block) と区別される、より細かい **「概念の内部構造の部分 carve」** という carving type が観察された:

- 完全 carve (1 言語 = 1 概念単位): JA「納得」
- 構造的 partial carve (内部構造の一部を別語に分配): DE「nachvollziehbar」+「überzeugen」
- 真の void (文脈別 paraphrase で全部分散): EN / ZH

これは [[carving-types-typology]] に Type O (内部構造の言語別 carve 分布) として追加できる候補。
