from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


mxbai_embedder = HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")

load_dotenv()

llm = ChatGoogleGenerativeAI(google_api_key=os.environ.get("GOOGLE_API_KEY"), 
                                   model="gemini-1.5-pro-latest")

# Load and split the PDF document into pages
pdf_loader = PyPDFLoader("LeaveNoContextBehind.pdf")
pages = pdf_loader.load_and_split()

# Split the pages into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(pages)

# Create a vector store from the document splits
vectorstore = Chroma.from_documents(documents=splits, embedding=mxbai_embedder)

# Retrieve and generate using the relevant snippets of the blog
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Define the RAG chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Invoke the RAG chain with a question
response = rag_chain.invoke("Can you summarize the document?")
print(response)
