from fastapi import Depends
from domain.user.user_repository import UserRepository
from application.exceptions import not_found, unauthorized_bearer
from domain.auth.auth_schema import LoginRequest


class LoginUseCase:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    async def excute(self, login_request: LoginRequest):
        user = await self.user_repository.get_user_by_email(email=login_request.email)

        if not user:
            raise not_found("User not found")

        is_password_valid = user.check_password(password=login_request.password)

        if not is_password_valid:
            raise unauthorized_bearer()

        return {
            "data": {"access_token": "access_token", "refresh_token": "refresh_token"}
        }
