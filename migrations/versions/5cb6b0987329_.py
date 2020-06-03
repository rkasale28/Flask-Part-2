"""empty message

Revision ID: 5cb6b0987329
Revises: b89b672bcc5a
Create Date: 2020-06-03 07:43:41.764539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cb6b0987329'
down_revision = 'b89b672bcc5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('listener', sa.Column('profile_pic', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('listener', 'profile_pic')
    # ### end Alembic commands ###
