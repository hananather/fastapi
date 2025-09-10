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

## Roadmap (aligned to FastAPI Tutorial)

| Chapter | Topic | Code | Test | Doc |
|---|---|---|---|---|
| 1.1 | First Steps | ☐ | ☐ | ☐ |
| 1.2 | Path Parameters | ☐ | ☐ | ☐ |
| 1.3 | Query Parameters | ☐ | ☐ | ☐ |
| 1.4 | Request Body | ☐ | ☐ | ☐ |
| 1.5 | Query Params & String Validations | ☐ | ☐ | ☐ |
| 1.6 | Path Params & Numeric Validations | ☐ | ☐ | ☐ |
| 1.7 | Body – Multiple Parameters | ☐ | ☐ | ☐ |
| 1.8 | Body – Fields | ☐ | ☐ | ☐ |
| 1.9 | Body – Nested Models | ☐ | ☐ | ☐ |
| 1.10 | Body – Updates | ☐ | ☐ | ☐ |
| 1.11 | Schema Extra Example | ☐ | ☐ | ☐ |
| 1.12 | Extra Models | ☐ | ☐ | ☐ |
| 1.13 | Extra Data Types | ☐ | ☐ | ☐ |
| 1.14 | Cookie Parameters | ☐ | ☐ | ☐ |
| 1.15 | Header Parameters | ☐ | ☐ | ☐ |
| 1.16 | Query Param Models | ☐ | ☐ | ☐ |
| 1.17 | Header Param Models | ☐ | ☐ | ☐ |
| 1.18 | Cookie Param Models | ☐ | ☐ | ☐ |
| 1.19 | Request Forms | ☐ | ☐ | ☐ |
| 1.20 | Request Files | ☐ | ☐ | ☐ |
| 1.21 | Request Forms and Files | ☐ | ☐ | ☐ |
| 1.22 | Response Model | ☐ | ☐ | ☐ |
| 1.23 | Response Status Code | ☐ | ☐ | ☐ |
| 1.24 | JSON Compatible Encoder | ☐ | ☐ | ☐ |
| 1.25 | Handling Errors | ☐ | ☐ | ☐ |
| 1.26 | Path Operation Configuration | ☐ | ☐ | ☐ |
| 1.27 | Metadata & Docs URLs | ☐ | ☐ | ☐ |
| 2.1 | Dependencies (Intro) | ☐ | ☐ | ☐ |
| 2.2 | Classes as Dependencies | ☐ | ☐ | ☐ |
| 2.3 | Sub-dependencies | ☐ | ☐ | ☐ |
| 2.4 | Dependencies with yield | ☐ | ☐ | ☐ |
| 2.5 | Dependencies in Path Operation Decorators | ☐ | ☐ | ☐ |
| 2.6 | Global Dependencies | ☐ | ☐ | ☐ |
| 3.1 | Security (Intro) | ☐ | ☐ | ☐ |
| 3.2 | Security – First Steps | ☐ | ☐ | ☐ |
| 3.3 | Security – Simple OAuth2 | ☐ | ☐ | ☐ |
| 3.4 | Security – Get Current User | ☐ | ☐ | ☐ |
| 3.5 | Security – OAuth2 with JWT | ☐ | ☐ | ☐ |
| 4.1 | Middleware | ☐ | ☐ | ☐ |
| 4.2 | CORS | ☐ | ☐ | ☐ |
| 5.1 | SQL Databases | ☐ | ☐ | ☐ |
| 5.2 | Bigger Applications – Multiple Files | ☐ | ☐ | ☐ |
| 5.3 | Background Tasks | ☐ | ☐ | ☐ |
| 5.4 | Static Files | ☐ | ☐ | ☐ |
| 5.5 | Testing | ☐ | ☐ | ☐ |
| 5.6 | Debugging | ☐ | ☐ | ☐ |

## References

- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- SQLModel: https://sqlmodel.tiangolo.com/
- Alembic: https://alembic.sqlalchemy.org/
- OpenTelemetry: https://opentelemetry.io/
