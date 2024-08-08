from fastapi import APIRouter
from modules.post.post_controller import router as post_router
from modules.user.user_controller import router as user_router

api_router = APIRouter()

api_router.include_router(post_router, prefix="/posts")
api_router.include_router(user_router, prefix="/users")
