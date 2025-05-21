from pydantic import BaseModel

class AcceptResponse(BaseModel):
    status: str
