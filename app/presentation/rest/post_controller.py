from fastapi import APIRouter, Depends
from domain.post.post_schema import PostRequest, PostResponse
from domain.post.post_service import PostService, get_post_service

router = APIRouter(tags=["Post"])


@router.get("/", response_model=list[PostResponse])
async def get_posts(
    post_service: PostService = Depends(get_post_service),
):
    return await post_service.get_posts()


@router.post("/", response_model=PostResponse)
async def create_post(
    post_request: PostRequest,
    post_service: PostService = Depends(get_post_service),
):
    return await post_service.create_post(post_request=post_request)
