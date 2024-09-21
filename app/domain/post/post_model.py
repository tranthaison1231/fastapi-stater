from sqlalchemy.orm import Mapped, mapped_column

from app.domain.base.base_model import Base


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
