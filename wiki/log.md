# Log

> 直近 7 日分のみ。全件 compact 履歴は [log.txt](log.txt)、それより古い entry の詳細は `git log -- wiki/log.md` で参照。
> 更新は `python3 scripts/refresh_logs.py` で log.txt と log.md を再生成する。

## [2026-05-28 11:00] filing-back | connotation asymmetry の observation を [[words-as-public-goods-lt]] に追記


README 表記の議論 (parent `c93f384`、ja `f344c34`) で出た observation を [[words-as-public-goods-lt]] の `## Updates` として filing back:

- 「wiki が見れるところ」という meta-notion をラベリングする際、JA「公開/公式サイト」は authoritative の含意を持つが、EN「Live site」/ ZH「公開網站」は中立
- LT の中核主張は「言語の voids」(対応語がない) だったが、本事例は「対応語はあるが connotation が違う」という refinement
- 本 wiki 森自身を書く過程で LT の理論が再帰的に体現された

## [2026-05-27 16:30] filing-back | registry と child wiki の双方向遅延 pattern を [[wiki-forest]] に追記



show_gaps.py の label 議論で出た構造的 observation を [[wiki-forest]] の `## Updates` として filing back:

- **registry-ahead (pending)** の 4 pattern: 新言語 column 追加直後 / Index 先行 / sibling 予測 / 上流変更先取り
- **child-wiki-ahead (unmapped)** との対称構造
- 両者が 0 でない方が「森が育っている健全な状態」、定常的に少し非ゼロが望ましい、という運用的 implication

## [2026-05-27 16:00] sync | (A) yaml の推測 fix + show_gaps.py の誤解招く label を修正




zh-tw subagent の book 観察と yaml annotation の食い違い 2 件を修正:

- `Augmented-Deliberation`: `zh-tw: 增強審議` → `擴增審議` (本書中文版 5-4 章タイトル)
- `Identity-and-Personhood`: `zh-tw: 身分認證` → `身分與人格權` (本書中文版 4-1 章タイトル、私の guess は ID verification の narrower 訳語だった)

並走で `scripts/show_gaps.py` の section #3 label を "Dangling references" → "Pending pages" に変更。"Dangling" は壊れた参照のニュアンスがあるが、実態は **registry が child wiki ingest より先行している sparse 状態** であり error ではない。各項目は将来 ingest の TODO、または検証できなければ `~` に retract できる、と明示。

## [2026-05-27 15:30] sync | correspondences.yaml の 2 件 naming follow-up





子 wiki の今回 ingest で発生した naming 整合性を反映:

- `なめらかな社会とその敵` の `en` を `~` → `Nameraka-Society` に更新。本書 upstream PR #1055 (2024-12-21) で 3-3 章「Quality Control and Nameraka Society」として 37 行の新規 sub-section に逆統合済み (EN wiki も page あり)
- `玉山からの眺め` の `zh-tw` を `玉山觀點` → `玉山視野` に修正。本書中文版の実際の章タイトルは「玉山視野」(zh-tw subagent が book から確認)

残る 28 件の zh-tw dangling refs (`身分認證` vs `身分與人格權` 等の訳語差) は別タスクとして残置。

## [2026-05-27 13:30] ingest | zh-tw 子 wiki を新規 scaffold (filesystem のみ)








[[words-as-public-goods-lt]] の漢字-道 観察 + [[kanji-as-ja-zh-bridge]] の経験的 support を受けて、第 3 の言語 wiki `wikis/plurality-llm-wiki-zh-tw/` を filesystem 上に scaffold (GitHub repo は未作成):

- `CLAUDE.md` / `wiki/index.md` / `wiki/log.md` を新規作成、scripts (build_index_txt / refresh_logs / lint_wiki) を ja からコピー
- シード source: 為何我是多元宇宙人 (Glen Weyl 2022-02-10, PDIS 平台, CC BY-NC-SA 4.0)
- 最初の concept: 多元 (Plurality の zh-tw 訳語、書本基底。変体: 多元宇宙 = Glen Weyl PDIS / 多元性 = 直譯)

並走で correspondences.yaml の `zh` column を `zh-tw` に rename (56 entries 全て)、kanji-as-ja-zh-bridge analysis 内の子 wiki 名 reference を更新。analysis 自体の filename は kanji-as-ja-zh-bridge のまま (zh = 漢字圏全体を指す総称として保持)。

## [2026-05-27 13:00] analysis | correspondences.yaml に zh 列を annotate、kanji-as-ja-zh-bridge を filing









words-as-public-goods LT (2024-01) が残した Open Question「zh 列を追加した場合 ja-zh 対応は en-ja より dense になるか」を経験的に test:

