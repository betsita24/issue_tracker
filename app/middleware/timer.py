import time
from fastapi import Request



async def timing_middleware_p(request: Request, call_next):
    start=time.perf_counter()
    response=await call_next(request)
    response.headers["X-Process-Time"]=f"{time.perf_counter() - start:.4f}s"
    return response