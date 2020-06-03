"""empty message

Revision ID: 6cf3f9d89970
Revises: 5cb6b0987329
Create Date: 2020-06-03 07:56:42.185254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cf3f9d89970'
down_revision = '5cb6b0987329'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('audiobook', sa.Column('name', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('audiobook', 'name')
    # ### end Alembic commands ###
