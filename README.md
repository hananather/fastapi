# FastAPI — Concepts & Roadmap

A concise, concept-first guide and tracker for building a robust FastAPI service. This README stays minimal: quickstart + topics we’ll cover, with status you can update as you go.

Legend: ✅ done · 🚧 in progress · ☐ planned

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install "fastapi[standard]" uvicorn pytest httpx

# Replace `app.main:app` with your module if different
uvicorn app.main:app --reload
```

OpenAPI docs: http://127.0.0.1:8000/docs

## Concepts Checklist

### 1. Basics
- ☐ Project layout & settings (Pydantic Settings)
- ☐ Routing: path, query, body params
- ☐ Pydantic models & validation
- ☐ Response models & status codes
- ☐ Dependency Injection (Depends)
- ☐ Error handling & custom exceptions
- ☐ Async best practices (I/O vs CPU)
- ☐ Testing: pytest + httpx

### 2. Data & Auth
- ☐ Database setup (SQLModel/SQLAlchemy)
- ☐ Alembic migrations
- ☐ CRUD patterns & transactions
- ☐ Auth: OAuth2 Password Flow + JWT
- ☐ CORS & rate limiting
- ☐ Background tasks & job queues
- ☐ Caching with Redis

### 3. APIs & Realtime
- ☐ OpenAPI customization (tags, examples, metadata)
- ☐ API versioning & deprecations
- ☐ Pagination, filtering, sorting
- ☐ File uploads & static files
- ☐ WebSockets & streaming responses (SSE)

### 4. Observability
- ☐ Structured logging
- ☐ Metrics (Prometheus/OpenTelemetry)
- ☐ Tracing (OpenTelemetry)
- ☐ Health, readiness, liveness probes

### 5. Performance & Security
- ☐ Performance tuning (uvicorn/gunicorn workers, uvloop)
- ☐ Concurrency (async DB, connection pooling)
- ☐ Profiling (CPU, memory)
- ☐ Security headers (CSP, HSTS), input hardening

### 6. Delivery
- ☐ Docker image & multi-stage build
- ☐ Production server (gunicorn + uvicorn workers)
- ☐ Reverse proxy (Nginx/Caddy) basics
- ☐ CI/CD (lint, test, build, release)

## Roadmap (Code · Test · Doc)

| Chapter | Topic | Code | Test | Doc |
|---|---|---|---|---|
| 1.1 | Routing: path/query/body | ☐ | ☐ | ☐ |
| 1.2 | Pydantic models & validation | ☐ | ☐ | ☐ |
| 1.3 | Response models & status | ☐ | ☐ | ☐ |
| 1.4 | Dependency Injection | ☐ | ☐ | ☐ |
| 1.5 | Error handling & exceptions | ☐ | ☐ | ☐ |
| 1.6 | Settings & config | ☐ | ☐ | ☐ |
| 1.7 | Testing (pytest + httpx) | ☐ | ☐ | ☐ |
| 2.1 | DB setup (SQLModel/SQLAlchemy) | ☐ | ☐ | ☐ |
| 2.2 | Alembic migrations | ☐ | ☐ | ☐ |
| 2.3 | CRUD & transactions | ☐ | ☐ | ☐ |
| 2.4 | Auth (OAuth2 + JWT) | ☐ | ☐ | ☐ |
| 2.5 | CORS & rate limiting | ☐ | ☐ | ☐ |
| 2.6 | Background tasks & queues | ☐ | ☐ | ☐ |
| 2.7 | Caching (Redis) | ☐ | ☐ | ☐ |
| 3.1 | OpenAPI customization | ☐ | ☐ | ☐ |
| 3.2 | API versioning | ☐ | ☐ | ☐ |
| 3.3 | Pagination & filtering | ☐ | ☐ | ☐ |
| 3.4 | File uploads & static | ☐ | ☐ | ☐ |
| 3.5 | WebSockets & streaming | ☐ | ☐ | ☐ |
| 4.1 | Logging & metrics | ☐ | ☐ | ☐ |
| 4.2 | Tracing & profiling | ☐ | ☐ | ☐ |
| 4.3 | Health/readiness/liveness | ☐ | ☐ | ☐ |
| 5.1 | Performance tuning | ☐ | ☐ | ☐ |
| 5.2 | Concurrency & pooling | ☐ | ☐ | ☐ |
| 5.3 | Security hardening | ☐ | ☐ | ☐ |
| 6.1 | Docker image | ☐ | ☐ | ☐ |
| 6.2 | Gunicorn + uvicorn workers | ☐ | ☐ | ☐ |
| 6.3 | Reverse proxy basics | ☐ | ☐ | ☐ |
| 6.4 | CI/CD pipeline | ☐ | ☐ | ☐ |

## References

- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- SQLModel: https://sqlmodel.tiangolo.com/
- Alembic: https://alembic.sqlalchemy.org/
- OpenTelemetry: https://opentelemetry.io/
