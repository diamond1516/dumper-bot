__all__ = (
    'Database',
)

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base



class Database(Base):
    __tablename__ = 'databases'

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



