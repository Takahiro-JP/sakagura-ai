import anthropic
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_post(product: dict, target: str) -> dict:
    prompt = f"""あなたは日本酒蔵「楯野川」の広報担当AIです。
以下の商品情報とターゲットに合わせたSNS投稿文を生成してください。

商品名: {product['name']}
シリーズ: {product['series']}
精米歩合: {product['seimaibuai']}%
価格: {product['price']}円
味わい: {product['flavor_notes']}
ターゲット層: {target}

以下のJSON形式のみで出力してください。余分なテキストは不要です。

{{
  "instagram": "絵文字・ハッシュタグ付き200文字程度の投稿文",
  "x": "140文字以内の投稿文",
  "facebook": "丁寧な文体300文字程度の投稿文"
}}
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        text = message.content[0].text
        # コードブロックを除去
        text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except json.JSONDecodeError:
        print("Claude出力:", message.content[0].text)
        return {"error": "生成に失敗しました。もう一度試してください。"}