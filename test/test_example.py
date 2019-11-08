from .dbtest import (
    DbTest,
    dbconnect
)

import os
from psycopg2.extras import RealDictCursor


PATH_TO_SQL_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "sql"
    )
)

class TestExample(DbTest):
    @dbconnect
    def test_select_organizations(self, conn):
        self.load_fixtures(
            conn,
            os.path.join(PATH_TO_SQL_DIR, "organizations.sql")
        )

        sql = """
        SELECT * FROM organizations;
        """
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql)
            organizations = cur.fetchall()
            
            assert len(organizations) == 7


    @dbconnect
    def test_select_addresses(self, conn):
        self.load_fixtures(
            conn,
            os.path.join(PATH_TO_SQL_DIR, "organizations.sql")
        )

        sql = """
        SELECT * FROM addresses;
        """
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql)
            addresses = cur.fetchall()
            
            assert len(addresses) == 7
