**`Annotated`** is a special Python type (introduced in [PEP 593](https://peps.python.org/pep-0593/)) that allows you to attach metadata to type hints. In the context of FastAPI, it's commonly used like this:

```python
from typing import Annotated
from fastapi import Query

q: Annotated[str | None, Query(max_length=50)]
```

**What does this do?**
- `Annotated` takes a type (e.g., `str | None`) and lets you **add extra metadata**, such as FastAPI's `Query` validation constraints.
- FastAPI then reads this metadata to generate documentation, perform validation, and add features like descriptions, titles, and more.
