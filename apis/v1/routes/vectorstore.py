from ..controllers.vectorstore_controller import upload_documents, search
from ..utils.response_fmt import jsonResponseFmt
from fastapi import APIRouter, File, UploadFile

router = APIRouter(prefix="/vectorstore", tags=["VectorStore"])

@router.post("/ingest")
async def ingest_doc(doc: UploadFile = File(...)):
    """
    Ingest a document into the vector store
    """
    data = await upload_documents(doc)
    return jsonResponseFmt(data, "Document ingested successfully")

@router.get("/retrive")
async def retrive(query: str):
    """
    Search for the relevant snippets in the vector store
    """
    retriver = search(query)
    return jsonResponseFmt(retriver, "Search results generated successfully")