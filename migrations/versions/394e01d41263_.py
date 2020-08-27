"""empty message

Revision ID: 394e01d41263
Revises: f5af31397b1f
Create Date: 2020-08-27 12:58:01.247333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '394e01d41263'
down_revision = 'f5af31397b1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('movie_genrs', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'movie_genrs')
    # ### end Alembic commands ###
