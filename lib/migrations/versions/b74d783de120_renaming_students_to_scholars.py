"""Renaming students to scholars

Revision ID: b74d783de120
Revises: 791279dd0760
Create Date: 2024-03-15 22:53:10.410397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b74d783de120'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
