"""empty message

Revision ID: 5bca3dd9481e
Revises: 1a4e9b644d60
Create Date: 2025-05-18 10:40:22.833053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bca3dd9481e'
down_revision = '1a4e9b644d60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app', schema=None) as batch_op:
        batch_op.add_column(sa.Column('flag', sa.DECIMAL(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app', schema=None) as batch_op:
        batch_op.drop_column('flag')

    # ### end Alembic commands ###
