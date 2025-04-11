"""Subscription

Revision ID: 475dad56634e
Revises: 312f505bfed3
Create Date: 2025-04-06 14:34:21.298419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '475dad56634e'
down_revision: Union[str, None] = '312f505bfed3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'subscription',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id', ondelete='CASCADE')),
    sa.Column('name', sa.String),
    sa.Column('service_provider', sa.String),
    sa.Column('start_date', sa.DateTime, nullable=False),
    sa.Column('expiry_date', sa.DateTime),
    sa.Column('is_trial', sa.Integer, sa.CheckConstraint('is_trial IN (0,1)'), nullable=False),
    sa.Column('is_recurring', sa.Integer, sa.CheckConstraint('is_recurring IN (0,1)'), nullable=False),
    sa.Column('payment_frequency', sa.String, nullable=False),
    sa.Column('cost', sa.Float),
    sa.Column('status', sa.String, nullable=False),
    sa.Column('subscription_type', sa.String),
    sa.Column('created_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'))
)


def downgrade() -> None:
    op.drop_table('subscription')

