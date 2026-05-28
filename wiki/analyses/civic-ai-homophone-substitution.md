---
type: analysis
summary: 唐鳳が「civic AI」を中文に訳す際、直訳の「公民 AI」「市民 AI」を採らず、人工智慧 (AI) を pun させた「仁工智慧」を選んだ。「人→仁」は同音異字 substitution で、字面を変えて漢字の表意性 (仁 = 儒家の benevolence) を新たに召喚するメカニズム ── kanji-as-ja-zh-bridge とは逆方向の cross-language carving 戦略。
sources:
  - correspondences.yaml
  - https://github.com/nishio/plurality-llm-wiki-zh-tw/blob/main/wiki/concepts/仁工智慧.md
  - https://github.com/nishio/plurality-llm-wiki-en/blob/main/wiki/concepts/Civic-AI.md
---

# Civic AI の同音替字翻訳: 「人工」→「仁工」

## 観察

唐鳳が EN "Civic AI" / 6-Pack of Care framework を中文化する際、選んだ訳語は **「仁工智慧」** だった。直訳経路の「公民 AI」「市民 AI」を採らない。

メカニズム:
- 既存の 人工智慧 (rén-gōng zhì-huì = artificial intelligence, AI) の **人 (rén) を 仁 (rén) に同音置換**
- 字面を変えて、漢字の表意性 (仁 = 儒家の benevolence、四端の中心徳) を新たに召喚
- 「人が作った」→「仁が作った」と意味を pivot

## 三経路の比較

| 訳語経路 | 倫理的 root | Agent の像 | 評価軸 |
|---|---|---|---|
| **civic AI** (EN) | Latin *civitas* → 共和主義的市民徳 | 市民を support する道具 | 市民にどう奉仕するか (instrumental) |
| **公民 AI / 市民 AI** (直訳経路、不採用) | 公的人格としての市民 | 同上 | 同上 |
| **仁工智慧** (唐鳳訳) | 儒家の四端 (仁義禮智) | **君子的徳を embody する存在** | **人間性を涵養するか** (substantive virtue) |

EN「civic」は agent の **public との関係性** を front loading するのに対し、zh-tw「仁」は agent の **内的 virtue** を front loading する。両者は哲学的に違う対象を語っている可能性がある。

## kanji-as-ja-zh-bridge との対比

両方とも漢字を媒介とした cross-language 現象だが mechanism が逆方向:

| 観察 | 仕組み |
|---|---|
| [[kanji-as-ja-zh-bridge]] | **字面が同じ→意味が共有される** (ja-zh 直結、新字体↔繁體字の微差は許容)。例: ja `多元投票` ↔ zh `多元投票`、ja `分人` ↔ zh `分人` |
| 仁工智慧の同音替字 | **字面を変えて (homophone replacement)→新たな意味層を召喚する**。例: 人工 → 仁工 |

後者は **kanji の表意性 (ideographic affordance) を creative に活用した翻訳戦略**。同音語が表意文字を持つ Chinese 圏固有のメカニズムで、EN にも (本格的には) JA にも equivalent がない。

英語の同音語 wordplay (例: "AI" / "I" / "eye") は綴り字が違うため意味の重層化が **音だけ** に留まる。漢字圏では同音語の **意味を視覚的に重ねる** ことが可能 — そこが zh-tw 翻訳者の独自リソース。

## JA はまだこの概念を carve していない

JA wiki に Civic-AI 概念ページが現時点 (2026-05-28) ない。JA が将来 ingest するとき、3 つの選択肢が考えられる:

1. **シビック AI** (katakana loanword) — JA の dominant 翻訳戦略から予測される第一候補。neutral だが儒家 layer は失われる
2. **公民 AI / 市民 AI** — 直訳、Confucian color なし
3. **仁工知能 / 仁 AI** — zh-tw からの kanji 逆輸入、儒家 layer を継承

JA 翻訳者 (山形浩生 か別人か) が「仁」を採用するかは興味深い観察対象。日本にも儒家伝統 (江戸期朱子学 / 陽明学、武士道) は存在するが、**現代日本語 AI discourse での「仁」は希薄**。zh-tw の 仁工智慧 lineage を JA が借入するか、それとも independent に katakana 化するか — これは [[loanword-retention-patterns]] が観察する翻訳者 agency の問題が、別の概念領域でどう発動するかの test case になる。

## 概念空間への影響

`correspondences.yaml` の単純な対応 row (en: Civic-AI ↔ zh-tw: 仁工智慧 ↔ ja: ?) では、この microstructure は見えない。両者を「同じ topic」として一行で結ぶことで、**翻訳者が概念空間に行った非自明な仕事が消える**。

これは Wikipedia の interlanguage link が抱えるのと同じ問題で、本 wiki 森が `analyses/` を持つ理由でもある: **対応の主張は緩やかに、その背後の微細な carving 差異は別途記録する**。

## Open Questions

- 唐鳳の「仁」選択は意図的な儒家連結か、それとも字面遊びが主で意味は後付けか? 唐鳳自身の発言で「仁工智慧」の選択理由を述べた箇所があれば、本 analysis を裏付けられる
- 仁工智慧 がどこまで定着しているか? PDIS 公式文書 / 媒体 / 学術論文での usage 頻度。一過性の唐鳳 personal usage なのか、コミュニティ標準語に近づいているのか
- 同音替字翻訳の他例: zh-tw 圏には他にも「人」→「仁」/「智」/「治」などの substitution 翻訳があるか? Plurality 関連概念で複数発生していれば、これは唐鳳 / PDIS の一貫した翻訳戦略
- 仁 が捕まえている儒家概念のうち、Plurality と整合的なのはどの面か? Mencius の「惻隠之心」(empathy) は care framework と直結するが、Confucian 統治論の elitist 側面 (君子→民) は Plurality の democratic 側面と緊張する。この緊張が「仁工智慧」名乗りの代償か
