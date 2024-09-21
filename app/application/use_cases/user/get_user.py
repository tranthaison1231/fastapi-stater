from app.domain.user.user_abstract import UserRepositoryInterface


class GetUserUseCase:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    async def excute(self, id: str):
        return await self.user_repository.get_user(id=id)
