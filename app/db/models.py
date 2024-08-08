from sqlalchemy.orm import Mapped, mapped_column
from common.helpers.hash import check_hash, get_hash
from db.base import Base


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()


class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    _password: Mapped[str] = mapped_column(name="password")

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str) -> None:
        self._password = get_hash(password)

    def check_password(self, password: str) -> bool:
        return check_hash(password, self.password)
