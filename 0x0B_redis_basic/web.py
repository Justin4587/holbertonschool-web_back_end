#!/usr/bin/env python3
"""something about redis"""
import redis
from functools import wraps
import requests
from typing import Callable

_redis = redis.Redis()


def get_page_count(method: Callable) -> Callable:
    """something about redis"""
    print("hello")

    @wraps(method)
    def wrapper(url):
        print(f"this is from args {url}")
        key = _redis.incr(f"count:{url}")
        cached = _redis.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')
        else:
            _redis.setex(f"cached:{url}", 10, key)
            
            return

    return wrapper


@get_page_count
def get_page(url: str) -> str:
    """something about redis"""
    print("hello before .get(url)")
    req = requests.get(url)
    print("hello after .get(url)")
    print(f"this the req.text {req.text}")
    return req.text
