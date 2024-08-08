from pydantic import BaseModel


class PostSchema(BaseModel):
    title: str
    content: str


class GetPostsResponse(BaseModel):
    data: list[PostSchema]


class CreatePostResponse(BaseModel):
    data: PostSchema
