from app.application.dependencies.current_user import current_user_dependency


class GetMeUseCase:
    def __init__(self, current_user: current_user_dependency) -> None:
        self.current_user = current_user

    async def excute(self):
        return self.current_user
