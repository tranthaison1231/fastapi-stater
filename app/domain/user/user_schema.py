from datetime import datetime
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    name: str
    email: str


class UserRequest(BaseModel):
    name: str
    email: str
    password: str
