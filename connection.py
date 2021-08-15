import psycopg2
from psycopg2.extras import RealDictCursor
from decouple import config

try:
    conn = psycopg2.connect(config("DATABASE_URL"))
    cursor = conn.cursor(cursor_factory=RealDictCursor)
except:
    "failed to establish connection"
