"""
SQLAlchemy Base Registry (base.py)
==================================
Imports all SQLAlchemy models so that `Base.metadata` has them registered before being
imported by Alembic migrations or the `app.main` SQLite bootstrapper. Failure to import
models here means Alembic will generate blank migration files!
"""

# Import all the models, so that Base has them before being
# imported by Alembic or the app setup logic
from app.db.session import Base  # noqa
from app.models.user_model import User  # noqa
