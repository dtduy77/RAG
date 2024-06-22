from typing import AnyStr
from fastapi import UploadFile, HTTPException, status, BackgroundTasks
import uuid
import time
from ..schemas.document_schema import DocSchema

# def get_all_docs():
#     '''
#     Get all the documents from the database.
#     '''
#     return Document.objects.all()


def _upload_docs(filename: AnyStr, doc: DocSchema):
    '''
    Get content type of file.
    '''
    # Get content type of file
    content_type = get_content_type(filename)
    path, url = storage_db.upload(data, filename, content_type)
    cv.update_path_url(path, url)

    return 

# def update_docs():
#     '''
#     Update a document in the database.
#     '''
#     return Document.objects.update()

# def delete_docs():
#     '''
#     Delete a document from the database.
#     '''
#     return Document.objects.delete()


async def upload_doc()
