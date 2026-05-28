---
type: analysis
summary: 唐鳳の post-book 主要展開「Civic AI / 6-Pack of Care」を 3 言語 wiki がどう carving しているかを比較。EN は source page を richen させる横展開、zh-tw は概念 hierarchy を richen させる縦展開、JA はまだ void。同じ source material からの構造的 carving 差異の事例。
sources:
  - https://github.com/nishio/plurality-llm-wiki-en/blob/main/wiki/concepts/Civic-AI.md
  - https://github.com/nishio/plurality-llm-wiki-zh-tw/blob/main/wiki/concepts/仁工智慧.md
  - https://github.com/audreyt/civic.ai
  - civic-ai-homophone-substitution.md
---

# Civic AI / 6-Pack of Care の 3 言語 carving 形状

## 観察

唐鳳の post-book 主要展開「Civic AI」(Joan Tronto の care ethics に依拠した 6-Pack of Care framework) を、3 言語 wiki がどう carving しているか:

| 言語 | 現状 | carving の形状 |
|---|---|---|
| **EN** | concept 1 (Civic-AI) + source 9 件 + 関連 entity (Joan-Tronto, Caroline-Green) 等 | **source 中心** に横展開 |
| **zh-tw** | concept 1 (仁工智慧) + 概念 hierarchy 7 件 (關懷六力 + 6 つの「力」) + source 1 件 (仁工智慧計畫) | **concept hierarchy** で縦展開 |
| **JA** | dedicated concept page なし。複数の post-book source page (デジタル民主主義の未来 等) に touching mention があるのみ | **void** (まだ carving されていない) |

## EN 側: source 中心の横展開

EN wiki の Civic-AI 関連は source page を richen させる方向:

EN source 一覧:
- `civic-ai-manifesto` (Google DeepMind, 2025-09)
- `ai-alignment-cannot-be-top-down` (AI Frontiers, 2025-11)
- `collaborative-immune-system` (LDP HQ Tokyo, 2025-12)
- `good-enough-ancestor-senate-canada` (Senate of Canada, 2026-04)
- `transparent-horse` (2040 retrospective, 2025)
- `democracy-needs-civic-ai` (Oxford Civic AI Conference, 2026-03)
- `inside-the-kami` (2026-03)
- `safer-sovereignty` (Kyndryl Institute, 2026-04)
- `civic-ai-conference-2026` (agenda + speaker roster)

これら 8+ source page が dedicated concept `Civic-AI` (本体) と entity `Caroline-Green` / `Joan-Tronto` から相互参照される。**concept は 1 つだけ、source page を多数並べる** carving 戦略。

## zh-tw 側: concept hierarchy の縦展開

zh-tw wiki は同じ Civic-AI を **9 件の互いに関連する concept page** で carving:

- **仁工智慧** (本体): Civic AI の zh-tw 訳。`人工` → `仁工` の同音異字置換 (詳細 [[civic-ai-homophone-substitution]])
- **關懷六力**: 6-Pack of Care の zh-tw 訳。Joan Tronto の枠組み総称
- **6 つの「力」を個別 concept として 6 件**:
  - 覺察力 (attentiveness)
  - 負責力 (responsibility)
  - 勝任力 (competence)
  - 回應力 (responsiveness)
  - 團結力 (solidarity)
  - 共生力 (plurality / co-existence)
- **地神** (Kami): Civic-AI が場所に紐づく境界のある AI agent を比喩する語 (詳細 [[kami-as-dishen]])

source は `仁工智慧計畫` 1 つだけだが、**概念を細かく individuated** することで knowledge を再構築。同じ civic.ai upstream 材料から「概念地図」型の carving。

## JA 側: void だが touching mentions あり

JA wiki に Civic-AI / 仁工智慧 / 公民 AI / シビック AI といった dedicated concept page は **存在しない**。ただし完全な void ではなく、複数の source page に touching mention がある:

- `デジタル民主主義の未来` (タン × 松尾豊 × 上野山勝也 対談 2025): タンの「AI の垂直な高度化ではなく水平な価値配分」発言 — これは Civic AI manifesto の中核フレーミングと一致する
- `サイボウズ式ブックス刊行記念トークイベント` (2025): タン × ワイル 対談で関連話題に触れている可能性
- `Meetup with Audrey and Glen` (2024-07): Tang の対話 source として touching

