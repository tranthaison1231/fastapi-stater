from fastapi import APIRouter
from domain.user.user_schema import UserResponse
from infrastructure.database.dependencies import db_dependency

from domain.user.user_service import UserService

router = APIRouter(tags=["User"])


@router.get("/", response_model=list[UserResponse])
async def get_users(db: db_dependency):
    user_service = UserService(db=db)
    return await user_service.get_users()


@router.get("/{id}")
async def get_user_by_id(id: str, db: db_dependency):
    user_service = UserService(db=db)
    user = await user_service.get_user(id=id)
    return {"data": user}
