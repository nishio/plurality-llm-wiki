---
type: source
summary: 3 子 wiki の wishlist (合計 33+ items) を集約した meta-wishlist。subagent では取得できない source を、人間が手動 fetch + raw/ 配置するための作業ガイド。優先度 (easy/medium/hard/specialized) 別に分類。
raw_sources:
  - https://github.com/nishio/plurality-llm-wiki-en/blob/main/wiki/sources/wishlist.md
  - https://github.com/nishio/plurality-llm-wiki-ja/blob/main/wiki/sources/wishlist.md
  - https://github.com/nishio/plurality-llm-wiki-zh-tw/blob/main/wiki/sources/wishlist.md
---

# Meta-Wishlist: 人間支援が必要な source 一覧

## 概要

各子 wiki に `wiki/sources/wishlist.md` があり、subagent (自動 ingest agent) が WebFetch / WebSearch の sandbox 制約で取得できなかった source を記録している。本ページは 3 子 wiki の wishlist を集約し、人間が「どれをどう手動 fetch すれば後続 ingest で取り込めるか」を easy / medium / hard / specialized で分類して提示する。

## 各子 wiki の詳細 wishlist

- EN: [plurality-llm-wiki-en/wiki/sources/wishlist.md](https://github.com/nishio/plurality-llm-wiki-en/blob/main/wiki/sources/wishlist.md) — 14 entries
- JA: [plurality-llm-wiki-ja/wiki/sources/wishlist.md](https://github.com/nishio/plurality-llm-wiki-ja/blob/main/wiki/sources/wishlist.md) — 12 entries (6 グループ)
- ZH-TW: [plurality-llm-wiki-zh-tw/wiki/sources/wishlist.md](https://github.com/nishio/plurality-llm-wiki-zh-tw/blob/main/wiki/sources/wishlist.md) — 7 entries

## 手動 fetch の共通手順

1. 該当 URL をブラウザで開く
2. ページの本文を保存 (簡単には "ページを別名で保存" → markdown / html / pdf)
3. 該当する子 wiki の `raw/<descriptive-name>.md` に置く (`raw/` は gitignored で commit 対象外)
4. 後で subagent 再起動 or 手動 ingest で wiki/ に取り込み

## 優先度別 (ease × impact で並べる)

### 🟢 Easy (open web、paywall なし)

技術的に subagent が取れない (sandbox の domain allowlist 外) だけで、人間が普通に web で読める。fetch コスト極低、impact 大。

| # | Item | Wiki | URL / 場所 | 期待される内容 |
|---|---|---|---|---|
| 1 | 集英社新書プラス連載「Plurality を読み解く」全話 | JA | `shinsho-plus.shueisha.co.jp/news/31459` 〜 `31463` | 駒村圭吾 (④ 既知) 以外の論者 (法学/政治学/哲学) による Plurality 解説 |
| 2 | 報導者 (twreporter.org) Plurality / 唐鳳 関連深度報道 | ZH-TW | twreporter.org で「唐鳳」「g0v」「數位民主」「多元宇宙」検索 | 公益新聞メディアの独立視点記事 |
| 3 | 總統盃黑客松年次成果報告 | ZH-TW | `presidential-hackathon.taiwan.gov.tw` の 2018-2024 PDF | 平方投票 (QV) の政府場域実装年次データ |
| 4 | デジタル民主主義 2030 web / note 連載 | JA | `dd2030.org/kouchou-ai/`、`dd2030.org/idobata/`、`note.com/digitaldemocracy/n/nb228136123f4` (PMF レポート) | 既存 JA wiki ページ「広聴AI」「いどばた」「デジタル民主主義 2030」の根拠補強 |
| 5 | WIRED Japan の Plurality 解説 | JA | `wired.jp/article/what-is-plurality-book/` (チームみらいマニフェストが公式参照) | post-book 解説の中核記事 |
| 6 | Noema (noemamag.com) の Plurality 関連 essay | EN | noemamag.com (一般に paywall なし) | EN 側 Plurality 思想的展開の補強 (Berggruen Institute magazine) |
| 7 | 岡田麻沙 theletter.jp 全 essays | JA | `okadaasa.theletter.jp/` | JA 批判層を網羅 (「チームみらいは誰の声を聞いているのか」以外) |
| 8 | 李舜志『テクノ専制とコモンへの道』記事 | JA | `diamond.jp/articles/-/370383` | 既存 JA wiki entity「李舜志」の根拠補強 |
| 9 | Allison Stanger 関連 essays | EN | `middlebury.edu/faculty/astanger`、`allisonstanger.com` | 本書 co-author の独立 voice (現状 EN wiki に Stanger entity なし) |
| 10 | audreyt.org 個人サイト | EN / ZH-TW | `audreyt.org/` | 唐鳳の中英文 essays / 講演 / 訪談 (wiki 森全体のソース) |

### 🟡 Medium (paywall / 部分公開)

| # | Item | Wiki | URL / 場所 | 注意 |
|---|---|---|---|---|
| 11 | Foreign Affairs の Plurality / Tang / Weyl 関連 | EN | foreignaffairs.com で検索 | paywall。購読者 access 推奨 |
| 12 | 端傳媒 (theinitium.com) の唐鳳・g0v 報道 | ZH-TW | theinitium.com | paywall (subscription model) |
| 13 | Wired (英語版) の Plurality 関連 | EN | wired.com | 一部 paywall |

### 🔴 Hard (SNS / login walls)

| # | Item | Wiki | URL / 場所 | 取得難度 |
|---|---|---|---|---|
| 14 | 鈴木健 SNS / note / Substack | JA | `@kensuzuki` (Twitter)、`note.com/ken_suzuki/` 等 | SNS scraping は技術的困難、手動 select |
| 15 | 安野貴博 SNS | JA | `@takahiroanno`、note、YouTube「AI あんの」 | 同上 |
| 16 | 法学者・政治学者・哲学者の SNS Plurality 言及 | JA | 東浩紀、宮台真司 等 | 1 年分 (2025-05〜2026-05) を巡回 |
| 17 | PDIS sayit archive | ZH-TW | `sayit.pdis.nat.gov.tw` (status uncertain — 唐鳳退任後 archive 化されている可能性) | まず存在確認 → 代表的 10 篇エクスポート |

### 🟣 Specialized (academic / 特殊 access)

| # | Item | Wiki | URL / 場所 | 必要 access |
|---|---|---|---|---|
| 18 | 中央研究院 学術論文 | ZH-TW | 華藝線上圖書館 `airitilibrary.com` | 機関契約 access |
| 19 | g0v.hackmd.io 重要会議記録 | ZH-TW | HackMD 個別 page | 特定 page を手動 export |
| 20 | 台灣《證券投資信託及顧問法》修正案 | ZH-TW | 全国法規資料庫 | 法規資料庫から条文 + 立法理由書 |
| 21 | Civic AI Conference 2026 非 Tang speakers の primary source | EN | Picard / Tronto / Gabriel+Neff+Tennison / Negi+Gayche / Farquharson / Palyutina+Agnew | 各 speaker の institutional page、Oxford 録音 |
| 22 | RxC blog / Glen Weyl 個人 essays / MSR Plural Technology Collaboratory | EN | radicalxchange.org/media/blog/、glenweyl.com、MSR blog | 手動 fetch |

## 観察された pattern

3 子 wiki の wishlist を集約して見える共通 pattern:

1. **失敗の中心は SNS と新聞・出版社 / メディア domain** — sandbox の WebFetch allowlist が `github.com` `plurality.net` 中心で、それ以外の domain を必要とする任務はほぼ失敗
2. **逆に成功するのは GitHub-hosted markdown** — 本書 upstream、OSS organization の README、共著者の GitHub blog (vitalik.eth.limo via `vbuterin/blog`)、PDIS の `web-jekyll` repo 等
3. **「Plurality 関連 critical reception」が最も網羅困難** — 出版社サイト (集英社) / 知識人 letterboxd / 学術論文 / SNS の批評はほぼ全部 sandbox 外
4. **GitHub に migrate されている content には特に強い** — 本書、civic.ai、team-mirai/manifesto-body 等 OSS-published material は容易に取れる。pluralitybook の運営戦略が偶然 subagent-friendly

## 注意点

- `raw/` は gitignored で各子 wiki repository に push されない (commit 対象外)
- 手動取得した content は license / copyright を尊重して保存 (CC0 / public domain なら自由、paywalled article は局所利用のみ)
- 取得後、wiki に取り込む際は wiki の規約 (frontmatter / wikilink) に従って ingest

## Open Questions

- 本 wishlist を quartile に分割した optimal な人間 task design は? (例: 🟢 Easy 10 件を 1 セッションで処理など)
- WebFetch allowlist の拡張要請が現実的か? (技術的に設定可能だが、安全性・rate limit の trade-off あり)
- pluralitybook 上流が将来 GitHub から離脱した場合、自動 ingest 経路が広く失われる — 本 wiki 森の resilience 戦略は?
