# FastAPI MongoDB Project

A modern FastAPI application with MongoDB integration, using UV for dependency management.

## Prerequisites

- Python 3.13 or higher
- UV package manager
- MongoDB instance (local or cloud)

## Project Structure

```
fastapi-mongo-db/
├── config/         # Configuration files
├── models/         # Database models
├── routes/         # API routes
├── schema/         # Pydantic schemas
├── main.py         # Application entry point
├── pyproject.toml  # Project dependencies
└── .env           # Environment variables
```

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/jameskanyiri/fastapi-mongo-db.git
cd fastapi-mongo-db
```

2. Create and activate virtual environment using UV:

```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
uv pip install -e .
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your MongoDB connection string and other configurations
```

5. Run the application:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:

- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Dependencies

- FastAPI with standard extras
- PyMongo with SRV support
- UV for dependency management

## Development

This project uses UV for dependency management and virtual environment handling. The main dependencies are managed in `pyproject.toml`.

