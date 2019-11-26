"""empty message

Revision ID: set_defaults_default_value
Revises: 1736fd8cb271
Create Date: 2018-04-17 15:18:43.863248

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'set_defaults_default_value'
down_revision = '1736fd8cb271'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("role", "defaults", server_default='{}')
    op.alter_column("provider", "defaults", server_default='{}')
    op.alter_column("region", "defaults", server_default='{}')
    op.alter_column("zone", "defaults", server_default='{}')
    op.alter_column("environment", "defaults", server_default='{}')
    op.alter_column("application", "defaults", server_default='{}')
    op.alter_column("stack", "defaults", server_default='{}')
    op.alter_column("service", "defaults", server_default='{}')
    op.alter_column("deployment", "defaults", server_default='{}')
    op.alter_column("service_config", "defaults", server_default='{}')


def downgrade():
    op.alter_column("role", "role", server_default=None)
    op.alter_column("provider", "defaults", server_default=None)
    op.alter_column("region", "defaults", server_default=None)
    op.alter_column("zone", "defaults", server_default=None)
    op.alter_column("environment", "defaults", server_default=None)
    op.alter_column("application", "defaults", server_default=None)
    op.alter_column("stack", "defaults", server_default=None)
    op.alter_column("service", "defaults", server_default=None)
    op.alter_column("deployment", "defaults", server_default=None)
    op.alter_column("service_config", "defaults", server_default=None)
