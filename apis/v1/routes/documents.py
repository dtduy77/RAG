from typing import Annotated
from io import BytesIO
from fastapi import APIRouter, Depends, BackgroundTasks
from ..interfaces.document_interface import DocumentUploadResponseInterface
router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/{document_id}", response_model=DocumentResponse)
async def get_document(document_id: str):
    """
    Get a document
    """
    
    return {"document_id": document_id}

@router.post("/upload", response_model=DocumentResponse)
async def upload_document(file: Annotated[BytesIO, Field(..., description="File to upload")], background_tasks: BackgroundTasks):
    """
    Upload a document
    """
    
    return DocumentUploadResponseInterface(file=file)

@router.update("/{document_id}", response_model=DocumentResponse)
async def update_document(document_id: str):
    """
    Update a document
    """

    return {"document_id": document_id}

@router.delete("/{document_id}")
async def delete_document(document_id: str):
    """
    Delete a document
    """
    
    return {"document_id": document_id}