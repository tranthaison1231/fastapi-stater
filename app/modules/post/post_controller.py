from fastapi import APIRouter
from modules.post.post_service import PostService
from db.dependency import db_dependency

router = APIRouter()


@router.get("/")
async def get_posts(db: db_dependency):
    post_service = PostService(db=db)

    posts = await post_service.get_posts()

    return posts


@router.post("/")
async def create_post(title: str, content: str, db: db_dependency):
    post_service = PostService(db=db)

    return await post_service.create_post(title=title, content=content)
