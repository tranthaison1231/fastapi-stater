from fastapi import APIRouter
from .post_controller import router as post_router
from .user_controller import router as user_router
from .auth_controller import router as auth_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(post_router, prefix="/posts")
api_router.include_router(user_router, prefix="/users")
