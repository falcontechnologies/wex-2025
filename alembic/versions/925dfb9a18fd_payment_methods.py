"""payment_methods

Revision ID: 925dfb9a18fd
Revises: 475dad56634e
Create Date: 2025-04-06 14:34:50.828165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '925dfb9a18fd'
down_revision: Union[str, None] = '475dad56634e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'payment_method',
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String),
    sa.Column('type', sa.String),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id', ondelete='CASCADE'))
)



def downgrade() -> None:
    op.drop_table('payment_method')

