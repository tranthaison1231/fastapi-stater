from app.domain.user.user_schema import UserRequest
from app.domain.user.user_model import User
from app.infrastructure.database.dependencies import db_dependency


class UserRepository:
    def __init__(self, db: db_dependency):
        self.db = db

    async def get_users(self):
        users = self.db.query(User).all()

        return users

    async def get_user_by_email(self, email: str) -> User | None:
        user = self.db.query(User).filter(User.email == email).first()

        return user

    async def get_user(self, id: str):
        user = self.db.query(User).filter(User.id == id).first()

        return user

    async def create_user(self, user_request: UserRequest):
        user = User(
            email=user_request.email,
            password=user_request.password,
            name=user_request.name,
        )

        self.db.add(user)
        self.db.commit()

        return user
