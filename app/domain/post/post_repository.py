from domain.post.post_schema import PostRequest
from domain.post.post_model import Post
from infrastructure.database.dependencies import db_dependency


class PostRepository:
    def __init__(self, db: db_dependency):
        self.db = db

    async def get_posts(self):
        return self.db.query(Post).all()

    async def create_post(self, post_request: PostRequest):
        post = Post(title=post_request.title, content=post_request.content)
        self.db.add(post)
        self.db.commit()

        return post
