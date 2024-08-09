from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.database.base import Base


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
