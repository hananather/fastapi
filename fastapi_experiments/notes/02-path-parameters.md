
## FastAPI Path Parameters

**Core Concepts**

- **Path Parameters** allow your API endpoints to accept dynamic segments (e.g., `/books/{book_id}`).
  - Enables flexible endpoints to handle many resources.
  - Type annotations (e.g., `int`, `str`) provide automatic validation and conversion.
- **How do users know what ID to use?**
  - Provide a “list” endpoint (e.g., `/books`) that returns available items with their IDs.
- **Restricting Allowed Values:**
  - Use Python `Enum` for path parameters to limit values to a fixed set.
  - FastAPI validates and auto-documents these allowable choices.
- **Path Convertor (`:path`):**
  - Lets you capture full sub-paths, not just single segments (e.g., `/files/{file_path:path}`).
  - Useful for files, nested resources, or folders—not just for file-serving.
- **RESTful Patterns:**
  - List endpoint: `/resources` (browse/search all)
  - Detail endpoint: `/resources/{id}` (fetch one item)
- **Validation & Documentation:**
  - Type hints and Enums improve error messages and generate interactive docs automatically.

***

**Quick Self-Quiz:**

- How do you make endpoint URLs dynamic and reusable in FastAPI?
- How can users or clients discover which path parameter values to use?
- How do you restrict a path parameter to only some specific allowed values?
- In what scenarios is the `:path` convertor indispensable?
- Why is a “list-detail” pattern standard in REST APIs?

***

- **How do you make endpoint URLs dynamic and reusable in FastAPI?**
  By using path parameters like `{item_id}` in your route definitions, you enable dynamic URLs that accept varying input values.

- **How can users or clients discover which path parameter values to use?**
  Provide a list endpoint (e.g., `/items`) that returns available resources and their IDs for discovery.

- **How do you restrict a path parameter to only some specific allowed values?**
  Declare the parameter as an Enum type so FastAPI only accepts predefined values and rejects others.

- **In what scenarios is the `:path` convertor indispensable?**
  Use the `:path` convertor to capture arbitrarily nested sub-paths—including slashes—whenever you need multi-segment resource paths.

- **Why is a “list-detail” pattern standard in REST APIs?**
  Because it cleanly separates resource discovery (list) from detailed retrieval (detail), making APIs intuitive and scalable.

[1](https://fastapi.tiangolo.com/tutorial/path-params/#return-enumeration-members)

**If you need more detail:**

[1](https://fastapi.tiangolo.com/tutorial/path-params/#path-convertor)
