__all__ = (
    'Database',
)

from typing import Literal

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Database(Base):
    __tablename__ = 'databases'

    project_name: Mapped['str'] = mapped_column(
        sa.String,
        unique=True,
    )
    name: Mapped['str'] = mapped_column(
        sa.String,
    )
    password: Mapped['str'] = mapped_column(
        sa.String,
    )
    user: Mapped['str'] = mapped_column(
        sa.String,
    )
    host: Mapped['str'] = mapped_column(
        sa.String,
        default='localhost'
    )
    port: Mapped['int'] = mapped_column(
        sa.Integer,
        default=5432
    )
    interval: Mapped['str'] = mapped_column(
        sa.String(255),
    )
    api: Mapped['str'] = mapped_column(
        sa.String,
    )

    interval_type: Mapped[Literal['hour', 'day', 'month', 'minute', 'schedule']] = mapped_column(
        sa.String(25),
    )



