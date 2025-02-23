"""initial

Revision ID: 5831e6778b61
Revises: 
Create Date: 2025-02-23 16:14:20.800113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5831e6778b61'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('databases',
    sa.Column('project_name', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('user', sa.String(), nullable=False),
    sa.Column('host', sa.String(), nullable=False),
    sa.Column('port', sa.Integer(), nullable=False),
    sa.Column('interval', sa.Integer(), nullable=False),
    sa.Column('api', sa.String(), nullable=False),
    sa.Column('id', sa.BigInteger(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('project_name')
    )
    op.create_index(op.f('ix_databases_id'), 'databases', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_databases_id'), table_name='databases')
    op.drop_table('databases')
    # ### end Alembic commands ###
