"""empty message

Revision ID: 5e1a86d9fa1d
Revises: 7c9c44863173
Create Date: 2019-07-10 18:55:04.065504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e1a86d9fa1d'
down_revision = '7c9c44863173'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nodegroup', sa.Column('cpu_total', sa.Integer(), nullable=True))
    op.add_column('nodegroup', sa.Column('memory_total', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('nodegroup', 'memory_total')
    op.drop_column('nodegroup', 'cpu_total')
    # ### end Alembic commands ###
