from typing import Annotated
from io import BytesIO
from fastapi import APIRouter, Depends, BackgroundTasks
from ..interfaces.rag_interface import RagResponseInterface
from ..controllers.rag_controller import invoke

router = APIRouter(prefix="/rag", tags=["Rag"])

@router.post("/", response_model=RagResponseInterface)
async def get_rag(doc_id: str, question: str):
    """
    Get response from RAG   
    """
    answer = invoke(doc_id, question)
    return answer