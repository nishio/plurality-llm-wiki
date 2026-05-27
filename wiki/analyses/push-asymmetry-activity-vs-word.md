---
type: analysis
summary: 少数言語 → 多数言語の cross-language push には activity(事実) push と word(概念) push の 2 種類あり、コストと時間順序が非対称。activity は事実なので受け取り側コストが低く先に push されやすい。word は対応 void を hosting するコストが高く、活動が articulate 不足を露呈した後に事後的に借入される、という仮説。
sources:
  - words-as-public-goods-lt.md
  - japan-reverse-import.md
---

# Push の非対称性: activity vs word

## 観察

[[words-as-public-goods-lt]] は「少数言語話者が独自に発達させた語彙を public goods として輸出することで世界全体の知的生産性が上がる」と論じた。LT から 2 年経過した 2026 年時点での実際の cross-language push を見ると、push される対象は均質ではなく、少なくとも 2 種類に分けられる。

| 種類 | 例 | 受け取り側コスト |
|---|---|---|
| **活動 (activity / fact) の push** | 安野貴博 2024 都知事選のブロードリスニング実装、デジタル民主主義 2030 プロジェクト | 低い。事実なので observe + 記述するだけ |
| **言葉 (word / concept) の push** | 「納得」型 void を埋める源言語の語彙借入 | 高い。受け取り側に void が存在し、新概念として hosting する必要 |

Plurality 本最新オンライン版には日本語コミュニティから英語コミュニティへの活動 push が反映済み (cf. [[japan-reverse-import]])。これは [[words-as-public-goods-lt]] の Open Question で当初「言葉の輸出は実装されていない」と書きかけたところを訂正する必要が出た発見でもある: 実装されているのは活動 push であり、word push はまた別の話。

## なぜコストが非対称か

**活動 push** は、受け取り側にとって以下で完結する:
1. 「日本でこういう実装/事例があった」と認識する
2. 既存の母語語彙 (broad listening, digital democracy 等) で十分に articulate できる
3. 本の改訂や記事で言及する

ここに対応概念の不在 (void) は不要。むしろ既存概念の例示として組み込まれる。

**言葉 push** は、それが有益であるためには以下の条件が必要:
1. 受け取り側言語に **対応概念がない (void である)** ── これが価値の源泉
2. 受け取り側が void を identify する (これ自体が能動的作業)
3. 源言語の語彙を音借りまたは意訳して新概念として host する
4. 周辺概念との関係を新言語コミュニティ内で再構成する

3-4 は「自分の言語に新しい概念を導入する」コストであり、活動の事例言及より格段に高い。

## 時間順序の仮説

上記のコスト構造から、**活動 push が先、言葉 push が事後** という時間順序が予測される:

1. ある言語コミュニティで実装/活動が生まれる (例: 都知事選のブロードリスニング実装)
2. 多言語側がその活動を事例として取り込む (低コストの activity push)
3. 取り込みの過程で **既存外国語語彙では十分 articulate しきれない部分** が認識される
4. 認識されたとき、初めて源言語の語が借入候補になる (高コストの word push)

ステップ 3 が起こらなければ word push は起こらない。逆に言えば、word push が起こったということは、受け取り側が articulate 不足の void を実際に経験したという観察可能な事実になる。

## 本 wiki 森にとっての含意

- `correspondences.yaml` で `~` (void) を記録する仕組みは、word push の **前提条件 (受け取り側 void の存在)** を first-class observable にしている。
- ただし現状 `~` で記録されている void が「実際に word push を呼び寄せた void」か「呼び寄せていない void」かは区別されていない。前者が観察できれば LT の予言の検証になる。
- 活動 push のみを記録する [[japan-reverse-import]] と本 analysis を双方向リンクし、将来 word push の事例が観察されたら本 page に追記していく。

## Open Questions

- 「納得」「空気」「いどばた (idobata)」「ブロードリスニング (broad listening)」のような日本語語彙のうち、英語コミュニティ側で借入が起こっているものはあるか? 「ブロードリスニング」は語彙自体が和製英語的に新造された語であり、活動と語が同時 push されている可能性あり ── 純粋な word push の事例とは扱いが異なるかもしれない。
- 逆方向: 英語コミュニティから日本語コミュニティへの word push は cardinal な日常で起こっているが (例: 「プルラリティ」「クアドラティック投票」)、これは多数言語 → 少数言語なので非対称が逆向き。受け取り側 (日本語) は活動なしでも word を借入しやすい構造があるか? それとも同じく活動が先か?
- 中国語 (zh) コミュニティを加えた場合、漢字共有 ([[words-as-public-goods-lt]] の論点 3) によって ja → zh の word push コストが en への push より低くなる仮説。zh column を `correspondences.yaml` に追加して観察する価値あり。
