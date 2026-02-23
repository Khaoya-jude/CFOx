import psycopg2
from psycopg2.extras import RealDictCursor
import json
from app.utils.logging import get_logger
import os

DATABASE_URL = os.getenv("DATABASE_URL")


logger = get_logger(__name__)

class PostgresMemory:
    """
    Persistent long-term memory for CFOx using Postgres.
    """

    def __init__(self, dsn: str):
        self.dsn = dsn
        self.conn = psycopg2.connect(dsn, cursor_factory=RealDictCursor)
        self._ensure_table()

    def _ensure_table(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS cfox_memory (
                    id SERIAL PRIMARY KEY,
                    event JSONB,
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)
            self.conn.commit()

    def remember(self, event: dict):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO cfox_memory (event) VALUES (%s);",
                (json.dumps(event),)
            )
            self.conn.commit()
            logger.info("Event persisted to Postgres memory")
    
    def recall(self, query: dict = None):
        with self.conn.cursor() as cur:
            cur.execute("SELECT event FROM cfox_memory ORDER BY created_at DESC;")
            results = cur.fetchall()
            return [r['event'] for r in results]

# Module-level memory instance (only if DATABASE_URL is provided)
memory = PostgresMemory(dsn=DATABASE_URL) if DATABASE_URL else None
