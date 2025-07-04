"""initial migration

Revision ID: 38eb2a3e2d53
Revises: 
Create Date: 2025-06-18 18:42:57.812135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38eb2a3e2d53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Earthquakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('magnitude', sa.Float(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Earthquakes')
    # ### end Alembic commands ###
