"""empty message

Revision ID: e40a35f90fa3
Revises: 7ba60adbad61
Create Date: 2016-06-24 14:18:58.538724

"""

# revision identifiers, used by Alembic.
revision = 'e40a35f90fa3'
down_revision = '7ba60adbad61'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_moderator', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('is_staff', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_staff')
    op.drop_column('users', 'is_moderator')
    ### end Alembic commands ###