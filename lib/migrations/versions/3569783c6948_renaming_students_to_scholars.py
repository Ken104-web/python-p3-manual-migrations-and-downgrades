"""Renaming students to scholars

Revision ID: 3569783c6948
Revises: 791279dd0760
Create Date: 2023-09-01 09:41:38.832121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3569783c6948'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
