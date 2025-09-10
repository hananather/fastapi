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
