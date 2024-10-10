from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa


class User(BaseModel):
    __tablename__ = 'users'
    chat_id: Mapped[int] = mapped_column(sa.INTEGER, unique=True, nullable=False)

