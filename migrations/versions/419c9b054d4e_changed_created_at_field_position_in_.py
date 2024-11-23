"""changed created at field position in Staff tables

Revision ID: 419c9b054d4e
Revises: 87e5fdc575b7
Create Date: 2024-11-23 02:02:36.937068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '419c9b054d4e'
down_revision = '87e5fdc575b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff', schema=None) as batch_op:
        batch_op.drop_column('pin')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pin', sa.TEXT(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###