# Query Parameters

- Query parameters are automatically detected: Any function parameter that is not a path parameter is interpreted as a query parameter.
- Type validation and conversion When you declare a function parameter with a type (like `int` or `bool`), FastAPI converts and validates the query parameter value to that Python type.
- To declare completely optional parameters, set their default to `None` (e.g., `q: str | None = None`). FastAPI will treat these as not required.
- Required query parameter: If you don’t provide a default value, the query parameter becomes required (e.g., `needy: str`).
- Type conversions are flexible: FastAPI can convert various representations (like `short=true`, `short=yes`, `short=on`, etc.) into corresponding Boolean values.
- Mixing types: You can define endpoints that use both path and query parameters in any order, and FastAPI will distinguish between them by name.
- Multiple parameters: Some parameters can be required, some optional (with default value), and some entirely optional (default `None`) all in the same endpoint.

Clear way to think about **query parameters vs. path parameters** in FastAPI:

- **Path parameters** are for locating a specific resource—use them as part of the URL path, like `/users/123` (where `123` is the user’s ID).
  *Think: “Which specific thing am I accessing?”*

- **Query parameters** are for filtering, searching, or modifying the result of a resource—use them after a `?`, like `/users?active=true&sort=name`.
  *Think: “How do I want to view or adjust the list or result?”*

**Table Comparison:**

| Criteria         | Path Parameters       | Query Parameters                 |
|------------------|----------------------|----------------------------------|
| Example URL      | `/items/45`          | `/items?type=book&sort=price`    |
| Purpose          | Identify one resource| Filter, search, or tweak output  |
| Data Location    | In the URL path      | After `?`, as key-value pairs    |
| Required?        | Usually required     | Usually optional                 |
| Use Case         | `/users/{user_id}`   | `/users?role=admin&active=true`  |

**In summary:**
- Use **path parameters** for the “thing” you want,
- Use **query parameters** for “how” you want (filter, sort, paginate, etc.).

## Example

In a simple chat application built with FastAPI, **query parameters** are useful for filtering, searching, or customizing what data you return from your API endpoints. Here’s how you might use them:

- **Fetching chat history:**
  You could provide query parameters like `user`, `limit`, `before`, or `after` to control what messages are returned. For example:
  ```python
  @app.get("/messages/")
  async def get_messages(user: str | None = None, limit: int = 20, before: str | None = None):
      # Return up to 'limit' messages, filter by user or time if provided
      pass
  ```
  Example usage:
  `/messages/?user=alice&limit=10` — gets the latest 10 messages from user "alice".

- **Searching messages:**
  If you wanted to search for messages containing a word:
  ```python
  @app.get("/messages/search")
  async def search_messages(q: str):
      # Find messages where text contains 'q'
      pass
  ```
  Example usage:
  `/messages/search?q=hello` — returns all messages containing "hello".

- **Customizing responses:**
  Allowing clients to request messages in a "short" or "long" format:
  ```python
  @app.get("/messages/")
  async def get_messages(short: bool = False):
      # If short=True, only return message IDs and timestamps
      pass
  ```
  `/messages/?short=true` — returns a simplified version of messages.

- **Pagination:**
  Use `skip` and `limit` query parameters (as shown in FastAPI docs) to allow the client to page through messages.

---

In FastAPI there are **two main types of parameters** used in routes:

1. **Path Parameters**
   - These are parts of the URL path itself.
   - Defined directly in the route, e.g. `/items/{item_id}`.
   - Used to uniquely identify a resource.
   - Example:
     ```python
     @app.get("/items/{item_id}")
     def read_item(item_id: int):
         return {"item_id": item_id}
     ```

2. **Query Parameters**
   - These come after the `?` in the URL.
   - Used for filtering, searching, or optional criteria.
   - Defined as function arguments that are not part of the path.
   - Example:
     ```python
     @app.get("/items/")
     def read_items(q: str = None):
         return {"q": q}
     ```
   - Called like: `/items/?q=foo`

**Summary Table:**

| Type            | Example URL                | Purpose                                | FastAPI Syntax      |
|-----------------|---------------------------|----------------------------------------|---------------------|
| Path Parameter  | `/items/123`              | Identify a specific resource           | `/items/{item_id}`  |
| Query Parameter | `/items/?q=foo&page=2`    | Filter, search, or refine the request  | `q: str = None`     |


- **Path** parameters: part of the route.
- **Query** parameters: used for filtering or optional arguments.
