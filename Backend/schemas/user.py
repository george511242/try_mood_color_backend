from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str

class UserResponse(BaseModel):
    username: str
    email: str
    password_hash: str
    created_at: datetime