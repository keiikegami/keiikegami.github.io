# 計量経済学II: 必要パッケージの一括インストール（不足分のみ）
pkgs <- c(
  "ggplot2", "dplyr", "tidyr", "scales", "patchwork", "knitr",
  "MASS", "Matrix", "numDeriv",
  "fixest", "mlogit", "rdrobust", "grf"
)
installed <- rownames(installed.packages())
todo <- setdiff(pkgs, installed)
if (length(todo) > 0) {
  message("Installing: ", paste(todo, collapse = ", "))
  install.packages(todo, repos = "https://cloud.r-project.org")
} else {
  message("All packages already installed.")
}
