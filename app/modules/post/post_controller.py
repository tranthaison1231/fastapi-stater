from fastapi import APIRouter
from modules.post.post_schema import PostRequest, PostResponse
from modules.post.post_service import PostService
from db.dependencies import db_dependency

router = APIRouter(tags=["Post"])


@router.get("/", response_model=list[PostResponse])
async def get_posts(db: db_dependency):
    post_service = PostService(db=db)

    return await post_service.get_posts()


@router.post("/", response_model=PostResponse)
async def create_post(post_request: PostRequest, db: db_dependency):
    post_service = PostService(db=db)

    return await post_service.create_post(post_request=post_request)
