# 2025‑09‑06 — fastapi-first-steps

### Q: What does `app = FastAPI()` actually set up?

**Simple:** It creates your web application object.
**Precise:** Instantiates a Starlette‑based **ASGI** app that holds routes, middleware, and metadata; servers like Uvicorn call it to handle HTTP requests.
**In code (server):**

```python
from fastapi import FastAPI

# Server: create the ASGI application (Starlette-based)
app = FastAPI()

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello World"}
```

### Q: What is a “path” in FastAPI?

**Simple:** The URL part after the domain (always starts with `/`).
**Precise:** A path identifies a resource/concern; the app maps requests by path plus method. Client: sends `GET /items/`; Server: matches the `/items/` route and runs its handler.
**In code (server):**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")                   # path is "/"
def home() -> dict[str, str]:
    return {"ok": "home"}

@app.get("/items/")             # path is "/items/"
def list_items() -> list[dict[str, str]]:
    return [{"id": "A1"}]
```

### Q: What is an “operation”?

**Simple:** The HTTP method (GET/POST/PUT/DELETE/…) used on a path.
**Precise:** In OpenAPI, an **operation** is a unique `(method, path)` entry with its params and responses (e.g., **GET /items/**). Semantics like “GET reads, POST creates” are conventions—not enforced by FastAPI—but following them keeps your API predictable.
**In code (server):**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")             # operation: GET /items/
def read_items() -> list[dict]:
    return []

@app.post("/items/")            # operation: POST /items/
def create_item() -> dict[str, bool]:
    return {"created": True}
```

### Q: What does a *path operation decorator* do?

**Simple:** It ties a function to a URL and method.
**Precise:** The decorator registers the handler and metadata on the app; FastAPI uses this to build routing tables and your OpenAPI document (which then powers `/docs` and `/redoc`).
**In code (server):**

```python
from fastapi import FastAPI

app = FastAPI()

# Maps (GET, "/") -> homepage. Function name is arbitrary.
@app.get("/")
def homepage() -> dict[str, str]:
    return {"message": "hi"}
```

### Q: What is the *path operation function*?

**Simple:** The Python function that runs for a matched request.
**Precise:** A callable invoked per request; may be `async def` or `def`. It returns JSON‑compatible data that FastAPI serializes into the HTTP response.
**In code (server):**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict[str, str]:  # async allows concurrent I/O later
    return {"message": "Hello World"}

@app.get("/non-async")
def non_async() -> dict[str, str]:   # sync works too
    return {"note": "sync handler"}
```

### Q: What can a handler return?

**Simple:** A dict, list, or simple value (str/int/bool), and FastAPI will JSON‑encode it.
**Precise:** Return JSON‑serializable objects; otherwise supply a model/encoder. (You’ll use Pydantic models later for typed schemas.)
**In code (server):**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/as-dict")
def as_dict() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/as-list")
def as_list() -> list[int]:
    return [1, 2, 3]

@app.get("/as-scalar")
def as_scalar() -> int:
    return 42
```

### Q: What are the interactive docs (`/docs` and `/redoc`) and why do they matter?

**Simple:** Auto‑generated UIs to explore and call your API.
**Precise:** Swagger UI (`/docs`) and ReDoc (`/redoc`) are driven by your OpenAPI schema. Client: they’re a built‑in HTTP client and shape viewer. Server: they reflect exactly what you declared (paths/ops/schemas), acting as a quick contract/validation surface.
**In code (server):**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/echo")
def echo() -> dict[str, str]:
    return {"echo": "try this in /docs or /redoc"}
# Run locally: `fastapi dev` then open http://127.0.0.1:8000/docs
```

### Q: What is the OpenAPI “schema” here?

**Simple:** A JSON document (`/openapi.json`) describing your API.
**Precise:** FastAPI emits OpenAPI (e.g., 3.1) that enumerates paths, operations, parameters, status codes, and links to JSON Schemas for your data. Tools (docs, code‑gen, testing) consume this contract.
**In code (server):**

```python
from fastapi import FastAPI

app = FastAPI()  # Visit /openapi.json to see the generated API schema

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello World"}
```

### Q: How do I run and check the server locally?

**Simple:** Start the dev server and open the URLs it prints.
**Precise:** Use `fastapi dev` (Uvicorn under the hood) → open `http://127.0.0.1:8000/` (JSON), `/docs` (Swagger UI), `/redoc` (ReDoc), and `/openapi.json` (schema).
**In code (server):**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello World"}
# Terminal: fastapi dev
# Browser:  http://127.0.0.1:8000  /docs  /redoc  /openapi.json
```
