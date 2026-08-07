#!/bin/bash
# 計量経済学II: 全講義ノート・課題・解答を一括render
# 使い方:  bash render_all.sh            # 全部（render済みで最新のものは自動スキップ）
#         bash render_all.sh lec3       # 特定の回だけ
#         FORCE=1 bash render_all.sh    # スキップせず全部render し直す
set -u
cd "$(dirname "$0")"

command -v quarto >/dev/null 2>&1 || { echo "quarto が見つかりません"; exit 1; }
command -v Rscript >/dev/null 2>&1 || { echo "Rscript が見つかりません"; exit 1; }

echo "== R パッケージ確認 =="
Rscript install_packages.R || exit 1

# quarto-live 拡張（ブラウザ実験室 playground{N}.qmd 用）の確認・自動インストール
# 注: `quarto add` はプロジェクト内の全qmdをスキャンする際に、まだ存在しない拡張への
#     include行で失敗する（鶏と卵）。そのためGitHubから直接ファイルを取得する。
if [ ! -f "_extensions/r-wasm/live/_knitr.qmd" ]; then
  echo "== quarto-live 拡張を取得（初回のみ、要インターネット） =="
  tmpdir="$(mktemp -d)"
  if command -v git >/dev/null 2>&1; then
    git clone --depth 1 https://github.com/r-wasm/quarto-live "${tmpdir}/quarto-live" \
      || { echo "quarto-live の取得に失敗しました（git clone）"; rm -rf "${tmpdir}"; exit 1; }
  else
    curl -fsSL https://github.com/r-wasm/quarto-live/archive/refs/heads/main.tar.gz | tar -xz -C "${tmpdir}" \
      && mv "${tmpdir}/quarto-live-main" "${tmpdir}/quarto-live" \
      || { echo "quarto-live の取得に失敗しました（curl）"; rm -rf "${tmpdir}"; exit 1; }
  fi
  mkdir -p _extensions/r-wasm
  rm -rf _extensions/r-wasm/live
  cp -R "${tmpdir}/quarto-live/_extensions/live" "_extensions/r-wasm/live"
  rm -rf "${tmpdir}"
  [ -f "_extensions/r-wasm/live/_knitr.qmd" ] && echo "  OK: _extensions/r-wasm/live" \
    || { echo "  拡張の配置に失敗しました"; exit 1; }
fi

LOG="render_log.txt"
: > "${LOG}"
fail=0
FORCE="${FORCE:-0}"

if [ $# -ge 1 ]; then
  dirs=("$@")
else
  dirs=(lec1 lec2 lec3 lec4 lec6 lec7 lec8 lec9 lec10 lec11 lec13 lec14 lec15)
fi

for d in "${dirs[@]}"; do
  [ -d "${d}" ] || continue
  for f in "${d}"/*.qmd; do
    [ -e "${f}" ] || continue
    out="${f%.qmd}.html"
    if [ "${FORCE}" != "1" ] && [ -f "${out}" ] && [ "${out}" -nt "${f}" ]; then
      echo "SKIP (render済み): ${f}"
      continue
    fi
    echo "=== RENDER: ${f} ==="
    echo "=== RENDER: ${f} ===" >> "${LOG}"
    if quarto render "${f}" >> "${LOG}" 2>&1; then
      echo "  OK"
    else
      echo "  FAIL  -> 詳細は ${LOG}"
      fail=1
    fi
  done
done

if [ -f index.qmd ] && [ $# -eq 0 ]; then
  if [ "${FORCE}" != "1" ] && [ -f index.html ] && [ index.html -nt index.qmd ]; then
    echo "SKIP (render済み): index.qmd"
  else
    echo "=== RENDER: index.qmd ==="
    echo "=== RENDER: index.qmd ===" >> "${LOG}"
    quarto render index.qmd >> "${LOG}" 2>&1 && echo "  OK" || { echo "  FAIL  -> 詳細は ${LOG}"; fail=1; }
  fi
fi

echo ""
if [ "${fail}" -eq 0 ]; then
  echo "全ファイルのrenderに成功しました。"
else
  echo "失敗があります。render_log.txt を確認してください（Claudeに読ませれば修正します）。"
fi
exit "${fail}"
