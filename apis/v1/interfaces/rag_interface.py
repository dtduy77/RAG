from typing import List, Dict
from fastapi import UploadFile, File
from pydantic import BaseModel, Field
from ..schemas.rag_schema import RAGModel

class RagResponseInterface(BaseModel):
    msg: str = Field(..., description="Message response")
    data: list[RAGModel] = Field(..., description="")