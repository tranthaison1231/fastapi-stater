from fastapi import Depends

from app.application.constants import ErrorMessages
from app.application.dtos.auth_schema import RegisterRequest
from app.application.exceptions import conflict
from app.domain.user.user_schema import UserRequest
from app.infrastructure.database.repositories.user_repository import UserRepository


class RegisterUseCase:
    def __init__(self, user_repository: UserRepository = Depends()) -> None:
        self.user_repository = user_repository

    async def excute(self, register_request: RegisterRequest):
        user = await self.user_repository.get_user_by_email(
            email=register_request.email,
        )

        if user:
            raise conflict(ErrorMessages.USER_ALREADY_EXISTS)

        user_request = UserRequest(
            email=register_request.email,
            password=register_request.password,
            name=register_request.username,
        )

        return await self.user_repository.create_user(user_request)
