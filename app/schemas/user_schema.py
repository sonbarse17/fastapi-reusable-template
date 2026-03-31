"""
Pydantic Schemas (user_schema.py)
=================================
This file defines validation contracts for incoming HTTP Requests and outgoing JSON Responses.
Unlike `user_model.py` which talks to the DB, these classes ensure users only send exactly
what they are supposed to, and we filter out sensitive fields (like hashed_password) before
sending JSON back to the frontend.
"""

from typing import Optional
from pydantic import BaseModel, EmailStr

# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None

# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str

# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None

# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

# Properties to return to client
class User(UserInDBBase):
    pass

# Properties properties stored in DB (including hash)
class UserInDB(UserInDBBase):
    hashed_password: str
