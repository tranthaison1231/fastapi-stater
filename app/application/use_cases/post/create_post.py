from fastapi import Depends

from app.application.dtos.post_schema import PostRequest
from app.infrastructure.database.repositories.post_repository import PostRepository


class CreatePostUseCase:
    def __init__(self, post_repository: PostRepository = Depends()) -> None:
        self.post_repository = post_repository

    async def excute(self, post_request: PostRequest):
        return await self.post_repository.create_post(post_request=post_request)
