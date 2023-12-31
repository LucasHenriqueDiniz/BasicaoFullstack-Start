"""Created livro database

Revision ID: b8c1f3fd1b69
Revises: 
Create Date: 2023-08-15 15:57:40.266196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8c1f3fd1b69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('livro',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('titulo', sa.String(length=255), nullable=False),
    sa.Column('autor', sa.String(length=255), nullable=False),
    sa.Column('ano_publicacao', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=255), nullable=False),
    sa.Column('capa', sa.String(length=255), nullable=True),
    sa.Column('sinopse', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('titulo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('livro')
    # ### end Alembic commands ###
