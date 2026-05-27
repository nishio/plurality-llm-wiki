---
type: analysis
summary: correspondences.yaml に zh column を annotation として追加すると、ja-zh 対応 (39 件) は en-ja 対応 (23 件) より dense になる。さらに 11 件は ja-zh で漢字を直接共有しており、「漢字が二言語間の道になる」 (words-as-public-goods-lt) の経験的検証となる。
sources:
  - correspondences.yaml
  - words-as-public-goods-lt.md
---

# Kanji as a ja-zh bridge: correspondences.yaml への zh column 実験

## 実験の動機

[[words-as-public-goods-lt]] (西尾, 2024-01-03) は翻訳実務上の観察として「英語→日本語より中国語→日本語の方が自然になることが多い。中国語と日本語は漢字という共通の表意文字体系を共有しており、漢字が意味を伝える『道』になる」と論じた。

この LT は派生 Open Question:

> 「漢字が二言語間の道になる」という観察は en ↔ ja の plurality-llm-wiki に組み込めるか? 現在の `correspondences.yaml` は en / ja の 2 column だが、zh column を追加した場合、ja-zh 対応の方が en-ja より dense になる可能性がある (本 LT の観察の検証)。

を残していた。本 analysis はこの hypothesis を経験的に test する。

## 方法

2026-05-27 時点の `correspondences.yaml` (56 entries) に `zh` 列を annotation として追加した。Plurality 本は元来 en/zh (繁體中文) バイリンガル出版であり、唐鳳が中文で書いた章を Glen Weyl が英訳した過程で発生した語彙が多いため、各概念の zh 表記は本書本文または周辺資料から調達可能。

JA-only エントリ (鈴木健 lineage, ブロードリスニング 等) については、その概念が中文の Plurality 言説でも参照されている場合に限り zh 列を充填、独自の日本概念には `~` を維持した。

