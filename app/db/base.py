from datetime import UTC, datetime
from uuid import uuid4
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: uuid4().hex,
        sort_order=-3,
    )
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC),
        nullable=False,
        sort_order=-2,
        type_=TIMESTAMP(timezone=True),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
        sort_order=-1,
        type_=TIMESTAMP(timezone=True),
    )
