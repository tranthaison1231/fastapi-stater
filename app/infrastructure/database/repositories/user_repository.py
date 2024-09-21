from app.domain.user.user_interface import UserRepositoryInterface
from app.domain.user.user_model import User
from app.domain.user.user_schema import UserRequest
from app.infrastructure.database.dependencies import db_dependency


class UserRepository(UserRepositoryInterface):
    def __init__(self, db: db_dependency) -> None:
        self.db = db

    async def get_users(self):
        return self.db.query(User).all()

    async def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    async def get_user(self, id: str):
        return self.db.query(User).filter(User.id == id).first()

    async def create_user(self, user_request: UserRequest):
        user = User(
            email=user_request.email,
            password=user_request.password,
            name=user_request.name,
        )

        self.db.add(user)
        self.db.commit()

        return user