注: 本実験時点で [`plurality-llm-wiki-zh-tw`](https://github.com/nishio/plurality-llm-wiki-zh-tw) 子 wiki は GitHub repo 作成済みだが seed page (1 source + 1 concept) のみ。zh-tw 列は実証用 annotation でもあり、子 wiki populate の進行と並走で精緻化される想定。

## Density 結果

|  | both non-null entries |
|---|---|
| en-ja | 23 |
| en-zh | 37 |
| **ja-zh** | **39** |

ja-zh (39) は en-ja (23) より 70% 以上 dense。**hypothesis 支持**。

ただし en-zh (37) も ja-zh (39) とほぼ同等。zh は en と ja のどちらにも (book bilingual の出版状況により) 直接接続している。en-ja が低いのは、JA-only post-book lineage (鈴木健 / 安野貴博 / デジタル民主主義 2030) に EN 対応がないことが主因で、これは book bilingual 構造ではなく **JA コミュニティの post-book 拡張** が引き起こす asymmetry。

## より強い観察: 直接 kanji-bridge の 11 事例

count density ではなく、ja-zh の language distance を見ると、11 entries で漢字が直接 bridge となっている (新字体↔繁體字の字形差を許容):

| ja | zh | 字形差 |
|---|---|---|
| 多元投票 | 多元投票 | 完全一致 |
| 社会市場 | 社會市場 | 会↔會 |
| 反社会 | 反社會 | 会↔會 |
| 中央集権 | 中央集權 | 権↔權 |
| 国家 | 國家 | 国↔國 |
| 資本主義 | 資本主義 | 完全一致 |
| 分人 | 分人 | 完全一致 |
| 分人民主主義 | 分人民主主義 | 完全一致 |
| 數位 | 數位 | 完全一致 (JA は中文を直接 borrow) |
| 玉山[からの眺め] | 玉山[觀點] | 共通根 "玉山" |
| PICSY | PICSY | 同 acronym |

これは en-ja 対応では成立しない構造。例えば en `Plural-Voting` ↔ ja `多元投票` ですら、kanji 経路は ja-zh 側 (多元投票 ↔ 多元投票) からきている — EN 直接ではなく **ZH を経由した kanji が JA に着地している**。

## 翻訳者 agency が ZH 経路を選ばない事例

ただし JA 翻訳者 (山形浩生) は常に ZH 経路を採るわけではない:

| en | zh | ja (山形訳) | 採られた経路 |
|---|---|---|---|
| Quadratic-Voting | 平方投票 | クアドラティック投票 | **EN** (katakana loanword) |
| Quadratic-Funding | 平方融資 | クアドラティック資金調達 | EN + 訳 hybrid |
| Liquid-Democracy | 流動民主 | 液体民主主義 | 独自訳 (zh の "流動" を採らず "液体" を選択) |
| Digital-Democracy | 數位民主 | デジタル民主主義 | **EN** (katakana loanword) |

`平方投票` の漢字熟語が JA でも完全に読解可能であるにもかかわらず、山形浩生は「クアドラティック投票」とカタカナを採用した。「液体民主主義」では zh の "流動" を採らず独自に "液体" を選んだ。

つまり ZH 経路は **available** であるが、翻訳者は概念ごとに「ZH 経路 (kanji import) / EN 経路 (katakana loanword) / 独自訳」を curate している。

## 「kanji-bridge」の真の意味

LT の主張は単に「ja-zh の漢字共有がある」ではなく、**翻訳者がその bridge を採るかどうかは選択** という point を含意していた。本実験はそれを確認する:

1. **available な漢字経路** が ja-zh 間に多数存在することは確認 (11 事例 + 名前部分一致多数)
2. **翻訳者の選択** によりその経路は採られたり採られなかったりする
3. **結果として deposit される語彙** は zh-shared kanji (多元投票, 社会市場, …) と en-loaned katakana (クアドラティック投票, デジタル民主主義, …) が混在する

## void と kanji-bridge の交差

[[words-as-public-goods-lt]] の中核主張は void の概念だった。本 zh annotation で発見された注目すべき void:

- **`數位` の en void**: ja-only として登録されていた `數位` は、実は zh で **同字形そのまま** 存在する。en には「digital と plural の合成語」概念は語として存在せず、Tang/Weyl が ⿻ という Unicode 記号で代用する。これは「en にだけ void、ja-zh は kanji shared」という非対称構造の典型
- **`分人` の en void**: 平野啓一郎が日本語で coined、鈴木健が拡張した概念。zh で「分人」字面読解可能。en には対応語なく "dividual" など neologism で訳されることがあるが定着していない
- **`玉山` の en void**: 玉山 (Yu Shan) は本書 2-1 章「玉山觀點」の地名で、JA はそのまま borrow し「からの眺め」を付加。EN 章タイトル "View from Yushan" は地名のローマ字転写となり kanji 経由の "意味の重み" が失われる

これらは LT が予言した「en に void、ja-zh は kanji 経由で語彙を共有する」事態の実例。

## 帰結

LT のテーゼは support された:

- **(a) ja-zh は en-ja より dense** (本 registry で 39 vs 23、約 70% 増)
- **(b) 漢字経路は available だが選択的** (11 entries で直接 kanji bridge、しかし山形浩生は概念ごとに ZH 経路 / EN 経路を curate)
- **(c) en の void が ja-zh で埋まる構造** (數位 / 分人 / 玉山 など)

## Open Questions

- `plurality-llm-wiki-zh-tw` 子 wiki を実際に populate した場合、本 annotation 由来の density 推定はどう変わるか。zh-tw コミュニティ独自の post-book 拡張 (本書中文版以降の議論) が登場すれば、zh-tw-only エントリも発生するはず
- 「翻訳者 agency による経路選択」自体を別 analysis として整理する価値あり。なぜ「液体民主主義」だが「クアドラティック投票」なのか、概念ごとの選択基準
- en-zh 経路の density (37 件) は ja-zh (39 件) とほぼ同じ。LT は「zh→ja の bridge」を主軸に論じたが、本実験は「zh が hub になり en/ja の両方を bridge する」ハブ構造を示唆する。ko 列を追加したらどうなるか
