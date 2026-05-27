# plurality-llm-wiki

## テーマ

各言語で自律的に発達した Plurality 概念体系を、言語ごとに独立した wiki として持ち、それらをまたぐ「概念の文節化の差異」を観察・分析する多言語 wiki森。

> **Wikipedia は言語間の概念の文節化の差異を observe するが、分析はしない。この wiki は分析もする。**

## アーキテクチャ

```
plurality-llm-wiki/                       # この repo (parent, github: nishio/plurality-llm-wiki)
├── CLAUDE.md                              # このファイル
├── correspondences.yaml                   # 言語間の概念対応 registry (機械可読)
├── raw/                                   # parent-level の生ソース (gitignored)
├── wiki/                                  # parent 自身の wiki content (cross-language analyses)
│   ├── index.md / index.txt               # 人間 / AI 向け navigation (kouchou pattern)
│   ├── log.md / log.txt
│   ├── concepts/  entities/  sources/
│   └── analyses/                          # 言語間の文節化差異の観察・分析
├── scripts/
│   ├── lint_wiki.py                       # wiki 健全性チェック
│   ├── build_index_txt.py                 # index.txt を frontmatter から regenerate
│   ├── refresh_logs.py                    # log.txt と log.md(直近7日) を同期
│   └── show_gaps.py                       # correspondences.yaml の言語別欠落を列挙
├── quartz/                                # GitHub Pages 配信用 Quartz
├── quartz.config.ts  /  quartz.layout.ts
├── package.json  /  pnpm-lock.yaml
├── .github/workflows/deploy-pages.yml     # main push で Pages 自動 deploy
└── wikis/                                 # 子言語 wikis (gitignored, 独立 repo)
    ├── plurality-llm-wiki-en/             # github: nishio/plurality-llm-wiki-en
    ├── plurality-llm-wiki-ja/             # github: nishio/plurality-llm-wiki-ja
    └── plurality-llm-wiki-zh-tw/          # github: nishio/plurality-llm-wiki-zh-tw
```

各言語 wiki は **独立した GitHub プロジェクト** として運営され、別 admin / contributor が参加できる。filesystem 上は `wikis/` 配下に nest するが、git 管理は完全に独立。

## Wikipedia メタファー

- **各言語 wiki は自律**: 各言語の concept page は独自の文節化を持ち、他言語の翻訳である必要はない
- **interlanguage link は緩やか**: `correspondences.yaml` で「同じ/関連する話題」と主張するだけで、内容の等価性は主張しない
- **片方にしか存在しない概念は単にリンクなし**: ja-only / en-only の概念は他言語側に stub を置く必要なし
- **N 言語への拡張が自然**: `plurality-llm-wiki-<lang>` を追加 → `correspondences.yaml` に該当言語 column を足すだけ

## 「差異が価値を生む」

「対応するはずの概念が言語によって少し解釈に違いがある」── これは Plurality 的に面白いことで、差異それ自体が価値を生む。本 wiki の運用が、本 wiki の主題 (多元性) を体現する構造になっている。

## 言語間対応の registry

`correspondences.yaml` が機械可読な言語間対応データ:

```yaml
- en: Plurality
  ja: プルラリティ
  # 将来 ko: ...  zh: ... を追加可能

- en: ~        # 英語に対応単語なし → 観察対象
  ja: <ja-only-concept>
  notes: 日本語イベントで言語化された概念で en 圏に対応する単一語がない

- en: <en-only-concept>
  ja: ~        # 日本語に対応単語なし
```

`null` (`~`) で表現した欠落を `python3 scripts/show_gaps.py` で列挙する。
新しい concept page を子 wiki に作ったら、対応する correspondence entry を追加するか、明示的に「片側のみ」として登録する。

## ページルール

### 全ページ共通
- 冒頭に YAML frontmatter: `type`, `summary`, `sources`
- 主張には出典を明記: `[[source名]]より`
- 矛盾・未解決の論点は `## Open Questions` で明示
- 更新は上書きせず `## Updates` で追記
- リンク書式は `[[Page Name]]` (double brackets, Wikipedia 形式)

### フロントマター例
```yaml
---
type: analysis
summary: 言語間の文節化差異についての観察 1 文
sources:
  - source-page-name.md
---
```

## 操作

### この parent wiki の役割
- **必須**: プロジェクト自体の解説 (CLAUDE.md, index.md, README)
- **創発**: 子 wiki を運営する中で発見された「言語間の文節化差異」を `wiki/analyses/` に記録
- **非役割**: 個別概念は子 wiki に住む。parent の concepts/entities/sources はメタ概念のみ

### Ingest / Query / Lint
基本フローは [[kouchou-ai-developer-wiki]] と同じ kouchou pattern:
- `wiki/index.md` 人間向け curated nav / `wiki/index.txt` AI 向け full catalog (auto-gen)
- `wiki/log.md` 人間向け直近 7 日 full / `wiki/log.txt` AI 向け全件 compact (auto-gen)
- ページ追加・rename・削除後は `python3 scripts/build_index_txt.py`
- ingest / filing-back 後は log.md 先頭に追加し `python3 scripts/refresh_logs.py`

### Gap 検出
```sh
python3 scripts/show_gaps.py
```

correspondences.yaml の言語別欠落と、子 wiki に存在するが registry 未登録の concept page を列挙する。

## GitHub Pages

main へ push すると `.github/workflows/deploy-pages.yml` が Quartz でビルドして Pages に deploy する (URL: https://nishio.github.io/plurality-llm-wiki/)。子 wiki も同様の workflow で各自の URL に deploy される。

## 運用方針

- ソースは「参考」であり無批判に採用しない
- 仮説 (「言語で文節化がズレる」) は実運用の結果として自然に蓄積されることを期待し、無理に先取りしない
- 実験を通じて得た気づきを重視
- スキーマ (このファイル) も実験を通じて改善していく
