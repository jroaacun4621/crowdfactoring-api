"""empty message

Revision ID: 5225f0e5566f
Revises: 
Create Date: 2018-11-17 21:38:26.497972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5225f0e5566f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """
    Creates position and candidates tables
    """
    page_info_table = op.create_table('page_info',
                    sa.Column('id', sa.String()),
                    sa.Column('visits', sa.Integer(), default=0),
                    sa.PrimaryKeyConstraint('visits')
                    )
    op.bulk_insert(page_info_table,
                   [
                       {'id': 1, 'visits': 0}
                   ]
                   )

    pass


def downgrade():
    """
    Drop positions and candidates tables
    """
    op.drop_table('page_info')
    pass
