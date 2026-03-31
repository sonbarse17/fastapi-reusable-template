"""
Request Logger Middleware (request_logger.py)
=============================================
Middleware sits in the middle of all HTTP traffic. Before FastAPI even touches an endpoint,
it passes through here. We start a timer, `await call_next(request)` to let the router 
process the action, and then log exactly how long it took before returning it to the client.
"""

import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logging import logger

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        
        logger.info(
            f"Method: {request.method} - Path: {request.url.path} - "
            f"Status: {response.status_code} - Duration: {process_time:.4f}s"
        )
        return response
