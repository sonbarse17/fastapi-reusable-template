"""
UI / Frontend Routes (home.py)
==============================
This is a legacy "Phase 1" hybrid route. While all backend data REST APIs live in `app/api/v1/...`,
you can still use FastAPI to serve fully Server-Side Rendered (SSR) HTML pages utilizing Jinja2
templates. This is exceptionally useful for Admin Dashboards or simple landing pages.
"""

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.business_logic import get_welcome_message

router = APIRouter(tags=["Home"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def home(request: Request):
    """Render the home page with a welcome message."""
    message = get_welcome_message()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": message},
    )
