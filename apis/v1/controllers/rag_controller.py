from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from ..utils.prompts import rag_prompt
from ..configs.llm_configs import gemini_model as llm
from ..controllers.vectorstore_controller import create_vector_store

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def predict(file_path: str, question: str) -> str:
    # Load and split the PDF document into pages
    pdf_loader = PyPDFLoader(file_path)
    pages = pdf_loader.load_and_split()

    # Split the pages into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(pages)

    # Retrieve and generate using the relevant snippets of the document
    retriever = create_vector_store(splits)

    custom_rag_prompt = PromptTemplate.from_template(rag_prompt)

    # Define the RAG chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | custom_rag_prompt
        | llm
        | StrOutputParser()
    )

    # Invoke the RAG chain with a question
    response = rag_chain.invoke(question)
    return response
