from typing import AnyStr
from fastapi import UploadFile, HTTPException, status, BackgroundTasks
import uuid
import time
from ..providers import firebase_db
from ..schemas.document_schema import DocSchema

def upload_document(data):
    """
    Upload a document
    """
    try:
        upload_document = firebase_db.upload_doc(data)
        return upload_document
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

def get_document(document_id: AnyStr):
    """
    Get a document
    """
    try:
        document = firebase_db.get_doc(document_id)
        return document
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def update_document(document_id: AnyStr, data):
    """
    Update a document
    """
    try:
        update_document = firebase_db.update_doc(document_id, data)
        return update_document
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
def delete_document(document_id: AnyStr):
    """
    Delete a document
    """
    try:
        delete_document = firebase_db.delete_doc(document_id)
        return delete_document
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))