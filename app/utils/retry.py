# Retry utilities
import asyncio
from functools import wraps
from typing import Callable, Any


def async_retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry async functions"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        await asyncio.sleep(delay * (attempt + 1))
            raise last_exception
        return wrapper
    return decorator


def sync_retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry synchronous functions"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        import time
                        time.sleep(delay * (attempt + 1))
            raise last_exception
        return wrapper
    return decorator
