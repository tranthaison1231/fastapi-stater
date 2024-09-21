from app.application.constants import ErrorMessages
from app.application.dtos.auth_schema import LoginRequest
from app.application.exceptions import not_found, unauthorized_bearer
from app.application.services.jwt_provider import JWTProvider
from app.domain.user.user_abstract import UserRepositoryInterface


class LoginUseCase:
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
    ) -> None:
        self.user_repository = user_repository

    async def excute(self, login_request: LoginRequest):
        user = await self.user_repository.get_user_by_email(email=login_request.email)

        if not user:
            raise not_found(ErrorMessages.USER_NOT_FOUND)

        is_password_valid = user.check_password(password=login_request.password)

        if not is_password_valid:
            raise unauthorized_bearer()

        access_token = JWTProvider.create_access_token(data={"userId": user.id})

        refresh_token = "!24"  # noqa: S105

        return {"access_token": access_token, "refresh_token": refresh_token}
