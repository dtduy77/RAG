from fastapi import APIRouter
from .v1.routes.documents import router as documents_router
from .v1.routes.rag import router as rag_router
from .v1.routes.vectorstore import router as vectorstore_router
api_v1_router = APIRouter(prefix="/v1")

# Register routes for the API
api_v1_router.include_router(documents_router)
api_v1_router.include_router(rag_router)
api_v1_router.include_router(vectorstore_router)