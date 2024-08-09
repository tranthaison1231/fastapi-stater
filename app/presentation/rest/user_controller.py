from fastapi import APIRouter, Depends
from domain.user.user_schema import UserResponse

from domain.user.user_service import UserService, get_user_service

router = APIRouter(tags=["User"])


@router.get("/", response_model=list[UserResponse])
async def get_users(user_service: UserService = Depends(get_user_service)):
    return await user_service.get_users()


@router.get("/{id}")
async def get_user(id: str, user_service: UserService = Depends(get_user_service)):
    user = await user_service.get_user(id=id)
    return {"data": user}
