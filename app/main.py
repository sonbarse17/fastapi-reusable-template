"""
FastAPI Phase-2 Application
============================
Application entry point responsible for:
- Initializing the FastAPI app instance
- Registering global middleware (logging, CORS, etc.)
- Registering API v1 routers and UI template routes
- Mounting static file directories
- Loading core configuration
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.router import api_router
from app.routes import home
from app.middlewares.request_logger import RequestLoggerMiddleware
from app.db.session import engine, Base

# PROTOTYPING SETUP: 
# This command tells SQLAlchemy to auto-create SQLite tables based on models/ classes.
# In a real Production environment, you should DELETE this and use Alembic migrations instead!
Base.metadata.create_all(bind=engine)

# Primary FastAPI Instance initialization
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A structured FastAPI Phase-2 architecture for scaling teams.",
    version="2.0.0",
)

# 1. Add Middlewares (Cross-Cutting Concerns)
app.add_middleware(RequestLoggerMiddleware)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# 2. Mount static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 3. Register UI routes (Phase-1 Legacy/Hybrid Layout)
app.include_router(home.router)

# 4. Register API v1 Controllers (Phase-2 additions)
app.include_router(api_router, prefix=settings.API_V1_STR)
