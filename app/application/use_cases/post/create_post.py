from app.domain.post.post_abstract import PostRepositoryInterface
from app.domain.post.post_schema import PostRequest


class CreatePostUseCase:
    def __init__(self, post_repository: PostRepositoryInterface) -> None:
        self.post_repository = post_repository

    async def excute(self, post_request: PostRequest):
        return await self.post_repository.create_post(post_request=post_request)
