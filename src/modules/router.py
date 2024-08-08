from fastapi import APIRouter
from modules.post.router import router as post_router
from modules.user.router import router as user_router

all_router = APIRouter()

all_router.include_router(post_router, prefix="/posts")
all_router.include_router(user_router, prefix="/users")
