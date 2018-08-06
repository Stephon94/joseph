"""empty message

Revision ID: e91d3a90a903
Revises: 
Create Date: 2018-06-14 16:54:01.626000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e91d3a90a903'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('about', sa.String(length=100), nullable=True),
    sa.Column('linkedin', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('about', sa.String(length=250), nullable=True),
    sa.Column('client_or_team', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('section',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('header', sa.String(length=50), nullable=True),
    sa.Column('content1', sa.String(length=500), nullable=True),
    sa.Column('content2', sa.String(length=500), nullable=True),
    sa.Column('content3', sa.String(length=500), nullable=True),
    sa.Column('image', sa.String(length=50), nullable=True),
    sa.Column('bg_image', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('social_media_link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('icon', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tech',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('icon', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member_stack',
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('tech_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.ForeignKeyConstraint(['tech_id'], ['tech.id'], )
    )
    op.create_table('project_stack',
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('tech_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['tech_id'], ['tech.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_stack')
    op.drop_table('member_stack')
    op.drop_table('tech')
    op.drop_table('social_media_link')
    op.drop_table('section')
    op.drop_table('project')
    op.drop_table('member')
    # ### end Alembic commands ###