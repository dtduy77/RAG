from typing import Annotated
from io import BytesIO
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, BackgroundTasks
from ..interfaces.document_interface import DocumentUploadResponseInterface
from ..utils.response_fmt import jsonResponseFmt

router = APIRouter(prefix="/documents", tags=["Documents"])


# @router.get("/{document_id}", response_model=DocumentResponse)
# async def get_document(document_id: str):
#     """
#     Get a document
#     """
    
#     return {"document_id": document_id}

@router.post("/upload", response_model=DocumentUploadResponseInterface)
async def upload_document():
    """
    Upload a document
    """
    
    return jsonResponseFmt(None,"Document uploaded successfully")

# @router.update("/{document_id}", response_model=DocumentResponse)
# async def update_document(document_id: str):
#     """
#     Update a document
#     """

#     return {"document_id": document_id}

# @router.delete("/{document_id}")
# async def delete_document(document_id: str):
#     """
#     Delete a document
#     """
    
#     return {"document_id": document_id}