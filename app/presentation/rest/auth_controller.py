from fastapi import APIRouter, Depends, status
from app.application.dtos.auth_schema import LoginRequest, RegisterRequest
from app.application.dtos.user_schema import UserResponse
from app.application.use_cases.auth.login import LoginUseCase
from app.application.use_cases.auth.register import RegisterUseCase

router = APIRouter(tags=["Auth"])


@router.post("/login")
async def login(login_request: LoginRequest, login_use_case: LoginUseCase = Depends()):
    return await login_use_case.excute(login_request)


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
async def register(
    register_request: RegisterRequest, register_use_case: RegisterUseCase = Depends()
):
    return await register_use_case.excute(register_request)
