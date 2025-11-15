# Async Routes
FastAPI is an async framework. It's designed to work with async I/O operations, and that's the reason why it's so fast.

However, FastAPI doesn't restrict you to only use async routes.
The developer can use sync routes as well.
**They are not the same**

- FastAPI runs `sync` routes in the threadpool, so blocking I/O operations won't stop the event loop from executing other tasks.
- If the route is `async`, then it's always called via `await`, and FastAPI trusts you to use only non-blocking I/O operations.

## I/O intensive tasks
```python
import asyncio
import time

from fastapi import APIRouter


router = APIRouter()


@router.get("/terrible-ping")
async def terrible_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds, the whole process will be blocked
    
    return {"pong": True}

@router.get("/good-ping")
def good_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds, but in a separate thread for the whole `good_ping` route

    return {"pong": True}

@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(10) # non-blocking I/O operation

    return {"pong": True}
```


1.  `GET /terrible-ping`
   1. FastAPI server recieves a request and starts handling it
   2. Sever's event loop and all the tasks in the queue will be waiting until `time.sleep()` is finsihed
      - Server thinks `time.sleep()` is not an I/O task, so it waits until its finished. 
      - server won't accept any new requests while its waiting
   3. Server returns the response.
      1. After a response is returned, server starts accepting new requests.

2. `GET /good-ping`
   1. FastAPI server recieves a request and starting handling it
   2. FastAPI sends the whole route `good_ping` to the threadpool, where a worker will run the function.
   3. While `good_ping` is being executed, event loop selects next task from the queue and works on them (e.g., accept new request, call db)
      - independenlty of the main thread (i.e., our FastAPI server), the worker thread will be waiting for `time.sleep()` to finish.
      - Sync operations only block the side thread, not the main one
   4. When `good_ping` finishes its work, server returns a response to the client. 

3. `GET /perfect-ping`
   1. FastAPI server receives a request and starts handling it
   2. FastAPI awaits `asyncio.sleep()
   3. Event loop selects next task from the queue and works on them (e.g., accept new request, call db)
   4. When `asyncio.sleep()` finishes, server finishes the execution of route and returns a response to the client. 



>[!WARNING]
>Notes on thread pool:
> - There's  performance penatly when you use non async functions in Pythons. Threads require more resources than coroutines, so they are not as cheap as async I/O operations. The  penatly comes from the fact that FastAPI will call [`run_in_pool`](https://github.com/Kludex/starlette/blob/9f16bf5c25e126200701f6e04330864f4a91a898/starlette/concurrency.py#L36-L42), which will run the funtion using a thread pool using [`anyio.to_thread.run_sync`](https://anyio.readthedocs.io/en/stable/threads.html#running-a-function-in-a-worker-thread)
> - There are only about 40 threads in the thread pool. If you use all of them, your app will be blocked. 

To change the number of threads, you can use the folowing code:
```python
import anyio
from contextlib import asynccontextmanager
from typing import Iterator

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> Iterator[None]:
    limiter = anyio.to_thread.current_default_thread_limiter()
    limiter.total_tokens = 100
    yield

app = FastAPI(lifespan=lifespan)
```

## CPU intensive tasks
Operations that are non-blocking awaitables or sent to the thread pool must be I/O intensive tasks (e.g. open file, db call, external API call)

- Awaiting CPU-intensive tasks (e.g., heavy calculations, data processing, video transcoding) is worthless since the CPU has to work to finish the task, while I/O operations are external and server does nothing while waiting for that operation to finish, thus it can go to the next tasks.
- Running CPU-intensive in in other threads also isn't effective, because of GIL. In short, GIL allows only one thread to work at a time. 
- If you want to optimize CPU intensive tasks you should send them to to workers in another process. [Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/#technical-details)


## Is there any benefit to using blocking (sync) libraries over async ones?

1. Simplicity of mental model

   Sync code is:

   ```python
   data = requests.get(url).json()
   save_to_db(data)
   ```
   For many small services or scripts, this is *way* easier to read, write, and debug.

2. Maturity and ecosystem

   Historically:

   * `requests` existed long before `httpx`/`aiohttp`.
   * `psycopg2` existed long before `asyncpg` or the async side of `psycopg3`.
   * Many SDKs for third-party APIs are still sync-only.

   That often means:

   * More docs, tutorials, StackOverflow answers
   * Longer battle-testing
   * Fewer edge-case bugs

3. You’re not actually chasing high concurrency

   If your service:

   * Handles low traffic
   * Mostly does quick DB calls and finishes
   * Runs behind a process manager (e.g. multiple Gunicorn/Uvicorn workers)

   then the scalability benefits of async might not be worth the extra complexity. A “boring” sync stack can be totally fine.



4. FastAPI already hides some pain with threads

   In FastAPI specifically, sync routes:

   ```python
   @router.get("/good-ping")
   def good_ping():
       time.sleep(10)
       return {"pong": True}
   ```

   are run in a **thread pool**, so they don’t block the main event loop. For moderate loads and reasonable latency, that’s often “good enough”.

   The trade-offs: threads cost more memory and you have a limited pool, but it’s a valid design.

## How to decide which to use (practically, in your FastAPI world)

You can think in terms of “what kind of work am I doing?” and “what kind of load do I expect?”

### Use async libraries when:

* You’re building an API that:

  * makes a lot of HTTP calls to other services, **or**
  * does lots of DB I/O, **or**
  * needs to handle many concurrent users without tons of threads.
* You’re comfortable with `async`/`await` and event loop concepts.
* The async client is reasonably mature (no huge missing features from the sync version).

Then your FastAPI routes are typically:

```python
@router.get("/something")
async def handler():
    user = await async_db.get_user(...)
    data = await async_http.get(...)
    return ...
```


**References:**
- [FastAPI Tips — Be careful with non-async functions (Kludex)](https://github.com/Kludex/fastapi-tips?tab=readme-ov-file#2-be-careful-with-non-async-functions)
- [FastAPI Best Practices (zhanymkanov)](https://github.com/zhanymkanov/fastapi-best-practices)
