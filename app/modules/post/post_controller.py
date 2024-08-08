from fastapi import APIRouter
from modules.post.post_schema import GetPostsResponse, PostSchema
from modules.post.post_service import PostService
from db.dependency import db_dependency

router = APIRouter()


@router.get("/", response_model=GetPostsResponse)
async def get_posts(db: db_dependency):
    post_service = PostService(db=db)

    posts = await post_service.get_posts()

    posts_data: list[PostSchema] = []

    for post in posts:
        posts_data.append(PostSchema(title=post.title, content=post.content))

    return GetPostsResponse(data=posts_data)


@router.post("/")
async def create_post(title: str, content: str, db: db_dependency):
    post_service = PostService(db=db)

    return await post_service.create_post(title=title, content=content)
