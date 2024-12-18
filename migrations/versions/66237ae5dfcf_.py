"""empty message

Revision ID: 66237ae5dfcf
Revises: 4c5b98573318
Create Date: 2024-11-07 10:13:13.801204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66237ae5dfcf'
down_revision = '4c5b98573318'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_genre',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'genre_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_genre')
    # ### end Alembic commands ###
