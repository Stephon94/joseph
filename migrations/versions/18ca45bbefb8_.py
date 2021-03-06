"""empty message

Revision ID: 18ca45bbefb8
Revises: f369da000157
Create Date: 2018-06-14 17:28:32.339000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18ca45bbefb8'
down_revision = 'f369da000157'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('url', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'url')
    # ### end Alembic commands ###
