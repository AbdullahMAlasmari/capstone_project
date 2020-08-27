"""empty message

Revision ID: f5af31397b1f
Revises: 
Create Date: 2020-08-27 12:57:40.717138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5af31397b1f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'movie_genrs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('movie_genrs', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
