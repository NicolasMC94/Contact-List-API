"""empty message

Revision ID: 37a6b42e8a27
Revises: 4909f627cfbb
Create Date: 2022-09-21 18:07:13.105439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37a6b42e8a27'
down_revision = '4909f627cfbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact_group',
    sa.Column('contact_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('contact_id', 'group_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact_group')
    op.drop_table('group')
    op.drop_table('contact')
    # ### end Alembic commands ###