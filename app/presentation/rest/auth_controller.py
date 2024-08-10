from fastapi import APIRouter, Depends
from domain.user.user_schema import UserResponse
from domain.auth.auth_schema import LoginRequest, RegisterRequest
from application.use_cases.auth.login import LoginUseCase
from application.use_cases.auth.register import RegisterUseCase

router = APIRouter(tags=["Auth"])


@router.post("/login")
async def login(login_request: LoginRequest, login_use_case: LoginUseCase = Depends()):
    return await login_use_case.excute(login_request)


@router.post("/register", response_model=UserResponse)
async def register(
    register_request: RegisterRequest, register_use_case: RegisterUseCase = Depends()
):
    return await register_use_case.excute(register_request)
