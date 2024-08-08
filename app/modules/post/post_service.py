from db.dependency import db_dependency
from db.models import Post


class PostService:
    def __init__(self, db: db_dependency):
        self.db = db

    async def get_posts(self):
        posts = self.db.query(Post).all()

        return posts

    async def create_post(self, title: str, content: str):
        post = Post(title=title, content=content)
        self.db.add(post)
        self.db.commit()

        return post
