"""empty message

Revision ID: 99f4ee6e7604
Revises: 
Create Date: 2022-11-25 17:10:18.605248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99f4ee6e7604'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pre_1', sa.String(), nullable=False),
    sa.Column('pre_2', sa.String(), nullable=False),
    sa.Column('pre_3', sa.String(), nullable=False),
    sa.Column('pre_4', sa.String(), nullable=False),
    sa.Column('pre_5', sa.String(), nullable=False),
    sa.Column('pre_6', sa.String(), nullable=False),
    sa.Column('post_1', sa.String(), nullable=False),
    sa.Column('post_2', sa.String(), nullable=False),
    sa.Column('post_3', sa.String(), nullable=False),
    sa.Column('post_4', sa.String(), nullable=False),
    sa.Column('post_5', sa.String(), nullable=False),
    sa.Column('post_6', sa.String(), nullable=False),
    sa.Column('post_7', sa.String(), nullable=False),
    sa.Column('post_8', sa.String(), nullable=False),
    sa.Column('interface_1_id', sa.String(), nullable=False),
    sa.Column('interface_2_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('response')
    # ### end Alembic commands ###