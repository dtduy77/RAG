from typing import AnyStr, Dict
from fastapi import UploadFile
from pydantic import BaseModel, Field
from ..providers import firebase_db
from ..utils.utils import get_current_time

class DocModel(BaseModel):
    id: str = Field(..., description="Document ID")
    name: str = Field(..., description="Document Name")
    content: str = Field(..., description="Document Content")
    upload_at: str = Field(..., description="Document Uploaded At")

class DocSchema:
    '''
    Schema and Validation for Document
    '''
    def __init__(
        self,
        doc_id: AnyStr = None,
        name: AnyStr = "",
        content: AnyStr = "",
        upload_at: AnyStr = get_current_time()
    ):
        self.id = doc_id
        self.name = name
        self.content = content
        self.upload_at = upload_at

    def to_dict(self, include_id = True):
        data_dict = {
            "name": self.name,
            "content": self.content,
            "upload_at": self.upload_at
        }
        if include_id:
            data_dict["id"] = self.id
        return data_dict

    @staticmethod
    def from_dict(data: Dict):
        return DocSchema(
            doc_id=data.get("id"),
            name=data.get("name"),
            content=data.get("content"),
            upload_at=data.get("upload_at")
        )

    def create_doc(self):
        doc_id = firebase_db.upload_doc(self.to_dict(include_id=False))
        self.id = doc_id
        return self

    def update_data(self, name: str, content: str):
        self.name = name
        self.content = content
        firebase_db.update_doc(self.id, {
            "name": self.name,
            "content": self.content,
        })

    

    