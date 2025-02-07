"""empty message

Revision ID: 7c9c44863173
Revises: 65c77e24f90c
Create Date: 2019-07-10 18:52:32.349866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c9c44863173'
down_revision = '65c77e24f90c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nodegroup',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('deployment_target_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('defaults', sa.Text(), server_default='{}', nullable=True),
    sa.ForeignKeyConstraint(['deployment_target_id'], ['deployment_target.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nodegroup')
    # ### end Alembic commands ###
