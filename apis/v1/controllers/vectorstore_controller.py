from langchain_chroma import Chroma
from ..configs.word_embedding_config import mxbai_embedder
from ..providers import vectorstore_db

def create_vector_store(split_docs):
    # Create a vector store from the document splits
    vectorstore = Chroma.from_documents(documents=split_docs, embedding=mxbai_embedder)
    # Upload the documents to the vector store
    # vectorstore_db.upload_documents(split_docs, mxbai_embedder)
    # Retrieve and generate using the relevant snippets of the blog
    retriever = vectorstore.as_retriever()
    # retriever = docsearch.as_retriever()
    return retriever

def upload_documents(file_path: str):
    # Ingest the document into the vector store
    vectorstore_db.ingest_doc(file_path)

def search(query: str):
    # Search for the relevant snippets in the vector store
    return vectorstore_db.search(query)
