from fastapi import APIRouter, Depends
from domain.user.user_schema import UserResponse

from application.use_cases.user.get_user import GetUserUseCase
from application.use_cases.user.get_users import GetUsersUseCase

router = APIRouter(tags=["User"])


@router.get("/", response_model=list[UserResponse])
async def get_users(get_users_use_case: GetUsersUseCase = Depends()):
    return await get_users_use_case.excute()


@router.get("/{id}")
async def get_user(id: str, get_user_use_case: GetUserUseCase = Depends()):
    return await get_user_use_case.excute(id=id)
