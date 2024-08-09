from domain.user.user_repository import UserRepository
from domain.user.user_schema import UserRequest
from infrastructure.database.dependencies import db_dependency


class UserService:
    def __init__(self, db: db_dependency):
        self.user_repository = UserRepository(db=db)

    async def get_users(self):
        return await self.user_repository.get_users()

    async def get_user_by_email(self, email: str):
        return await self.user_repository.get_user_by_email(email=email)

    async def get_user(self, id: str):
        return await self.user_repository.get_user(id=id)

    async def create_user(self, user_request: UserRequest):
        return await self.user_repository.create_user(user_request=user_request)


def get_user_service(db: db_dependency):
    return UserService(db=db)
