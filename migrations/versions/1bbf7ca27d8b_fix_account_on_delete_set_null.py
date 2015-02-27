"""fix_account_on_delete_set_null

Revision ID: 1bbf7ca27d8b
Revises: 39fa82d3168e
Create Date: 2015-02-18 17:34:38.115278

"""

# revision identifiers, used by Alembic.
revision = '1bbf7ca27d8b'
down_revision = '2d8a350b4885'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


def upgrade():
    conn = op.get_bind()
    conn.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
    conn.execute(text("ALTER TABLE account DROP FOREIGN KEY `account_ibfk_10`"))
    conn.execute(text("ALTER TABLE account ADD CONSTRAINT `account_ibfk_10` FOREIGN KEY (`default_calendar_id`) REFERENCES `calendar` (`id`) ON DELETE SET NULL"))
    conn.execute(text("SET FOREIGN_KEY_CHECKS=1;"))


def downgrade():
    conn = op.get_bind()

    conn.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
    conn.execute(text("ALTER TABLE account DROP FOREIGN KEY `account_ibfk_10`"))
    conn.execute(text("ALTER TABLE account ADD CONSTRAINT `account_ibfk_10` FOREIGN KEY (`default_calendar_id`) REFERENCES `calendar` (`id`)"))
    conn.execute(text("SET FOREIGN_KEY_CHECKS=1;"))
