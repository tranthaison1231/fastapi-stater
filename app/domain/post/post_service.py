from domain.post.post_repository import PostRepository
from domain.post.post_schema import PostRequest
from infrastructure.database.dependencies import db_dependency


class PostService:
    def __init__(self, db: db_dependency):
        self.post_repository = PostRepository(db=db)

    async def get_posts(self):
        return self.post_repository.get_posts()

    async def create_post(self, post_request: PostRequest):
        return self.post_repository.create_post(post_request=post_request)
