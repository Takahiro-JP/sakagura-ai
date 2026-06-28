import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyPDF2 import PdfReader
from rag.retriever import add_document

def load_pdf(filepath: str, doc_type: str = "pdf"):
    reader = PdfReader(filepath)
    filename = os.path.basename(filepath)

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text.strip():
            continue

        doc_id = f"{filename}_page{i+1}"
        add_document(
            doc_id=doc_id,
            text=text,
            metadata={"type": doc_type, "source": filename, "page": i+1}
        )
        print(f"登録: {doc_id}")

    print(f"{filename} の登録完了（{len(reader.pages)}ページ）")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python3 rag/pdf_loader.py ファイル名.pdf")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"ファイルが見つかりません: {filepath}")
        sys.exit(1)

    load_pdf(filepath)