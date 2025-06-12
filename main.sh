#!/bin/env bash
set -euo pipefail

# 必要なコマンドのパスを通す (前回追加した部分)
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/sbin:/sbin:$PATH"

# ★ここを修正/追加★
# スクリプトの実行ディレクトリに移動
cd /mnt/c/Users/yukim/akishima2025/

# Python仮想環境をアクティベートする (前回追加した部分)
source venv/bin/activate


#cd ~/github/poster-map/ #Path to the folder
git pull

# Download latest CSV from spreadsheet database
curl -sL "https://docs.google.com/spreadsheets/d/1jX6HPImNFtsjj9nmQq95GqqY3ZGLL5URT7Nla-YyZRY/export?format=csv" > public/data/all.csv

# all.json
python3 csv2json_small.py public/data/all.csv public/data/

# summary.json
python3 summarize_progress.py ./public/data/summary.json

# summary_absolute.json
python3 summarize_progress_absolute.py ./public/data/summary_absolute.json

git add -N .

if ! git diff --exit-code --quiet
then
    git add .
    git commit -m "Update"
    git push
    source .env
    npx netlify-cli deploy --prod --message "Deploy" --dir=./public --auth $NETLIFY_AUTH_TOKEN
fi
