# FastAPI Starter Template

A standardized FastAPI starter structure that helps teams begin feature development quickly while keeping the codebase scalable, readable, and easy to extend.

## Features

- API versioning with a modular `v1` router structure
- SQLAlchemy session management with SQLite for local development
- Centralized configuration, logging, and security setup
- Pydantic schemas for request and response validation
- Service-layer separation for business and AI logic
- Middleware support for cross-cutting concerns like request logging
- Docker and local Python workflows for development

## Getting Started

### Environment Setup

1. Create your local environment file:
   ```bash
   cp .env.example .env
   ```
   On Windows PowerShell:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Review `.env` and update values if needed.

The default configuration uses SQLite, so the project can run locally without extra infrastructure.

### Option 1: Using Docker Compose

1. Make sure Docker and Docker Compose are installed.
2. Start the application:
   ```bash
   docker compose up --build
   ```
3. Stop the application when finished:
   ```bash
   docker compose down
   ```

### Option 2: Using a Local Python Environment

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   On Windows PowerShell:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```
   On Windows PowerShell:
   ```powershell
   .\venv\Scripts\python.exe -m uvicorn app.main:app --reload
   ```

## View Application

Once the server is running, open:

- Application home: [http://localhost:8000/](http://localhost:8000/)
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Health check: [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)

## Environment Variables

The app settings are loaded from `.env` through Pydantic settings. A starter template is provided in `.env.example`.

```env
PROJECT_NAME="FastAPI Starter App"
API_V1_STR="/api/v1"
ENVIRONMENT="development"
DEBUG=true
BACKEND_CORS_ORIGINS=["http://localhost","http://localhost:8000","http://localhost:3000"]
SECRET_KEY="change-me-in-production"
ACCESS_TOKEN_EXPIRE_MINUTES=11520
DATABASE_URL="sqlite:///./sql_app.db"
```

## Project Structure

```text
app/                    # Application package
  api/v1/endpoints/     # Versioned API endpoints
  core/                 # Configuration, logging, security
  db/                   # Database engine and base setup
  middlewares/          # Request and response middleware
  models/               # SQLAlchemy models
  routes/               # Template-rendered routes
  schemas/              # Pydantic schemas
  services/             # Business and AI service layer
  static/               # CSS and JavaScript assets
  templates/            # Jinja2 templates
  main.py               # FastAPI application entry point
scripts/                # Utility scripts
tests/                  # Test suite
.env.example            # Shareable environment template
.env                    # Local environment overrides
docker-compose.yml      # Docker Compose app startup
Dockerfile              # Container build definition
requirements.txt        # Python dependencies
```

## Future Iterations

This starter can be extended with richer database integrations, authentication flows, background workers, caching, and testing layers without restructuring the entire application.
