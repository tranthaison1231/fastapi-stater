from db.models import User
from db.dependency import db_dependency


class UserService:
    def __init__(self, db: db_dependency):
        self.db = db

    async def get_users(self):
        users = self.db.query(User).all()

        return users

