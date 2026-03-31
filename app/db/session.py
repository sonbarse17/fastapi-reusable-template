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

# SQLite needs a special thread-safety flag; other engines should use default arguments.
engine_kwargs = {}
if settings.DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(settings.DATABASE_URL, **engine_kwargs)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
