from fastapi import Depends
from app.application.dtos.auth_schema import LoginRequest
from app.domain.user.user_repository import UserRepository
from app.application.exceptions import not_found, unauthorized_bearer
from app.infrastructure.authentication.jwt_provider import JWTProvider


class LoginUseCase:
    def __init__(
        self,
        user_repository: UserRepository = Depends(),
        jwt_provider: JWTProvider = Depends(),
    ):
        self.user_repository = user_repository
        self.jwt_provider = jwt_provider

    async def excute(self, login_request: LoginRequest):
        user = await self.user_repository.get_user_by_email(email=login_request.email)

        if not user:
            raise not_found("User not found")

        is_password_valid = user.check_password(password=login_request.password)

        if not is_password_valid:
            raise unauthorized_bearer()

        access_token = self.jwt_provider.create_access_token(data={"userId": user.id})

        refresh_token = "!24"

        return {"data": {"access_token": access_token, "refresh_token": refresh_token}}
