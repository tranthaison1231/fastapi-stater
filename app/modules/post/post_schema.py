from pydantic import BaseModel

from db.models.post import Post


class GetPostsResponse(BaseModel):
    posts: list[Post]


class CreatePostResponse(BaseModel):
    post: Post
