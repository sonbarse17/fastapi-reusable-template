"""
Business Logic Service
======================
Contains core business logic separated from route handlers.
This ensures cleaner routes, reusable logic, and better testability.

Extend this module with:
- AI inference calls
- Database operations
- External API integrations
- Data transformation logic
- Workflow orchestration
"""


def get_welcome_message() -> str:
    """Return the welcome message displayed on the home page."""
    return "Welcome to FastAPI Starter Template"
