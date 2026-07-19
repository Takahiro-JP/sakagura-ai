import csv
import io
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def analyze_sns(csv_text: str) -> str:
    prompt = f"""あなたは日本酒蔵「楯野川」の広報担当AIです。
以下のSNS投稿データを分析してください。

{csv_text}

以下の観点で分析してレポートを作成してください：

1. 保存率が高い投稿の特徴（saves / impressions）
2. エンゲージメントが高い投稿の特徴（likes + comments / impressions）
3. プラットフォーム別のパフォーマンス比較
4. 改善提案（具体的に）
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,  # 1000 → 4096に変更
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text