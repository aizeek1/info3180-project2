"""empty message

Revision ID: f1ef372cbe66
Revises: 1c19fb3e4e4b
Create Date: 2017-04-26 23:33:53.726919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1ef372cbe66'
down_revision = '1c19fb3e4e4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wishlist',
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('itemid', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=2500), nullable=True),
    sa.Column('item_url', sa.String(length=255), nullable=True),
    sa.Column('image_url', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('itemid'),
    sa.UniqueConstraint('itemid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wishlist')
    # ### end Alembic commands ###
