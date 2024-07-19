from typing import AnyStr, Dict
from fastapi import UploadFile, HTTPException, status, BackgroundTasks
import os
from ..schemas.document_schema import DocSchema
from ..utils.utils import  validate_file_extension
from ..utils.extractor import get_content
from ..utils.constants import CACHE_DIR
from ..providers import firebase_db

def _upload_document(content: str, file_name: str, doc: DocSchema):
    """
    Upload a document
    """
    try:
        # Upload the document to Firebase
        doc.create_doc()
        doc.update_data(file_name, content)
        return None
    except Exception as e:
        print("Error in function _upload_document in document_controller")      
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
async def upload_document(doc: UploadFile, bg_tasks: BackgroundTasks):
    """
    Upload a document
    """ 
    try:
        # Validate the file extension
        validate_file_extension(doc.filename)

         # Ensure the cache directory exists
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)

        # Save the uploaded file to the cache directory
        file_path = os.path.join(CACHE_DIR, doc.filename)
        with open(file_path, 'wb') as cache_file:
            cache_file.write(await doc.read())
        # Read the file content
        file_content = get_content(file_path)
        # print('\n\n',file_content,'\n\n')

        doc_init = DocSchema()
        # doc_init.create_doc()
        # doc_init.update_data(doc.filename, file_content)

        # Add the task to the background task
        bg_tasks.add_task(_upload_document, file_content, doc.filename, doc_init)
        return None
        # return file_content
    except Exception as e:
        print("Error in function upload_document in document_controller")
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