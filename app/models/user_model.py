"""
SQLAlchemy Models (user_model.py)
=================================
This file defines the actual Database Tables. It maps Python classes directly to SQL queries.
WARNING: DO NOT use these identical classes for returning JSON to the user! Always parse
database models through Pydantic schemas before returning them to avoid leaking passwords.
"""

from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
