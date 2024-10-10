from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import Integer, DateTime
import utils


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class BaseModel(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(DateTime, default=utils.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=utils.now, onupdate=utils.now)

