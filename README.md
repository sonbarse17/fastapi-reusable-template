# FastAPI Starter Template

A reusable FastAPI starter for building API-first applications with a clean folder structure, versioned routes, configuration management, SQLAlchemy integration, and optional server-rendered pages.

## Overview

This project includes:

- FastAPI application bootstrap in `app/main.py`
- Versioned API routes under `app/api/v1`
- SQLAlchemy setup with SQLite as the default local database
- Pydantic-based settings loaded from `.env`
- Password hashing and JWT token auth helpers
- Jinja2 templates and static assets for a simple homepage
- Docker and local Python development workflows

## Prerequisites

Choose one of the following ways to run the project.

### Docker workflow

Install:

- Docker Desktop or Docker Engine
- Docker Compose support via `docker compose`

Recommended checks:

```bash
docker --version
docker compose version
```

### Local Python workflow

Install:

- Python 3.12+ recommended
- `pip`
- A shell such as PowerShell, Command Prompt, Git Bash, or a Unix shell

Recommended checks:

```bash
python --version
pip --version
```

## Project Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd fastapi-reusable-template
```

If you already have the project locally, just open the repo root.

### 2. Create the environment file

Copy `.env.example` to `.env`.

macOS/Linux:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

### 3. Review environment variables

The defaults are enough for local development. The app currently uses SQLite by default, so no extra database service is required to get started.

Current environment template:

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

## Environment Variables Reference

### Application

- `PROJECT_NAME`
  Display name used by the FastAPI app metadata.

- `API_V1_STR`
  Base prefix for version 1 API routes. Default: `/api/v1`

- `ENVIRONMENT`
  General environment label such as `development`, `staging`, or `production`.

- `DEBUG`
  Boolean flag for development behavior. Use `true` or `false`.

- `BACKEND_CORS_ORIGINS`
  JSON-style list of allowed frontend origins.

### Security

- `SECRET_KEY`
  Secret used to sign JWT access tokens. Change this for any shared or production deployment.

- `ACCESS_TOKEN_EXPIRE_MINUTES`
  Token expiration in minutes.

### Database

- `DATABASE_URL`
  SQLAlchemy database connection string.
  Default uses a local SQLite file: `sqlite:///./sql_app.db`

## Running With Docker Compose

This is the easiest way to start the project because the app environment is built for you.

### Start the app

```bash
docker compose up --build
```

To run in detached mode:

```bash
docker compose up --build -d
```

### Stop the app

```bash
docker compose down
```

### View container status

```bash
docker compose ps
```

### View logs

```bash
docker compose logs
```

To follow logs live:

```bash
docker compose logs -f
```

### Rebuild after dependency or Dockerfile changes

```bash
docker compose up --build
```

## Running Locally With Python

### 1. Create a virtual environment

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the development server

macOS/Linux:

```bash
uvicorn app.main:app --reload
```

Windows PowerShell:

```powershell
.\venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

## Available URLs

Once the server is running, open:

- Home page: `http://localhost:8000/`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- Health check: `http://localhost:8000/api/v1/health`

Legacy support:

- `http://localhost:8000/health` redirects to `/api/v1/health`

## Authentication Flow

The project includes a token login endpoint:

- `POST /api/v1/login/access-token`

Typical flow:

1. Create a user with `POST /api/v1/users`
2. Log in with email and password at `POST /api/v1/login/access-token`
3. Use the returned bearer token for protected endpoints

You can also use the built-in Swagger UI at `/docs` to authorize requests.

## Example API Requests

### Create a user

```bash
curl -X POST "http://localhost:8000/api/v1/users" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"user@example.com\",\"password\":\"pass1234\",\"full_name\":\"Example User\"}"
```

### Log in

```bash
curl -X POST "http://localhost:8000/api/v1/login/access-token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=pass1234"
```

### Health check

```bash
curl "http://localhost:8000/api/v1/health"
```

## Project Structure

```text
app/                    # Main application package
  api/                  # API routers and dependencies
    v1/                 # Version 1 API namespace
  core/                 # Settings, logging, and security helpers
  db/                   # SQLAlchemy engine, sessions, and base registry
  middlewares/          # HTTP middleware
  models/               # SQLAlchemy ORM models
  routes/               # Template-rendered routes
  schemas/              # Pydantic request/response schemas
  services/             # Business logic and external integrations
  static/               # CSS and JavaScript assets
  templates/            # Jinja2 templates
  main.py               # FastAPI app entry point
tests/                  # Test package
scripts/                # Helper scripts
.env.example            # Example environment configuration
.env                    # Local environment overrides
Dockerfile              # Docker image definition
docker-compose.yml      # Docker Compose service definition
requirements.txt        # Python dependencies
README.md               # Project documentation
```

## Development Notes

- The app auto-creates tables on startup for local prototyping.
- SQLite is the default local database.
- Static assets are served from `/static`.
- The homepage uses Jinja2 templates from `app/templates`.
- Docker Compose bind-mounts the project directory for live code reload.

## Troubleshooting

### Docker daemon or permission errors

If Docker commands fail with daemon or permission errors:

- make sure Docker Desktop is running
- make sure your terminal can access Docker
- retry `docker compose up --build`

### Port 8000 already in use

If `localhost:8000` is occupied:

- stop the process using that port
- or change the published port in `docker-compose.yml`
- or run Uvicorn locally on a different port

### Environment variable parsing issues

If the app fails during startup due to settings validation:

- confirm `.env` matches `.env.example`
- make sure booleans use `true` or `false`
- make sure `BACKEND_CORS_ORIGINS` stays in JSON list format

### Dependency issues after changing packages

If you update `requirements.txt`:

- rebuild Docker images with `docker compose up --build`
- or reinstall locally with `pip install -r requirements.txt`

## Next Improvements

Typical next steps for this template:

- add automated tests for auth and user flows
- add Alembic for migrations
- add role-based authorization
- replace SQLite with Postgres for multi-user environments
- add CI checks for formatting, linting, and tests
