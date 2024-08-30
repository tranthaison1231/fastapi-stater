from fastapi import Depends

from app.infrastructure.database.repositories.post_repository import PostRepository


class GetPostsUseCase:
    def __init__(self, post_repository: PostRepository = Depends()) -> None:
        self.post_repository = post_repository

    async def excute(self):
        return await self.post_repository.get_posts()
