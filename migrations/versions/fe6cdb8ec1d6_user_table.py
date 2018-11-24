"""empty message

Revision ID: fe6cdb8ec1d6
Revises: 20ff35c30044
Create Date: 2018-11-24 16:19:21.789500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe6cdb8ec1d6'
down_revision = '20ff35c30044'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('auth_id', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.add_column('loans', sa.Column('user_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'loans', 'users', ['user_id'], ['id'])


def downgrade():
    op.drop_constraint(None, 'loans', type_='foreignkey')
    op.drop_column('loans', 'user_id')
    op.drop_table('users')
