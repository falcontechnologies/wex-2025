"""transaction_history

Revision ID: d9603a5d42d0
Revises: 925dfb9a18fd
Create Date: 2025-04-06 14:35:13.058316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9603a5d42d0'
down_revision: Union[str, None] = '925dfb9a18fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'transaction_history',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('subscription_id', sa.Integer, sa.ForeignKey('subscription.id', ondelete='CASCADE')),
    sa.Column('payment_id', sa.Integer, sa.ForeignKey('payment_method.id', ondelete='CASCADE')),
    sa.Column('amount_paid', sa.Float, nullable=False),
    sa.Column('date_paid', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'))
)


def downgrade() -> None:
    op.drop_table('transaction_history')
