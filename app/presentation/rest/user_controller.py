from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.dependencies.current_user import current_user_dependency
from app.application.use_cases.user.get_user import GetUserUseCase
from app.application.use_cases.user.get_users import GetUsersUseCase
from app.domain.user.user_schema import UserResponse
from app.infrastructure.database.repositories.user_repository import UserRepository

router = APIRouter(tags=["User"])


@router.get("/", response_model=list[UserResponse])
async def get_users(user_repository: Annotated[UserRepository, Depends()]):
    get_users_use_case = GetUsersUseCase(user_repository)
    return await get_users_use_case.excute()


@router.get("/me")
async def get_me(current_user: current_user_dependency):
    return current_user


@router.get("/{id}")
async def get_user(id: str, user_repository: Annotated[UserRepository, Depends()]):
    get_user_use_case = GetUserUseCase(user_repository)

    return await get_user_use_case.excute(id=id)
