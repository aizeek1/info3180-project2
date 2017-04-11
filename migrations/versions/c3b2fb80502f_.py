"""empty message

Revision ID: c3b2fb80502f
Revises: e9ed62215d6b
Create Date: 2017-04-10 00:44:16.704825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3b2fb80502f'
down_revision = 'e9ed62215d6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=180), nullable=True),
    sa.Column('hash_number', sa.String(length=180), nullable=True),
    sa.Column('secretques', sa.String(length=255), nullable=True),
    sa.Column('secretans', sa.String(length=180), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('accept_tos', sa.String(length=6), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('userid'),
    sa.UniqueConstraint('userid'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###