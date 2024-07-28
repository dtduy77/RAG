from ..utils.constants import INDEX_NAME
from ..configs.vectorstore_config import pc
from ..configs.llm_config import gemini_model
from ..configs.word_embedding_config import google_embedder
from ..utils.constants import INDEX_NAME   
from ..utils.prompts import retrival_qa_chat 
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub


class VectorStoreProvider:
    def __init__(self, index_name=INDEX_NAME, pc=pc, embeddings=google_embedder, llm=gemini_model): 
        self.index_name = index_name
        self.pc = pc
        self.embeddings = embeddings
        self.llm = llm

    def ingest_doc(self, file_path: str):
        print("Ingesting...")
        loader = PyPDFLoader(file_path)
        document = loader.load()

        print("splitting...")
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(document)
        print(f"created {len(texts)} chunks")
        embeddings = self.embeddings

        print("ingesting...")
        PineconeVectorStore.from_documents(
            texts, embeddings, index_name=self.index_name
        )
        print("finish")

    def search(self, query: str):
        print(" Retrieving...")

        embeddings = self.embeddings
        model = self.llm
        chain = PromptTemplate.from_template(template=query) | model

        vectorstore = PineconeVectorStore(
            index_name=self.index_name, embedding=embeddings
        )

        retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
        combine_docs_chain = create_stuff_documents_chain(model, retrieval_qa_chat_prompt)
        retrival_chain = create_retrieval_chain(
            retriever=vectorstore.as_retriever(), combine_docs_chain=combine_docs_chain
        )

        result = retrival_chain.invoke(input={"input": query})
        return result['answer']
