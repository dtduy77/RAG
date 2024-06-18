from typing import Annotated
from io import BytesIO
from fastapi import APIRouter, Depends, BackgroundTasks
from ..interfaces.document_interface import DocumentUploadResponseInterface
router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/upload", response_model=DocumentResponse)
async def upload_document(file: Annotated[BytesIO, Field(..., description="File to upload")], background_tasks: BackgroundTasks):
    """
    Upload a document
    """
    
    return DocumentUploadResponseInterface(file=file)