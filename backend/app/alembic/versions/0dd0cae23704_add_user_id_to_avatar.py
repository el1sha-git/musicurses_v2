"""add user_id to avatar

Revision ID: 0dd0cae23704
Revises: e0e1ab64525b
Create Date: 2021-06-08 17:32:31.542559

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0dd0cae23704'
down_revision = 'e0e1ab64525b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('avatar', sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('avatar', 'user_id')
    # ### end Alembic commands ###