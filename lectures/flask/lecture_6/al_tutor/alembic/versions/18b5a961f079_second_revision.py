"""Second revision

Revision ID: 18b5a961f079
Revises: 4fef86c6d6aa
Create Date: 2021-03-11 19:59:04.593303

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '18b5a961f079'
down_revision = '4fef86c6d6aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pets',
        sa.Column('id', postgresql.INTEGER(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=True),
    )


def downgrade():
    op.drop_table('pets')
