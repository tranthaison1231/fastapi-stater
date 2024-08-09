from fastapi import APIRouter, Depends
from domain.user.user_schema import UserRequest, UserResponse
from application.exceptions import conflict, not_found, unauthorized_bearer
from domain.user.user_service import UserService, get_user_service
from domain.auth.auth_schema import LoginRequest, RegisterRequest


router = APIRouter(tags=["Auth"])


@router.post("/login")
async def login(
    login_request: LoginRequest,
    user_service: UserService = Depends(get_user_service),
):
    user = await user_service.get_user_by_email(email=login_request.email)

    if not user:
        raise not_found("User not found")

    is_password_valid = user.check_password(password=login_request.password)

    if not is_password_valid:
        raise unauthorized_bearer()

    return {"data": {"access_token": "access_token", "refresh_token": "refresh_token"}}


@router.post("/register", response_model=UserResponse)
async def register(
    register_request: RegisterRequest,
    user_service: UserService = Depends(get_user_service),
):
    user = await user_service.get_user_by_email(email=register_request.email)

    if user:
        raise conflict("User with this email already exists")

    user_request = UserRequest(
        email=register_request.email,
        password=register_request.password,
        name=register_request.username,
    )

    user_created = await user_service.create_user(user_request)

    return user_created
