from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.database.base import Base
import bcrypt  # type: ignore


class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    _password: Mapped[str] = mapped_column(name="password")

    @property
    def password(self) -> str:
        return self._password

    @staticmethod
    def get_hash(value: str) -> str:
        return bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @staticmethod
    def check_hash(value: str, hashed: str) -> bool:
        return bcrypt.checkpw(value.encode("utf-8"), hashed.encode("utf-8"))

    @password.setter
    def password(self, password: str) -> None:
        self._password = self.get_hash(password)

    def check_password(self, password: str) -> bool:
        return self.check_hash(password, self.password)
