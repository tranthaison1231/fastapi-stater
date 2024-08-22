from fastapi import APIRouter, Depends
from app.application.dtos.post_schema import PostRequest, PostResponse
from app.application.use_cases.post.create_post import CreatePostUseCase
from app.application.use_cases.post.get_posts import GetPostsUseCase
from typing_extensions import Annotated

router = APIRouter(tags=["Post"])


@router.get("/", response_model=list[PostResponse])
async def get_posts(
    get_posts_use_case: Annotated[GetPostsUseCase, Depends()],
):
    return await get_posts_use_case.excute()


@router.post("/", response_model=PostResponse)
async def create_post(
    post_request: PostRequest,
    create_post_use_case: Annotated[CreatePostUseCase, Depends()],
):
    return await create_post_use_case.excute(post_request=post_request)
