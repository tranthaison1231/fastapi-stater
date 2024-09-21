from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from app.application.use_cases.post.create_post import CreatePostUseCase
from app.application.use_cases.post.get_posts import GetPostsUseCase
from app.domain.post.post_schema import PostRequest, PostResponse
from app.infrastructure.database.repositories.post_repository import PostRepository

router = APIRouter(tags=["Post"])


@router.get("/", response_model=list[PostResponse])
async def get_posts(post_repository: Annotated[PostRepository, Depends()]):
    get_posts_use_case = GetPostsUseCase(post_repository)

    return await get_posts_use_case.excute()


@router.post("/", response_model=PostResponse)
async def create_post(
    post_request: PostRequest, post_repository: Annotated[PostRepository, Depends()]
):
    create_post_use_case = CreatePostUseCase(post_repository)

    return await create_post_use_case.excute(post_request=post_request)
