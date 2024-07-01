from ..utils.constants import INDEX_NAME
from ..configs.vectorstore_config import pc
from langchain_pinecone import PineconeVectorStore

class VectorStoreProvider:
    def __init__(self) :
        self.index_name = INDEX_NAME
        self.pc = pc

    def upload_documents(self, documents, embeddings):
        # for doc in documents:
        #     new_url = doc.metadata["source"]
        #     # new_url = new_url.replace("langchain-docs", "https:/")
        #     doc.metadata.update({"source": new_url})
        print(f"Going to add {len(documents)} to Pinecone")
        PineconeVectorStore.from_documents(documents, embeddings, index_name=self.index_name)
        print("****Loading to vectorstore done ***")
       