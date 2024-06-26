"""Increase password_hash column size

Revision ID: 1723ba2fa637
Revises: 60a3a8d150ba
Create Date: 2024-06-22 02:14:20.111191

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1723ba2fa637'
down_revision = '60a3a8d150ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=255),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=False)
    # ### end Alembic commands ###
