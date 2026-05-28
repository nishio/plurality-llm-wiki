# plurality-llm-wiki

[English README](README.md)

各言語の Plurality 言説を自律的な wiki として持ち、同じ概念空間が言語ごとにどう違って文節化されるかを観察・分析する多言語 **wiki森**。

> Wikipedia は言語間の概念の文節化の差異を *observe* するが、分析はしない。この wiki森 は分析もする。

**閲覧 URL:** https://nishio.github.io/plurality-llm-wiki/

## なぜこの project が存在するか

Plurality ── Audrey Tang と E. Glen Weyl による「社会的差異を超えたコラボレーションのための技術」── は、それ自体が「多様性が価値を生む」ことについての project である。各言語で言説が発展するにつれ、コミュニティは概念空間を微妙に違うやり方で文節化する: どの概念に名前が付くか、どの loanword が定着するか、どの系譜が前景化されるか。

これらの wiki を互いに翻訳してしまうと、研究すべき差異そのものが消える。そこで本 project は各言語 wiki を自律させ、文節化の差異それ自体を分析対象とする。

## Repository 構成

これは **parent repo**。以下を持つ:
- 言語間対応の registry (`correspondences.yaml`)
- meta-wiki (`wiki/`) ── cross-language analyses が住む
- 共有 scripts と GitHub Pages 用 Quartz 設定

各言語 wiki は **独立した GitHub repo** で、別々に admin / contributor が参加できる:

| Wiki | Repo | 閲覧 URL |
|---|---|---|
| 英語 | [nishio/plurality-llm-wiki-en](https://github.com/nishio/plurality-llm-wiki-en) | https://nishio.github.io/plurality-llm-wiki-en/ |
| 日本語 | [nishio/plurality-llm-wiki-ja](https://github.com/nishio/plurality-llm-wiki-ja) | https://nishio.github.io/plurality-llm-wiki-ja/ |
| 繁体中文 (台湾) | [nishio/plurality-llm-wiki-zh-tw](https://github.com/nishio/plurality-llm-wiki-zh-tw) | https://nishio.github.io/plurality-llm-wiki-zh-tw/ |
| ドイツ語 | [nishio/plurality-llm-wiki-de](https://github.com/nishio/plurality-llm-wiki-de) | https://nishio.github.io/plurality-llm-wiki-de/ |

N 言語目への拡張は: `plurality-llm-wiki-<lang>` という repo を作り、`correspondences.yaml` にその言語 column を追加するだけ。

## 仕組み

**各言語 wiki は自律的**。en 側の concept page が ja 側に翻訳として存在する必要はないし、その逆もない。片方の言語にしか存在しない概念は、それ自体が一級の観察対象。

**Interlanguage link は緩やか**。`correspondences.yaml` は Wikipedia の interlanguage link に相当する ── 行は「これらのページは同じ/関連する話題について」と主張するだけで、内容の等価性は主張しない:

```yaml
- en: Plurality
  ja: プルラリティ

- en: ~                  # 英語側に対応単語なし → 記録された観察
  ja: <ja-only-concept>

- en: <en-only-concept>
  ja: ~
```

**文節化の差異は本 parent repo の `wiki/analyses/`** に住む ── 実運用の中で見つかったものを ad-hoc に記録するもので、仮説を先取りはしない。

## Contributor 向け

- 運用詳細とページ規約: [CLAUDE.md](CLAUDE.md)
- registry の言語別欠落検出: `python3 scripts/show_gaps.py`
- index / log の regenerate: `python3 scripts/build_index_txt.py`, `python3 scripts/refresh_logs.py`

## License

各言語 wiki のコンテンツは個別 repo の LICENSE に従う。本 parent repo の scripts / schema は再利用可能 ── 詳細は個別ファイルを参照。
