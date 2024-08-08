from fastapi import APIRouter
from db.dependency import db_dependency

from modules.user.user_service import UserService

router = APIRouter()


@router.get("/")
async def get_users(db: db_dependency):
    user_service = UserService(db=db)
    return await user_service.get_users()
