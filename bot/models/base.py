from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

import utils


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return str(cls.__name__) + 's'

    id: Mapped[int] = mapped_column(
        sa.BigInteger(),
        primary_key=True,
        autoincrement=True,
        index=True,
        server_default=sa.Identity(
            always=False,
            start=1,
            increment=1,
            minvalue=1,
            maxvalue=9223372036854775807,
            cycle=False,
            cache=1,
        ),
    )


class BaseModel(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), default=utils.now)
    updated_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), default=utils.now, onupdate=utils.now)

