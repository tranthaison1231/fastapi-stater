from pydantic import BaseModel


class PostResponse(BaseModel):
    title: str
    content: str


class PostRequest(BaseModel):
    title: str
    content: str
