from fastapi import APIRouter
from .v1.routes.documents import router as documents_router


api_v1_router = APIRouter(prefix="/v1")
api_v1_router.include_router(documents_router)
