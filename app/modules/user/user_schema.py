from datetime import datetime
from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    created_at: datetime
    updated_at: datetime
    name: str
    email: str


class UserRequest(BaseModel):
    name: str
    email: str
    password: str
