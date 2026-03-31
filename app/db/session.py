"""
Database Session Manager (session.py)
=====================================
Sets up the central connection to the physical database file (`sqlite:///./sql_app.db`).
The `SessionLocal` class is used by Dependency Injection (`get_db`) to create isolated
database connections for every API request, preventing cross-talk between requests.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

# Since we are using SQLite, we need connect_args={"check_same_thread": False}
engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
