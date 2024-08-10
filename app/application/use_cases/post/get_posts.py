from fastapi import Depends
from domain.post.post_repository import PostRepository


class GetPostsUseCase:
    def __init__(self, post_repository: PostRepository = Depends()):
        self.post_repository = post_repository

    async def excute(self):
        return await self.post_repository.get_posts()
