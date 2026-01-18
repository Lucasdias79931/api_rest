from dotenv import load_dotenv
from psycopg_pool import AsyncConnectionPool
import os, asyncio, psycopg
from ..config import settings


DATABASE_URL = settings.DATABASE_URL