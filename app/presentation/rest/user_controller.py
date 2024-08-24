from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.dtos.user_schema import UserResponse
from app.application.use_cases.user.get_me import GetMeUseCase
from app.application.use_cases.user.get_user import GetUserUseCase
from app.application.use_cases.user.get_users import GetUsersUseCase

router = APIRouter(tags=["User"])


@router.get("/", response_model=list[UserResponse])
async def get_users(get_users_use_case: Annotated[GetUsersUseCase, Depends()]):
    return await get_users_use_case.excute()


@router.get("/me")
async def get_me(get_me_use_case: Annotated[GetMeUseCase, Depends()]):
    return await get_me_use_case.excute()


@router.get("/{id}")
async def get_user(id: str, get_user_use_case: Annotated[GetUserUseCase, Depends()]):
    return await get_user_use_case.excute(id=id)
