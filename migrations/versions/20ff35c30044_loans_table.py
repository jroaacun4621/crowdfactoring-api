"""empty message

Revision ID: 20ff35c30044
Revises: 5225f0e5566f
Create Date: 2018-11-23 00:27:38.473161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20ff35c30044'
down_revision = '5225f0e5566f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('loans',
                    sa.Column('id', sa.Text(), nullable=False),
                    sa.Column('count_id', sa.Text(), nullable=True),
                    sa.Column('value', sa.Text(), nullable=True),
                    sa.Column('interest', sa.Integer(), nullable=True),
                    sa.Column('sold_percent', sa.Integer(), nullable=True),
                    sa.Column('investor', sa.Text(), nullable=True),
                    sa.Column('product_type', sa.Text(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('loans')
