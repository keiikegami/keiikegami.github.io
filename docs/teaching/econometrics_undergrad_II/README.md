# 計量経済学II 講義教材

実証産業組織論・quantitative marketing入門の講義教材一式（Quarto）。

## フォルダ構成

```
lec{N}/                # N = 1,2,3,4,6,7,8,9,10,11,13,14,15（第5・12回はゲスト講義のため無し）
  lecture{N}.qmd       # 講義ノート
  slides{N}.qmd        # 講義スライド（reveal.js。冒頭にQuizプレースホルダ、スピーカーノート付き）
  quiz{N}.qmd          # 講義冒頭の前回復習クイズ（配布用・解答なし。N=1は無し）
  quiz{N}_solution.qmd # クイズ解答・解説（クイズ実施後に公開。N=1は無し）
  playground{N}.qmd    # ブラウザ実験室（quarto-live/webR。ブラウザ内でRが動く）
  assignment{N}.qmd    # coding課題（Part 1: シミュレーション設計 / Part 2: 推定・推論）
  solution{N}.qmd      # 課題解答（解説・配点基準付き）
index.qmd              # コーストップページ（全回へのリンクと紹介文）
_quarto.yml            # プロジェクト設定（ルートの_extensions/をlec配下から解決するため）
slides_theme.scss      # スライド共通テーマ（全回で共有）
STYLE_GUIDE.md         # 執筆仕様書（記法統一・構成テンプレ。今後の改訂用）
install_packages.R     # 必要Rパッケージの一括インストール
render_all.sh          # 一括レンダースクリプト（quarto-live拡張も初回に自動インストール）
```

## ブラウザ実験室（playground）について

- `playground{N}.qmd` は [quarto-live](https://github.com/r-wasm/quarto-live) 拡張を使い、webR（WebAssembly版R）でコードセルをブラウザ内実行します。受講者の環境構築は不要です。
- 拡張は `render_all.sh` が初回に自動でGitHubから取得し `_extensions/r-wasm/live/` に配置します（要インターネット。`quarto add` はプロジェクトスキャン時のinclude解決で失敗するため使いません）。
- 閲覧には **Webサーバー経由での配信が必要**です（`file://` で直接開くと動きません）。GitHub Pages等にそのまま置けば動きます。閲覧時もwebR本体をCDNから取得するためインターネット接続が必要です。
- 実験室内のプロットのラベルは英語です（webRの描画で日本語フォントが保証されないため）。
- 公開時の注意: `quiz{N}_solution.html` はクイズ実施前に見えないよう、公開タイミングを管理してください。

## レンダー手順

必要環境: R（4.1以上推奨）、Quarto、初回のみインターネット接続（パッケージ導入）。

```bash
cd このフォルダ
bash render_all.sh          # 全39ファイル + index をrender（初回は数十分かかります）
bash render_all.sh lec3     # 特定の回だけrender
```

- 各 `lec{N}/` に `.html` が生成されます。`index.html` から全ノートへリンクが張られています。
- 使用パッケージ: ggplot2, dplyr, tidyr, scales, patchwork, knitr, MASS, Matrix, numDeriv, fixest, mlogit, rdrobust, grf（`install_packages.R` が不足分だけ自動インストール）。
- 実行時間の目安: 第4回（ミニBLP）、第7回（モンテカルロ多め）、第13回（NFXP）がやや重め（各2〜3分程度）。

## レンダーに失敗したら

`render_log.txt` に全ログが残ります。失敗があった場合はこのファイルをClaudeに渡してください（該当箇所を特定して修正します）。
qmd内のRコードはすべて執筆時にPython/numpyでロジック検証済みですが、R環境での実行は初回renderが最初のテストになります。

## 公開時の注意

- 解答（`solution{N}.html`）を公開したくない場合は、`index.qmd` の「解答」リンクを削除して再renderしてください。
- 各HTMLは `embed-resources: true` の自己完結ファイルなので、そのままWebサイトに配置できます。

## 設計メモ

- 全データはqmd内のシミュレーションで自給（外部データファイル不要、再現性100%）。
- 記法はコース全体で統一（STYLE_GUIDE.md §7）。δ_jt・α（価格係数）は需要推定ブロック、β（割引因子）・θは動学ブロック、と定義し、衝突箇所は本文中で明示的に断っています。
- 文体・構成は計量経済学I（econometrics_undergrad）を踏襲。
