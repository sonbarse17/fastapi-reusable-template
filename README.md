# FastAPI Starter Template

A standardized FastAPI starter structure that enables developers to quickly begin feature development while maintaining scalability, readability, and separation of concerns.

## Features

- **API Versioning** using a modular router structure (`v1`).
- **Database Backend** with SQLAlchemy session management (SQLite).
- **Core Abstraction** handling configuration, security, and logging.
- **Request Validation** enforcing clear contracts using Pydantic schemas.
- **Service Isolation** separating endpoints from business and AI logic.
- **Middlewares** for cross-cutting logic like request logging.
- **Evergreen Dependencies** configured to always pull the latest stable version of packages (FastAPI, SQLAlchemy, Pydantic, etc.) for a completely up-to-date starting point.

## Getting Started

### Option 1: Using Docker (Recommended)

The easiest way to get started is using Docker Compose. It will automatically build the environment and run the server.

1. Make sure you have Docker and Docker Compose installed.
2. Run the application:
   ```bash
   docker compose up --build
   ```

### Option 2: Local Python Environment

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

### View Application

Once the server is running (either via Docker or natively), access it at:
- Application home: [http://localhost:8000/](http://localhost:8000/)
- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Health check: [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)

## Project Structure

```text
├── app/
│   ├── api/v1/ endpoints/ # Versioned API Endpoints (users, auth, health)
│   ├── core/            # Global App Settings, Logging, Security 
│   ├── db/              # SQLAlchemy Database connecting and base
│   ├── middlewares/     # HTTP lifecycle interceptors (e.g. logging)
│   ├── models/          # Database Models mapping to SQL 
│   ├── schemas/         # Pydantic Schemas mapping API input/output
│   ├── services/        # Business Logic / LLM integrations
│   ├── main.py          # Application entry point binding routes and MW
│   ├── static/          # Legacy UI CSS, JS, Images
│   └── templates/       # Legacy UI Jinja2 HTML templates
├── scripts/             # Python automation and utility scripts
├── tests/               # Pytest suites
├── docker-compose.yml   # Multi-service setup (App, DB, Redis config)
├── Dockerfile           # App container instruction blueprint
├── .env                 # Local environment overrides
└── requirements.txt     # Python dependencies
```

## Future Iterations
After the initial setup, you can scale this structure to include modules for databases, models, schemas, middleware, auth, and testing without rewriting the core application footprint.