- `correspondences.yaml` の 56 entries に zh 列を annotation として追加 (本書 en/zh バイリンガル出版を活用、JA-only 概念は zh で読解可能なら充填)
- 結果: en-ja = 23 / en-zh = 37 / **ja-zh = 39**。LT 仮説支持 (ja-zh > en-ja で 70% 増)
- 直接 kanji-bridge 11 entries (多元投票 / 数位 / 分人 / 玉山 / 社会市場 / 国家 / 資本主義 etc.) を [[kanji-as-ja-zh-bridge]] に整理
- 山形浩生訳が「クアドラティック投票」では zh 経路 (平方投票) を採らず EN 経路を採ったことなど、翻訳者 agency による経路選択も観察

## [2026-05-27 12:00] concept | wiki-forest をメタ概念ページ化、英語 README から「wiki森」表記を除去










英語 README に紛れていた「wiki森」(英語読者には読めない) を `wiki forest` に置換し、forest metaphor の 1 段落説明を追加。同時に本 architecture のメタ概念として [[wiki-forest]] を `wiki/concepts/` に新規作成 (parent concepts/ の初ページ)。木 = 各言語独立 wiki、forest = 横断観察の場、`correspondences.yaml` = 森の地図、`analyses/` = 観察記録 という分解を明示し、Wikipedia の interlanguage link との差別化点 (対応欠落を first-class observable 化 / 差異を分析対象化) を整理。

## [2026-05-27 11:30] filing-back | push の非対称性 (activity vs word) を analysis 化











[[words-as-public-goods-lt]] の Open Question を修正する過程で、ユーザーから cross-language push のコスト非対称性と時間順序の仮説が示された。

- activity (事実) push: 受け取り側コスト低、既に Plurality 本最新オンライン版に反映済み ([[japan-reverse-import]])
- word (概念) push: 受け取り側に void が必要 + hosting コスト高、活動が articulate 不足を露呈した後に事後的に起こる

[[push-asymmetry-activity-vs-word]] として analysis 化。`correspondences.yaml` の `~` 記録が word push の前提条件 (受け取り側 void) の observable 化になっている点も整理。

## [2026-05-27 11:00] ingest | sources/ に本 wiki 森の発想の根底 LT を登録












本 multilingual wiki 森 architecture の発想の根底である西尾 LT「Words as Public Goods / 公共財としての言葉」(2024-01-03, Plurality Tokyo "Glen in Japan") を [[words-as-public-goods-lt]] として sources/ に追加。

CC-0 license の Scrapbox ページから論証チェーン (Plurality ↔ チームワークあふれる社会、二言語の道としての漢字、納得型 void、日本語話者のマイノリティとしての公共財輸出) を抽出し、本 wiki 森 architecture との対応 (`correspondences.yaml` の `~` = void、`analyses/` で文節化差を分析する設計) を明示。

## [2026-05-26 22:30] filing-back | 同じ概念の文節境界 / 説明差を扱う 5 analysis を追加













両 wiki の対応 page pair を実際に読み比べて、同じ概念に対する両言語の articulation 差を 5 件 analysis 化:

- [[plural-voting-lineages]]: 多元投票 ↔ Plural-Voting (理論的祖先の選び方)
- [[augmented-deliberation-examples]]: 拡張熟議 ↔ Augmented-Deliberation (canonical example)
- [[quadratic-voting-framings]]: クアドラティック投票 ↔ Quadratic-Voting (説明の重心)
- [[plurality-definition-framings]]: プルラリティ ↔ Plurality (概念の外周)
- [[loanword-retention-patterns]]: 山形浩生訳のカタカナ残し / 翻訳の選び分け

なお既存 [[suzuki-ken-lineage]] と [[japan-reverse-import]] は「同じ概念の境界差」ではなく「JA 固有 lineage 記録」として index.md でセクション分離。

## [2026-05-26 21:00] filing-back | 子 wiki の ingest と correspondences.yaml 整備から得た cross-language carving observations














両子 wiki への Plurality 本 ingest (EN: source + 36 concepts + 45 entities、JA: source + 41 concepts + 35 entities) と correspondences.yaml への全 79 concept 登録から、3 つの文節化差異の pattern を analyses/ にページ化:

- [[suzuki-ken-lineage]]: JA 固有の鈴木健由来 lineage 4 concept
- [[role-vs-ideology-noun-split]]: 日本語の外来語形態が drive する concept split
- [[japan-reverse-import]]: 本書執筆後の日本コミュニティ実践が JA 版に逆輸入される pattern
