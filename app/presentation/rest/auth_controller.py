from fastapi import APIRouter, Depends, status
from typing_extensions import Annotated

from app.application.dtos.auth_schema import LoginRequest, RegisterRequest
from app.application.use_cases.auth.login import LoginUseCase
from app.application.use_cases.auth.register import RegisterUseCase
from app.domain.user.user_schema import UserResponse
from app.infrastructure.database.repositories.user_repository import UserRepository

router = APIRouter(tags=["Auth"])


@router.post("/login")
async def login(
    login_request: LoginRequest,
    user_repository: Annotated[UserRepository, Depends()],
):
    login_use_case = LoginUseCase(user_repository)
    return await login_use_case.excute(login_request)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    register_request: RegisterRequest,
    user_repository: Annotated[UserRepository, Depends()],
):
    register_use_case = RegisterUseCase(user_repository)
    return await register_use_case.excute(register_request)
