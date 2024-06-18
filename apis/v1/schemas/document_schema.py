from typing import AnyStr, Dict
from pydantic import BaseModel, Field
from ..providers import jd_db


class DocumentResponse(BaseModel):
    