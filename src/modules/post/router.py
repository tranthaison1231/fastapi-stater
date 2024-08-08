from fastapi import APIRouter
from db.dependency import db_dependency
from modules.post.schema import Post

router = APIRouter()


@router.get("/")
def get_posts(db: db_dependency):
    posts = db.query(Post).all()

    return posts
