"""empty message

Revision ID: e1d407c1fc1e
Revises: None
Create Date: 2016-06-23 19:08:52.071058

"""

# revision identifiers, used by Alembic.
revision = 'e1d407c1fc1e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=25), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.Column('is_auth', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###