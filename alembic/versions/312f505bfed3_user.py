"""User

Revision ID: 312f505bfed3
Revises: 
Create Date: 2025-04-06 14:33:01.569960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '312f505bfed3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'user',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('email', sa.String, nullable=False),
    sa.Column('phone_number', sa.String),
    sa.Column('username', sa.String, nullable=False),
    sa.Column('password', sa.String, nullable=False),
    sa.Column('role', sa.String, nullable=False),
    sa.Column('created_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP')),
    sa.Column('last_login', sa.DateTime)
)


def downgrade() -> None:
    op.drop_table('user')

