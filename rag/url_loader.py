import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from bs4 import BeautifulSoup
from rag.retriever import add_document
import hashlib

def load_url(url: str, doc_type: str = "web"):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")

    # 不要なタグを除去
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    # 空行を整理
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    text = "\n".join(lines)

    # URLからdoc_idを生成
    doc_id = hashlib.md5(url.encode()).hexdigest()[:12]

    add_document(
        doc_id=doc_id,
        text=text[:3000],  # 長すぎる場合は先頭3000文字
        metadata={"type": doc_type, "source": url}
    )
    print(f"登録完了: {url}")
    return text[:200]  # 確認用に先頭200文字を返す

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python3 rag/url_loader.py https://...")
        sys.exit(1)
    url = sys.argv[1]
    preview = load_url(url)
    print("プレビュー:")
    print(preview)
