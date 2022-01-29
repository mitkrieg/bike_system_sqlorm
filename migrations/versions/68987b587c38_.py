"""empty message

Revision ID: 68987b587c38
Revises: 8f7bb7718b39
Create Date: 2022-01-29 17:36:28.085564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68987b587c38'
down_revision = '8f7bb7718b39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('trips', 'bike_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('trips', 'rider_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('trips', 'rider_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('trips', 'bike_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
