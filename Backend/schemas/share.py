# schemas/share.py
from pydantic import BaseModel

class ShareResponse(BaseModel):
    status: str
