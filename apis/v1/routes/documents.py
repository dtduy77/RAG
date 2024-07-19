from typing import Annotated
from io import BytesIO
from pydantic import BaseModel, Field
from fastapi import APIRouter, UploadFile, Depends, BackgroundTasks
from ..controllers.document_controller import upload_document, get_document, update_document, delete_document
from ..interfaces.document_interface import DocumentUploadResponseInterface
from ..utils.response_fmt import jsonResponseFmt

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/{document_id}", response_model=DocumentUploadResponseInterface)
async def get_doc(document_id: str):
    """
    Get a document
    """
    document = get_document(document_id)
    return jsonResponseFmt(document,"Document retrieved successfully")

@router.post("/upload", response_model=DocumentUploadResponseInterface)
async def upload_doc(data: UploadFile, bg_tasks: BackgroundTasks):
    """
    Upload a document
    """
    await upload_document(data, bg_tasks)
    return jsonResponseFmt(None,"Document uploaded successfully")

@router.put("/{document_id}", response_model=DocumentUploadResponseInterface)
async def update_doc(document_id: str, data: dict):
    """
    Update a document
    """
    document = update_document(document_id, data)
    return jsonResponseFmt(document,"Document updated successfully")

@router.delete("/{document_id}", response_model=DocumentUploadResponseInterface)
async def delete_doc(document_id: str):
    """
    Delete a document
    """
    document = delete_document(document_id)
    return jsonResponseFmt(document,"Document deleted successfully")