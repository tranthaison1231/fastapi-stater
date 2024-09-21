from abc import ABC, abstractmethod

from app.domain.user.user_model import User
from app.domain.user.user_schema import UserRequest


class UserRepositoryInterface(ABC):
    @abstractmethod
    async def get_users(self) -> list[User]:
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    async def get_user(self, id: str) -> User | None:
        pass

    @abstractmethod
    async def create_user(self, user_request: UserRequest) -> User:
        pass
