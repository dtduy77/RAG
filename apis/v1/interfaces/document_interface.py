from typing import List, Dict
from fastapi import UploadFile, File
from pydantic import BaseModel, Field
from ..schemas.document_schema import DocModel

class DocumentUploadResponseInterface(BaseModel):
    msg: str = Field(..., description="Message response")
    data: DocModel = Field(..., description="Document Data")
