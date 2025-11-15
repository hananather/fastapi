# Repository Guidelines

## Project Structure & Module Organization
- Root: `README.md` (quickstart, roadmap, links).
- Notes: `notes/` holds learning notes per chapter (e.g., `01-first-steps.md`).
- App code (when added): place under `app/` with entrypoint `app/main.py` exposing `app`. Tests live in `tests/` mirroring package layout.

## Build, Test, and Development Commands
- Environment setup:
  - `python -m venv .venv && source .venv/bin/activate`
  - `pip install "fastapi[standard]" uvicorn pytest httpx`
- Run local API (if `app/main.py` exists):
  - `uvicorn app.main:app --reload`
- Lint/format (recommended if code is added):
  - `ruff check .` and `black .` (configure in `pyproject.toml` if needed)

## Coding Style & Naming Conventions
- Python 3.x, PEP 8, 4‑space indentation, type hints required for public functions.
- Names: `snake_case` for modules/functions, `CamelCase` for classes, `UPPER_CASE` for constants.
- FastAPI: separate routers under `app/routers/`, schemas under `app/schemas/` (Pydantic models), services under `app/services/`.
- Keep functions small and focused; prefer explicit imports.

## Testing Guidelines
- Framework: `pytest` with `httpx` for request tests.
- Layout: `tests/` mirrors `app/` (e.g., `tests/routers/test_items.py`).
- Naming: files `test_*.py`; tests `test_*` functions.
- Run: `pytest -q` (add `-k` to filter). Aim for coverage on critical paths; use `anyio` for async tests when needed.

## Commit & Pull Request Guidelines
- Follow Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, optional scope (e.g., `docs(fastapi): ...`).
- Commits should be small and scoped; include rationale if behavior changes.
- PRs must include: concise description, linked issue or roadmap item, verification steps, and screenshots for docs when relevant. Keep diffs focused; update `README.md` or `Notes Index` when adding new notes.

## Security & Configuration Tips
- Do not commit secrets. Use `.env` (ignored) and provide `.env.example`.
- Prefer dependency injection for configs; validate settings with Pydantic models.
- Pin critical dependencies when introducing runtime code.

## Agent-Specific Instructions
- Keep edits minimal and in-scope; avoid renames without justification.
- When adding code, also add tests and update docs. Maintain the structure above.
