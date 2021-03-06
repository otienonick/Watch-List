"""Initial Migration

Revision ID: 3fce4df08b30
Revises: 02df1c186ee2
Create Date: 2021-09-15 16:09:28.896037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fce4df08b30'
down_revision = '02df1c186ee2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
