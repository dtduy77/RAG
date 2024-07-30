from sentence_transformers import SentenceTransformer, util
embedding_model = SentenceTransformer("hiieu/halong_embedding")
def get_embedding(text: str) -> list[float]:
    if not text.strip():
        print("Attempted to get embedding for empty text.")
        return []
    embedding = embedding_model.encode(text)
    return embedding.tolist()