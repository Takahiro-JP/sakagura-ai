import chromadb
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

chroma_client = chromadb.PersistentClient(path="data/chroma")
collection = chroma_client.get_or_create_collection(name="sakagura")

def add_document(doc_id: str, text: str, metadata: dict = {}):
    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[doc_id]
    )

def search(query: str, n_results: int = 3) -> list:
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results["documents"][0] if results["documents"] else []