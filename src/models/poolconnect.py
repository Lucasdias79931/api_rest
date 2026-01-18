from psycopg_pool import AsyncConnectionPool
from ..config import settings_db





pool = AsyncConnectionPool(
    conninfo=settings_db.DATABASE_URL,
    min_size=settings_db.MIN_SIZE,
    max_size=settings_db.MAX_SIZE,

)