from typing import Annotated
import tempfile
import os
from fastapi import UploadFile,APIRouter, Depends, BackgroundTasks, Form
from ..interfaces.rag_interface import RagResponseInterface
from ..controllers.rag_controller import predict
from ..utils.response_fmt import jsonResponseFmt
router = APIRouter(prefix="/rag", tags=["Rag"])

@router.post("/upload", response_model=RagResponseInterface)
async def get_rag(doc: UploadFile, question: str= Form(...)):
    """
    Get response from RAG   
    """
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(await doc.read())
        tmp_file_path = tmp_file.name
    try:
        answer = predict(tmp_file_path, question)
        return jsonResponseFmt(answer, "RAG response generated successfully")
    finally:
        # Clean up the temporary file
        os.remove(tmp_file_path)