"""initial migration

Revision ID: 3b3beb603ca0
Revises: de6c6d1160cf
Create Date: 2018-05-18 15:00:44.314012

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3b3beb603ca0'
down_revision = 'de6c6d1160cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'gavatar_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('gavatar_hash', mysql.VARCHAR(length=32), nullable=True))
    # ### end Alembic commands ###
