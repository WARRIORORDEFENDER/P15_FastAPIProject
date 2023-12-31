"""models created

Revision ID: 69c7a073be91
Revises: 
Create Date: 2023-12-16 14:09:23.990301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '69c7a073be91'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('phone', sa.String(), nullable=True),
                    sa.Column('username', sa.String(), nullable=True),
                    sa.Column('password', sa.String(), nullable=True),
                    sa.Column('birth_date', sa.Date(), nullable=True),
                    sa.Column('balance', sa.Float(), nullable=True),
                    sa.Column('registered_date', sa.TIMESTAMP(), nullable=True),
                    sa.Column('last_login', sa.TIMESTAMP(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('product',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('owner_id', sa.Integer(), nullable=True),
                    sa.Column('category', sa.Integer(), nullable=True),
                    sa.Column('topic', sa.Integer(), nullable=True),
                    sa.Column('compatible', sa.String(), nullable=True),
                    sa.Column('price', sa.Integer(), nullable=True),
                    sa.Column('sold_count', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('role',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('category',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('product_count', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('comment',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('product_id', sa.Integer(), nullable=True),
                    sa.Column('message', sa.Text(), nullable=True),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('hashtags',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('product_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('topic',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('product_count', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user_saved_items',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('product_id', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_saved_items')
    op.drop_table('topic')
    op.drop_table('hashtags')
    op.drop_table('comment')
    op.drop_table('category')
    op.drop_table('role')
    op.drop_table('product')
    op.drop_table('user')
    # ### end Alembic commands ###
