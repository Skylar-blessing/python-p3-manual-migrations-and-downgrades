"""Renaming students to scholars

Revision ID: 3e1147d4a3f1
Revises: 791279dd0760
Create Date: 2023-06-01 17:13:05.973563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e1147d4a3f1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
