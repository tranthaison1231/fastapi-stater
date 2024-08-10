from fastapi import Depends
from domain.user.user_repository import UserRepository


class GetUsersUseCase:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    async def excute(self):
        return await self.user_repository.get_users()
