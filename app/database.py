from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:********%405@localhost/aiqa"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

try:
    conn = engine.connect()
    print("✅ Database connected successfully!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:")
    print(e)