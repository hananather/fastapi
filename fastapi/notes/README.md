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

## Notes Index

- 01 — First Steps: 01-first-steps.md
- 02 — Path Parameters: 02-path-parameters.md
- 03 — Query Parameters: 03-query-parameters.md
- 04 — Request Body: 04-request-body.md
- 05 — Query Params & String Validations: 05-query-params-and-string-validations.md
- 06 — Path Params & Numeric Validations: 06-path-params-and-numeric-validations.md
- 07 — Body – Multiple Parameters: 07-body-multiple-parameters.md
- 08 — Body – Fields: 08-body-fields.md
- 09 — Body – Nested Models: 09-body-nested-models.md
- 10 — Body – Updates: 10-body-updates.md
- 11 — Schema Extra Example: 11-schema-extra-example.md
- 12 — Extra Models: 12-extra-models.md
- 13 — Extra Data Types: 13-extra-data-types.md
- 14 — Cookie Parameters: 14-cookie-parameters.md
- 15 — Header Parameters: 15-header-parameters.md
- 16 — Query Param Models: 16-query-param-models.md
- 17 — Header Param Models: 17-header-param-models.md
- 18 — Cookie Param Models: 18-cookie-param-models.md
- 19 — Request Forms: 19-request-forms.md
- 20 — Request Files: 20-request-files.md
- 21 — Request Forms and Files: 21-request-forms-and-files.md
- 22 — Response Model: 22-response-model.md
- 23 — Response Status Code: 23-response-status-code.md
- 24 — JSON Compatible Encoder: 24-json-compatible-encoder.md
- 25 — Handling Errors: 25-handling-errors.md
- 26 — Path Operation Configuration: 26-path-operation-configuration.md
- 27 — Metadata & Docs URLs: 27-metadata-and-docs-urls.md
- 28 — Dependencies (Intro): 28-dependencies-intro.md
- 29 — Classes as Dependencies: 29-classes-as-dependencies.md
- 30 — Sub-dependencies: 30-sub-dependencies.md
- 31 — Dependencies with yield: 31-dependencies-with-yield.md
- 32 — Dependencies in Path Operation Decorators: 32-dependencies-in-path-operation-decorators.md
- 33 — Global Dependencies: 33-global-dependencies.md
- 34 — Security (Intro): 34-security-intro.md
- 35 — Security – First Steps: 35-security-first-steps.md
- 36 — Security – Simple OAuth2: 36-security-simple-oauth2.md
- 37 — Security – Get Current User: 37-security-get-current-user.md
- 38 — Security – OAuth2 with JWT: 38-security-oauth2-with-jwt.md
- 39 — Middleware: 39-middleware.md
- 40 — CORS: 40-cors.md
- 41 — SQL Databases: 41-sql-databases.md
- 42 — Bigger Applications – Multiple Files: 42-bigger-applications-multiple-files.md
- 43 — Background Tasks: 43-background-tasks.md
- 44 — Static Files: 44-static-files.md
- 45 — Testing: 45-testing.md
- 46 — Debugging: 46-debugging.md

## Roadmap (aligned to FastAPI Tutorial)

