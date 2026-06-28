# 酒蔵AIアシスタント

楯野川酒造の広報業務をAIで効率化するDiscord Botです。

## 機能

- `/post [商品名] [ターゲット]` : Instagram・X・Facebook向け投稿文を一括生成
- 生成した投稿文をSQLiteに自動保存

## 技術スタック

- Python / discord.py
- Claude API (claude-sonnet-4-6)
- SQLite

## セットアップ

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install anthropic discord.py python-dotenv
cp .env.example .env  # APIキーを設定
python3 seed.py       # 初期データ投入
python3 bot/main.py   # Bot起動
```

## 使用例
/post 楯野川純米大吟醸清流 50代
![screenshot](screenshot.png)