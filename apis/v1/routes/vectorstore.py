from ..controllers.vectorstore_controller import upload_documents, search
from ..utils.response_fmt import jsonResponseFmt
from fastapi import APIRouter, File, UploadFile
import os
import tempfile

router = APIRouter(prefix="/vectorstore", tags=["VectorStore"])

@router.post("/ingest")
async def ingest_doc(doc: UploadFile = File(...)):
    """
    Ingest a document into the vector store
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(await doc.read())
        tmp_file_path = tmp_file.name
    try:
        data = upload_documents(tmp_file_path)
        return jsonResponseFmt(data, "Document ingested successfully")
    finally:
        # Clean up the temporary file
        os.remove(tmp_file_path)

@router.get("/retrieve")
async def retrieve(query: str):
    """
    Search for the relevant snippets in the vector store
    """
    retriver = search(query)
    return jsonResponseFmt(retriver, "Search results generated successfully")