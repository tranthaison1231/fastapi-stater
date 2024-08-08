from db.models import Post
from db.dependency import db_dependency


class PostService:
    def __init__(self, db: db_dependency):
        self.db = db

    async def get_posts(self):
        return self.db.query(Post).all()

    async def create_post(self, title: str, content: str):
        post = Post(title=title, content=content)
        self.db.add(post)
        self.db.commit()

        return post
