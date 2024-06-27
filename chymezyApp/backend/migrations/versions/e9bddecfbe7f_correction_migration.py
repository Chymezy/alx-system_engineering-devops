"""correction migration

Revision ID: e9bddecfbe7f
Revises: 
Create Date: 2024-06-26 18:15:13.467323

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e9bddecfbe7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('analytics', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('analytics', sa.Column('username', mysql.VARCHAR(length=80), nullable=False))
    # ### end Alembic commands ###
