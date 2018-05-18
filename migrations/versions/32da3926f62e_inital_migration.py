"""inital migration

Revision ID: 32da3926f62e
Revises: 2d9e75cd0912
Create Date: 2018-05-11 16:27:29.556089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32da3926f62e'
down_revision = '2d9e75cd0912'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
