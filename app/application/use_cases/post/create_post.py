from fastapi import Depends
from domain.post.post_repository import PostRepository
from domain.post.post_schema import PostRequest


class CreatePostUseCase:
    def __init__(self, post_repository: PostRepository = Depends()):
        self.post_repository = post_repository

    async def excute(self, post_request: PostRequest):
        return await self.post_repository.create_post(post_request=post_request)
