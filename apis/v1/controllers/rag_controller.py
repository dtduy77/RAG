from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from ..utils.prompts import rag_prompt
from ..configs.llm_configs import gemini_model as llm



def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def invoke(retriever, question:str) -> str:
    
    prompt = PromptTemplate.from_template(rag_prompt)
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    response = rag_chain.invoke(question)
    return response