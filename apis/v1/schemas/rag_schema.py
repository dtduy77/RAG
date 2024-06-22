from typing import AnyStr, Dict
import enum
from pydantic import BaseModel, Field
# from ..providers import rag_db
# from ..providers import storage_db



class RAGModel(BaseModel):
    doc_id: str = Field(None, title="Doc ID")
    path: str = Field("", title="Doc Path")
    content: str = Field("", title="Doc Content")
    question: list = Field("",title="List of questions about that document")

