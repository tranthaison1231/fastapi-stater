from fastapi import Depends
from app.domain.user.user_repository import UserRepository
from app.application.exceptions import conflict
from app.domain.auth.auth_schema import RegisterRequest
from app.domain.user.user_schema import UserRequest


class RegisterUseCase:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    async def excute(self, register_request: RegisterRequest):
        user = await self.user_repository.get_user_by_email(
            email=register_request.email
        )

        if user:
            raise conflict("User with this email already exists")

        user_request = UserRequest(
            email=register_request.email,
            password=register_request.password,
            name=register_request.username,
        )

        user_created = await self.user_repository.create_user(user_request)

        return user_created