| Chapter | Topic | Code | Test | Doc |
|---|---|---|---|---|
| 1.1 | [First Steps](01-first-steps.md) | ☐ | ☐ | ☐ |
| 1.2 | [Path Parameters](02-path-parameters.md) | ☐ | ☐ | ☐ |
| 1.3 | [Query Parameters](03-query-parameters.md) | ☐ | ☐ | ☐ |
| 1.4 | [Request Body](04-request-body.md) | ☐ | ☐ | ☐ |
| 1.5 | [Query Params & String Validations](05-query-params-and-string-validations.md) | ☐ | ☐ | ☐ |
| 1.6 | [Path Params & Numeric Validations](06-path-params-and-numeric-validations.md) | ☐ | ☐ | ☐ |
| 1.7 | [Body – Multiple Parameters](07-body-multiple-parameters.md) | ☐ | ☐ | ☐ |
| 1.8 | [Body – Fields](08-body-fields.md) | ☐ | ☐ | ☐ |
| 1.9 | [Body – Nested Models](09-body-nested-models.md) | ☐ | ☐ | ☐ |
| 1.10 | [Body – Updates](10-body-updates.md) | ☐ | ☐ | ☐ |
| 1.11 | [Schema Extra Example](11-schema-extra-example.md) | ☐ | ☐ | ☐ |
| 1.12 | [Extra Models](12-extra-models.md) | ☐ | ☐ | ☐ |
| 1.13 | [Extra Data Types](13-extra-data-types.md) | ☐ | ☐ | ☐ |
| 1.14 | [Cookie Parameters](14-cookie-parameters.md) | ☐ | ☐ | ☐ |
| 1.15 | [Header Parameters](15-header-parameters.md) | ☐ | ☐ | ☐ |
| 1.16 | [Query Param Models](16-query-param-models.md) | ☐ | ☐ | ☐ |
| 1.17 | [Header Param Models](17-header-param-models.md) | ☐ | ☐ | ☐ |
| 1.18 | [Cookie Param Models](18-cookie-param-models.md) | ☐ | ☐ | ☐ |
| 1.19 | [Request Forms](19-request-forms.md) | ☐ | ☐ | ☐ |
| 1.20 | [Request Files](20-request-files.md) | ☐ | ☐ | ☐ |
| 1.21 | [Request Forms and Files](21-request-forms-and-files.md) | ☐ | ☐ | ☐ |
| 1.22 | [Response Model](22-response-model.md) | ☐ | ☐ | ☐ |
| 1.23 | [Response Status Code](23-response-status-code.md) | ☐ | ☐ | ☐ |
| 1.24 | [JSON Compatible Encoder](24-json-compatible-encoder.md) | ☐ | ☐ | ☐ |
| 1.25 | [Handling Errors](25-handling-errors.md) | ☐ | ☐ | ☐ |
| 1.26 | [Path Operation Configuration](26-path-operation-configuration.md) | ☐ | ☐ | ☐ |
| 1.27 | [Metadata & Docs URLs](27-metadata-and-docs-urls.md) | ☐ | ☐ | ☐ |
| 2.1 | [Dependencies (Intro)](28-dependencies-intro.md) | ☐ | ☐ | ☐ |
| 2.2 | [Classes as Dependencies](29-classes-as-dependencies.md) | ☐ | ☐ | ☐ |
| 2.3 | [Sub-dependencies](30-sub-dependencies.md) | ☐ | ☐ | ☐ |
| 2.4 | [Dependencies with yield](31-dependencies-with-yield.md) | ☐ | ☐ | ☐ |
| 2.5 | [Dependencies in Path Operation Decorators](32-dependencies-in-path-operation-decorators.md) | ☐ | ☐ | ☐ |
| 2.6 | [Global Dependencies](33-global-dependencies.md) | ☐ | ☐ | ☐ |
| 3.1 | [Security (Intro)](34-security-intro.md) | ☐ | ☐ | ☐ |
| 3.2 | [Security – First Steps](35-security-first-steps.md) | ☐ | ☐ | ☐ |
| 3.3 | [Security – Simple OAuth2](36-security-simple-oauth2.md) | ☐ | ☐ | ☐ |
| 3.4 | [Security – Get Current User](37-security-get-current-user.md) | ☐ | ☐ | ☐ |
| 3.5 | [Security – OAuth2 with JWT](38-security-oauth2-with-jwt.md) | ☐ | ☐ | ☐ |
| 4.1 | [Middleware](39-middleware.md) | ☐ | ☐ | ☐ |
| 4.2 | [CORS](40-cors.md) | ☐ | ☐ | ☐ |
| 5.1 | [SQL Databases](41-sql-databases.md) | ☐ | ☐ | ☐ |
| 5.2 | [Bigger Applications – Multiple Files](42-bigger-applications-multiple-files.md) | ☐ | ☐ | ☐ |
| 5.3 | [Background Tasks](43-background-tasks.md) | ☐ | ☐ | ☐ |
| 5.4 | [Static Files](44-static-files.md) | ☐ | ☐ | ☐ |
| 5.5 | [Testing](45-testing.md) | ☐ | ☐ | ☐ |
| 5.6 | [Debugging](46-debugging.md) | ☐ | ☐ | ☐ |

## References

- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- SQLModel: https://sqlmodel.tiangolo.com/
- Alembic: https://alembic.sqlalchemy.org/
- OpenTelemetry: https://opentelemetry.io/
