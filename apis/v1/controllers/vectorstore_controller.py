from langchain_chroma import Chroma
from ..configs.word_embedding_config import mxbai_embedder

def create_vector_store(split_docs):
    # Create a vector store from the document splits
    vectorstore = Chroma.from_documents(documents=split_docs, embedding=mxbai_embedder)

    # Retrieve and generate using the relevant snippets of the blog
    retriever = vectorstore.as_retriever()
    return retriever