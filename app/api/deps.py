"""
Dependencies Module (deps.py)
=============================
This file stores reusable FastAPI Dependencies. Dependencies run BEFORE the endpoint logic
executes. They are perfect for extracting JWT tokens from headers, connecting to databases,
and verifying user roles.
"""

from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal
from app.models.user_model import User
from app.schemas.user_schema import User as UserSchema

# This tells FastAPI where the client should send the request to get the token.
# It automatically generates the visual "Authorize" button in the /docs Swagger UI!
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)

def get_db() -> Generator:
    """
    Dependency to yield a SQLAlchemy Database session per request.
    This pattern ensures the database connection closes safely even if the endpoint crashes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    """
    Dependency that intercepts the request, grabs the JWT Bearer token from the Auth header,
    validates the cryptographic signature, and returns the User object from the database.
    If the token is invalid or expired, it raises a 403 Forbidden.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = payload.get("sub")
        if token_data is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    user = db.query(User).filter(User.id == int(token_data)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Wrap get_current_user to also check if the user is_active.
    Use this dependency to secure endpoints:
    `def my_secure_route(user: User = Depends(get_current_active_user)): ...`
    """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
