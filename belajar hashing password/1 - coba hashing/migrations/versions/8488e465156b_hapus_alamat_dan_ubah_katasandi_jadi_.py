"""hapus alamat dan ubah katasandi jadi katasandi hash

Revision ID: 8488e465156b
Revises: bf199af2a3f5
Create Date: 2022-09-16 19:14:48.301691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8488e465156b'
down_revision = 'bf199af2a3f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pengguna', sa.Column('kataSandi_hash', sa.String(length=128), nullable=False))
    op.drop_column('pengguna', 'kataSandi')
    op.drop_column('pengguna', 'alamat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pengguna', sa.Column('alamat', sa.VARCHAR(length=128), nullable=True))
    op.add_column('pengguna', sa.Column('kataSandi', sa.VARCHAR(length=100), nullable=False))
    op.drop_column('pengguna', 'kataSandi_hash')
    # ### end Alembic commands ###