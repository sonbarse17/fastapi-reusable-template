"""
API V1 Master Router (router.py)
================================
Registers and aggregates all sub-routers (like /users and /auth) into one central
`api_router`. You only need to import this one router into `app/main.py`.
"""

from fastapi import APIRouter
from app.api.v1.endpoints import users, auth, health

api_router = APIRouter()
api_router.include_router(auth.router, tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(health.router, tags=["Health"])