つまり JA は **Civic AI に関連する materials は持っているが、それを「Civic AI」という単一の concept として個別 carving していない**。`シビック AI` / `公民 AI` / `仁 AI` のどれを採るかの判断もまだなされていない (詳細 [[civic-ai-homophone-substitution]] の Open Question 参照)。

## 同じ source の異なる「形」

3 言語の richness はどれも実体があるが、形が違う:

| 形 | 特徴 | trade-off |
|---|---|---|
| EN (source 横展開) | 時系列・場所別の articulation を保存。Tang の発言進化が見える | 概念 hierarchy が浅い。「結局 Civic AI とは何の集合か」が概観しにくい |
| zh-tw (concept 縦展開) | 6 力の構造が clean に見える。概念地図的に navigate しやすい | source の時系列・context 情報が薄い。各力の articulation の出典が辿りにくい |
| JA (void with touching mentions) | 関連 mention が source page に散在、carving 前の素材状態 | 「Civic AI」概念を 1 つの単位として議論できない |

## なぜ形が違うか — 仮説

### 仮説 1: ingest agent の判断差

3 言語の subagent はそれぞれ独立に動き、ingest 戦略を独自に決めた:
- EN agent: civic.ai repo の各 essay を独立 source page として個別 ingest (素材の保存重視)
- zh-tw agent: civic.ai の tw-*.md (中文版 translation) を読み、原語 (中文) で書かれている概念を見つけて individuated concept page に展開 (概念構造の articulate 重視)
- JA agent: Civic AI に直接 access しなかった (a.txt や Scrapbox 経由の indirect mention のみ)

### 仮説 2: 言語 community の prior

各言語コミュニティが Plurality 全体をどう view するかで、Civic AI の取り扱いも変わる:
- EN: post-book の direction を「次の理論的展開」として注視 → essay 単位の縦長受容
- zh-tw: 唐鳳の本国言説の自然な延長として概念地図的に再構築。儒家倫理との接続が直接の affordance
- JA: post-book よりも book 本体 + 日本 community lineage (鈴木健 / 安野貴博) に focus が向いている

### 仮説 3: source material の bilingual edition 効果

civic.ai repo は en / tw-* / zh-cn 等の bilingual edition を持つが ja edition はない。これは:
- zh-tw 側が「中文版本書」として直接 ingest できた
- ja 側は「英語 → 日本語」の翻訳経路を介する必要があった
- 結果として ja での Civic AI 単独 carving が低優先になる

## 帰結

この 3 言語の形状差異は、本 wiki 森が観察するに値する事例:

- **「同じ概念が 3 言語にある」と単純化できない**。EN「source 集合」/ zh-tw「概念 hierarchy」/ JA「分散 mention」と、知識の格納形式自体が違う
- `correspondences.yaml` の 1 行 (en: Civic-AI ↔ zh-tw: 仁工智慧 ↔ ja: ~) では、この shape の違いは見えない
- 3 言語 wiki が **独立に発達する** という本 wiki 森の基本前提が、これほど exposing な形で観察された例

JA 側が将来 Civic AI を carving する際、EN の source 横展開を真似るか、zh-tw の concept 縦展開を真似るか、独自の形を採るかは、次の test case。

## Open Questions

- 「source 横展開」vs「concept 縦展開」のどちらが long-term に sustainable か? source は時間と共に追加され続けるが、concept hierarchy は構造変更が稀
- JA が将来 Civic AI を carving するとき、3 つの命名候補 (シビック AI / 公民 AI / 仁 AI) のどれを採るかで、その carving 戦略が露わになる
- zh-tw の「關懷六力」hierarchy は、原典 (civic.ai) で Joan Tronto の care ethics framework としてどこまで articulated されているか? もし zh-tw 翻訳者が独自に individuate したとすれば、これは「translation as conceptual elaboration」という新パターン
- 「concept hierarchy 型」と「source 集合型」の併用は可能か? 同一 wiki 内で両方やる場合の navigation 設計
