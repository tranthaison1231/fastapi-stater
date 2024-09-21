from app.domain.post.post_abstract import PostRepositoryInterface


class GetPostsUseCase:
    def __init__(self, post_repository: PostRepositoryInterface) -> None:
        self.post_repository = post_repository

    async def excute(self):
        return await self.post_repository.get_posts()
