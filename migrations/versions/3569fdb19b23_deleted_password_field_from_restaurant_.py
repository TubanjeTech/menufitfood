"""deleted password field from restaurant table

Revision ID: 3569fdb19b23
Revises: b10012f4b346
Create Date: 2024-11-22 12:28:53.177003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3569fdb19b23'
down_revision = 'b10012f4b346'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
